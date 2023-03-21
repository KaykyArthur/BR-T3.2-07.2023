import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAMEOVER, SOUNDS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

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
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.score = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score+=1

        if self.score %100 == 0:
            self.game_speed+=5
            SOUNDS[2].play()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f'Score: {self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu_texts(self, menu_text, position):
        font = pygame.font.Font(FONT_STYLE, 20)
        menu_text = font.render(menu_text, True, (0,0,0))
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = position
        self.screen.blit(menu_text, menu_text_rect)

    def show_menu(self):
        self.screen.fill((255,255,255))

        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            self.screen.blit(ICON, (510,100))
            self.show_menu_texts('Press (S) to start playing', (half_screen_width, half_screen_height))
        else:
            self.screen.blit(GAMEOVER, (355,200))
            self.show_menu_texts('Press (C) to continue playing', (half_screen_width, half_screen_height - 30))
            self.show_menu_texts('Press (R) to start a new game', (half_screen_width, half_screen_height + 30))

        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.run()
                    self.obstacle_manager.reset_obstacles()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.run()
                    self.reset_game()

