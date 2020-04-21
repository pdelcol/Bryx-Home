import LoadConfig
import BryxConnector
import HueController
import DatabaseConnector
import time


config = LoadConfig.Config()
database = DatabaseConnector.Database(config)

def addCall(call):
    database.mycol.insert_one(call)
    HueController.turnOnLights(config.bridgeaddress)


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
    searchCalls(calls)


while True:
    grabCalls()
    time.sleep(5)
    print("Checked Calls")
