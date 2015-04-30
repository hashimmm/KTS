import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
class KalturaDistributionAction:
    SUBMIT = 1
    UPDATE = 2
    DELETE = 3
    FETCH_REPORT = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionErrorType:
    MISSING_FLAVOR = 1
    MISSING_THUMBNAIL = 2
    MISSING_METADATA = 3
    INVALID_DATA = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProfileActionStatus:
    DISABLED = 1
    AUTOMATIC = 2
    MANUAL = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProfileStatus:
    DISABLED = 1
    ENABLED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProtocol:
    FTP = 1
    SCP = 2
    SFTP = 3
    HTTP = 4
    HTTPS = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProviderOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDistributionProviderType:
    GENERIC = "1"
    SYNDICATION = "2"
    YOUTUBE_API = "youtubeApiDistribution.YOUTUBE_API"
    DAILYMOTION = "dailymotionDistribution.DAILYMOTION"
    MSN = "msnDistribution.MSN"
    VERIZON = "verizonDistribution.VERIZON"
    COMCAST = "comcastDistribution.COMCAST"
    YOUTUBE = "youTubeDistribution.YOUTUBE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryDistributionFlag:
    NONE = 0
    SUBMIT_REQUIRED = 1
    DELETE_REQUIRED = 2
    UPDATE_REQUIRED = 3
    ENABLE_REQUIRED = 4
    DISABLE_REQUIRED = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryDistributionOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    SUBMITTED_AT_ASC = "+submittedAt"
    SUBMITTED_AT_DESC = "-submittedAt"
    SUNRISE_ASC = "+sunrise"
    SUNRISE_DESC = "-sunrise"
    SUNSET_ASC = "+sunset"
    SUNSET_DESC = "-sunset"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryDistributionStatus:
    PENDING = 0
    QUEUED = 1
    READY = 2
    DELETED = 3
    SUBMITTING = 4
    UPDATING = 5
    DELETING = 6
    ERROR_SUBMITTING = 7
    ERROR_UPDATING = 8
    ERROR_DELETING = 9
    REMOVED = 10

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryDistributionSunStatus:
    BEFORE_SUNRISE = 1
    AFTER_SUNRISE = 2
    AFTER_SUNSET = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericDistributionProviderActionOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericDistributionProviderOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericDistributionProviderParser:
    XSL = 1
    XPATH = 2
    REGEX = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericDistributionProviderStatus:
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaDistributionThumbDimensions(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.width = None

        # @var int
        self.height = None


    PROPERTY_LOADERS = {
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionThumbDimensions.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionThumbDimensions")
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        return kparams

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight


class KalturaDistributionProfile(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Auto generated unique id
        # @var int
        # @readonly
        self.id = None

        # Profile creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Profile last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var KalturaDistributionProviderType
        # @insertonly
        self.providerType = None

        # @var string
        self.name = None

        # @var KalturaDistributionProfileStatus
        self.status = None

        # @var KalturaDistributionProfileActionStatus
        self.submitEnabled = None

        # @var KalturaDistributionProfileActionStatus
        self.updateEnabled = None

        # @var KalturaDistributionProfileActionStatus
        self.deleteEnabled = None

        # @var KalturaDistributionProfileActionStatus
        self.reportEnabled = None

        # Comma separated flavor params ids that should be auto converted
        # @var string
        self.autoCreateFlavors = None

        # Comma separated thumbnail params ids that should be auto generated
        # @var string
        self.autoCreateThumb = None

        # Comma separated flavor params ids that should be submitted if ready
        # @var string
        self.optionalFlavorParamsIds = None

        # Comma separated flavor params ids that required to be readt before submission
        # @var string
        self.requiredFlavorParamsIds = None

        # Thumbnail dimensions that should be submitted if ready
        # @var array of KalturaDistributionThumbDimensions
        self.optionalThumbDimensions = None

        # Thumbnail dimensions that required to be readt before submission
        # @var array of KalturaDistributionThumbDimensions
        self.requiredThumbDimensions = None

        # If entry distribution sunrise not specified that will be the default since entry creation time, in seconds
        # @var int
        self.sunriseDefaultOffset = None

        # If entry distribution sunset not specified that will be the default since entry creation time, in seconds
        # @var int
        self.sunsetDefaultOffset = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'providerType': (KalturaEnumsFactory.createString, "KalturaDistributionProviderType"), 
        'name': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileStatus"), 
        'submitEnabled': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileActionStatus"), 
        'updateEnabled': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileActionStatus"), 
        'deleteEnabled': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileActionStatus"), 
        'reportEnabled': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileActionStatus"), 
        'autoCreateFlavors': getXmlNodeText, 
        'autoCreateThumb': getXmlNodeText, 
        'optionalFlavorParamsIds': getXmlNodeText, 
        'requiredFlavorParamsIds': getXmlNodeText, 
        'optionalThumbDimensions': (KalturaObjectFactory.createArray, KalturaDistributionThumbDimensions), 
        'requiredThumbDimensions': (KalturaObjectFactory.createArray, KalturaDistributionThumbDimensions), 
        'sunriseDefaultOffset': getXmlNodeInt, 
        'sunsetDefaultOffset': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionProfile")
        kparams.addStringEnumIfNotNone("providerType", self.providerType)
        kparams.addStringIfNotNone("name", self.name)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addIntEnumIfNotNone("submitEnabled", self.submitEnabled)
        kparams.addIntEnumIfNotNone("updateEnabled", self.updateEnabled)
        kparams.addIntEnumIfNotNone("deleteEnabled", self.deleteEnabled)
        kparams.addIntEnumIfNotNone("reportEnabled", self.reportEnabled)
        kparams.addStringIfNotNone("autoCreateFlavors", self.autoCreateFlavors)
        kparams.addStringIfNotNone("autoCreateThumb", self.autoCreateThumb)
        kparams.addStringIfNotNone("optionalFlavorParamsIds", self.optionalFlavorParamsIds)
        kparams.addStringIfNotNone("requiredFlavorParamsIds", self.requiredFlavorParamsIds)
        kparams.addObjectIfNotNone("optionalThumbDimensions", self.optionalThumbDimensions)
        kparams.addObjectIfNotNone("requiredThumbDimensions", self.requiredThumbDimensions)
        kparams.addIntIfNotNone("sunriseDefaultOffset", self.sunriseDefaultOffset)
        kparams.addIntIfNotNone("sunsetDefaultOffset", self.sunsetDefaultOffset)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerId(self):
        return self.partnerId

    def getProviderType(self):
        return self.providerType

    def setProviderType(self, newProviderType):
        self.providerType = newProviderType

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getSubmitEnabled(self):
        return self.submitEnabled

    def setSubmitEnabled(self, newSubmitEnabled):
        self.submitEnabled = newSubmitEnabled

    def getUpdateEnabled(self):
        return self.updateEnabled

    def setUpdateEnabled(self, newUpdateEnabled):
        self.updateEnabled = newUpdateEnabled

    def getDeleteEnabled(self):
        return self.deleteEnabled

    def setDeleteEnabled(self, newDeleteEnabled):
        self.deleteEnabled = newDeleteEnabled

    def getReportEnabled(self):
        return self.reportEnabled

    def setReportEnabled(self, newReportEnabled):
        self.reportEnabled = newReportEnabled

    def getAutoCreateFlavors(self):
        return self.autoCreateFlavors

    def setAutoCreateFlavors(self, newAutoCreateFlavors):
        self.autoCreateFlavors = newAutoCreateFlavors

    def getAutoCreateThumb(self):
        return self.autoCreateThumb

    def setAutoCreateThumb(self, newAutoCreateThumb):
        self.autoCreateThumb = newAutoCreateThumb

    def getOptionalFlavorParamsIds(self):
        return self.optionalFlavorParamsIds

    def setOptionalFlavorParamsIds(self, newOptionalFlavorParamsIds):
        self.optionalFlavorParamsIds = newOptionalFlavorParamsIds

    def getRequiredFlavorParamsIds(self):
        return self.requiredFlavorParamsIds

    def setRequiredFlavorParamsIds(self, newRequiredFlavorParamsIds):
        self.requiredFlavorParamsIds = newRequiredFlavorParamsIds

    def getOptionalThumbDimensions(self):
        return self.optionalThumbDimensions

    def setOptionalThumbDimensions(self, newOptionalThumbDimensions):
        self.optionalThumbDimensions = newOptionalThumbDimensions

    def getRequiredThumbDimensions(self):
        return self.requiredThumbDimensions

    def setRequiredThumbDimensions(self, newRequiredThumbDimensions):
        self.requiredThumbDimensions = newRequiredThumbDimensions

    def getSunriseDefaultOffset(self):
        return self.sunriseDefaultOffset

    def setSunriseDefaultOffset(self, newSunriseDefaultOffset):
        self.sunriseDefaultOffset = newSunriseDefaultOffset

    def getSunsetDefaultOffset(self):
        return self.sunsetDefaultOffset

    def setSunsetDefaultOffset(self, newSunsetDefaultOffset):
        self.sunsetDefaultOffset = newSunsetDefaultOffset


class KalturaDistributionProfileBaseFilter(KalturaFilter):
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

        # @var KalturaDistributionProfileStatus
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
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaDistributionProfileStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaDistributionProfileBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
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

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaDistributionProfileFilter(KalturaDistributionProfileBaseFilter):
    def __init__(self):
        KalturaDistributionProfileBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDistributionProfileFilter")
        return kparams


class KalturaDistributionProfileListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDistributionProfile
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDistributionProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDistributionValidationError(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var KalturaDistributionAction
        self.action = None

        # @var KalturaDistributionErrorType
        self.errorType = None

        # @var string
        self.description = None


    PROPERTY_LOADERS = {
        'action': (KalturaEnumsFactory.createInt, "KalturaDistributionAction"), 
        'errorType': (KalturaEnumsFactory.createInt, "KalturaDistributionErrorType"), 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionValidationError.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionValidationError")
        kparams.addIntEnumIfNotNone("action", self.action)
        kparams.addIntEnumIfNotNone("errorType", self.errorType)
        kparams.addStringIfNotNone("description", self.description)
        return kparams

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getErrorType(self):
        return self.errorType

    def setErrorType(self, newErrorType):
        self.errorType = newErrorType

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


class KalturaEntryDistribution(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Auto generated unique id
        # @var int
        # @readonly
        self.id = None

        # Entry distribution creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Entry distribution last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # Entry distribution submission date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.submittedAt = None

        # @var string
        # @insertonly
        self.entryId = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var int
        # @insertonly
        self.distributionProfileId = None

        # @var KalturaEntryDistributionStatus
        # @readonly
        self.status = None

        # @var KalturaEntryDistributionSunStatus
        # @readonly
        self.sunStatus = None

        # @var KalturaEntryDistributionFlag
        # @readonly
        self.dirtyStatus = None

        # Comma separated thumbnail asset ids
        # @var string
        self.thumbAssetIds = None

        # Comma separated flavor asset ids
        # @var string
        self.flavorAssetIds = None

        # Entry distribution publish time as Unix timestamp (In seconds)
        # @var int
        self.sunrise = None

        # Entry distribution un-publish time as Unix timestamp (In seconds)
        # @var int
        self.sunset = None

        # The id as returned from the distributed destination
        # @var string
        # @readonly
        self.remoteId = None

        # The plays as retrieved from the remote destination reports
        # @var int
        # @readonly
        self.plays = None

        # The views as retrieved from the remote destination reports
        # @var int
        # @readonly
        self.views = None

        # @var array of KalturaDistributionValidationError
        # @readonly
        self.validationErrors = None

        # @var KalturaBatchJobErrorTypes
        # @readonly
        self.errorType = None

        # @var int
        # @readonly
        self.errorNumber = None

        # @var string
        # @readonly
        self.errorDescription = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasSubmitResultsLog = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasSubmitSentDataLog = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasUpdateResultsLog = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasUpdateSentDataLog = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasDeleteResultsLog = None

        # @var KalturaNullableBoolean
        # @readonly
        self.hasDeleteSentDataLog = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'submittedAt': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'distributionProfileId': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaEntryDistributionStatus"), 
        'sunStatus': (KalturaEnumsFactory.createInt, "KalturaEntryDistributionSunStatus"), 
        'dirtyStatus': (KalturaEnumsFactory.createInt, "KalturaEntryDistributionFlag"), 
        'thumbAssetIds': getXmlNodeText, 
        'flavorAssetIds': getXmlNodeText, 
        'sunrise': getXmlNodeInt, 
        'sunset': getXmlNodeInt, 
        'remoteId': getXmlNodeText, 
        'plays': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'validationErrors': (KalturaObjectFactory.createArray, KalturaDistributionValidationError), 
        'errorType': (KalturaEnumsFactory.createInt, "KalturaBatchJobErrorTypes"), 
        'errorNumber': getXmlNodeInt, 
        'errorDescription': getXmlNodeText, 
        'hasSubmitResultsLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'hasSubmitSentDataLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'hasUpdateResultsLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'hasUpdateSentDataLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'hasDeleteResultsLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'hasDeleteSentDataLog': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryDistribution.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryDistribution")
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addIntIfNotNone("distributionProfileId", self.distributionProfileId)
        kparams.addStringIfNotNone("thumbAssetIds", self.thumbAssetIds)
        kparams.addStringIfNotNone("flavorAssetIds", self.flavorAssetIds)
        kparams.addIntIfNotNone("sunrise", self.sunrise)
        kparams.addIntIfNotNone("sunset", self.sunset)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getSubmittedAt(self):
        return self.submittedAt

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getPartnerId(self):
        return self.partnerId

    def getDistributionProfileId(self):
        return self.distributionProfileId

    def setDistributionProfileId(self, newDistributionProfileId):
        self.distributionProfileId = newDistributionProfileId

    def getStatus(self):
        return self.status

    def getSunStatus(self):
        return self.sunStatus

    def getDirtyStatus(self):
        return self.dirtyStatus

    def getThumbAssetIds(self):
        return self.thumbAssetIds

    def setThumbAssetIds(self, newThumbAssetIds):
        self.thumbAssetIds = newThumbAssetIds

    def getFlavorAssetIds(self):
        return self.flavorAssetIds

    def setFlavorAssetIds(self, newFlavorAssetIds):
        self.flavorAssetIds = newFlavorAssetIds

    def getSunrise(self):
        return self.sunrise

    def setSunrise(self, newSunrise):
        self.sunrise = newSunrise

    def getSunset(self):
        return self.sunset

    def setSunset(self, newSunset):
        self.sunset = newSunset

    def getRemoteId(self):
        return self.remoteId

    def getPlays(self):
        return self.plays

    def getViews(self):
        return self.views

    def getValidationErrors(self):
        return self.validationErrors

    def getErrorType(self):
        return self.errorType

    def getErrorNumber(self):
        return self.errorNumber

    def getErrorDescription(self):
        return self.errorDescription

    def getHasSubmitResultsLog(self):
        return self.hasSubmitResultsLog

    def getHasSubmitSentDataLog(self):
        return self.hasSubmitSentDataLog

    def getHasUpdateResultsLog(self):
        return self.hasUpdateResultsLog

    def getHasUpdateSentDataLog(self):
        return self.hasUpdateSentDataLog

    def getHasDeleteResultsLog(self):
        return self.hasDeleteResultsLog

    def getHasDeleteSentDataLog(self):
        return self.hasDeleteSentDataLog


class KalturaEntryDistributionBaseFilter(KalturaFilter):
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
        self.submittedAtGreaterThanOrEqual = None

        # @var int
        self.submittedAtLessThanOrEqual = None

        # @var string
        self.entryIdEqual = None

        # @var string
        self.entryIdIn = None

        # @var int
        self.distributionProfileIdEqual = None

        # @var string
        self.distributionProfileIdIn = None

        # @var KalturaEntryDistributionStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var KalturaEntryDistributionFlag
        self.dirtyStatusEqual = None

        # @var string
        self.dirtyStatusIn = None

        # @var int
        self.sunriseGreaterThanOrEqual = None

        # @var int
        self.sunriseLessThanOrEqual = None

        # @var int
        self.sunsetGreaterThanOrEqual = None

        # @var int
        self.sunsetLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'submittedAtGreaterThanOrEqual': getXmlNodeInt, 
        'submittedAtLessThanOrEqual': getXmlNodeInt, 
        'entryIdEqual': getXmlNodeText, 
        'entryIdIn': getXmlNodeText, 
        'distributionProfileIdEqual': getXmlNodeInt, 
        'distributionProfileIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaEntryDistributionStatus"), 
        'statusIn': getXmlNodeText, 
        'dirtyStatusEqual': (KalturaEnumsFactory.createInt, "KalturaEntryDistributionFlag"), 
        'dirtyStatusIn': getXmlNodeText, 
        'sunriseGreaterThanOrEqual': getXmlNodeInt, 
        'sunriseLessThanOrEqual': getXmlNodeInt, 
        'sunsetGreaterThanOrEqual': getXmlNodeInt, 
        'sunsetLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryDistributionBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaEntryDistributionBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("submittedAtGreaterThanOrEqual", self.submittedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("submittedAtLessThanOrEqual", self.submittedAtLessThanOrEqual)
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfNotNone("entryIdIn", self.entryIdIn)
        kparams.addIntIfNotNone("distributionProfileIdEqual", self.distributionProfileIdEqual)
        kparams.addStringIfNotNone("distributionProfileIdIn", self.distributionProfileIdIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addIntEnumIfNotNone("dirtyStatusEqual", self.dirtyStatusEqual)
        kparams.addStringIfNotNone("dirtyStatusIn", self.dirtyStatusIn)
        kparams.addIntIfNotNone("sunriseGreaterThanOrEqual", self.sunriseGreaterThanOrEqual)
        kparams.addIntIfNotNone("sunriseLessThanOrEqual", self.sunriseLessThanOrEqual)
        kparams.addIntIfNotNone("sunsetGreaterThanOrEqual", self.sunsetGreaterThanOrEqual)
        kparams.addIntIfNotNone("sunsetLessThanOrEqual", self.sunsetLessThanOrEqual)
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

    def getSubmittedAtGreaterThanOrEqual(self):
        return self.submittedAtGreaterThanOrEqual

    def setSubmittedAtGreaterThanOrEqual(self, newSubmittedAtGreaterThanOrEqual):
        self.submittedAtGreaterThanOrEqual = newSubmittedAtGreaterThanOrEqual

    def getSubmittedAtLessThanOrEqual(self):
        return self.submittedAtLessThanOrEqual

    def setSubmittedAtLessThanOrEqual(self, newSubmittedAtLessThanOrEqual):
        self.submittedAtLessThanOrEqual = newSubmittedAtLessThanOrEqual

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getEntryIdIn(self):
        return self.entryIdIn

    def setEntryIdIn(self, newEntryIdIn):
        self.entryIdIn = newEntryIdIn

    def getDistributionProfileIdEqual(self):
        return self.distributionProfileIdEqual

    def setDistributionProfileIdEqual(self, newDistributionProfileIdEqual):
        self.distributionProfileIdEqual = newDistributionProfileIdEqual

    def getDistributionProfileIdIn(self):
        return self.distributionProfileIdIn

    def setDistributionProfileIdIn(self, newDistributionProfileIdIn):
        self.distributionProfileIdIn = newDistributionProfileIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getDirtyStatusEqual(self):
        return self.dirtyStatusEqual

    def setDirtyStatusEqual(self, newDirtyStatusEqual):
        self.dirtyStatusEqual = newDirtyStatusEqual

    def getDirtyStatusIn(self):
        return self.dirtyStatusIn

    def setDirtyStatusIn(self, newDirtyStatusIn):
        self.dirtyStatusIn = newDirtyStatusIn

    def getSunriseGreaterThanOrEqual(self):
        return self.sunriseGreaterThanOrEqual

    def setSunriseGreaterThanOrEqual(self, newSunriseGreaterThanOrEqual):
        self.sunriseGreaterThanOrEqual = newSunriseGreaterThanOrEqual

    def getSunriseLessThanOrEqual(self):
        return self.sunriseLessThanOrEqual

    def setSunriseLessThanOrEqual(self, newSunriseLessThanOrEqual):
        self.sunriseLessThanOrEqual = newSunriseLessThanOrEqual

    def getSunsetGreaterThanOrEqual(self):
        return self.sunsetGreaterThanOrEqual

    def setSunsetGreaterThanOrEqual(self, newSunsetGreaterThanOrEqual):
        self.sunsetGreaterThanOrEqual = newSunsetGreaterThanOrEqual

    def getSunsetLessThanOrEqual(self):
        return self.sunsetLessThanOrEqual

    def setSunsetLessThanOrEqual(self, newSunsetLessThanOrEqual):
        self.sunsetLessThanOrEqual = newSunsetLessThanOrEqual


class KalturaEntryDistributionFilter(KalturaEntryDistributionBaseFilter):
    def __init__(self):
        KalturaEntryDistributionBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEntryDistributionBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryDistributionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryDistributionBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaEntryDistributionFilter")
        return kparams


class KalturaEntryDistributionListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaEntryDistribution
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaEntryDistribution), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryDistributionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryDistributionListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDistributionProviderBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var KalturaDistributionProviderType
        self.typeEqual = None

        # @var string
        self.typeIn = None


    PROPERTY_LOADERS = {
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaDistributionProviderType"), 
        'typeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaDistributionProviderBaseFilter")
        kparams.addStringEnumIfNotNone("typeEqual", self.typeEqual)
        kparams.addStringIfNotNone("typeIn", self.typeIn)
        return kparams

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn


class KalturaDistributionProviderFilter(KalturaDistributionProviderBaseFilter):
    def __init__(self):
        KalturaDistributionProviderBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDistributionProviderFilter")
        return kparams


class KalturaDistributionProvider(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var KalturaDistributionProviderType
        # @readonly
        self.type = None

        # @var string
        self.name = None

        # @var bool
        self.scheduleUpdateEnabled = None

        # @var bool
        self.availabilityUpdateEnabled = None

        # @var bool
        self.deleteInsteadUpdate = None

        # @var int
        self.intervalBeforeSunrise = None

        # @var int
        self.intervalBeforeSunset = None

        # @var string
        self.updateRequiredEntryFields = None

        # @var string
        self.updateRequiredMetadataXPaths = None


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaDistributionProviderType"), 
        'name': getXmlNodeText, 
        'scheduleUpdateEnabled': getXmlNodeBool, 
        'availabilityUpdateEnabled': getXmlNodeBool, 
        'deleteInsteadUpdate': getXmlNodeBool, 
        'intervalBeforeSunrise': getXmlNodeInt, 
        'intervalBeforeSunset': getXmlNodeInt, 
        'updateRequiredEntryFields': getXmlNodeText, 
        'updateRequiredMetadataXPaths': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionProvider")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addBoolIfNotNone("scheduleUpdateEnabled", self.scheduleUpdateEnabled)
        kparams.addBoolIfNotNone("availabilityUpdateEnabled", self.availabilityUpdateEnabled)
        kparams.addBoolIfNotNone("deleteInsteadUpdate", self.deleteInsteadUpdate)
        kparams.addIntIfNotNone("intervalBeforeSunrise", self.intervalBeforeSunrise)
        kparams.addIntIfNotNone("intervalBeforeSunset", self.intervalBeforeSunset)
        kparams.addStringIfNotNone("updateRequiredEntryFields", self.updateRequiredEntryFields)
        kparams.addStringIfNotNone("updateRequiredMetadataXPaths", self.updateRequiredMetadataXPaths)
        return kparams

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getScheduleUpdateEnabled(self):
        return self.scheduleUpdateEnabled

    def setScheduleUpdateEnabled(self, newScheduleUpdateEnabled):
        self.scheduleUpdateEnabled = newScheduleUpdateEnabled

    def getAvailabilityUpdateEnabled(self):
        return self.availabilityUpdateEnabled

    def setAvailabilityUpdateEnabled(self, newAvailabilityUpdateEnabled):
        self.availabilityUpdateEnabled = newAvailabilityUpdateEnabled

    def getDeleteInsteadUpdate(self):
        return self.deleteInsteadUpdate

    def setDeleteInsteadUpdate(self, newDeleteInsteadUpdate):
        self.deleteInsteadUpdate = newDeleteInsteadUpdate

    def getIntervalBeforeSunrise(self):
        return self.intervalBeforeSunrise

    def setIntervalBeforeSunrise(self, newIntervalBeforeSunrise):
        self.intervalBeforeSunrise = newIntervalBeforeSunrise

    def getIntervalBeforeSunset(self):
        return self.intervalBeforeSunset

    def setIntervalBeforeSunset(self, newIntervalBeforeSunset):
        self.intervalBeforeSunset = newIntervalBeforeSunset

    def getUpdateRequiredEntryFields(self):
        return self.updateRequiredEntryFields

    def setUpdateRequiredEntryFields(self, newUpdateRequiredEntryFields):
        self.updateRequiredEntryFields = newUpdateRequiredEntryFields

    def getUpdateRequiredMetadataXPaths(self):
        return self.updateRequiredMetadataXPaths

    def setUpdateRequiredMetadataXPaths(self, newUpdateRequiredMetadataXPaths):
        self.updateRequiredMetadataXPaths = newUpdateRequiredMetadataXPaths


class KalturaDistributionProviderListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDistributionProvider
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDistributionProvider), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDistributionProviderListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDistributionProviderListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaGenericDistributionProvider(KalturaDistributionProvider):
    def __init__(self):
        KalturaDistributionProvider.__init__(self)

        # Auto generated
        # @var int
        # @readonly
        self.id = None

        # Generic distribution provider creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Generic distribution provider last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var bool
        self.isDefault = None

        # @var KalturaGenericDistributionProviderStatus
        # @readonly
        self.status = None

        # @var string
        self.optionalFlavorParamsIds = None

        # @var string
        self.requiredFlavorParamsIds = None

        # @var array of KalturaDistributionThumbDimensions
        self.optionalThumbDimensions = None

        # @var array of KalturaDistributionThumbDimensions
        self.requiredThumbDimensions = None

        # @var string
        self.editableFields = None

        # @var string
        self.mandatoryFields = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'isDefault': getXmlNodeBool, 
        'status': (KalturaEnumsFactory.createInt, "KalturaGenericDistributionProviderStatus"), 
        'optionalFlavorParamsIds': getXmlNodeText, 
        'requiredFlavorParamsIds': getXmlNodeText, 
        'optionalThumbDimensions': (KalturaObjectFactory.createArray, KalturaDistributionThumbDimensions), 
        'requiredThumbDimensions': (KalturaObjectFactory.createArray, KalturaDistributionThumbDimensions), 
        'editableFields': getXmlNodeText, 
        'mandatoryFields': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDistributionProvider.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProvider")
        kparams.addBoolIfNotNone("isDefault", self.isDefault)
        kparams.addStringIfNotNone("optionalFlavorParamsIds", self.optionalFlavorParamsIds)
        kparams.addStringIfNotNone("requiredFlavorParamsIds", self.requiredFlavorParamsIds)
        kparams.addObjectIfNotNone("optionalThumbDimensions", self.optionalThumbDimensions)
        kparams.addObjectIfNotNone("requiredThumbDimensions", self.requiredThumbDimensions)
        kparams.addStringIfNotNone("editableFields", self.editableFields)
        kparams.addStringIfNotNone("mandatoryFields", self.mandatoryFields)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerId(self):
        return self.partnerId

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getStatus(self):
        return self.status

    def getOptionalFlavorParamsIds(self):
        return self.optionalFlavorParamsIds

    def setOptionalFlavorParamsIds(self, newOptionalFlavorParamsIds):
        self.optionalFlavorParamsIds = newOptionalFlavorParamsIds

    def getRequiredFlavorParamsIds(self):
        return self.requiredFlavorParamsIds

    def setRequiredFlavorParamsIds(self, newRequiredFlavorParamsIds):
        self.requiredFlavorParamsIds = newRequiredFlavorParamsIds

    def getOptionalThumbDimensions(self):
        return self.optionalThumbDimensions

    def setOptionalThumbDimensions(self, newOptionalThumbDimensions):
        self.optionalThumbDimensions = newOptionalThumbDimensions

    def getRequiredThumbDimensions(self):
        return self.requiredThumbDimensions

    def setRequiredThumbDimensions(self, newRequiredThumbDimensions):
        self.requiredThumbDimensions = newRequiredThumbDimensions

    def getEditableFields(self):
        return self.editableFields

    def setEditableFields(self, newEditableFields):
        self.editableFields = newEditableFields

    def getMandatoryFields(self):
        return self.mandatoryFields

    def setMandatoryFields(self, newMandatoryFields):
        self.mandatoryFields = newMandatoryFields


class KalturaGenericDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self):
        KalturaDistributionProviderFilter.__init__(self)

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

        # @var bool
        self.isDefaultEqual = None

        # @var string
        self.isDefaultIn = None

        # @var KalturaGenericDistributionProviderStatus
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
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'isDefaultEqual': getXmlNodeBool, 
        'isDefaultIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaGenericDistributionProviderStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDistributionProviderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addBoolIfNotNone("isDefaultEqual", self.isDefaultEqual)
        kparams.addStringIfNotNone("isDefaultIn", self.isDefaultIn)
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

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getIsDefaultEqual(self):
        return self.isDefaultEqual

    def setIsDefaultEqual(self, newIsDefaultEqual):
        self.isDefaultEqual = newIsDefaultEqual

    def getIsDefaultIn(self):
        return self.isDefaultIn

    def setIsDefaultIn(self, newIsDefaultIn):
        self.isDefaultIn = newIsDefaultIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaGenericDistributionProviderFilter(KalturaGenericDistributionProviderBaseFilter):
    def __init__(self):
        KalturaGenericDistributionProviderBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderFilter")
        return kparams


class KalturaGenericDistributionProviderListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaGenericDistributionProvider
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaGenericDistributionProvider), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaGenericDistributionProviderAction(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Auto generated
        # @var int
        # @readonly
        self.id = None

        # Generic distribution provider action creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Generic distribution provider action last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # @var int
        # @insertonly
        self.genericDistributionProviderId = None

        # @var KalturaDistributionAction
        # @insertonly
        self.action = None

        # @var KalturaGenericDistributionProviderStatus
        # @readonly
        self.status = None

        # @var KalturaGenericDistributionProviderParser
        self.resultsParser = None

        # @var KalturaDistributionProtocol
        self.protocol = None

        # @var string
        self.serverAddress = None

        # @var string
        self.remotePath = None

        # @var string
        self.remoteUsername = None

        # @var string
        self.remotePassword = None

        # @var string
        self.editableFields = None

        # @var string
        self.mandatoryFields = None

        # @var string
        # @readonly
        self.mrssTransformer = None

        # @var string
        # @readonly
        self.mrssValidator = None

        # @var string
        # @readonly
        self.resultsTransformer = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'genericDistributionProviderId': getXmlNodeInt, 
        'action': (KalturaEnumsFactory.createInt, "KalturaDistributionAction"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaGenericDistributionProviderStatus"), 
        'resultsParser': (KalturaEnumsFactory.createInt, "KalturaGenericDistributionProviderParser"), 
        'protocol': (KalturaEnumsFactory.createInt, "KalturaDistributionProtocol"), 
        'serverAddress': getXmlNodeText, 
        'remotePath': getXmlNodeText, 
        'remoteUsername': getXmlNodeText, 
        'remotePassword': getXmlNodeText, 
        'editableFields': getXmlNodeText, 
        'mandatoryFields': getXmlNodeText, 
        'mrssTransformer': getXmlNodeText, 
        'mrssValidator': getXmlNodeText, 
        'resultsTransformer': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderAction")
        kparams.addIntIfNotNone("genericDistributionProviderId", self.genericDistributionProviderId)
        kparams.addIntEnumIfNotNone("action", self.action)
        kparams.addIntEnumIfNotNone("resultsParser", self.resultsParser)
        kparams.addIntEnumIfNotNone("protocol", self.protocol)
        kparams.addStringIfNotNone("serverAddress", self.serverAddress)
        kparams.addStringIfNotNone("remotePath", self.remotePath)
        kparams.addStringIfNotNone("remoteUsername", self.remoteUsername)
        kparams.addStringIfNotNone("remotePassword", self.remotePassword)
        kparams.addStringIfNotNone("editableFields", self.editableFields)
        kparams.addStringIfNotNone("mandatoryFields", self.mandatoryFields)
        return kparams

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getGenericDistributionProviderId(self):
        return self.genericDistributionProviderId

    def setGenericDistributionProviderId(self, newGenericDistributionProviderId):
        self.genericDistributionProviderId = newGenericDistributionProviderId

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getStatus(self):
        return self.status

    def getResultsParser(self):
        return self.resultsParser

    def setResultsParser(self, newResultsParser):
        self.resultsParser = newResultsParser

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, newProtocol):
        self.protocol = newProtocol

    def getServerAddress(self):
        return self.serverAddress

    def setServerAddress(self, newServerAddress):
        self.serverAddress = newServerAddress

    def getRemotePath(self):
        return self.remotePath

    def setRemotePath(self, newRemotePath):
        self.remotePath = newRemotePath

    def getRemoteUsername(self):
        return self.remoteUsername

    def setRemoteUsername(self, newRemoteUsername):
        self.remoteUsername = newRemoteUsername

    def getRemotePassword(self):
        return self.remotePassword

    def setRemotePassword(self, newRemotePassword):
        self.remotePassword = newRemotePassword

    def getEditableFields(self):
        return self.editableFields

    def setEditableFields(self, newEditableFields):
        self.editableFields = newEditableFields

    def getMandatoryFields(self):
        return self.mandatoryFields

    def setMandatoryFields(self, newMandatoryFields):
        self.mandatoryFields = newMandatoryFields

    def getMrssTransformer(self):
        return self.mrssTransformer

    def getMrssValidator(self):
        return self.mrssValidator

    def getResultsTransformer(self):
        return self.resultsTransformer


class KalturaGenericDistributionProviderActionBaseFilter(KalturaFilter):
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
        self.genericDistributionProviderIdEqual = None

        # @var string
        self.genericDistributionProviderIdIn = None

        # @var KalturaDistributionAction
        self.actionEqual = None

        # @var string
        self.actionIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'genericDistributionProviderIdEqual': getXmlNodeInt, 
        'genericDistributionProviderIdIn': getXmlNodeText, 
        'actionEqual': (KalturaEnumsFactory.createInt, "KalturaDistributionAction"), 
        'actionIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderActionBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderActionBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("genericDistributionProviderIdEqual", self.genericDistributionProviderIdEqual)
        kparams.addStringIfNotNone("genericDistributionProviderIdIn", self.genericDistributionProviderIdIn)
        kparams.addIntEnumIfNotNone("actionEqual", self.actionEqual)
        kparams.addStringIfNotNone("actionIn", self.actionIn)
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

    def getGenericDistributionProviderIdEqual(self):
        return self.genericDistributionProviderIdEqual

    def setGenericDistributionProviderIdEqual(self, newGenericDistributionProviderIdEqual):
        self.genericDistributionProviderIdEqual = newGenericDistributionProviderIdEqual

    def getGenericDistributionProviderIdIn(self):
        return self.genericDistributionProviderIdIn

    def setGenericDistributionProviderIdIn(self, newGenericDistributionProviderIdIn):
        self.genericDistributionProviderIdIn = newGenericDistributionProviderIdIn

    def getActionEqual(self):
        return self.actionEqual

    def setActionEqual(self, newActionEqual):
        self.actionEqual = newActionEqual

    def getActionIn(self):
        return self.actionIn

    def setActionIn(self, newActionIn):
        self.actionIn = newActionIn


class KalturaGenericDistributionProviderActionFilter(KalturaGenericDistributionProviderActionBaseFilter):
    def __init__(self):
        KalturaGenericDistributionProviderActionBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericDistributionProviderActionBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderActionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericDistributionProviderActionBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderActionFilter")
        return kparams


class KalturaGenericDistributionProviderActionListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaGenericDistributionProviderAction
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaGenericDistributionProviderAction), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericDistributionProviderActionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaGenericDistributionProviderActionListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


########## services ##########

class KalturaDistributionProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, distributionProfile):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("distributionProfile", distributionProfile)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfile)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfile)

    def update(self, id, distributionProfile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("distributionProfile", distributionProfile)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfile)

    def updateStatus(self, id, status):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("status", status)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfile)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfileListResponse)

    def listByPartner(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_distributionprofile", "listByPartner", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProfileListResponse)


class KalturaEntryDistributionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryDistribution):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("entryDistribution", entryDistribution)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def validate(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "validate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def update(self, id, entryDistribution):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("entryDistribution", entryDistribution)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistributionListResponse)

    def submitAdd(self, id, submitWhenReady = False):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("submitWhenReady", submitWhenReady)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "submitAdd", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def submitUpdate(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "submitUpdate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def submitFetchReport(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "submitFetchReport", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def submitDelete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "submitDelete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)

    def retrySubmit(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_entrydistribution", "retrySubmit", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryDistribution)


class KalturaDistributionProviderService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_distributionprovider", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDistributionProviderListResponse)


class KalturaGenericDistributionProviderService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, genericDistributionProvider):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("genericDistributionProvider", genericDistributionProvider)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovider", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProvider)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovider", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProvider)

    def update(self, id, genericDistributionProvider):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("genericDistributionProvider", genericDistributionProvider)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovider", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProvider)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovider", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovider", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderListResponse)


class KalturaGenericDistributionProviderActionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, genericDistributionProviderAction):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("genericDistributionProviderAction", genericDistributionProviderAction)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addMrssTransform(self, id, xslData):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("xslData", xslData)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addMrssTransform", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addMrssTransformFromFile(self, id, xslFile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("xslFile", xslFile)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addMrssTransformFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addMrssValidate(self, id, xsdData):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("xsdData", xsdData)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addMrssValidate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addMrssValidateFromFile(self, id, xsdFile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("xsdFile", xsdFile)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addMrssValidateFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addResultsTransform(self, id, transformData):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("transformData", transformData)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addResultsTransform", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def addResultsTransformFromFile(self, id, transformFile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kfiles = KalturaFiles()
        kfiles.put("transformFile", transformFile)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "addResultsTransformFromFile", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def getByProviderId(self, genericDistributionProviderId, actionType):
        kparams = KalturaParams()
        kparams.put("genericDistributionProviderId", genericDistributionProviderId)
        kparams.put("actionType", actionType)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "getByProviderId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def updateByProviderId(self, genericDistributionProviderId, actionType, genericDistributionProviderAction):
        kparams = KalturaParams()
        kparams.put("genericDistributionProviderId", genericDistributionProviderId)
        kparams.put("actionType", actionType)
        kparams.addObjectIfNotNone("genericDistributionProviderAction", genericDistributionProviderAction)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "updateByProviderId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def update(self, id, genericDistributionProviderAction):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("genericDistributionProviderAction", genericDistributionProviderAction)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderAction)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def deleteByProviderId(self, genericDistributionProviderId, actionType):
        kparams = KalturaParams()
        kparams.put("genericDistributionProviderId", genericDistributionProviderId)
        kparams.put("actionType", actionType)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "deleteByProviderId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("contentdistribution_genericdistributionprovideraction", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaGenericDistributionProviderActionListResponse)

########## main ##########
class KalturaContentDistributionClientPlugin(KalturaClientPlugin):
    # KalturaContentDistributionClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaContentDistributionClientPlugin
    @staticmethod
    def get(client):
        if KalturaContentDistributionClientPlugin.instance == None:
            KalturaContentDistributionClientPlugin.instance = KalturaContentDistributionClientPlugin(client)
        return KalturaContentDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'distributionProfile': KalturaDistributionProfileService,
            'entryDistribution': KalturaEntryDistributionService,
            'distributionProvider': KalturaDistributionProviderService,
            'genericDistributionProvider': KalturaGenericDistributionProviderService,
            'genericDistributionProviderAction': KalturaGenericDistributionProviderActionService,
        }

    def getEnums(self):
        return {
            'KalturaDistributionAction': KalturaDistributionAction,
            'KalturaDistributionErrorType': KalturaDistributionErrorType,
            'KalturaDistributionProfileActionStatus': KalturaDistributionProfileActionStatus,
            'KalturaDistributionProfileOrderBy': KalturaDistributionProfileOrderBy,
            'KalturaDistributionProfileStatus': KalturaDistributionProfileStatus,
            'KalturaDistributionProtocol': KalturaDistributionProtocol,
            'KalturaDistributionProviderOrderBy': KalturaDistributionProviderOrderBy,
            'KalturaDistributionProviderType': KalturaDistributionProviderType,
            'KalturaEntryDistributionFlag': KalturaEntryDistributionFlag,
            'KalturaEntryDistributionOrderBy': KalturaEntryDistributionOrderBy,
            'KalturaEntryDistributionStatus': KalturaEntryDistributionStatus,
            'KalturaEntryDistributionSunStatus': KalturaEntryDistributionSunStatus,
            'KalturaGenericDistributionProviderActionOrderBy': KalturaGenericDistributionProviderActionOrderBy,
            'KalturaGenericDistributionProviderOrderBy': KalturaGenericDistributionProviderOrderBy,
            'KalturaGenericDistributionProviderParser': KalturaGenericDistributionProviderParser,
            'KalturaGenericDistributionProviderStatus': KalturaGenericDistributionProviderStatus,
        }

    def getTypes(self):
        return {
            'KalturaDistributionThumbDimensions': KalturaDistributionThumbDimensions,
            'KalturaDistributionProfile': KalturaDistributionProfile,
            'KalturaDistributionProfileBaseFilter': KalturaDistributionProfileBaseFilter,
            'KalturaDistributionProfileFilter': KalturaDistributionProfileFilter,
            'KalturaDistributionProfileListResponse': KalturaDistributionProfileListResponse,
            'KalturaDistributionValidationError': KalturaDistributionValidationError,
            'KalturaEntryDistribution': KalturaEntryDistribution,
            'KalturaEntryDistributionBaseFilter': KalturaEntryDistributionBaseFilter,
            'KalturaEntryDistributionFilter': KalturaEntryDistributionFilter,
            'KalturaEntryDistributionListResponse': KalturaEntryDistributionListResponse,
            'KalturaDistributionProviderBaseFilter': KalturaDistributionProviderBaseFilter,
            'KalturaDistributionProviderFilter': KalturaDistributionProviderFilter,
            'KalturaDistributionProvider': KalturaDistributionProvider,
            'KalturaDistributionProviderListResponse': KalturaDistributionProviderListResponse,
            'KalturaGenericDistributionProvider': KalturaGenericDistributionProvider,
            'KalturaGenericDistributionProviderBaseFilter': KalturaGenericDistributionProviderBaseFilter,
            'KalturaGenericDistributionProviderFilter': KalturaGenericDistributionProviderFilter,
            'KalturaGenericDistributionProviderListResponse': KalturaGenericDistributionProviderListResponse,
            'KalturaGenericDistributionProviderAction': KalturaGenericDistributionProviderAction,
            'KalturaGenericDistributionProviderActionBaseFilter': KalturaGenericDistributionProviderActionBaseFilter,
            'KalturaGenericDistributionProviderActionFilter': KalturaGenericDistributionProviderActionFilter,
            'KalturaGenericDistributionProviderActionListResponse': KalturaGenericDistributionProviderActionListResponse,
        }

    # @return string
    def getName(self):
        return 'contentDistribution'

