import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaAuditTrailAction:
    CREATED = "CREATED"
    COPIED = "COPIED"
    CHANGED = "CHANGED"
    DELETED = "DELETED"
    VIEWED = "VIEWED"
    CONTENT_VIEWED = "CONTENT_VIEWED"
    FILE_SYNC_CREATED = "FILE_SYNC_CREATED"
    RELATION_ADDED = "RELATION_ADDED"
    RELATION_REMOVED = "RELATION_REMOVED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAuditTrailContext:
    CLIENT = -1
    SCRIPT = 0
    PS2 = 1
    API_V3 = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAuditTrailObjectType:
    ACCESS_CONTROL = "accessControl"
    ADMIN_KUSER = "adminKuser"
    BATCH_JOB = "BatchJob"
    CATEGORY = "category"
    CONVERSION_PROFILE_2 = "conversionProfile2"
    EMAIL_INGESTION_PROFILE = "EmailIngestionProfile"
    ENTRY = "entry"
    FILE_SYNC = "FileSync"
    FLAVOR_ASSET = "flavorAsset"
    FLAVOR_PARAMS = "flavorParams"
    FLAVOR_PARAMS_CONVERSION_PROFILE = "flavorParamsConversionProfile"
    FLAVOR_PARAMS_OUTPUT = "flavorParamsOutput"
    KSHOW = "kshow"
    KSHOW_KUSER = "KshowKuser"
    KUSER = "kuser"
    MEDIA_INFO = "mediaInfo"
    MODERATION = "moderation"
    PARTNER = "Partner"
    ROUGHCUT = "roughcutEntry"
    SYNDICATION = "syndicationFeed"
    UI_CONF = "uiConf"
    UPLOAD_TOKEN = "UploadToken"
    WIDGET = "widget"
    METADATA = "Metadata"
    METADATA_PROFILE = "MetadataProfile"
    USER_LOGIN_DATA = "UserLoginData"
    USER_ROLE = "UserRole"
    PERMISSION = "Permission"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAuditTrailOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    PARSED_AT_ASC = "+parsedAt"
    PARSED_AT_DESC = "-parsedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAuditTrailStatus:
    PENDING = 1
    READY = 2
    FAILED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaAuditTrailBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.parsedAtGreaterThanOrEqual = None

        # @var int
        self.parsedAtLessThanOrEqual = None

        # @var KalturaAuditTrailStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var KalturaAuditTrailObjectType
        self.auditObjectTypeEqual = None

        # @var string
        self.auditObjectTypeIn = None

        # @var string
        self.objectIdEqual = None

        # @var string
        self.objectIdIn = None

        # @var string
        self.relatedObjectIdEqual = None

        # @var string
        self.relatedObjectIdIn = None

        # @var KalturaAuditTrailObjectType
        self.relatedObjectTypeEqual = None

        # @var string
        self.relatedObjectTypeIn = None

        # @var string
        self.entryIdEqual = None

        # @var string
        self.entryIdIn = None

        # @var int
        self.masterPartnerIdEqual = None

        # @var string
        self.masterPartnerIdIn = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.requestIdEqual = None

        # @var string
        self.requestIdIn = None

        # @var string
        self.userIdEqual = None

        # @var string
        self.userIdIn = None

        # @var KalturaAuditTrailAction
        self.actionEqual = None

        # @var string
        self.actionIn = None

        # @var string
        self.ksEqual = None

        # @var KalturaAuditTrailContext
        self.contextEqual = None

        # @var string
        self.contextIn = None

        # @var string
        self.entryPointEqual = None

        # @var string
        self.entryPointIn = None

        # @var string
        self.serverNameEqual = None

        # @var string
        self.serverNameIn = None

        # @var string
        self.ipAddressEqual = None

        # @var string
        self.ipAddressIn = None

        # @var string
        self.clientTagEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'parsedAtGreaterThanOrEqual': getXmlNodeInt, 
        'parsedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaAuditTrailStatus"), 
        'statusIn': getXmlNodeText, 
        'auditObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaAuditTrailObjectType"), 
        'auditObjectTypeIn': getXmlNodeText, 
        'objectIdEqual': getXmlNodeText, 
        'objectIdIn': getXmlNodeText, 
        'relatedObjectIdEqual': getXmlNodeText, 
        'relatedObjectIdIn': getXmlNodeText, 
        'relatedObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaAuditTrailObjectType"), 
        'relatedObjectTypeIn': getXmlNodeText, 
        'entryIdEqual': getXmlNodeText, 
        'entryIdIn': getXmlNodeText, 
        'masterPartnerIdEqual': getXmlNodeInt, 
        'masterPartnerIdIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'requestIdEqual': getXmlNodeText, 
        'requestIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
        'actionEqual': (KalturaEnumsFactory.createString, "KalturaAuditTrailAction"), 
        'actionIn': getXmlNodeText, 
        'ksEqual': getXmlNodeText, 
        'contextEqual': (KalturaEnumsFactory.createInt, "KalturaAuditTrailContext"), 
        'contextIn': getXmlNodeText, 
        'entryPointEqual': getXmlNodeText, 
        'entryPointIn': getXmlNodeText, 
        'serverNameEqual': getXmlNodeText, 
        'serverNameIn': getXmlNodeText, 
        'ipAddressEqual': getXmlNodeText, 
        'ipAddressIn': getXmlNodeText, 
        'clientTagEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAuditTrailBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAuditTrailBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("parsedAtGreaterThanOrEqual", self.parsedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("parsedAtLessThanOrEqual", self.parsedAtLessThanOrEqual)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringEnumIfNotNone("auditObjectTypeEqual", self.auditObjectTypeEqual)
        kparams.addStringIfNotNone("auditObjectTypeIn", self.auditObjectTypeIn)
        kparams.addStringIfNotNone("objectIdEqual", self.objectIdEqual)
        kparams.addStringIfNotNone("objectIdIn", self.objectIdIn)
        kparams.addStringIfNotNone("relatedObjectIdEqual", self.relatedObjectIdEqual)
        kparams.addStringIfNotNone("relatedObjectIdIn", self.relatedObjectIdIn)
        kparams.addStringEnumIfNotNone("relatedObjectTypeEqual", self.relatedObjectTypeEqual)
        kparams.addStringIfNotNone("relatedObjectTypeIn", self.relatedObjectTypeIn)
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfNotNone("entryIdIn", self.entryIdIn)
        kparams.addIntIfNotNone("masterPartnerIdEqual", self.masterPartnerIdEqual)
        kparams.addStringIfNotNone("masterPartnerIdIn", self.masterPartnerIdIn)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("requestIdEqual", self.requestIdEqual)
        kparams.addStringIfNotNone("requestIdIn", self.requestIdIn)
        kparams.addStringIfNotNone("userIdEqual", self.userIdEqual)
        kparams.addStringIfNotNone("userIdIn", self.userIdIn)
        kparams.addStringEnumIfNotNone("actionEqual", self.actionEqual)
        kparams.addStringIfNotNone("actionIn", self.actionIn)
        kparams.addStringIfNotNone("ksEqual", self.ksEqual)
        kparams.addIntEnumIfNotNone("contextEqual", self.contextEqual)
        kparams.addStringIfNotNone("contextIn", self.contextIn)
        kparams.addStringIfNotNone("entryPointEqual", self.entryPointEqual)
        kparams.addStringIfNotNone("entryPointIn", self.entryPointIn)
        kparams.addStringIfNotNone("serverNameEqual", self.serverNameEqual)
        kparams.addStringIfNotNone("serverNameIn", self.serverNameIn)
        kparams.addStringIfNotNone("ipAddressEqual", self.ipAddressEqual)
        kparams.addStringIfNotNone("ipAddressIn", self.ipAddressIn)
        kparams.addStringIfNotNone("clientTagEqual", self.clientTagEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getParsedAtGreaterThanOrEqual(self):
        return self.parsedAtGreaterThanOrEqual

    def setParsedAtGreaterThanOrEqual(self, newParsedAtGreaterThanOrEqual):
        self.parsedAtGreaterThanOrEqual = newParsedAtGreaterThanOrEqual

    def getParsedAtLessThanOrEqual(self):
        return self.parsedAtLessThanOrEqual

    def setParsedAtLessThanOrEqual(self, newParsedAtLessThanOrEqual):
        self.parsedAtLessThanOrEqual = newParsedAtLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getAuditObjectTypeEqual(self):
        return self.auditObjectTypeEqual

    def setAuditObjectTypeEqual(self, newAuditObjectTypeEqual):
        self.auditObjectTypeEqual = newAuditObjectTypeEqual

    def getAuditObjectTypeIn(self):
        return self.auditObjectTypeIn

    def setAuditObjectTypeIn(self, newAuditObjectTypeIn):
        self.auditObjectTypeIn = newAuditObjectTypeIn

    def getObjectIdEqual(self):
        return self.objectIdEqual

    def setObjectIdEqual(self, newObjectIdEqual):
        self.objectIdEqual = newObjectIdEqual

    def getObjectIdIn(self):
        return self.objectIdIn

    def setObjectIdIn(self, newObjectIdIn):
        self.objectIdIn = newObjectIdIn

    def getRelatedObjectIdEqual(self):
        return self.relatedObjectIdEqual

    def setRelatedObjectIdEqual(self, newRelatedObjectIdEqual):
        self.relatedObjectIdEqual = newRelatedObjectIdEqual

    def getRelatedObjectIdIn(self):
        return self.relatedObjectIdIn

    def setRelatedObjectIdIn(self, newRelatedObjectIdIn):
        self.relatedObjectIdIn = newRelatedObjectIdIn

    def getRelatedObjectTypeEqual(self):
        return self.relatedObjectTypeEqual

    def setRelatedObjectTypeEqual(self, newRelatedObjectTypeEqual):
        self.relatedObjectTypeEqual = newRelatedObjectTypeEqual

    def getRelatedObjectTypeIn(self):
        return self.relatedObjectTypeIn

    def setRelatedObjectTypeIn(self, newRelatedObjectTypeIn):
        self.relatedObjectTypeIn = newRelatedObjectTypeIn

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getEntryIdIn(self):
        return self.entryIdIn

    def setEntryIdIn(self, newEntryIdIn):
        self.entryIdIn = newEntryIdIn

    def getMasterPartnerIdEqual(self):
        return self.masterPartnerIdEqual

    def setMasterPartnerIdEqual(self, newMasterPartnerIdEqual):
        self.masterPartnerIdEqual = newMasterPartnerIdEqual

    def getMasterPartnerIdIn(self):
        return self.masterPartnerIdIn

    def setMasterPartnerIdIn(self, newMasterPartnerIdIn):
        self.masterPartnerIdIn = newMasterPartnerIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getRequestIdEqual(self):
        return self.requestIdEqual

    def setRequestIdEqual(self, newRequestIdEqual):
        self.requestIdEqual = newRequestIdEqual

    def getRequestIdIn(self):
        return self.requestIdIn

    def setRequestIdIn(self, newRequestIdIn):
        self.requestIdIn = newRequestIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getUserIdIn(self):
        return self.userIdIn

    def setUserIdIn(self, newUserIdIn):
        self.userIdIn = newUserIdIn

    def getActionEqual(self):
        return self.actionEqual

    def setActionEqual(self, newActionEqual):
        self.actionEqual = newActionEqual

    def getActionIn(self):
        return self.actionIn

    def setActionIn(self, newActionIn):
        self.actionIn = newActionIn

    def getKsEqual(self):
        return self.ksEqual

    def setKsEqual(self, newKsEqual):
        self.ksEqual = newKsEqual

    def getContextEqual(self):
        return self.contextEqual

    def setContextEqual(self, newContextEqual):
        self.contextEqual = newContextEqual

    def getContextIn(self):
        return self.contextIn

    def setContextIn(self, newContextIn):
        self.contextIn = newContextIn

    def getEntryPointEqual(self):
        return self.entryPointEqual

    def setEntryPointEqual(self, newEntryPointEqual):
        self.entryPointEqual = newEntryPointEqual

    def getEntryPointIn(self):
        return self.entryPointIn

    def setEntryPointIn(self, newEntryPointIn):
        self.entryPointIn = newEntryPointIn

    def getServerNameEqual(self):
        return self.serverNameEqual

    def setServerNameEqual(self, newServerNameEqual):
        self.serverNameEqual = newServerNameEqual

    def getServerNameIn(self):
        return self.serverNameIn

    def setServerNameIn(self, newServerNameIn):
        self.serverNameIn = newServerNameIn

    def getIpAddressEqual(self):
        return self.ipAddressEqual

    def setIpAddressEqual(self, newIpAddressEqual):
        self.ipAddressEqual = newIpAddressEqual

    def getIpAddressIn(self):
        return self.ipAddressIn

    def setIpAddressIn(self, newIpAddressIn):
        self.ipAddressIn = newIpAddressIn

    def getClientTagEqual(self):
        return self.clientTagEqual

    def setClientTagEqual(self, newClientTagEqual):
        self.clientTagEqual = newClientTagEqual


class KalturaAuditTrailFilter(KalturaAuditTrailBaseFilter):
    def __init__(self):
        KalturaAuditTrailBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAuditTrailBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAuditTrailFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAuditTrailBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAuditTrailFilter")
        return kparams


class KalturaAuditTrailInfo(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAuditTrailInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAuditTrailInfo")
        return kparams


class KalturaAuditTrail(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.createdAt = None

        # Indicates when the data was parsed
        # @var int
        # @readonly
        self.parsedAt = None

        # @var KalturaAuditTrailStatus
        # @readonly
        self.status = None

        # @var KalturaAuditTrailObjectType
        self.auditObjectType = None

        # @var string
        self.objectId = None

        # @var string
        self.relatedObjectId = None

        # @var KalturaAuditTrailObjectType
        self.relatedObjectType = None

        # @var string
        self.entryId = None

        # @var int
        # @readonly
        self.masterPartnerId = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        # @readonly
        self.requestId = None

        # @var string
        self.userId = None

        # @var KalturaAuditTrailAction
        self.action = None

        # @var KalturaAuditTrailInfo
        self.data = None

        # @var string
        # @readonly
        self.ks = None

        # @var KalturaAuditTrailContext
        # @readonly
        self.context = None

        # The API service and action that called and caused this audit
        # @var string
        # @readonly
        self.entryPoint = None

        # @var string
        # @readonly
        self.serverName = None

        # @var string
        # @readonly
        self.ipAddress = None

        # @var string
        # @readonly
        self.userAgent = None

        # @var string
        self.clientTag = None

        # @var string
        self.description = None

        # @var string
        # @readonly
        self.errorDescription = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'parsedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaAuditTrailStatus"), 
        'auditObjectType': (KalturaEnumsFactory.createString, "KalturaAuditTrailObjectType"), 
        'objectId': getXmlNodeText, 
        'relatedObjectId': getXmlNodeText, 
        'relatedObjectType': (KalturaEnumsFactory.createString, "KalturaAuditTrailObjectType"), 
        'entryId': getXmlNodeText, 
        'masterPartnerId': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'requestId': getXmlNodeText, 
        'userId': getXmlNodeText, 
        'action': (KalturaEnumsFactory.createString, "KalturaAuditTrailAction"), 
        'data': (KalturaObjectFactory.create, KalturaAuditTrailInfo), 
        'ks': getXmlNodeText, 
        'context': (KalturaEnumsFactory.createInt, "KalturaAuditTrailContext"), 
        'entryPoint': getXmlNodeText, 
        'serverName': getXmlNodeText, 
        'ipAddress': getXmlNodeText, 
        'userAgent': getXmlNodeText, 
        'clientTag': getXmlNodeText, 
        'description': getXmlNodeText, 
        'errorDescription': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAuditTrail.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAuditTrail")
        kparams.addStringEnumIfNotNone("auditObjectType", self.auditObjectType)
        kparams.addStringIfNotNone("objectId", self.objectId)
        kparams.addStringIfNotNone("relatedObjectId", self.relatedObjectId)
        kparams.addStringEnumIfNotNone("relatedObjectType", self.relatedObjectType)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addStringIfNotNone("userId", self.userId)
        kparams.addStringEnumIfNotNone("action", self.action)
        kparams.addObjectIfNotNone("data", self.data)
        kparams.addStringIfNotNone("clientTag", self.clientTag)
        kparams.addStringIfNotNone("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getParsedAt(self):
        return self.parsedAt

    def getStatus(self):
        return self.status

    def getAuditObjectType(self):
        return self.auditObjectType

    def setAuditObjectType(self, newAuditObjectType):
        self.auditObjectType = newAuditObjectType

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getRelatedObjectId(self):
        return self.relatedObjectId

    def setRelatedObjectId(self, newRelatedObjectId):
        self.relatedObjectId = newRelatedObjectId

    def getRelatedObjectType(self):
        return self.relatedObjectType

    def setRelatedObjectType(self, newRelatedObjectType):
        self.relatedObjectType = newRelatedObjectType

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getMasterPartnerId(self):
        return self.masterPartnerId

    def getPartnerId(self):
        return self.partnerId

    def getRequestId(self):
        return self.requestId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getKs(self):
        return self.ks

    def getContext(self):
        return self.context

    def getEntryPoint(self):
        return self.entryPoint

    def getServerName(self):
        return self.serverName

    def getIpAddress(self):
        return self.ipAddress

    def getUserAgent(self):
        return self.userAgent

    def getClientTag(self):
        return self.clientTag

    def setClientTag(self, newClientTag):
        self.clientTag = newClientTag

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getErrorDescription(self):
        return self.errorDescription


class KalturaAuditTrailListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaAuditTrail
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAuditTrail), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAuditTrailListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAuditTrailListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaAuditTrailService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("audit_audittrail", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAuditTrailListResponse)

    def add(self, auditTrail):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("auditTrail", auditTrail)
        self.client.queueServiceActionCall("audit_audittrail", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAuditTrail)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("audit_audittrail", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAuditTrail)

########## main ##########
class KalturaAuditClientPlugin(KalturaClientPlugin):
    # KalturaAuditClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaAuditClientPlugin
    @staticmethod
    def get(client):
        if KalturaAuditClientPlugin.instance == None:
            KalturaAuditClientPlugin.instance = KalturaAuditClientPlugin(client)
        return KalturaAuditClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'auditTrail': KalturaAuditTrailService,
        }

    def getEnums(self):
        return {
            'KalturaAuditTrailAction': KalturaAuditTrailAction,
            'KalturaAuditTrailContext': KalturaAuditTrailContext,
            'KalturaAuditTrailObjectType': KalturaAuditTrailObjectType,
            'KalturaAuditTrailOrderBy': KalturaAuditTrailOrderBy,
            'KalturaAuditTrailStatus': KalturaAuditTrailStatus,
        }

    def getTypes(self):
        return {
            'KalturaAuditTrailBaseFilter': KalturaAuditTrailBaseFilter,
            'KalturaAuditTrailFilter': KalturaAuditTrailFilter,
            'KalturaAuditTrailInfo': KalturaAuditTrailInfo,
            'KalturaAuditTrail': KalturaAuditTrail,
            'KalturaAuditTrailListResponse': KalturaAuditTrailListResponse,
        }

    # @return string
    def getName(self):
        return 'audit'

