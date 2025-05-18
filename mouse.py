import pyautogui as pag
import math

class Mouse:
    def __init__(self):
        self.screen_width, self.screen_height = pag.size()
        self.leftMouseDown = False
        self.rightMouseDown = False

    def left_click(self):
        pag.click()
    
    def right_click(self):
        pag.rightClick()
    
    def move(self, camera_x, camera_y):
        new_width, new_height = self.__calculateNewCoordinates(camera_x, camera_y)
        pag.moveTo(new_width, new_height, pag.MINIMUM_DURATION)
    
    def left_click_drag(self, camera_x, camera_y):
        if(self.rightMouseDown): self.release()
        if(self.leftMouseDown == False):
            pag.mouseDown()
            self.leftMouseDown = True
        self.move(camera_x, camera_y)

    def right_click_drag(self, camera_x, camera_y):
        if(self.leftMouseDown): self.release()
        if(self.rightMouseDown == False):
            pag.mouseDown(button='right')
            self.rightMouseDown = True
        self.move(camera_x, camera_y)
    
    def release(self):
        pag.mouseUp()
        pag.mouseUp(button="right")
        if(self.leftMouseDown): self.leftMouseDown = False
        if(self.rightMouseDown): self.rightMouseDown = False
    
    def scroll(self, camera_dy):
        pag.scroll(-10 * math.floor(self.screen_height * camera_dy))
        
    def __calculateNewCoordinates(self, camera_x, camera_y):
        new_width = math.floor(self.screen_width * camera_x)
        new_height = math.floor(self.screen_height * camera_y)
        return new_width, new_height
