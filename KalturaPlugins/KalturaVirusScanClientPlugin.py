import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaVirusFoundAction:
    NONE = 0
    DELETE = 1
    CLEAN_NONE = 2
    CLEAN_DELETE = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanEngineType:
    SYMANTEC_SCAN_ENGINE = "symantecScanEngine.SymantecScanEngine"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVirusScanProfileStatus:
    DISABLED = 1
    ENABLED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaVirusScanProfileBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var KalturaVirusScanProfileStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var KalturaVirusScanEngineType
        self.engineTypeEqual = None

        # @var string
        self.engineTypeIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaVirusScanProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'engineTypeEqual': (KalturaEnumsFactory.createString, "KalturaVirusScanEngineType"), 
        'engineTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringEnumIfNotNone("engineTypeEqual", self.engineTypeEqual)
        kparams.addStringIfNotNone("engineTypeIn", self.engineTypeIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getEngineTypeEqual(self):
        return self.engineTypeEqual

    def setEngineTypeEqual(self, newEngineTypeEqual):
        self.engineTypeEqual = newEngineTypeEqual

    def getEngineTypeIn(self):
        return self.engineTypeIn

    def setEngineTypeIn(self, newEngineTypeIn):
        self.engineTypeIn = newEngineTypeIn


class KalturaVirusScanProfileFilter(KalturaVirusScanProfileBaseFilter):
    def __init__(self):
        KalturaVirusScanProfileBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVirusScanProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVirusScanProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileFilter")
        return kparams


class KalturaVirusScanProfile(KalturaObjectBase):
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

        # @var KalturaVirusScanProfileStatus
        self.status = None

        # @var KalturaVirusScanEngineType
        self.engineType = None

        # @var KalturaBaseEntryFilter
        self.entryFilter = None

        # @var KalturaVirusFoundAction
        self.actionIfInfected = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaVirusScanProfileStatus"), 
        'engineType': (KalturaEnumsFactory.createString, "KalturaVirusScanEngineType"), 
        'entryFilter': (KalturaObjectFactory.create, KalturaBaseEntryFilter), 
        'actionIfInfected': (KalturaEnumsFactory.createInt, "KalturaVirusFoundAction"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfile")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addStringEnumIfNotNone("engineType", self.engineType)
        kparams.addObjectIfNotNone("entryFilter", self.entryFilter)
        kparams.addIntEnumIfNotNone("actionIfInfected", self.actionIfInfected)
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

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getEngineType(self):
        return self.engineType

    def setEngineType(self, newEngineType):
        self.engineType = newEngineType

    def getEntryFilter(self):
        return self.entryFilter

    def setEntryFilter(self, newEntryFilter):
        self.entryFilter = newEntryFilter

    def getActionIfInfected(self):
        return self.actionIfInfected

    def setActionIfInfected(self, newActionIfInfected):
        self.actionIfInfected = newActionIfInfected


class KalturaVirusScanProfileListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaVirusScanProfile
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaVirusScanProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirusScanProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVirusScanProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaVirusScanProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfileListResponse)

    def add(self, virusScanProfile):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("virusScanProfile", virusScanProfile)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def get(self, virusScanProfileId):
        kparams = KalturaParams()
        kparams.put("virusScanProfileId", virusScanProfileId)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def update(self, virusScanProfileId, virusScanProfile):
        kparams = KalturaParams()
        kparams.put("virusScanProfileId", virusScanProfileId)
        kparams.addObjectIfNotNone("virusScanProfile", virusScanProfile)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def delete(self, virusScanProfileId):
        kparams = KalturaParams()
        kparams.put("virusScanProfileId", virusScanProfileId)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaVirusScanProfile)

    def scan(self, flavorAssetId, virusScanProfileId = ""):
        kparams = KalturaParams()
        kparams.put("flavorAssetId", flavorAssetId)
        kparams.put("virusScanProfileId", virusScanProfileId)
        self.client.queueServiceActionCall("virusscan_virusscanprofile", "scan", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

########## main ##########
class KalturaVirusScanClientPlugin(KalturaClientPlugin):
    # KalturaVirusScanClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaVirusScanClientPlugin
    @staticmethod
    def get(client):
        if KalturaVirusScanClientPlugin.instance == None:
            KalturaVirusScanClientPlugin.instance = KalturaVirusScanClientPlugin(client)
        return KalturaVirusScanClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'virusScanProfile': KalturaVirusScanProfileService,
        }

    def getEnums(self):
        return {
            'KalturaVirusFoundAction': KalturaVirusFoundAction,
            'KalturaVirusScanEngineType': KalturaVirusScanEngineType,
            'KalturaVirusScanProfileOrderBy': KalturaVirusScanProfileOrderBy,
            'KalturaVirusScanProfileStatus': KalturaVirusScanProfileStatus,
        }

    def getTypes(self):
        return {
            'KalturaVirusScanProfileBaseFilter': KalturaVirusScanProfileBaseFilter,
            'KalturaVirusScanProfileFilter': KalturaVirusScanProfileFilter,
            'KalturaVirusScanProfile': KalturaVirusScanProfile,
            'KalturaVirusScanProfileListResponse': KalturaVirusScanProfileListResponse,
        }

    # @return string
    def getName(self):
        return 'virusScan'

