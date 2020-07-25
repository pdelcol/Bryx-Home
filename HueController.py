from phue import Bridge


class HueBridge:
    def __init__(self, BridgeAddress):
        self.b = Bridge(BridgeAddress)
        self.b.connect()

    def turnOnLights(self):
        self.b.set_light('Tachi', 'on', True)
        self.b.set_light('Tachi', 'bri', 254)
        self.b.set_light('Tachi', 'sat', 254)
        self.b.set_light('Tachi', 'hue', 0)
