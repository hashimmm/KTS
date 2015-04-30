import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaClientBase import *

########## enums ##########
########## classes ##########
class KalturaSystemPartnerUsageFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # Date range from
        # @var int
        self.fromDate = None

        # Date range to
        # @var int
        self.toDate = None


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageFilter")
        kparams.addIntIfNotNone("fromDate", self.fromDate)
        kparams.addIntIfNotNone("toDate", self.toDate)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate


class KalturaSystemPartnerUsageItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Partner ID
        # @var int
        self.partnerId = None

        # Partner name
        # @var string
        self.partnerName = None

        # Partner status
        # @var KalturaPartnerStatus
        self.partnerStatus = None

        # Partner package
        # @var int
        self.partnerPackage = None

        # Partner creation date (Unix timestamp)
        # @var int
        self.partnerCreatedAt = None

        # Number of player loads in the specific date range
        # @var int
        self.views = None

        # Number of plays in the specific date range
        # @var int
        self.plays = None

        # Number of new entries created during specific date range
        # @var int
        self.entriesCount = None

        # Total number of entries
        # @var int
        self.totalEntriesCount = None

        # Number of new video entries created during specific date range
        # @var int
        self.videoEntriesCount = None

        # Number of new image entries created during specific date range
        # @var int
        self.imageEntriesCount = None

        # Number of new audio entries created during specific date range
        # @var int
        self.audioEntriesCount = None

        # Number of new mix entries created during specific date range
        # @var int
        self.mixEntriesCount = None

        # The total bandwidth usage during the given date range (in MB)
        # @var float
        self.bandwidth = None

        # The total storage consumption (in MB)
        # @var float
        self.totalStorage = None

        # The change in storage consumption (new uploads) during the given date range (in MB)
        # @var float
        self.storage = None


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'partnerStatus': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'partnerPackage': getXmlNodeInt, 
        'partnerCreatedAt': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'plays': getXmlNodeInt, 
        'entriesCount': getXmlNodeInt, 
        'totalEntriesCount': getXmlNodeInt, 
        'videoEntriesCount': getXmlNodeInt, 
        'imageEntriesCount': getXmlNodeInt, 
        'audioEntriesCount': getXmlNodeInt, 
        'mixEntriesCount': getXmlNodeInt, 
        'bandwidth': getXmlNodeFloat, 
        'totalStorage': getXmlNodeFloat, 
        'storage': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageItem")
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("partnerName", self.partnerName)
        kparams.addIntEnumIfNotNone("partnerStatus", self.partnerStatus)
        kparams.addIntIfNotNone("partnerPackage", self.partnerPackage)
        kparams.addIntIfNotNone("partnerCreatedAt", self.partnerCreatedAt)
        kparams.addIntIfNotNone("views", self.views)
        kparams.addIntIfNotNone("plays", self.plays)
        kparams.addIntIfNotNone("entriesCount", self.entriesCount)
        kparams.addIntIfNotNone("totalEntriesCount", self.totalEntriesCount)
        kparams.addIntIfNotNone("videoEntriesCount", self.videoEntriesCount)
        kparams.addIntIfNotNone("imageEntriesCount", self.imageEntriesCount)
        kparams.addIntIfNotNone("audioEntriesCount", self.audioEntriesCount)
        kparams.addIntIfNotNone("mixEntriesCount", self.mixEntriesCount)
        kparams.addFloatIfNotNone("bandwidth", self.bandwidth)
        kparams.addFloatIfNotNone("totalStorage", self.totalStorage)
        kparams.addFloatIfNotNone("storage", self.storage)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getPartnerStatus(self):
        return self.partnerStatus

    def setPartnerStatus(self, newPartnerStatus):
        self.partnerStatus = newPartnerStatus

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getPartnerCreatedAt(self):
        return self.partnerCreatedAt

    def setPartnerCreatedAt(self, newPartnerCreatedAt):
        self.partnerCreatedAt = newPartnerCreatedAt

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getPlays(self):
        return self.plays

    def setPlays(self, newPlays):
        self.plays = newPlays

    def getEntriesCount(self):
        return self.entriesCount

    def setEntriesCount(self, newEntriesCount):
        self.entriesCount = newEntriesCount

    def getTotalEntriesCount(self):
        return self.totalEntriesCount

    def setTotalEntriesCount(self, newTotalEntriesCount):
        self.totalEntriesCount = newTotalEntriesCount

    def getVideoEntriesCount(self):
        return self.videoEntriesCount

    def setVideoEntriesCount(self, newVideoEntriesCount):
        self.videoEntriesCount = newVideoEntriesCount

    def getImageEntriesCount(self):
        return self.imageEntriesCount

    def setImageEntriesCount(self, newImageEntriesCount):
        self.imageEntriesCount = newImageEntriesCount

    def getAudioEntriesCount(self):
        return self.audioEntriesCount

    def setAudioEntriesCount(self, newAudioEntriesCount):
        self.audioEntriesCount = newAudioEntriesCount

    def getMixEntriesCount(self):
        return self.mixEntriesCount

    def setMixEntriesCount(self, newMixEntriesCount):
        self.mixEntriesCount = newMixEntriesCount

    def getBandwidth(self):
        return self.bandwidth

    def setBandwidth(self, newBandwidth):
        self.bandwidth = newBandwidth

    def getTotalStorage(self):
        return self.totalStorage

    def setTotalStorage(self, newTotalStorage):
        self.totalStorage = newTotalStorage

    def getStorage(self):
        return self.storage

    def setStorage(self, newStorage):
        self.storage = newStorage


class KalturaSystemPartnerUsageListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaSystemPartnerUsageItem
        self.objects = None

        # @var int
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSystemPartnerUsageItem), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageListResponse")
        kparams.addObjectIfNotNone("objects", self.objects)
        kparams.addIntIfNotNone("totalCount", self.totalCount)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount


class KalturaSystemPartnerConfiguration(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.partnerName = None

        # @var string
        self.description = None

        # @var string
        self.adminName = None

        # @var string
        self.adminEmail = None

        # @var string
        self.host = None

        # @var string
        self.cdnHost = None

        # @var int
        self.maxBulkSize = None

        # @var int
        self.partnerPackage = None

        # @var int
        self.monitorUsage = None

        # @var bool
        self.liveStreamEnabled = None

        # @var bool
        self.moderateContent = None

        # @var string
        self.rtmpUrl = None

        # @var bool
        self.storageDeleteFromKaltura = None

        # @var KalturaStorageServePriority
        self.storageServePriority = None

        # @var int
        self.kmcVersion = None

        # @var bool
        self.enableAnalyticsTab = None

        # @var bool
        self.enableSilverLight = None

        # @var bool
        self.enableVast = None

        # @var bool
        self.enable508Players = None

        # @var bool
        self.enableMetadata = None

        # @var bool
        self.enableContentDistribution = None

        # @var bool
        self.enableAuditTrail = None

        # @var bool
        self.enableAnnotation = None

        # @var bool
        self.enableMobileFlavors = None

        # @var bool
        self.enablePs2PermissionValidation = None

        # @var int
        self.defThumbOffset = None

        # @var int
        self.adminLoginUsersQuota = None

        # @var int
        self.userSessionRoleId = None

        # @var int
        self.adminSessionRoleId = None

        # @var string
        self.alwaysAllowedPermissionNames = None


    PROPERTY_LOADERS = {
        'partnerName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'adminName': getXmlNodeText, 
        'adminEmail': getXmlNodeText, 
        'host': getXmlNodeText, 
        'cdnHost': getXmlNodeText, 
        'maxBulkSize': getXmlNodeInt, 
        'partnerPackage': getXmlNodeInt, 
        'monitorUsage': getXmlNodeInt, 
        'liveStreamEnabled': getXmlNodeBool, 
        'moderateContent': getXmlNodeBool, 
        'rtmpUrl': getXmlNodeText, 
        'storageDeleteFromKaltura': getXmlNodeBool, 
        'storageServePriority': (KalturaEnumsFactory.createInt, "KalturaStorageServePriority"), 
        'kmcVersion': getXmlNodeInt, 
        'enableAnalyticsTab': getXmlNodeBool, 
        'enableSilverLight': getXmlNodeBool, 
        'enableVast': getXmlNodeBool, 
        'enable508Players': getXmlNodeBool, 
        'enableMetadata': getXmlNodeBool, 
        'enableContentDistribution': getXmlNodeBool, 
        'enableAuditTrail': getXmlNodeBool, 
        'enableAnnotation': getXmlNodeBool, 
        'enableMobileFlavors': getXmlNodeBool, 
        'enablePs2PermissionValidation': getXmlNodeBool, 
        'defThumbOffset': getXmlNodeInt, 
        'adminLoginUsersQuota': getXmlNodeInt, 
        'userSessionRoleId': getXmlNodeInt, 
        'adminSessionRoleId': getXmlNodeInt, 
        'alwaysAllowedPermissionNames': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerConfiguration")
        kparams.addStringIfNotNone("partnerName", self.partnerName)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("adminName", self.adminName)
        kparams.addStringIfNotNone("adminEmail", self.adminEmail)
        kparams.addStringIfNotNone("host", self.host)
        kparams.addStringIfNotNone("cdnHost", self.cdnHost)
        kparams.addIntIfNotNone("maxBulkSize", self.maxBulkSize)
        kparams.addIntIfNotNone("partnerPackage", self.partnerPackage)
        kparams.addIntIfNotNone("monitorUsage", self.monitorUsage)
        kparams.addBoolIfNotNone("liveStreamEnabled", self.liveStreamEnabled)
        kparams.addBoolIfNotNone("moderateContent", self.moderateContent)
        kparams.addStringIfNotNone("rtmpUrl", self.rtmpUrl)
        kparams.addBoolIfNotNone("storageDeleteFromKaltura", self.storageDeleteFromKaltura)
        kparams.addIntEnumIfNotNone("storageServePriority", self.storageServePriority)
        kparams.addIntIfNotNone("kmcVersion", self.kmcVersion)
        kparams.addBoolIfNotNone("enableAnalyticsTab", self.enableAnalyticsTab)
        kparams.addBoolIfNotNone("enableSilverLight", self.enableSilverLight)
        kparams.addBoolIfNotNone("enableVast", self.enableVast)
        kparams.addBoolIfNotNone("enable508Players", self.enable508Players)
        kparams.addBoolIfNotNone("enableMetadata", self.enableMetadata)
        kparams.addBoolIfNotNone("enableContentDistribution", self.enableContentDistribution)
        kparams.addBoolIfNotNone("enableAuditTrail", self.enableAuditTrail)
        kparams.addBoolIfNotNone("enableAnnotation", self.enableAnnotation)
        kparams.addBoolIfNotNone("enableMobileFlavors", self.enableMobileFlavors)
        kparams.addBoolIfNotNone("enablePs2PermissionValidation", self.enablePs2PermissionValidation)
        kparams.addIntIfNotNone("defThumbOffset", self.defThumbOffset)
        kparams.addIntIfNotNone("adminLoginUsersQuota", self.adminLoginUsersQuota)
        kparams.addIntIfNotNone("userSessionRoleId", self.userSessionRoleId)
        kparams.addIntIfNotNone("adminSessionRoleId", self.adminSessionRoleId)
        kparams.addStringIfNotNone("alwaysAllowedPermissionNames", self.alwaysAllowedPermissionNames)
        return kparams

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getAdminName(self):
        return self.adminName

    def setAdminName(self, newAdminName):
        self.adminName = newAdminName

    def getAdminEmail(self):
        return self.adminEmail

    def setAdminEmail(self, newAdminEmail):
        self.adminEmail = newAdminEmail

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getCdnHost(self):
        return self.cdnHost

    def setCdnHost(self, newCdnHost):
        self.cdnHost = newCdnHost

    def getMaxBulkSize(self):
        return self.maxBulkSize

    def setMaxBulkSize(self, newMaxBulkSize):
        self.maxBulkSize = newMaxBulkSize

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getMonitorUsage(self):
        return self.monitorUsage

    def setMonitorUsage(self, newMonitorUsage):
        self.monitorUsage = newMonitorUsage

    def getLiveStreamEnabled(self):
        return self.liveStreamEnabled

    def setLiveStreamEnabled(self, newLiveStreamEnabled):
        self.liveStreamEnabled = newLiveStreamEnabled

    def getModerateContent(self):
        return self.moderateContent

    def setModerateContent(self, newModerateContent):
        self.moderateContent = newModerateContent

    def getRtmpUrl(self):
        return self.rtmpUrl

    def setRtmpUrl(self, newRtmpUrl):
        self.rtmpUrl = newRtmpUrl

    def getStorageDeleteFromKaltura(self):
        return self.storageDeleteFromKaltura

    def setStorageDeleteFromKaltura(self, newStorageDeleteFromKaltura):
        self.storageDeleteFromKaltura = newStorageDeleteFromKaltura

    def getStorageServePriority(self):
        return self.storageServePriority

    def setStorageServePriority(self, newStorageServePriority):
        self.storageServePriority = newStorageServePriority

    def getKmcVersion(self):
        return self.kmcVersion

    def setKmcVersion(self, newKmcVersion):
        self.kmcVersion = newKmcVersion

    def getEnableAnalyticsTab(self):
        return self.enableAnalyticsTab

    def setEnableAnalyticsTab(self, newEnableAnalyticsTab):
        self.enableAnalyticsTab = newEnableAnalyticsTab

    def getEnableSilverLight(self):
        return self.enableSilverLight

    def setEnableSilverLight(self, newEnableSilverLight):
        self.enableSilverLight = newEnableSilverLight

    def getEnableVast(self):
        return self.enableVast

    def setEnableVast(self, newEnableVast):
        self.enableVast = newEnableVast

    def getEnable508Players(self):
        return self.enable508Players

    def setEnable508Players(self, newEnable508Players):
        self.enable508Players = newEnable508Players

    def getEnableMetadata(self):
        return self.enableMetadata

    def setEnableMetadata(self, newEnableMetadata):
        self.enableMetadata = newEnableMetadata

    def getEnableContentDistribution(self):
        return self.enableContentDistribution

    def setEnableContentDistribution(self, newEnableContentDistribution):
        self.enableContentDistribution = newEnableContentDistribution

    def getEnableAuditTrail(self):
        return self.enableAuditTrail

    def setEnableAuditTrail(self, newEnableAuditTrail):
        self.enableAuditTrail = newEnableAuditTrail

    def getEnableAnnotation(self):
        return self.enableAnnotation

    def setEnableAnnotation(self, newEnableAnnotation):
        self.enableAnnotation = newEnableAnnotation

    def getEnableMobileFlavors(self):
        return self.enableMobileFlavors

    def setEnableMobileFlavors(self, newEnableMobileFlavors):
        self.enableMobileFlavors = newEnableMobileFlavors

    def getEnablePs2PermissionValidation(self):
        return self.enablePs2PermissionValidation

    def setEnablePs2PermissionValidation(self, newEnablePs2PermissionValidation):
        self.enablePs2PermissionValidation = newEnablePs2PermissionValidation

    def getDefThumbOffset(self):
        return self.defThumbOffset

    def setDefThumbOffset(self, newDefThumbOffset):
        self.defThumbOffset = newDefThumbOffset

    def getAdminLoginUsersQuota(self):
        return self.adminLoginUsersQuota

    def setAdminLoginUsersQuota(self, newAdminLoginUsersQuota):
        self.adminLoginUsersQuota = newAdminLoginUsersQuota

    def getUserSessionRoleId(self):
        return self.userSessionRoleId

    def setUserSessionRoleId(self, newUserSessionRoleId):
        self.userSessionRoleId = newUserSessionRoleId

    def getAdminSessionRoleId(self):
        return self.adminSessionRoleId

    def setAdminSessionRoleId(self, newAdminSessionRoleId):
        self.adminSessionRoleId = newAdminSessionRoleId

    def getAlwaysAllowedPermissionNames(self):
        return self.alwaysAllowedPermissionNames

    def setAlwaysAllowedPermissionNames(self, newAlwaysAllowedPermissionNames):
        self.alwaysAllowedPermissionNames = newAlwaysAllowedPermissionNames


class KalturaSystemPartnerPackage(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = None

        # @var string
        self.name = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerPackage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerPackage")
        kparams.addIntIfNotNone("id", self.id)
        kparams.addStringIfNotNone("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


########## services ##########

class KalturaSystemPartnerService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, partnerId):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        self.client.queueServiceActionCall("systempartner_systempartner", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getUsage(self, partnerFilter = None, usageFilter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("partnerFilter", partnerFilter)
        kparams.addObjectIfNotNone("usageFilter", usageFilter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "getUsage", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerUsageListResponse)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartnerListResponse)

    def updateStatus(self, partnerId, status):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        kparams.put("status", status)
        self.client.queueServiceActionCall("systempartner_systempartner", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getAdminSession(self, partnerId, userId = ""):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        kparams.put("userId", userId)
        self.client.queueServiceActionCall("systempartner_systempartner", "getAdminSession", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateConfiguration(self, partnerId, configuration):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        kparams.addObjectIfNotNone("configuration", configuration)
        self.client.queueServiceActionCall("systempartner_systempartner", "updateConfiguration", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getConfiguration(self, partnerId):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        self.client.queueServiceActionCall("systempartner_systempartner", "getConfiguration", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerConfiguration)

    def getPackages(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackages", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

########## main ##########
class KalturaSystemPartnerClientPlugin(KalturaClientPlugin):
    # KalturaSystemPartnerClientPlugin
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaSystemPartnerClientPlugin
    @staticmethod
    def get(client):
        if KalturaSystemPartnerClientPlugin.instance == None:
            KalturaSystemPartnerClientPlugin.instance = KalturaSystemPartnerClientPlugin(client)
        return KalturaSystemPartnerClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'systemPartner': KalturaSystemPartnerService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaSystemPartnerUsageFilter': KalturaSystemPartnerUsageFilter,
            'KalturaSystemPartnerUsageItem': KalturaSystemPartnerUsageItem,
            'KalturaSystemPartnerUsageListResponse': KalturaSystemPartnerUsageListResponse,
            'KalturaSystemPartnerConfiguration': KalturaSystemPartnerConfiguration,
            'KalturaSystemPartnerPackage': KalturaSystemPartnerPackage,
        }

    # @return string
    def getName(self):
        return 'systemPartner'

