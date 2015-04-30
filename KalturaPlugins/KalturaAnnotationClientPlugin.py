import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaAnnotationOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaAnnotationBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var string
        self.idEqual = None

        # @var string
        self.entryIdEqual = None

        # @var string
        self.parentIdEqual = None

        # @var string
        self.parentIdIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var string
        self.userIdEqual = None

        # @var string
        self.userIdIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'entryIdEqual': getXmlNodeText, 
        'parentIdEqual': getXmlNodeText, 
        'parentIdIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnotationBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAnnotationBaseFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfNotNone("parentIdEqual", self.parentIdEqual)
        kparams.addStringIfNotNone("parentIdIn", self.parentIdIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addStringIfNotNone("userIdEqual", self.userIdEqual)
        kparams.addStringIfNotNone("userIdIn", self.userIdIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getParentIdEqual(self):
        return self.parentIdEqual

    def setParentIdEqual(self, newParentIdEqual):
        self.parentIdEqual = newParentIdEqual

    def getParentIdIn(self):
        return self.parentIdIn

    def setParentIdIn(self, newParentIdIn):
        self.parentIdIn = newParentIdIn

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

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getUserIdIn(self):
        return self.userIdIn

    def setUserIdIn(self, newUserIdIn):
        self.userIdIn = newUserIdIn


class KalturaAnnotationFilter(KalturaAnnotationBaseFilter):
    def __init__(self):
        KalturaAnnotationBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAnnotationBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnotationFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAnnotationBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAnnotationFilter")
        return kparams


class KalturaAnnotation(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = None

        # @var string
        self.entryId = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.parentId = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var string
        self.text = None

        # @var string
        self.tags = None

        # @var int
        self.startTime = None

        # @var int
        self.endTime = None

        # @var string
        # @readonly
        self.userId = None

        # @var string
        self.partnerData = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'parentId': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'text': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'startTime': getXmlNodeInt, 
        'endTime': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'partnerData': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnotation.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAnnotation")
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addStringIfNotNone("parentId", self.parentId)
        kparams.addStringIfNotNone("text", self.text)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addIntIfNotNone("startTime", self.startTime)
        kparams.addIntIfNotNone("endTime", self.endTime)
        kparams.addStringIfNotNone("partnerData", self.partnerData)
        return kparams

    def getId(self):
        return self.id

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getPartnerId(self):
        return self.partnerId

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getText(self):
        return self.text

    def setText(self, newText):
        self.text = newText

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getUserId(self):
        return self.userId

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData


class KalturaAnnotationListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaAnnotation
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAnnotation), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnotationListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAnnotationListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaAnnotationService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("annotation_annotation", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnotationListResponse)

    def add(self, annotation):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("annotation", annotation)
        self.client.queueServiceActionCall("annotation_annotation", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnotation)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("annotation_annotation", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnotation)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("annotation_annotation", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def update(self, id, annotation):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("annotation", annotation)
        self.client.queueServiceActionCall("annotation_annotation", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnotation)

########## main ##########
class KalturaAnnotationClientPlugin(KalturaClientPlugin):
    # KalturaAnnotationClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaAnnotationClientPlugin
    @staticmethod
    def get(client):
        if KalturaAnnotationClientPlugin.instance == None:
            KalturaAnnotationClientPlugin.instance = KalturaAnnotationClientPlugin(client)
        return KalturaAnnotationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'annotation': KalturaAnnotationService,
        }

    def getEnums(self):
        return {
            'KalturaAnnotationOrderBy': KalturaAnnotationOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaAnnotationBaseFilter': KalturaAnnotationBaseFilter,
            'KalturaAnnotationFilter': KalturaAnnotationFilter,
            'KalturaAnnotation': KalturaAnnotation,
            'KalturaAnnotationListResponse': KalturaAnnotationListResponse,
        }

    # @return string
    def getName(self):
        return 'annotation'

