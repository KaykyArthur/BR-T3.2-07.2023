from dino_runner.utils.constants import SLOWMO, SLOWMO_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Slowmo(PowerUp):
    def __init__(self):
        super().__init__(SLOWMO, SLOWMO_TYPE)

