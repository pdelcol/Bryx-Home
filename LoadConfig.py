import configparser


class Config:
    def saveNewToken(self,token):
        self.config['BRYX']['token'] = token
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.token = self.config['BRYX']['token']
        self.password = self.config['DATABASE']['password']
        self.bridgeaddress = self.config['HUE']['BridgeAddress']
        self.bryxusername = self.config['BRYX']['username']
        self.bryxpassword = self.config['BRYX']['password']
        self.dbstring = self.config['DATABASE']['databasestring']


