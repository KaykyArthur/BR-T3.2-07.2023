import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "jala Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "romulus.ttf"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
SLOWMO_TYPE = "slowmo"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", 'Sounds')

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

SOUNDS = [
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "die.wav")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "jump.wav")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "point.wav")),
]

MUSICS = [
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "8_Bit_Menu.mp3")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "8_Bit_Adventure.mp3")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "8_Bit_Retro.mp3")),
]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

BAT = [
    pygame.image.load(os.path.join(IMG_DIR, "Bat/Bat1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bat/Bat2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bat/Bat3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bat/Bat4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bat/Bat5.png")),

]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Power_ups/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Power_ups/hammer.png'))
SLOWMO = pygame.image.load(os.path.join(IMG_DIR, 'Power_ups/chunk_rotten.png'))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

TILES = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg.png'))
BG1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg1.png'))

X_POS_TILES = 0
Y_POS_TILES = 285
X_POS_BG = 0
Y_POS_BG = 0

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
