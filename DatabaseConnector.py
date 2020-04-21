import pymongo


class Database:
    def __init__(self, config):
        self.myclient = pymongo.MongoClient("mongodb://bryxconnector:" + config.password + "@cluster0-shard-00-00-osc62.gcp.mongodb.net:27017,cluster0-shard-00-01-osc62.gcp.mongodb.net:27017,cluster0-shard-00-02-osc62.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
        self.mydb = self.myclient["CallData"]
        self.mycol = self.mydb["Calls"]
