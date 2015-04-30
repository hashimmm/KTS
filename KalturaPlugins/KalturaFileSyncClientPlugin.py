import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
########## classes ##########
########## services ##########
########## main ##########
class KalturaFileSyncClientPlugin(KalturaClientPlugin):
    # KalturaFileSyncClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaFileSyncClientPlugin
    @staticmethod
    def get(client):
        if KalturaFileSyncClientPlugin.instance == None:
            KalturaFileSyncClientPlugin.instance = KalturaFileSyncClientPlugin(client)
        return KalturaFileSyncClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'fileSync'

