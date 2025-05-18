import pyautogui as pag
import math

class Mouse:
    def __init__(self, camera_width, camera_height):
        self.camera_width = camera_width;
        self.camera_height = camera_height;
        self.screen_width, self.screen_height = pag.size();

    def left_click(self):
        pag.click();
    
    def right_click(self):
        pag.rightClick();
    
    def move(self, camera_x, camera_y):
        new_width, new_height = self.__calculateNewCoordinates(camera_x, camera_y);
        pag.moveTo(new_width, new_height, pag.MINIMUM_DURATION);
    
    def left_click_drag(self, camera_x, camera_y):
        pag.mouseDown();
        self.move(camera_x, camera_y);

    def right_click_drag(self, camera_x, camera_y):
        pag.mouseDown(button='right');
        self.move(camera_x, camera_y);
    
    def release(self):
        pag.mouseUp();
    
    def scroll(self, camera_dy):
        pag.scroll(-10 * math.floor(self.screen_height * camera_dy / self.camera_height));
        
    def __calculateNewCoordinates(self, camera_x, camera_y):
        new_width = math.floor(self.screen_width * camera_x / self.camera_width);
        new_height = math.floor(self.screen_height * camera_y / self.camera_height);
        return new_width, new_height;
