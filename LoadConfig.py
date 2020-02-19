import configparser



class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.token = config['BRYX']['token']
        self.db = config['DATABASE']['db']
        self.user = config['DATABASE']['username']
        self.password = config['DATABASE']['password']
        self.bridgeaddress = config['HUE']['BridgeAddress']

