import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaTrackEntryEventType:
    UPLOADED_FILE = 1
    WEBCAM_COMPLETED = 2
    IMPORT_STARTED = 3
    ADD_ENTRY = 4
    UPDATE_ENTRY = 5
    DELETED_ENTRY = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaFlavorParamsOutputListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaFlavorParamsOutput
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFlavorParamsOutput), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutputListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutputListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaThumbParamsOutputListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaThumbParamsOutput
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaThumbParamsOutput), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutputListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutputListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMediaInfoListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMediaInfo
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMediaInfo), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfoListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaInfoListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaTrackEntry(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = None

        # @var KalturaTrackEntryEventType
        self.trackEventType = None

        # @var string
        self.psVersion = None

        # @var string
        self.context = None

        # @var int
        self.partnerId = None

        # @var string
        self.entryId = None

        # @var string
        self.hostName = None

        # @var string
        self.userId = None

        # @var string
        self.changedProperties = None

        # @var string
        self.paramStr1 = None

        # @var string
        self.paramStr2 = None

        # @var string
        self.paramStr3 = None

        # @var string
        self.ks = None

        # @var string
        self.description = None

        # @var int
        self.createdAt = None

        # @var int
        self.updatedAt = None

        # @var string
        self.userIp = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'trackEventType': (KalturaEnumsFactory.createInt, "KalturaTrackEntryEventType"), 
        'psVersion': getXmlNodeText, 
        'context': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'hostName': getXmlNodeText, 
        'userId': getXmlNodeText, 
        'changedProperties': getXmlNodeText, 
        'paramStr1': getXmlNodeText, 
        'paramStr2': getXmlNodeText, 
        'paramStr3': getXmlNodeText, 
        'ks': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'userIp': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTrackEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTrackEntry")
        kparams.addIntIfNotNone("id", self.id)
        kparams.addIntEnumIfNotNone("trackEventType", self.trackEventType)
        kparams.addStringIfNotNone("psVersion", self.psVersion)
        kparams.addStringIfNotNone("context", self.context)
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addStringIfNotNone("hostName", self.hostName)
        kparams.addStringIfNotNone("userId", self.userId)
        kparams.addStringIfNotNone("changedProperties", self.changedProperties)
        kparams.addStringIfNotNone("paramStr1", self.paramStr1)
        kparams.addStringIfNotNone("paramStr2", self.paramStr2)
        kparams.addStringIfNotNone("paramStr3", self.paramStr3)
        kparams.addStringIfNotNone("ks", self.ks)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntIfNotNone("createdAt", self.createdAt)
        kparams.addIntIfNotNone("updatedAt", self.updatedAt)
        kparams.addStringIfNotNone("userIp", self.userIp)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTrackEventType(self):
        return self.trackEventType

    def setTrackEventType(self, newTrackEventType):
        self.trackEventType = newTrackEventType

    def getPsVersion(self):
        return self.psVersion

    def setPsVersion(self, newPsVersion):
        self.psVersion = newPsVersion

    def getContext(self):
        return self.context

    def setContext(self, newContext):
        self.context = newContext

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getHostName(self):
        return self.hostName

    def setHostName(self, newHostName):
        self.hostName = newHostName

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getChangedProperties(self):
        return self.changedProperties

    def setChangedProperties(self, newChangedProperties):
        self.changedProperties = newChangedProperties

    def getParamStr1(self):
        return self.paramStr1

    def setParamStr1(self, newParamStr1):
        self.paramStr1 = newParamStr1

    def getParamStr2(self):
        return self.paramStr2

    def setParamStr2(self, newParamStr2):
        self.paramStr2 = newParamStr2

    def getParamStr3(self):
        return self.paramStr3

    def setParamStr3(self, newParamStr3):
        self.paramStr3 = newParamStr3

    def getKs(self):
        return self.ks

    def setKs(self, newKs):
        self.ks = newKs

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def setCreatedAt(self, newCreatedAt):
        self.createdAt = newCreatedAt

    def getUpdatedAt(self):
        return self.updatedAt

    def setUpdatedAt(self, newUpdatedAt):
        self.updatedAt = newUpdatedAt

    def getUserIp(self):
        return self.userIp

    def setUserIp(self, newUserIp):
        self.userIp = newUserIp


class KalturaTrackEntryListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaTrackEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaTrackEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTrackEntryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTrackEntryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUiConfAdmin(KalturaUiConf):
    def __init__(self):
        KalturaUiConf.__init__(self)

        # @var bool
        self.isPublic = None


    PROPERTY_LOADERS = {
        'isPublic': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaUiConf.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdmin.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConf.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdmin")
        kparams.addBoolIfNotNone("isPublic", self.isPublic)
        return kparams

    def getIsPublic(self):
        return self.isPublic

    def setIsPublic(self, newIsPublic):
        self.isPublic = newIsPublic


class KalturaUiConfAdminListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUiConfAdmin
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUiConfAdmin), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdminListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdminListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaFlavorParamsOutputService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("adminconsole_flavorparamsoutput", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParamsOutputListResponse)


class KalturaThumbParamsOutputService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("adminconsole_thumbparamsoutput", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParamsOutputListResponse)


class KalturaMediaInfoService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("adminconsole_mediainfo", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaInfoListResponse)


class KalturaEntryAdminService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("adminconsole_entryadmin", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getByFlavorId(self, flavorId, version = -1):
        kparams = KalturaParams()
        kparams.put("flavorId", flavorId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("adminconsole_entryadmin", "getByFlavorId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getTracks(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("adminconsole_entryadmin", "getTracks", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTrackEntryListResponse)


class KalturaUiConfAdminService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uiConf):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("uiConf", uiConf)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def update(self, id, uiConf):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("uiConf", uiConf)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdminListResponse)

########## main ##########
class KalturaAdminConsoleClientPlugin(KalturaClientPlugin):
    # KalturaAdminConsoleClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaAdminConsoleClientPlugin
    @staticmethod
    def get(client):
        if KalturaAdminConsoleClientPlugin.instance == None:
            KalturaAdminConsoleClientPlugin.instance = KalturaAdminConsoleClientPlugin(client)
        return KalturaAdminConsoleClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'flavorParamsOutput': KalturaFlavorParamsOutputService,
            'thumbParamsOutput': KalturaThumbParamsOutputService,
            'mediaInfo': KalturaMediaInfoService,
            'entryAdmin': KalturaEntryAdminService,
            'uiConfAdmin': KalturaUiConfAdminService,
        }

    def getEnums(self):
        return {
            'KalturaTrackEntryEventType': KalturaTrackEntryEventType,
        }

    def getTypes(self):
        return {
            'KalturaFlavorParamsOutputListResponse': KalturaFlavorParamsOutputListResponse,
            'KalturaThumbParamsOutputListResponse': KalturaThumbParamsOutputListResponse,
            'KalturaMediaInfoListResponse': KalturaMediaInfoListResponse,
            'KalturaTrackEntry': KalturaTrackEntry,
            'KalturaTrackEntryListResponse': KalturaTrackEntryListResponse,
            'KalturaUiConfAdmin': KalturaUiConfAdmin,
            'KalturaUiConfAdminListResponse': KalturaUiConfAdminListResponse,
        }

    # @return string
    def getName(self):
        return 'adminConsole'

