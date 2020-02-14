import LoadConfig
import BryxConnector
config = LoadConfig.Config()

BryxConnector.getCallData(config.token)
