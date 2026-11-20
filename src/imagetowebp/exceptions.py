
class InvalidPathError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AnimatedImageError(Exception):
    def __init__(self, message):
            self.message = message
            super().__init__(self.message)
