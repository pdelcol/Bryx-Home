from phue import Bridge


def getApi(BridgeAddress):
    b = Bridge(BridgeAddress)
    b.connect()
    lights = b.lights
    for l in lights:
        print(l.name)


