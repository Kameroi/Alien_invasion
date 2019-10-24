class Settings ():
    """Store settings"""
    def __init__(self):
        """Initialize static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)


        # Bullets settings
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = 80, 80, 80
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_drop = 10

        self.max_health = 2

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
         """Initialize settings that change throughout the game."""
         self.ship_speed = 1.5
         self.bullet_speed = 3.0
         self.alien_speed = 1.0
         #fleet_direction of 1 represents right; -1 represents left. self.fleet_direction = 1
         self.fleet_direction = 1

    def speedup (self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
