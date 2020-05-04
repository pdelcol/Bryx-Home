import pymongo


class Database:
    def __init__(self, config):
        self.myclient = pymongo.MongoClient("mongodb://bryxconnector:" + config.password + "" + config.dbstring)
        self.mydb = self.myclient["CallData"]
        self.mycol = self.mydb["Calls"]
