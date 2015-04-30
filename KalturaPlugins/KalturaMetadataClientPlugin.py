import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaMetadataObjectType:
    ENTRY = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMetadataOrderBy:
    METADATA_PROFILE_VERSION_ASC = "+metadataProfileVersion"
    METADATA_PROFILE_VERSION_DESC = "-metadataProfileVersion"
    VERSION_ASC = "+version"
    VERSION_DESC = "-version"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMetadataProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMetadataProfileStatus:
    ACTIVE = 1
    DEPRECATED = 2
    TRANSFORMING = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMetadataStatus:
    VALID = 1
    INVALID = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaMetadataBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.partnerIdEqual = None

        # @var int
        self.metadataProfileIdEqual = None

        # @var int
        self.metadataProfileVersionEqual = None

        # @var int
        self.metadataProfileVersionGreaterThanOrEqual = None

        # @var int
        self.metadataProfileVersionLessThanOrEqual = None

        # @var KalturaMetadataObjectType
        self.metadataObjectTypeEqual = None

        # @var string
        self.objectIdEqual = None

        # @var string
        self.objectIdIn = None

        # @var int
        self.versionEqual = None

        # @var int
        self.versionGreaterThanOrEqual = None

        # @var int
        self.versionLessThanOrEqual = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var KalturaMetadataStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'metadataProfileIdEqual': getXmlNodeInt, 
        'metadataProfileVersionEqual': getXmlNodeInt, 
        'metadataProfileVersionGreaterThanOrEqual': getXmlNodeInt, 
        'metadataProfileVersionLessThanOrEqual': getXmlNodeInt, 
        'metadataObjectTypeEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataObjectType"), 
        'objectIdEqual': getXmlNodeText, 
        'objectIdIn': getXmlNodeText, 
        'versionEqual': getXmlNodeInt, 
        'versionGreaterThanOrEqual': getXmlNodeInt, 
        'versionLessThanOrEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataBaseFilter")
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addIntIfNotNone("metadataProfileIdEqual", self.metadataProfileIdEqual)
        kparams.addIntIfNotNone("metadataProfileVersionEqual", self.metadataProfileVersionEqual)
        kparams.addIntIfNotNone("metadataProfileVersionGreaterThanOrEqual", self.metadataProfileVersionGreaterThanOrEqual)
        kparams.addIntIfNotNone("metadataProfileVersionLessThanOrEqual", self.metadataProfileVersionLessThanOrEqual)
        kparams.addIntEnumIfNotNone("metadataObjectTypeEqual", self.metadataObjectTypeEqual)
        kparams.addStringIfNotNone("objectIdEqual", self.objectIdEqual)
        kparams.addStringIfNotNone("objectIdIn", self.objectIdIn)
        kparams.addIntIfNotNone("versionEqual", self.versionEqual)
        kparams.addIntIfNotNone("versionGreaterThanOrEqual", self.versionGreaterThanOrEqual)
        kparams.addIntIfNotNone("versionLessThanOrEqual", self.versionLessThanOrEqual)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getMetadataProfileIdEqual(self):
        return self.metadataProfileIdEqual

    def setMetadataProfileIdEqual(self, newMetadataProfileIdEqual):
        self.metadataProfileIdEqual = newMetadataProfileIdEqual

    def getMetadataProfileVersionEqual(self):
        return self.metadataProfileVersionEqual

    def setMetadataProfileVersionEqual(self, newMetadataProfileVersionEqual):
        self.metadataProfileVersionEqual = newMetadataProfileVersionEqual

    def getMetadataProfileVersionGreaterThanOrEqual(self):
        return self.metadataProfileVersionGreaterThanOrEqual

    def setMetadataProfileVersionGreaterThanOrEqual(self, newMetadataProfileVersionGreaterThanOrEqual):
        self.metadataProfileVersionGreaterThanOrEqual = newMetadataProfileVersionGreaterThanOrEqual

    def getMetadataProfileVersionLessThanOrEqual(self):
        return self.metadataProfileVersionLessThanOrEqual

    def setMetadataProfileVersionLessThanOrEqual(self, newMetadataProfileVersionLessThanOrEqual):
        self.metadataProfileVersionLessThanOrEqual = newMetadataProfileVersionLessThanOrEqual

    def getMetadataObjectTypeEqual(self):
        return self.metadataObjectTypeEqual

    def setMetadataObjectTypeEqual(self, newMetadataObjectTypeEqual):
        self.metadataObjectTypeEqual = newMetadataObjectTypeEqual

    def getObjectIdEqual(self):
        return self.objectIdEqual

    def setObjectIdEqual(self, newObjectIdEqual):
        self.objectIdEqual = newObjectIdEqual

    def getObjectIdIn(self):
        return self.objectIdIn

    def setObjectIdIn(self, newObjectIdIn):
        self.objectIdIn = newObjectIdIn

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual

    def getVersionGreaterThanOrEqual(self):
        return self.versionGreaterThanOrEqual

    def setVersionGreaterThanOrEqual(self, newVersionGreaterThanOrEqual):
        self.versionGreaterThanOrEqual = newVersionGreaterThanOrEqual

    def getVersionLessThanOrEqual(self):
        return self.versionLessThanOrEqual

    def setVersionLessThanOrEqual(self, newVersionLessThanOrEqual):
        self.versionLessThanOrEqual = newVersionLessThanOrEqual

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

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaMetadataFilter(KalturaMetadataBaseFilter):
    def __init__(self):
        KalturaMetadataBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMetadataBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMetadataBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataFilter")
        return kparams


class KalturaMetadata(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var int
        # @readonly
        self.metadataProfileId = None

        # @var int
        # @readonly
        self.metadataProfileVersion = None

        # @var KalturaMetadataObjectType
        # @readonly
        self.metadataObjectType = None

        # @var string
        # @readonly
        self.objectId = None

        # @var int
        # @readonly
        self.version = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var KalturaMetadataStatus
        # @readonly
        self.status = None

        # @var string
        # @readonly
        self.xml = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataProfileVersion': getXmlNodeInt, 
        'metadataObjectType': (KalturaEnumsFactory.createInt, "KalturaMetadataObjectType"), 
        'objectId': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaMetadataStatus"), 
        'xml': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadata.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadata")
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def getMetadataProfileVersion(self):
        return self.metadataProfileVersion

    def getMetadataObjectType(self):
        return self.metadataObjectType

    def getObjectId(self):
        return self.objectId

    def getVersion(self):
        return self.version

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getXml(self):
        return self.xml


class KalturaMetadataListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadata
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadata), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMetadataProfileBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var int
        self.partnerIdEqual = None

        # @var KalturaMetadataObjectType
        self.metadataObjectTypeEqual = None

        # @var int
        self.versionEqual = None

        # @var string
        self.nameEqual = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var KalturaMetadataProfileStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'metadataObjectTypeEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataObjectType"), 
        'versionEqual': getXmlNodeInt, 
        'nameEqual': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addIntEnumIfNotNone("metadataObjectTypeEqual", self.metadataObjectTypeEqual)
        kparams.addIntIfNotNone("versionEqual", self.versionEqual)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getMetadataObjectTypeEqual(self):
        return self.metadataObjectTypeEqual

    def setMetadataObjectTypeEqual(self, newMetadataObjectTypeEqual):
        self.metadataObjectTypeEqual = newMetadataObjectTypeEqual

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

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

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaMetadataProfileFilter(KalturaMetadataProfileBaseFilter):
    def __init__(self):
        KalturaMetadataProfileBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMetadataProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMetadataProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileFilter")
        return kparams


class KalturaMetadataProfile(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var KalturaMetadataObjectType
        self.metadataObjectType = None

        # @var int
        # @readonly
        self.version = None

        # @var string
        self.name = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var KalturaMetadataProfileStatus
        # @readonly
        self.status = None

        # @var string
        # @readonly
        self.xsd = None

        # @var string
        # @readonly
        self.views = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'metadataObjectType': (KalturaEnumsFactory.createInt, "KalturaMetadataObjectType"), 
        'version': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaMetadataProfileStatus"), 
        'xsd': getXmlNodeText, 
        'views': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfile")
        kparams.addIntEnumIfNotNone("metadataObjectType", self.metadataObjectType)
        kparams.addStringIfNotNone("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getMetadataObjectType(self):
        return self.metadataObjectType

    def setMetadataObjectType(self, newMetadataObjectType):
        self.metadataObjectType = newMetadataObjectType

    def getVersion(self):
        return self.version

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getXsd(self):
        return self.xsd

    def getViews(self):
        return self.views


class KalturaMetadataProfileListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadataProfile
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadataProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMetadataProfileField(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var string
        # @readonly
        self.xPath = None

        # @var string
        # @readonly
        self.key = None

        # @var string
        # @readonly
        self.label = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'xPath': getXmlNodeText, 
        'key': getXmlNodeText, 
        'label': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileField.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileField")
        return kparams

    def getId(self):
        return self.id

    def getXPath(self):
        return self.xPath

    def getKey(self):
        return self.key

    def getLabel(self):
        return self.label


class KalturaMetadataProfileFieldListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMetadataProfileField
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMetadataProfileField), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataProfileFieldListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMetadataProfileFieldListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaMetadataService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("metadata_metadata", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataListResponse)

    def add(self, metadataProfileId, objectType, objectId, xmlData):
        kparams = KalturaParams()
        kparams.put("metadataProfileId", metadataProfileId)
        kparams.put("objectType", objectType)
        kparams.put("objectId", objectId)
        kparams.put("xmlData", xmlData)
        self.client.queueServiceActionCall("metadata_metadata", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromFile(self, metadataProfileId, objectType, objectId, xmlFile):
        kparams = KalturaParams()
        kparams.put("metadataProfileId", metadataProfileId)
        kparams.put("objectType", objectType)
        kparams.put("objectId", objectId)
        kfiles = KalturaFiles()
        kfiles.put("xmlFile", xmlFile)
        self.client.queueServiceActionCall("metadata_metadata", "addFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromUrl(self, metadataProfileId, objectType, objectId, url):
        kparams = KalturaParams()
        kparams.put("metadataProfileId", metadataProfileId)
        kparams.put("objectType", objectType)
        kparams.put("objectId", objectId)
        kparams.put("url", url)
        self.client.queueServiceActionCall("metadata_metadata", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def addFromBulk(self, metadataProfileId, objectType, objectId, url):
        kparams = KalturaParams()
        kparams.put("metadataProfileId", metadataProfileId)
        kparams.put("objectType", objectType)
        kparams.put("objectId", objectId)
        kparams.put("url", url)
        self.client.queueServiceActionCall("metadata_metadata", "addFromBulk", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("metadata_metadata", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def invalidate(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("metadata_metadata", "invalidate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("metadata_metadata", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def update(self, id, xmlData = ""):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("xmlData", xmlData)
        self.client.queueServiceActionCall("metadata_metadata", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)

    def updateFromFile(self, id, xmlFile = None):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("xmlFile", xmlFile)
        self.client.queueServiceActionCall("metadata_metadata", "updateFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadata)


class KalturaMetadataProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("metadata_metadataprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfileListResponse)

    def listFields(self, metadataProfileId):
        kparams = KalturaParams()
        kparams.put("metadataProfileId", metadataProfileId)
        self.client.queueServiceActionCall("metadata_metadataprofile", "listFields", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfileFieldListResponse)

    def add(self, metadataProfile, xsdData, viewsData = ""):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("metadataProfile", metadataProfile)
        kparams.put("xsdData", xsdData)
        kparams.put("viewsData", viewsData)
        self.client.queueServiceActionCall("metadata_metadataprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def addFromFile(self, metadataProfile, xsdFile, viewsFile = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("metadataProfile", metadataProfile)
        kfiles = KalturaFiles()
        kfiles.put("xsdFile", xsdFile)
        kfiles.put("viewsFile", viewsFile)
        self.client.queueServiceActionCall("metadata_metadataprofile", "addFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("metadata_metadataprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("metadata_metadataprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def update(self, id, metadataProfile, xsdData = "", viewsData = ""):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("metadataProfile", metadataProfile)
        kparams.put("xsdData", xsdData)
        kparams.put("viewsData", viewsData)
        self.client.queueServiceActionCall("metadata_metadataprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def revert(self, id, toVersion):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("toVersion", toVersion)
        self.client.queueServiceActionCall("metadata_metadataprofile", "revert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def updateDefinitionFromFile(self, id, xsdFile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("xsdFile", xsdFile)
        self.client.queueServiceActionCall("metadata_metadataprofile", "updateDefinitionFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

    def updateViewsFromFile(self, id, viewsFile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("viewsFile", viewsFile)
        self.client.queueServiceActionCall("metadata_metadataprofile", "updateViewsFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMetadataProfile)

########## main ##########
class KalturaMetadataClientPlugin(KalturaClientPlugin):
    # KalturaMetadataClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaMetadataClientPlugin
    @staticmethod
    def get(client):
        if KalturaMetadataClientPlugin.instance == None:
            KalturaMetadataClientPlugin.instance = KalturaMetadataClientPlugin(client)
        return KalturaMetadataClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'metadata': KalturaMetadataService,
            'metadataProfile': KalturaMetadataProfileService,
        }

    def getEnums(self):
        return {
            'KalturaMetadataObjectType': KalturaMetadataObjectType,
            'KalturaMetadataOrderBy': KalturaMetadataOrderBy,
            'KalturaMetadataProfileOrderBy': KalturaMetadataProfileOrderBy,
            'KalturaMetadataProfileStatus': KalturaMetadataProfileStatus,
            'KalturaMetadataStatus': KalturaMetadataStatus,
        }

    def getTypes(self):
        return {
            'KalturaMetadataBaseFilter': KalturaMetadataBaseFilter,
            'KalturaMetadataFilter': KalturaMetadataFilter,
            'KalturaMetadata': KalturaMetadata,
            'KalturaMetadataListResponse': KalturaMetadataListResponse,
            'KalturaMetadataProfileBaseFilter': KalturaMetadataProfileBaseFilter,
            'KalturaMetadataProfileFilter': KalturaMetadataProfileFilter,
            'KalturaMetadataProfile': KalturaMetadataProfile,
            'KalturaMetadataProfileListResponse': KalturaMetadataProfileListResponse,
            'KalturaMetadataProfileField': KalturaMetadataProfileField,
            'KalturaMetadataProfileFieldListResponse': KalturaMetadataProfileFieldListResponse,
        }

    # @return string
    def getName(self):
        return 'metadata'

