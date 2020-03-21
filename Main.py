import LoadConfig
import BryxConnector
import HueController
import pymongo
import time

def addCall(call):
    mycol.insert_one(call)
    HueController.turnOnLights(config.bridgeaddress)


def searchCalls(calls):
    for call in calls:
        findCallQuery = {"id": call["id"]}
        mydoc = mycol.find_one(findCallQuery)
        if mydoc is None:
            addCall(call)
            print("Found new call")

def grabCalls():
    calls = BryxConnector.getCallData(config.token)
    searchCalls(calls)

config = LoadConfig.Config()
myclient = pymongo.MongoClient("mongodb://bryxconnector:"+config.password+"@cluster0-shard-00-00-osc62.gcp.mongodb.net:27017,cluster0-shard-00-01-osc62.gcp.mongodb.net:27017,cluster0-shard-00-02-osc62.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = myclient["CallData"]
mycol = mydb["Calls"]


while True:
    grabCalls()
    time.sleep(5)
    print("Checked Calls")
