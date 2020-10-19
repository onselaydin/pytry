import pygame
pygame.joystick.init()
 
 
class InputDevice:
    def __init__(self):
        self._name =None
        self._button =[]
        self._button_total =0
        self._hat =[]
        self._hat_total =0
        self._axis =[]
        self._axis_total =0
    # __init__() ------------------------------------------------------------
 
# InputDevices --------------------------------------------------------------
 
 
 
class Controller:
    """Version 1.0
    Class - Joystick controller to assist with managing game controllers.
    Properties - axis, buttons, hats.
    Methods - joystick_count, joystick_name.
    """
# ---------------------------------------------------------------------------
# Description:
#   Designed to assist with handling the input from a joystick controller.
#
# Properties:
#   axis
#       Return: <list object>
#           The statuses of axis for this joystick.
#
#   buttons
#       Return: <list object>
#           The statuses of the buttons registered on this
#       controller.
#
#   hats
#       Return: <list object>
#           The statuses of arrow pads registered on this
#       controller.
# ---------------------------------------------------------------------------
    def __init__(self, index):
        self._device =None
 
        if pygame.joystick.get_count(): #   There's at least one game device connected.
            if index <=(pygame.joystick.get_count() -1): # index in range.
                self._device =InputDevice()
                self._index =index
                pygame.joystick.Joystick(index).init() # Initialise before first use.
 
                self._device._name =self.joystick_name(index)
                self._device._button_total =pygame.joystick.Joystick(index).get_numbuttons()
                self._device._hat_total =pygame.joystick.Joystick(index).get_numhats()
                self._device._axis_total =pygame.joystick.Joystick(index).get_numaxes()
 
                #    ------------- Prep list for buttons -------------
                #   Lets create the ellements in our list so we can store the
                # button states in them.
                for bi in range(self._device._button_total):
                    self._device._button.append(None)
                #   _.
 
                #    ------------- Prep list for hats -------------
                #   Examine the state of the arrow pad (NOT sticks) to see if the
                # player has pressed the pad to go left, right, up, etc.
                for hi in range(self._device._hat_total):
                    self._device._hat.append(None)
                #   _.
 
                #    ------------- Prep list for axis -------------
                #   Examing the state of the axis and store the
                # data in our list.
                for ai in range(self._device._axis_total):
                    #self.__axis.append(self.__joystick.get_axis(i))
                    self._device._axis.append(None)
                #   _.
            # end if
        # end if
    # __init__() ------------------------------------------------------------
     
     
    @property
    def axis(self):
        'Method - scans the device and returns the status of all the axis.'
        if not self._device ==None:
            return self._device._axis
        # end if
         
    # axis() ----------------------------------------------------------------
 
 
    @property
    def buttons(self):
        'Method - scans the device and returns the status of all the buttons.'
        if not self._device ==None:
            return self._device._button
        # end if
         
    # buttons() -------------------------------------------------------------
 
     
    @property
    def hats(self):
        'Method - scans the device and returns the status of all the hats.'
        if not self._device ==None:
            return self._device._hat
        # end if
         
    # hats() ----------------------------------------------------------------
 
 
 
    @staticmethod
    def joystick_count():
        'Mehtod - returns the number of controllers connected to device.'
        return pygame.joystick.get_count()
    # joystick_count() ------------------------------------------------------
 
     
 
    @staticmethod
    def joystick_name(joystick_index):
        'Method - returns the name of the joystick.'
        joystick =pygame.joystick.Joystick(joystick_index)
         
        return joystick.get_name()
    # joystick_name() -------------------------------------------------------
 
 
    def read_joystick_buffer(self):
        'Read all the events from pygame.'
        #   Reset the array.
        for hi in range(self._device._hat_total):
            self._device._hat[hi] =(0, 0)
        #   _.
         
        #   Events
        for event in pygame.event.get():
            print("Event type:", event.type)
            if event.type ==pygame.constants.JOYHATMOTION:
                for hi in range(self._device._hat_total):
                    eh1, eh2 =pygame.joystick.Joystick(self._index).get_hat(hi)
                    print("Hat values from pygame:", eh1, eh2)
                    if eh1 !=0 or eh2 !=0:
                        deh1, deh2 =self._device._hat[hi]
                        if eh1 !=0:
                            deh1 =eh1
                        # end if
                        if eh2 !=0:
                            deh2 =eh2
                        # end if
                        self._device._hat[hi] =(deh1, deh2)
                        print(self._device._hat[hi])
                    # end if
                # end for
                 
                for bi in range(self._device._button_total):
                    self._device._button[bi] =pygame.joystick.Joystick(self._index).get_button(bi)
                # end for
 
                for ai in range(self._device._axis_total):
                    self._device._axis[ai] =pygame.joystick.Joystick(self._index).get_axis(ai)
                # end for
            # end if
        # end for loop
                 
##            JOYAXISMOTION
##            JOYBALLMOTION
##            JOYBUTTONDOWN
##            JOYBUTTONUP
##            JOYHATMOTION
##
##            # Note: do the events stay there if they are NOT looked at
##            # (keyboard) ??? 
     
# Controller() ------------------------------------------------------