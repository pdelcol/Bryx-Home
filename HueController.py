from phue import Bridge


def turnOnLights(BridgeAddress):
    b = Bridge(BridgeAddress)
    b.connect()
    b.set_light('Tachi', 'on', True)
    b.set_light('Tachi', 'bri', 254)
    b.set_light('Tachi', 'hue', 150)
