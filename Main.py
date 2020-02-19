import LoadConfig
import BryxConnector
import HueController
config = LoadConfig.Config()

BryxConnector.getCallData(config.token)
HueController.getApi(config.bridgeaddress)