import LoadConfig
import BryxConnector
import HueController
import DatabaseConnector
import time

config = LoadConfig.Config()
config.loadConfig()
database = DatabaseConnector.Database(config)
hue = HueController.HueBridge(config.bridgeaddress)


def addCall(call):
    hue.turnOnLights()
    database.mycol.insert_one(call)


def updateCall(call):
    database.mycol.update_one({"id": call["id"]}, {"$set": call})


def searchCalls(calls):
    for call in calls:
        findCallQuery = {"id": call["id"]}
        mydoc = database.mycol.find_one(findCallQuery)
        if mydoc is None:
            addCall(call)
            print("Found new call")
        else:
            updateCall(call)
            print("Updated Call")


def grabCalls():
    calls = BryxConnector.getCallData(config.token)
    if calls != '':
        searchCalls(calls)
    else:
        config.saveNewToken(BryxConnector.getToken(config))
        config.loadConfig()


while True:
    grabCalls()
    time.sleep(10)
    print("Checked Calls")
