import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SOUNDS, MUSICS, BAT


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.obstacle_type = random.randint(0, 3)
        if len(self.obstacles) == 0 and self.obstacle_type == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS, 325))
        if len(self.obstacles) == 0 and self.obstacle_type == 1:
            self.obstacles.append(Cactus(LARGE_CACTUS, 300))
        if len(self.obstacles) == 0 and self.obstacle_type == 2:
            self.obstacles.append(Bird(BIRD, random.randint(215, 300)))
        if len(self.obstacles) == 0 and self.obstacle_type == 3:
            self.obstacles.append(Bird(BAT, random.randint(215, 300)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    MUSICS[0].stop()
                    MUSICS[1].stop()
                    SOUNDS[0].play()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count+=1
                    break                
                else:
                    self.obstacles.remove(obstacle)
                break                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()
