class Settings ():
    """Store settings"""
    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5

        # Bullets settings
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 80, 80, 80
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 2
        self.fleet_drop = 60
        self.max_health = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1