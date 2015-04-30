import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
########## classes ##########
class KalturaInternalToolsSession(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.partner_id = None

        # @var int
        self.valid_until = None

        # @var string
        self.partner_pattern = None

        # @var KalturaSessionType
        self.type = None

        # @var string
        self.error = None

        # @var int
        self.rand = None

        # @var string
        self.user = None

        # @var string
        self.privileges = None


    PROPERTY_LOADERS = {
        'partner_id': getXmlNodeInt, 
        'valid_until': getXmlNodeInt, 
        'partner_pattern': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createInt, "KalturaSessionType"), 
        'error': getXmlNodeText, 
        'rand': getXmlNodeInt, 
        'user': getXmlNodeText, 
        'privileges': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInternalToolsSession.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInternalToolsSession")
        kparams.addIntIfNotNone("partner_id", self.partner_id)
        kparams.addIntIfNotNone("valid_until", self.valid_until)
        kparams.addStringIfNotNone("partner_pattern", self.partner_pattern)
        kparams.addIntEnumIfNotNone("type", self.type)
        kparams.addStringIfNotNone("error", self.error)
        kparams.addIntIfNotNone("rand", self.rand)
        kparams.addStringIfNotNone("user", self.user)
        kparams.addStringIfNotNone("privileges", self.privileges)
        return kparams

    def getPartner_id(self):
        return self.partner_id

    def setPartner_id(self, newPartner_id):
        self.partner_id = newPartner_id

    def getValid_until(self):
        return self.valid_until

    def setValid_until(self, newValid_until):
        self.valid_until = newValid_until

    def getPartner_pattern(self):
        return self.partner_pattern

    def setPartner_pattern(self, newPartner_pattern):
        self.partner_pattern = newPartner_pattern

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getError(self):
        return self.error

    def setError(self, newError):
        self.error = newError

    def getRand(self):
        return self.rand

    def setRand(self, newRand):
        self.rand = newRand

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getPrivileges(self):
        return self.privileges

    def setPrivileges(self, newPrivileges):
        self.privileges = newPrivileges


########## services ##########

class KalturaKalturaInternalToolsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)


class KalturaKalturaInternalToolsSystemHelperService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def fromSecureString(self, str):
        kparams = KalturaParams()
        kparams.put("str", str)
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "fromSecureString", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaInternalToolsSession)

    def iptocountry(self, remote_addr):
        kparams = KalturaParams()
        kparams.put("remote_addr", remote_addr)
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "iptocountry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getRemoteAddress(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "getRemoteAddress", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaKalturaInternalToolsClientPlugin(KalturaClientPlugin):
    # KalturaKalturaInternalToolsClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaKalturaInternalToolsClientPlugin
    @staticmethod
    def get(client):
        if KalturaKalturaInternalToolsClientPlugin.instance == None:
            KalturaKalturaInternalToolsClientPlugin.instance = KalturaKalturaInternalToolsClientPlugin(client)
        return KalturaKalturaInternalToolsClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'KalturaInternalTools': KalturaKalturaInternalToolsService,
            'KalturaInternalToolsSystemHelper': KalturaKalturaInternalToolsSystemHelperService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaInternalToolsSession': KalturaInternalToolsSession,
        }

    # @return string
    def getName(self):
        return 'KalturaInternalTools'

