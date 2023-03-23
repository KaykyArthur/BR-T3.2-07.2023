import pygame
from dino_runner.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAMEOVER, SOUNDS, TILES, MUSICS, BG1
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_tiles = 0
        self.y_pos_tiles = 285
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0
        self.score = 0
        self.menu_active = 1
        self.scores = []
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.player = Dinosaur()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        MUSICS[0].stop()
        MUSICS[1].stop()
        self.play_music(1)
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        self.update_scores()

    def update_score(self):
        self.score+=1

        if self.score %500 == 0:
            self.game_speed+=5
            SOUNDS[2].play()

    def update_scores(self):
        self.scores.append(self.score)

    def play_music(self, index):
        MUSICS[index].play()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background(BG)
        self.draw_tiles(TILES)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.draw_scores()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.flip()

    def draw_background(self, IMG):
        image_width = IMG.get_width()
        self.screen.blit(IMG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(IMG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(IMG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_tiles(self, IMG):
        image_width = IMG.get_width()
        self.screen.blit(IMG, (self.x_pos_tiles, self.y_pos_tiles))
        self.screen.blit(IMG, (image_width + self.x_pos_tiles, self.y_pos_tiles))
        if self.x_pos_tiles <= -image_width:
            self.screen.blit(IMG, (image_width + self.x_pos_tiles, self.y_pos_tiles))
            self.x_pos_tiles = 0
        self.x_pos_tiles -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f'{self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (900, 50)
        self.screen.blit(text, text_rect)        

    def draw_scores(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        self.scores_rank = font.render(f'HI {max(self.scores)}', True, (0,0,0))
        text_rect = self.scores_rank.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(self.scores_rank, text_rect)      

    def draw_menu_texts(self, menu_text, position, fontsize):
        font = pygame.font.Font(FONT_STYLE, fontsize)
        menu_text = font.render(menu_text, True, (0,0,0))
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = position
        self.screen.blit(menu_text, menu_text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up: {time_to_show}", True, (255,0,0))
                text_rect = text.get_rect()
                text_rect.x = 425
                text_rect.y = 100
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_menu(self):
        self.draw_background(BG1)
        self.menu_active = 1
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        self.play_music(0)
        if self.death_count == 0:
            self.draw_menu_texts('Dino Runner', (half_screen_width, half_screen_height -30), 40)
            self.draw_menu_texts('Press (S) to start playing', (half_screen_width, half_screen_height +30), 20)
        else:
            self.screen.blit(GAMEOVER, (355,200))
            self.draw_menu_texts(f'Best Score: {max(self.scores)}', (half_screen_width, half_screen_height + 90), 20)
            self.draw_menu_texts('Press (C) to continue playing', (half_screen_width, half_screen_height - 30), 20)
            self.draw_menu_texts('Press (R) to start a new game', (half_screen_width, half_screen_height + 30), 20)
        pygame.display.update()
        self.handle_events_on_menu()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0

    def continue_game(self):
        self.player.dino_jump = False
        self.obstacle_manager.reset_obstacles()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and self.death_count > 0:
                    self.continue_game()
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r] and self.death_count > 0:
                    self.reset_game()
                    self.run()

