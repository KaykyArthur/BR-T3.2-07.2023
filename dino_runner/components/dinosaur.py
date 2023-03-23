import pygame

from dino_runner.utils.constants import RUNNING, SOUNDS, JUMPING, DUCKING, DEFAULT_TYPE,SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, SLOWMO_TYPE

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD, SLOWMO_TYPE: DUCKING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, SLOWMO_TYPE: JUMPING}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, SLOWMO_TYPE: RUNNING}
X_POS = 80
Y_POS = 312
Y_POSDUCK = 347
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL

        self.has_power_up = False

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5] 
        self.dino_rect.y = Y_POS
        self.step_index+=1     
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
 
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5] 
        self.dino_rect.y = Y_POSDUCK
        self.step_index+=1        
 
    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            SOUNDS[1].play()
        elif not self.dino_jump:
            self.dino_run = True
        elif self.dino_duck:
            self.jump_vel -=0.8

        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        else:
            self.dino_duck = False
        
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()  
        elif self.dino_duck:
            self.duck()            
            
        if user_input[pygame.K_RIGHT]:
            self.dino_rect.x +=10

        elif user_input[pygame.K_LEFT]:
            self.dino_rect.x -=10

        if self.step_index >= 10:
            self.step_index = 0       

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))