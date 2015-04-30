import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaDocumentEntryOrderBy:
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDocumentType:
    DOCUMENT = 11
    SWF = 12
    PDF = 13

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaDocumentEntry(KalturaBaseEntry):
    def __init__(self):
        KalturaBaseEntry.__init__(self)

        # The type of the document
        # @var KalturaDocumentType
        # @insertonly
        self.documentType = None

        # Conversion profile ID to override the default conversion profile
        # @var string
        # @insertonly
        self.conversionProfileId = None


    PROPERTY_LOADERS = {
        'documentType': (KalturaEnumsFactory.createInt, "KalturaDocumentType"), 
        'conversionProfileId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntry")
        kparams.addIntEnumIfNotNone("documentType", self.documentType)
        kparams.addStringIfNotNone("conversionProfileId", self.conversionProfileId)
        return kparams

    def getDocumentType(self):
        return self.documentType

    def setDocumentType(self, newDocumentType):
        self.documentType = newDocumentType

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId


class KalturaDocumentEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self):
        KalturaBaseEntryFilter.__init__(self)

        # @var KalturaDocumentType
        self.documentTypeEqual = None

        # @var string
        self.documentTypeIn = None


    PROPERTY_LOADERS = {
        'documentTypeEqual': (KalturaEnumsFactory.createInt, "KalturaDocumentType"), 
        'documentTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntryBaseFilter")
        kparams.addIntEnumIfNotNone("documentTypeEqual", self.documentTypeEqual)
        kparams.addStringIfNotNone("documentTypeIn", self.documentTypeIn)
        return kparams

    def getDocumentTypeEqual(self):
        return self.documentTypeEqual

    def setDocumentTypeEqual(self, newDocumentTypeEqual):
        self.documentTypeEqual = newDocumentTypeEqual

    def getDocumentTypeIn(self):
        return self.documentTypeIn

    def setDocumentTypeIn(self, newDocumentTypeIn):
        self.documentTypeIn = newDocumentTypeIn


class KalturaDocumentEntryFilter(KalturaDocumentEntryBaseFilter):
    def __init__(self):
        KalturaDocumentEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDocumentEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDocumentEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDocumentEntryFilter")
        return kparams


class KalturaDocumentListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDocumentEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDocumentEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDocumentListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDocumentListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaDocumentsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def addFromUploadedFile(self, documentEntry, uploadTokenId):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("documentEntry", documentEntry)
        kparams.put("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("document_documents", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromEntry(self, sourceEntryId, documentEntry = None, sourceFlavorParamsId = ""):
        kparams = KalturaParams()
        kparams.put("sourceEntryId", sourceEntryId)
        kparams.addObjectIfNotNone("documentEntry", documentEntry)
        kparams.put("sourceFlavorParamsId", sourceFlavorParamsId)
        self.client.queueServiceActionCall("document_documents", "addFromEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromFlavorAsset(self, sourceFlavorAssetId, documentEntry = None):
        kparams = KalturaParams()
        kparams.put("sourceFlavorAssetId", sourceFlavorAssetId)
        kparams.addObjectIfNotNone("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document_documents", "addFromFlavorAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def convert(self, entryId, conversionProfileId = "", dynamicConversionAttributes = None):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("conversionProfileId", conversionProfileId)
        kparams.addArrayIfNotNone("dynamicConversionAttributes", dynamicConversionAttributes)
        self.client.queueServiceActionCall("document_documents", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("document_documents", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def update(self, entryId, documentEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document_documents", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("document_documents", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("document_documents", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentListResponse)

    def upload(self, fileData):
        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("document_documents", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def convertPptToSwf(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("document_documents", "convertPptToSwf", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaDocumentClientPlugin(KalturaClientPlugin):
    # KalturaDocumentClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaDocumentClientPlugin
    @staticmethod
    def get(client):
        if KalturaDocumentClientPlugin.instance == None:
            KalturaDocumentClientPlugin.instance = KalturaDocumentClientPlugin(client)
        return KalturaDocumentClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'documents': KalturaDocumentsService,
        }

    def getEnums(self):
        return {
            'KalturaDocumentEntryOrderBy': KalturaDocumentEntryOrderBy,
            'KalturaDocumentType': KalturaDocumentType,
        }

    def getTypes(self):
        return {
            'KalturaDocumentEntry': KalturaDocumentEntry,
            'KalturaDocumentEntryBaseFilter': KalturaDocumentEntryBaseFilter,
            'KalturaDocumentEntryFilter': KalturaDocumentEntryFilter,
            'KalturaDocumentListResponse': KalturaDocumentListResponse,
        }

    # @return string
    def getName(self):
        return 'document'

