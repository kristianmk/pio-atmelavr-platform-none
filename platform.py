from platformio.public import PlatformBase

class AvrnonePlatform(PlatformBase):
  def is_embedded(self):
    return True

