import logging
import contextlib
import os
import socket
import subprocess
import time
import threading
import cv2 as cv
import numpy as np


from droneapp.models.base import Singleton
#https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
#https://github.com/dji-sdk/Tello-Python/blob/master/Tello_Video/install/Windows/install.bat

logger = logging.getLogger(__name__)
#1 feet = 30.48 centimeters
DEFAULT_DISTANCE = 0.30
DEFAULT_SPEED = 10
DEFAULT_DEGREE = 10 # rotalama sağa sola dönme konusu

FRAME_X = int(960/3)
FRAME_Y = int(720/3)
FRAME_AREA = FRAME_X * FRAME_Y

FRAME_SIZE = FRAME_AREA * 3
FRAME_CENTER_X = FRAME_X / 2
FRAME_CENTER_y = FRAME_Y / 2

CMD_FFMPEG = (f'ffmpeg -hwaccel auto -hwaccel_device opencl -i pipe:0 '
                f'-pix_fmt bgr24 -s {FRAME_X}x{FRAME_Y} -f rawvideo pipe:1')


#class DroneManager(object):
class DroneManager(metaclass=Singleton):
    def __init__(self, host_ip='192.168.10.2',host_port=8889,
                    drone_ip='192.168.10.1',drone_port=8889,
                    is_imperial=False, speed=DEFAULT_SPEED):
        self.host_ip=host_ip
        self.host_port=host_port
        self.drone_ip=drone_ip
        self.drone_port=drone_port
        self.drone_address=(drone_ip,drone_port)
        self.is_imperial = is_imperial
        self.speed = speed
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.bind((self.host_ip,self.host_port))
        # self.socket.sendto(b'command',self.drone_address)
        # self.socket.sendto(b'streamon',self.drone_address)
        self.response=None
        self.stop_event = threading.Event()
        self._response_thread = threading.Thread(target=self.receive_response,
                                            args=(self.stop_event,))
        
        self._response_thread.start()

        self.proc = subprocess.Popen(CMD_FFMPEG.split(' '),
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)

        self.proc_stdin = self.proc.stdin
        self.proc_stdout = self.proc.stdout

        self.video_port = 11111

        self._receive_video_thread = threading.Thread(
            target=self.receive_video,
            args=(self.stop_event, self.proc_stdin,
                  self.host_ip, self.video_port,))
        self._receive_video_thread.start()

        self.send_command('command')
        self.send_command('streamon')
        self.set_speed(self.speed)
    
    def receive_response(self, stop_event):
        while not stop_event.is_set():
            try:
                self.response, ip = self.socket.recvfrom(3000)
                logger.info({'action':'receive_response','response': self.response})
            except socket.error as ex:
                logger.error({'action': 'receive_response','ex':ex})
                break
    
    def __dell_(self):
        self.stop()

    def stop(self):
        self.stop_event.set()
        retry = 0
        while self._response_thread.isAlive():
            time.sleep(0.3)
            if retry > 30:
                break
            retry += 1
        self.socket.close()
        os.kill(self.proc.pid,9)
        #windows
        #import signal
        #os.kill(self.proc.pid, signal.CTRL_C_EVENT)
    def send_command(self,command):
        logger.info({'action':'send_command','command':command})
        self.socket.sendto(command.encode('utf-8'),self.drone_address)
        retry = 0
        while self.response is None:
            time.sleep(0.3)
            if retry > 3:
                break
            retry += 1
        if self.response is None:
            response = None
        else:
            response=self.response.decode('utf-8')
        self.response =None
        return response

    def takeoff(self):
        return self.send_command('takeoff')

    def land(self):
        return self.send_command('land')
    
    def move(self,direction,distance):
        distance=float(distance)
        if self.is_imperial:
            distance=int(round(distance*30.48)) # 1cm
        else:
            distance = int(round(distance*100))
        return self.send_command(f'{direction} {distance}')
    
    def up(self,distance=DEFAULT_DISTANCE):
        return self.move('up',distance)
    def down(self,distance=DEFAULT_DISTANCE):
        return self.move('down',distance)
    def left(self,distance=DEFAULT_DISTANCE):
        return self.move('left',distance)
    def right(self,distance=DEFAULT_DISTANCE):
        return self.move('right',distance)
    def forward(self,distance=DEFAULT_DISTANCE):
        return self.move('forward',distance)
    def back(self,distance=DEFAULT_DISTANCE):
        return self.move('back',distance)
    def set_speed(self, speed):
        return self.send_command(f'speed {speed}')
    def clockwise(self, degree=DEFAULT_DEGREE): # saat yönünde
        return self.send_command(f'cw {degree}')
    def counter_clockwise(self, degree=DEFAULT_DEGREE): # saat yönün tersine
        return self.send_command(f'cw {degree}')
    def flip_front(self): # öne takla at fonksiyonu
        return self.send_command('flip f')
    def flip_back(self): # getiye takla at metodu
        return self.send_command('flip b')
    def flip_left(self):
        return self.send_command('flip l')
    def flip_right(self):
        return self.send_command('flip r')
    
    def receive_video(self, stop_event, pipe_in, host_ip, video_port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_video:
            sock_video.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            sock_video.settimeout(.5)
            sock_video.bind((host_ip, video_port))
            data = bytearray(2048)
            while not stop_event.is_set():
                try:
                    size, addr = sock_video.recvfrom_into(data)
                    #logger.info({'action':'receive_video','data':data})
                except socket.timeout as ex:
                    logger.warning({'action': 'receive_video', 'ex': ex })
                    time.sleep(0.5)
                    continue
                except socket.error as ex:
                    logger.error({'action': 'receive_video','ex':ex})
                    break

                try:
                    pipe_in.write(data[:size])
                    pipe_in.flush()
                except Exception as ex:
                    logger.error({'action':'receive_video','ex': ex})
                    break
    def video_binary_generator(self):
        while True:
            try:
                frame = self.proc_stdout.read(FRAME_SIZE)
            except Exception as ex:
                logger.error({'action':'video_binary_generator','ex': ex})
                continue
            if not frame:
                continue

            frame = np.fromstring(frame, np.uint8).reshape(FRAME_X,FRAME_Y,3)
            yield frame
    
    def video_jpeg_generator(self):
        for frame in self.video_binary_generator():
            _, jpeg = cv.imencode('.jpg',frame)
            jpeg_binary = jpeg.tobytes()
            yield jpeg_binary