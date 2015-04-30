import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaStorageProfileProtocol:
    KALTURA_DC = 0
    FTP = 1
    SCP = 2
    SFTP = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageProfileStatus:
    DISABLED = 1
    AUTOMATIC = 2
    MANUAL = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageServePriority:
    KALTURA_ONLY = 1
    KALTURA_FIRST = 2
    EXTERNAL_FIRST = 3
    EXTERNAL_ONLY = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaStorageProfile(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.name = None

        # @var string
        self.desciption = None

        # @var KalturaStorageProfileStatus
        self.status = None

        # @var KalturaStorageProfileProtocol
        self.protocol = None

        # @var string
        self.storageUrl = None

        # @var string
        self.storageBaseDir = None

        # @var string
        self.storageUsername = None

        # @var string
        self.storagePassword = None

        # @var bool
        self.storageFtpPassiveMode = None

        # @var string
        self.deliveryHttpBaseUrl = None

        # @var string
        self.deliveryRmpBaseUrl = None

        # @var string
        self.deliveryIisBaseUrl = None

        # @var int
        self.minFileSize = None

        # @var int
        self.maxFileSize = None

        # @var string
        self.flavorParamsIds = None

        # @var int
        self.maxConcurrentConnections = None

        # @var string
        self.pathManagerClass = None

        # @var string
        self.urlManagerClass = None

        # TODO - remove after events manager is implemented
        # No need to create enum for temp field
        # @var int
        self.trigger = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'desciption': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaStorageProfileStatus"), 
        'protocol': (KalturaEnumsFactory.createInt, "KalturaStorageProfileProtocol"), 
        'storageUrl': getXmlNodeText, 
        'storageBaseDir': getXmlNodeText, 
        'storageUsername': getXmlNodeText, 
        'storagePassword': getXmlNodeText, 
        'storageFtpPassiveMode': getXmlNodeBool, 
        'deliveryHttpBaseUrl': getXmlNodeText, 
        'deliveryRmpBaseUrl': getXmlNodeText, 
        'deliveryIisBaseUrl': getXmlNodeText, 
        'minFileSize': getXmlNodeInt, 
        'maxFileSize': getXmlNodeInt, 
        'flavorParamsIds': getXmlNodeText, 
        'maxConcurrentConnections': getXmlNodeInt, 
        'pathManagerClass': getXmlNodeText, 
        'urlManagerClass': getXmlNodeText, 
        'trigger': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStorageProfile")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("desciption", self.desciption)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addIntEnumIfNotNone("protocol", self.protocol)
        kparams.addStringIfNotNone("storageUrl", self.storageUrl)
        kparams.addStringIfNotNone("storageBaseDir", self.storageBaseDir)
        kparams.addStringIfNotNone("storageUsername", self.storageUsername)
        kparams.addStringIfNotNone("storagePassword", self.storagePassword)
        kparams.addBoolIfNotNone("storageFtpPassiveMode", self.storageFtpPassiveMode)
        kparams.addStringIfNotNone("deliveryHttpBaseUrl", self.deliveryHttpBaseUrl)
        kparams.addStringIfNotNone("deliveryRmpBaseUrl", self.deliveryRmpBaseUrl)
        kparams.addStringIfNotNone("deliveryIisBaseUrl", self.deliveryIisBaseUrl)
        kparams.addIntIfNotNone("minFileSize", self.minFileSize)
        kparams.addIntIfNotNone("maxFileSize", self.maxFileSize)
        kparams.addStringIfNotNone("flavorParamsIds", self.flavorParamsIds)
        kparams.addIntIfNotNone("maxConcurrentConnections", self.maxConcurrentConnections)
        kparams.addStringIfNotNone("pathManagerClass", self.pathManagerClass)
        kparams.addStringIfNotNone("urlManagerClass", self.urlManagerClass)
        kparams.addIntIfNotNone("trigger", self.trigger)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDesciption(self):
        return self.desciption

    def setDesciption(self, newDesciption):
        self.desciption = newDesciption

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, newProtocol):
        self.protocol = newProtocol

    def getStorageUrl(self):
        return self.storageUrl

    def setStorageUrl(self, newStorageUrl):
        self.storageUrl = newStorageUrl

    def getStorageBaseDir(self):
        return self.storageBaseDir

    def setStorageBaseDir(self, newStorageBaseDir):
        self.storageBaseDir = newStorageBaseDir

    def getStorageUsername(self):
        return self.storageUsername

    def setStorageUsername(self, newStorageUsername):
        self.storageUsername = newStorageUsername

    def getStoragePassword(self):
        return self.storagePassword

    def setStoragePassword(self, newStoragePassword):
        self.storagePassword = newStoragePassword

    def getStorageFtpPassiveMode(self):
        return self.storageFtpPassiveMode

    def setStorageFtpPassiveMode(self, newStorageFtpPassiveMode):
        self.storageFtpPassiveMode = newStorageFtpPassiveMode

    def getDeliveryHttpBaseUrl(self):
        return self.deliveryHttpBaseUrl

    def setDeliveryHttpBaseUrl(self, newDeliveryHttpBaseUrl):
        self.deliveryHttpBaseUrl = newDeliveryHttpBaseUrl

    def getDeliveryRmpBaseUrl(self):
        return self.deliveryRmpBaseUrl

    def setDeliveryRmpBaseUrl(self, newDeliveryRmpBaseUrl):
        self.deliveryRmpBaseUrl = newDeliveryRmpBaseUrl

    def getDeliveryIisBaseUrl(self):
        return self.deliveryIisBaseUrl

    def setDeliveryIisBaseUrl(self, newDeliveryIisBaseUrl):
        self.deliveryIisBaseUrl = newDeliveryIisBaseUrl

    def getMinFileSize(self):
        return self.minFileSize

    def setMinFileSize(self, newMinFileSize):
        self.minFileSize = newMinFileSize

    def getMaxFileSize(self):
        return self.maxFileSize

    def setMaxFileSize(self, newMaxFileSize):
        self.maxFileSize = newMaxFileSize

    def getFlavorParamsIds(self):
        return self.flavorParamsIds

    def setFlavorParamsIds(self, newFlavorParamsIds):
        self.flavorParamsIds = newFlavorParamsIds

    def getMaxConcurrentConnections(self):
        return self.maxConcurrentConnections

    def setMaxConcurrentConnections(self, newMaxConcurrentConnections):
        self.maxConcurrentConnections = newMaxConcurrentConnections

    def getPathManagerClass(self):
        return self.pathManagerClass

    def setPathManagerClass(self, newPathManagerClass):
        self.pathManagerClass = newPathManagerClass

    def getUrlManagerClass(self):
        return self.urlManagerClass

    def setUrlManagerClass(self, newUrlManagerClass):
        self.urlManagerClass = newUrlManagerClass

    def getTrigger(self):
        return self.trigger

    def setTrigger(self, newTrigger):
        self.trigger = newTrigger


class KalturaStorageProfileListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaStorageProfile
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaStorageProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStorageProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaStorageProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def listByPartner(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("storageprofile_storageprofile", "listByPartner", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfileListResponse)

    def updateStatus(self, storageId, status):
        kparams = KalturaParams()
        kparams.put("storageId", storageId)
        kparams.put("status", status)
        self.client.queueServiceActionCall("storageprofile_storageprofile", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, storageProfileId):
        kparams = KalturaParams()
        kparams.put("storageProfileId", storageProfileId)
        self.client.queueServiceActionCall("storageprofile_storageprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

    def update(self, storageProfileId, storageProfile):
        kparams = KalturaParams()
        kparams.put("storageProfileId", storageProfileId)
        kparams.addObjectIfNotNone("storageProfile", storageProfile)
        self.client.queueServiceActionCall("storageprofile_storageprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

    def add(self, storageProfile):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("storageProfile", storageProfile)
        self.client.queueServiceActionCall("storageprofile_storageprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

########## main ##########
class KalturaStorageProfileClientPlugin(KalturaClientPlugin):
    # KalturaStorageProfileClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaStorageProfileClientPlugin
    @staticmethod
    def get(client):
        if KalturaStorageProfileClientPlugin.instance == None:
            KalturaStorageProfileClientPlugin.instance = KalturaStorageProfileClientPlugin(client)
        return KalturaStorageProfileClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'storageProfile': KalturaStorageProfileService,
        }

    def getEnums(self):
        return {
            'KalturaStorageProfileProtocol': KalturaStorageProfileProtocol,
            'KalturaStorageProfileStatus': KalturaStorageProfileStatus,
            'KalturaStorageServePriority': KalturaStorageServePriority,
        }

    def getTypes(self):
        return {
            'KalturaStorageProfile': KalturaStorageProfile,
            'KalturaStorageProfileListResponse': KalturaStorageProfileListResponse,
        }

    # @return string
    def getName(self):
        return 'storageProfile'

