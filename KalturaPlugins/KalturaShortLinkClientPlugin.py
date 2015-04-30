import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaShortLinkOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    EXPIRES_AT_ASC = "+expiresAt"
    EXPIRES_AT_DESC = "-expiresAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaShortLinkStatus:
    DISABLED = 1
    ENABLED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaShortLinkBaseFilter(KalturaFilter):
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
        self.expiresAtGreaterThanOrEqual = None

        # @var int
        self.expiresAtLessThanOrEqual = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.userIdEqual = None

        # @var string
        self.userIdIn = None

        # @var string
        self.systemNameEqual = None

        # @var string
        self.systemNameIn = None

        # @var KalturaShortLinkStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'expiresAtGreaterThanOrEqual': getXmlNodeInt, 
        'expiresAtLessThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaShortLinkStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaShortLinkBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("expiresAtGreaterThanOrEqual", self.expiresAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("expiresAtLessThanOrEqual", self.expiresAtLessThanOrEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("userIdEqual", self.userIdEqual)
        kparams.addStringIfNotNone("userIdIn", self.userIdIn)
        kparams.addStringIfNotNone("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfNotNone("systemNameIn", self.systemNameIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
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

    def getExpiresAtGreaterThanOrEqual(self):
        return self.expiresAtGreaterThanOrEqual

    def setExpiresAtGreaterThanOrEqual(self, newExpiresAtGreaterThanOrEqual):
        self.expiresAtGreaterThanOrEqual = newExpiresAtGreaterThanOrEqual

    def getExpiresAtLessThanOrEqual(self):
        return self.expiresAtLessThanOrEqual

    def setExpiresAtLessThanOrEqual(self, newExpiresAtLessThanOrEqual):
        self.expiresAtLessThanOrEqual = newExpiresAtLessThanOrEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getUserIdIn(self):
        return self.userIdIn

    def setUserIdIn(self, newUserIdIn):
        self.userIdIn = newUserIdIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaShortLinkFilter(KalturaShortLinkBaseFilter):
    def __init__(self):
        KalturaShortLinkBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaShortLinkBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaShortLinkBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaShortLinkFilter")
        return kparams


class KalturaShortLink(KalturaObjectBase):
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
        self.expiresAt = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.userId = None

        # @var string
        self.name = None

        # @var string
        self.systemName = None

        # @var string
        self.fullUrl = None

        # @var KalturaShortLinkStatus
        self.status = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'expiresAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'fullUrl': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaShortLinkStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLink.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaShortLink")
        kparams.addIntIfNotNone("expiresAt", self.expiresAt)
        kparams.addStringIfNotNone("userId", self.userId)
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("systemName", self.systemName)
        kparams.addStringIfNotNone("fullUrl", self.fullUrl)
        kparams.addIntEnumIfNotNone("status", self.status)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getExpiresAt(self):
        return self.expiresAt

    def setExpiresAt(self, newExpiresAt):
        self.expiresAt = newExpiresAt

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getFullUrl(self):
        return self.fullUrl

    def setFullUrl(self, newFullUrl):
        self.fullUrl = newFullUrl

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus


class KalturaShortLinkListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaShortLink
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaShortLink), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaShortLinkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaShortLinkListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaShortLinkService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("shortlink_shortlink", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLinkListResponse)

    def add(self, shortLink):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("shortLink", shortLink)
        self.client.queueServiceActionCall("shortlink_shortlink", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("shortlink_shortlink", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def update(self, id, shortLink):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("shortLink", shortLink)
        self.client.queueServiceActionCall("shortlink_shortlink", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("shortlink_shortlink", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaShortLink)

########## main ##########
class KalturaShortLinkClientPlugin(KalturaClientPlugin):
    # KalturaShortLinkClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaShortLinkClientPlugin
    @staticmethod
    def get(client):
        if KalturaShortLinkClientPlugin.instance == None:
            KalturaShortLinkClientPlugin.instance = KalturaShortLinkClientPlugin(client)
        return KalturaShortLinkClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'shortLink': KalturaShortLinkService,
        }

    def getEnums(self):
        return {
            'KalturaShortLinkOrderBy': KalturaShortLinkOrderBy,
            'KalturaShortLinkStatus': KalturaShortLinkStatus,
        }

    def getTypes(self):
        return {
            'KalturaShortLinkBaseFilter': KalturaShortLinkBaseFilter,
            'KalturaShortLinkFilter': KalturaShortLinkFilter,
            'KalturaShortLink': KalturaShortLink,
            'KalturaShortLinkListResponse': KalturaShortLinkListResponse,
        }

    # @return string
    def getName(self):
        return 'shortLink'

