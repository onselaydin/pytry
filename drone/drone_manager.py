import logging
import socket
import sys
import time
import threading

#https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
#https://github.com/dji-sdk/Tello-Python/blob/master/Tello_Video/install/Windows/install.bat

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)
#1 feet = 30.48 centimeters
DEFAULT_DISTANCE = 0.30
DEFAULT_SPEED = 10
DEFAULT_DEGREE = 10 # rotalama sağa sola dönme konusu

class DroneManager(object):
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
        self._response_thread = threading.Thread(target=self.receive_response,args=(self.stop_event,))
        
        self._response_thread.start()

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
        return self.move('up',distance +' cm')
    def down(self,distance=DEFAULT_DISTANCE):
        return self.move('down',distance+' cm')
    def left(self,distance=DEFAULT_DISTANCE):
        return self.move('left',distance+' cm')
    def right(self,distance=DEFAULT_DISTANCE):
        return self.move('right',distance+' cm')
    def forward(self,distance=DEFAULT_DISTANCE):
        return self.move('forward',distance+' cm')
    def back(self,distance=DEFAULT_DISTANCE):
        return self.move('back',distance+' cm')
    def set_speed(self, speed):
        return self.send_command(f'speed {speed}')
    def clockwise(self, degree=DEFAULT_DEGREE): # saat yönünde
        return self.send_command(f'cw {degree}')
    def counter_clockwise(self, degree=DEFAULT_DEGREE): # saat yönün tersine
        return self.send_command(f'cw {degree}')
    def flip_front(self): # öne takla at fonksiyonu
        retun self.send_command('flip f')
    def flip_back(self): # getiye takla at metodu
        retun self.send_command('flip b')
    def flip_left(self):
        retun self.send_command('flip l')
    def flip_right(self):
        retun self.send_command('flip r')

if __name__ == '__main__':
    drone_manager = DroneManager()

    drone_manager.set_speed(100) #100 cm/s
    drone_manager.takeoff()
    time.sleep(10) # 10 sn benle
    #drone_manager.forward() # 30 cm ileri
    drone_manager.clockwise(90)
    time.sleep(5)
    drone_manager.counter_clockwise(90)
    time.sleep(5)
    # drone_manager.right() # 30 cm sağ
    # time.sleep(5)
    # drone_manager.back()
    # time.sleep(5)
    # drone_manager.left()
    # time.sleep(5)
    # drone_manager.set_speed(10)
    # time.sleep(1)
    # drone_manager.up() # 30 cm yukarı
    # time.sleep(5)
    # drone_manager.down() # 30 cm aşağı
    # time.sleep(5)

    drone_manager.land()
    drone_manager.stop()