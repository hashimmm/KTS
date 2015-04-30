import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaCaptionClientPlugin import *
from KalturaClientBase import *

########## enums ##########
########## classes ##########
class KalturaCaptionAssetItemFilter(KalturaCaptionAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            contentLike=NotImplemented,
            contentMultiLikeOr=NotImplemented,
            contentMultiLikeAnd=NotImplemented,
            partnerDescriptionLike=NotImplemented,
            partnerDescriptionMultiLikeOr=NotImplemented,
            partnerDescriptionMultiLikeAnd=NotImplemented,
            languageEqual=NotImplemented,
            languageIn=NotImplemented,
            labelEqual=NotImplemented,
            labelIn=NotImplemented,
            startTimeGreaterThanOrEqual=NotImplemented,
            startTimeLessThanOrEqual=NotImplemented,
            endTimeGreaterThanOrEqual=NotImplemented,
            endTimeLessThanOrEqual=NotImplemented):
        KalturaCaptionAssetFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            formatEqual,
            formatIn,
            statusEqual,
            statusIn,
            statusNotIn)

        # @var string
        self.tagsLike = tagsLike

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var string
        self.contentLike = contentLike

        # @var string
        self.contentMultiLikeOr = contentMultiLikeOr

        # @var string
        self.contentMultiLikeAnd = contentMultiLikeAnd

        # @var string
        self.partnerDescriptionLike = partnerDescriptionLike

        # @var string
        self.partnerDescriptionMultiLikeOr = partnerDescriptionMultiLikeOr

        # @var string
        self.partnerDescriptionMultiLikeAnd = partnerDescriptionMultiLikeAnd

        # @var KalturaLanguage
        self.languageEqual = languageEqual

        # @var string
        self.languageIn = languageIn

        # @var string
        self.labelEqual = labelEqual

        # @var string
        self.labelIn = labelIn

        # @var int
        self.startTimeGreaterThanOrEqual = startTimeGreaterThanOrEqual

        # @var int
        self.startTimeLessThanOrEqual = startTimeLessThanOrEqual

        # @var int
        self.endTimeGreaterThanOrEqual = endTimeGreaterThanOrEqual

        # @var int
        self.endTimeLessThanOrEqual = endTimeLessThanOrEqual


    PROPERTY_LOADERS = {
        'tagsLike': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'contentLike': getXmlNodeText, 
        'contentMultiLikeOr': getXmlNodeText, 
        'contentMultiLikeAnd': getXmlNodeText, 
        'partnerDescriptionLike': getXmlNodeText, 
        'partnerDescriptionMultiLikeOr': getXmlNodeText, 
        'partnerDescriptionMultiLikeAnd': getXmlNodeText, 
        'languageEqual': (KalturaEnumsFactory.createString, "KalturaLanguage"), 
        'languageIn': getXmlNodeText, 
        'labelEqual': getXmlNodeText, 
        'labelIn': getXmlNodeText, 
        'startTimeGreaterThanOrEqual': getXmlNodeInt, 
        'startTimeLessThanOrEqual': getXmlNodeInt, 
        'endTimeGreaterThanOrEqual': getXmlNodeInt, 
        'endTimeLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaCaptionAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCaptionAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetItemFilter")
        kparams.addStringIfDefined("tagsLike", self.tagsLike)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addStringIfDefined("contentLike", self.contentLike)
        kparams.addStringIfDefined("contentMultiLikeOr", self.contentMultiLikeOr)
        kparams.addStringIfDefined("contentMultiLikeAnd", self.contentMultiLikeAnd)
        kparams.addStringIfDefined("partnerDescriptionLike", self.partnerDescriptionLike)
        kparams.addStringIfDefined("partnerDescriptionMultiLikeOr", self.partnerDescriptionMultiLikeOr)
        kparams.addStringIfDefined("partnerDescriptionMultiLikeAnd", self.partnerDescriptionMultiLikeAnd)
        kparams.addStringEnumIfDefined("languageEqual", self.languageEqual)
        kparams.addStringIfDefined("languageIn", self.languageIn)
        kparams.addStringIfDefined("labelEqual", self.labelEqual)
        kparams.addStringIfDefined("labelIn", self.labelIn)
        kparams.addIntIfDefined("startTimeGreaterThanOrEqual", self.startTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("startTimeLessThanOrEqual", self.startTimeLessThanOrEqual)
        kparams.addIntIfDefined("endTimeGreaterThanOrEqual", self.endTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("endTimeLessThanOrEqual", self.endTimeLessThanOrEqual)
        return kparams

    def getTagsLike(self):
        return self.tagsLike

    def setTagsLike(self, newTagsLike):
        self.tagsLike = newTagsLike

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getContentLike(self):
        return self.contentLike

    def setContentLike(self, newContentLike):
        self.contentLike = newContentLike

    def getContentMultiLikeOr(self):
        return self.contentMultiLikeOr

    def setContentMultiLikeOr(self, newContentMultiLikeOr):
        self.contentMultiLikeOr = newContentMultiLikeOr

    def getContentMultiLikeAnd(self):
        return self.contentMultiLikeAnd

    def setContentMultiLikeAnd(self, newContentMultiLikeAnd):
        self.contentMultiLikeAnd = newContentMultiLikeAnd

    def getPartnerDescriptionLike(self):
        return self.partnerDescriptionLike

    def setPartnerDescriptionLike(self, newPartnerDescriptionLike):
        self.partnerDescriptionLike = newPartnerDescriptionLike

    def getPartnerDescriptionMultiLikeOr(self):
        return self.partnerDescriptionMultiLikeOr

    def setPartnerDescriptionMultiLikeOr(self, newPartnerDescriptionMultiLikeOr):
        self.partnerDescriptionMultiLikeOr = newPartnerDescriptionMultiLikeOr

    def getPartnerDescriptionMultiLikeAnd(self):
        return self.partnerDescriptionMultiLikeAnd

    def setPartnerDescriptionMultiLikeAnd(self, newPartnerDescriptionMultiLikeAnd):
        self.partnerDescriptionMultiLikeAnd = newPartnerDescriptionMultiLikeAnd

    def getLanguageEqual(self):
        return self.languageEqual

    def setLanguageEqual(self, newLanguageEqual):
        self.languageEqual = newLanguageEqual

    def getLanguageIn(self):
        return self.languageIn

    def setLanguageIn(self, newLanguageIn):
        self.languageIn = newLanguageIn

    def getLabelEqual(self):
        return self.labelEqual

    def setLabelEqual(self, newLabelEqual):
        self.labelEqual = newLabelEqual

    def getLabelIn(self):
        return self.labelIn

    def setLabelIn(self, newLabelIn):
        self.labelIn = newLabelIn

    def getStartTimeGreaterThanOrEqual(self):
        return self.startTimeGreaterThanOrEqual

    def setStartTimeGreaterThanOrEqual(self, newStartTimeGreaterThanOrEqual):
        self.startTimeGreaterThanOrEqual = newStartTimeGreaterThanOrEqual

    def getStartTimeLessThanOrEqual(self):
        return self.startTimeLessThanOrEqual

    def setStartTimeLessThanOrEqual(self, newStartTimeLessThanOrEqual):
        self.startTimeLessThanOrEqual = newStartTimeLessThanOrEqual

    def getEndTimeGreaterThanOrEqual(self):
        return self.endTimeGreaterThanOrEqual

    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual):
        self.endTimeGreaterThanOrEqual = newEndTimeGreaterThanOrEqual

    def getEndTimeLessThanOrEqual(self):
        return self.endTimeLessThanOrEqual

    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual):
        self.endTimeLessThanOrEqual = newEndTimeLessThanOrEqual


class KalturaCaptionAssetItem(KalturaObjectBase):
    def __init__(self,
            asset=NotImplemented,
            entry=NotImplemented,
            startTime=NotImplemented,
            endTime=NotImplemented,
            content=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The Caption Asset object
        # @var KalturaCaptionAsset
        self.asset = asset

        # The entry object
        # @var KalturaBaseEntry
        self.entry = entry

        # @var int
        self.startTime = startTime

        # @var int
        self.endTime = endTime

        # @var string
        self.content = content


    PROPERTY_LOADERS = {
        'asset': (KalturaObjectFactory.create, KalturaCaptionAsset), 
        'entry': (KalturaObjectFactory.create, KalturaBaseEntry), 
        'startTime': getXmlNodeInt, 
        'endTime': getXmlNodeInt, 
        'content': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetItem")
        kparams.addObjectIfDefined("asset", self.asset)
        kparams.addObjectIfDefined("entry", self.entry)
        kparams.addIntIfDefined("startTime", self.startTime)
        kparams.addIntIfDefined("endTime", self.endTime)
        kparams.addStringIfDefined("content", self.content)
        return kparams

    def getAsset(self):
        return self.asset

    def setAsset(self, newAsset):
        self.asset = newAsset

    def getEntry(self):
        return self.entry

    def setEntry(self, newEntry):
        self.entry = newEntry

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getContent(self):
        return self.content

    def setContent(self, newContent):
        self.content = newContent


class KalturaCaptionAssetItemListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaCaptionAssetItem
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaCaptionAssetItem), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetItemListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetItemListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaCaptionAssetItemService(KalturaServiceBase):
    """Search caption asset items"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def search(self, entryFilter = NotImplemented, captionAssetItemFilter = NotImplemented, captionAssetItemPager = NotImplemented):
        """Search caption asset items by filter, pager and free text"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("entryFilter", entryFilter)
        kparams.addObjectIfDefined("captionAssetItemFilter", captionAssetItemFilter)
        kparams.addObjectIfDefined("captionAssetItemPager", captionAssetItemPager)
        self.client.queueServiceActionCall("captionsearch_captionassetitem", "search", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCaptionAssetItemListResponse)

########## main ##########
class KalturaCaptionSearchClientPlugin(KalturaClientPlugin):
    # KalturaCaptionSearchClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaCaptionSearchClientPlugin
    @staticmethod
    def get(client):
        if KalturaCaptionSearchClientPlugin.instance == None:
            KalturaCaptionSearchClientPlugin.instance = KalturaCaptionSearchClientPlugin(client)
        return KalturaCaptionSearchClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'captionAssetItem': KalturaCaptionAssetItemService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaCaptionAssetItemFilter': KalturaCaptionAssetItemFilter,
            'KalturaCaptionAssetItem': KalturaCaptionAssetItem,
            'KalturaCaptionAssetItemListResponse': KalturaCaptionAssetItemListResponse,
        }

    # @return string
    def getName(self):
        return 'captionSearch'

