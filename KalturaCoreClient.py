from KalturaClientBase import *

API_VERSION = '3.1.4'

########## enums ##########
class KalturaAccessControlOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAdminUserOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiActionPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiParameterPermissionItemAction:
    READ = "read"
    UPDATE = "update"
    INSERT = "insert"
    USEAGE = "all"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiParameterPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetParamsOrigin:
    CONVERT = 0
    INGEST = 1
    CONVERT_WHEN_MISSING = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetStatus:
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAudioCodec:
    NONE = ""
    MP3 = "mp3"
    AAC = "aac"
    VORBIS = "vorbis"
    WMA = "wma"
    WMAPRO = "wmapro"
    AMRNB = "amrnb"
    MPEG2 = "mpeg2"
    COPY = "copy"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseEntryOrderBy:
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseJobOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobErrorTypes:
    APP = 0
    RUNTIME = 1
    HTTP = 2
    CURL = 3
    KALTURA_API = 4
    KALTURA_CLIENT = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobOrderBy:
    STATUS_ASC = "+status"
    STATUS_DESC = "-status"
    CHECK_AGAIN_TIMEOUT_ASC = "+checkAgainTimeout"
    CHECK_AGAIN_TIMEOUT_DESC = "-checkAgainTimeout"
    PROGRESS_ASC = "+progress"
    PROGRESS_DESC = "-progress"
    UPDATES_COUNT_ASC = "+updatesCount"
    UPDATES_COUNT_DESC = "-updatesCount"
    PRIORITY_ASC = "+priority"
    PRIORITY_DESC = "-priority"
    QUEUE_TIME_ASC = "+queueTime"
    QUEUE_TIME_DESC = "-queueTime"
    FINISH_TIME_ASC = "+finishTime"
    FINISH_TIME_DESC = "-finishTime"
    FILE_SIZE_ASC = "+fileSize"
    FILE_SIZE_DESC = "-fileSize"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobStatus:
    PENDING = 0
    QUEUED = 1
    PROCESSING = 2
    PROCESSED = 3
    MOVEFILE = 4
    FINISHED = 5
    FAILED = 6
    ABORTED = 7
    ALMOST_DONE = 8
    RETRY = 9
    FATAL = 10
    DONT_PROCESS = 11

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobType:
    CONVERT = "0"
    IMPORT = "1"
    DELETE = "2"
    FLATTEN = "3"
    BULKUPLOAD = "4"
    DVDCREATOR = "5"
    DOWNLOAD = "6"
    OOCONVERT = "7"
    CONVERT_PROFILE = "10"
    POSTCONVERT = "11"
    PULL = "12"
    REMOTE_CONVERT = "13"
    EXTRACT_MEDIA = "14"
    MAIL = "15"
    NOTIFICATION = "16"
    CLEANUP = "17"
    SCHEDULER_HELPER = "18"
    BULKDOWNLOAD = "19"
    DB_CLEANUP = "20"
    PROVISION_PROVIDE = "21"
    CONVERT_COLLECTION = "22"
    STORAGE_EXPORT = "23"
    PROVISION_DELETE = "24"
    STORAGE_DELETE = "25"
    EMAIL_INGESTION = "26"
    METADATA_IMPORT = "27"
    METADATA_TRANSFORM = "28"
    FILESYNC_IMPORT = "29"
    CAPTURE_THUMB = "30"
    VIRUS_SCAN = "virusScan.VirusScan"
    DISTRIBUTION_SUBMIT = "contentDistribution.DistributionSubmit"
    DISTRIBUTION_UPDATE = "contentDistribution.DistributionUpdate"
    DISTRIBUTION_DELETE = "contentDistribution.DistributionDelete"
    DISTRIBUTION_FETCH_REPORT = "contentDistribution.DistributionFetchReport"
    DISTRIBUTION_ENABLE = "contentDistribution.DistributionEnable"
    DISTRIBUTION_DISABLE = "contentDistribution.DistributionDisable"
    DISTRIBUTION_SYNC = "contentDistribution.DistributionSync"
    DROP_FOLDER_WATCHER = "dropFolder.DropFolderWatcher"
    DROP_FOLDER_HANDLER = "dropFolder.DropFolderHandler"
    PARSE_CAPTION_ASSET = "captionSearch.parseCaptionAsset"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBitRateMode:
    CBR = 1
    VBR = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBulkUploadAction:
    ADD = 1
    UPDATE = 2
    DELETE = 3
    REPLACE = 4
    TRANSFORM_XSLT = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBulkUploadResultObjectType:
    ENTRY = "1"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBulkUploadType:
    CSV = "bulkUploadCsv.CSV"
    XML = "bulkUploadXml.XML"
    DROP_FOLDER_XML = "dropFolderXmlBulkUpload.DROP_FOLDER_XML"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCategoryOrderBy:
    DEPTH_ASC = "+depth"
    DEPTH_DESC = "-depth"
    FULL_NAME_ASC = "+fullName"
    FULL_NAME_DESC = "-fullName"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCommercialUseType:
    COMMERCIAL_USE = 1
    NON_COMMERCIAL_USE = 0

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaContainerFormat:
    FLV = "flv"
    MP4 = "mp4"
    AVI = "avi"
    MOV = "mov"
    MP3 = "mp3"
    _3GP = "3gp"
    OGG = "ogg"
    WMV = "wmv"
    WMA = "wma"
    ISMV = "ismv"
    MKV = "mkv"
    WEBM = "webm"
    MPEG = "mpeg"
    MPEGTS = "mpegts"
    APPLEHTTP = "applehttp"
    SWF = "swf"
    PDF = "pdf"
    JPG = "jpg"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandStatus:
    PENDING = 1
    HANDLED = 2
    DONE = 3
    FAILED = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandTargetType:
    DATA_CENTER = 1
    SCHEDULER = 2
    JOB_TYPE = 3
    JOB = 4
    BATCH = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandType:
    STOP = 1
    START = 2
    CONFIG = 3
    KILL = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaConversionProfileAssetParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaConversionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaConversionProfileStatus:
    DISABLED = "1"
    ENABLED = "2"
    DELETED = "3"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCountryRestrictionType:
    RESTRICT_COUNTRY_LIST = 0
    ALLOW_COUNTRY_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDataEntryOrderBy:
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDirectoryRestrictionType:
    DONT_DISPLAY = 0
    DISPLAY_WITH_LINK = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDurationType:
    NOT_AVAILABLE = "notavailable"
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEditorType:
    SIMPLE = 1
    ADVANCED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEmailIngestionProfileStatus:
    INACTIVE = 0
    ACTIVE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryModerationStatus:
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3
    FLAGGED_FOR_REVIEW = 5
    AUTO_APPROVED = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryReplacementStatus:
    NONE = "0"
    APPROVED_BUT_NOT_READY = "1"
    READY_BUT_NOT_APPROVED = "2"
    NOT_READY_AND_NOT_APPROVED = "3"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryStatus:
    ERROR_IMPORTING = "-2"
    ERROR_CONVERTING = "-1"
    IMPORT = "0"
    PRECONVERT = "1"
    READY = "2"
    DELETED = "3"
    PENDING = "4"
    MODERATE = "5"
    BLOCKED = "6"
    NO_CONTENT = "7"
    INFECTED = "virusScan.Infected"
    SCAN_FAILURE = "virusScan.ScanFailure"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryType:
    AUTOMATIC = "-1"
    MEDIA_CLIP = "1"
    MIX = "2"
    PLAYLIST = "5"
    DATA = "6"
    LIVE_STREAM = "7"
    DOCUMENT = "10"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFileSyncObjectType:
    ENTRY = "1"
    UICONF = "2"
    BATCHJOB = "3"
    ASSET = "4"
    METADATA = "5"
    METADATA_PROFILE = "6"
    SYNDICATION_FEED = "7"
    CONVERSION_PROFILE = "8"
    FLAVOR_ASSET = "4"
    GENERIC_DISTRIBUTION_ACTION = "contentDistribution.GenericDistributionAction"
    ENTRY_DISTRIBUTION = "contentDistribution.EntryDistribution"
    DISTRIBUTION_PROFILE = "contentDistribution.DistributionProfile"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorAssetStatus:
    CONVERTING = 1
    NOT_APPLICABLE = 4
    TEMP = 5
    WAIT_FOR_CONVERT = 6
    VALIDATING = 8
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorReadyBehaviorType:
    INHERIT_FLAVOR_PARAMS = 0
    REQUIRED = 1
    OPTIONAL = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGender:
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericXsltSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGoogleSyndicationFeedAdultValues:
    YES = "Yes"
    NO = "No"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGoogleVideoSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedAdultValues:
    YES = "yes"
    NO = "no"
    CLEAN = "clean"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedCategories:
    ARTS = "Arts"
    ARTS_DESIGN = "Arts/Design"
    ARTS_FASHION_BEAUTY = "Arts/Fashion &amp; Beauty"
    ARTS_FOOD = "Arts/Food"
    ARTS_LITERATURE = "Arts/Literature"
    ARTS_PERFORMING_ARTS = "Arts/Performing Arts"
    ARTS_VISUAL_ARTS = "Arts/Visual Arts"
    BUSINESS = "Business"
    BUSINESS_BUSINESS_NEWS = "Business/Business News"
    BUSINESS_CAREERS = "Business/Careers"
    BUSINESS_INVESTING = "Business/Investing"
    BUSINESS_MANAGEMENT_MARKETING = "Business/Management &amp; Marketing"
    BUSINESS_SHOPPING = "Business/Shopping"
    COMEDY = "Comedy"
    EDUCATION = "Education"
    EDUCATION_TECHNOLOGY = "Education/Education Technology"
    EDUCATION_HIGHER_EDUCATION = "Education/Higher Education"
    EDUCATION_K_12 = "Education/K-12"
    EDUCATION_LANGUAGE_COURSES = "Education/Language Courses"
    EDUCATION_TRAINING = "Education/Training"
    GAMES_HOBBIES = "Games &amp; Hobbies"
    GAMES_HOBBIES_AUTOMOTIVE = "Games &amp; Hobbies/Automotive"
    GAMES_HOBBIES_AVIATION = "Games &amp; Hobbies/Aviation"
    GAMES_HOBBIES_HOBBIES = "Games &amp; Hobbies/Hobbies"
    GAMES_HOBBIES_OTHER_GAMES = "Games &amp; Hobbies/Other Games"
    GAMES_HOBBIES_VIDEO_GAMES = "Games &amp; Hobbies/Video Games"
    GOVERNMENT_ORGANIZATIONS = "Government &amp; Organizations"
    GOVERNMENT_ORGANIZATIONS_LOCAL = "Government &amp; Organizations/Local"
    GOVERNMENT_ORGANIZATIONS_NATIONAL = "Government &amp; Organizations/National"
    GOVERNMENT_ORGANIZATIONS_NON_PROFIT = "Government &amp; Organizations/Non-Profit"
    GOVERNMENT_ORGANIZATIONS_REGIONAL = "Government &amp; Organizations/Regional"
    HEALTH = "Health"
    HEALTH_ALTERNATIVE_HEALTH = "Health/Alternative Health"
    HEALTH_FITNESS_NUTRITION = "Health/Fitness &amp; Nutrition"
    HEALTH_SELF_HELP = "Health/Self-Help"
    HEALTH_SEXUALITY = "Health/Sexuality"
    KIDS_FAMILY = "Kids &amp; Family"
    MUSIC = "Music"
    NEWS_POLITICS = "News &amp; Politics"
    RELIGION_SPIRITUALITY = "Religion &amp; Spirituality"
    RELIGION_SPIRITUALITY_BUDDHISM = "Religion &amp; Spirituality/Buddhism"
    RELIGION_SPIRITUALITY_CHRISTIANITY = "Religion &amp; Spirituality/Christianity"
    RELIGION_SPIRITUALITY_HINDUISM = "Religion &amp; Spirituality/Hinduism"
    RELIGION_SPIRITUALITY_ISLAM = "Religion &amp; Spirituality/Islam"
    RELIGION_SPIRITUALITY_JUDAISM = "Religion &amp; Spirituality/Judaism"
    RELIGION_SPIRITUALITY_OTHER = "Religion &amp; Spirituality/Other"
    RELIGION_SPIRITUALITY_SPIRITUALITY = "Religion &amp; Spirituality/Spirituality"
    SCIENCE_MEDICINE = "Science &amp; Medicine"
    SCIENCE_MEDICINE_MEDICINE = "Science &amp; Medicine/Medicine"
    SCIENCE_MEDICINE_NATURAL_SCIENCES = "Science &amp; Medicine/Natural Sciences"
    SCIENCE_MEDICINE_SOCIAL_SCIENCES = "Science &amp; Medicine/Social Sciences"
    SOCIETY_CULTURE = "Society &amp; Culture"
    SOCIETY_CULTURE_HISTORY = "Society &amp; Culture/History"
    SOCIETY_CULTURE_PERSONAL_JOURNALS = "Society &amp; Culture/Personal Journals"
    SOCIETY_CULTURE_PHILOSOPHY = "Society &amp; Culture/Philosophy"
    SOCIETY_CULTURE_PLACES_TRAVEL = "Society &amp; Culture/Places &amp; Travel"
    SPORTS_RECREATION = "Sports &amp; Recreation"
    SPORTS_RECREATION_AMATEUR = "Sports &amp; Recreation/Amateur"
    SPORTS_RECREATION_COLLEGE_HIGH_SCHOOL = "Sports &amp; Recreation/College &amp; High School"
    SPORTS_RECREATION_OUTDOOR = "Sports &amp; Recreation/Outdoor"
    SPORTS_RECREATION_PROFESSIONAL = "Sports &amp; Recreation/Professional"
    TECHNOLOGY = "Technology"
    TECHNOLOGY_GADGETS = "Technology/Gadgets"
    TECHNOLOGY_TECH_NEWS = "Technology/Tech News"
    TECHNOLOGY_PODCASTING = "Technology/Podcasting"
    TECHNOLOGY_SOFTWARE_HOW_TO = "Technology/Software How-To"
    TV_FILM = "TV &amp; Film"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaIpAddressRestrictionType:
    RESTRICT_LIST = 0
    ALLOW_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLanguage:
    AB = "Abkhazian"
    AA = "Afar"
    AF = "Afrikaans"
    SQ = "Albanian"
    AM = "Amharic"
    AR = "Arabic"
    HY = "Armenian"
    AS_ = "Assamese"
    AY = "Aymara"
    AZ = "Azerbaijani"
    BA = "Bashkir"
    EU = "Basque"
    BN = "Bengali (Bangla)"
    DZ = "Bhutani"
    BH = "Bihari"
    BI = "Bislama"
    BR = "Breton"
    BG = "Bulgarian"
    MY = "Burmese"
    BE = "Byelorussian (Belarusian)"
    KM = "Cambodian"
    CA = "Catalan"
    ZH = "Chinese"
    CO = "Corsican"
    HR = "Croatian"
    CS = "Czech"
    DA = "Danish"
    NL = "Dutch"
    EN = "English"
    EO = "Esperanto"
    ET = "Estonian"
    FO = "Faeroese"
    FA = "Farsi"
    FJ = "Fiji"
    FI = "Finnish"
    FR = "French"
    FY = "Frisian"
    GL = "Galician"
    GD = "Gaelic (Scottish)"
    GV = "Gaelic (Manx)"
    KA = "Georgian"
    DE = "German"
    EL = "Greek"
    KL = "Greenlandic"
    GN = "Guarani"
    GU = "Gujarati"
    HA = "Hausa"
    HE = "Hebrew"
    IW = "Hebrew"
    HI = "Hindi"
    HU = "Hungarian"
    IS = "Icelandic"
    ID = "Indonesian"
    IN = "Indonesian"
    IA = "Interlingua"
    IE = "Interlingue"
    IU = "Inuktitut"
    IK = "Inupiak"
    GA = "Irish"
    IT = "Italian"
    JA = "Japanese"
    JV = "Javanese"
    KN = "Kannada"
    KS = "Kashmiri"
    KK = "Kazakh"
    RW = "Kinyarwanda (Ruanda)"
    KY = "Kirghiz"
    RN = "Kirundi (Rundi)"
    KO = "Korean"
    KU = "Kurdish"
    LO = "Laothian"
    LA = "Latin"
    LV = "Latvian (Lettish)"
    LI = "Limburgish ( Limburger)"
    LN = "Lingala"
    LT = "Lithuanian"
    MK = "Macedonian"
    MG = "Malagasy"
    MS = "Malay"
    ML = "Malayalam"
    MT = "Maltese"
    MI = "Maori"
    MR = "Marathi"
    MO = "Moldavian"
    MN = "Mongolian"
    NA = "Nauru"
    NE = "Nepali"
    NO = "Norwegian"
    OC = "Occitan"
    OR_ = "Oriya"
    OM = "Oromo (Afan, Galla)"
    PS = "Pashto (Pushto)"
    PL = "Polish"
    PT = "Portuguese"
    PA = "Punjabi"
    QU = "Quechua"
    RM = "Rhaeto-Romance"
    RO = "Romanian"
    RU = "Russian"
    SM = "Samoan"
    SG = "Sangro"
    SA = "Sanskrit"
    SR = "Serbian"
    SH = "Serbo-Croatian"
    ST = "Sesotho"
    TN = "Setswana"
    SN = "Shona"
    SD = "Sindhi"
    SI = "Sinhalese"
    SS = "Siswati"
    SK = "Slovak"
    SL = "Slovenian"
    SO = "Somali"
    ES = "Spanish"
    SU = "Sundanese"
    SW = "Swahili (Kiswahili)"
    SV = "Swedish"
    TL = "Tagalog"
    TG = "Tajik"
    TA = "Tamil"
    TT = "Tatar"
    TE = "Telugu"
    TH = "Thai"
    BO = "Tibetan"
    TI = "Tigrinya"
    TO = "Tonga"
    TS = "Tsonga"
    TR = "Turkish"
    TK = "Turkmen"
    TW = "Twi"
    UG = "Uighur"
    UK = "Ukrainian"
    UR = "Urdu"
    UZ = "Uzbek"
    VI = "Vietnamese"
    VO = "Volapuk"
    CY = "Welsh"
    WO = "Wolof"
    XH = "Xhosa"
    YI = "Yiddish"
    JI = "Yiddish"
    YO = "Yoruba"
    ZU = "Zulu"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLanguageCode:
    AB = "ab"
    AA = "aa"
    AF = "af"
    SQ = "sq"
    AM = "am"
    AR = "ar"
    HY = "hy"
    AS_ = "as"
    AY = "ay"
    AZ = "az"
    BA = "ba"
    EU = "eu"
    BN = "bn"
    DZ = "dz"
    BH = "bh"
    BI = "bi"
    BR = "br"
    BG = "bg"
    MY = "my"
    BE = "be"
    KM = "km"
    CA = "ca"
    ZH = "zh"
    CO = "co"
    HR = "hr"
    CS = "cs"
    DA = "da"
    NL = "nl"
    EN = "en"
    EO = "eo"
    ET = "et"
    FO = "fo"
    FA = "fa"
    FJ = "fj"
    FI = "fi"
    FR = "fr"
    FY = "fy"
    GL = "gl"
    GD = "gd"
    GV = "gv"
    KA = "ka"
    DE = "de"
    EL = "el"
    KL = "kl"
    GN = "gn"
    GU = "gu"
    HA = "ha"
    HE = "he"
    IW = "iw"
    HI = "hi"
    HU = "hu"
    IS = "is"
    ID = "id"
    IN = "in"
    IA = "ia"
    IE = "ie"
    IU = "iu"
    IK = "ik"
    GA = "ga"
    IT = "it"
    JA = "ja"
    JV = "jv"
    KN = "kn"
    KS = "ks"
    KK = "kk"
    RW = "rw"
    KY = "ky"
    RN = "rn"
    KO = "ko"
    KU = "ku"
    LO = "lo"
    LA = "la"
    LV = "lv"
    LI = "li"
    LN = "ln"
    LT = "lt"
    MK = "mk"
    MG = "mg"
    MS = "ms"
    ML = "ml"
    MT = "mt"
    MI = "mi"
    MR = "mr"
    MO = "mo"
    MN = "mn"
    NA = "na"
    NE = "ne"
    NO = "no"
    OC = "oc"
    OR_ = "or"
    OM = "om"
    PS = "ps"
    PL = "pl"
    PT = "pt"
    PA = "pa"
    QU = "qu"
    RM = "rm"
    RO = "ro"
    RU = "ru"
    SM = "sm"
    SG = "sg"
    SA = "sa"
    SR = "sr"
    SH = "sh"
    ST = "st"
    TN = "tn"
    SN = "sn"
    SD = "sd"
    SI = "si"
    SS = "ss"
    SK = "sk"
    SL = "sl"
    SO = "so"
    ES = "es"
    SU = "su"
    SW = "sw"
    SV = "sv"
    TL = "tl"
    TG = "tg"
    TA = "ta"
    TT = "tt"
    TE = "te"
    TH = "th"
    BO = "bo"
    TI = "ti"
    TO = "to"
    TS = "ts"
    TR = "tr"
    TK = "tk"
    TW = "tw"
    UG = "ug"
    UK = "uk"
    UR = "ur"
    UZ = "uz"
    VI = "vi"
    VO = "vo"
    CY = "cy"
    WO = "wo"
    XH = "xh"
    YI = "yi"
    JI = "ji"
    YO = "yo"
    ZU = "zu"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLicenseType:
    UNKNOWN = -1
    NONE = 0
    COPYRIGHTED = 1
    PUBLIC_DOMAIN = 2
    CREATIVECOMMONS_ATTRIBUTION = 3
    CREATIVECOMMONS_ATTRIBUTION_SHARE_ALIKE = 4
    CREATIVECOMMONS_ATTRIBUTION_NO_DERIVATIVES = 5
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL = 6
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL_SHARE_ALIKE = 7
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL_NO_DERIVATIVES = 8
    GFDL = 9
    GPL = 10
    AFFERO_GPL = 11
    LGPL = 12
    BSD = 13
    APACHE = 14
    MOZILLA = 15

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLiveStreamAdminEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLiveStreamEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMailJobOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaInfoOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaType:
    VIDEO = 1
    IMAGE = 2
    AUDIO = 5
    LIVE_STREAM_FLASH = 201
    LIVE_STREAM_WINDOWS_MEDIA = 202
    LIVE_STREAM_REAL_MEDIA = 203
    LIVE_STREAM_QUICKTIME = 204

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMixEntryOrderBy:
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationFlagStatus:
    PENDING = 1
    MODERATED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationFlagType:
    SEXUAL_CONTENT = 1
    VIOLENT_REPULSIVE = 2
    HARMFUL_DANGEROUS = 3
    SPAM_COMMERCIALS = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationObjectType:
    ENTRY = 2
    USER = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNotificationOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNotificationType:
    ENTRY_ADD = 1
    ENTR_UPDATE_PERMISSIONS = 2
    ENTRY_DELETE = 3
    ENTRY_BLOCK = 4
    ENTRY_UPDATE = 5
    ENTRY_UPDATE_THUMBNAIL = 6
    ENTRY_UPDATE_MODERATION = 7
    USER_ADD = 21
    USER_BANNED = 26

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNullableBoolean:
    NULL_VALUE = -1
    FALSE_VALUE = 0
    TRUE_VALUE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerGroupType:
    PUBLISHER = 1
    VAR_GROUP = 2
    GROUP = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    WEBSITE_ASC = "+website"
    WEBSITE_DESC = "-website"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    ADMIN_NAME_ASC = "+adminName"
    ADMIN_NAME_DESC = "-adminName"
    ADMIN_EMAIL_ASC = "+adminEmail"
    ADMIN_EMAIL_DESC = "-adminEmail"
    STATUS_ASC = "+status"
    STATUS_DESC = "-status"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerStatus:
    ACTIVE = 1
    BLOCKED = 2
    FULL_BLOCK = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerType:
    KMC = 1
    WIKI = 100
    WORDPRESS = 101
    DRUPAL = 102
    DEKIWIKI = 103
    MOODLE = 104
    COMMUNITY_EDITION = 105
    JOOMLA = 106
    BLACKBOARD = 107
    SAKAI = 108

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionItemType:
    API_ACTION_ITEM = "kApiActionPermissionItem"
    API_PARAMETER_ITEM = "kApiParameterPermissionItem"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionStatus:
    ACTIVE = 1
    BLOCKED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionType:
    NORMAL = 1
    SPECIAL_FEATURE = 2
    PLUGIN = 3
    PARTNER_GROUP = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlayableEntryOrderBy:
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlaylistOrderBy:
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
    START_DATE_ASC = "+startDate"
    START_DATE_DESC = "-startDate"
    END_DATE_ASC = "+endDate"
    END_DATE_DESC = "-endDate"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlaylistType:
    DYNAMIC = 10
    STATIC_LIST = 3
    EXTERNAL = 101

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaReportOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaReportType:
    TOP_CONTENT = 1
    CONTENT_DROPOFF = 2
    CONTENT_INTERACTIONS = 3
    MAP_OVERLAY = 4
    TOP_CONTRIBUTORS = 5
    TOP_SYNDICATION = 6
    CONTENT_CONTRIBUTIONS = 7
    WIDGETS_STATS = 8

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSchemaType:
    SYNDICATION = "syndication"
    SERVE_API = "cuePoint.serveAPI"
    INGEST_API = "cuePoint.ingestAPI"
    BULK_UPLOAD_XML = "bulkUploadXml.bulkUploadXML"
    BULK_UPLOAD_RESULT_XML = "bulkUploadXml.bulkUploadResultXML"
    DROP_FOLDER_XML = "dropFolderXmlBulkUpload.dropFolderXml"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchConditionComparison:
    EQUEL = 1
    GREATER_THAN = 2
    GREATER_THAN_OR_EQUEL = 3
    LESS_THAN = 4
    LESS_THAN_OR_EQUEL = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchOperatorType:
    SEARCH_AND = 1
    SEARCH_OR = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchProviderType:
    FLICKR = 3
    YOUTUBE = 4
    MYSPACE = 7
    PHOTOBUCKET = 8
    JAMENDO = 9
    CCMIXTER = 10
    NYPL = 11
    CURRENT = 12
    MEDIA_COMMONS = 13
    KALTURA = 20
    KALTURA_USER_CLIPS = 21
    ARCHIVE_ORG = 22
    KALTURA_PARTNER = 23
    METACAFE = 24
    SEARCH_PROXY = 28
    PARTNER_SPECIFIC = 100

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSessionType:
    USER = 0
    ADMIN = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSiteRestrictionType:
    RESTRICT_SITE_LIST = 0
    ALLOW_SITE_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSourceType:
    FILE = "1"
    WEBCAM = "2"
    URL = "5"
    SEARCH_PROVIDER = "6"
    AKAMAI_LIVE = "29"
    MANUAL_LIVE_STREAM = "30"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStatsEventType:
    WIDGET_LOADED = 1
    MEDIA_LOADED = 2
    PLAY = 3
    PLAY_REACHED_25 = 4
    PLAY_REACHED_50 = 5
    PLAY_REACHED_75 = 6
    PLAY_REACHED_100 = 7
    OPEN_EDIT = 8
    OPEN_VIRAL = 9
    OPEN_DOWNLOAD = 10
    OPEN_REPORT = 11
    BUFFER_START = 12
    BUFFER_END = 13
    OPEN_FULL_SCREEN = 14
    CLOSE_FULL_SCREEN = 15
    REPLAY = 16
    SEEK = 17
    OPEN_UPLOAD = 18
    SAVE_PUBLISH = 19
    CLOSE_EDITOR = 20
    PRE_BUMPER_PLAYED = 21
    POST_BUMPER_PLAYED = 22
    BUMPER_CLICKED = 23
    PREROLL_STARTED = 24
    MIDROLL_STARTED = 25
    POSTROLL_STARTED = 26
    OVERLAY_STARTED = 27
    PREROLL_CLICKED = 28
    MIDROLL_CLICKED = 29
    POSTROLL_CLICKED = 30
    OVERLAY_CLICKED = 31
    PREROLL_25 = 32
    PREROLL_50 = 33
    PREROLL_75 = 34
    MIDROLL_25 = 35
    MIDROLL_50 = 36
    MIDROLL_75 = 37
    POSTROLL_25 = 38
    POSTROLL_50 = 39
    POSTROLL_75 = 40

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStatsKmcEventType:
    CONTENT_PAGE_VIEW = 1001
    CONTENT_ADD_PLAYLIST = 1010
    CONTENT_EDIT_PLAYLIST = 1011
    CONTENT_DELETE_PLAYLIST = 1012
    CONTENT_DELETE_ITEM = 1058
    CONTENT_DELETE_MIX = 1059
    CONTENT_EDIT_ENTRY = 1013
    CONTENT_CHANGE_THUMBNAIL = 1014
    CONTENT_ADD_TAGS = 1015
    CONTENT_REMOVE_TAGS = 1016
    CONTENT_ADD_ADMIN_TAGS = 1017
    CONTENT_REMOVE_ADMIN_TAGS = 1018
    CONTENT_DOWNLOAD = 1019
    CONTENT_APPROVE_MODERATION = 1020
    CONTENT_REJECT_MODERATION = 1021
    CONTENT_BULK_UPLOAD = 1022
    CONTENT_ADMIN_KCW_UPLOAD = 1023
    CONTENT_CONTENT_GO_TO_PAGE = 1057
    CONTENT_ENTRY_DRILLDOWN = 1088
    CONTENT_OPEN_PREVIEW_AND_EMBED = 1089
    ACCOUNT_CHANGE_PARTNER_INFO = 1030
    ACCOUNT_CHANGE_LOGIN_INFO = 1031
    ACCOUNT_CONTACT_US_USAGE = 1032
    ACCOUNT_UPDATE_SERVER_SETTINGS = 1033
    ACCOUNT_ACCOUNT_OVERVIEW = 1034
    ACCOUNT_ACCESS_CONTROL = 1035
    ACCOUNT_TRANSCODING_SETTINGS = 1036
    ACCOUNT_ACCOUNT_UPGRADE = 1037
    ACCOUNT_SAVE_SERVER_SETTINGS = 1038
    ACCOUNT_ACCESS_CONTROL_DELETE = 1039
    ACCOUNT_SAVE_TRANSCODING_SETTINGS = 1040
    LOGIN = 1041
    DASHBOARD_IMPORT_CONTENT = 1042
    DASHBOARD_UPDATE_CONTENT = 1043
    DASHBOARD_ACCOUNT_CONTACT_US = 1044
    DASHBOARD_VIEW_REPORTS = 1045
    DASHBOARD_EMBED_PLAYER = 1046
    DASHBOARD_EMBED_PLAYLIST = 1047
    DASHBOARD_CUSTOMIZE_PLAYERS = 1048
    APP_STUDIO_NEW_PLAYER_SINGLE_VIDEO = 1050
    APP_STUDIO_NEW_PLAYER_PLAYLIST = 1051
    APP_STUDIO_NEW_PLAYER_MULTI_TAB_PLAYLIST = 1052
    APP_STUDIO_EDIT_PLAYER_SINGLE_VIDEO = 1053
    APP_STUDIO_EDIT_PLAYER_PLAYLIST = 1054
    APP_STUDIO_EDIT_PLAYER_MULTI_TAB_PLAYLIST = 1055
    APP_STUDIO_DUPLICATE_PLAYER = 1056
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_TAB = 1070
    REPORTS_AND_ANALYTICS_CONTENT_REPORTS_TAB = 1071
    REPORTS_AND_ANALYTICS_USERS_AND_COMMUNITY_REPORTS_TAB = 1072
    REPORTS_AND_ANALYTICS_TOP_CONTRIBUTORS = 1073
    REPORTS_AND_ANALYTICS_MAP_OVERLAYS = 1074
    REPORTS_AND_ANALYTICS_TOP_SYNDICATIONS = 1075
    REPORTS_AND_ANALYTICS_TOP_CONTENT = 1076
    REPORTS_AND_ANALYTICS_CONTENT_DROPOFF = 1077
    REPORTS_AND_ANALYTICS_CONTENT_INTERACTIONS = 1078
    REPORTS_AND_ANALYTICS_CONTENT_CONTRIBUTIONS = 1079
    REPORTS_AND_ANALYTICS_VIDEO_DRILL_DOWN = 1080
    REPORTS_AND_ANALYTICS_CONTENT_DRILL_DOWN_INTERACTION = 1081
    REPORTS_AND_ANALYTICS_CONTENT_CONTRIBUTIONS_DRILLDOWN = 1082
    REPORTS_AND_ANALYTICS_VIDEO_DRILL_DOWN_DROPOFF = 1083
    REPORTS_AND_ANALYTICS_MAP_OVERLAYS_DRILLDOWN = 1084
    REPORTS_AND_ANALYTICS_TOP_SYNDICATIONS_DRILL_DOWN = 1085
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_VIEW_MONTHLY = 1086
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_VIEW_YEARLY = 1087

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageProfileDeliveryStatus:
    ACTIVE = 1
    BLOCKED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageProfileProtocol:
    KALTURA_DC = 0
    FTP = 1
    SCP = 2
    SFTP = 3
    S3 = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageProfileStatus:
    DISABLED = 1
    AUTOMATIC = 2
    MANUAL = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStorageServePriority:
    KALTURA_ONLY = 1
    KALTURA_FIRST = 2
    EXTERNAL_FIRST = 3
    EXTERNAL_ONLY = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSyndicationFeedStatus:
    DELETED = -1
    ACTIVE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSyndicationFeedType:
    GOOGLE_VIDEO = 1
    YAHOO = 2
    ITUNES = 3
    TUBE_MOGUL = 4
    KALTURA = 5
    KALTURA_XSLT = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbAssetStatus:
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbCropType:
    RESIZE = 1
    RESIZE_WITH_PADDING = 2
    CROP = 3
    CROP_FROM_TOP = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaTubeMogulSyndicationFeedCategories:
    ARTS_AND_ANIMATION = "Arts &amp; Animation"
    COMEDY = "Comedy"
    ENTERTAINMENT = "Entertainment"
    MUSIC = "Music"
    NEWS_AND_BLOGS = "News &amp; Blogs"
    SCIENCE_AND_TECHNOLOGY = "Science &amp; Technology"
    SPORTS = "Sports"
    TRAVEL_AND_PLACES = "Travel &amp; Places"
    VIDEO_GAMES = "Video Games"
    ANIMALS_AND_PETS = "Animals &amp; Pets"
    AUTOS = "Autos"
    VLOGS_PEOPLE = "Vlogs &amp; People"
    HOW_TO_INSTRUCTIONAL_DIY = "How To/Instructional/DIY"
    COMMERCIALS_PROMOTIONAL = "Commercials/Promotional"
    FAMILY_AND_KIDS = "Family &amp; Kids"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaTubeMogulSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfCreationMode:
    WIZARD = 2
    ADVANCED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfObjType:
    PLAYER = 1
    CONTRIBUTION_WIZARD = 2
    SIMPLE_EDITOR = 3
    ADVANCED_EDITOR = 4
    PLAYLIST = 5
    APP_STUDIO = 6
    KRECORD = 7
    PLAYER_V3 = 8
    KMC_ACCOUNT = 9
    KMC_ANALYTICS = 10
    KMC_CONTENT = 11
    KMC_DASHBOARD = 12
    KMC_LOGIN = 13
    PLAYER_SL = 14
    CLIENTSIDE_ENCODER = 15
    KMC_GENERAL = 16
    KMC_ROLES_AND_PERMISSIONS = 17
    CLIPPER = 18

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadErrorCode:
    NO_ERROR = 0
    GENERAL_ERROR = 1
    PARTIAL_UPLOAD = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadTokenOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadTokenStatus:
    PENDING = 0
    PARTIAL_UPLOAD = 1
    FULL_UPLOAD = 2
    CLOSED = 3
    TIMED_OUT = 4
    DELETED = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserAgentRestrictionType:
    RESTRICT_LIST = 0
    ALLOW_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserLoginDataOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserRoleOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserRoleStatus:
    ACTIVE = 1
    BLOCKED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserStatus:
    BLOCKED = 0
    ACTIVE = 1
    DELETED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVideoCodec:
    NONE = ""
    VP6 = "vp6"
    H263 = "h263"
    H264 = "h264"
    H264B = "h264b"
    H264M = "h264m"
    H264H = "h264h"
    FLV = "flv"
    MPEG4 = "mpeg4"
    THEORA = "theora"
    WMV2 = "wmv2"
    WMV3 = "wmv3"
    WVC1A = "wvc1a"
    VP8 = "vp8"
    MPEG2 = "mpeg2"
    COPY = "copy"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaWidgetOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaWidgetSecurityType:
    NONE = 1
    TIMEHASH = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedAdultValues:
    ADULT = "adult"
    NON_ADULT = "nonadult"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedCategories:
    ACTION = "Action"
    ART_AND_ANIMATION = "Art &amp; Animation"
    ENTERTAINMENT_AND_TV = "Entertainment &amp; TV"
    FOOD = "Food"
    GAMES = "Games"
    HOW_TO = "How-To"
    MUSIC = "Music"
    PEOPLE_AND_VLOGS = "People &amp; Vlogs"
    SCIENCE_AND_ENVIRONMENT = "Science &amp; Environment"
    TRANSPORTATION = "Transportation"
    ANIMALS = "Animals"
    COMMERCIALS = "Commercials"
    FAMILY = "Family"
    FUNNY_VIDEOS = "Funny Videos"
    HEALTH_AND_BEAUTY = "Health &amp; Beauty"
    MOVIES_AND_SHORTS = "Movies &amp; Shorts"
    NEWS_AND_POLITICS = "News &amp; Politics"
    PRODUCTS_AND_TECH = "Products &amp; Tech."
    SPORTS = "Sports"
    TRAVEL = "Travel"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaBaseRestriction(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseRestriction")
        return kparams


class KalturaAccessControl(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isDefault=NotImplemented,
            restrictions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the Access Control Profile
        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The name of the Access Control Profile
        # @var string
        self.name = name

        # System name of the Access Control Profile
        # @var string
        self.systemName = systemName

        # The description of the Access Control Profile
        # @var string
        self.description = description

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # True if this Conversion Profile is the default
        # @var KalturaNullableBoolean
        self.isDefault = isDefault

        # Array of Access Control Restrictions
        # @var array of KalturaBaseRestriction
        self.restrictions = restrictions


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'restrictions': (KalturaObjectFactory.createArray, KalturaBaseRestriction), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControl.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAccessControl")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("isDefault", self.isDefault)
        kparams.addArrayIfDefined("restrictions", self.restrictions)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getRestrictions(self):
        return self.restrictions

    def setRestrictions(self, newRestrictions):
        self.restrictions = newRestrictions


class KalturaSearchItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchItem")
        return kparams


class KalturaFilter(KalturaObjectBase):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.orderBy = orderBy

        # @var KalturaSearchItem
        self.advancedSearch = advancedSearch


    PROPERTY_LOADERS = {
        'orderBy': getXmlNodeText, 
        'advancedSearch': (KalturaObjectFactory.create, KalturaSearchItem), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilter")
        kparams.addStringIfDefined("orderBy", self.orderBy)
        kparams.addObjectIfDefined("advancedSearch", self.advancedSearch)
        return kparams

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy

    def getAdvancedSearch(self):
        return self.advancedSearch

    def setAdvancedSearch(self, newAdvancedSearch):
        self.advancedSearch = newAdvancedSearch


class KalturaAccessControlBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAccessControlBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual


class KalturaAccessControlFilter(KalturaAccessControlBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented):
        KalturaAccessControlBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            systemNameEqual,
            systemNameIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAccessControlBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAccessControlBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAccessControlFilter")
        return kparams


class KalturaFilterPager(KalturaObjectBase):
    """The KalturaFilterPager object enables paging management to be applied upon service list actions."""

    def __init__(self,
            pageSize=NotImplemented,
            pageIndex=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The number of objects to retrieve. (Default is 30, maximum page size is 500).
        # @var int
        self.pageSize = pageSize

        # The page number for which {pageSize} of objects should be retrieved (Default is 1).
        # @var int
        self.pageIndex = pageIndex


    PROPERTY_LOADERS = {
        'pageSize': getXmlNodeInt, 
        'pageIndex': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilterPager.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilterPager")
        kparams.addIntIfDefined("pageSize", self.pageSize)
        kparams.addIntIfDefined("pageIndex", self.pageIndex)
        return kparams

    def getPageSize(self):
        return self.pageSize

    def setPageSize(self, newPageSize):
        self.pageSize = newPageSize

    def getPageIndex(self):
        return self.pageIndex

    def setPageIndex(self, newPageIndex):
        self.pageIndex = newPageIndex


class KalturaAccessControlListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaAccessControl
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAccessControl), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAccessControlListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUser(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            screenName=NotImplemented,
            fullName=NotImplemented,
            email=NotImplemented,
            dateOfBirth=NotImplemented,
            country=NotImplemented,
            state=NotImplemented,
            city=NotImplemented,
            zip=NotImplemented,
            thumbnailUrl=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            gender=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerData=NotImplemented,
            indexedPartnerDataInt=NotImplemented,
            indexedPartnerDataString=NotImplemented,
            storageSize=NotImplemented,
            password=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            isAdmin=NotImplemented,
            lastLoginTime=NotImplemented,
            statusUpdatedAt=NotImplemented,
            deletedAt=NotImplemented,
            loginEnabled=NotImplemented,
            roleIds=NotImplemented,
            roleNames=NotImplemented,
            isAccountOwner=NotImplemented,
            allowedPartnerIds=NotImplemented,
            allowedPartnerPackages=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.screenName = screenName

        # DEPRECATED
        # @var string
        self.fullName = fullName

        # @var string
        self.email = email

        # @var int
        self.dateOfBirth = dateOfBirth

        # @var string
        self.country = country

        # @var string
        self.state = state

        # @var string
        self.city = city

        # @var string
        self.zip = zip

        # @var string
        self.thumbnailUrl = thumbnailUrl

        # @var string
        self.description = description

        # @var string
        self.tags = tags

        # Admin tags can be updated only by using an admin session
        # @var string
        self.adminTags = adminTags

        # @var KalturaGender
        self.gender = gender

        # @var KalturaUserStatus
        self.status = status

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = partnerData

        # @var int
        self.indexedPartnerDataInt = indexedPartnerDataInt

        # @var string
        self.indexedPartnerDataString = indexedPartnerDataString

        # @var int
        # @readonly
        self.storageSize = storageSize

        # @var string
        # @insertonly
        self.password = password

        # @var string
        self.firstName = firstName

        # @var string
        self.lastName = lastName

        # @var bool
        self.isAdmin = isAdmin

        # @var int
        # @readonly
        self.lastLoginTime = lastLoginTime

        # @var int
        # @readonly
        self.statusUpdatedAt = statusUpdatedAt

        # @var int
        # @readonly
        self.deletedAt = deletedAt

        # @var bool
        # @readonly
        self.loginEnabled = loginEnabled

        # @var string
        self.roleIds = roleIds

        # @var string
        # @readonly
        self.roleNames = roleNames

        # @var bool
        # @readonly
        self.isAccountOwner = isAccountOwner

        # @var string
        self.allowedPartnerIds = allowedPartnerIds

        # @var string
        self.allowedPartnerPackages = allowedPartnerPackages


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'screenName': getXmlNodeText, 
        'fullName': getXmlNodeText, 
        'email': getXmlNodeText, 
        'dateOfBirth': getXmlNodeInt, 
        'country': getXmlNodeText, 
        'state': getXmlNodeText, 
        'city': getXmlNodeText, 
        'zip': getXmlNodeText, 
        'thumbnailUrl': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'adminTags': getXmlNodeText, 
        'gender': (KalturaEnumsFactory.createInt, "KalturaGender"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaUserStatus"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'indexedPartnerDataInt': getXmlNodeInt, 
        'indexedPartnerDataString': getXmlNodeText, 
        'storageSize': getXmlNodeInt, 
        'password': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
        'isAdmin': getXmlNodeBool, 
        'lastLoginTime': getXmlNodeInt, 
        'statusUpdatedAt': getXmlNodeInt, 
        'deletedAt': getXmlNodeInt, 
        'loginEnabled': getXmlNodeBool, 
        'roleIds': getXmlNodeText, 
        'roleNames': getXmlNodeText, 
        'isAccountOwner': getXmlNodeBool, 
        'allowedPartnerIds': getXmlNodeText, 
        'allowedPartnerPackages': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUser")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("screenName", self.screenName)
        kparams.addStringIfDefined("fullName", self.fullName)
        kparams.addStringIfDefined("email", self.email)
        kparams.addIntIfDefined("dateOfBirth", self.dateOfBirth)
        kparams.addStringIfDefined("country", self.country)
        kparams.addStringIfDefined("state", self.state)
        kparams.addStringIfDefined("city", self.city)
        kparams.addStringIfDefined("zip", self.zip)
        kparams.addStringIfDefined("thumbnailUrl", self.thumbnailUrl)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("adminTags", self.adminTags)
        kparams.addIntEnumIfDefined("gender", self.gender)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addIntIfDefined("indexedPartnerDataInt", self.indexedPartnerDataInt)
        kparams.addStringIfDefined("indexedPartnerDataString", self.indexedPartnerDataString)
        kparams.addStringIfDefined("password", self.password)
        kparams.addStringIfDefined("firstName", self.firstName)
        kparams.addStringIfDefined("lastName", self.lastName)
        kparams.addBoolIfDefined("isAdmin", self.isAdmin)
        kparams.addStringIfDefined("roleIds", self.roleIds)
        kparams.addStringIfDefined("allowedPartnerIds", self.allowedPartnerIds)
        kparams.addStringIfDefined("allowedPartnerPackages", self.allowedPartnerPackages)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getPartnerId(self):
        return self.partnerId

    def getScreenName(self):
        return self.screenName

    def setScreenName(self, newScreenName):
        self.screenName = newScreenName

    def getFullName(self):
        return self.fullName

    def setFullName(self, newFullName):
        self.fullName = newFullName

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getDateOfBirth(self):
        return self.dateOfBirth

    def setDateOfBirth(self, newDateOfBirth):
        self.dateOfBirth = newDateOfBirth

    def getCountry(self):
        return self.country

    def setCountry(self, newCountry):
        self.country = newCountry

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState

    def getCity(self):
        return self.city

    def setCity(self, newCity):
        self.city = newCity

    def getZip(self):
        return self.zip

    def setZip(self, newZip):
        self.zip = newZip

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getAdminTags(self):
        return self.adminTags

    def setAdminTags(self, newAdminTags):
        self.adminTags = newAdminTags

    def getGender(self):
        return self.gender

    def setGender(self, newGender):
        self.gender = newGender

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getIndexedPartnerDataInt(self):
        return self.indexedPartnerDataInt

    def setIndexedPartnerDataInt(self, newIndexedPartnerDataInt):
        self.indexedPartnerDataInt = newIndexedPartnerDataInt

    def getIndexedPartnerDataString(self):
        return self.indexedPartnerDataString

    def setIndexedPartnerDataString(self, newIndexedPartnerDataString):
        self.indexedPartnerDataString = newIndexedPartnerDataString

    def getStorageSize(self):
        return self.storageSize

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getIsAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, newIsAdmin):
        self.isAdmin = newIsAdmin

    def getLastLoginTime(self):
        return self.lastLoginTime

    def getStatusUpdatedAt(self):
        return self.statusUpdatedAt

    def getDeletedAt(self):
        return self.deletedAt

    def getLoginEnabled(self):
        return self.loginEnabled

    def getRoleIds(self):
        return self.roleIds

    def setRoleIds(self, newRoleIds):
        self.roleIds = newRoleIds

    def getRoleNames(self):
        return self.roleNames

    def getIsAccountOwner(self):
        return self.isAccountOwner

    def getAllowedPartnerIds(self):
        return self.allowedPartnerIds

    def setAllowedPartnerIds(self, newAllowedPartnerIds):
        self.allowedPartnerIds = newAllowedPartnerIds

    def getAllowedPartnerPackages(self):
        return self.allowedPartnerPackages

    def setAllowedPartnerPackages(self, newAllowedPartnerPackages):
        self.allowedPartnerPackages = newAllowedPartnerPackages


class KalturaAdminUser(KalturaUser):
    """DEPRECATED"""

    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            screenName=NotImplemented,
            fullName=NotImplemented,
            email=NotImplemented,
            dateOfBirth=NotImplemented,
            country=NotImplemented,
            state=NotImplemented,
            city=NotImplemented,
            zip=NotImplemented,
            thumbnailUrl=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            gender=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerData=NotImplemented,
            indexedPartnerDataInt=NotImplemented,
            indexedPartnerDataString=NotImplemented,
            storageSize=NotImplemented,
            password=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            isAdmin=NotImplemented,
            lastLoginTime=NotImplemented,
            statusUpdatedAt=NotImplemented,
            deletedAt=NotImplemented,
            loginEnabled=NotImplemented,
            roleIds=NotImplemented,
            roleNames=NotImplemented,
            isAccountOwner=NotImplemented,
            allowedPartnerIds=NotImplemented,
            allowedPartnerPackages=NotImplemented):
        KalturaUser.__init__(self,
            id,
            partnerId,
            screenName,
            fullName,
            email,
            dateOfBirth,
            country,
            state,
            city,
            zip,
            thumbnailUrl,
            description,
            tags,
            adminTags,
            gender,
            status,
            createdAt,
            updatedAt,
            partnerData,
            indexedPartnerDataInt,
            indexedPartnerDataString,
            storageSize,
            password,
            firstName,
            lastName,
            isAdmin,
            lastLoginTime,
            statusUpdatedAt,
            deletedAt,
            loginEnabled,
            roleIds,
            roleNames,
            isAccountOwner,
            allowedPartnerIds,
            allowedPartnerPackages)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUser.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdminUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUser.toParams(self)
        kparams.put("objectType", "KalturaAdminUser")
        return kparams


class KalturaDynamicEnum(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDynamicEnum.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDynamicEnum")
        return kparams


class KalturaOperationAttributes(KalturaObjectBase):
    """Base class to all operation attributes types"""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOperationAttributes.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOperationAttributes")
        return kparams


class KalturaBaseEntry(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Auto generated 10 characters alphanumeric string
        # @var string
        # @readonly
        self.id = id

        # Entry name (Min 1 chars)
        # @var string
        self.name = name

        # Entry description
        # @var string
        self.description = description

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The ID of the user who is the owner of this entry
        # @var string
        self.userId = userId

        # Entry tags
        # @var string
        self.tags = tags

        # Entry admin tags can be updated only by administrators
        # @var string
        self.adminTags = adminTags

        # @var string
        self.categories = categories

        # @var string
        self.categoriesIds = categoriesIds

        # @var KalturaEntryStatus
        # @readonly
        self.status = status

        # Entry moderation status
        # @var KalturaEntryModerationStatus
        # @readonly
        self.moderationStatus = moderationStatus

        # Number of moderation requests waiting for this entry
        # @var int
        # @readonly
        self.moderationCount = moderationCount

        # The type of the entry, this is auto filled by the derived entry object
        # @var KalturaEntryType
        self.type = type

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Entry update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # Calculated rank
        # @var float
        # @readonly
        self.rank = rank

        # The total (sum) of all votes
        # @var int
        # @readonly
        self.totalRank = totalRank

        # Number of votes
        # @var int
        # @readonly
        self.votes = votes

        # @var int
        self.groupId = groupId

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = partnerData

        # Download URL for the entry
        # @var string
        # @readonly
        self.downloadUrl = downloadUrl

        # Indexed search text for full text search
        # @var string
        # @readonly
        self.searchText = searchText

        # License type used for this entry
        # @var KalturaLicenseType
        self.licenseType = licenseType

        # Version of the entry data
        # @var int
        # @readonly
        self.version = version

        # Thumbnail URL
        # @var string
        # @insertonly
        self.thumbnailUrl = thumbnailUrl

        # The Access Control ID assigned to this entry (null when not set, send -1 to remove)
        # @var int
        self.accessControlId = accessControlId

        # Entry scheduling start date (null when not set, send -1 to remove)
        # @var int
        self.startDate = startDate

        # Entry scheduling end date (null when not set, send -1 to remove)
        # @var int
        self.endDate = endDate

        # Entry external reference id
        # @var string
        self.referenceId = referenceId

        # ID of temporary entry that will replace this entry when it's approved and ready for replacement
        # @var string
        # @readonly
        self.replacingEntryId = replacingEntryId

        # ID of the entry that will be replaced when the replacement approved and this entry is ready
        # @var string
        # @readonly
        self.replacedEntryId = replacedEntryId

        # Status of the replacement readiness and approval
        # @var KalturaEntryReplacementStatus
        # @readonly
        self.replacementStatus = replacementStatus

        # Can be used to store various partner related data as a numeric value
        # @var int
        self.partnerSortValue = partnerSortValue

        # Override the default ingestion profile
        # @var int
        self.conversionProfileId = conversionProfileId

        # ID of source root entry, used for clipped, skipped and cropped entries that created from another entry
        # @var string
        # @readonly
        self.rootEntryId = rootEntryId

        # clipping, skipping and cropping attributes that used to create this entry
        # @var array of KalturaOperationAttributes
        self.operationAttributes = operationAttributes


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'adminTags': getXmlNodeText, 
        'categories': getXmlNodeText, 
        'categoriesIds': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'moderationStatus': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationCount': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaEntryType"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'rank': getXmlNodeFloat, 
        'totalRank': getXmlNodeInt, 
        'votes': getXmlNodeInt, 
        'groupId': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'downloadUrl': getXmlNodeText, 
        'searchText': getXmlNodeText, 
        'licenseType': (KalturaEnumsFactory.createInt, "KalturaLicenseType"), 
        'version': getXmlNodeInt, 
        'thumbnailUrl': getXmlNodeText, 
        'accessControlId': getXmlNodeInt, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'referenceId': getXmlNodeText, 
        'replacingEntryId': getXmlNodeText, 
        'replacedEntryId': getXmlNodeText, 
        'replacementStatus': (KalturaEnumsFactory.createString, "KalturaEntryReplacementStatus"), 
        'partnerSortValue': getXmlNodeInt, 
        'conversionProfileId': getXmlNodeInt, 
        'rootEntryId': getXmlNodeText, 
        'operationAttributes': (KalturaObjectFactory.createArray, KalturaOperationAttributes), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseEntry")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("adminTags", self.adminTags)
        kparams.addStringIfDefined("categories", self.categories)
        kparams.addStringIfDefined("categoriesIds", self.categoriesIds)
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addIntIfDefined("groupId", self.groupId)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addIntEnumIfDefined("licenseType", self.licenseType)
        kparams.addStringIfDefined("thumbnailUrl", self.thumbnailUrl)
        kparams.addIntIfDefined("accessControlId", self.accessControlId)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addStringIfDefined("referenceId", self.referenceId)
        kparams.addIntIfDefined("partnerSortValue", self.partnerSortValue)
        kparams.addIntIfDefined("conversionProfileId", self.conversionProfileId)
        kparams.addArrayIfDefined("operationAttributes", self.operationAttributes)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getAdminTags(self):
        return self.adminTags

    def setAdminTags(self, newAdminTags):
        self.adminTags = newAdminTags

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories

    def getCategoriesIds(self):
        return self.categoriesIds

    def setCategoriesIds(self, newCategoriesIds):
        self.categoriesIds = newCategoriesIds

    def getStatus(self):
        return self.status

    def getModerationStatus(self):
        return self.moderationStatus

    def getModerationCount(self):
        return self.moderationCount

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getRank(self):
        return self.rank

    def getTotalRank(self):
        return self.totalRank

    def getVotes(self):
        return self.votes

    def getGroupId(self):
        return self.groupId

    def setGroupId(self, newGroupId):
        self.groupId = newGroupId

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getDownloadUrl(self):
        return self.downloadUrl

    def getSearchText(self):
        return self.searchText

    def getLicenseType(self):
        return self.licenseType

    def setLicenseType(self, newLicenseType):
        self.licenseType = newLicenseType

    def getVersion(self):
        return self.version

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getAccessControlId(self):
        return self.accessControlId

    def setAccessControlId(self, newAccessControlId):
        self.accessControlId = newAccessControlId

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getReferenceId(self):
        return self.referenceId

    def setReferenceId(self, newReferenceId):
        self.referenceId = newReferenceId

    def getReplacingEntryId(self):
        return self.replacingEntryId

    def getReplacedEntryId(self):
        return self.replacedEntryId

    def getReplacementStatus(self):
        return self.replacementStatus

    def getPartnerSortValue(self):
        return self.partnerSortValue

    def setPartnerSortValue(self, newPartnerSortValue):
        self.partnerSortValue = newPartnerSortValue

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getRootEntryId(self):
        return self.rootEntryId

    def getOperationAttributes(self):
        return self.operationAttributes

    def setOperationAttributes(self, newOperationAttributes):
        self.operationAttributes = newOperationAttributes


class KalturaResource(KalturaObjectBase):
    """Used to ingest entry object, as single resource or list of resources accompanied by asset params ids."""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaResource")
        return kparams


class KalturaRemotePath(KalturaObjectBase):
    def __init__(self,
            storageProfileId=NotImplemented,
            uri=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.storageProfileId = storageProfileId

        # @var string
        # @readonly
        self.uri = uri


    PROPERTY_LOADERS = {
        'storageProfileId': getXmlNodeInt, 
        'uri': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemotePath.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRemotePath")
        return kparams

    def getStorageProfileId(self):
        return self.storageProfileId

    def getUri(self):
        return self.uri


class KalturaRemotePathListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaRemotePath
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaRemotePath), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemotePathListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRemotePathListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaBaseEntryBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # This filter should be in use for retrieving only a specific entry (identified by its entryId).
        # @var string
        # @var string
        self.idEqual = idEqual

        # This filter should be in use for retrieving few specific entries (string should include comma separated list of entryId strings).
        # @var string
        # @var string
        self.idIn = idIn

        # @var string
        self.idNotIn = idNotIn

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry names (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameLike = nameLike

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry names, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameMultiLikeOr = nameMultiLikeOr

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry names, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameMultiLikeAnd = nameMultiLikeAnd

        # This filter should be in use for retrieving entries with a specific name.
        # @var string
        # @var string
        self.nameEqual = nameEqual

        # This filter should be in use for retrieving only entries which were uploaded by/assigned to users of a specific Kaltura Partner (identified by Partner ID).
        # @var int
        # @var int
        self.partnerIdEqual = partnerIdEqual

        # This filter should be in use for retrieving only entries within Kaltura network which were uploaded by/assigned to users of few Kaltura Partners  (string should include comma separated list of PartnerIDs)
        # @var string
        # @var string
        self.partnerIdIn = partnerIdIn

        # This filter parameter should be in use for retrieving only entries, uploaded by/assigned to a specific user (identified by user Id).
        # @var string
        # @var string
        self.userIdEqual = userIdEqual

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry tags (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsLike = tagsLike

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry tags set by an ADMIN user (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsLike = adminTagsLike

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, set by an ADMIN user, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsMultiLikeOr = adminTagsMultiLikeOr

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, set by an ADMIN user, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsMultiLikeAnd = adminTagsMultiLikeAnd

        # @var string
        self.categoriesMatchAnd = categoriesMatchAnd

        # @var string
        self.categoriesMatchOr = categoriesMatchOr

        # @var string
        self.categoriesIdsMatchAnd = categoriesIdsMatchAnd

        # @var string
        self.categoriesIdsMatchOr = categoriesIdsMatchOr

        # This filter should be in use for retrieving only entries, at a specific {@link ?object=KalturaEntryStatus KalturaEntryStatus}.
        # @var KalturaEntryStatus
        # @var KalturaEntryStatus
        self.statusEqual = statusEqual

        # This filter should be in use for retrieving only entries, not at a specific {@link ?object=KalturaEntryStatus KalturaEntryStatus}.
        # @var KalturaEntryStatus
        # @var KalturaEntryStatus
        self.statusNotEqual = statusNotEqual

        # This filter should be in use for retrieving only entries, at few specific {@link ?object=KalturaEntryStatus KalturaEntryStatus} (comma separated).
        # @dynamicType KalturaEntryStatus
        # @var string
        self.statusIn = statusIn

        # This filter should be in use for retrieving only entries, not at few specific {@link ?object=KalturaEntryStatus KalturaEntryStatus} (comma separated).
        # @dynamicType KalturaEntryStatus
        # @var string
        self.statusNotIn = statusNotIn

        # @var KalturaEntryModerationStatus
        self.moderationStatusEqual = moderationStatusEqual

        # @var KalturaEntryModerationStatus
        self.moderationStatusNotEqual = moderationStatusNotEqual

        # @var string
        self.moderationStatusIn = moderationStatusIn

        # @var string
        self.moderationStatusNotIn = moderationStatusNotIn

        # @var KalturaEntryType
        self.typeEqual = typeEqual

        # This filter should be in use for retrieving entries of few {@link ?object=KalturaEntryType KalturaEntryType} (string should include a comma separated list of {@link ?object=KalturaEntryType KalturaEntryType} enumerated parameters).
        # @dynamicType KalturaEntryType
        # @var string
        self.typeIn = typeIn

        # This filter parameter should be in use for retrieving only entries which were created at Kaltura system after a specific time/date (standard timestamp format).
        # @var int
        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # This filter parameter should be in use for retrieving only entries which were created at Kaltura system before a specific time/date (standard timestamp format).
        # @var int
        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.groupIdEqual = groupIdEqual

        # This filter should be in use for retrieving specific entries while search match the input string within all of the following metadata attributes: name, description, tags, adminTags.
        # @var string
        # @var string
        self.searchTextMatchAnd = searchTextMatchAnd

        # This filter should be in use for retrieving specific entries while search match the input string within at least one of the following metadata attributes: name, description, tags, adminTags.
        # @var string
        # @var string
        self.searchTextMatchOr = searchTextMatchOr

        # @var int
        self.accessControlIdEqual = accessControlIdEqual

        # @var string
        self.accessControlIdIn = accessControlIdIn

        # @var int
        self.startDateGreaterThanOrEqual = startDateGreaterThanOrEqual

        # @var int
        self.startDateLessThanOrEqual = startDateLessThanOrEqual

        # @var int
        self.startDateGreaterThanOrEqualOrNull = startDateGreaterThanOrEqualOrNull

        # @var int
        self.startDateLessThanOrEqualOrNull = startDateLessThanOrEqualOrNull

        # @var int
        self.endDateGreaterThanOrEqual = endDateGreaterThanOrEqual

        # @var int
        self.endDateLessThanOrEqual = endDateLessThanOrEqual

        # @var int
        self.endDateGreaterThanOrEqualOrNull = endDateGreaterThanOrEqualOrNull

        # @var int
        self.endDateLessThanOrEqualOrNull = endDateLessThanOrEqualOrNull

        # @var string
        self.referenceIdEqual = referenceIdEqual

        # @var string
        self.referenceIdIn = referenceIdIn

        # @var string
        self.replacingEntryIdEqual = replacingEntryIdEqual

        # @var string
        self.replacingEntryIdIn = replacingEntryIdIn

        # @var string
        self.replacedEntryIdEqual = replacedEntryIdEqual

        # @var string
        self.replacedEntryIdIn = replacedEntryIdIn

        # @var KalturaEntryReplacementStatus
        self.replacementStatusEqual = replacementStatusEqual

        # @var string
        self.replacementStatusIn = replacementStatusIn

        # @var int
        self.partnerSortValueGreaterThanOrEqual = partnerSortValueGreaterThanOrEqual

        # @var int
        self.partnerSortValueLessThanOrEqual = partnerSortValueLessThanOrEqual

        # @var string
        self.rootEntryIdEqual = rootEntryIdEqual

        # @var string
        self.rootEntryIdIn = rootEntryIdIn

        # @var string
        self.tagsNameMultiLikeOr = tagsNameMultiLikeOr

        # @var string
        self.tagsAdminTagsMultiLikeOr = tagsAdminTagsMultiLikeOr

        # @var string
        self.tagsAdminTagsNameMultiLikeOr = tagsAdminTagsNameMultiLikeOr

        # @var string
        self.tagsNameMultiLikeAnd = tagsNameMultiLikeAnd

        # @var string
        self.tagsAdminTagsMultiLikeAnd = tagsAdminTagsMultiLikeAnd

        # @var string
        self.tagsAdminTagsNameMultiLikeAnd = tagsAdminTagsNameMultiLikeAnd


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'idNotIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'nameMultiLikeOr': getXmlNodeText, 
        'nameMultiLikeAnd': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'tagsLike': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'adminTagsLike': getXmlNodeText, 
        'adminTagsMultiLikeOr': getXmlNodeText, 
        'adminTagsMultiLikeAnd': getXmlNodeText, 
        'categoriesMatchAnd': getXmlNodeText, 
        'categoriesMatchOr': getXmlNodeText, 
        'categoriesIdsMatchAnd': getXmlNodeText, 
        'categoriesIdsMatchOr': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'statusNotEqual': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
        'moderationStatusEqual': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationStatusNotEqual': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationStatusIn': getXmlNodeText, 
        'moderationStatusNotIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaEntryType"), 
        'typeIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'groupIdEqual': getXmlNodeInt, 
        'searchTextMatchAnd': getXmlNodeText, 
        'searchTextMatchOr': getXmlNodeText, 
        'accessControlIdEqual': getXmlNodeInt, 
        'accessControlIdIn': getXmlNodeText, 
        'startDateGreaterThanOrEqual': getXmlNodeInt, 
        'startDateLessThanOrEqual': getXmlNodeInt, 
        'startDateGreaterThanOrEqualOrNull': getXmlNodeInt, 
        'startDateLessThanOrEqualOrNull': getXmlNodeInt, 
        'endDateGreaterThanOrEqual': getXmlNodeInt, 
        'endDateLessThanOrEqual': getXmlNodeInt, 
        'endDateGreaterThanOrEqualOrNull': getXmlNodeInt, 
        'endDateLessThanOrEqualOrNull': getXmlNodeInt, 
        'referenceIdEqual': getXmlNodeText, 
        'referenceIdIn': getXmlNodeText, 
        'replacingEntryIdEqual': getXmlNodeText, 
        'replacingEntryIdIn': getXmlNodeText, 
        'replacedEntryIdEqual': getXmlNodeText, 
        'replacedEntryIdIn': getXmlNodeText, 
        'replacementStatusEqual': (KalturaEnumsFactory.createString, "KalturaEntryReplacementStatus"), 
        'replacementStatusIn': getXmlNodeText, 
        'partnerSortValueGreaterThanOrEqual': getXmlNodeInt, 
        'partnerSortValueLessThanOrEqual': getXmlNodeInt, 
        'rootEntryIdEqual': getXmlNodeText, 
        'rootEntryIdIn': getXmlNodeText, 
        'tagsNameMultiLikeOr': getXmlNodeText, 
        'tagsAdminTagsMultiLikeOr': getXmlNodeText, 
        'tagsAdminTagsNameMultiLikeOr': getXmlNodeText, 
        'tagsNameMultiLikeAnd': getXmlNodeText, 
        'tagsAdminTagsMultiLikeAnd': getXmlNodeText, 
        'tagsAdminTagsNameMultiLikeAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryBaseFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("idNotIn", self.idNotIn)
        kparams.addStringIfDefined("nameLike", self.nameLike)
        kparams.addStringIfDefined("nameMultiLikeOr", self.nameMultiLikeOr)
        kparams.addStringIfDefined("nameMultiLikeAnd", self.nameMultiLikeAnd)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addStringIfDefined("tagsLike", self.tagsLike)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addStringIfDefined("adminTagsLike", self.adminTagsLike)
        kparams.addStringIfDefined("adminTagsMultiLikeOr", self.adminTagsMultiLikeOr)
        kparams.addStringIfDefined("adminTagsMultiLikeAnd", self.adminTagsMultiLikeAnd)
        kparams.addStringIfDefined("categoriesMatchAnd", self.categoriesMatchAnd)
        kparams.addStringIfDefined("categoriesMatchOr", self.categoriesMatchOr)
        kparams.addStringIfDefined("categoriesIdsMatchAnd", self.categoriesIdsMatchAnd)
        kparams.addStringIfDefined("categoriesIdsMatchOr", self.categoriesIdsMatchOr)
        kparams.addStringEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringEnumIfDefined("statusNotEqual", self.statusNotEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        kparams.addIntEnumIfDefined("moderationStatusEqual", self.moderationStatusEqual)
        kparams.addIntEnumIfDefined("moderationStatusNotEqual", self.moderationStatusNotEqual)
        kparams.addStringIfDefined("moderationStatusIn", self.moderationStatusIn)
        kparams.addStringIfDefined("moderationStatusNotIn", self.moderationStatusNotIn)
        kparams.addStringEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("groupIdEqual", self.groupIdEqual)
        kparams.addStringIfDefined("searchTextMatchAnd", self.searchTextMatchAnd)
        kparams.addStringIfDefined("searchTextMatchOr", self.searchTextMatchOr)
        kparams.addIntIfDefined("accessControlIdEqual", self.accessControlIdEqual)
        kparams.addStringIfDefined("accessControlIdIn", self.accessControlIdIn)
        kparams.addIntIfDefined("startDateGreaterThanOrEqual", self.startDateGreaterThanOrEqual)
        kparams.addIntIfDefined("startDateLessThanOrEqual", self.startDateLessThanOrEqual)
        kparams.addIntIfDefined("startDateGreaterThanOrEqualOrNull", self.startDateGreaterThanOrEqualOrNull)
        kparams.addIntIfDefined("startDateLessThanOrEqualOrNull", self.startDateLessThanOrEqualOrNull)
        kparams.addIntIfDefined("endDateGreaterThanOrEqual", self.endDateGreaterThanOrEqual)
        kparams.addIntIfDefined("endDateLessThanOrEqual", self.endDateLessThanOrEqual)
        kparams.addIntIfDefined("endDateGreaterThanOrEqualOrNull", self.endDateGreaterThanOrEqualOrNull)
        kparams.addIntIfDefined("endDateLessThanOrEqualOrNull", self.endDateLessThanOrEqualOrNull)
        kparams.addStringIfDefined("referenceIdEqual", self.referenceIdEqual)
        kparams.addStringIfDefined("referenceIdIn", self.referenceIdIn)
        kparams.addStringIfDefined("replacingEntryIdEqual", self.replacingEntryIdEqual)
        kparams.addStringIfDefined("replacingEntryIdIn", self.replacingEntryIdIn)
        kparams.addStringIfDefined("replacedEntryIdEqual", self.replacedEntryIdEqual)
        kparams.addStringIfDefined("replacedEntryIdIn", self.replacedEntryIdIn)
        kparams.addStringEnumIfDefined("replacementStatusEqual", self.replacementStatusEqual)
        kparams.addStringIfDefined("replacementStatusIn", self.replacementStatusIn)
        kparams.addIntIfDefined("partnerSortValueGreaterThanOrEqual", self.partnerSortValueGreaterThanOrEqual)
        kparams.addIntIfDefined("partnerSortValueLessThanOrEqual", self.partnerSortValueLessThanOrEqual)
        kparams.addStringIfDefined("rootEntryIdEqual", self.rootEntryIdEqual)
        kparams.addStringIfDefined("rootEntryIdIn", self.rootEntryIdIn)
        kparams.addStringIfDefined("tagsNameMultiLikeOr", self.tagsNameMultiLikeOr)
        kparams.addStringIfDefined("tagsAdminTagsMultiLikeOr", self.tagsAdminTagsMultiLikeOr)
        kparams.addStringIfDefined("tagsAdminTagsNameMultiLikeOr", self.tagsAdminTagsNameMultiLikeOr)
        kparams.addStringIfDefined("tagsNameMultiLikeAnd", self.tagsNameMultiLikeAnd)
        kparams.addStringIfDefined("tagsAdminTagsMultiLikeAnd", self.tagsAdminTagsMultiLikeAnd)
        kparams.addStringIfDefined("tagsAdminTagsNameMultiLikeAnd", self.tagsAdminTagsNameMultiLikeAnd)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getIdNotIn(self):
        return self.idNotIn

    def setIdNotIn(self, newIdNotIn):
        self.idNotIn = newIdNotIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getNameMultiLikeOr(self):
        return self.nameMultiLikeOr

    def setNameMultiLikeOr(self, newNameMultiLikeOr):
        self.nameMultiLikeOr = newNameMultiLikeOr

    def getNameMultiLikeAnd(self):
        return self.nameMultiLikeAnd

    def setNameMultiLikeAnd(self, newNameMultiLikeAnd):
        self.nameMultiLikeAnd = newNameMultiLikeAnd

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

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

    def getAdminTagsLike(self):
        return self.adminTagsLike

    def setAdminTagsLike(self, newAdminTagsLike):
        self.adminTagsLike = newAdminTagsLike

    def getAdminTagsMultiLikeOr(self):
        return self.adminTagsMultiLikeOr

    def setAdminTagsMultiLikeOr(self, newAdminTagsMultiLikeOr):
        self.adminTagsMultiLikeOr = newAdminTagsMultiLikeOr

    def getAdminTagsMultiLikeAnd(self):
        return self.adminTagsMultiLikeAnd

    def setAdminTagsMultiLikeAnd(self, newAdminTagsMultiLikeAnd):
        self.adminTagsMultiLikeAnd = newAdminTagsMultiLikeAnd

    def getCategoriesMatchAnd(self):
        return self.categoriesMatchAnd

    def setCategoriesMatchAnd(self, newCategoriesMatchAnd):
        self.categoriesMatchAnd = newCategoriesMatchAnd

    def getCategoriesMatchOr(self):
        return self.categoriesMatchOr

    def setCategoriesMatchOr(self, newCategoriesMatchOr):
        self.categoriesMatchOr = newCategoriesMatchOr

    def getCategoriesIdsMatchAnd(self):
        return self.categoriesIdsMatchAnd

    def setCategoriesIdsMatchAnd(self, newCategoriesIdsMatchAnd):
        self.categoriesIdsMatchAnd = newCategoriesIdsMatchAnd

    def getCategoriesIdsMatchOr(self):
        return self.categoriesIdsMatchOr

    def setCategoriesIdsMatchOr(self, newCategoriesIdsMatchOr):
        self.categoriesIdsMatchOr = newCategoriesIdsMatchOr

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusNotEqual(self):
        return self.statusNotEqual

    def setStatusNotEqual(self, newStatusNotEqual):
        self.statusNotEqual = newStatusNotEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn

    def getModerationStatusEqual(self):
        return self.moderationStatusEqual

    def setModerationStatusEqual(self, newModerationStatusEqual):
        self.moderationStatusEqual = newModerationStatusEqual

    def getModerationStatusNotEqual(self):
        return self.moderationStatusNotEqual

    def setModerationStatusNotEqual(self, newModerationStatusNotEqual):
        self.moderationStatusNotEqual = newModerationStatusNotEqual

    def getModerationStatusIn(self):
        return self.moderationStatusIn

    def setModerationStatusIn(self, newModerationStatusIn):
        self.moderationStatusIn = newModerationStatusIn

    def getModerationStatusNotIn(self):
        return self.moderationStatusNotIn

    def setModerationStatusNotIn(self, newModerationStatusNotIn):
        self.moderationStatusNotIn = newModerationStatusNotIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

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

    def getGroupIdEqual(self):
        return self.groupIdEqual

    def setGroupIdEqual(self, newGroupIdEqual):
        self.groupIdEqual = newGroupIdEqual

    def getSearchTextMatchAnd(self):
        return self.searchTextMatchAnd

    def setSearchTextMatchAnd(self, newSearchTextMatchAnd):
        self.searchTextMatchAnd = newSearchTextMatchAnd

    def getSearchTextMatchOr(self):
        return self.searchTextMatchOr

    def setSearchTextMatchOr(self, newSearchTextMatchOr):
        self.searchTextMatchOr = newSearchTextMatchOr

    def getAccessControlIdEqual(self):
        return self.accessControlIdEqual

    def setAccessControlIdEqual(self, newAccessControlIdEqual):
        self.accessControlIdEqual = newAccessControlIdEqual

    def getAccessControlIdIn(self):
        return self.accessControlIdIn

    def setAccessControlIdIn(self, newAccessControlIdIn):
        self.accessControlIdIn = newAccessControlIdIn

    def getStartDateGreaterThanOrEqual(self):
        return self.startDateGreaterThanOrEqual

    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual):
        self.startDateGreaterThanOrEqual = newStartDateGreaterThanOrEqual

    def getStartDateLessThanOrEqual(self):
        return self.startDateLessThanOrEqual

    def setStartDateLessThanOrEqual(self, newStartDateLessThanOrEqual):
        self.startDateLessThanOrEqual = newStartDateLessThanOrEqual

    def getStartDateGreaterThanOrEqualOrNull(self):
        return self.startDateGreaterThanOrEqualOrNull

    def setStartDateGreaterThanOrEqualOrNull(self, newStartDateGreaterThanOrEqualOrNull):
        self.startDateGreaterThanOrEqualOrNull = newStartDateGreaterThanOrEqualOrNull

    def getStartDateLessThanOrEqualOrNull(self):
        return self.startDateLessThanOrEqualOrNull

    def setStartDateLessThanOrEqualOrNull(self, newStartDateLessThanOrEqualOrNull):
        self.startDateLessThanOrEqualOrNull = newStartDateLessThanOrEqualOrNull

    def getEndDateGreaterThanOrEqual(self):
        return self.endDateGreaterThanOrEqual

    def setEndDateGreaterThanOrEqual(self, newEndDateGreaterThanOrEqual):
        self.endDateGreaterThanOrEqual = newEndDateGreaterThanOrEqual

    def getEndDateLessThanOrEqual(self):
        return self.endDateLessThanOrEqual

    def setEndDateLessThanOrEqual(self, newEndDateLessThanOrEqual):
        self.endDateLessThanOrEqual = newEndDateLessThanOrEqual

    def getEndDateGreaterThanOrEqualOrNull(self):
        return self.endDateGreaterThanOrEqualOrNull

    def setEndDateGreaterThanOrEqualOrNull(self, newEndDateGreaterThanOrEqualOrNull):
        self.endDateGreaterThanOrEqualOrNull = newEndDateGreaterThanOrEqualOrNull

    def getEndDateLessThanOrEqualOrNull(self):
        return self.endDateLessThanOrEqualOrNull

    def setEndDateLessThanOrEqualOrNull(self, newEndDateLessThanOrEqualOrNull):
        self.endDateLessThanOrEqualOrNull = newEndDateLessThanOrEqualOrNull

    def getReferenceIdEqual(self):
        return self.referenceIdEqual

    def setReferenceIdEqual(self, newReferenceIdEqual):
        self.referenceIdEqual = newReferenceIdEqual

    def getReferenceIdIn(self):
        return self.referenceIdIn

    def setReferenceIdIn(self, newReferenceIdIn):
        self.referenceIdIn = newReferenceIdIn

    def getReplacingEntryIdEqual(self):
        return self.replacingEntryIdEqual

    def setReplacingEntryIdEqual(self, newReplacingEntryIdEqual):
        self.replacingEntryIdEqual = newReplacingEntryIdEqual

    def getReplacingEntryIdIn(self):
        return self.replacingEntryIdIn

    def setReplacingEntryIdIn(self, newReplacingEntryIdIn):
        self.replacingEntryIdIn = newReplacingEntryIdIn

    def getReplacedEntryIdEqual(self):
        return self.replacedEntryIdEqual

    def setReplacedEntryIdEqual(self, newReplacedEntryIdEqual):
        self.replacedEntryIdEqual = newReplacedEntryIdEqual

    def getReplacedEntryIdIn(self):
        return self.replacedEntryIdIn

    def setReplacedEntryIdIn(self, newReplacedEntryIdIn):
        self.replacedEntryIdIn = newReplacedEntryIdIn

    def getReplacementStatusEqual(self):
        return self.replacementStatusEqual

    def setReplacementStatusEqual(self, newReplacementStatusEqual):
        self.replacementStatusEqual = newReplacementStatusEqual

    def getReplacementStatusIn(self):
        return self.replacementStatusIn

    def setReplacementStatusIn(self, newReplacementStatusIn):
        self.replacementStatusIn = newReplacementStatusIn

    def getPartnerSortValueGreaterThanOrEqual(self):
        return self.partnerSortValueGreaterThanOrEqual

    def setPartnerSortValueGreaterThanOrEqual(self, newPartnerSortValueGreaterThanOrEqual):
        self.partnerSortValueGreaterThanOrEqual = newPartnerSortValueGreaterThanOrEqual

    def getPartnerSortValueLessThanOrEqual(self):
        return self.partnerSortValueLessThanOrEqual

    def setPartnerSortValueLessThanOrEqual(self, newPartnerSortValueLessThanOrEqual):
        self.partnerSortValueLessThanOrEqual = newPartnerSortValueLessThanOrEqual

    def getRootEntryIdEqual(self):
        return self.rootEntryIdEqual

    def setRootEntryIdEqual(self, newRootEntryIdEqual):
        self.rootEntryIdEqual = newRootEntryIdEqual

    def getRootEntryIdIn(self):
        return self.rootEntryIdIn

    def setRootEntryIdIn(self, newRootEntryIdIn):
        self.rootEntryIdIn = newRootEntryIdIn

    def getTagsNameMultiLikeOr(self):
        return self.tagsNameMultiLikeOr

    def setTagsNameMultiLikeOr(self, newTagsNameMultiLikeOr):
        self.tagsNameMultiLikeOr = newTagsNameMultiLikeOr

    def getTagsAdminTagsMultiLikeOr(self):
        return self.tagsAdminTagsMultiLikeOr

    def setTagsAdminTagsMultiLikeOr(self, newTagsAdminTagsMultiLikeOr):
        self.tagsAdminTagsMultiLikeOr = newTagsAdminTagsMultiLikeOr

    def getTagsAdminTagsNameMultiLikeOr(self):
        return self.tagsAdminTagsNameMultiLikeOr

    def setTagsAdminTagsNameMultiLikeOr(self, newTagsAdminTagsNameMultiLikeOr):
        self.tagsAdminTagsNameMultiLikeOr = newTagsAdminTagsNameMultiLikeOr

    def getTagsNameMultiLikeAnd(self):
        return self.tagsNameMultiLikeAnd

    def setTagsNameMultiLikeAnd(self, newTagsNameMultiLikeAnd):
        self.tagsNameMultiLikeAnd = newTagsNameMultiLikeAnd

    def getTagsAdminTagsMultiLikeAnd(self):
        return self.tagsAdminTagsMultiLikeAnd

    def setTagsAdminTagsMultiLikeAnd(self, newTagsAdminTagsMultiLikeAnd):
        self.tagsAdminTagsMultiLikeAnd = newTagsAdminTagsMultiLikeAnd

    def getTagsAdminTagsNameMultiLikeAnd(self):
        return self.tagsAdminTagsNameMultiLikeAnd

    def setTagsAdminTagsNameMultiLikeAnd(self, newTagsAdminTagsNameMultiLikeAnd):
        self.tagsAdminTagsNameMultiLikeAnd = newTagsAdminTagsNameMultiLikeAnd


class KalturaBaseEntryFilter(KalturaBaseEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented):
        KalturaBaseEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd)

        # @var string
        self.freeText = freeText

        # @var KalturaNullableBoolean
        self.isRoot = isRoot


    PROPERTY_LOADERS = {
        'freeText': getXmlNodeText, 
        'isRoot': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaBaseEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryFilter")
        kparams.addStringIfDefined("freeText", self.freeText)
        kparams.addIntEnumIfDefined("isRoot", self.isRoot)
        return kparams

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText

    def getIsRoot(self):
        return self.isRoot

    def setIsRoot(self, newIsRoot):
        self.isRoot = newIsRoot


class KalturaBaseEntryListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBaseEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBaseEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaModerationFlag(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            moderationObjectType=NotImplemented,
            flaggedEntryId=NotImplemented,
            flaggedUserId=NotImplemented,
            status=NotImplemented,
            comments=NotImplemented,
            flagType=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Moderation flag id
        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The user id that added the moderation flag
        # @var string
        # @readonly
        self.userId = userId

        # The type of the moderation flag (entry or user)
        # @var KalturaModerationObjectType
        # @readonly
        self.moderationObjectType = moderationObjectType

        # If moderation flag is set for entry, this is the flagged entry id
        # @var string
        self.flaggedEntryId = flaggedEntryId

        # If moderation flag is set for user, this is the flagged user id
        # @var string
        self.flaggedUserId = flaggedUserId

        # The moderation flag status
        # @var KalturaModerationFlagStatus
        # @readonly
        self.status = status

        # The comment that was added to the flag
        # @var string
        self.comments = comments

        # @var KalturaModerationFlagType
        self.flagType = flagType

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'moderationObjectType': (KalturaEnumsFactory.createInt, "KalturaModerationObjectType"), 
        'flaggedEntryId': getXmlNodeText, 
        'flaggedUserId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaModerationFlagStatus"), 
        'comments': getXmlNodeText, 
        'flagType': (KalturaEnumsFactory.createInt, "KalturaModerationFlagType"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaModerationFlag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaModerationFlag")
        kparams.addStringIfDefined("flaggedEntryId", self.flaggedEntryId)
        kparams.addStringIfDefined("flaggedUserId", self.flaggedUserId)
        kparams.addStringIfDefined("comments", self.comments)
        kparams.addIntEnumIfDefined("flagType", self.flagType)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def getModerationObjectType(self):
        return self.moderationObjectType

    def getFlaggedEntryId(self):
        return self.flaggedEntryId

    def setFlaggedEntryId(self, newFlaggedEntryId):
        self.flaggedEntryId = newFlaggedEntryId

    def getFlaggedUserId(self):
        return self.flaggedUserId

    def setFlaggedUserId(self, newFlaggedUserId):
        self.flaggedUserId = newFlaggedUserId

    def getStatus(self):
        return self.status

    def getComments(self):
        return self.comments

    def setComments(self, newComments):
        self.comments = newComments

    def getFlagType(self):
        return self.flagType

    def setFlagType(self, newFlagType):
        self.flagType = newFlagType

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaModerationFlagListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaModerationFlag
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaModerationFlag), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaModerationFlagListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaModerationFlagListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaEntryContextDataParams(KalturaObjectBase):
    def __init__(self,
            referrer=NotImplemented,
            flavorAssetId=NotImplemented,
            streamerType=NotImplemented,
            mediaProtocol=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.referrer = referrer

        # @var string
        self.flavorAssetId = flavorAssetId

        # @var string
        self.streamerType = streamerType

        # @var string
        self.mediaProtocol = mediaProtocol


    PROPERTY_LOADERS = {
        'referrer': getXmlNodeText, 
        'flavorAssetId': getXmlNodeText, 
        'streamerType': getXmlNodeText, 
        'mediaProtocol': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryContextDataParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryContextDataParams")
        kparams.addStringIfDefined("referrer", self.referrer)
        kparams.addStringIfDefined("flavorAssetId", self.flavorAssetId)
        kparams.addStringIfDefined("streamerType", self.streamerType)
        kparams.addStringIfDefined("mediaProtocol", self.mediaProtocol)
        return kparams

    def getReferrer(self):
        return self.referrer

    def setReferrer(self, newReferrer):
        self.referrer = newReferrer

    def getFlavorAssetId(self):
        return self.flavorAssetId

    def setFlavorAssetId(self, newFlavorAssetId):
        self.flavorAssetId = newFlavorAssetId

    def getStreamerType(self):
        return self.streamerType

    def setStreamerType(self, newStreamerType):
        self.streamerType = newStreamerType

    def getMediaProtocol(self):
        return self.mediaProtocol

    def setMediaProtocol(self, newMediaProtocol):
        self.mediaProtocol = newMediaProtocol


class KalturaEntryContextDataResult(KalturaObjectBase):
    def __init__(self,
            isSiteRestricted=NotImplemented,
            isCountryRestricted=NotImplemented,
            isSessionRestricted=NotImplemented,
            isIpAddressRestricted=NotImplemented,
            isUserAgentRestricted=NotImplemented,
            previewLength=NotImplemented,
            isScheduledNow=NotImplemented,
            isAdmin=NotImplemented,
            streamerType=NotImplemented,
            mediaProtocol=NotImplemented,
            storageProfilesXML=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var bool
        self.isSiteRestricted = isSiteRestricted

        # @var bool
        self.isCountryRestricted = isCountryRestricted

        # @var bool
        self.isSessionRestricted = isSessionRestricted

        # @var bool
        self.isIpAddressRestricted = isIpAddressRestricted

        # @var bool
        self.isUserAgentRestricted = isUserAgentRestricted

        # @var int
        self.previewLength = previewLength

        # @var bool
        self.isScheduledNow = isScheduledNow

        # @var bool
        self.isAdmin = isAdmin

        # http/rtmp/hdnetwork
        # @var string
        self.streamerType = streamerType

        # http/https, rtmp/rtmpe
        # @var string
        self.mediaProtocol = mediaProtocol

        # @var string
        self.storageProfilesXML = storageProfilesXML


    PROPERTY_LOADERS = {
        'isSiteRestricted': getXmlNodeBool, 
        'isCountryRestricted': getXmlNodeBool, 
        'isSessionRestricted': getXmlNodeBool, 
        'isIpAddressRestricted': getXmlNodeBool, 
        'isUserAgentRestricted': getXmlNodeBool, 
        'previewLength': getXmlNodeInt, 
        'isScheduledNow': getXmlNodeBool, 
        'isAdmin': getXmlNodeBool, 
        'streamerType': getXmlNodeText, 
        'mediaProtocol': getXmlNodeText, 
        'storageProfilesXML': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryContextDataResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryContextDataResult")
        kparams.addBoolIfDefined("isSiteRestricted", self.isSiteRestricted)
        kparams.addBoolIfDefined("isCountryRestricted", self.isCountryRestricted)
        kparams.addBoolIfDefined("isSessionRestricted", self.isSessionRestricted)
        kparams.addBoolIfDefined("isIpAddressRestricted", self.isIpAddressRestricted)
        kparams.addBoolIfDefined("isUserAgentRestricted", self.isUserAgentRestricted)
        kparams.addIntIfDefined("previewLength", self.previewLength)
        kparams.addBoolIfDefined("isScheduledNow", self.isScheduledNow)
        kparams.addBoolIfDefined("isAdmin", self.isAdmin)
        kparams.addStringIfDefined("streamerType", self.streamerType)
        kparams.addStringIfDefined("mediaProtocol", self.mediaProtocol)
        kparams.addStringIfDefined("storageProfilesXML", self.storageProfilesXML)
        return kparams

    def getIsSiteRestricted(self):
        return self.isSiteRestricted

    def setIsSiteRestricted(self, newIsSiteRestricted):
        self.isSiteRestricted = newIsSiteRestricted

    def getIsCountryRestricted(self):
        return self.isCountryRestricted

    def setIsCountryRestricted(self, newIsCountryRestricted):
        self.isCountryRestricted = newIsCountryRestricted

    def getIsSessionRestricted(self):
        return self.isSessionRestricted

    def setIsSessionRestricted(self, newIsSessionRestricted):
        self.isSessionRestricted = newIsSessionRestricted

    def getIsIpAddressRestricted(self):
        return self.isIpAddressRestricted

    def setIsIpAddressRestricted(self, newIsIpAddressRestricted):
        self.isIpAddressRestricted = newIsIpAddressRestricted

    def getIsUserAgentRestricted(self):
        return self.isUserAgentRestricted

    def setIsUserAgentRestricted(self, newIsUserAgentRestricted):
        self.isUserAgentRestricted = newIsUserAgentRestricted

    def getPreviewLength(self):
        return self.previewLength

    def setPreviewLength(self, newPreviewLength):
        self.previewLength = newPreviewLength

    def getIsScheduledNow(self):
        return self.isScheduledNow

    def setIsScheduledNow(self, newIsScheduledNow):
        self.isScheduledNow = newIsScheduledNow

    def getIsAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, newIsAdmin):
        self.isAdmin = newIsAdmin

    def getStreamerType(self):
        return self.streamerType

    def setStreamerType(self, newStreamerType):
        self.streamerType = newStreamerType

    def getMediaProtocol(self):
        return self.mediaProtocol

    def setMediaProtocol(self, newMediaProtocol):
        self.mediaProtocol = newMediaProtocol

    def getStorageProfilesXML(self):
        return self.storageProfilesXML

    def setStorageProfilesXML(self, newStorageProfilesXML):
        self.storageProfilesXML = newStorageProfilesXML


class KalturaBulkUploadPluginData(KalturaObjectBase):
    def __init__(self,
            field=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.field = field

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'field': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadPluginData")
        kparams.addStringIfDefined("field", self.field)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getField(self):
        return self.field

    def setField(self, newField):
        self.field = newField

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaBulkUploadResult(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            bulkUploadJobId=NotImplemented,
            lineIndex=NotImplemented,
            partnerId=NotImplemented,
            action=NotImplemented,
            entryId=NotImplemented,
            objectId=NotImplemented,
            bulkUploadResultObjectType=NotImplemented,
            entryStatus=NotImplemented,
            rowData=NotImplemented,
            title=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            url=NotImplemented,
            contentType=NotImplemented,
            conversionProfileId=NotImplemented,
            accessControlProfileId=NotImplemented,
            category=NotImplemented,
            scheduleStartDate=NotImplemented,
            scheduleEndDate=NotImplemented,
            thumbnailUrl=NotImplemented,
            thumbnailSaved=NotImplemented,
            partnerData=NotImplemented,
            errorDescription=NotImplemented,
            pluginsData=NotImplemented,
            sshPrivateKey=NotImplemented,
            sshPublicKey=NotImplemented,
            sshKeyPassphrase=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the result
        # @var int
        # @readonly
        self.id = id

        # The id of the parent job
        # @var int
        self.bulkUploadJobId = bulkUploadJobId

        # The index of the line in the CSV
        # @var int
        self.lineIndex = lineIndex

        # @var int
        self.partnerId = partnerId

        # @var KalturaBulkUploadAction
        self.action = action

        # @var string
        self.entryId = entryId

        # @var string
        self.objectId = objectId

        # @var KalturaBulkUploadResultObjectType
        self.bulkUploadResultObjectType = bulkUploadResultObjectType

        # @var int
        self.entryStatus = entryStatus

        # The data as recieved in the csv
        # @var string
        self.rowData = rowData

        # @var string
        self.title = title

        # @var string
        self.description = description

        # @var string
        self.tags = tags

        # @var string
        self.url = url

        # @var string
        self.contentType = contentType

        # @var int
        self.conversionProfileId = conversionProfileId

        # @var int
        self.accessControlProfileId = accessControlProfileId

        # @var string
        self.category = category

        # @var int
        self.scheduleStartDate = scheduleStartDate

        # @var int
        self.scheduleEndDate = scheduleEndDate

        # @var string
        self.thumbnailUrl = thumbnailUrl

        # @var bool
        self.thumbnailSaved = thumbnailSaved

        # @var string
        self.partnerData = partnerData

        # @var string
        self.errorDescription = errorDescription

        # @var array of KalturaBulkUploadPluginData
        self.pluginsData = pluginsData

        # @var string
        self.sshPrivateKey = sshPrivateKey

        # @var string
        self.sshPublicKey = sshPublicKey

        # @var string
        self.sshKeyPassphrase = sshKeyPassphrase


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'bulkUploadJobId': getXmlNodeInt, 
        'lineIndex': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'action': (KalturaEnumsFactory.createInt, "KalturaBulkUploadAction"), 
        'entryId': getXmlNodeText, 
        'objectId': getXmlNodeText, 
        'bulkUploadResultObjectType': (KalturaEnumsFactory.createString, "KalturaBulkUploadResultObjectType"), 
        'entryStatus': getXmlNodeInt, 
        'rowData': getXmlNodeText, 
        'title': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'url': getXmlNodeText, 
        'contentType': getXmlNodeText, 
        'conversionProfileId': getXmlNodeInt, 
        'accessControlProfileId': getXmlNodeInt, 
        'category': getXmlNodeText, 
        'scheduleStartDate': getXmlNodeInt, 
        'scheduleEndDate': getXmlNodeInt, 
        'thumbnailUrl': getXmlNodeText, 
        'thumbnailSaved': getXmlNodeBool, 
        'partnerData': getXmlNodeText, 
        'errorDescription': getXmlNodeText, 
        'pluginsData': (KalturaObjectFactory.createArray, KalturaBulkUploadPluginData), 
        'sshPrivateKey': getXmlNodeText, 
        'sshPublicKey': getXmlNodeText, 
        'sshKeyPassphrase': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadResult")
        kparams.addIntIfDefined("bulkUploadJobId", self.bulkUploadJobId)
        kparams.addIntIfDefined("lineIndex", self.lineIndex)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addIntEnumIfDefined("action", self.action)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("objectId", self.objectId)
        kparams.addStringEnumIfDefined("bulkUploadResultObjectType", self.bulkUploadResultObjectType)
        kparams.addIntIfDefined("entryStatus", self.entryStatus)
        kparams.addStringIfDefined("rowData", self.rowData)
        kparams.addStringIfDefined("title", self.title)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("url", self.url)
        kparams.addStringIfDefined("contentType", self.contentType)
        kparams.addIntIfDefined("conversionProfileId", self.conversionProfileId)
        kparams.addIntIfDefined("accessControlProfileId", self.accessControlProfileId)
        kparams.addStringIfDefined("category", self.category)
        kparams.addIntIfDefined("scheduleStartDate", self.scheduleStartDate)
        kparams.addIntIfDefined("scheduleEndDate", self.scheduleEndDate)
        kparams.addStringIfDefined("thumbnailUrl", self.thumbnailUrl)
        kparams.addBoolIfDefined("thumbnailSaved", self.thumbnailSaved)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addStringIfDefined("errorDescription", self.errorDescription)
        kparams.addArrayIfDefined("pluginsData", self.pluginsData)
        kparams.addStringIfDefined("sshPrivateKey", self.sshPrivateKey)
        kparams.addStringIfDefined("sshPublicKey", self.sshPublicKey)
        kparams.addStringIfDefined("sshKeyPassphrase", self.sshKeyPassphrase)
        return kparams

    def getId(self):
        return self.id

    def getBulkUploadJobId(self):
        return self.bulkUploadJobId

    def setBulkUploadJobId(self, newBulkUploadJobId):
        self.bulkUploadJobId = newBulkUploadJobId

    def getLineIndex(self):
        return self.lineIndex

    def setLineIndex(self, newLineIndex):
        self.lineIndex = newLineIndex

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getBulkUploadResultObjectType(self):
        return self.bulkUploadResultObjectType

    def setBulkUploadResultObjectType(self, newBulkUploadResultObjectType):
        self.bulkUploadResultObjectType = newBulkUploadResultObjectType

    def getEntryStatus(self):
        return self.entryStatus

    def setEntryStatus(self, newEntryStatus):
        self.entryStatus = newEntryStatus

    def getRowData(self):
        return self.rowData

    def setRowData(self, newRowData):
        self.rowData = newRowData

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getContentType(self):
        return self.contentType

    def setContentType(self, newContentType):
        self.contentType = newContentType

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getAccessControlProfileId(self):
        return self.accessControlProfileId

    def setAccessControlProfileId(self, newAccessControlProfileId):
        self.accessControlProfileId = newAccessControlProfileId

    def getCategory(self):
        return self.category

    def setCategory(self, newCategory):
        self.category = newCategory

    def getScheduleStartDate(self):
        return self.scheduleStartDate

    def setScheduleStartDate(self, newScheduleStartDate):
        self.scheduleStartDate = newScheduleStartDate

    def getScheduleEndDate(self):
        return self.scheduleEndDate

    def setScheduleEndDate(self, newScheduleEndDate):
        self.scheduleEndDate = newScheduleEndDate

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getThumbnailSaved(self):
        return self.thumbnailSaved

    def setThumbnailSaved(self, newThumbnailSaved):
        self.thumbnailSaved = newThumbnailSaved

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, newErrorDescription):
        self.errorDescription = newErrorDescription

    def getPluginsData(self):
        return self.pluginsData

    def setPluginsData(self, newPluginsData):
        self.pluginsData = newPluginsData

    def getSshPrivateKey(self):
        return self.sshPrivateKey

    def setSshPrivateKey(self, newSshPrivateKey):
        self.sshPrivateKey = newSshPrivateKey

    def getSshPublicKey(self):
        return self.sshPublicKey

    def setSshPublicKey(self, newSshPublicKey):
        self.sshPublicKey = newSshPublicKey

    def getSshKeyPassphrase(self):
        return self.sshKeyPassphrase

    def setSshKeyPassphrase(self, newSshKeyPassphrase):
        self.sshKeyPassphrase = newSshKeyPassphrase


class KalturaBulkUpload(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            uploadedBy=NotImplemented,
            uploadedByUserId=NotImplemented,
            uploadedOn=NotImplemented,
            numOfEntries=NotImplemented,
            status=NotImplemented,
            logFileUrl=NotImplemented,
            csvFileUrl=NotImplemented,
            bulkFileUrl=NotImplemented,
            bulkUploadType=NotImplemented,
            results=NotImplemented,
            error=NotImplemented,
            errorType=NotImplemented,
            errorNumber=NotImplemented,
            fileName=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = id

        # @var string
        self.uploadedBy = uploadedBy

        # @var string
        self.uploadedByUserId = uploadedByUserId

        # @var int
        self.uploadedOn = uploadedOn

        # @var int
        self.numOfEntries = numOfEntries

        # @var KalturaBatchJobStatus
        self.status = status

        # @var string
        self.logFileUrl = logFileUrl

        # DEPRECATED
        # @var string
        self.csvFileUrl = csvFileUrl

        # @var string
        self.bulkFileUrl = bulkFileUrl

        # @var KalturaBulkUploadType
        self.bulkUploadType = bulkUploadType

        # @var array of KalturaBulkUploadResult
        self.results = results

        # @var string
        self.error = error

        # @var KalturaBatchJobErrorTypes
        self.errorType = errorType

        # @var int
        self.errorNumber = errorNumber

        # @var string
        self.fileName = fileName

        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'uploadedBy': getXmlNodeText, 
        'uploadedByUserId': getXmlNodeText, 
        'uploadedOn': getXmlNodeInt, 
        'numOfEntries': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaBatchJobStatus"), 
        'logFileUrl': getXmlNodeText, 
        'csvFileUrl': getXmlNodeText, 
        'bulkFileUrl': getXmlNodeText, 
        'bulkUploadType': (KalturaEnumsFactory.createString, "KalturaBulkUploadType"), 
        'results': (KalturaObjectFactory.createArray, KalturaBulkUploadResult), 
        'error': getXmlNodeText, 
        'errorType': (KalturaEnumsFactory.createInt, "KalturaBatchJobErrorTypes"), 
        'errorNumber': getXmlNodeInt, 
        'fileName': getXmlNodeText, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUpload.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUpload")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("uploadedBy", self.uploadedBy)
        kparams.addStringIfDefined("uploadedByUserId", self.uploadedByUserId)
        kparams.addIntIfDefined("uploadedOn", self.uploadedOn)
        kparams.addIntIfDefined("numOfEntries", self.numOfEntries)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("logFileUrl", self.logFileUrl)
        kparams.addStringIfDefined("csvFileUrl", self.csvFileUrl)
        kparams.addStringIfDefined("bulkFileUrl", self.bulkFileUrl)
        kparams.addStringEnumIfDefined("bulkUploadType", self.bulkUploadType)
        kparams.addArrayIfDefined("results", self.results)
        kparams.addStringIfDefined("error", self.error)
        kparams.addIntEnumIfDefined("errorType", self.errorType)
        kparams.addIntIfDefined("errorNumber", self.errorNumber)
        kparams.addStringIfDefined("fileName", self.fileName)
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getUploadedBy(self):
        return self.uploadedBy

    def setUploadedBy(self, newUploadedBy):
        self.uploadedBy = newUploadedBy

    def getUploadedByUserId(self):
        return self.uploadedByUserId

    def setUploadedByUserId(self, newUploadedByUserId):
        self.uploadedByUserId = newUploadedByUserId

    def getUploadedOn(self):
        return self.uploadedOn

    def setUploadedOn(self, newUploadedOn):
        self.uploadedOn = newUploadedOn

    def getNumOfEntries(self):
        return self.numOfEntries

    def setNumOfEntries(self, newNumOfEntries):
        self.numOfEntries = newNumOfEntries

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getLogFileUrl(self):
        return self.logFileUrl

    def setLogFileUrl(self, newLogFileUrl):
        self.logFileUrl = newLogFileUrl

    def getCsvFileUrl(self):
        return self.csvFileUrl

    def setCsvFileUrl(self, newCsvFileUrl):
        self.csvFileUrl = newCsvFileUrl

    def getBulkFileUrl(self):
        return self.bulkFileUrl

    def setBulkFileUrl(self, newBulkFileUrl):
        self.bulkFileUrl = newBulkFileUrl

    def getBulkUploadType(self):
        return self.bulkUploadType

    def setBulkUploadType(self, newBulkUploadType):
        self.bulkUploadType = newBulkUploadType

    def getResults(self):
        return self.results

    def setResults(self, newResults):
        self.results = newResults

    def getError(self):
        return self.error

    def setError(self, newError):
        self.error = newError

    def getErrorType(self):
        return self.errorType

    def setErrorType(self, newErrorType):
        self.errorType = newErrorType

    def getErrorNumber(self):
        return self.errorNumber

    def setErrorNumber(self, newErrorNumber):
        self.errorNumber = newErrorNumber

    def getFileName(self):
        return self.fileName

    def setFileName(self, newFileName):
        self.fileName = newFileName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


class KalturaBulkUploadListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBulkUpload
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBulkUpload), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaCategory(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            parentId=NotImplemented,
            depth=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            fullName=NotImplemented,
            entriesCount=NotImplemented,
            createdAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the Category
        # @var int
        # @readonly
        self.id = id

        # @var int
        self.parentId = parentId

        # @var int
        # @readonly
        self.depth = depth

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The name of the Category. 
        # The following characters are not allowed: '<', '>', ','
        # @var string
        self.name = name

        # The full name of the Category
        # @var string
        # @readonly
        self.fullName = fullName

        # Number of entries in this Category (including child categories)
        # @var int
        # @readonly
        self.entriesCount = entriesCount

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'parentId': getXmlNodeInt, 
        'depth': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'fullName': getXmlNodeText, 
        'entriesCount': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCategory")
        kparams.addIntIfDefined("parentId", self.parentId)
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getDepth(self):
        return self.depth

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFullName(self):
        return self.fullName

    def getEntriesCount(self):
        return self.entriesCount

    def getCreatedAt(self):
        return self.createdAt


class KalturaCategoryBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            parentIdEqual=NotImplemented,
            parentIdIn=NotImplemented,
            depthEqual=NotImplemented,
            fullNameEqual=NotImplemented,
            fullNameStartsWith=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.parentIdEqual = parentIdEqual

        # @var string
        self.parentIdIn = parentIdIn

        # @var int
        self.depthEqual = depthEqual

        # @var string
        self.fullNameEqual = fullNameEqual

        # @var string
        self.fullNameStartsWith = fullNameStartsWith


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'parentIdEqual': getXmlNodeInt, 
        'parentIdIn': getXmlNodeText, 
        'depthEqual': getXmlNodeInt, 
        'fullNameEqual': getXmlNodeText, 
        'fullNameStartsWith': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaCategoryBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("parentIdEqual", self.parentIdEqual)
        kparams.addStringIfDefined("parentIdIn", self.parentIdIn)
        kparams.addIntIfDefined("depthEqual", self.depthEqual)
        kparams.addStringIfDefined("fullNameEqual", self.fullNameEqual)
        kparams.addStringIfDefined("fullNameStartsWith", self.fullNameStartsWith)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getParentIdEqual(self):
        return self.parentIdEqual

    def setParentIdEqual(self, newParentIdEqual):
        self.parentIdEqual = newParentIdEqual

    def getParentIdIn(self):
        return self.parentIdIn

    def setParentIdIn(self, newParentIdIn):
        self.parentIdIn = newParentIdIn

    def getDepthEqual(self):
        return self.depthEqual

    def setDepthEqual(self, newDepthEqual):
        self.depthEqual = newDepthEqual

    def getFullNameEqual(self):
        return self.fullNameEqual

    def setFullNameEqual(self, newFullNameEqual):
        self.fullNameEqual = newFullNameEqual

    def getFullNameStartsWith(self):
        return self.fullNameStartsWith

    def setFullNameStartsWith(self, newFullNameStartsWith):
        self.fullNameStartsWith = newFullNameStartsWith


class KalturaCategoryFilter(KalturaCategoryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            parentIdEqual=NotImplemented,
            parentIdIn=NotImplemented,
            depthEqual=NotImplemented,
            fullNameEqual=NotImplemented,
            fullNameStartsWith=NotImplemented):
        KalturaCategoryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            parentIdEqual,
            parentIdIn,
            depthEqual,
            fullNameEqual,
            fullNameStartsWith)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCategoryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCategoryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCategoryFilter")
        return kparams


class KalturaCategoryListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaCategory
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaCategory), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCategoryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaConversionProfileAssetParamsBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            assetParamsIdEqual=NotImplemented,
            assetParamsIdIn=NotImplemented,
            readyBehaviorEqual=NotImplemented,
            readyBehaviorIn=NotImplemented,
            originEqual=NotImplemented,
            originIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.conversionProfileIdEqual = conversionProfileIdEqual

        # @var string
        self.conversionProfileIdIn = conversionProfileIdIn

        # @var int
        self.assetParamsIdEqual = assetParamsIdEqual

        # @var string
        self.assetParamsIdIn = assetParamsIdIn

        # @var KalturaFlavorReadyBehaviorType
        self.readyBehaviorEqual = readyBehaviorEqual

        # @var string
        self.readyBehaviorIn = readyBehaviorIn

        # @var KalturaAssetParamsOrigin
        self.originEqual = originEqual

        # @var string
        self.originIn = originIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn


    PROPERTY_LOADERS = {
        'conversionProfileIdEqual': getXmlNodeInt, 
        'conversionProfileIdIn': getXmlNodeText, 
        'assetParamsIdEqual': getXmlNodeInt, 
        'assetParamsIdIn': getXmlNodeText, 
        'readyBehaviorEqual': (KalturaEnumsFactory.createInt, "KalturaFlavorReadyBehaviorType"), 
        'readyBehaviorIn': getXmlNodeText, 
        'originEqual': (KalturaEnumsFactory.createInt, "KalturaAssetParamsOrigin"), 
        'originIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileAssetParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileAssetParamsBaseFilter")
        kparams.addIntIfDefined("conversionProfileIdEqual", self.conversionProfileIdEqual)
        kparams.addStringIfDefined("conversionProfileIdIn", self.conversionProfileIdIn)
        kparams.addIntIfDefined("assetParamsIdEqual", self.assetParamsIdEqual)
        kparams.addStringIfDefined("assetParamsIdIn", self.assetParamsIdIn)
        kparams.addIntEnumIfDefined("readyBehaviorEqual", self.readyBehaviorEqual)
        kparams.addStringIfDefined("readyBehaviorIn", self.readyBehaviorIn)
        kparams.addIntEnumIfDefined("originEqual", self.originEqual)
        kparams.addStringIfDefined("originIn", self.originIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        return kparams

    def getConversionProfileIdEqual(self):
        return self.conversionProfileIdEqual

    def setConversionProfileIdEqual(self, newConversionProfileIdEqual):
        self.conversionProfileIdEqual = newConversionProfileIdEqual

    def getConversionProfileIdIn(self):
        return self.conversionProfileIdIn

    def setConversionProfileIdIn(self, newConversionProfileIdIn):
        self.conversionProfileIdIn = newConversionProfileIdIn

    def getAssetParamsIdEqual(self):
        return self.assetParamsIdEqual

    def setAssetParamsIdEqual(self, newAssetParamsIdEqual):
        self.assetParamsIdEqual = newAssetParamsIdEqual

    def getAssetParamsIdIn(self):
        return self.assetParamsIdIn

    def setAssetParamsIdIn(self, newAssetParamsIdIn):
        self.assetParamsIdIn = newAssetParamsIdIn

    def getReadyBehaviorEqual(self):
        return self.readyBehaviorEqual

    def setReadyBehaviorEqual(self, newReadyBehaviorEqual):
        self.readyBehaviorEqual = newReadyBehaviorEqual

    def getReadyBehaviorIn(self):
        return self.readyBehaviorIn

    def setReadyBehaviorIn(self, newReadyBehaviorIn):
        self.readyBehaviorIn = newReadyBehaviorIn

    def getOriginEqual(self):
        return self.originEqual

    def setOriginEqual(self, newOriginEqual):
        self.originEqual = newOriginEqual

    def getOriginIn(self):
        return self.originIn

    def setOriginIn(self, newOriginIn):
        self.originIn = newOriginIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn


class KalturaConversionProfileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            nameEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            defaultEntryIdEqual=NotImplemented,
            defaultEntryIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var KalturaConversionProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var string
        self.defaultEntryIdEqual = defaultEntryIdEqual

        # @var string
        self.defaultEntryIdIn = defaultEntryIdIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaConversionProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'defaultEntryIdEqual': getXmlNodeText, 
        'defaultEntryIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addStringIfDefined("defaultEntryIdEqual", self.defaultEntryIdEqual)
        kparams.addStringIfDefined("defaultEntryIdIn", self.defaultEntryIdIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getDefaultEntryIdEqual(self):
        return self.defaultEntryIdEqual

    def setDefaultEntryIdEqual(self, newDefaultEntryIdEqual):
        self.defaultEntryIdEqual = newDefaultEntryIdEqual

    def getDefaultEntryIdIn(self):
        return self.defaultEntryIdIn

    def setDefaultEntryIdIn(self, newDefaultEntryIdIn):
        self.defaultEntryIdIn = newDefaultEntryIdIn


class KalturaConversionProfileFilter(KalturaConversionProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            nameEqual=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            defaultEntryIdEqual=NotImplemented,
            defaultEntryIdIn=NotImplemented):
        KalturaConversionProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            statusEqual,
            statusIn,
            nameEqual,
            systemNameEqual,
            systemNameIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            defaultEntryIdEqual,
            defaultEntryIdIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConversionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConversionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileFilter")
        return kparams


class KalturaAssetParamsBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var KalturaNullableBoolean
        self.isSystemDefaultEqual = isSystemDefaultEqual

        # @var string
        self.tagsEqual = tagsEqual


    PROPERTY_LOADERS = {
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'isSystemDefaultEqual': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'tagsEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsBaseFilter")
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntEnumIfDefined("isSystemDefaultEqual", self.isSystemDefaultEqual)
        kparams.addStringIfDefined("tagsEqual", self.tagsEqual)
        return kparams

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getIsSystemDefaultEqual(self):
        return self.isSystemDefaultEqual

    def setIsSystemDefaultEqual(self, newIsSystemDefaultEqual):
        self.isSystemDefaultEqual = newIsSystemDefaultEqual

    def getTagsEqual(self):
        return self.tagsEqual

    def setTagsEqual(self, newTagsEqual):
        self.tagsEqual = newTagsEqual


class KalturaAssetParamsFilter(KalturaAssetParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented):
        KalturaAssetParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsFilter")
        return kparams


class KalturaConversionProfileAssetParamsFilter(KalturaConversionProfileAssetParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            conversionProfileIdEqual=NotImplemented,
            conversionProfileIdIn=NotImplemented,
            assetParamsIdEqual=NotImplemented,
            assetParamsIdIn=NotImplemented,
            readyBehaviorEqual=NotImplemented,
            readyBehaviorIn=NotImplemented,
            originEqual=NotImplemented,
            originIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            conversionProfileIdFilter=NotImplemented,
            assetParamsIdFilter=NotImplemented):
        KalturaConversionProfileAssetParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            assetParamsIdEqual,
            assetParamsIdIn,
            readyBehaviorEqual,
            readyBehaviorIn,
            originEqual,
            originIn,
            systemNameEqual,
            systemNameIn)

        # @var KalturaConversionProfileFilter
        self.conversionProfileIdFilter = conversionProfileIdFilter

        # @var KalturaAssetParamsFilter
        self.assetParamsIdFilter = assetParamsIdFilter


    PROPERTY_LOADERS = {
        'conversionProfileIdFilter': (KalturaObjectFactory.create, KalturaConversionProfileFilter), 
        'assetParamsIdFilter': (KalturaObjectFactory.create, KalturaAssetParamsFilter), 
    }

    def fromXml(self, node):
        KalturaConversionProfileAssetParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileAssetParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConversionProfileAssetParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileAssetParamsFilter")
        kparams.addObjectIfDefined("conversionProfileIdFilter", self.conversionProfileIdFilter)
        kparams.addObjectIfDefined("assetParamsIdFilter", self.assetParamsIdFilter)
        return kparams

    def getConversionProfileIdFilter(self):
        return self.conversionProfileIdFilter

    def setConversionProfileIdFilter(self, newConversionProfileIdFilter):
        self.conversionProfileIdFilter = newConversionProfileIdFilter

    def getAssetParamsIdFilter(self):
        return self.assetParamsIdFilter

    def setAssetParamsIdFilter(self, newAssetParamsIdFilter):
        self.assetParamsIdFilter = newAssetParamsIdFilter


class KalturaConversionProfileAssetParams(KalturaObjectBase):
    def __init__(self,
            conversionProfileId=NotImplemented,
            assetParamsId=NotImplemented,
            readyBehavior=NotImplemented,
            origin=NotImplemented,
            systemName=NotImplemented,
            forceNoneComplied=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the conversion profile
        # @var int
        # @readonly
        self.conversionProfileId = conversionProfileId

        # The id of the asset params
        # @var int
        # @readonly
        self.assetParamsId = assetParamsId

        # The ingestion origin of the asset params
        # @var KalturaFlavorReadyBehaviorType
        self.readyBehavior = readyBehavior

        # The ingestion origin of the asset params
        # @var KalturaAssetParamsOrigin
        self.origin = origin

        # Asset params system name
        # @var string
        self.systemName = systemName

        # Starts conversion even if the decision layer reduced the configuration to comply with the source
        # @var KalturaNullableBoolean
        self.forceNoneComplied = forceNoneComplied


    PROPERTY_LOADERS = {
        'conversionProfileId': getXmlNodeInt, 
        'assetParamsId': getXmlNodeInt, 
        'readyBehavior': (KalturaEnumsFactory.createInt, "KalturaFlavorReadyBehaviorType"), 
        'origin': (KalturaEnumsFactory.createInt, "KalturaAssetParamsOrigin"), 
        'systemName': getXmlNodeText, 
        'forceNoneComplied': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileAssetParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileAssetParams")
        kparams.addIntEnumIfDefined("readyBehavior", self.readyBehavior)
        kparams.addIntEnumIfDefined("origin", self.origin)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addIntEnumIfDefined("forceNoneComplied", self.forceNoneComplied)
        return kparams

    def getConversionProfileId(self):
        return self.conversionProfileId

    def getAssetParamsId(self):
        return self.assetParamsId

    def getReadyBehavior(self):
        return self.readyBehavior

    def setReadyBehavior(self, newReadyBehavior):
        self.readyBehavior = newReadyBehavior

    def getOrigin(self):
        return self.origin

    def setOrigin(self, newOrigin):
        self.origin = newOrigin

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getForceNoneComplied(self):
        return self.forceNoneComplied

    def setForceNoneComplied(self, newForceNoneComplied):
        self.forceNoneComplied = newForceNoneComplied


class KalturaConversionProfileAssetParamsListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaConversionProfileAssetParams
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaConversionProfileAssetParams), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileAssetParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileAssetParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaCropDimensions(KalturaObjectBase):
    def __init__(self,
            left=NotImplemented,
            top=NotImplemented,
            width=NotImplemented,
            height=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Crop left point
        # @var int
        self.left = left

        # Crop top point
        # @var int
        self.top = top

        # Crop width
        # @var int
        self.width = width

        # Crop height
        # @var int
        self.height = height


    PROPERTY_LOADERS = {
        'left': getXmlNodeInt, 
        'top': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCropDimensions.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCropDimensions")
        kparams.addIntIfDefined("left", self.left)
        kparams.addIntIfDefined("top", self.top)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        return kparams

    def getLeft(self):
        return self.left

    def setLeft(self, newLeft):
        self.left = newLeft

    def getTop(self):
        return self.top

    def setTop(self, newTop):
        self.top = newTop

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight


class KalturaConversionProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            status=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            tags=NotImplemented,
            description=NotImplemented,
            defaultEntryId=NotImplemented,
            createdAt=NotImplemented,
            flavorParamsIds=NotImplemented,
            isDefault=NotImplemented,
            isPartnerDefault=NotImplemented,
            cropDimensions=NotImplemented,
            clipStart=NotImplemented,
            clipDuration=NotImplemented,
            xslTransformation=NotImplemented,
            storageProfileId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the Conversion Profile
        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var KalturaConversionProfileStatus
        self.status = status

        # The name of the Conversion Profile
        # @var string
        self.name = name

        # System name of the Conversion Profile
        # @var string
        self.systemName = systemName

        # Comma separated tags
        # @var string
        self.tags = tags

        # The description of the Conversion Profile
        # @var string
        self.description = description

        # ID of the default entry to be used for template data
        # @var string
        self.defaultEntryId = defaultEntryId

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # List of included flavor ids (comma separated)
        # @var string
        self.flavorParamsIds = flavorParamsIds

        # Indicates that this conversion profile is system default
        # @var KalturaNullableBoolean
        self.isDefault = isDefault

        # Indicates that this conversion profile is partner default
        # @var bool
        # @readonly
        self.isPartnerDefault = isPartnerDefault

        # Cropping dimensions
        # DEPRECATED
        # @var KalturaCropDimensions
        self.cropDimensions = cropDimensions

        # Clipping start position (in miliseconds)
        # DEPRECATED
        # @var int
        self.clipStart = clipStart

        # Clipping duration (in miliseconds)
        # DEPRECATED
        # @var int
        self.clipDuration = clipDuration

        # XSL to transform ingestion MRSS XML
        # @var string
        self.xslTransformation = xslTransformation

        # ID of default storage profile to be used for linked net-storage file syncs
        # @var int
        self.storageProfileId = storageProfileId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaConversionProfileStatus"), 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'description': getXmlNodeText, 
        'defaultEntryId': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'flavorParamsIds': getXmlNodeText, 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'isPartnerDefault': getXmlNodeBool, 
        'cropDimensions': (KalturaObjectFactory.create, KalturaCropDimensions), 
        'clipStart': getXmlNodeInt, 
        'clipDuration': getXmlNodeInt, 
        'xslTransformation': getXmlNodeText, 
        'storageProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfile")
        kparams.addStringEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("defaultEntryId", self.defaultEntryId)
        kparams.addStringIfDefined("flavorParamsIds", self.flavorParamsIds)
        kparams.addIntEnumIfDefined("isDefault", self.isDefault)
        kparams.addObjectIfDefined("cropDimensions", self.cropDimensions)
        kparams.addIntIfDefined("clipStart", self.clipStart)
        kparams.addIntIfDefined("clipDuration", self.clipDuration)
        kparams.addStringIfDefined("xslTransformation", self.xslTransformation)
        kparams.addIntIfDefined("storageProfileId", self.storageProfileId)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getDefaultEntryId(self):
        return self.defaultEntryId

    def setDefaultEntryId(self, newDefaultEntryId):
        self.defaultEntryId = newDefaultEntryId

    def getCreatedAt(self):
        return self.createdAt

    def getFlavorParamsIds(self):
        return self.flavorParamsIds

    def setFlavorParamsIds(self, newFlavorParamsIds):
        self.flavorParamsIds = newFlavorParamsIds

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getIsPartnerDefault(self):
        return self.isPartnerDefault

    def getCropDimensions(self):
        return self.cropDimensions

    def setCropDimensions(self, newCropDimensions):
        self.cropDimensions = newCropDimensions

    def getClipStart(self):
        return self.clipStart

    def setClipStart(self, newClipStart):
        self.clipStart = newClipStart

    def getClipDuration(self):
        return self.clipDuration

    def setClipDuration(self, newClipDuration):
        self.clipDuration = newClipDuration

    def getXslTransformation(self):
        return self.xslTransformation

    def setXslTransformation(self, newXslTransformation):
        self.xslTransformation = newXslTransformation

    def getStorageProfileId(self):
        return self.storageProfileId

    def setStorageProfileId(self, newStorageProfileId):
        self.storageProfileId = newStorageProfileId


class KalturaConversionProfileListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaConversionProfile
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaConversionProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDataEntry(KalturaBaseEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            dataContent=NotImplemented,
            retrieveDataContentByGet=NotImplemented):
        KalturaBaseEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes)

        # The data of the entry
        # @var string
        self.dataContent = dataContent

        # indicator whether to return the object for get action with the dataContent field.
        # @var bool
        # @insertonly
        self.retrieveDataContentByGet = retrieveDataContentByGet


    PROPERTY_LOADERS = {
        'dataContent': getXmlNodeText, 
        'retrieveDataContentByGet': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaDataEntry")
        kparams.addStringIfDefined("dataContent", self.dataContent)
        kparams.addBoolIfDefined("retrieveDataContentByGet", self.retrieveDataContentByGet)
        return kparams

    def getDataContent(self):
        return self.dataContent

    def setDataContent(self, newDataContent):
        self.dataContent = newDataContent

    def getRetrieveDataContentByGet(self):
        return self.retrieveDataContentByGet

    def setRetrieveDataContentByGet(self, newRetrieveDataContentByGet):
        self.retrieveDataContentByGet = newRetrieveDataContentByGet


class KalturaDataEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented):
        KalturaBaseEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaDataEntryBaseFilter")
        return kparams


class KalturaDataEntryFilter(KalturaDataEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented):
        KalturaDataEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDataEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDataEntryFilter")
        return kparams


class KalturaDataListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDataEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDataEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDataListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaConversionAttribute(KalturaObjectBase):
    def __init__(self,
            flavorParamsId=NotImplemented,
            name=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the flavor params, set to null for source flavor
        # @var int
        self.flavorParamsId = flavorParamsId

        # Attribute name
        # @var string
        self.name = name

        # Attribute value
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionAttribute.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionAttribute")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaEmailIngestionProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            emailAddress=NotImplemented,
            mailboxId=NotImplemented,
            partnerId=NotImplemented,
            conversionProfile2Id=NotImplemented,
            moderationStatus=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            defaultCategory=NotImplemented,
            defaultUserId=NotImplemented,
            defaultTags=NotImplemented,
            defaultAdminTags=NotImplemented,
            maxAttachmentSizeKbytes=NotImplemented,
            maxAttachmentsPerMail=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.name = name

        # @var string
        self.description = description

        # @var string
        self.emailAddress = emailAddress

        # @var string
        self.mailboxId = mailboxId

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        self.conversionProfile2Id = conversionProfile2Id

        # @var KalturaEntryModerationStatus
        self.moderationStatus = moderationStatus

        # @var KalturaEmailIngestionProfileStatus
        # @readonly
        self.status = status

        # @var string
        # @readonly
        self.createdAt = createdAt

        # @var string
        self.defaultCategory = defaultCategory

        # @var string
        self.defaultUserId = defaultUserId

        # @var string
        self.defaultTags = defaultTags

        # @var string
        self.defaultAdminTags = defaultAdminTags

        # @var int
        self.maxAttachmentSizeKbytes = maxAttachmentSizeKbytes

        # @var int
        self.maxAttachmentsPerMail = maxAttachmentsPerMail


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'emailAddress': getXmlNodeText, 
        'mailboxId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'conversionProfile2Id': getXmlNodeInt, 
        'moderationStatus': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaEmailIngestionProfileStatus"), 
        'createdAt': getXmlNodeText, 
        'defaultCategory': getXmlNodeText, 
        'defaultUserId': getXmlNodeText, 
        'defaultTags': getXmlNodeText, 
        'defaultAdminTags': getXmlNodeText, 
        'maxAttachmentSizeKbytes': getXmlNodeInt, 
        'maxAttachmentsPerMail': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEmailIngestionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEmailIngestionProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("emailAddress", self.emailAddress)
        kparams.addStringIfDefined("mailboxId", self.mailboxId)
        kparams.addIntIfDefined("conversionProfile2Id", self.conversionProfile2Id)
        kparams.addIntEnumIfDefined("moderationStatus", self.moderationStatus)
        kparams.addStringIfDefined("defaultCategory", self.defaultCategory)
        kparams.addStringIfDefined("defaultUserId", self.defaultUserId)
        kparams.addStringIfDefined("defaultTags", self.defaultTags)
        kparams.addStringIfDefined("defaultAdminTags", self.defaultAdminTags)
        kparams.addIntIfDefined("maxAttachmentSizeKbytes", self.maxAttachmentSizeKbytes)
        kparams.addIntIfDefined("maxAttachmentsPerMail", self.maxAttachmentsPerMail)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getEmailAddress(self):
        return self.emailAddress

    def setEmailAddress(self, newEmailAddress):
        self.emailAddress = newEmailAddress

    def getMailboxId(self):
        return self.mailboxId

    def setMailboxId(self, newMailboxId):
        self.mailboxId = newMailboxId

    def getPartnerId(self):
        return self.partnerId

    def getConversionProfile2Id(self):
        return self.conversionProfile2Id

    def setConversionProfile2Id(self, newConversionProfile2Id):
        self.conversionProfile2Id = newConversionProfile2Id

    def getModerationStatus(self):
        return self.moderationStatus

    def setModerationStatus(self, newModerationStatus):
        self.moderationStatus = newModerationStatus

    def getStatus(self):
        return self.status

    def getCreatedAt(self):
        return self.createdAt

    def getDefaultCategory(self):
        return self.defaultCategory

    def setDefaultCategory(self, newDefaultCategory):
        self.defaultCategory = newDefaultCategory

    def getDefaultUserId(self):
        return self.defaultUserId

    def setDefaultUserId(self, newDefaultUserId):
        self.defaultUserId = newDefaultUserId

    def getDefaultTags(self):
        return self.defaultTags

    def setDefaultTags(self, newDefaultTags):
        self.defaultTags = newDefaultTags

    def getDefaultAdminTags(self):
        return self.defaultAdminTags

    def setDefaultAdminTags(self, newDefaultAdminTags):
        self.defaultAdminTags = newDefaultAdminTags

    def getMaxAttachmentSizeKbytes(self):
        return self.maxAttachmentSizeKbytes

    def setMaxAttachmentSizeKbytes(self, newMaxAttachmentSizeKbytes):
        self.maxAttachmentSizeKbytes = newMaxAttachmentSizeKbytes

    def getMaxAttachmentsPerMail(self):
        return self.maxAttachmentsPerMail

    def setMaxAttachmentsPerMail(self, newMaxAttachmentsPerMail):
        self.maxAttachmentsPerMail = newMaxAttachmentsPerMail


class KalturaPlayableEntry(KalturaBaseEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            duration=NotImplemented,
            msDuration=NotImplemented,
            durationType=NotImplemented):
        KalturaBaseEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes)

        # Number of plays
        # @var int
        # @readonly
        self.plays = plays

        # Number of views
        # @var int
        # @readonly
        self.views = views

        # The width in pixels
        # @var int
        # @readonly
        self.width = width

        # The height in pixels
        # @var int
        # @readonly
        self.height = height

        # The duration in seconds
        # @var int
        # @readonly
        self.duration = duration

        # The duration in miliseconds
        # @var int
        self.msDuration = msDuration

        # The duration type (short for 0-4 mins, medium for 4-20 mins, long for 20+ mins)
        # @var KalturaDurationType
        # @readonly
        self.durationType = durationType


    PROPERTY_LOADERS = {
        'plays': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'msDuration': getXmlNodeInt, 
        'durationType': (KalturaEnumsFactory.createString, "KalturaDurationType"), 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntry")
        kparams.addIntIfDefined("msDuration", self.msDuration)
        return kparams

    def getPlays(self):
        return self.plays

    def getViews(self):
        return self.views

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDuration(self):
        return self.duration

    def getMsDuration(self):
        return self.msDuration

    def setMsDuration(self, newMsDuration):
        self.msDuration = newMsDuration

    def getDurationType(self):
        return self.durationType


class KalturaMediaEntry(KalturaPlayableEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            duration=NotImplemented,
            msDuration=NotImplemented,
            durationType=NotImplemented,
            mediaType=NotImplemented,
            conversionQuality=NotImplemented,
            sourceType=NotImplemented,
            searchProviderType=NotImplemented,
            searchProviderId=NotImplemented,
            creditUserName=NotImplemented,
            creditUrl=NotImplemented,
            mediaDate=NotImplemented,
            dataUrl=NotImplemented,
            flavorParamsIds=NotImplemented):
        KalturaPlayableEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes,
            plays,
            views,
            width,
            height,
            duration,
            msDuration,
            durationType)

        # The media type of the entry
        # @var KalturaMediaType
        # @insertonly
        self.mediaType = mediaType

        # Override the default conversion quality
        # DEPRECATED - use conversionProfileId instead
        # @var string
        # @insertonly
        self.conversionQuality = conversionQuality

        # The source type of the entry
        # @var KalturaSourceType
        # @insertonly
        self.sourceType = sourceType

        # The search provider type used to import this entry
        # @var KalturaSearchProviderType
        # @insertonly
        self.searchProviderType = searchProviderType

        # The ID of the media in the importing site
        # @var string
        # @insertonly
        self.searchProviderId = searchProviderId

        # The user name used for credits
        # @var string
        self.creditUserName = creditUserName

        # The URL for credits
        # @var string
        self.creditUrl = creditUrl

        # The media date extracted from EXIF data (For images) as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.mediaDate = mediaDate

        # The URL used for playback. This is not the download URL.
        # @var string
        # @readonly
        self.dataUrl = dataUrl

        # Comma separated flavor params ids that exists for this media entry
        # @var string
        # @readonly
        self.flavorParamsIds = flavorParamsIds


    PROPERTY_LOADERS = {
        'mediaType': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'conversionQuality': getXmlNodeText, 
        'sourceType': (KalturaEnumsFactory.createString, "KalturaSourceType"), 
        'searchProviderType': (KalturaEnumsFactory.createInt, "KalturaSearchProviderType"), 
        'searchProviderId': getXmlNodeText, 
        'creditUserName': getXmlNodeText, 
        'creditUrl': getXmlNodeText, 
        'mediaDate': getXmlNodeInt, 
        'dataUrl': getXmlNodeText, 
        'flavorParamsIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntry.toParams(self)
        kparams.put("objectType", "KalturaMediaEntry")
        kparams.addIntEnumIfDefined("mediaType", self.mediaType)
        kparams.addStringIfDefined("conversionQuality", self.conversionQuality)
        kparams.addStringEnumIfDefined("sourceType", self.sourceType)
        kparams.addIntEnumIfDefined("searchProviderType", self.searchProviderType)
        kparams.addStringIfDefined("searchProviderId", self.searchProviderId)
        kparams.addStringIfDefined("creditUserName", self.creditUserName)
        kparams.addStringIfDefined("creditUrl", self.creditUrl)
        return kparams

    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def getConversionQuality(self):
        return self.conversionQuality

    def setConversionQuality(self, newConversionQuality):
        self.conversionQuality = newConversionQuality

    def getSourceType(self):
        return self.sourceType

    def setSourceType(self, newSourceType):
        self.sourceType = newSourceType

    def getSearchProviderType(self):
        return self.searchProviderType

    def setSearchProviderType(self, newSearchProviderType):
        self.searchProviderType = newSearchProviderType

    def getSearchProviderId(self):
        return self.searchProviderId

    def setSearchProviderId(self, newSearchProviderId):
        self.searchProviderId = newSearchProviderId

    def getCreditUserName(self):
        return self.creditUserName

    def setCreditUserName(self, newCreditUserName):
        self.creditUserName = newCreditUserName

    def getCreditUrl(self):
        return self.creditUrl

    def setCreditUrl(self, newCreditUrl):
        self.creditUrl = newCreditUrl

    def getMediaDate(self):
        return self.mediaDate

    def getDataUrl(self):
        return self.dataUrl

    def getFlavorParamsIds(self):
        return self.flavorParamsIds


class KalturaAsset(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The ID of the Flavor Asset
        # @var string
        # @readonly
        self.id = id

        # The entry ID of the Flavor Asset
        # @var string
        # @readonly
        self.entryId = entryId

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The version of the Flavor Asset
        # @var int
        # @readonly
        self.version = version

        # The size (in KBytes) of the Flavor Asset
        # @var int
        # @readonly
        self.size = size

        # Tags used to identify the Flavor Asset in various scenarios
        # @var string
        self.tags = tags

        # The file extension
        # @var string
        # @insertonly
        self.fileExt = fileExt

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        # @readonly
        self.deletedAt = deletedAt

        # System description, error message, warnings and failure cause.
        # @var string
        # @readonly
        self.description = description

        # Partner private data
        # @var string
        self.partnerData = partnerData

        # Partner friendly description
        # @var string
        self.partnerDescription = partnerDescription


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'version': getXmlNodeInt, 
        'size': getXmlNodeInt, 
        'tags': getXmlNodeText, 
        'fileExt': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'deletedAt': getXmlNodeInt, 
        'description': getXmlNodeText, 
        'partnerData': getXmlNodeText, 
        'partnerDescription': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAsset")
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("fileExt", self.fileExt)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addStringIfDefined("partnerDescription", self.partnerDescription)
        return kparams

    def getId(self):
        return self.id

    def getEntryId(self):
        return self.entryId

    def getPartnerId(self):
        return self.partnerId

    def getVersion(self):
        return self.version

    def getSize(self):
        return self.size

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getFileExt(self):
        return self.fileExt

    def setFileExt(self, newFileExt):
        self.fileExt = newFileExt

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getDeletedAt(self):
        return self.deletedAt

    def getDescription(self):
        return self.description

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getPartnerDescription(self):
        return self.partnerDescription

    def setPartnerDescription(self, newPartnerDescription):
        self.partnerDescription = newPartnerDescription


class KalturaFlavorAsset(KalturaAsset):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented,
            flavorParamsId=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            bitrate=NotImplemented,
            frameRate=NotImplemented,
            isOriginal=NotImplemented,
            isWeb=NotImplemented,
            containerFormat=NotImplemented,
            videoCodecId=NotImplemented,
            status=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            entryId,
            partnerId,
            version,
            size,
            tags,
            fileExt,
            createdAt,
            updatedAt,
            deletedAt,
            description,
            partnerData,
            partnerDescription)

        # The Flavor Params used to create this Flavor Asset
        # @var int
        # @insertonly
        self.flavorParamsId = flavorParamsId

        # The width of the Flavor Asset
        # @var int
        # @readonly
        self.width = width

        # The height of the Flavor Asset
        # @var int
        # @readonly
        self.height = height

        # The overall bitrate (in KBits) of the Flavor Asset
        # @var int
        # @readonly
        self.bitrate = bitrate

        # The frame rate (in FPS) of the Flavor Asset
        # @var int
        # @readonly
        self.frameRate = frameRate

        # True if this Flavor Asset is the original source
        # @var bool
        # @readonly
        self.isOriginal = isOriginal

        # True if this Flavor Asset is playable in KDP
        # @var bool
        # @readonly
        self.isWeb = isWeb

        # The container format
        # @var string
        # @readonly
        self.containerFormat = containerFormat

        # The video codec
        # @var string
        # @readonly
        self.videoCodecId = videoCodecId

        # The status of the Flavor Asset
        # @var KalturaFlavorAssetStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'bitrate': getXmlNodeInt, 
        'frameRate': getXmlNodeInt, 
        'isOriginal': getXmlNodeBool, 
        'isWeb': getXmlNodeBool, 
        'containerFormat': getXmlNodeText, 
        'videoCodecId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaFlavorAssetStatus"), 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaFlavorAsset")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getBitrate(self):
        return self.bitrate

    def getFrameRate(self):
        return self.frameRate

    def getIsOriginal(self):
        return self.isOriginal

    def getIsWeb(self):
        return self.isWeb

    def getContainerFormat(self):
        return self.containerFormat

    def getVideoCodecId(self):
        return self.videoCodecId

    def getStatus(self):
        return self.status


class KalturaContentResource(KalturaResource):
    """Is a unified way to add content to Kaltura whether it's an uploaded file, webcam recording, imported URL or existing file sync."""

    def __init__(self):
        KalturaResource.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaContentResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaResource.toParams(self)
        kparams.put("objectType", "KalturaContentResource")
        return kparams


class KalturaAssetBaseFilter(KalturaFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.entryIdEqual = entryIdEqual

        # @var string
        self.entryIdIn = entryIdIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var int
        self.sizeGreaterThanOrEqual = sizeGreaterThanOrEqual

        # @var int
        self.sizeLessThanOrEqual = sizeLessThanOrEqual

        # @var string
        self.tagsLike = tagsLike

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.deletedAtGreaterThanOrEqual = deletedAtGreaterThanOrEqual

        # @var int
        self.deletedAtLessThanOrEqual = deletedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'entryIdEqual': getXmlNodeText, 
        'entryIdIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'sizeGreaterThanOrEqual': getXmlNodeInt, 
        'sizeLessThanOrEqual': getXmlNodeInt, 
        'tagsLike': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'deletedAtGreaterThanOrEqual': getXmlNodeInt, 
        'deletedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetBaseFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfDefined("entryIdIn", self.entryIdIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addIntIfDefined("sizeGreaterThanOrEqual", self.sizeGreaterThanOrEqual)
        kparams.addIntIfDefined("sizeLessThanOrEqual", self.sizeLessThanOrEqual)
        kparams.addStringIfDefined("tagsLike", self.tagsLike)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("deletedAtGreaterThanOrEqual", self.deletedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("deletedAtLessThanOrEqual", self.deletedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getEntryIdIn(self):
        return self.entryIdIn

    def setEntryIdIn(self, newEntryIdIn):
        self.entryIdIn = newEntryIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getSizeGreaterThanOrEqual(self):
        return self.sizeGreaterThanOrEqual

    def setSizeGreaterThanOrEqual(self, newSizeGreaterThanOrEqual):
        self.sizeGreaterThanOrEqual = newSizeGreaterThanOrEqual

    def getSizeLessThanOrEqual(self):
        return self.sizeLessThanOrEqual

    def setSizeLessThanOrEqual(self, newSizeLessThanOrEqual):
        self.sizeLessThanOrEqual = newSizeLessThanOrEqual

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

    def getDeletedAtGreaterThanOrEqual(self):
        return self.deletedAtGreaterThanOrEqual

    def setDeletedAtGreaterThanOrEqual(self, newDeletedAtGreaterThanOrEqual):
        self.deletedAtGreaterThanOrEqual = newDeletedAtGreaterThanOrEqual

    def getDeletedAtLessThanOrEqual(self):
        return self.deletedAtLessThanOrEqual

    def setDeletedAtLessThanOrEqual(self, newDeletedAtLessThanOrEqual):
        self.deletedAtLessThanOrEqual = newDeletedAtLessThanOrEqual


class KalturaAssetFilter(KalturaAssetBaseFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented):
        KalturaAssetBaseFilter.__init__(self,
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
            deletedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetFilter")
        return kparams


class KalturaFlavorAssetListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaFlavorAsset
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFlavorAsset), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaString(KalturaObjectBase):
    """A string representation to return an array of strings"""

    def __init__(self,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaString.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaString")
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaAssetParams(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the Flavor Params
        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # The name of the Flavor Params
        # @var string
        self.name = name

        # System name of the Flavor Params
        # @var string
        self.systemName = systemName

        # The description of the Flavor Params
        # @var string
        self.description = description

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # True if those Flavor Params are part of system defaults
        # @var KalturaNullableBoolean
        # @readonly
        self.isSystemDefault = isSystemDefault

        # The Flavor Params tags are used to identify the flavor for different usage (e.g. web, hd, mobile)
        # @var string
        self.tags = tags

        # Array of partner permisison names that required for using this asset params
        # @var array of KalturaString
        self.requiredPermissions = requiredPermissions


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'isSystemDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'tags': getXmlNodeText, 
        'requiredPermissions': (KalturaObjectFactory.createArray, KalturaString), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetParams")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addArrayIfDefined("requiredPermissions", self.requiredPermissions)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getIsSystemDefault(self):
        return self.isSystemDefault

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getRequiredPermissions(self):
        return self.requiredPermissions

    def setRequiredPermissions(self, newRequiredPermissions):
        self.requiredPermissions = newRequiredPermissions


class KalturaFlavorParams(KalturaAssetParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented):
        KalturaAssetParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions)

        # The video codec of the Flavor Params
        # @var KalturaVideoCodec
        self.videoCodec = videoCodec

        # The video bitrate (in KBits) of the Flavor Params
        # @var int
        self.videoBitrate = videoBitrate

        # The audio codec of the Flavor Params
        # @var KalturaAudioCodec
        self.audioCodec = audioCodec

        # The audio bitrate (in KBits) of the Flavor Params
        # @var int
        self.audioBitrate = audioBitrate

        # The number of audio channels for "downmixing"
        # @var int
        self.audioChannels = audioChannels

        # The audio sample rate of the Flavor Params
        # @var int
        self.audioSampleRate = audioSampleRate

        # The desired width of the Flavor Params
        # @var int
        self.width = width

        # The desired height of the Flavor Params
        # @var int
        self.height = height

        # The frame rate of the Flavor Params
        # @var int
        self.frameRate = frameRate

        # The gop size of the Flavor Params
        # @var int
        self.gopSize = gopSize

        # The list of conversion engines (comma separated)
        # @var string
        self.conversionEngines = conversionEngines

        # The list of conversion engines extra params (separated with "|")
        # @var string
        self.conversionEnginesExtraParams = conversionEnginesExtraParams

        # @var bool
        self.twoPass = twoPass

        # @var int
        self.deinterlice = deinterlice

        # @var int
        self.rotate = rotate

        # @var string
        self.operators = operators

        # @var int
        self.engineVersion = engineVersion

        # The container format of the Flavor Params
        # @var KalturaContainerFormat
        self.format = format

        # @var int
        self.aspectRatioProcessingMode = aspectRatioProcessingMode

        # @var int
        self.forceFrameToMultiplication16 = forceFrameToMultiplication16

        # @var int
        self.videoConstantBitrate = videoConstantBitrate

        # @var int
        self.videoBitrateTolerance = videoBitrateTolerance


    PROPERTY_LOADERS = {
        'videoCodec': (KalturaEnumsFactory.createString, "KalturaVideoCodec"), 
        'videoBitrate': getXmlNodeInt, 
        'audioCodec': (KalturaEnumsFactory.createString, "KalturaAudioCodec"), 
        'audioBitrate': getXmlNodeInt, 
        'audioChannels': getXmlNodeInt, 
        'audioSampleRate': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'frameRate': getXmlNodeInt, 
        'gopSize': getXmlNodeInt, 
        'conversionEngines': getXmlNodeText, 
        'conversionEnginesExtraParams': getXmlNodeText, 
        'twoPass': getXmlNodeBool, 
        'deinterlice': getXmlNodeInt, 
        'rotate': getXmlNodeInt, 
        'operators': getXmlNodeText, 
        'engineVersion': getXmlNodeInt, 
        'format': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
        'aspectRatioProcessingMode': getXmlNodeInt, 
        'forceFrameToMultiplication16': getXmlNodeInt, 
        'videoConstantBitrate': getXmlNodeInt, 
        'videoBitrateTolerance': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaFlavorParams")
        kparams.addStringEnumIfDefined("videoCodec", self.videoCodec)
        kparams.addIntIfDefined("videoBitrate", self.videoBitrate)
        kparams.addStringEnumIfDefined("audioCodec", self.audioCodec)
        kparams.addIntIfDefined("audioBitrate", self.audioBitrate)
        kparams.addIntIfDefined("audioChannels", self.audioChannels)
        kparams.addIntIfDefined("audioSampleRate", self.audioSampleRate)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        kparams.addIntIfDefined("frameRate", self.frameRate)
        kparams.addIntIfDefined("gopSize", self.gopSize)
        kparams.addStringIfDefined("conversionEngines", self.conversionEngines)
        kparams.addStringIfDefined("conversionEnginesExtraParams", self.conversionEnginesExtraParams)
        kparams.addBoolIfDefined("twoPass", self.twoPass)
        kparams.addIntIfDefined("deinterlice", self.deinterlice)
        kparams.addIntIfDefined("rotate", self.rotate)
        kparams.addStringIfDefined("operators", self.operators)
        kparams.addIntIfDefined("engineVersion", self.engineVersion)
        kparams.addStringEnumIfDefined("format", self.format)
        kparams.addIntIfDefined("aspectRatioProcessingMode", self.aspectRatioProcessingMode)
        kparams.addIntIfDefined("forceFrameToMultiplication16", self.forceFrameToMultiplication16)
        kparams.addIntIfDefined("videoConstantBitrate", self.videoConstantBitrate)
        kparams.addIntIfDefined("videoBitrateTolerance", self.videoBitrateTolerance)
        return kparams

    def getVideoCodec(self):
        return self.videoCodec

    def setVideoCodec(self, newVideoCodec):
        self.videoCodec = newVideoCodec

    def getVideoBitrate(self):
        return self.videoBitrate

    def setVideoBitrate(self, newVideoBitrate):
        self.videoBitrate = newVideoBitrate

    def getAudioCodec(self):
        return self.audioCodec

    def setAudioCodec(self, newAudioCodec):
        self.audioCodec = newAudioCodec

    def getAudioBitrate(self):
        return self.audioBitrate

    def setAudioBitrate(self, newAudioBitrate):
        self.audioBitrate = newAudioBitrate

    def getAudioChannels(self):
        return self.audioChannels

    def setAudioChannels(self, newAudioChannels):
        self.audioChannels = newAudioChannels

    def getAudioSampleRate(self):
        return self.audioSampleRate

    def setAudioSampleRate(self, newAudioSampleRate):
        self.audioSampleRate = newAudioSampleRate

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getFrameRate(self):
        return self.frameRate

    def setFrameRate(self, newFrameRate):
        self.frameRate = newFrameRate

    def getGopSize(self):
        return self.gopSize

    def setGopSize(self, newGopSize):
        self.gopSize = newGopSize

    def getConversionEngines(self):
        return self.conversionEngines

    def setConversionEngines(self, newConversionEngines):
        self.conversionEngines = newConversionEngines

    def getConversionEnginesExtraParams(self):
        return self.conversionEnginesExtraParams

    def setConversionEnginesExtraParams(self, newConversionEnginesExtraParams):
        self.conversionEnginesExtraParams = newConversionEnginesExtraParams

    def getTwoPass(self):
        return self.twoPass

    def setTwoPass(self, newTwoPass):
        self.twoPass = newTwoPass

    def getDeinterlice(self):
        return self.deinterlice

    def setDeinterlice(self, newDeinterlice):
        self.deinterlice = newDeinterlice

    def getRotate(self):
        return self.rotate

    def setRotate(self, newRotate):
        self.rotate = newRotate

    def getOperators(self):
        return self.operators

    def setOperators(self, newOperators):
        self.operators = newOperators

    def getEngineVersion(self):
        return self.engineVersion

    def setEngineVersion(self, newEngineVersion):
        self.engineVersion = newEngineVersion

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getAspectRatioProcessingMode(self):
        return self.aspectRatioProcessingMode

    def setAspectRatioProcessingMode(self, newAspectRatioProcessingMode):
        self.aspectRatioProcessingMode = newAspectRatioProcessingMode

    def getForceFrameToMultiplication16(self):
        return self.forceFrameToMultiplication16

    def setForceFrameToMultiplication16(self, newForceFrameToMultiplication16):
        self.forceFrameToMultiplication16 = newForceFrameToMultiplication16

    def getVideoConstantBitrate(self):
        return self.videoConstantBitrate

    def setVideoConstantBitrate(self, newVideoConstantBitrate):
        self.videoConstantBitrate = newVideoConstantBitrate

    def getVideoBitrateTolerance(self):
        return self.videoBitrateTolerance

    def setVideoBitrateTolerance(self, newVideoBitrateTolerance):
        self.videoBitrateTolerance = newVideoBitrateTolerance


class KalturaFlavorAssetWithParams(KalturaObjectBase):
    def __init__(self,
            flavorAsset=NotImplemented,
            flavorParams=NotImplemented,
            entryId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The Flavor Asset (Can be null when there are params without asset)
        # @var KalturaFlavorAsset
        self.flavorAsset = flavorAsset

        # The Flavor Params
        # @var KalturaFlavorParams
        self.flavorParams = flavorParams

        # The entry id
        # @var string
        self.entryId = entryId


    PROPERTY_LOADERS = {
        'flavorAsset': (KalturaObjectFactory.create, KalturaFlavorAsset), 
        'flavorParams': (KalturaObjectFactory.create, KalturaFlavorParams), 
        'entryId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetWithParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetWithParams")
        kparams.addObjectIfDefined("flavorAsset", self.flavorAsset)
        kparams.addObjectIfDefined("flavorParams", self.flavorParams)
        kparams.addStringIfDefined("entryId", self.entryId)
        return kparams

    def getFlavorAsset(self):
        return self.flavorAsset

    def setFlavorAsset(self, newFlavorAsset):
        self.flavorAsset = newFlavorAsset

    def getFlavorParams(self):
        return self.flavorParams

    def setFlavorParams(self, newFlavorParams):
        self.flavorParams = newFlavorParams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId


class KalturaFlavorParamsBaseFilter(KalturaAssetParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaAssetParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual)

        # @var KalturaContainerFormat
        self.formatEqual = formatEqual


    PROPERTY_LOADERS = {
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsBaseFilter")
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        return kparams

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual


class KalturaFlavorParamsFilter(KalturaFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsFilter")
        return kparams


class KalturaFlavorParamsListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaFlavorParams
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFlavorParams), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaLiveStreamBitrate(KalturaObjectBase):
    def __init__(self,
            bitrate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.bitrate = bitrate

        # @var int
        self.width = width

        # @var int
        self.height = height


    PROPERTY_LOADERS = {
        'bitrate': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamBitrate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamBitrate")
        kparams.addIntIfDefined("bitrate", self.bitrate)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        return kparams

    def getBitrate(self):
        return self.bitrate

    def setBitrate(self, newBitrate):
        self.bitrate = newBitrate

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight


class KalturaLiveStreamEntry(KalturaMediaEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            duration=NotImplemented,
            msDuration=NotImplemented,
            durationType=NotImplemented,
            mediaType=NotImplemented,
            conversionQuality=NotImplemented,
            sourceType=NotImplemented,
            searchProviderType=NotImplemented,
            searchProviderId=NotImplemented,
            creditUserName=NotImplemented,
            creditUrl=NotImplemented,
            mediaDate=NotImplemented,
            dataUrl=NotImplemented,
            flavorParamsIds=NotImplemented,
            offlineMessage=NotImplemented,
            streamRemoteId=NotImplemented,
            streamRemoteBackupId=NotImplemented,
            bitrates=NotImplemented,
            primaryBroadcastingUrl=NotImplemented,
            secondaryBroadcastingUrl=NotImplemented,
            streamName=NotImplemented,
            streamUrl=NotImplemented):
        KalturaMediaEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes,
            plays,
            views,
            width,
            height,
            duration,
            msDuration,
            durationType,
            mediaType,
            conversionQuality,
            sourceType,
            searchProviderType,
            searchProviderId,
            creditUserName,
            creditUrl,
            mediaDate,
            dataUrl,
            flavorParamsIds)

        # The message to be presented when the stream is offline
        # @var string
        self.offlineMessage = offlineMessage

        # The stream id as provided by the provider
        # @var string
        # @readonly
        self.streamRemoteId = streamRemoteId

        # The backup stream id as provided by the provider
        # @var string
        # @readonly
        self.streamRemoteBackupId = streamRemoteBackupId

        # Array of supported bitrates
        # @var array of KalturaLiveStreamBitrate
        self.bitrates = bitrates

        # @var string
        self.primaryBroadcastingUrl = primaryBroadcastingUrl

        # @var string
        self.secondaryBroadcastingUrl = secondaryBroadcastingUrl

        # @var string
        self.streamName = streamName

        # The stream url
        # @var string
        self.streamUrl = streamUrl


    PROPERTY_LOADERS = {
        'offlineMessage': getXmlNodeText, 
        'streamRemoteId': getXmlNodeText, 
        'streamRemoteBackupId': getXmlNodeText, 
        'bitrates': (KalturaObjectFactory.createArray, KalturaLiveStreamBitrate), 
        'primaryBroadcastingUrl': getXmlNodeText, 
        'secondaryBroadcastingUrl': getXmlNodeText, 
        'streamName': getXmlNodeText, 
        'streamUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaMediaEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntry.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntry")
        kparams.addStringIfDefined("offlineMessage", self.offlineMessage)
        kparams.addArrayIfDefined("bitrates", self.bitrates)
        kparams.addStringIfDefined("primaryBroadcastingUrl", self.primaryBroadcastingUrl)
        kparams.addStringIfDefined("secondaryBroadcastingUrl", self.secondaryBroadcastingUrl)
        kparams.addStringIfDefined("streamName", self.streamName)
        kparams.addStringIfDefined("streamUrl", self.streamUrl)
        return kparams

    def getOfflineMessage(self):
        return self.offlineMessage

    def setOfflineMessage(self, newOfflineMessage):
        self.offlineMessage = newOfflineMessage

    def getStreamRemoteId(self):
        return self.streamRemoteId

    def getStreamRemoteBackupId(self):
        return self.streamRemoteBackupId

    def getBitrates(self):
        return self.bitrates

    def setBitrates(self, newBitrates):
        self.bitrates = newBitrates

    def getPrimaryBroadcastingUrl(self):
        return self.primaryBroadcastingUrl

    def setPrimaryBroadcastingUrl(self, newPrimaryBroadcastingUrl):
        self.primaryBroadcastingUrl = newPrimaryBroadcastingUrl

    def getSecondaryBroadcastingUrl(self):
        return self.secondaryBroadcastingUrl

    def setSecondaryBroadcastingUrl(self, newSecondaryBroadcastingUrl):
        self.secondaryBroadcastingUrl = newSecondaryBroadcastingUrl

    def getStreamName(self):
        return self.streamName

    def setStreamName(self, newStreamName):
        self.streamName = newStreamName

    def getStreamUrl(self):
        return self.streamUrl

    def setStreamUrl(self, newStreamUrl):
        self.streamUrl = newStreamUrl


class KalturaLiveStreamAdminEntry(KalturaLiveStreamEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            duration=NotImplemented,
            msDuration=NotImplemented,
            durationType=NotImplemented,
            mediaType=NotImplemented,
            conversionQuality=NotImplemented,
            sourceType=NotImplemented,
            searchProviderType=NotImplemented,
            searchProviderId=NotImplemented,
            creditUserName=NotImplemented,
            creditUrl=NotImplemented,
            mediaDate=NotImplemented,
            dataUrl=NotImplemented,
            flavorParamsIds=NotImplemented,
            offlineMessage=NotImplemented,
            streamRemoteId=NotImplemented,
            streamRemoteBackupId=NotImplemented,
            bitrates=NotImplemented,
            primaryBroadcastingUrl=NotImplemented,
            secondaryBroadcastingUrl=NotImplemented,
            streamName=NotImplemented,
            streamUrl=NotImplemented,
            encodingIP1=NotImplemented,
            encodingIP2=NotImplemented,
            streamPassword=NotImplemented,
            streamUsername=NotImplemented):
        KalturaLiveStreamEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes,
            plays,
            views,
            width,
            height,
            duration,
            msDuration,
            durationType,
            mediaType,
            conversionQuality,
            sourceType,
            searchProviderType,
            searchProviderId,
            creditUserName,
            creditUrl,
            mediaDate,
            dataUrl,
            flavorParamsIds,
            offlineMessage,
            streamRemoteId,
            streamRemoteBackupId,
            bitrates,
            primaryBroadcastingUrl,
            secondaryBroadcastingUrl,
            streamName,
            streamUrl)

        # The broadcast primary ip
        # @var string
        self.encodingIP1 = encodingIP1

        # The broadcast secondary ip
        # @var string
        self.encodingIP2 = encodingIP2

        # The broadcast password
        # @var string
        self.streamPassword = streamPassword

        # The broadcast username
        # @var string
        # @readonly
        self.streamUsername = streamUsername


    PROPERTY_LOADERS = {
        'encodingIP1': getXmlNodeText, 
        'encodingIP2': getXmlNodeText, 
        'streamPassword': getXmlNodeText, 
        'streamUsername': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaLiveStreamEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntry.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntry")
        kparams.addStringIfDefined("encodingIP1", self.encodingIP1)
        kparams.addStringIfDefined("encodingIP2", self.encodingIP2)
        kparams.addStringIfDefined("streamPassword", self.streamPassword)
        return kparams

    def getEncodingIP1(self):
        return self.encodingIP1

    def setEncodingIP1(self, newEncodingIP1):
        self.encodingIP1 = newEncodingIP1

    def getEncodingIP2(self):
        return self.encodingIP2

    def setEncodingIP2(self, newEncodingIP2):
        self.encodingIP2 = newEncodingIP2

    def getStreamPassword(self):
        return self.streamPassword

    def setStreamPassword(self, newStreamPassword):
        self.streamPassword = newStreamPassword

    def getStreamUsername(self):
        return self.streamUsername


class KalturaPlayableEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented):
        KalturaBaseEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)

        # @var int
        self.durationLessThan = durationLessThan

        # @var int
        self.durationGreaterThan = durationGreaterThan

        # @var int
        self.durationLessThanOrEqual = durationLessThanOrEqual

        # @var int
        self.durationGreaterThanOrEqual = durationGreaterThanOrEqual

        # @var int
        self.msDurationLessThan = msDurationLessThan

        # @var int
        self.msDurationGreaterThan = msDurationGreaterThan

        # @var int
        self.msDurationLessThanOrEqual = msDurationLessThanOrEqual

        # @var int
        self.msDurationGreaterThanOrEqual = msDurationGreaterThanOrEqual

        # @var string
        self.durationTypeMatchOr = durationTypeMatchOr


    PROPERTY_LOADERS = {
        'durationLessThan': getXmlNodeInt, 
        'durationGreaterThan': getXmlNodeInt, 
        'durationLessThanOrEqual': getXmlNodeInt, 
        'durationGreaterThanOrEqual': getXmlNodeInt, 
        'msDurationLessThan': getXmlNodeInt, 
        'msDurationGreaterThan': getXmlNodeInt, 
        'msDurationLessThanOrEqual': getXmlNodeInt, 
        'msDurationGreaterThanOrEqual': getXmlNodeInt, 
        'durationTypeMatchOr': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntryBaseFilter")
        kparams.addIntIfDefined("durationLessThan", self.durationLessThan)
        kparams.addIntIfDefined("durationGreaterThan", self.durationGreaterThan)
        kparams.addIntIfDefined("durationLessThanOrEqual", self.durationLessThanOrEqual)
        kparams.addIntIfDefined("durationGreaterThanOrEqual", self.durationGreaterThanOrEqual)
        kparams.addIntIfDefined("msDurationLessThan", self.msDurationLessThan)
        kparams.addIntIfDefined("msDurationGreaterThan", self.msDurationGreaterThan)
        kparams.addIntIfDefined("msDurationLessThanOrEqual", self.msDurationLessThanOrEqual)
        kparams.addIntIfDefined("msDurationGreaterThanOrEqual", self.msDurationGreaterThanOrEqual)
        kparams.addStringIfDefined("durationTypeMatchOr", self.durationTypeMatchOr)
        return kparams

    def getDurationLessThan(self):
        return self.durationLessThan

    def setDurationLessThan(self, newDurationLessThan):
        self.durationLessThan = newDurationLessThan

    def getDurationGreaterThan(self):
        return self.durationGreaterThan

    def setDurationGreaterThan(self, newDurationGreaterThan):
        self.durationGreaterThan = newDurationGreaterThan

    def getDurationLessThanOrEqual(self):
        return self.durationLessThanOrEqual

    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual):
        self.durationLessThanOrEqual = newDurationLessThanOrEqual

    def getDurationGreaterThanOrEqual(self):
        return self.durationGreaterThanOrEqual

    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual):
        self.durationGreaterThanOrEqual = newDurationGreaterThanOrEqual

    def getMsDurationLessThan(self):
        return self.msDurationLessThan

    def setMsDurationLessThan(self, newMsDurationLessThan):
        self.msDurationLessThan = newMsDurationLessThan

    def getMsDurationGreaterThan(self):
        return self.msDurationGreaterThan

    def setMsDurationGreaterThan(self, newMsDurationGreaterThan):
        self.msDurationGreaterThan = newMsDurationGreaterThan

    def getMsDurationLessThanOrEqual(self):
        return self.msDurationLessThanOrEqual

    def setMsDurationLessThanOrEqual(self, newMsDurationLessThanOrEqual):
        self.msDurationLessThanOrEqual = newMsDurationLessThanOrEqual

    def getMsDurationGreaterThanOrEqual(self):
        return self.msDurationGreaterThanOrEqual

    def setMsDurationGreaterThanOrEqual(self, newMsDurationGreaterThanOrEqual):
        self.msDurationGreaterThanOrEqual = newMsDurationGreaterThanOrEqual

    def getDurationTypeMatchOr(self):
        return self.durationTypeMatchOr

    def setDurationTypeMatchOr(self, newDurationTypeMatchOr):
        self.durationTypeMatchOr = newDurationTypeMatchOr


class KalturaPlayableEntryFilter(KalturaPlayableEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented):
        KalturaPlayableEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlayableEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntryFilter")
        return kparams


class KalturaMediaEntryBaseFilter(KalturaPlayableEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaPlayableEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr)

        # @var KalturaMediaType
        self.mediaTypeEqual = mediaTypeEqual

        # @var string
        self.mediaTypeIn = mediaTypeIn

        # @var int
        self.mediaDateGreaterThanOrEqual = mediaDateGreaterThanOrEqual

        # @var int
        self.mediaDateLessThanOrEqual = mediaDateLessThanOrEqual

        # @var string
        self.flavorParamsIdsMatchOr = flavorParamsIdsMatchOr

        # @var string
        self.flavorParamsIdsMatchAnd = flavorParamsIdsMatchAnd


    PROPERTY_LOADERS = {
        'mediaTypeEqual': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'mediaTypeIn': getXmlNodeText, 
        'mediaDateGreaterThanOrEqual': getXmlNodeInt, 
        'mediaDateLessThanOrEqual': getXmlNodeInt, 
        'flavorParamsIdsMatchOr': getXmlNodeText, 
        'flavorParamsIdsMatchAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryBaseFilter")
        kparams.addIntEnumIfDefined("mediaTypeEqual", self.mediaTypeEqual)
        kparams.addStringIfDefined("mediaTypeIn", self.mediaTypeIn)
        kparams.addIntIfDefined("mediaDateGreaterThanOrEqual", self.mediaDateGreaterThanOrEqual)
        kparams.addIntIfDefined("mediaDateLessThanOrEqual", self.mediaDateLessThanOrEqual)
        kparams.addStringIfDefined("flavorParamsIdsMatchOr", self.flavorParamsIdsMatchOr)
        kparams.addStringIfDefined("flavorParamsIdsMatchAnd", self.flavorParamsIdsMatchAnd)
        return kparams

    def getMediaTypeEqual(self):
        return self.mediaTypeEqual

    def setMediaTypeEqual(self, newMediaTypeEqual):
        self.mediaTypeEqual = newMediaTypeEqual

    def getMediaTypeIn(self):
        return self.mediaTypeIn

    def setMediaTypeIn(self, newMediaTypeIn):
        self.mediaTypeIn = newMediaTypeIn

    def getMediaDateGreaterThanOrEqual(self):
        return self.mediaDateGreaterThanOrEqual

    def setMediaDateGreaterThanOrEqual(self, newMediaDateGreaterThanOrEqual):
        self.mediaDateGreaterThanOrEqual = newMediaDateGreaterThanOrEqual

    def getMediaDateLessThanOrEqual(self):
        return self.mediaDateLessThanOrEqual

    def setMediaDateLessThanOrEqual(self, newMediaDateLessThanOrEqual):
        self.mediaDateLessThanOrEqual = newMediaDateLessThanOrEqual

    def getFlavorParamsIdsMatchOr(self):
        return self.flavorParamsIdsMatchOr

    def setFlavorParamsIdsMatchOr(self, newFlavorParamsIdsMatchOr):
        self.flavorParamsIdsMatchOr = newFlavorParamsIdsMatchOr

    def getFlavorParamsIdsMatchAnd(self):
        return self.flavorParamsIdsMatchAnd

    def setFlavorParamsIdsMatchAnd(self, newFlavorParamsIdsMatchAnd):
        self.flavorParamsIdsMatchAnd = newFlavorParamsIdsMatchAnd


class KalturaMediaEntryFilter(KalturaMediaEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaMediaEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryFilter")
        return kparams


class KalturaLiveStreamEntryBaseFilter(KalturaMediaEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaMediaEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntryBaseFilter")
        return kparams


class KalturaLiveStreamEntryFilter(KalturaLiveStreamEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaLiveStreamEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntryFilter")
        return kparams


class KalturaLiveStreamListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaLiveStreamEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaLiveStreamEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMediaInfoBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            flavorAssetIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.flavorAssetIdEqual = flavorAssetIdEqual


    PROPERTY_LOADERS = {
        'flavorAssetIdEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfoBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaInfoBaseFilter")
        kparams.addStringIfDefined("flavorAssetIdEqual", self.flavorAssetIdEqual)
        return kparams

    def getFlavorAssetIdEqual(self):
        return self.flavorAssetIdEqual

    def setFlavorAssetIdEqual(self, newFlavorAssetIdEqual):
        self.flavorAssetIdEqual = newFlavorAssetIdEqual


class KalturaMediaInfoFilter(KalturaMediaInfoBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            flavorAssetIdEqual=NotImplemented):
        KalturaMediaInfoBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            flavorAssetIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaInfoBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfoFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaInfoBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaInfoFilter")
        return kparams


class KalturaMediaInfo(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            flavorAssetId=NotImplemented,
            fileSize=NotImplemented,
            containerFormat=NotImplemented,
            containerId=NotImplemented,
            containerProfile=NotImplemented,
            containerDuration=NotImplemented,
            containerBitRate=NotImplemented,
            videoFormat=NotImplemented,
            videoCodecId=NotImplemented,
            videoDuration=NotImplemented,
            videoBitRate=NotImplemented,
            videoBitRateMode=NotImplemented,
            videoWidth=NotImplemented,
            videoHeight=NotImplemented,
            videoFrameRate=NotImplemented,
            videoDar=NotImplemented,
            videoRotation=NotImplemented,
            audioFormat=NotImplemented,
            audioCodecId=NotImplemented,
            audioDuration=NotImplemented,
            audioBitRate=NotImplemented,
            audioBitRateMode=NotImplemented,
            audioChannels=NotImplemented,
            audioSamplingRate=NotImplemented,
            audioResolution=NotImplemented,
            writingLib=NotImplemented,
            rawData=NotImplemented,
            multiStreamInfo=NotImplemented,
            scanType=NotImplemented,
            multiStream=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the media info
        # @var int
        # @readonly
        self.id = id

        # The id of the related flavor asset
        # @var string
        self.flavorAssetId = flavorAssetId

        # The file size
        # @var int
        self.fileSize = fileSize

        # The container format
        # @var string
        self.containerFormat = containerFormat

        # The container id
        # @var string
        self.containerId = containerId

        # The container profile
        # @var string
        self.containerProfile = containerProfile

        # The container duration
        # @var int
        self.containerDuration = containerDuration

        # The container bit rate
        # @var int
        self.containerBitRate = containerBitRate

        # The video format
        # @var string
        self.videoFormat = videoFormat

        # The video codec id
        # @var string
        self.videoCodecId = videoCodecId

        # The video duration
        # @var int
        self.videoDuration = videoDuration

        # The video bit rate
        # @var int
        self.videoBitRate = videoBitRate

        # The video bit rate mode
        # @var KalturaBitRateMode
        self.videoBitRateMode = videoBitRateMode

        # The video width
        # @var int
        self.videoWidth = videoWidth

        # The video height
        # @var int
        self.videoHeight = videoHeight

        # The video frame rate
        # @var float
        self.videoFrameRate = videoFrameRate

        # The video display aspect ratio (dar)
        # @var float
        self.videoDar = videoDar

        # @var int
        self.videoRotation = videoRotation

        # The audio format
        # @var string
        self.audioFormat = audioFormat

        # The audio codec id
        # @var string
        self.audioCodecId = audioCodecId

        # The audio duration
        # @var int
        self.audioDuration = audioDuration

        # The audio bit rate
        # @var int
        self.audioBitRate = audioBitRate

        # The audio bit rate mode
        # @var KalturaBitRateMode
        self.audioBitRateMode = audioBitRateMode

        # The number of audio channels
        # @var int
        self.audioChannels = audioChannels

        # The audio sampling rate
        # @var int
        self.audioSamplingRate = audioSamplingRate

        # The audio resolution
        # @var int
        self.audioResolution = audioResolution

        # The writing library
        # @var string
        self.writingLib = writingLib

        # The data as returned by the mediainfo command line
        # @var string
        self.rawData = rawData

        # @var string
        self.multiStreamInfo = multiStreamInfo

        # @var int
        self.scanType = scanType

        # @var string
        self.multiStream = multiStream


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'flavorAssetId': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'containerFormat': getXmlNodeText, 
        'containerId': getXmlNodeText, 
        'containerProfile': getXmlNodeText, 
        'containerDuration': getXmlNodeInt, 
        'containerBitRate': getXmlNodeInt, 
        'videoFormat': getXmlNodeText, 
        'videoCodecId': getXmlNodeText, 
        'videoDuration': getXmlNodeInt, 
        'videoBitRate': getXmlNodeInt, 
        'videoBitRateMode': (KalturaEnumsFactory.createInt, "KalturaBitRateMode"), 
        'videoWidth': getXmlNodeInt, 
        'videoHeight': getXmlNodeInt, 
        'videoFrameRate': getXmlNodeFloat, 
        'videoDar': getXmlNodeFloat, 
        'videoRotation': getXmlNodeInt, 
        'audioFormat': getXmlNodeText, 
        'audioCodecId': getXmlNodeText, 
        'audioDuration': getXmlNodeInt, 
        'audioBitRate': getXmlNodeInt, 
        'audioBitRateMode': (KalturaEnumsFactory.createInt, "KalturaBitRateMode"), 
        'audioChannels': getXmlNodeInt, 
        'audioSamplingRate': getXmlNodeInt, 
        'audioResolution': getXmlNodeInt, 
        'writingLib': getXmlNodeText, 
        'rawData': getXmlNodeText, 
        'multiStreamInfo': getXmlNodeText, 
        'scanType': getXmlNodeInt, 
        'multiStream': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaInfo")
        kparams.addStringIfDefined("flavorAssetId", self.flavorAssetId)
        kparams.addIntIfDefined("fileSize", self.fileSize)
        kparams.addStringIfDefined("containerFormat", self.containerFormat)
        kparams.addStringIfDefined("containerId", self.containerId)
        kparams.addStringIfDefined("containerProfile", self.containerProfile)
        kparams.addIntIfDefined("containerDuration", self.containerDuration)
        kparams.addIntIfDefined("containerBitRate", self.containerBitRate)
        kparams.addStringIfDefined("videoFormat", self.videoFormat)
        kparams.addStringIfDefined("videoCodecId", self.videoCodecId)
        kparams.addIntIfDefined("videoDuration", self.videoDuration)
        kparams.addIntIfDefined("videoBitRate", self.videoBitRate)
        kparams.addIntEnumIfDefined("videoBitRateMode", self.videoBitRateMode)
        kparams.addIntIfDefined("videoWidth", self.videoWidth)
        kparams.addIntIfDefined("videoHeight", self.videoHeight)
        kparams.addFloatIfDefined("videoFrameRate", self.videoFrameRate)
        kparams.addFloatIfDefined("videoDar", self.videoDar)
        kparams.addIntIfDefined("videoRotation", self.videoRotation)
        kparams.addStringIfDefined("audioFormat", self.audioFormat)
        kparams.addStringIfDefined("audioCodecId", self.audioCodecId)
        kparams.addIntIfDefined("audioDuration", self.audioDuration)
        kparams.addIntIfDefined("audioBitRate", self.audioBitRate)
        kparams.addIntEnumIfDefined("audioBitRateMode", self.audioBitRateMode)
        kparams.addIntIfDefined("audioChannels", self.audioChannels)
        kparams.addIntIfDefined("audioSamplingRate", self.audioSamplingRate)
        kparams.addIntIfDefined("audioResolution", self.audioResolution)
        kparams.addStringIfDefined("writingLib", self.writingLib)
        kparams.addStringIfDefined("rawData", self.rawData)
        kparams.addStringIfDefined("multiStreamInfo", self.multiStreamInfo)
        kparams.addIntIfDefined("scanType", self.scanType)
        kparams.addStringIfDefined("multiStream", self.multiStream)
        return kparams

    def getId(self):
        return self.id

    def getFlavorAssetId(self):
        return self.flavorAssetId

    def setFlavorAssetId(self, newFlavorAssetId):
        self.flavorAssetId = newFlavorAssetId

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getContainerFormat(self):
        return self.containerFormat

    def setContainerFormat(self, newContainerFormat):
        self.containerFormat = newContainerFormat

    def getContainerId(self):
        return self.containerId

    def setContainerId(self, newContainerId):
        self.containerId = newContainerId

    def getContainerProfile(self):
        return self.containerProfile

    def setContainerProfile(self, newContainerProfile):
        self.containerProfile = newContainerProfile

    def getContainerDuration(self):
        return self.containerDuration

    def setContainerDuration(self, newContainerDuration):
        self.containerDuration = newContainerDuration

    def getContainerBitRate(self):
        return self.containerBitRate

    def setContainerBitRate(self, newContainerBitRate):
        self.containerBitRate = newContainerBitRate

    def getVideoFormat(self):
        return self.videoFormat

    def setVideoFormat(self, newVideoFormat):
        self.videoFormat = newVideoFormat

    def getVideoCodecId(self):
        return self.videoCodecId

    def setVideoCodecId(self, newVideoCodecId):
        self.videoCodecId = newVideoCodecId

    def getVideoDuration(self):
        return self.videoDuration

    def setVideoDuration(self, newVideoDuration):
        self.videoDuration = newVideoDuration

    def getVideoBitRate(self):
        return self.videoBitRate

    def setVideoBitRate(self, newVideoBitRate):
        self.videoBitRate = newVideoBitRate

    def getVideoBitRateMode(self):
        return self.videoBitRateMode

    def setVideoBitRateMode(self, newVideoBitRateMode):
        self.videoBitRateMode = newVideoBitRateMode

    def getVideoWidth(self):
        return self.videoWidth

    def setVideoWidth(self, newVideoWidth):
        self.videoWidth = newVideoWidth

    def getVideoHeight(self):
        return self.videoHeight

    def setVideoHeight(self, newVideoHeight):
        self.videoHeight = newVideoHeight

    def getVideoFrameRate(self):
        return self.videoFrameRate

    def setVideoFrameRate(self, newVideoFrameRate):
        self.videoFrameRate = newVideoFrameRate

    def getVideoDar(self):
        return self.videoDar

    def setVideoDar(self, newVideoDar):
        self.videoDar = newVideoDar

    def getVideoRotation(self):
        return self.videoRotation

    def setVideoRotation(self, newVideoRotation):
        self.videoRotation = newVideoRotation

    def getAudioFormat(self):
        return self.audioFormat

    def setAudioFormat(self, newAudioFormat):
        self.audioFormat = newAudioFormat

    def getAudioCodecId(self):
        return self.audioCodecId

    def setAudioCodecId(self, newAudioCodecId):
        self.audioCodecId = newAudioCodecId

    def getAudioDuration(self):
        return self.audioDuration

    def setAudioDuration(self, newAudioDuration):
        self.audioDuration = newAudioDuration

    def getAudioBitRate(self):
        return self.audioBitRate

    def setAudioBitRate(self, newAudioBitRate):
        self.audioBitRate = newAudioBitRate

    def getAudioBitRateMode(self):
        return self.audioBitRateMode

    def setAudioBitRateMode(self, newAudioBitRateMode):
        self.audioBitRateMode = newAudioBitRateMode

    def getAudioChannels(self):
        return self.audioChannels

    def setAudioChannels(self, newAudioChannels):
        self.audioChannels = newAudioChannels

    def getAudioSamplingRate(self):
        return self.audioSamplingRate

    def setAudioSamplingRate(self, newAudioSamplingRate):
        self.audioSamplingRate = newAudioSamplingRate

    def getAudioResolution(self):
        return self.audioResolution

    def setAudioResolution(self, newAudioResolution):
        self.audioResolution = newAudioResolution

    def getWritingLib(self):
        return self.writingLib

    def setWritingLib(self, newWritingLib):
        self.writingLib = newWritingLib

    def getRawData(self):
        return self.rawData

    def setRawData(self, newRawData):
        self.rawData = newRawData

    def getMultiStreamInfo(self):
        return self.multiStreamInfo

    def setMultiStreamInfo(self, newMultiStreamInfo):
        self.multiStreamInfo = newMultiStreamInfo

    def getScanType(self):
        return self.scanType

    def setScanType(self, newScanType):
        self.scanType = newScanType

    def getMultiStream(self):
        return self.multiStream

    def setMultiStream(self, newMultiStream):
        self.multiStream = newMultiStream


class KalturaMediaInfoListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMediaInfo
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


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


class KalturaSearch(KalturaObjectBase):
    def __init__(self,
            keyWords=NotImplemented,
            searchSource=NotImplemented,
            mediaType=NotImplemented,
            extraData=NotImplemented,
            authData=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.keyWords = keyWords

        # @var KalturaSearchProviderType
        self.searchSource = searchSource

        # @var KalturaMediaType
        self.mediaType = mediaType

        # Use this field to pass dynamic data for searching
        # For example - if you set this field to "mymovies_$partner_id"
        # The $partner_id will be automatically replcaed with your real partner Id
        # @var string
        self.extraData = extraData

        # @var string
        self.authData = authData


    PROPERTY_LOADERS = {
        'keyWords': getXmlNodeText, 
        'searchSource': (KalturaEnumsFactory.createInt, "KalturaSearchProviderType"), 
        'mediaType': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'extraData': getXmlNodeText, 
        'authData': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearch.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearch")
        kparams.addStringIfDefined("keyWords", self.keyWords)
        kparams.addIntEnumIfDefined("searchSource", self.searchSource)
        kparams.addIntEnumIfDefined("mediaType", self.mediaType)
        kparams.addStringIfDefined("extraData", self.extraData)
        kparams.addStringIfDefined("authData", self.authData)
        return kparams

    def getKeyWords(self):
        return self.keyWords

    def setKeyWords(self, newKeyWords):
        self.keyWords = newKeyWords

    def getSearchSource(self):
        return self.searchSource

    def setSearchSource(self, newSearchSource):
        self.searchSource = newSearchSource

    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def getExtraData(self):
        return self.extraData

    def setExtraData(self, newExtraData):
        self.extraData = newExtraData

    def getAuthData(self):
        return self.authData

    def setAuthData(self, newAuthData):
        self.authData = newAuthData


class KalturaSearchResult(KalturaSearch):
    def __init__(self,
            keyWords=NotImplemented,
            searchSource=NotImplemented,
            mediaType=NotImplemented,
            extraData=NotImplemented,
            authData=NotImplemented,
            id=NotImplemented,
            title=NotImplemented,
            thumbUrl=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            url=NotImplemented,
            sourceLink=NotImplemented,
            credit=NotImplemented,
            licenseType=NotImplemented,
            flashPlaybackType=NotImplemented):
        KalturaSearch.__init__(self,
            keyWords,
            searchSource,
            mediaType,
            extraData,
            authData)

        # @var string
        self.id = id

        # @var string
        self.title = title

        # @var string
        self.thumbUrl = thumbUrl

        # @var string
        self.description = description

        # @var string
        self.tags = tags

        # @var string
        self.url = url

        # @var string
        self.sourceLink = sourceLink

        # @var string
        self.credit = credit

        # @var KalturaLicenseType
        self.licenseType = licenseType

        # @var string
        self.flashPlaybackType = flashPlaybackType


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'title': getXmlNodeText, 
        'thumbUrl': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'url': getXmlNodeText, 
        'sourceLink': getXmlNodeText, 
        'credit': getXmlNodeText, 
        'licenseType': (KalturaEnumsFactory.createInt, "KalturaLicenseType"), 
        'flashPlaybackType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearch.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearch.toParams(self)
        kparams.put("objectType", "KalturaSearchResult")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("title", self.title)
        kparams.addStringIfDefined("thumbUrl", self.thumbUrl)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("url", self.url)
        kparams.addStringIfDefined("sourceLink", self.sourceLink)
        kparams.addStringIfDefined("credit", self.credit)
        kparams.addIntEnumIfDefined("licenseType", self.licenseType)
        kparams.addStringIfDefined("flashPlaybackType", self.flashPlaybackType)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getThumbUrl(self):
        return self.thumbUrl

    def setThumbUrl(self, newThumbUrl):
        self.thumbUrl = newThumbUrl

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getSourceLink(self):
        return self.sourceLink

    def setSourceLink(self, newSourceLink):
        self.sourceLink = newSourceLink

    def getCredit(self):
        return self.credit

    def setCredit(self, newCredit):
        self.credit = newCredit

    def getLicenseType(self):
        return self.licenseType

    def setLicenseType(self, newLicenseType):
        self.licenseType = newLicenseType

    def getFlashPlaybackType(self):
        return self.flashPlaybackType

    def setFlashPlaybackType(self, newFlashPlaybackType):
        self.flashPlaybackType = newFlashPlaybackType


class KalturaMediaListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMediaEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMediaEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMixEntry(KalturaPlayableEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            duration=NotImplemented,
            msDuration=NotImplemented,
            durationType=NotImplemented,
            hasRealThumbnail=NotImplemented,
            editorType=NotImplemented,
            dataContent=NotImplemented):
        KalturaPlayableEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes,
            plays,
            views,
            width,
            height,
            duration,
            msDuration,
            durationType)

        # Indicates whether the user has submited a real thumbnail to the mix (Not the one that was generated automaticaly)
        # @var bool
        # @readonly
        self.hasRealThumbnail = hasRealThumbnail

        # The editor type used to edit the metadata
        # @var KalturaEditorType
        self.editorType = editorType

        # The xml data of the mix
        # @var string
        self.dataContent = dataContent


    PROPERTY_LOADERS = {
        'hasRealThumbnail': getXmlNodeBool, 
        'editorType': (KalturaEnumsFactory.createInt, "KalturaEditorType"), 
        'dataContent': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntry.toParams(self)
        kparams.put("objectType", "KalturaMixEntry")
        kparams.addIntEnumIfDefined("editorType", self.editorType)
        kparams.addStringIfDefined("dataContent", self.dataContent)
        return kparams

    def getHasRealThumbnail(self):
        return self.hasRealThumbnail

    def getEditorType(self):
        return self.editorType

    def setEditorType(self, newEditorType):
        self.editorType = newEditorType

    def getDataContent(self):
        return self.dataContent

    def setDataContent(self, newDataContent):
        self.dataContent = newDataContent


class KalturaMixEntryBaseFilter(KalturaPlayableEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented):
        KalturaPlayableEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlayableEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMixEntryBaseFilter")
        return kparams


class KalturaMixEntryFilter(KalturaMixEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented):
        KalturaMixEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMixEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMixEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMixEntryFilter")
        return kparams


class KalturaMixListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMixEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMixEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMixListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaClientNotification(KalturaObjectBase):
    """Client notification object to hold the notification url and the data when sending client side notifications"""

    def __init__(self,
            url=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The URL where the notification should be sent to
        # @var string
        self.url = url

        # The serialized notification data to send
        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'url': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaClientNotification.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaClientNotification")
        kparams.addStringIfDefined("url", self.url)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaKeyValue(KalturaObjectBase):
    """A key value pair representation to return an array of key-value pairs (associative array)"""

    def __init__(self,
            key=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.key = key

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'key': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaKeyValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaKeyValue")
        kparams.addStringIfDefined("key", self.key)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaPartner(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            website=NotImplemented,
            notificationUrl=NotImplemented,
            appearInSearch=NotImplemented,
            createdAt=NotImplemented,
            adminName=NotImplemented,
            adminEmail=NotImplemented,
            description=NotImplemented,
            commercialUse=NotImplemented,
            landingPage=NotImplemented,
            userLandingPage=NotImplemented,
            contentCategories=NotImplemented,
            type=NotImplemented,
            phone=NotImplemented,
            describeYourself=NotImplemented,
            adultContent=NotImplemented,
            defConversionProfileType=NotImplemented,
            notify=NotImplemented,
            status=NotImplemented,
            allowQuickEdit=NotImplemented,
            mergeEntryLists=NotImplemented,
            notificationsConfig=NotImplemented,
            maxUploadSize=NotImplemented,
            partnerPackage=NotImplemented,
            secret=NotImplemented,
            adminSecret=NotImplemented,
            cmsPassword=NotImplemented,
            allowMultiNotification=NotImplemented,
            adminLoginUsersQuota=NotImplemented,
            adminUserId=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            country=NotImplemented,
            state=NotImplemented,
            additionalParams=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.name = name

        # @var string
        self.website = website

        # @var string
        self.notificationUrl = notificationUrl

        # @var int
        self.appearInSearch = appearInSearch

        # @var int
        # @readonly
        self.createdAt = createdAt

        # deprecated - lastName and firstName replaces this field
        # @var string
        self.adminName = adminName

        # @var string
        self.adminEmail = adminEmail

        # @var string
        self.description = description

        # @var KalturaCommercialUseType
        self.commercialUse = commercialUse

        # @var string
        self.landingPage = landingPage

        # @var string
        self.userLandingPage = userLandingPage

        # @var string
        self.contentCategories = contentCategories

        # @var KalturaPartnerType
        self.type = type

        # @var string
        self.phone = phone

        # @var string
        self.describeYourself = describeYourself

        # @var bool
        self.adultContent = adultContent

        # @var string
        self.defConversionProfileType = defConversionProfileType

        # @var int
        self.notify = notify

        # @var KalturaPartnerStatus
        # @readonly
        self.status = status

        # @var int
        self.allowQuickEdit = allowQuickEdit

        # @var int
        self.mergeEntryLists = mergeEntryLists

        # @var string
        self.notificationsConfig = notificationsConfig

        # @var int
        self.maxUploadSize = maxUploadSize

        # @var int
        # @readonly
        self.partnerPackage = partnerPackage

        # @var string
        # @readonly
        self.secret = secret

        # @var string
        # @readonly
        self.adminSecret = adminSecret

        # @var string
        # @readonly
        self.cmsPassword = cmsPassword

        # @var int
        self.allowMultiNotification = allowMultiNotification

        # @var int
        # @readonly
        self.adminLoginUsersQuota = adminLoginUsersQuota

        # @var string
        self.adminUserId = adminUserId

        # firstName and lastName replace the old (deprecated) adminName
        # @var string
        self.firstName = firstName

        # lastName and firstName replace the old (deprecated) adminName
        # @var string
        self.lastName = lastName

        # country code (2char) - this field is optional
        # @var string
        self.country = country

        # state code (2char) - this field is optional
        # @var string
        self.state = state

        # @var array of KalturaKeyValue
        # @insertonly
        self.additionalParams = additionalParams


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'website': getXmlNodeText, 
        'notificationUrl': getXmlNodeText, 
        'appearInSearch': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'adminName': getXmlNodeText, 
        'adminEmail': getXmlNodeText, 
        'description': getXmlNodeText, 
        'commercialUse': (KalturaEnumsFactory.createInt, "KalturaCommercialUseType"), 
        'landingPage': getXmlNodeText, 
        'userLandingPage': getXmlNodeText, 
        'contentCategories': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createInt, "KalturaPartnerType"), 
        'phone': getXmlNodeText, 
        'describeYourself': getXmlNodeText, 
        'adultContent': getXmlNodeBool, 
        'defConversionProfileType': getXmlNodeText, 
        'notify': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'allowQuickEdit': getXmlNodeInt, 
        'mergeEntryLists': getXmlNodeInt, 
        'notificationsConfig': getXmlNodeText, 
        'maxUploadSize': getXmlNodeInt, 
        'partnerPackage': getXmlNodeInt, 
        'secret': getXmlNodeText, 
        'adminSecret': getXmlNodeText, 
        'cmsPassword': getXmlNodeText, 
        'allowMultiNotification': getXmlNodeInt, 
        'adminLoginUsersQuota': getXmlNodeInt, 
        'adminUserId': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
        'country': getXmlNodeText, 
        'state': getXmlNodeText, 
        'additionalParams': (KalturaObjectFactory.createArray, KalturaKeyValue), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartner.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartner")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("website", self.website)
        kparams.addStringIfDefined("notificationUrl", self.notificationUrl)
        kparams.addIntIfDefined("appearInSearch", self.appearInSearch)
        kparams.addStringIfDefined("adminName", self.adminName)
        kparams.addStringIfDefined("adminEmail", self.adminEmail)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("commercialUse", self.commercialUse)
        kparams.addStringIfDefined("landingPage", self.landingPage)
        kparams.addStringIfDefined("userLandingPage", self.userLandingPage)
        kparams.addStringIfDefined("contentCategories", self.contentCategories)
        kparams.addIntEnumIfDefined("type", self.type)
        kparams.addStringIfDefined("phone", self.phone)
        kparams.addStringIfDefined("describeYourself", self.describeYourself)
        kparams.addBoolIfDefined("adultContent", self.adultContent)
        kparams.addStringIfDefined("defConversionProfileType", self.defConversionProfileType)
        kparams.addIntIfDefined("notify", self.notify)
        kparams.addIntIfDefined("allowQuickEdit", self.allowQuickEdit)
        kparams.addIntIfDefined("mergeEntryLists", self.mergeEntryLists)
        kparams.addStringIfDefined("notificationsConfig", self.notificationsConfig)
        kparams.addIntIfDefined("maxUploadSize", self.maxUploadSize)
        kparams.addIntIfDefined("allowMultiNotification", self.allowMultiNotification)
        kparams.addStringIfDefined("adminUserId", self.adminUserId)
        kparams.addStringIfDefined("firstName", self.firstName)
        kparams.addStringIfDefined("lastName", self.lastName)
        kparams.addStringIfDefined("country", self.country)
        kparams.addStringIfDefined("state", self.state)
        kparams.addArrayIfDefined("additionalParams", self.additionalParams)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getWebsite(self):
        return self.website

    def setWebsite(self, newWebsite):
        self.website = newWebsite

    def getNotificationUrl(self):
        return self.notificationUrl

    def setNotificationUrl(self, newNotificationUrl):
        self.notificationUrl = newNotificationUrl

    def getAppearInSearch(self):
        return self.appearInSearch

    def setAppearInSearch(self, newAppearInSearch):
        self.appearInSearch = newAppearInSearch

    def getCreatedAt(self):
        return self.createdAt

    def getAdminName(self):
        return self.adminName

    def setAdminName(self, newAdminName):
        self.adminName = newAdminName

    def getAdminEmail(self):
        return self.adminEmail

    def setAdminEmail(self, newAdminEmail):
        self.adminEmail = newAdminEmail

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCommercialUse(self):
        return self.commercialUse

    def setCommercialUse(self, newCommercialUse):
        self.commercialUse = newCommercialUse

    def getLandingPage(self):
        return self.landingPage

    def setLandingPage(self, newLandingPage):
        self.landingPage = newLandingPage

    def getUserLandingPage(self):
        return self.userLandingPage

    def setUserLandingPage(self, newUserLandingPage):
        self.userLandingPage = newUserLandingPage

    def getContentCategories(self):
        return self.contentCategories

    def setContentCategories(self, newContentCategories):
        self.contentCategories = newContentCategories

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getPhone(self):
        return self.phone

    def setPhone(self, newPhone):
        self.phone = newPhone

    def getDescribeYourself(self):
        return self.describeYourself

    def setDescribeYourself(self, newDescribeYourself):
        self.describeYourself = newDescribeYourself

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getDefConversionProfileType(self):
        return self.defConversionProfileType

    def setDefConversionProfileType(self, newDefConversionProfileType):
        self.defConversionProfileType = newDefConversionProfileType

    def getNotify(self):
        return self.notify

    def setNotify(self, newNotify):
        self.notify = newNotify

    def getStatus(self):
        return self.status

    def getAllowQuickEdit(self):
        return self.allowQuickEdit

    def setAllowQuickEdit(self, newAllowQuickEdit):
        self.allowQuickEdit = newAllowQuickEdit

    def getMergeEntryLists(self):
        return self.mergeEntryLists

    def setMergeEntryLists(self, newMergeEntryLists):
        self.mergeEntryLists = newMergeEntryLists

    def getNotificationsConfig(self):
        return self.notificationsConfig

    def setNotificationsConfig(self, newNotificationsConfig):
        self.notificationsConfig = newNotificationsConfig

    def getMaxUploadSize(self):
        return self.maxUploadSize

    def setMaxUploadSize(self, newMaxUploadSize):
        self.maxUploadSize = newMaxUploadSize

    def getPartnerPackage(self):
        return self.partnerPackage

    def getSecret(self):
        return self.secret

    def getAdminSecret(self):
        return self.adminSecret

    def getCmsPassword(self):
        return self.cmsPassword

    def getAllowMultiNotification(self):
        return self.allowMultiNotification

    def setAllowMultiNotification(self, newAllowMultiNotification):
        self.allowMultiNotification = newAllowMultiNotification

    def getAdminLoginUsersQuota(self):
        return self.adminLoginUsersQuota

    def getAdminUserId(self):
        return self.adminUserId

    def setAdminUserId(self, newAdminUserId):
        self.adminUserId = newAdminUserId

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getCountry(self):
        return self.country

    def setCountry(self, newCountry):
        self.country = newCountry

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState

    def getAdditionalParams(self):
        return self.additionalParams

    def setAdditionalParams(self, newAdditionalParams):
        self.additionalParams = newAdditionalParams


class KalturaPartnerUsage(KalturaObjectBase):
    def __init__(self,
            hostingGB=NotImplemented,
            Percent=NotImplemented,
            packageBW=NotImplemented,
            usageGB=NotImplemented,
            reachedLimitDate=NotImplemented,
            usageGraph=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Partner total hosting in GB on the disk
        # @var float
        # @readonly
        self.hostingGB = hostingGB

        # percent of usage out of partner's package. if usageGB is 5 and package is 10GB, this value will be 50
        # @var float
        # @readonly
        self.Percent = Percent

        # package total BW - actually this is usage, which represents BW+storage
        # @var int
        # @readonly
        self.packageBW = packageBW

        # total usage in GB - including bandwidth and storage
        # @var int
        # @readonly
        self.usageGB = usageGB

        # date when partner reached the limit of his package (timestamp)
        # @var int
        # @readonly
        self.reachedLimitDate = reachedLimitDate

        # a semi-colon separated list of comma-separated key-values to represent a usage graph.
        # keys could be 1-12 for a year view (1,1.2;2,1.1;3,0.9;...;12,1.4;)
        # keys could be 1-[28,29,30,31] depending on the requested month, for a daily view in a given month (1,0.4;2,0.2;...;31,0.1;)
        # @var string
        # @readonly
        self.usageGraph = usageGraph


    PROPERTY_LOADERS = {
        'hostingGB': getXmlNodeFloat, 
        'Percent': getXmlNodeFloat, 
        'packageBW': getXmlNodeInt, 
        'usageGB': getXmlNodeInt, 
        'reachedLimitDate': getXmlNodeInt, 
        'usageGraph': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerUsage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerUsage")
        return kparams

    def getHostingGB(self):
        return self.hostingGB

    def getPercent(self):
        return self.Percent

    def getPackageBW(self):
        return self.packageBW

    def getUsageGB(self):
        return self.usageGB

    def getReachedLimitDate(self):
        return self.reachedLimitDate

    def getUsageGraph(self):
        return self.usageGraph


class KalturaPermissionItem(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            partnerId=NotImplemented,
            tags=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var KalturaPermissionItemType
        # @readonly
        self.type = type

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.tags = tags

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaPermissionItemType"), 
        'partnerId': getXmlNodeInt, 
        'tags': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionItem")
        kparams.addStringIfDefined("tags", self.tags)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getPartnerId(self):
        return self.partnerId

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaPermissionItemBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var KalturaPermissionItemType
        self.typeEqual = typeEqual

        # @var string
        self.typeIn = typeIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaPermissionItemType"), 
        'typeIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

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


class KalturaPermissionItemFilter(KalturaPermissionItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaPermissionItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemFilter")
        return kparams


class KalturaPermissionItemListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPermissionItem
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPermissionItem), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaPermission(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            friendlyName=NotImplemented,
            description=NotImplemented,
            status=NotImplemented,
            partnerId=NotImplemented,
            dependsOnPermissionNames=NotImplemented,
            tags=NotImplemented,
            permissionItemsIds=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerGroup=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var KalturaPermissionType
        # @readonly
        self.type = type

        # @var string
        self.name = name

        # @var string
        self.friendlyName = friendlyName

        # @var string
        self.description = description

        # @var KalturaPermissionStatus
        self.status = status

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.dependsOnPermissionNames = dependsOnPermissionNames

        # @var string
        self.tags = tags

        # @var string
        self.permissionItemsIds = permissionItemsIds

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var string
        self.partnerGroup = partnerGroup


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createInt, "KalturaPermissionType"), 
        'name': getXmlNodeText, 
        'friendlyName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaPermissionStatus"), 
        'partnerId': getXmlNodeInt, 
        'dependsOnPermissionNames': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'permissionItemsIds': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerGroup': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermission.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermission")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("friendlyName", self.friendlyName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("dependsOnPermissionNames", self.dependsOnPermissionNames)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("permissionItemsIds", self.permissionItemsIds)
        kparams.addStringIfDefined("partnerGroup", self.partnerGroup)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFriendlyName(self):
        return self.friendlyName

    def setFriendlyName(self, newFriendlyName):
        self.friendlyName = newFriendlyName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getPartnerId(self):
        return self.partnerId

    def getDependsOnPermissionNames(self):
        return self.dependsOnPermissionNames

    def setDependsOnPermissionNames(self, newDependsOnPermissionNames):
        self.dependsOnPermissionNames = newDependsOnPermissionNames

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getPermissionItemsIds(self):
        return self.permissionItemsIds

    def setPermissionItemsIds(self, newPermissionItemsIds):
        self.permissionItemsIds = newPermissionItemsIds

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerGroup(self):
        return self.partnerGroup

    def setPartnerGroup(self, newPartnerGroup):
        self.partnerGroup = newPartnerGroup


class KalturaPermissionBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            friendlyNameLike=NotImplemented,
            descriptionLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            dependsOnPermissionNamesMultiLikeOr=NotImplemented,
            dependsOnPermissionNamesMultiLikeAnd=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var KalturaPermissionType
        self.typeEqual = typeEqual

        # @var string
        self.typeIn = typeIn

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.nameIn = nameIn

        # @var string
        self.friendlyNameLike = friendlyNameLike

        # @var string
        self.descriptionLike = descriptionLike

        # @var KalturaPermissionStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.dependsOnPermissionNamesMultiLikeOr = dependsOnPermissionNamesMultiLikeOr

        # @var string
        self.dependsOnPermissionNamesMultiLikeAnd = dependsOnPermissionNamesMultiLikeAnd

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createInt, "KalturaPermissionType"), 
        'typeIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'nameIn': getXmlNodeText, 
        'friendlyNameLike': getXmlNodeText, 
        'descriptionLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaPermissionStatus"), 
        'statusIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'dependsOnPermissionNamesMultiLikeOr': getXmlNodeText, 
        'dependsOnPermissionNamesMultiLikeAnd': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("nameIn", self.nameIn)
        kparams.addStringIfDefined("friendlyNameLike", self.friendlyNameLike)
        kparams.addStringIfDefined("descriptionLike", self.descriptionLike)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("dependsOnPermissionNamesMultiLikeOr", self.dependsOnPermissionNamesMultiLikeOr)
        kparams.addStringIfDefined("dependsOnPermissionNamesMultiLikeAnd", self.dependsOnPermissionNamesMultiLikeAnd)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameIn(self):
        return self.nameIn

    def setNameIn(self, newNameIn):
        self.nameIn = newNameIn

    def getFriendlyNameLike(self):
        return self.friendlyNameLike

    def setFriendlyNameLike(self, newFriendlyNameLike):
        self.friendlyNameLike = newFriendlyNameLike

    def getDescriptionLike(self):
        return self.descriptionLike

    def setDescriptionLike(self, newDescriptionLike):
        self.descriptionLike = newDescriptionLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getDependsOnPermissionNamesMultiLikeOr(self):
        return self.dependsOnPermissionNamesMultiLikeOr

    def setDependsOnPermissionNamesMultiLikeOr(self, newDependsOnPermissionNamesMultiLikeOr):
        self.dependsOnPermissionNamesMultiLikeOr = newDependsOnPermissionNamesMultiLikeOr

    def getDependsOnPermissionNamesMultiLikeAnd(self):
        return self.dependsOnPermissionNamesMultiLikeAnd

    def setDependsOnPermissionNamesMultiLikeAnd(self, newDependsOnPermissionNamesMultiLikeAnd):
        self.dependsOnPermissionNamesMultiLikeAnd = newDependsOnPermissionNamesMultiLikeAnd

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

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


class KalturaPermissionFilter(KalturaPermissionBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            friendlyNameLike=NotImplemented,
            descriptionLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            dependsOnPermissionNamesMultiLikeOr=NotImplemented,
            dependsOnPermissionNamesMultiLikeAnd=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaPermissionBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            nameEqual,
            nameIn,
            friendlyNameLike,
            descriptionLike,
            statusEqual,
            statusIn,
            partnerIdEqual,
            partnerIdIn,
            dependsOnPermissionNamesMultiLikeOr,
            dependsOnPermissionNamesMultiLikeAnd,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionFilter")
        return kparams


class KalturaPermissionListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPermission
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPermission), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMediaEntryFilterForPlaylist(KalturaMediaEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented,
            limit=NotImplemented):
        KalturaMediaEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)

        # @var int
        self.limit = limit


    PROPERTY_LOADERS = {
        'limit': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaMediaEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryFilterForPlaylist.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryFilterForPlaylist")
        kparams.addIntIfDefined("limit", self.limit)
        return kparams

    def getLimit(self):
        return self.limit

    def setLimit(self, newLimit):
        self.limit = newLimit


class KalturaPlaylist(KalturaBaseEntry):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIds=NotImplemented,
            status=NotImplemented,
            moderationStatus=NotImplemented,
            moderationCount=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            rank=NotImplemented,
            totalRank=NotImplemented,
            votes=NotImplemented,
            groupId=NotImplemented,
            partnerData=NotImplemented,
            downloadUrl=NotImplemented,
            searchText=NotImplemented,
            licenseType=NotImplemented,
            version=NotImplemented,
            thumbnailUrl=NotImplemented,
            accessControlId=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            referenceId=NotImplemented,
            replacingEntryId=NotImplemented,
            replacedEntryId=NotImplemented,
            replacementStatus=NotImplemented,
            partnerSortValue=NotImplemented,
            conversionProfileId=NotImplemented,
            rootEntryId=NotImplemented,
            operationAttributes=NotImplemented,
            playlistContent=NotImplemented,
            filters=NotImplemented,
            totalResults=NotImplemented,
            playlistType=NotImplemented,
            plays=NotImplemented,
            views=NotImplemented,
            duration=NotImplemented):
        KalturaBaseEntry.__init__(self,
            id,
            name,
            description,
            partnerId,
            userId,
            tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            rootEntryId,
            operationAttributes)

        # Content of the playlist - 
        # XML if the playlistType is dynamic 
        # text if the playlistType is static 
        # url if the playlistType is mRss
        # @var string
        self.playlistContent = playlistContent

        # @var array of KalturaMediaEntryFilterForPlaylist
        self.filters = filters

        # @var int
        self.totalResults = totalResults

        # Type of playlist
        # @var KalturaPlaylistType
        self.playlistType = playlistType

        # Number of plays
        # @var int
        # @readonly
        self.plays = plays

        # Number of views
        # @var int
        # @readonly
        self.views = views

        # The duration in seconds
        # @var int
        # @readonly
        self.duration = duration


    PROPERTY_LOADERS = {
        'playlistContent': getXmlNodeText, 
        'filters': (KalturaObjectFactory.createArray, KalturaMediaEntryFilterForPlaylist), 
        'totalResults': getXmlNodeInt, 
        'playlistType': (KalturaEnumsFactory.createInt, "KalturaPlaylistType"), 
        'plays': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylist.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaPlaylist")
        kparams.addStringIfDefined("playlistContent", self.playlistContent)
        kparams.addArrayIfDefined("filters", self.filters)
        kparams.addIntIfDefined("totalResults", self.totalResults)
        kparams.addIntEnumIfDefined("playlistType", self.playlistType)
        return kparams

    def getPlaylistContent(self):
        return self.playlistContent

    def setPlaylistContent(self, newPlaylistContent):
        self.playlistContent = newPlaylistContent

    def getFilters(self):
        return self.filters

    def setFilters(self, newFilters):
        self.filters = newFilters

    def getTotalResults(self):
        return self.totalResults

    def setTotalResults(self, newTotalResults):
        self.totalResults = newTotalResults

    def getPlaylistType(self):
        return self.playlistType

    def setPlaylistType(self, newPlaylistType):
        self.playlistType = newPlaylistType

    def getPlays(self):
        return self.plays

    def getViews(self):
        return self.views

    def getDuration(self):
        return self.duration


class KalturaPlaylistBaseFilter(KalturaBaseEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented):
        KalturaBaseEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaPlaylistBaseFilter")
        return kparams


class KalturaPlaylistFilter(KalturaPlaylistBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented):
        KalturaPlaylistBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlaylistBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlaylistBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPlaylistFilter")
        return kparams


class KalturaPlaylistListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPlaylist
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPlaylist), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPlaylistListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaReportInputFilter(KalturaObjectBase):
    def __init__(self,
            fromDate=NotImplemented,
            toDate=NotImplemented,
            keywords=NotImplemented,
            searchInTags=NotImplemented,
            searchInAdminTags=NotImplemented,
            categories=NotImplemented,
            timeZoneOffset=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.fromDate = fromDate

        # @var int
        self.toDate = toDate

        # @var string
        self.keywords = keywords

        # @var bool
        self.searchInTags = searchInTags

        # @var bool
        self.searchInAdminTags = searchInAdminTags

        # @var string
        self.categories = categories

        # time zone offset in minutes
        # @var int
        self.timeZoneOffset = timeZoneOffset


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
        'keywords': getXmlNodeText, 
        'searchInTags': getXmlNodeBool, 
        'searchInAdminTags': getXmlNodeBool, 
        'categories': getXmlNodeText, 
        'timeZoneOffset': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportInputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportInputFilter")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("toDate", self.toDate)
        kparams.addStringIfDefined("keywords", self.keywords)
        kparams.addBoolIfDefined("searchInTags", self.searchInTags)
        kparams.addBoolIfDefined("searchInAdminTags", self.searchInAdminTags)
        kparams.addStringIfDefined("categories", self.categories)
        kparams.addIntIfDefined("timeZoneOffset", self.timeZoneOffset)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate

    def getKeywords(self):
        return self.keywords

    def setKeywords(self, newKeywords):
        self.keywords = newKeywords

    def getSearchInTags(self):
        return self.searchInTags

    def setSearchInTags(self, newSearchInTags):
        self.searchInTags = newSearchInTags

    def getSearchInAdminTags(self):
        return self.searchInAdminTags

    def setSearchInAdminTags(self, newSearchInAdminTags):
        self.searchInAdminTags = newSearchInAdminTags

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories

    def getTimeZoneOffset(self):
        return self.timeZoneOffset

    def setTimeZoneOffset(self, newTimeZoneOffset):
        self.timeZoneOffset = newTimeZoneOffset


class KalturaReportGraph(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.id = id

        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportGraph.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportGraph")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaReportTotal(KalturaObjectBase):
    def __init__(self,
            header=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.header = header

        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'header': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportTotal.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportTotal")
        kparams.addStringIfDefined("header", self.header)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getHeader(self):
        return self.header

    def setHeader(self, newHeader):
        self.header = newHeader

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaReportTable(KalturaObjectBase):
    def __init__(self,
            header=NotImplemented,
            data=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.header = header

        # @var string
        # @readonly
        self.data = data

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'header': getXmlNodeText, 
        'data': getXmlNodeText, 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportTable.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportTable")
        return kparams

    def getHeader(self):
        return self.header

    def getData(self):
        return self.data

    def getTotalCount(self):
        return self.totalCount


class KalturaReportResponse(KalturaObjectBase):
    def __init__(self,
            columns=NotImplemented,
            results=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.columns = columns

        # @var array of KalturaString
        self.results = results


    PROPERTY_LOADERS = {
        'columns': getXmlNodeText, 
        'results': (KalturaObjectFactory.createArray, KalturaString), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportResponse")
        kparams.addStringIfDefined("columns", self.columns)
        kparams.addArrayIfDefined("results", self.results)
        return kparams

    def getColumns(self):
        return self.columns

    def setColumns(self, newColumns):
        self.columns = newColumns

    def getResults(self):
        return self.results

    def setResults(self, newResults):
        self.results = newResults


class KalturaSearchResultResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            needMediaInfo=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaSearchResult
        # @readonly
        self.objects = objects

        # @var bool
        # @readonly
        self.needMediaInfo = needMediaInfo


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSearchResult), 
        'needMediaInfo': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchResultResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchResultResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getNeedMediaInfo(self):
        return self.needMediaInfo


class KalturaSearchAuthData(KalturaObjectBase):
    def __init__(self,
            authData=NotImplemented,
            loginUrl=NotImplemented,
            message=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The authentication data that further should be used for search
        # @var string
        self.authData = authData

        # Login URL when user need to sign-in and authorize the search
        # @var string
        self.loginUrl = loginUrl

        # Information when there was an error
        # @var string
        self.message = message


    PROPERTY_LOADERS = {
        'authData': getXmlNodeText, 
        'loginUrl': getXmlNodeText, 
        'message': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchAuthData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchAuthData")
        kparams.addStringIfDefined("authData", self.authData)
        kparams.addStringIfDefined("loginUrl", self.loginUrl)
        kparams.addStringIfDefined("message", self.message)
        return kparams

    def getAuthData(self):
        return self.authData

    def setAuthData(self, newAuthData):
        self.authData = newAuthData

    def getLoginUrl(self):
        return self.loginUrl

    def setLoginUrl(self, newLoginUrl):
        self.loginUrl = newLoginUrl

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage


class KalturaStartWidgetSessionResponse(KalturaObjectBase):
    def __init__(self,
            partnerId=NotImplemented,
            ks=NotImplemented,
            userId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        # @readonly
        self.ks = ks

        # @var string
        # @readonly
        self.userId = userId


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'ks': getXmlNodeText, 
        'userId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStartWidgetSessionResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStartWidgetSessionResponse")
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def getKs(self):
        return self.ks

    def getUserId(self):
        return self.userId


class KalturaStatsEvent(KalturaObjectBase):
    """Will hold data from the Kaltura UI components to be passed on to the reports and analytics system"""

    def __init__(self,
            clientVer=NotImplemented,
            eventType=NotImplemented,
            eventTimestamp=NotImplemented,
            sessionId=NotImplemented,
            partnerId=NotImplemented,
            entryId=NotImplemented,
            uniqueViewer=NotImplemented,
            widgetId=NotImplemented,
            uiconfId=NotImplemented,
            userId=NotImplemented,
            currentPoint=NotImplemented,
            duration=NotImplemented,
            userIp=NotImplemented,
            processDuration=NotImplemented,
            controlId=NotImplemented,
            seek=NotImplemented,
            newPoint=NotImplemented,
            referrer=NotImplemented,
            isFirstInSession=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.clientVer = clientVer

        # @var KalturaStatsEventType
        self.eventType = eventType

        # the client's timestamp of this event
        # @var float
        self.eventTimestamp = eventTimestamp

        # a unique string generated by the client that will represent the client-side session: the primary component will pass it on to other components that sprout from it
        # @var string
        self.sessionId = sessionId

        # @var int
        self.partnerId = partnerId

        # @var string
        self.entryId = entryId

        # the UV cookie - creates in the operational system and should be passed on ofr every event
        # @var string
        self.uniqueViewer = uniqueViewer

        # @var string
        self.widgetId = widgetId

        # @var int
        self.uiconfId = uiconfId

        # the partner's user id
        # @var string
        self.userId = userId

        # the timestamp along the video when the event happend
        # @var int
        self.currentPoint = currentPoint

        # the duration of the video in milliseconds - will make it much faster than quering the db for each entry
        # @var int
        self.duration = duration

        # will be retrieved from the request of the user
        # @var string
        # @readonly
        self.userIp = userIp

        # the time in milliseconds the event took
        # @var int
        self.processDuration = processDuration

        # the id of the GUI control - will be used in the future to better understand what the user clicked
        # @var string
        self.controlId = controlId

        # true if the user ever used seek in this session
        # @var bool
        self.seek = seek

        # timestamp of the new point on the timeline of the video after the user seeks
        # @var int
        self.newPoint = newPoint

        # the referrer of the client
        # @var string
        self.referrer = referrer

        # will indicate if the event is thrown for the first video in the session
        # @var bool
        self.isFirstInSession = isFirstInSession


    PROPERTY_LOADERS = {
        'clientVer': getXmlNodeText, 
        'eventType': (KalturaEnumsFactory.createInt, "KalturaStatsEventType"), 
        'eventTimestamp': getXmlNodeFloat, 
        'sessionId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'uniqueViewer': getXmlNodeText, 
        'widgetId': getXmlNodeText, 
        'uiconfId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'currentPoint': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'userIp': getXmlNodeText, 
        'processDuration': getXmlNodeInt, 
        'controlId': getXmlNodeText, 
        'seek': getXmlNodeBool, 
        'newPoint': getXmlNodeInt, 
        'referrer': getXmlNodeText, 
        'isFirstInSession': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStatsEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStatsEvent")
        kparams.addStringIfDefined("clientVer", self.clientVer)
        kparams.addIntEnumIfDefined("eventType", self.eventType)
        kparams.addFloatIfDefined("eventTimestamp", self.eventTimestamp)
        kparams.addStringIfDefined("sessionId", self.sessionId)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("uniqueViewer", self.uniqueViewer)
        kparams.addStringIfDefined("widgetId", self.widgetId)
        kparams.addIntIfDefined("uiconfId", self.uiconfId)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addIntIfDefined("currentPoint", self.currentPoint)
        kparams.addIntIfDefined("duration", self.duration)
        kparams.addIntIfDefined("processDuration", self.processDuration)
        kparams.addStringIfDefined("controlId", self.controlId)
        kparams.addBoolIfDefined("seek", self.seek)
        kparams.addIntIfDefined("newPoint", self.newPoint)
        kparams.addStringIfDefined("referrer", self.referrer)
        kparams.addBoolIfDefined("isFirstInSession", self.isFirstInSession)
        return kparams

    def getClientVer(self):
        return self.clientVer

    def setClientVer(self, newClientVer):
        self.clientVer = newClientVer

    def getEventType(self):
        return self.eventType

    def setEventType(self, newEventType):
        self.eventType = newEventType

    def getEventTimestamp(self):
        return self.eventTimestamp

    def setEventTimestamp(self, newEventTimestamp):
        self.eventTimestamp = newEventTimestamp

    def getSessionId(self):
        return self.sessionId

    def setSessionId(self, newSessionId):
        self.sessionId = newSessionId

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getUniqueViewer(self):
        return self.uniqueViewer

    def setUniqueViewer(self, newUniqueViewer):
        self.uniqueViewer = newUniqueViewer

    def getWidgetId(self):
        return self.widgetId

    def setWidgetId(self, newWidgetId):
        self.widgetId = newWidgetId

    def getUiconfId(self):
        return self.uiconfId

    def setUiconfId(self, newUiconfId):
        self.uiconfId = newUiconfId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getCurrentPoint(self):
        return self.currentPoint

    def setCurrentPoint(self, newCurrentPoint):
        self.currentPoint = newCurrentPoint

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration

    def getUserIp(self):
        return self.userIp

    def getProcessDuration(self):
        return self.processDuration

    def setProcessDuration(self, newProcessDuration):
        self.processDuration = newProcessDuration

    def getControlId(self):
        return self.controlId

    def setControlId(self, newControlId):
        self.controlId = newControlId

    def getSeek(self):
        return self.seek

    def setSeek(self, newSeek):
        self.seek = newSeek

    def getNewPoint(self):
        return self.newPoint

    def setNewPoint(self, newNewPoint):
        self.newPoint = newNewPoint

    def getReferrer(self):
        return self.referrer

    def setReferrer(self, newReferrer):
        self.referrer = newReferrer

    def getIsFirstInSession(self):
        return self.isFirstInSession

    def setIsFirstInSession(self, newIsFirstInSession):
        self.isFirstInSession = newIsFirstInSession


class KalturaStatsKmcEvent(KalturaObjectBase):
    """Will hold data from the Kaltura UI components to be passed on to the reports and analytics system"""

    def __init__(self,
            clientVer=NotImplemented,
            kmcEventActionPath=NotImplemented,
            kmcEventType=NotImplemented,
            eventTimestamp=NotImplemented,
            sessionId=NotImplemented,
            partnerId=NotImplemented,
            entryId=NotImplemented,
            widgetId=NotImplemented,
            uiconfId=NotImplemented,
            userId=NotImplemented,
            userIp=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.clientVer = clientVer

        # @var string
        self.kmcEventActionPath = kmcEventActionPath

        # @var KalturaStatsKmcEventType
        self.kmcEventType = kmcEventType

        # the client's timestamp of this event
        # @var float
        self.eventTimestamp = eventTimestamp

        # a unique string generated by the client that will represent the client-side session: the primary component will pass it on to other components that sprout from it
        # @var string
        self.sessionId = sessionId

        # @var int
        self.partnerId = partnerId

        # @var string
        self.entryId = entryId

        # @var string
        self.widgetId = widgetId

        # @var int
        self.uiconfId = uiconfId

        # the partner's user id
        # @var string
        self.userId = userId

        # will be retrieved from the request of the user
        # @var string
        # @readonly
        self.userIp = userIp


    PROPERTY_LOADERS = {
        'clientVer': getXmlNodeText, 
        'kmcEventActionPath': getXmlNodeText, 
        'kmcEventType': (KalturaEnumsFactory.createInt, "KalturaStatsKmcEventType"), 
        'eventTimestamp': getXmlNodeFloat, 
        'sessionId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'widgetId': getXmlNodeText, 
        'uiconfId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'userIp': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStatsKmcEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStatsKmcEvent")
        kparams.addStringIfDefined("clientVer", self.clientVer)
        kparams.addStringIfDefined("kmcEventActionPath", self.kmcEventActionPath)
        kparams.addIntEnumIfDefined("kmcEventType", self.kmcEventType)
        kparams.addFloatIfDefined("eventTimestamp", self.eventTimestamp)
        kparams.addStringIfDefined("sessionId", self.sessionId)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("widgetId", self.widgetId)
        kparams.addIntIfDefined("uiconfId", self.uiconfId)
        kparams.addStringIfDefined("userId", self.userId)
        return kparams

    def getClientVer(self):
        return self.clientVer

    def setClientVer(self, newClientVer):
        self.clientVer = newClientVer

    def getKmcEventActionPath(self):
        return self.kmcEventActionPath

    def setKmcEventActionPath(self, newKmcEventActionPath):
        self.kmcEventActionPath = newKmcEventActionPath

    def getKmcEventType(self):
        return self.kmcEventType

    def setKmcEventType(self, newKmcEventType):
        self.kmcEventType = newKmcEventType

    def getEventTimestamp(self):
        return self.eventTimestamp

    def setEventTimestamp(self, newEventTimestamp):
        self.eventTimestamp = newEventTimestamp

    def getSessionId(self):
        return self.sessionId

    def setSessionId(self, newSessionId):
        self.sessionId = newSessionId

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getWidgetId(self):
        return self.widgetId

    def setWidgetId(self, newWidgetId):
        self.widgetId = newWidgetId

    def getUiconfId(self):
        return self.uiconfId

    def setUiconfId(self, newUiconfId):
        self.uiconfId = newUiconfId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getUserIp(self):
        return self.userIp


class KalturaCEError(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            browser=NotImplemented,
            serverIp=NotImplemented,
            serverOs=NotImplemented,
            phpVersion=NotImplemented,
            ceAdminEmail=NotImplemented,
            type=NotImplemented,
            description=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = id

        # @var int
        self.partnerId = partnerId

        # @var string
        self.browser = browser

        # @var string
        self.serverIp = serverIp

        # @var string
        self.serverOs = serverOs

        # @var string
        self.phpVersion = phpVersion

        # @var string
        self.ceAdminEmail = ceAdminEmail

        # @var string
        self.type = type

        # @var string
        self.description = description

        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'browser': getXmlNodeText, 
        'serverIp': getXmlNodeText, 
        'serverOs': getXmlNodeText, 
        'phpVersion': getXmlNodeText, 
        'ceAdminEmail': getXmlNodeText, 
        'type': getXmlNodeText, 
        'description': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCEError.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCEError")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("browser", self.browser)
        kparams.addStringIfDefined("serverIp", self.serverIp)
        kparams.addStringIfDefined("serverOs", self.serverOs)
        kparams.addStringIfDefined("phpVersion", self.phpVersion)
        kparams.addStringIfDefined("ceAdminEmail", self.ceAdminEmail)
        kparams.addStringIfDefined("type", self.type)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getBrowser(self):
        return self.browser

    def setBrowser(self, newBrowser):
        self.browser = newBrowser

    def getServerIp(self):
        return self.serverIp

    def setServerIp(self, newServerIp):
        self.serverIp = newServerIp

    def getServerOs(self):
        return self.serverOs

    def setServerOs(self, newServerOs):
        self.serverOs = newServerOs

    def getPhpVersion(self):
        return self.phpVersion

    def setPhpVersion(self, newPhpVersion):
        self.phpVersion = newPhpVersion

    def getCeAdminEmail(self):
        return self.ceAdminEmail

    def setCeAdminEmail(self, newCeAdminEmail):
        self.ceAdminEmail = newCeAdminEmail

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaStorageProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            desciption=NotImplemented,
            status=NotImplemented,
            protocol=NotImplemented,
            storageUrl=NotImplemented,
            storageBaseDir=NotImplemented,
            storageUsername=NotImplemented,
            storagePassword=NotImplemented,
            storageFtpPassiveMode=NotImplemented,
            deliveryHttpBaseUrl=NotImplemented,
            deliveryRmpBaseUrl=NotImplemented,
            deliveryIisBaseUrl=NotImplemented,
            minFileSize=NotImplemented,
            maxFileSize=NotImplemented,
            flavorParamsIds=NotImplemented,
            maxConcurrentConnections=NotImplemented,
            pathManagerClass=NotImplemented,
            pathManagerParams=NotImplemented,
            urlManagerClass=NotImplemented,
            urlManagerParams=NotImplemented,
            trigger=NotImplemented,
            deliveryPriority=NotImplemented,
            deliveryStatus=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.name = name

        # @var string
        self.systemName = systemName

        # @var string
        self.desciption = desciption

        # @var KalturaStorageProfileStatus
        self.status = status

        # @var KalturaStorageProfileProtocol
        self.protocol = protocol

        # @var string
        self.storageUrl = storageUrl

        # @var string
        self.storageBaseDir = storageBaseDir

        # @var string
        self.storageUsername = storageUsername

        # @var string
        self.storagePassword = storagePassword

        # @var bool
        self.storageFtpPassiveMode = storageFtpPassiveMode

        # @var string
        self.deliveryHttpBaseUrl = deliveryHttpBaseUrl

        # @var string
        self.deliveryRmpBaseUrl = deliveryRmpBaseUrl

        # @var string
        self.deliveryIisBaseUrl = deliveryIisBaseUrl

        # @var int
        self.minFileSize = minFileSize

        # @var int
        self.maxFileSize = maxFileSize

        # @var string
        self.flavorParamsIds = flavorParamsIds

        # @var int
        self.maxConcurrentConnections = maxConcurrentConnections

        # @var string
        self.pathManagerClass = pathManagerClass

        # @var array of KalturaKeyValue
        self.pathManagerParams = pathManagerParams

        # @var string
        self.urlManagerClass = urlManagerClass

        # @var array of KalturaKeyValue
        self.urlManagerParams = urlManagerParams

        # No need to create enum for temp field
        # @var int
        self.trigger = trigger

        # Delivery Priority
        # @var int
        self.deliveryPriority = deliveryPriority

        # @var KalturaStorageProfileDeliveryStatus
        self.deliveryStatus = deliveryStatus


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'desciption': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaStorageProfileStatus"), 
        'protocol': (KalturaEnumsFactory.createInt, "KalturaStorageProfileProtocol"), 
        'storageUrl': getXmlNodeText, 
        'storageBaseDir': getXmlNodeText, 
        'storageUsername': getXmlNodeText, 
        'storagePassword': getXmlNodeText, 
        'storageFtpPassiveMode': getXmlNodeBool, 
        'deliveryHttpBaseUrl': getXmlNodeText, 
        'deliveryRmpBaseUrl': getXmlNodeText, 
        'deliveryIisBaseUrl': getXmlNodeText, 
        'minFileSize': getXmlNodeInt, 
        'maxFileSize': getXmlNodeInt, 
        'flavorParamsIds': getXmlNodeText, 
        'maxConcurrentConnections': getXmlNodeInt, 
        'pathManagerClass': getXmlNodeText, 
        'pathManagerParams': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'urlManagerClass': getXmlNodeText, 
        'urlManagerParams': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'trigger': getXmlNodeInt, 
        'deliveryPriority': getXmlNodeInt, 
        'deliveryStatus': (KalturaEnumsFactory.createInt, "KalturaStorageProfileDeliveryStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStorageProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("desciption", self.desciption)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addIntEnumIfDefined("protocol", self.protocol)
        kparams.addStringIfDefined("storageUrl", self.storageUrl)
        kparams.addStringIfDefined("storageBaseDir", self.storageBaseDir)
        kparams.addStringIfDefined("storageUsername", self.storageUsername)
        kparams.addStringIfDefined("storagePassword", self.storagePassword)
        kparams.addBoolIfDefined("storageFtpPassiveMode", self.storageFtpPassiveMode)
        kparams.addStringIfDefined("deliveryHttpBaseUrl", self.deliveryHttpBaseUrl)
        kparams.addStringIfDefined("deliveryRmpBaseUrl", self.deliveryRmpBaseUrl)
        kparams.addStringIfDefined("deliveryIisBaseUrl", self.deliveryIisBaseUrl)
        kparams.addIntIfDefined("minFileSize", self.minFileSize)
        kparams.addIntIfDefined("maxFileSize", self.maxFileSize)
        kparams.addStringIfDefined("flavorParamsIds", self.flavorParamsIds)
        kparams.addIntIfDefined("maxConcurrentConnections", self.maxConcurrentConnections)
        kparams.addStringIfDefined("pathManagerClass", self.pathManagerClass)
        kparams.addArrayIfDefined("pathManagerParams", self.pathManagerParams)
        kparams.addStringIfDefined("urlManagerClass", self.urlManagerClass)
        kparams.addArrayIfDefined("urlManagerParams", self.urlManagerParams)
        kparams.addIntIfDefined("trigger", self.trigger)
        kparams.addIntIfDefined("deliveryPriority", self.deliveryPriority)
        kparams.addIntEnumIfDefined("deliveryStatus", self.deliveryStatus)
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

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDesciption(self):
        return self.desciption

    def setDesciption(self, newDesciption):
        self.desciption = newDesciption

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, newProtocol):
        self.protocol = newProtocol

    def getStorageUrl(self):
        return self.storageUrl

    def setStorageUrl(self, newStorageUrl):
        self.storageUrl = newStorageUrl

    def getStorageBaseDir(self):
        return self.storageBaseDir

    def setStorageBaseDir(self, newStorageBaseDir):
        self.storageBaseDir = newStorageBaseDir

    def getStorageUsername(self):
        return self.storageUsername

    def setStorageUsername(self, newStorageUsername):
        self.storageUsername = newStorageUsername

    def getStoragePassword(self):
        return self.storagePassword

    def setStoragePassword(self, newStoragePassword):
        self.storagePassword = newStoragePassword

    def getStorageFtpPassiveMode(self):
        return self.storageFtpPassiveMode

    def setStorageFtpPassiveMode(self, newStorageFtpPassiveMode):
        self.storageFtpPassiveMode = newStorageFtpPassiveMode

    def getDeliveryHttpBaseUrl(self):
        return self.deliveryHttpBaseUrl

    def setDeliveryHttpBaseUrl(self, newDeliveryHttpBaseUrl):
        self.deliveryHttpBaseUrl = newDeliveryHttpBaseUrl

    def getDeliveryRmpBaseUrl(self):
        return self.deliveryRmpBaseUrl

    def setDeliveryRmpBaseUrl(self, newDeliveryRmpBaseUrl):
        self.deliveryRmpBaseUrl = newDeliveryRmpBaseUrl

    def getDeliveryIisBaseUrl(self):
        return self.deliveryIisBaseUrl

    def setDeliveryIisBaseUrl(self, newDeliveryIisBaseUrl):
        self.deliveryIisBaseUrl = newDeliveryIisBaseUrl

    def getMinFileSize(self):
        return self.minFileSize

    def setMinFileSize(self, newMinFileSize):
        self.minFileSize = newMinFileSize

    def getMaxFileSize(self):
        return self.maxFileSize

    def setMaxFileSize(self, newMaxFileSize):
        self.maxFileSize = newMaxFileSize

    def getFlavorParamsIds(self):
        return self.flavorParamsIds

    def setFlavorParamsIds(self, newFlavorParamsIds):
        self.flavorParamsIds = newFlavorParamsIds

    def getMaxConcurrentConnections(self):
        return self.maxConcurrentConnections

    def setMaxConcurrentConnections(self, newMaxConcurrentConnections):
        self.maxConcurrentConnections = newMaxConcurrentConnections

    def getPathManagerClass(self):
        return self.pathManagerClass

    def setPathManagerClass(self, newPathManagerClass):
        self.pathManagerClass = newPathManagerClass

    def getPathManagerParams(self):
        return self.pathManagerParams

    def setPathManagerParams(self, newPathManagerParams):
        self.pathManagerParams = newPathManagerParams

    def getUrlManagerClass(self):
        return self.urlManagerClass

    def setUrlManagerClass(self, newUrlManagerClass):
        self.urlManagerClass = newUrlManagerClass

    def getUrlManagerParams(self):
        return self.urlManagerParams

    def setUrlManagerParams(self, newUrlManagerParams):
        self.urlManagerParams = newUrlManagerParams

    def getTrigger(self):
        return self.trigger

    def setTrigger(self, newTrigger):
        self.trigger = newTrigger

    def getDeliveryPriority(self):
        return self.deliveryPriority

    def setDeliveryPriority(self, newDeliveryPriority):
        self.deliveryPriority = newDeliveryPriority

    def getDeliveryStatus(self):
        return self.deliveryStatus

    def setDeliveryStatus(self, newDeliveryStatus):
        self.deliveryStatus = newDeliveryStatus


class KalturaStorageProfileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            protocolEqual=NotImplemented,
            protocolIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var KalturaStorageProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaStorageProfileProtocol
        self.protocolEqual = protocolEqual

        # @var string
        self.protocolIn = protocolIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaStorageProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'protocolEqual': (KalturaEnumsFactory.createInt, "KalturaStorageProfileProtocol"), 
        'protocolIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaStorageProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntEnumIfDefined("protocolEqual", self.protocolEqual)
        kparams.addStringIfDefined("protocolIn", self.protocolIn)
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

    def getProtocolEqual(self):
        return self.protocolEqual

    def setProtocolEqual(self, newProtocolEqual):
        self.protocolEqual = newProtocolEqual

    def getProtocolIn(self):
        return self.protocolIn

    def setProtocolIn(self, newProtocolIn):
        self.protocolIn = newProtocolIn


class KalturaStorageProfileFilter(KalturaStorageProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            protocolEqual=NotImplemented,
            protocolIn=NotImplemented):
        KalturaStorageProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            systemNameEqual,
            systemNameIn,
            statusEqual,
            statusIn,
            protocolEqual,
            protocolIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaStorageProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaStorageProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaStorageProfileFilter")
        return kparams


class KalturaStorageProfileListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaStorageProfile
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaStorageProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStorageProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStorageProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaBaseSyndicationFeed(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = id

        # @var string
        # @readonly
        self.feedUrl = feedUrl

        # @var int
        # @readonly
        self.partnerId = partnerId

        # link a playlist that will set what content the feed will include
        # if empty, all content will be included in feed
        # @var string
        self.playlistId = playlistId

        # feed name
        # @var string
        self.name = name

        # feed status
        # @var KalturaSyndicationFeedStatus
        # @readonly
        self.status = status

        # feed type
        # @var KalturaSyndicationFeedType
        # @insertonly
        self.type = type

        # Base URL for each video, on the partners site
        # This is required by all syndication types.
        # @var string
        self.landingPage = landingPage

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # allow_embed tells google OR yahoo weather to allow embedding the video on google OR yahoo video results
        # or just to provide a link to the landing page.
        # it is applied on the video-player_loc property in the XML (google)
        # and addes media-player tag (yahoo)
        # @var bool
        self.allowEmbed = allowEmbed

        # Select a uiconf ID as player skin to include in the kwidget url
        # @var int
        self.playerUiconfId = playerUiconfId

        # @var int
        self.flavorParamId = flavorParamId

        # @var bool
        self.transcodeExistingContent = transcodeExistingContent

        # @var bool
        self.addToDefaultConversionProfile = addToDefaultConversionProfile

        # @var string
        self.categories = categories

        # @var int
        self.storageId = storageId


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'feedUrl': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'playlistId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaSyndicationFeedStatus"), 
        'type': (KalturaEnumsFactory.createInt, "KalturaSyndicationFeedType"), 
        'landingPage': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'allowEmbed': getXmlNodeBool, 
        'playerUiconfId': getXmlNodeInt, 
        'flavorParamId': getXmlNodeInt, 
        'transcodeExistingContent': getXmlNodeBool, 
        'addToDefaultConversionProfile': getXmlNodeBool, 
        'categories': getXmlNodeText, 
        'storageId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeed")
        kparams.addStringIfDefined("playlistId", self.playlistId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntEnumIfDefined("type", self.type)
        kparams.addStringIfDefined("landingPage", self.landingPage)
        kparams.addBoolIfDefined("allowEmbed", self.allowEmbed)
        kparams.addIntIfDefined("playerUiconfId", self.playerUiconfId)
        kparams.addIntIfDefined("flavorParamId", self.flavorParamId)
        kparams.addBoolIfDefined("transcodeExistingContent", self.transcodeExistingContent)
        kparams.addBoolIfDefined("addToDefaultConversionProfile", self.addToDefaultConversionProfile)
        kparams.addStringIfDefined("categories", self.categories)
        kparams.addIntIfDefined("storageId", self.storageId)
        return kparams

    def getId(self):
        return self.id

    def getFeedUrl(self):
        return self.feedUrl

    def getPartnerId(self):
        return self.partnerId

    def getPlaylistId(self):
        return self.playlistId

    def setPlaylistId(self, newPlaylistId):
        self.playlistId = newPlaylistId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getStatus(self):
        return self.status

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getLandingPage(self):
        return self.landingPage

    def setLandingPage(self, newLandingPage):
        self.landingPage = newLandingPage

    def getCreatedAt(self):
        return self.createdAt

    def getAllowEmbed(self):
        return self.allowEmbed

    def setAllowEmbed(self, newAllowEmbed):
        self.allowEmbed = newAllowEmbed

    def getPlayerUiconfId(self):
        return self.playerUiconfId

    def setPlayerUiconfId(self, newPlayerUiconfId):
        self.playerUiconfId = newPlayerUiconfId

    def getFlavorParamId(self):
        return self.flavorParamId

    def setFlavorParamId(self, newFlavorParamId):
        self.flavorParamId = newFlavorParamId

    def getTranscodeExistingContent(self):
        return self.transcodeExistingContent

    def setTranscodeExistingContent(self, newTranscodeExistingContent):
        self.transcodeExistingContent = newTranscodeExistingContent

    def getAddToDefaultConversionProfile(self):
        return self.addToDefaultConversionProfile

    def setAddToDefaultConversionProfile(self, newAddToDefaultConversionProfile):
        self.addToDefaultConversionProfile = newAddToDefaultConversionProfile

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories

    def getStorageId(self):
        return self.storageId

    def setStorageId(self, newStorageId):
        self.storageId = newStorageId


class KalturaBaseSyndicationFeedBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedBaseFilter")
        return kparams


class KalturaBaseSyndicationFeedFilter(KalturaBaseSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedFilter")
        return kparams


class KalturaBaseSyndicationFeedListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBaseSyndicationFeed
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBaseSyndicationFeed), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaSyndicationFeedEntryCount(KalturaObjectBase):
    def __init__(self,
            totalEntryCount=NotImplemented,
            actualEntryCount=NotImplemented,
            requireTranscodingCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # the total count of entries that should appear in the feed without flavor filtering
        # @var int
        self.totalEntryCount = totalEntryCount

        # count of entries that will appear in the feed (including all relevant filters)
        # @var int
        self.actualEntryCount = actualEntryCount

        # count of entries that requires transcoding in order to be included in feed
        # @var int
        self.requireTranscodingCount = requireTranscodingCount


    PROPERTY_LOADERS = {
        'totalEntryCount': getXmlNodeInt, 
        'actualEntryCount': getXmlNodeInt, 
        'requireTranscodingCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSyndicationFeedEntryCount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSyndicationFeedEntryCount")
        kparams.addIntIfDefined("totalEntryCount", self.totalEntryCount)
        kparams.addIntIfDefined("actualEntryCount", self.actualEntryCount)
        kparams.addIntIfDefined("requireTranscodingCount", self.requireTranscodingCount)
        return kparams

    def getTotalEntryCount(self):
        return self.totalEntryCount

    def setTotalEntryCount(self, newTotalEntryCount):
        self.totalEntryCount = newTotalEntryCount

    def getActualEntryCount(self):
        return self.actualEntryCount

    def setActualEntryCount(self, newActualEntryCount):
        self.actualEntryCount = newActualEntryCount

    def getRequireTranscodingCount(self):
        return self.requireTranscodingCount

    def setRequireTranscodingCount(self, newRequireTranscodingCount):
        self.requireTranscodingCount = newRequireTranscodingCount


class KalturaThumbAsset(KalturaAsset):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented,
            thumbParamsId=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            status=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            entryId,
            partnerId,
            version,
            size,
            tags,
            fileExt,
            createdAt,
            updatedAt,
            deletedAt,
            description,
            partnerData,
            partnerDescription)

        # The Flavor Params used to create this Flavor Asset
        # @var int
        # @insertonly
        self.thumbParamsId = thumbParamsId

        # The width of the Flavor Asset
        # @var int
        # @readonly
        self.width = width

        # The height of the Flavor Asset
        # @var int
        # @readonly
        self.height = height

        # The status of the asset
        # @var KalturaThumbAssetStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'thumbParamsId': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaThumbAssetStatus"), 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaThumbAsset")
        kparams.addIntIfDefined("thumbParamsId", self.thumbParamsId)
        return kparams

    def getThumbParamsId(self):
        return self.thumbParamsId

    def setThumbParamsId(self, newThumbParamsId):
        self.thumbParamsId = newThumbParamsId

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getStatus(self):
        return self.status


class KalturaThumbParams(KalturaAssetParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            cropType=NotImplemented,
            quality=NotImplemented,
            cropX=NotImplemented,
            cropY=NotImplemented,
            cropWidth=NotImplemented,
            cropHeight=NotImplemented,
            videoOffset=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            scaleWidth=NotImplemented,
            scaleHeight=NotImplemented,
            backgroundColor=NotImplemented,
            sourceParamsId=NotImplemented,
            format=NotImplemented,
            density=NotImplemented):
        KalturaAssetParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions)

        # @var KalturaThumbCropType
        self.cropType = cropType

        # @var int
        self.quality = quality

        # @var int
        self.cropX = cropX

        # @var int
        self.cropY = cropY

        # @var int
        self.cropWidth = cropWidth

        # @var int
        self.cropHeight = cropHeight

        # @var float
        self.videoOffset = videoOffset

        # @var int
        self.width = width

        # @var int
        self.height = height

        # @var float
        self.scaleWidth = scaleWidth

        # @var float
        self.scaleHeight = scaleHeight

        # Hexadecimal value
        # @var string
        self.backgroundColor = backgroundColor

        # Id of the flavor params or the thumbnail params to be used as source for the thumbnail creation
        # @var int
        self.sourceParamsId = sourceParamsId

        # The container format of the Flavor Params
        # @var KalturaContainerFormat
        self.format = format

        # The image density (dpi) for example: 72 or 96
        # @var int
        self.density = density


    PROPERTY_LOADERS = {
        'cropType': (KalturaEnumsFactory.createInt, "KalturaThumbCropType"), 
        'quality': getXmlNodeInt, 
        'cropX': getXmlNodeInt, 
        'cropY': getXmlNodeInt, 
        'cropWidth': getXmlNodeInt, 
        'cropHeight': getXmlNodeInt, 
        'videoOffset': getXmlNodeFloat, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'scaleWidth': getXmlNodeFloat, 
        'scaleHeight': getXmlNodeFloat, 
        'backgroundColor': getXmlNodeText, 
        'sourceParamsId': getXmlNodeInt, 
        'format': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
        'density': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaThumbParams")
        kparams.addIntEnumIfDefined("cropType", self.cropType)
        kparams.addIntIfDefined("quality", self.quality)
        kparams.addIntIfDefined("cropX", self.cropX)
        kparams.addIntIfDefined("cropY", self.cropY)
        kparams.addIntIfDefined("cropWidth", self.cropWidth)
        kparams.addIntIfDefined("cropHeight", self.cropHeight)
        kparams.addFloatIfDefined("videoOffset", self.videoOffset)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        kparams.addFloatIfDefined("scaleWidth", self.scaleWidth)
        kparams.addFloatIfDefined("scaleHeight", self.scaleHeight)
        kparams.addStringIfDefined("backgroundColor", self.backgroundColor)
        kparams.addIntIfDefined("sourceParamsId", self.sourceParamsId)
        kparams.addStringEnumIfDefined("format", self.format)
        kparams.addIntIfDefined("density", self.density)
        return kparams

    def getCropType(self):
        return self.cropType

    def setCropType(self, newCropType):
        self.cropType = newCropType

    def getQuality(self):
        return self.quality

    def setQuality(self, newQuality):
        self.quality = newQuality

    def getCropX(self):
        return self.cropX

    def setCropX(self, newCropX):
        self.cropX = newCropX

    def getCropY(self):
        return self.cropY

    def setCropY(self, newCropY):
        self.cropY = newCropY

    def getCropWidth(self):
        return self.cropWidth

    def setCropWidth(self, newCropWidth):
        self.cropWidth = newCropWidth

    def getCropHeight(self):
        return self.cropHeight

    def setCropHeight(self, newCropHeight):
        self.cropHeight = newCropHeight

    def getVideoOffset(self):
        return self.videoOffset

    def setVideoOffset(self, newVideoOffset):
        self.videoOffset = newVideoOffset

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getScaleWidth(self):
        return self.scaleWidth

    def setScaleWidth(self, newScaleWidth):
        self.scaleWidth = newScaleWidth

    def getScaleHeight(self):
        return self.scaleHeight

    def setScaleHeight(self, newScaleHeight):
        self.scaleHeight = newScaleHeight

    def getBackgroundColor(self):
        return self.backgroundColor

    def setBackgroundColor(self, newBackgroundColor):
        self.backgroundColor = newBackgroundColor

    def getSourceParamsId(self):
        return self.sourceParamsId

    def setSourceParamsId(self, newSourceParamsId):
        self.sourceParamsId = newSourceParamsId

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getDensity(self):
        return self.density

    def setDensity(self, newDensity):
        self.density = newDensity


class KalturaThumbAssetListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaThumbAsset
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaThumbAsset), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaThumbParamsBaseFilter(KalturaAssetParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaAssetParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual)

        # @var KalturaContainerFormat
        self.formatEqual = formatEqual


    PROPERTY_LOADERS = {
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsBaseFilter")
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        return kparams

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual


class KalturaThumbParamsFilter(KalturaThumbParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaThumbParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsFilter")
        return kparams


class KalturaThumbParamsListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaThumbParams
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaThumbParams), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUiConf(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            objType=NotImplemented,
            objTypeAsString=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            htmlParams=NotImplemented,
            swfUrl=NotImplemented,
            confFilePath=NotImplemented,
            confFile=NotImplemented,
            confFileFeatures=NotImplemented,
            confVars=NotImplemented,
            useCdn=NotImplemented,
            tags=NotImplemented,
            swfUrlVersion=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            creationMode=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # Name of the uiConf, this is not a primary key
        # @var string
        self.name = name

        # @var string
        self.description = description

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var KalturaUiConfObjType
        self.objType = objType

        # @var string
        # @readonly
        self.objTypeAsString = objTypeAsString

        # @var int
        self.width = width

        # @var int
        self.height = height

        # @var string
        self.htmlParams = htmlParams

        # @var string
        self.swfUrl = swfUrl

        # @var string
        # @readonly
        self.confFilePath = confFilePath

        # @var string
        self.confFile = confFile

        # @var string
        self.confFileFeatures = confFileFeatures

        # @var string
        self.confVars = confVars

        # @var bool
        self.useCdn = useCdn

        # @var string
        self.tags = tags

        # @var string
        self.swfUrlVersion = swfUrlVersion

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var KalturaUiConfCreationMode
        self.creationMode = creationMode


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'objType': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'objTypeAsString': getXmlNodeText, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'htmlParams': getXmlNodeText, 
        'swfUrl': getXmlNodeText, 
        'confFilePath': getXmlNodeText, 
        'confFile': getXmlNodeText, 
        'confFileFeatures': getXmlNodeText, 
        'confVars': getXmlNodeText, 
        'useCdn': getXmlNodeBool, 
        'tags': getXmlNodeText, 
        'swfUrlVersion': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'creationMode': (KalturaEnumsFactory.createInt, "KalturaUiConfCreationMode"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConf.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConf")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("objType", self.objType)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        kparams.addStringIfDefined("htmlParams", self.htmlParams)
        kparams.addStringIfDefined("swfUrl", self.swfUrl)
        kparams.addStringIfDefined("confFile", self.confFile)
        kparams.addStringIfDefined("confFileFeatures", self.confFileFeatures)
        kparams.addStringIfDefined("confVars", self.confVars)
        kparams.addBoolIfDefined("useCdn", self.useCdn)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("swfUrlVersion", self.swfUrlVersion)
        kparams.addIntEnumIfDefined("creationMode", self.creationMode)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getPartnerId(self):
        return self.partnerId

    def getObjType(self):
        return self.objType

    def setObjType(self, newObjType):
        self.objType = newObjType

    def getObjTypeAsString(self):
        return self.objTypeAsString

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getHtmlParams(self):
        return self.htmlParams

    def setHtmlParams(self, newHtmlParams):
        self.htmlParams = newHtmlParams

    def getSwfUrl(self):
        return self.swfUrl

    def setSwfUrl(self, newSwfUrl):
        self.swfUrl = newSwfUrl

    def getConfFilePath(self):
        return self.confFilePath

    def getConfFile(self):
        return self.confFile

    def setConfFile(self, newConfFile):
        self.confFile = newConfFile

    def getConfFileFeatures(self):
        return self.confFileFeatures

    def setConfFileFeatures(self, newConfFileFeatures):
        self.confFileFeatures = newConfFileFeatures

    def getConfVars(self):
        return self.confVars

    def setConfVars(self, newConfVars):
        self.confVars = newConfVars

    def getUseCdn(self):
        return self.useCdn

    def setUseCdn(self, newUseCdn):
        self.useCdn = newUseCdn

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getSwfUrlVersion(self):
        return self.swfUrlVersion

    def setSwfUrlVersion(self, newSwfUrlVersion):
        self.swfUrlVersion = newSwfUrlVersion

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getCreationMode(self):
        return self.creationMode

    def setCreationMode(self, newCreationMode):
        self.creationMode = newCreationMode


class KalturaUiConfBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            objTypeEqual=NotImplemented,
            objTypeIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            creationModeEqual=NotImplemented,
            creationModeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.nameLike = nameLike

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var KalturaUiConfObjType
        self.objTypeEqual = objTypeEqual

        # @var string
        self.objTypeIn = objTypeIn

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaUiConfCreationMode
        self.creationModeEqual = creationModeEqual

        # @var string
        self.creationModeIn = creationModeIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'objTypeEqual': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'objTypeIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'creationModeEqual': (KalturaEnumsFactory.createInt, "KalturaUiConfCreationMode"), 
        'creationModeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("nameLike", self.nameLike)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addIntEnumIfDefined("objTypeEqual", self.objTypeEqual)
        kparams.addStringIfDefined("objTypeIn", self.objTypeIn)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfDefined("creationModeEqual", self.creationModeEqual)
        kparams.addStringIfDefined("creationModeIn", self.creationModeIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getObjTypeEqual(self):
        return self.objTypeEqual

    def setObjTypeEqual(self, newObjTypeEqual):
        self.objTypeEqual = newObjTypeEqual

    def getObjTypeIn(self):
        return self.objTypeIn

    def setObjTypeIn(self, newObjTypeIn):
        self.objTypeIn = newObjTypeIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

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

    def getCreationModeEqual(self):
        return self.creationModeEqual

    def setCreationModeEqual(self, newCreationModeEqual):
        self.creationModeEqual = newCreationModeEqual

    def getCreationModeIn(self):
        return self.creationModeIn

    def setCreationModeIn(self, newCreationModeIn):
        self.creationModeIn = newCreationModeIn


class KalturaUiConfFilter(KalturaUiConfBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            objTypeEqual=NotImplemented,
            objTypeIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            creationModeEqual=NotImplemented,
            creationModeIn=NotImplemented):
        KalturaUiConfBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            nameLike,
            partnerIdEqual,
            partnerIdIn,
            objTypeEqual,
            objTypeIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            creationModeEqual,
            creationModeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUiConfBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConfBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfFilter")
        return kparams


class KalturaUiConfListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUiConf
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUiConf), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUiConfTypeInfo(KalturaObjectBase):
    """Info about uiconf type"""

    def __init__(self,
            type=NotImplemented,
            versions=NotImplemented,
            directory=NotImplemented,
            filename=NotImplemented):
        KalturaObjectBase.__init__(self)

        # UiConf Type
        # @var KalturaUiConfObjType
        self.type = type

        # Available versions
        # @var array of KalturaString
        self.versions = versions

        # The direcotry this type is saved at
        # @var string
        self.directory = directory

        # Filename for this UiConf type
        # @var string
        self.filename = filename


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'versions': (KalturaObjectFactory.createArray, KalturaString), 
        'directory': getXmlNodeText, 
        'filename': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfTypeInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfTypeInfo")
        kparams.addIntEnumIfDefined("type", self.type)
        kparams.addArrayIfDefined("versions", self.versions)
        kparams.addStringIfDefined("directory", self.directory)
        kparams.addStringIfDefined("filename", self.filename)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getVersions(self):
        return self.versions

    def setVersions(self, newVersions):
        self.versions = newVersions

    def getDirectory(self):
        return self.directory

    def setDirectory(self, newDirectory):
        self.directory = newDirectory

    def getFilename(self):
        return self.filename

    def setFilename(self, newFilename):
        self.filename = newFilename


class KalturaUploadResponse(KalturaObjectBase):
    def __init__(self,
            uploadTokenId=NotImplemented,
            fileSize=NotImplemented,
            errorCode=NotImplemented,
            errorDescription=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.uploadTokenId = uploadTokenId

        # @var int
        self.fileSize = fileSize

        # @var KalturaUploadErrorCode
        self.errorCode = errorCode

        # @var string
        self.errorDescription = errorDescription


    PROPERTY_LOADERS = {
        'uploadTokenId': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'errorCode': (KalturaEnumsFactory.createInt, "KalturaUploadErrorCode"), 
        'errorDescription': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadResponse")
        kparams.addStringIfDefined("uploadTokenId", self.uploadTokenId)
        kparams.addIntIfDefined("fileSize", self.fileSize)
        kparams.addIntEnumIfDefined("errorCode", self.errorCode)
        kparams.addStringIfDefined("errorDescription", self.errorDescription)
        return kparams

    def getUploadTokenId(self):
        return self.uploadTokenId

    def setUploadTokenId(self, newUploadTokenId):
        self.uploadTokenId = newUploadTokenId

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, newErrorCode):
        self.errorCode = newErrorCode

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, newErrorDescription):
        self.errorDescription = newErrorDescription


class KalturaUploadToken(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            status=NotImplemented,
            fileName=NotImplemented,
            fileSize=NotImplemented,
            uploadedFileSize=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Upload token unique ID
        # @var string
        # @readonly
        self.id = id

        # Partner ID of the upload token
        # @var int
        # @readonly
        self.partnerId = partnerId

        # User id for the upload token
        # @var string
        # @readonly
        self.userId = userId

        # Status of the upload token
        # @var KalturaUploadTokenStatus
        # @readonly
        self.status = status

        # Name of the file for the upload token, can be empty when the upload token is created and will be updated internally after the file is uploaded
        # @var string
        # @insertonly
        self.fileName = fileName

        # File size in bytes, can be empty when the upload token is created and will be updated internally after the file is uploaded
        # @var float
        # @insertonly
        self.fileSize = fileSize

        # Uploaded file size in bytes, can be used to identify how many bytes were uploaded before resuming
        # @var float
        # @readonly
        self.uploadedFileSize = uploadedFileSize

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaUploadTokenStatus"), 
        'fileName': getXmlNodeText, 
        'fileSize': getXmlNodeFloat, 
        'uploadedFileSize': getXmlNodeFloat, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadToken.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadToken")
        kparams.addStringIfDefined("fileName", self.fileName)
        kparams.addFloatIfDefined("fileSize", self.fileSize)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def getStatus(self):
        return self.status

    def getFileName(self):
        return self.fileName

    def setFileName(self, newFileName):
        self.fileName = newFileName

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getUploadedFileSize(self):
        return self.uploadedFileSize

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaUploadTokenBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            userIdEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.userIdEqual = userIdEqual

        # @var KalturaUploadTokenStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUploadTokenStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenBaseFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaUploadTokenFilter(KalturaUploadTokenBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            userIdEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaUploadTokenBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            userIdEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUploadTokenBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUploadTokenBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenFilter")
        return kparams


class KalturaUploadTokenListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUploadToken
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUploadToken), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUserRole(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            status=NotImplemented,
            partnerId=NotImplemented,
            permissionNames=NotImplemented,
            tags=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.name = name

        # @var string
        self.description = description

        # @var KalturaUserRoleStatus
        self.status = status

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.permissionNames = permissionNames

        # @var string
        self.tags = tags

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaUserRoleStatus"), 
        'partnerId': getXmlNodeInt, 
        'permissionNames': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRole.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRole")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("permissionNames", self.permissionNames)
        kparams.addStringIfDefined("tags", self.tags)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getPartnerId(self):
        return self.partnerId

    def getPermissionNames(self):
        return self.permissionNames

    def setPermissionNames(self, newPermissionNames):
        self.permissionNames = newPermissionNames

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaUserRoleBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            descriptionLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.nameIn = nameIn

        # @var string
        self.descriptionLike = descriptionLike

        # @var KalturaUserRoleStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'nameIn': getXmlNodeText, 
        'descriptionLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUserRoleStatus"), 
        'statusIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("nameIn", self.nameIn)
        kparams.addStringIfDefined("descriptionLike", self.descriptionLike)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameIn(self):
        return self.nameIn

    def setNameIn(self, newNameIn):
        self.nameIn = newNameIn

    def getDescriptionLike(self):
        return self.descriptionLike

    def setDescriptionLike(self, newDescriptionLike):
        self.descriptionLike = newDescriptionLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

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


class KalturaUserRoleFilter(KalturaUserRoleBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            descriptionLike=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaUserRoleBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            nameEqual,
            nameIn,
            descriptionLike,
            statusEqual,
            statusIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserRoleBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserRoleBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleFilter")
        return kparams


class KalturaUserRoleListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUserRole
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUserRole), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRoleListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUserBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            screenNameLike=NotImplemented,
            screenNameStartsWith=NotImplemented,
            emailLike=NotImplemented,
            emailStartsWith=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            isAdminEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.screenNameLike = screenNameLike

        # @var string
        self.screenNameStartsWith = screenNameStartsWith

        # @var string
        self.emailLike = emailLike

        # @var string
        self.emailStartsWith = emailStartsWith

        # @var string
        self.tagsMultiLikeOr = tagsMultiLikeOr

        # @var string
        self.tagsMultiLikeAnd = tagsMultiLikeAnd

        # @var KalturaUserStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var bool
        self.isAdminEqual = isAdminEqual


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'screenNameLike': getXmlNodeText, 
        'screenNameStartsWith': getXmlNodeText, 
        'emailLike': getXmlNodeText, 
        'emailStartsWith': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUserStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'isAdminEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserBaseFilter")
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("screenNameLike", self.screenNameLike)
        kparams.addStringIfDefined("screenNameStartsWith", self.screenNameStartsWith)
        kparams.addStringIfDefined("emailLike", self.emailLike)
        kparams.addStringIfDefined("emailStartsWith", self.emailStartsWith)
        kparams.addStringIfDefined("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfDefined("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addBoolIfDefined("isAdminEqual", self.isAdminEqual)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getScreenNameLike(self):
        return self.screenNameLike

    def setScreenNameLike(self, newScreenNameLike):
        self.screenNameLike = newScreenNameLike

    def getScreenNameStartsWith(self):
        return self.screenNameStartsWith

    def setScreenNameStartsWith(self, newScreenNameStartsWith):
        self.screenNameStartsWith = newScreenNameStartsWith

    def getEmailLike(self):
        return self.emailLike

    def setEmailLike(self, newEmailLike):
        self.emailLike = newEmailLike

    def getEmailStartsWith(self):
        return self.emailStartsWith

    def setEmailStartsWith(self, newEmailStartsWith):
        self.emailStartsWith = newEmailStartsWith

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getIsAdminEqual(self):
        return self.isAdminEqual

    def setIsAdminEqual(self, newIsAdminEqual):
        self.isAdminEqual = newIsAdminEqual


class KalturaUserFilter(KalturaUserBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            screenNameLike=NotImplemented,
            screenNameStartsWith=NotImplemented,
            emailLike=NotImplemented,
            emailStartsWith=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            isAdminEqual=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            loginEnabledEqual=NotImplemented):
        KalturaUserBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            screenNameLike,
            screenNameStartsWith,
            emailLike,
            emailStartsWith,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            isAdminEqual)

        # @var string
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var bool
        self.loginEnabledEqual = loginEnabledEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'loginEnabledEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaUserBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addBoolIfDefined("loginEnabledEqual", self.loginEnabledEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getLoginEnabledEqual(self):
        return self.loginEnabledEqual

    def setLoginEnabledEqual(self, newLoginEnabledEqual):
        self.loginEnabledEqual = newLoginEnabledEqual


class KalturaUserListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUser
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUser), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaWidget(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            sourceWidgetId=NotImplemented,
            rootWidgetId=NotImplemented,
            partnerId=NotImplemented,
            entryId=NotImplemented,
            uiConfId=NotImplemented,
            securityType=NotImplemented,
            securityPolicy=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerData=NotImplemented,
            widgetHTML=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = id

        # @var string
        self.sourceWidgetId = sourceWidgetId

        # @var string
        # @readonly
        self.rootWidgetId = rootWidgetId

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var string
        self.entryId = entryId

        # @var int
        self.uiConfId = uiConfId

        # @var KalturaWidgetSecurityType
        self.securityType = securityType

        # @var int
        self.securityPolicy = securityPolicy

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = partnerData

        # @var string
        # @readonly
        self.widgetHTML = widgetHTML


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'sourceWidgetId': getXmlNodeText, 
        'rootWidgetId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'uiConfId': getXmlNodeInt, 
        'securityType': (KalturaEnumsFactory.createInt, "KalturaWidgetSecurityType"), 
        'securityPolicy': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'widgetHTML': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidget.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaWidget")
        kparams.addStringIfDefined("sourceWidgetId", self.sourceWidgetId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addIntIfDefined("uiConfId", self.uiConfId)
        kparams.addIntEnumIfDefined("securityType", self.securityType)
        kparams.addIntIfDefined("securityPolicy", self.securityPolicy)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        return kparams

    def getId(self):
        return self.id

    def getSourceWidgetId(self):
        return self.sourceWidgetId

    def setSourceWidgetId(self, newSourceWidgetId):
        self.sourceWidgetId = newSourceWidgetId

    def getRootWidgetId(self):
        return self.rootWidgetId

    def getPartnerId(self):
        return self.partnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getUiConfId(self):
        return self.uiConfId

    def setUiConfId(self, newUiConfId):
        self.uiConfId = newUiConfId

    def getSecurityType(self):
        return self.securityType

    def setSecurityType(self, newSecurityType):
        self.securityType = newSecurityType

    def getSecurityPolicy(self):
        return self.securityPolicy

    def setSecurityPolicy(self, newSecurityPolicy):
        self.securityPolicy = newSecurityPolicy

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getWidgetHTML(self):
        return self.widgetHTML


class KalturaWidgetBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            sourceWidgetIdEqual=NotImplemented,
            rootWidgetIdEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            uiConfIdEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerDataLike=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.sourceWidgetIdEqual = sourceWidgetIdEqual

        # @var string
        self.rootWidgetIdEqual = rootWidgetIdEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.entryIdEqual = entryIdEqual

        # @var int
        self.uiConfIdEqual = uiConfIdEqual

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var string
        self.partnerDataLike = partnerDataLike


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'sourceWidgetIdEqual': getXmlNodeText, 
        'rootWidgetIdEqual': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'entryIdEqual': getXmlNodeText, 
        'uiConfIdEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'partnerDataLike': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaWidgetBaseFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("sourceWidgetIdEqual", self.sourceWidgetIdEqual)
        kparams.addStringIfDefined("rootWidgetIdEqual", self.rootWidgetIdEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("entryIdEqual", self.entryIdEqual)
        kparams.addIntIfDefined("uiConfIdEqual", self.uiConfIdEqual)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addStringIfDefined("partnerDataLike", self.partnerDataLike)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getSourceWidgetIdEqual(self):
        return self.sourceWidgetIdEqual

    def setSourceWidgetIdEqual(self, newSourceWidgetIdEqual):
        self.sourceWidgetIdEqual = newSourceWidgetIdEqual

    def getRootWidgetIdEqual(self):
        return self.rootWidgetIdEqual

    def setRootWidgetIdEqual(self, newRootWidgetIdEqual):
        self.rootWidgetIdEqual = newRootWidgetIdEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getUiConfIdEqual(self):
        return self.uiConfIdEqual

    def setUiConfIdEqual(self, newUiConfIdEqual):
        self.uiConfIdEqual = newUiConfIdEqual

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

    def getPartnerDataLike(self):
        return self.partnerDataLike

    def setPartnerDataLike(self, newPartnerDataLike):
        self.partnerDataLike = newPartnerDataLike


class KalturaWidgetFilter(KalturaWidgetBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            sourceWidgetIdEqual=NotImplemented,
            rootWidgetIdEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            uiConfIdEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            partnerDataLike=NotImplemented):
        KalturaWidgetBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            sourceWidgetIdEqual,
            rootWidgetIdEqual,
            partnerIdEqual,
            entryIdEqual,
            uiConfIdEqual,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            partnerDataLike)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaWidgetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaWidgetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaWidgetFilter")
        return kparams


class KalturaWidgetListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaWidget
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaWidget), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaWidgetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaPartnerBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerPackageEqual=NotImplemented,
            partnerPackageGreaterThanOrEqual=NotImplemented,
            partnerPackageLessThanOrEqual=NotImplemented,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.nameLike = nameLike

        # @var string
        self.nameMultiLikeOr = nameMultiLikeOr

        # @var string
        self.nameMultiLikeAnd = nameMultiLikeAnd

        # @var string
        self.nameEqual = nameEqual

        # @var KalturaPartnerStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.partnerPackageEqual = partnerPackageEqual

        # @var int
        self.partnerPackageGreaterThanOrEqual = partnerPackageGreaterThanOrEqual

        # @var int
        self.partnerPackageLessThanOrEqual = partnerPackageLessThanOrEqual

        # @var string
        self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike = partnerNameDescriptionWebsiteAdminNameAdminEmailLike


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'nameMultiLikeOr': getXmlNodeText, 
        'nameMultiLikeAnd': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'statusIn': getXmlNodeText, 
        'partnerPackageEqual': getXmlNodeInt, 
        'partnerPackageGreaterThanOrEqual': getXmlNodeInt, 
        'partnerPackageLessThanOrEqual': getXmlNodeInt, 
        'partnerNameDescriptionWebsiteAdminNameAdminEmailLike': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPartnerBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("nameLike", self.nameLike)
        kparams.addStringIfDefined("nameMultiLikeOr", self.nameMultiLikeOr)
        kparams.addStringIfDefined("nameMultiLikeAnd", self.nameMultiLikeAnd)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("partnerPackageEqual", self.partnerPackageEqual)
        kparams.addIntIfDefined("partnerPackageGreaterThanOrEqual", self.partnerPackageGreaterThanOrEqual)
        kparams.addIntIfDefined("partnerPackageLessThanOrEqual", self.partnerPackageLessThanOrEqual)
        kparams.addStringIfDefined("partnerNameDescriptionWebsiteAdminNameAdminEmailLike", self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getNameMultiLikeOr(self):
        return self.nameMultiLikeOr

    def setNameMultiLikeOr(self, newNameMultiLikeOr):
        self.nameMultiLikeOr = newNameMultiLikeOr

    def getNameMultiLikeAnd(self):
        return self.nameMultiLikeAnd

    def setNameMultiLikeAnd(self, newNameMultiLikeAnd):
        self.nameMultiLikeAnd = newNameMultiLikeAnd

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerPackageEqual(self):
        return self.partnerPackageEqual

    def setPartnerPackageEqual(self, newPartnerPackageEqual):
        self.partnerPackageEqual = newPartnerPackageEqual

    def getPartnerPackageGreaterThanOrEqual(self):
        return self.partnerPackageGreaterThanOrEqual

    def setPartnerPackageGreaterThanOrEqual(self, newPartnerPackageGreaterThanOrEqual):
        self.partnerPackageGreaterThanOrEqual = newPartnerPackageGreaterThanOrEqual

    def getPartnerPackageLessThanOrEqual(self):
        return self.partnerPackageLessThanOrEqual

    def setPartnerPackageLessThanOrEqual(self, newPartnerPackageLessThanOrEqual):
        self.partnerPackageLessThanOrEqual = newPartnerPackageLessThanOrEqual

    def getPartnerNameDescriptionWebsiteAdminNameAdminEmailLike(self):
        return self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike

    def setPartnerNameDescriptionWebsiteAdminNameAdminEmailLike(self, newPartnerNameDescriptionWebsiteAdminNameAdminEmailLike):
        self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike = newPartnerNameDescriptionWebsiteAdminNameAdminEmailLike


class KalturaPartnerFilter(KalturaPartnerBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerPackageEqual=NotImplemented,
            partnerPackageGreaterThanOrEqual=NotImplemented,
            partnerPackageLessThanOrEqual=NotImplemented,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike=NotImplemented):
        KalturaPartnerBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            statusEqual,
            statusIn,
            partnerPackageEqual,
            partnerPackageGreaterThanOrEqual,
            partnerPackageLessThanOrEqual,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPartnerBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPartnerFilter")
        return kparams


class KalturaPartnerListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPartner
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPartner), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUserLoginDataBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            loginEmailEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.loginEmailEqual = loginEmailEqual


    PROPERTY_LOADERS = {
        'loginEmailEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserLoginDataBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserLoginDataBaseFilter")
        kparams.addStringIfDefined("loginEmailEqual", self.loginEmailEqual)
        return kparams

    def getLoginEmailEqual(self):
        return self.loginEmailEqual

    def setLoginEmailEqual(self, newLoginEmailEqual):
        self.loginEmailEqual = newLoginEmailEqual


class KalturaUserLoginDataFilter(KalturaUserLoginDataBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            loginEmailEqual=NotImplemented):
        KalturaUserLoginDataBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            loginEmailEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserLoginDataBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserLoginDataFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserLoginDataBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserLoginDataFilter")
        return kparams


class KalturaUserLoginData(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            loginEmail=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.id = id

        # @var string
        self.loginEmail = loginEmail


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'loginEmail': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserLoginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserLoginData")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("loginEmail", self.loginEmail)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getLoginEmail(self):
        return self.loginEmail

    def setLoginEmail(self, newLoginEmail):
        self.loginEmail = newLoginEmail


class KalturaUserLoginDataListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUserLoginData
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUserLoginData), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserLoginDataListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserLoginDataListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaFlavorParamsOutputBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)

        # @var int
        self.flavorParamsIdEqual = flavorParamsIdEqual

        # @var string
        self.flavorParamsVersionEqual = flavorParamsVersionEqual

        # @var string
        self.flavorAssetIdEqual = flavorAssetIdEqual

        # @var string
        self.flavorAssetVersionEqual = flavorAssetVersionEqual


    PROPERTY_LOADERS = {
        'flavorParamsIdEqual': getXmlNodeInt, 
        'flavorParamsVersionEqual': getXmlNodeText, 
        'flavorAssetIdEqual': getXmlNodeText, 
        'flavorAssetVersionEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutputBaseFilter")
        kparams.addIntIfDefined("flavorParamsIdEqual", self.flavorParamsIdEqual)
        kparams.addStringIfDefined("flavorParamsVersionEqual", self.flavorParamsVersionEqual)
        kparams.addStringIfDefined("flavorAssetIdEqual", self.flavorAssetIdEqual)
        kparams.addStringIfDefined("flavorAssetVersionEqual", self.flavorAssetVersionEqual)
        return kparams

    def getFlavorParamsIdEqual(self):
        return self.flavorParamsIdEqual

    def setFlavorParamsIdEqual(self, newFlavorParamsIdEqual):
        self.flavorParamsIdEqual = newFlavorParamsIdEqual

    def getFlavorParamsVersionEqual(self):
        return self.flavorParamsVersionEqual

    def setFlavorParamsVersionEqual(self, newFlavorParamsVersionEqual):
        self.flavorParamsVersionEqual = newFlavorParamsVersionEqual

    def getFlavorAssetIdEqual(self):
        return self.flavorAssetIdEqual

    def setFlavorAssetIdEqual(self, newFlavorAssetIdEqual):
        self.flavorAssetIdEqual = newFlavorAssetIdEqual

    def getFlavorAssetVersionEqual(self):
        return self.flavorAssetVersionEqual

    def setFlavorAssetVersionEqual(self, newFlavorAssetVersionEqual):
        self.flavorAssetVersionEqual = newFlavorAssetVersionEqual


class KalturaFlavorParamsOutputFilter(KalturaFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutputFilter")
        return kparams


class KalturaFlavorParamsOutput(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance)

        # @var int
        self.flavorParamsId = flavorParamsId

        # @var string
        self.commandLinesStr = commandLinesStr

        # @var string
        self.flavorParamsVersion = flavorParamsVersion

        # @var string
        self.flavorAssetId = flavorAssetId

        # @var string
        self.flavorAssetVersion = flavorAssetVersion

        # @var int
        self.readyBehavior = readyBehavior


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'commandLinesStr': getXmlNodeText, 
        'flavorParamsVersion': getXmlNodeText, 
        'flavorAssetId': getXmlNodeText, 
        'flavorAssetVersion': getXmlNodeText, 
        'readyBehavior': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutput")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        kparams.addStringIfDefined("commandLinesStr", self.commandLinesStr)
        kparams.addStringIfDefined("flavorParamsVersion", self.flavorParamsVersion)
        kparams.addStringIfDefined("flavorAssetId", self.flavorAssetId)
        kparams.addStringIfDefined("flavorAssetVersion", self.flavorAssetVersion)
        kparams.addIntIfDefined("readyBehavior", self.readyBehavior)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getCommandLinesStr(self):
        return self.commandLinesStr

    def setCommandLinesStr(self, newCommandLinesStr):
        self.commandLinesStr = newCommandLinesStr

    def getFlavorParamsVersion(self):
        return self.flavorParamsVersion

    def setFlavorParamsVersion(self, newFlavorParamsVersion):
        self.flavorParamsVersion = newFlavorParamsVersion

    def getFlavorAssetId(self):
        return self.flavorAssetId

    def setFlavorAssetId(self, newFlavorAssetId):
        self.flavorAssetId = newFlavorAssetId

    def getFlavorAssetVersion(self):
        return self.flavorAssetVersion

    def setFlavorAssetVersion(self, newFlavorAssetVersion):
        self.flavorAssetVersion = newFlavorAssetVersion

    def getReadyBehavior(self):
        return self.readyBehavior

    def setReadyBehavior(self, newReadyBehavior):
        self.readyBehavior = newReadyBehavior


class KalturaThumbParamsOutputBaseFilter(KalturaThumbParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            thumbParamsIdEqual=NotImplemented,
            thumbParamsVersionEqual=NotImplemented,
            thumbAssetIdEqual=NotImplemented,
            thumbAssetVersionEqual=NotImplemented):
        KalturaThumbParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)

        # @var int
        self.thumbParamsIdEqual = thumbParamsIdEqual

        # @var string
        self.thumbParamsVersionEqual = thumbParamsVersionEqual

        # @var string
        self.thumbAssetIdEqual = thumbAssetIdEqual

        # @var string
        self.thumbAssetVersionEqual = thumbAssetVersionEqual


    PROPERTY_LOADERS = {
        'thumbParamsIdEqual': getXmlNodeInt, 
        'thumbParamsVersionEqual': getXmlNodeText, 
        'thumbAssetIdEqual': getXmlNodeText, 
        'thumbAssetVersionEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaThumbParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutputBaseFilter")
        kparams.addIntIfDefined("thumbParamsIdEqual", self.thumbParamsIdEqual)
        kparams.addStringIfDefined("thumbParamsVersionEqual", self.thumbParamsVersionEqual)
        kparams.addStringIfDefined("thumbAssetIdEqual", self.thumbAssetIdEqual)
        kparams.addStringIfDefined("thumbAssetVersionEqual", self.thumbAssetVersionEqual)
        return kparams

    def getThumbParamsIdEqual(self):
        return self.thumbParamsIdEqual

    def setThumbParamsIdEqual(self, newThumbParamsIdEqual):
        self.thumbParamsIdEqual = newThumbParamsIdEqual

    def getThumbParamsVersionEqual(self):
        return self.thumbParamsVersionEqual

    def setThumbParamsVersionEqual(self, newThumbParamsVersionEqual):
        self.thumbParamsVersionEqual = newThumbParamsVersionEqual

    def getThumbAssetIdEqual(self):
        return self.thumbAssetIdEqual

    def setThumbAssetIdEqual(self, newThumbAssetIdEqual):
        self.thumbAssetIdEqual = newThumbAssetIdEqual

    def getThumbAssetVersionEqual(self):
        return self.thumbAssetVersionEqual

    def setThumbAssetVersionEqual(self, newThumbAssetVersionEqual):
        self.thumbAssetVersionEqual = newThumbAssetVersionEqual


class KalturaThumbParamsOutputFilter(KalturaThumbParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            thumbParamsIdEqual=NotImplemented,
            thumbParamsVersionEqual=NotImplemented,
            thumbAssetIdEqual=NotImplemented,
            thumbAssetVersionEqual=NotImplemented):
        KalturaThumbParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            thumbParamsIdEqual,
            thumbParamsVersionEqual,
            thumbAssetIdEqual,
            thumbAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutputFilter")
        return kparams


class KalturaThumbParamsOutput(KalturaThumbParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            cropType=NotImplemented,
            quality=NotImplemented,
            cropX=NotImplemented,
            cropY=NotImplemented,
            cropWidth=NotImplemented,
            cropHeight=NotImplemented,
            videoOffset=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            scaleWidth=NotImplemented,
            scaleHeight=NotImplemented,
            backgroundColor=NotImplemented,
            sourceParamsId=NotImplemented,
            format=NotImplemented,
            density=NotImplemented,
            thumbParamsId=NotImplemented,
            thumbParamsVersion=NotImplemented,
            thumbAssetId=NotImplemented,
            thumbAssetVersion=NotImplemented):
        KalturaThumbParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            cropType,
            quality,
            cropX,
            cropY,
            cropWidth,
            cropHeight,
            videoOffset,
            width,
            height,
            scaleWidth,
            scaleHeight,
            backgroundColor,
            sourceParamsId,
            format,
            density)

        # @var int
        self.thumbParamsId = thumbParamsId

        # @var string
        self.thumbParamsVersion = thumbParamsVersion

        # @var string
        self.thumbAssetId = thumbAssetId

        # @var string
        self.thumbAssetVersion = thumbAssetVersion


    PROPERTY_LOADERS = {
        'thumbParamsId': getXmlNodeInt, 
        'thumbParamsVersion': getXmlNodeText, 
        'thumbAssetId': getXmlNodeText, 
        'thumbAssetVersion': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaThumbParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParams.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutput")
        kparams.addIntIfDefined("thumbParamsId", self.thumbParamsId)
        kparams.addStringIfDefined("thumbParamsVersion", self.thumbParamsVersion)
        kparams.addStringIfDefined("thumbAssetId", self.thumbAssetId)
        kparams.addStringIfDefined("thumbAssetVersion", self.thumbAssetVersion)
        return kparams

    def getThumbParamsId(self):
        return self.thumbParamsId

    def setThumbParamsId(self, newThumbParamsId):
        self.thumbParamsId = newThumbParamsId

    def getThumbParamsVersion(self):
        return self.thumbParamsVersion

    def setThumbParamsVersion(self, newThumbParamsVersion):
        self.thumbParamsVersion = newThumbParamsVersion

    def getThumbAssetId(self):
        return self.thumbAssetId

    def setThumbAssetId(self, newThumbAssetId):
        self.thumbAssetId = newThumbAssetId

    def getThumbAssetVersion(self):
        return self.thumbAssetVersion

    def setThumbAssetVersion(self, newThumbAssetVersion):
        self.thumbAssetVersion = newThumbAssetVersion


class KalturaReport(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            query=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Report id
        # @var int
        # @readonly
        self.id = id

        # Partner id associated with the report
        # @var int
        self.partnerId = partnerId

        # Report name
        # @var string
        self.name = name

        # Used to identify system reports in a friendly way
        # @var string
        self.systemName = systemName

        # Report description
        # @var string
        self.description = description

        # Report query
        # @var string
        self.query = query

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'query': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReport.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReport")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("query", self.query)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getQuery(self):
        return self.query

    def setQuery(self, newQuery):
        self.query = newQuery

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaReportBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaReportBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn


class KalturaReportFilter(KalturaReportBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented):
        KalturaReportBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            systemNameEqual,
            systemNameIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaReportBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReportBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaReportFilter")
        return kparams


class KalturaReportListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaReport
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaReport), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaCountryRestriction(KalturaBaseRestriction):
    def __init__(self,
            countryRestrictionType=NotImplemented,
            countryList=NotImplemented):
        KalturaBaseRestriction.__init__(self)

        # Country restriction type (Allow or deny)
        # @var KalturaCountryRestrictionType
        self.countryRestrictionType = countryRestrictionType

        # Comma separated list of country codes to allow to deny
        # @var string
        self.countryList = countryList


    PROPERTY_LOADERS = {
        'countryRestrictionType': (KalturaEnumsFactory.createInt, "KalturaCountryRestrictionType"), 
        'countryList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountryRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaCountryRestriction")
        kparams.addIntEnumIfDefined("countryRestrictionType", self.countryRestrictionType)
        kparams.addStringIfDefined("countryList", self.countryList)
        return kparams

    def getCountryRestrictionType(self):
        return self.countryRestrictionType

    def setCountryRestrictionType(self, newCountryRestrictionType):
        self.countryRestrictionType = newCountryRestrictionType

    def getCountryList(self):
        return self.countryList

    def setCountryList(self, newCountryList):
        self.countryList = newCountryList


class KalturaDirectoryRestriction(KalturaBaseRestriction):
    def __init__(self,
            directoryRestrictionType=NotImplemented):
        KalturaBaseRestriction.__init__(self)

        # Kaltura directory restriction type
        # @var KalturaDirectoryRestrictionType
        self.directoryRestrictionType = directoryRestrictionType


    PROPERTY_LOADERS = {
        'directoryRestrictionType': (KalturaEnumsFactory.createInt, "KalturaDirectoryRestrictionType"), 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDirectoryRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaDirectoryRestriction")
        kparams.addIntEnumIfDefined("directoryRestrictionType", self.directoryRestrictionType)
        return kparams

    def getDirectoryRestrictionType(self):
        return self.directoryRestrictionType

    def setDirectoryRestrictionType(self, newDirectoryRestrictionType):
        self.directoryRestrictionType = newDirectoryRestrictionType


class KalturaIpAddressRestriction(KalturaBaseRestriction):
    def __init__(self,
            ipAddressRestrictionType=NotImplemented,
            ipAddressList=NotImplemented):
        KalturaBaseRestriction.__init__(self)

        # Ip address restriction type (Allow or deny)
        # @var KalturaIpAddressRestrictionType
        self.ipAddressRestrictionType = ipAddressRestrictionType

        # Comma separated list of ip address to allow to deny
        # @var string
        self.ipAddressList = ipAddressList


    PROPERTY_LOADERS = {
        'ipAddressRestrictionType': (KalturaEnumsFactory.createInt, "KalturaIpAddressRestrictionType"), 
        'ipAddressList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIpAddressRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaIpAddressRestriction")
        kparams.addIntEnumIfDefined("ipAddressRestrictionType", self.ipAddressRestrictionType)
        kparams.addStringIfDefined("ipAddressList", self.ipAddressList)
        return kparams

    def getIpAddressRestrictionType(self):
        return self.ipAddressRestrictionType

    def setIpAddressRestrictionType(self, newIpAddressRestrictionType):
        self.ipAddressRestrictionType = newIpAddressRestrictionType

    def getIpAddressList(self):
        return self.ipAddressList

    def setIpAddressList(self, newIpAddressList):
        self.ipAddressList = newIpAddressList


class KalturaSessionRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaSessionRestriction")
        return kparams


class KalturaPreviewRestriction(KalturaSessionRestriction):
    def __init__(self,
            previewLength=NotImplemented):
        KalturaSessionRestriction.__init__(self)

        # The preview restriction length
        # @var int
        self.previewLength = previewLength


    PROPERTY_LOADERS = {
        'previewLength': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSessionRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPreviewRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSessionRestriction.toParams(self)
        kparams.put("objectType", "KalturaPreviewRestriction")
        kparams.addIntIfDefined("previewLength", self.previewLength)
        return kparams

    def getPreviewLength(self):
        return self.previewLength

    def setPreviewLength(self, newPreviewLength):
        self.previewLength = newPreviewLength


class KalturaSiteRestriction(KalturaBaseRestriction):
    def __init__(self,
            siteRestrictionType=NotImplemented,
            siteList=NotImplemented):
        KalturaBaseRestriction.__init__(self)

        # The site restriction type (allow or deny)
        # @var KalturaSiteRestrictionType
        self.siteRestrictionType = siteRestrictionType

        # Comma separated list of sites (domains) to allow or deny
        # @var string
        self.siteList = siteList


    PROPERTY_LOADERS = {
        'siteRestrictionType': (KalturaEnumsFactory.createInt, "KalturaSiteRestrictionType"), 
        'siteList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSiteRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaSiteRestriction")
        kparams.addIntEnumIfDefined("siteRestrictionType", self.siteRestrictionType)
        kparams.addStringIfDefined("siteList", self.siteList)
        return kparams

    def getSiteRestrictionType(self):
        return self.siteRestrictionType

    def setSiteRestrictionType(self, newSiteRestrictionType):
        self.siteRestrictionType = newSiteRestrictionType

    def getSiteList(self):
        return self.siteList

    def setSiteList(self, newSiteList):
        self.siteList = newSiteList


class KalturaUserAgentRestriction(KalturaBaseRestriction):
    def __init__(self,
            userAgentRestrictionType=NotImplemented,
            userAgentRegexList=NotImplemented):
        KalturaBaseRestriction.__init__(self)

        # User agent restriction type (Allow or deny)
        # @var KalturaUserAgentRestrictionType
        self.userAgentRestrictionType = userAgentRestrictionType

        # A comma seperated list of user agent regular expressions
        # @var string
        self.userAgentRegexList = userAgentRegexList


    PROPERTY_LOADERS = {
        'userAgentRestrictionType': (KalturaEnumsFactory.createInt, "KalturaUserAgentRestrictionType"), 
        'userAgentRegexList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAgentRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaUserAgentRestriction")
        kparams.addIntEnumIfDefined("userAgentRestrictionType", self.userAgentRestrictionType)
        kparams.addStringIfDefined("userAgentRegexList", self.userAgentRegexList)
        return kparams

    def getUserAgentRestrictionType(self):
        return self.userAgentRestrictionType

    def setUserAgentRestrictionType(self, newUserAgentRestrictionType):
        self.userAgentRestrictionType = newUserAgentRestrictionType

    def getUserAgentRegexList(self):
        return self.userAgentRegexList

    def setUserAgentRegexList(self, newUserAgentRegexList):
        self.userAgentRegexList = newUserAgentRegexList


class KalturaSearchCondition(KalturaSearchItem):
    def __init__(self,
            field=NotImplemented,
            value=NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var string
        self.field = field

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'field': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaSearchCondition")
        kparams.addStringIfDefined("field", self.field)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getField(self):
        return self.field

    def setField(self, newField):
        self.field = newField

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaSearchComparableCondition(KalturaSearchCondition):
    def __init__(self,
            field=NotImplemented,
            value=NotImplemented,
            comparison=NotImplemented):
        KalturaSearchCondition.__init__(self,
            field,
            value)

        # @var KalturaSearchConditionComparison
        self.comparison = comparison


    PROPERTY_LOADERS = {
        'comparison': (KalturaEnumsFactory.createInt, "KalturaSearchConditionComparison"), 
    }

    def fromXml(self, node):
        KalturaSearchCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchComparableCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchCondition.toParams(self)
        kparams.put("objectType", "KalturaSearchComparableCondition")
        kparams.addIntEnumIfDefined("comparison", self.comparison)
        return kparams

    def getComparison(self):
        return self.comparison

    def setComparison(self, newComparison):
        self.comparison = newComparison


class KalturaSearchOperator(KalturaSearchItem):
    def __init__(self,
            type=NotImplemented,
            items=NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var KalturaSearchOperatorType
        self.type = type

        # @var array of KalturaSearchItem
        self.items = items


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createInt, "KalturaSearchOperatorType"), 
        'items': (KalturaObjectFactory.createArray, KalturaSearchItem), 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaSearchOperator")
        kparams.addIntEnumIfDefined("type", self.type)
        kparams.addArrayIfDefined("items", self.items)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getItems(self):
        return self.items

    def setItems(self, newItems):
        self.items = newItems


class KalturaBaseJobBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var int
        self.idGreaterThanOrEqual = idGreaterThanOrEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.partnerIdNotIn = partnerIdNotIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.processorExpirationGreaterThanOrEqual = processorExpirationGreaterThanOrEqual

        # @var int
        self.processorExpirationLessThanOrEqual = processorExpirationLessThanOrEqual

        # @var int
        self.executionAttemptsGreaterThanOrEqual = executionAttemptsGreaterThanOrEqual

        # @var int
        self.executionAttemptsLessThanOrEqual = executionAttemptsLessThanOrEqual

        # @var int
        self.lockVersionGreaterThanOrEqual = lockVersionGreaterThanOrEqual

        # @var int
        self.lockVersionLessThanOrEqual = lockVersionLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idGreaterThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'partnerIdNotIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'processorExpirationGreaterThanOrEqual': getXmlNodeInt, 
        'processorExpirationLessThanOrEqual': getXmlNodeInt, 
        'executionAttemptsGreaterThanOrEqual': getXmlNodeInt, 
        'executionAttemptsLessThanOrEqual': getXmlNodeInt, 
        'lockVersionGreaterThanOrEqual': getXmlNodeInt, 
        'lockVersionLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseJobBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addIntIfDefined("idGreaterThanOrEqual", self.idGreaterThanOrEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("partnerIdNotIn", self.partnerIdNotIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("processorExpirationGreaterThanOrEqual", self.processorExpirationGreaterThanOrEqual)
        kparams.addIntIfDefined("processorExpirationLessThanOrEqual", self.processorExpirationLessThanOrEqual)
        kparams.addIntIfDefined("executionAttemptsGreaterThanOrEqual", self.executionAttemptsGreaterThanOrEqual)
        kparams.addIntIfDefined("executionAttemptsLessThanOrEqual", self.executionAttemptsLessThanOrEqual)
        kparams.addIntIfDefined("lockVersionGreaterThanOrEqual", self.lockVersionGreaterThanOrEqual)
        kparams.addIntIfDefined("lockVersionLessThanOrEqual", self.lockVersionLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdGreaterThanOrEqual(self):
        return self.idGreaterThanOrEqual

    def setIdGreaterThanOrEqual(self, newIdGreaterThanOrEqual):
        self.idGreaterThanOrEqual = newIdGreaterThanOrEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getPartnerIdNotIn(self):
        return self.partnerIdNotIn

    def setPartnerIdNotIn(self, newPartnerIdNotIn):
        self.partnerIdNotIn = newPartnerIdNotIn

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

    def getProcessorExpirationGreaterThanOrEqual(self):
        return self.processorExpirationGreaterThanOrEqual

    def setProcessorExpirationGreaterThanOrEqual(self, newProcessorExpirationGreaterThanOrEqual):
        self.processorExpirationGreaterThanOrEqual = newProcessorExpirationGreaterThanOrEqual

    def getProcessorExpirationLessThanOrEqual(self):
        return self.processorExpirationLessThanOrEqual

    def setProcessorExpirationLessThanOrEqual(self, newProcessorExpirationLessThanOrEqual):
        self.processorExpirationLessThanOrEqual = newProcessorExpirationLessThanOrEqual

    def getExecutionAttemptsGreaterThanOrEqual(self):
        return self.executionAttemptsGreaterThanOrEqual

    def setExecutionAttemptsGreaterThanOrEqual(self, newExecutionAttemptsGreaterThanOrEqual):
        self.executionAttemptsGreaterThanOrEqual = newExecutionAttemptsGreaterThanOrEqual

    def getExecutionAttemptsLessThanOrEqual(self):
        return self.executionAttemptsLessThanOrEqual

    def setExecutionAttemptsLessThanOrEqual(self, newExecutionAttemptsLessThanOrEqual):
        self.executionAttemptsLessThanOrEqual = newExecutionAttemptsLessThanOrEqual

    def getLockVersionGreaterThanOrEqual(self):
        return self.lockVersionGreaterThanOrEqual

    def setLockVersionGreaterThanOrEqual(self, newLockVersionGreaterThanOrEqual):
        self.lockVersionGreaterThanOrEqual = newLockVersionGreaterThanOrEqual

    def getLockVersionLessThanOrEqual(self):
        return self.lockVersionLessThanOrEqual

    def setLockVersionLessThanOrEqual(self, newLockVersionLessThanOrEqual):
        self.lockVersionLessThanOrEqual = newLockVersionLessThanOrEqual


class KalturaBaseJobFilter(KalturaBaseJobBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaBaseJobBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseJobFilter")
        return kparams


class KalturaBatchJobBaseFilter(KalturaBaseJobFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            jobTypeEqual=NotImplemented,
            jobTypeIn=NotImplemented,
            jobTypeNotIn=NotImplemented,
            jobSubTypeEqual=NotImplemented,
            jobSubTypeIn=NotImplemented,
            jobSubTypeNotIn=NotImplemented,
            onStressDivertToEqual=NotImplemented,
            onStressDivertToIn=NotImplemented,
            onStressDivertToNotIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            abortEqual=NotImplemented,
            checkAgainTimeoutGreaterThanOrEqual=NotImplemented,
            checkAgainTimeoutLessThanOrEqual=NotImplemented,
            progressGreaterThanOrEqual=NotImplemented,
            progressLessThanOrEqual=NotImplemented,
            updatesCountGreaterThanOrEqual=NotImplemented,
            updatesCountLessThanOrEqual=NotImplemented,
            priorityGreaterThanOrEqual=NotImplemented,
            priorityLessThanOrEqual=NotImplemented,
            priorityEqual=NotImplemented,
            priorityIn=NotImplemented,
            priorityNotIn=NotImplemented,
            twinJobIdEqual=NotImplemented,
            twinJobIdIn=NotImplemented,
            twinJobIdNotIn=NotImplemented,
            bulkJobIdEqual=NotImplemented,
            bulkJobIdIn=NotImplemented,
            bulkJobIdNotIn=NotImplemented,
            parentJobIdEqual=NotImplemented,
            parentJobIdIn=NotImplemented,
            parentJobIdNotIn=NotImplemented,
            rootJobIdEqual=NotImplemented,
            rootJobIdIn=NotImplemented,
            rootJobIdNotIn=NotImplemented,
            queueTimeGreaterThanOrEqual=NotImplemented,
            queueTimeLessThanOrEqual=NotImplemented,
            finishTimeGreaterThanOrEqual=NotImplemented,
            finishTimeLessThanOrEqual=NotImplemented,
            errTypeEqual=NotImplemented,
            errTypeIn=NotImplemented,
            errTypeNotIn=NotImplemented,
            errNumberEqual=NotImplemented,
            errNumberIn=NotImplemented,
            errNumberNotIn=NotImplemented,
            fileSizeLessThan=NotImplemented,
            fileSizeGreaterThan=NotImplemented,
            lastWorkerRemoteEqual=NotImplemented,
            schedulerIdEqual=NotImplemented,
            schedulerIdIn=NotImplemented,
            schedulerIdNotIn=NotImplemented,
            workerIdEqual=NotImplemented,
            workerIdIn=NotImplemented,
            workerIdNotIn=NotImplemented,
            batchIndexEqual=NotImplemented,
            batchIndexIn=NotImplemented,
            batchIndexNotIn=NotImplemented,
            lastSchedulerIdEqual=NotImplemented,
            lastSchedulerIdIn=NotImplemented,
            lastSchedulerIdNotIn=NotImplemented,
            lastWorkerIdEqual=NotImplemented,
            lastWorkerIdIn=NotImplemented,
            lastWorkerIdNotIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            dcNotIn=NotImplemented):
        KalturaBaseJobFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)

        # @var string
        self.entryIdEqual = entryIdEqual

        # @var KalturaBatchJobType
        self.jobTypeEqual = jobTypeEqual

        # @var string
        self.jobTypeIn = jobTypeIn

        # @var string
        self.jobTypeNotIn = jobTypeNotIn

        # @var int
        self.jobSubTypeEqual = jobSubTypeEqual

        # @var string
        self.jobSubTypeIn = jobSubTypeIn

        # @var string
        self.jobSubTypeNotIn = jobSubTypeNotIn

        # @var int
        self.onStressDivertToEqual = onStressDivertToEqual

        # @var string
        self.onStressDivertToIn = onStressDivertToIn

        # @var string
        self.onStressDivertToNotIn = onStressDivertToNotIn

        # @var KalturaBatchJobStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.statusNotIn = statusNotIn

        # @var int
        self.abortEqual = abortEqual

        # @var int
        self.checkAgainTimeoutGreaterThanOrEqual = checkAgainTimeoutGreaterThanOrEqual

        # @var int
        self.checkAgainTimeoutLessThanOrEqual = checkAgainTimeoutLessThanOrEqual

        # @var int
        self.progressGreaterThanOrEqual = progressGreaterThanOrEqual

        # @var int
        self.progressLessThanOrEqual = progressLessThanOrEqual

        # @var int
        self.updatesCountGreaterThanOrEqual = updatesCountGreaterThanOrEqual

        # @var int
        self.updatesCountLessThanOrEqual = updatesCountLessThanOrEqual

        # @var int
        self.priorityGreaterThanOrEqual = priorityGreaterThanOrEqual

        # @var int
        self.priorityLessThanOrEqual = priorityLessThanOrEqual

        # @var int
        self.priorityEqual = priorityEqual

        # @var string
        self.priorityIn = priorityIn

        # @var string
        self.priorityNotIn = priorityNotIn

        # @var int
        self.twinJobIdEqual = twinJobIdEqual

        # @var string
        self.twinJobIdIn = twinJobIdIn

        # @var string
        self.twinJobIdNotIn = twinJobIdNotIn

        # @var int
        self.bulkJobIdEqual = bulkJobIdEqual

        # @var string
        self.bulkJobIdIn = bulkJobIdIn

        # @var string
        self.bulkJobIdNotIn = bulkJobIdNotIn

        # @var int
        self.parentJobIdEqual = parentJobIdEqual

        # @var string
        self.parentJobIdIn = parentJobIdIn

        # @var string
        self.parentJobIdNotIn = parentJobIdNotIn

        # @var int
        self.rootJobIdEqual = rootJobIdEqual

        # @var string
        self.rootJobIdIn = rootJobIdIn

        # @var string
        self.rootJobIdNotIn = rootJobIdNotIn

        # @var int
        self.queueTimeGreaterThanOrEqual = queueTimeGreaterThanOrEqual

        # @var int
        self.queueTimeLessThanOrEqual = queueTimeLessThanOrEqual

        # @var int
        self.finishTimeGreaterThanOrEqual = finishTimeGreaterThanOrEqual

        # @var int
        self.finishTimeLessThanOrEqual = finishTimeLessThanOrEqual

        # @var KalturaBatchJobErrorTypes
        self.errTypeEqual = errTypeEqual

        # @var string
        self.errTypeIn = errTypeIn

        # @var string
        self.errTypeNotIn = errTypeNotIn

        # @var int
        self.errNumberEqual = errNumberEqual

        # @var string
        self.errNumberIn = errNumberIn

        # @var string
        self.errNumberNotIn = errNumberNotIn

        # @var int
        self.fileSizeLessThan = fileSizeLessThan

        # @var int
        self.fileSizeGreaterThan = fileSizeGreaterThan

        # @var bool
        self.lastWorkerRemoteEqual = lastWorkerRemoteEqual

        # @var int
        self.schedulerIdEqual = schedulerIdEqual

        # @var string
        self.schedulerIdIn = schedulerIdIn

        # @var string
        self.schedulerIdNotIn = schedulerIdNotIn

        # @var int
        self.workerIdEqual = workerIdEqual

        # @var string
        self.workerIdIn = workerIdIn

        # @var string
        self.workerIdNotIn = workerIdNotIn

        # @var int
        self.batchIndexEqual = batchIndexEqual

        # @var string
        self.batchIndexIn = batchIndexIn

        # @var string
        self.batchIndexNotIn = batchIndexNotIn

        # @var int
        self.lastSchedulerIdEqual = lastSchedulerIdEqual

        # @var string
        self.lastSchedulerIdIn = lastSchedulerIdIn

        # @var string
        self.lastSchedulerIdNotIn = lastSchedulerIdNotIn

        # @var int
        self.lastWorkerIdEqual = lastWorkerIdEqual

        # @var string
        self.lastWorkerIdIn = lastWorkerIdIn

        # @var string
        self.lastWorkerIdNotIn = lastWorkerIdNotIn

        # @var int
        self.dcEqual = dcEqual

        # @var string
        self.dcIn = dcIn

        # @var string
        self.dcNotIn = dcNotIn


    PROPERTY_LOADERS = {
        'entryIdEqual': getXmlNodeText, 
        'jobTypeEqual': (KalturaEnumsFactory.createString, "KalturaBatchJobType"), 
        'jobTypeIn': getXmlNodeText, 
        'jobTypeNotIn': getXmlNodeText, 
        'jobSubTypeEqual': getXmlNodeInt, 
        'jobSubTypeIn': getXmlNodeText, 
        'jobSubTypeNotIn': getXmlNodeText, 
        'onStressDivertToEqual': getXmlNodeInt, 
        'onStressDivertToIn': getXmlNodeText, 
        'onStressDivertToNotIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaBatchJobStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
        'abortEqual': getXmlNodeInt, 
        'checkAgainTimeoutGreaterThanOrEqual': getXmlNodeInt, 
        'checkAgainTimeoutLessThanOrEqual': getXmlNodeInt, 
        'progressGreaterThanOrEqual': getXmlNodeInt, 
        'progressLessThanOrEqual': getXmlNodeInt, 
        'updatesCountGreaterThanOrEqual': getXmlNodeInt, 
        'updatesCountLessThanOrEqual': getXmlNodeInt, 
        'priorityGreaterThanOrEqual': getXmlNodeInt, 
        'priorityLessThanOrEqual': getXmlNodeInt, 
        'priorityEqual': getXmlNodeInt, 
        'priorityIn': getXmlNodeText, 
        'priorityNotIn': getXmlNodeText, 
        'twinJobIdEqual': getXmlNodeInt, 
        'twinJobIdIn': getXmlNodeText, 
        'twinJobIdNotIn': getXmlNodeText, 
        'bulkJobIdEqual': getXmlNodeInt, 
        'bulkJobIdIn': getXmlNodeText, 
        'bulkJobIdNotIn': getXmlNodeText, 
        'parentJobIdEqual': getXmlNodeInt, 
        'parentJobIdIn': getXmlNodeText, 
        'parentJobIdNotIn': getXmlNodeText, 
        'rootJobIdEqual': getXmlNodeInt, 
        'rootJobIdIn': getXmlNodeText, 
        'rootJobIdNotIn': getXmlNodeText, 
        'queueTimeGreaterThanOrEqual': getXmlNodeInt, 
        'queueTimeLessThanOrEqual': getXmlNodeInt, 
        'finishTimeGreaterThanOrEqual': getXmlNodeInt, 
        'finishTimeLessThanOrEqual': getXmlNodeInt, 
        'errTypeEqual': (KalturaEnumsFactory.createInt, "KalturaBatchJobErrorTypes"), 
        'errTypeIn': getXmlNodeText, 
        'errTypeNotIn': getXmlNodeText, 
        'errNumberEqual': getXmlNodeInt, 
        'errNumberIn': getXmlNodeText, 
        'errNumberNotIn': getXmlNodeText, 
        'fileSizeLessThan': getXmlNodeInt, 
        'fileSizeGreaterThan': getXmlNodeInt, 
        'lastWorkerRemoteEqual': getXmlNodeBool, 
        'schedulerIdEqual': getXmlNodeInt, 
        'schedulerIdIn': getXmlNodeText, 
        'schedulerIdNotIn': getXmlNodeText, 
        'workerIdEqual': getXmlNodeInt, 
        'workerIdIn': getXmlNodeText, 
        'workerIdNotIn': getXmlNodeText, 
        'batchIndexEqual': getXmlNodeInt, 
        'batchIndexIn': getXmlNodeText, 
        'batchIndexNotIn': getXmlNodeText, 
        'lastSchedulerIdEqual': getXmlNodeInt, 
        'lastSchedulerIdIn': getXmlNodeText, 
        'lastSchedulerIdNotIn': getXmlNodeText, 
        'lastWorkerIdEqual': getXmlNodeInt, 
        'lastWorkerIdIn': getXmlNodeText, 
        'lastWorkerIdNotIn': getXmlNodeText, 
        'dcEqual': getXmlNodeInt, 
        'dcIn': getXmlNodeText, 
        'dcNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobBaseFilter")
        kparams.addStringIfDefined("entryIdEqual", self.entryIdEqual)
        kparams.addStringEnumIfDefined("jobTypeEqual", self.jobTypeEqual)
        kparams.addStringIfDefined("jobTypeIn", self.jobTypeIn)
        kparams.addStringIfDefined("jobTypeNotIn", self.jobTypeNotIn)
        kparams.addIntIfDefined("jobSubTypeEqual", self.jobSubTypeEqual)
        kparams.addStringIfDefined("jobSubTypeIn", self.jobSubTypeIn)
        kparams.addStringIfDefined("jobSubTypeNotIn", self.jobSubTypeNotIn)
        kparams.addIntIfDefined("onStressDivertToEqual", self.onStressDivertToEqual)
        kparams.addStringIfDefined("onStressDivertToIn", self.onStressDivertToIn)
        kparams.addStringIfDefined("onStressDivertToNotIn", self.onStressDivertToNotIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        kparams.addIntIfDefined("abortEqual", self.abortEqual)
        kparams.addIntIfDefined("checkAgainTimeoutGreaterThanOrEqual", self.checkAgainTimeoutGreaterThanOrEqual)
        kparams.addIntIfDefined("checkAgainTimeoutLessThanOrEqual", self.checkAgainTimeoutLessThanOrEqual)
        kparams.addIntIfDefined("progressGreaterThanOrEqual", self.progressGreaterThanOrEqual)
        kparams.addIntIfDefined("progressLessThanOrEqual", self.progressLessThanOrEqual)
        kparams.addIntIfDefined("updatesCountGreaterThanOrEqual", self.updatesCountGreaterThanOrEqual)
        kparams.addIntIfDefined("updatesCountLessThanOrEqual", self.updatesCountLessThanOrEqual)
        kparams.addIntIfDefined("priorityGreaterThanOrEqual", self.priorityGreaterThanOrEqual)
        kparams.addIntIfDefined("priorityLessThanOrEqual", self.priorityLessThanOrEqual)
        kparams.addIntIfDefined("priorityEqual", self.priorityEqual)
        kparams.addStringIfDefined("priorityIn", self.priorityIn)
        kparams.addStringIfDefined("priorityNotIn", self.priorityNotIn)
        kparams.addIntIfDefined("twinJobIdEqual", self.twinJobIdEqual)
        kparams.addStringIfDefined("twinJobIdIn", self.twinJobIdIn)
        kparams.addStringIfDefined("twinJobIdNotIn", self.twinJobIdNotIn)
        kparams.addIntIfDefined("bulkJobIdEqual", self.bulkJobIdEqual)
        kparams.addStringIfDefined("bulkJobIdIn", self.bulkJobIdIn)
        kparams.addStringIfDefined("bulkJobIdNotIn", self.bulkJobIdNotIn)
        kparams.addIntIfDefined("parentJobIdEqual", self.parentJobIdEqual)
        kparams.addStringIfDefined("parentJobIdIn", self.parentJobIdIn)
        kparams.addStringIfDefined("parentJobIdNotIn", self.parentJobIdNotIn)
        kparams.addIntIfDefined("rootJobIdEqual", self.rootJobIdEqual)
        kparams.addStringIfDefined("rootJobIdIn", self.rootJobIdIn)
        kparams.addStringIfDefined("rootJobIdNotIn", self.rootJobIdNotIn)
        kparams.addIntIfDefined("queueTimeGreaterThanOrEqual", self.queueTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("queueTimeLessThanOrEqual", self.queueTimeLessThanOrEqual)
        kparams.addIntIfDefined("finishTimeGreaterThanOrEqual", self.finishTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("finishTimeLessThanOrEqual", self.finishTimeLessThanOrEqual)
        kparams.addIntEnumIfDefined("errTypeEqual", self.errTypeEqual)
        kparams.addStringIfDefined("errTypeIn", self.errTypeIn)
        kparams.addStringIfDefined("errTypeNotIn", self.errTypeNotIn)
        kparams.addIntIfDefined("errNumberEqual", self.errNumberEqual)
        kparams.addStringIfDefined("errNumberIn", self.errNumberIn)
        kparams.addStringIfDefined("errNumberNotIn", self.errNumberNotIn)
        kparams.addIntIfDefined("fileSizeLessThan", self.fileSizeLessThan)
        kparams.addIntIfDefined("fileSizeGreaterThan", self.fileSizeGreaterThan)
        kparams.addBoolIfDefined("lastWorkerRemoteEqual", self.lastWorkerRemoteEqual)
        kparams.addIntIfDefined("schedulerIdEqual", self.schedulerIdEqual)
        kparams.addStringIfDefined("schedulerIdIn", self.schedulerIdIn)
        kparams.addStringIfDefined("schedulerIdNotIn", self.schedulerIdNotIn)
        kparams.addIntIfDefined("workerIdEqual", self.workerIdEqual)
        kparams.addStringIfDefined("workerIdIn", self.workerIdIn)
        kparams.addStringIfDefined("workerIdNotIn", self.workerIdNotIn)
        kparams.addIntIfDefined("batchIndexEqual", self.batchIndexEqual)
        kparams.addStringIfDefined("batchIndexIn", self.batchIndexIn)
        kparams.addStringIfDefined("batchIndexNotIn", self.batchIndexNotIn)
        kparams.addIntIfDefined("lastSchedulerIdEqual", self.lastSchedulerIdEqual)
        kparams.addStringIfDefined("lastSchedulerIdIn", self.lastSchedulerIdIn)
        kparams.addStringIfDefined("lastSchedulerIdNotIn", self.lastSchedulerIdNotIn)
        kparams.addIntIfDefined("lastWorkerIdEqual", self.lastWorkerIdEqual)
        kparams.addStringIfDefined("lastWorkerIdIn", self.lastWorkerIdIn)
        kparams.addStringIfDefined("lastWorkerIdNotIn", self.lastWorkerIdNotIn)
        kparams.addIntIfDefined("dcEqual", self.dcEqual)
        kparams.addStringIfDefined("dcIn", self.dcIn)
        kparams.addStringIfDefined("dcNotIn", self.dcNotIn)
        return kparams

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getJobTypeEqual(self):
        return self.jobTypeEqual

    def setJobTypeEqual(self, newJobTypeEqual):
        self.jobTypeEqual = newJobTypeEqual

    def getJobTypeIn(self):
        return self.jobTypeIn

    def setJobTypeIn(self, newJobTypeIn):
        self.jobTypeIn = newJobTypeIn

    def getJobTypeNotIn(self):
        return self.jobTypeNotIn

    def setJobTypeNotIn(self, newJobTypeNotIn):
        self.jobTypeNotIn = newJobTypeNotIn

    def getJobSubTypeEqual(self):
        return self.jobSubTypeEqual

    def setJobSubTypeEqual(self, newJobSubTypeEqual):
        self.jobSubTypeEqual = newJobSubTypeEqual

    def getJobSubTypeIn(self):
        return self.jobSubTypeIn

    def setJobSubTypeIn(self, newJobSubTypeIn):
        self.jobSubTypeIn = newJobSubTypeIn

    def getJobSubTypeNotIn(self):
        return self.jobSubTypeNotIn

    def setJobSubTypeNotIn(self, newJobSubTypeNotIn):
        self.jobSubTypeNotIn = newJobSubTypeNotIn

    def getOnStressDivertToEqual(self):
        return self.onStressDivertToEqual

    def setOnStressDivertToEqual(self, newOnStressDivertToEqual):
        self.onStressDivertToEqual = newOnStressDivertToEqual

    def getOnStressDivertToIn(self):
        return self.onStressDivertToIn

    def setOnStressDivertToIn(self, newOnStressDivertToIn):
        self.onStressDivertToIn = newOnStressDivertToIn

    def getOnStressDivertToNotIn(self):
        return self.onStressDivertToNotIn

    def setOnStressDivertToNotIn(self, newOnStressDivertToNotIn):
        self.onStressDivertToNotIn = newOnStressDivertToNotIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn

    def getAbortEqual(self):
        return self.abortEqual

    def setAbortEqual(self, newAbortEqual):
        self.abortEqual = newAbortEqual

    def getCheckAgainTimeoutGreaterThanOrEqual(self):
        return self.checkAgainTimeoutGreaterThanOrEqual

    def setCheckAgainTimeoutGreaterThanOrEqual(self, newCheckAgainTimeoutGreaterThanOrEqual):
        self.checkAgainTimeoutGreaterThanOrEqual = newCheckAgainTimeoutGreaterThanOrEqual

    def getCheckAgainTimeoutLessThanOrEqual(self):
        return self.checkAgainTimeoutLessThanOrEqual

    def setCheckAgainTimeoutLessThanOrEqual(self, newCheckAgainTimeoutLessThanOrEqual):
        self.checkAgainTimeoutLessThanOrEqual = newCheckAgainTimeoutLessThanOrEqual

    def getProgressGreaterThanOrEqual(self):
        return self.progressGreaterThanOrEqual

    def setProgressGreaterThanOrEqual(self, newProgressGreaterThanOrEqual):
        self.progressGreaterThanOrEqual = newProgressGreaterThanOrEqual

    def getProgressLessThanOrEqual(self):
        return self.progressLessThanOrEqual

    def setProgressLessThanOrEqual(self, newProgressLessThanOrEqual):
        self.progressLessThanOrEqual = newProgressLessThanOrEqual

    def getUpdatesCountGreaterThanOrEqual(self):
        return self.updatesCountGreaterThanOrEqual

    def setUpdatesCountGreaterThanOrEqual(self, newUpdatesCountGreaterThanOrEqual):
        self.updatesCountGreaterThanOrEqual = newUpdatesCountGreaterThanOrEqual

    def getUpdatesCountLessThanOrEqual(self):
        return self.updatesCountLessThanOrEqual

    def setUpdatesCountLessThanOrEqual(self, newUpdatesCountLessThanOrEqual):
        self.updatesCountLessThanOrEqual = newUpdatesCountLessThanOrEqual

    def getPriorityGreaterThanOrEqual(self):
        return self.priorityGreaterThanOrEqual

    def setPriorityGreaterThanOrEqual(self, newPriorityGreaterThanOrEqual):
        self.priorityGreaterThanOrEqual = newPriorityGreaterThanOrEqual

    def getPriorityLessThanOrEqual(self):
        return self.priorityLessThanOrEqual

    def setPriorityLessThanOrEqual(self, newPriorityLessThanOrEqual):
        self.priorityLessThanOrEqual = newPriorityLessThanOrEqual

    def getPriorityEqual(self):
        return self.priorityEqual

    def setPriorityEqual(self, newPriorityEqual):
        self.priorityEqual = newPriorityEqual

    def getPriorityIn(self):
        return self.priorityIn

    def setPriorityIn(self, newPriorityIn):
        self.priorityIn = newPriorityIn

    def getPriorityNotIn(self):
        return self.priorityNotIn

    def setPriorityNotIn(self, newPriorityNotIn):
        self.priorityNotIn = newPriorityNotIn

    def getTwinJobIdEqual(self):
        return self.twinJobIdEqual

    def setTwinJobIdEqual(self, newTwinJobIdEqual):
        self.twinJobIdEqual = newTwinJobIdEqual

    def getTwinJobIdIn(self):
        return self.twinJobIdIn

    def setTwinJobIdIn(self, newTwinJobIdIn):
        self.twinJobIdIn = newTwinJobIdIn

    def getTwinJobIdNotIn(self):
        return self.twinJobIdNotIn

    def setTwinJobIdNotIn(self, newTwinJobIdNotIn):
        self.twinJobIdNotIn = newTwinJobIdNotIn

    def getBulkJobIdEqual(self):
        return self.bulkJobIdEqual

    def setBulkJobIdEqual(self, newBulkJobIdEqual):
        self.bulkJobIdEqual = newBulkJobIdEqual

    def getBulkJobIdIn(self):
        return self.bulkJobIdIn

    def setBulkJobIdIn(self, newBulkJobIdIn):
        self.bulkJobIdIn = newBulkJobIdIn

    def getBulkJobIdNotIn(self):
        return self.bulkJobIdNotIn

    def setBulkJobIdNotIn(self, newBulkJobIdNotIn):
        self.bulkJobIdNotIn = newBulkJobIdNotIn

    def getParentJobIdEqual(self):
        return self.parentJobIdEqual

    def setParentJobIdEqual(self, newParentJobIdEqual):
        self.parentJobIdEqual = newParentJobIdEqual

    def getParentJobIdIn(self):
        return self.parentJobIdIn

    def setParentJobIdIn(self, newParentJobIdIn):
        self.parentJobIdIn = newParentJobIdIn

    def getParentJobIdNotIn(self):
        return self.parentJobIdNotIn

    def setParentJobIdNotIn(self, newParentJobIdNotIn):
        self.parentJobIdNotIn = newParentJobIdNotIn

    def getRootJobIdEqual(self):
        return self.rootJobIdEqual

    def setRootJobIdEqual(self, newRootJobIdEqual):
        self.rootJobIdEqual = newRootJobIdEqual

    def getRootJobIdIn(self):
        return self.rootJobIdIn

    def setRootJobIdIn(self, newRootJobIdIn):
        self.rootJobIdIn = newRootJobIdIn

    def getRootJobIdNotIn(self):
        return self.rootJobIdNotIn

    def setRootJobIdNotIn(self, newRootJobIdNotIn):
        self.rootJobIdNotIn = newRootJobIdNotIn

    def getQueueTimeGreaterThanOrEqual(self):
        return self.queueTimeGreaterThanOrEqual

    def setQueueTimeGreaterThanOrEqual(self, newQueueTimeGreaterThanOrEqual):
        self.queueTimeGreaterThanOrEqual = newQueueTimeGreaterThanOrEqual

    def getQueueTimeLessThanOrEqual(self):
        return self.queueTimeLessThanOrEqual

    def setQueueTimeLessThanOrEqual(self, newQueueTimeLessThanOrEqual):
        self.queueTimeLessThanOrEqual = newQueueTimeLessThanOrEqual

    def getFinishTimeGreaterThanOrEqual(self):
        return self.finishTimeGreaterThanOrEqual

    def setFinishTimeGreaterThanOrEqual(self, newFinishTimeGreaterThanOrEqual):
        self.finishTimeGreaterThanOrEqual = newFinishTimeGreaterThanOrEqual

    def getFinishTimeLessThanOrEqual(self):
        return self.finishTimeLessThanOrEqual

    def setFinishTimeLessThanOrEqual(self, newFinishTimeLessThanOrEqual):
        self.finishTimeLessThanOrEqual = newFinishTimeLessThanOrEqual

    def getErrTypeEqual(self):
        return self.errTypeEqual

    def setErrTypeEqual(self, newErrTypeEqual):
        self.errTypeEqual = newErrTypeEqual

    def getErrTypeIn(self):
        return self.errTypeIn

    def setErrTypeIn(self, newErrTypeIn):
        self.errTypeIn = newErrTypeIn

    def getErrTypeNotIn(self):
        return self.errTypeNotIn

    def setErrTypeNotIn(self, newErrTypeNotIn):
        self.errTypeNotIn = newErrTypeNotIn

    def getErrNumberEqual(self):
        return self.errNumberEqual

    def setErrNumberEqual(self, newErrNumberEqual):
        self.errNumberEqual = newErrNumberEqual

    def getErrNumberIn(self):
        return self.errNumberIn

    def setErrNumberIn(self, newErrNumberIn):
        self.errNumberIn = newErrNumberIn

    def getErrNumberNotIn(self):
        return self.errNumberNotIn

    def setErrNumberNotIn(self, newErrNumberNotIn):
        self.errNumberNotIn = newErrNumberNotIn

    def getFileSizeLessThan(self):
        return self.fileSizeLessThan

    def setFileSizeLessThan(self, newFileSizeLessThan):
        self.fileSizeLessThan = newFileSizeLessThan

    def getFileSizeGreaterThan(self):
        return self.fileSizeGreaterThan

    def setFileSizeGreaterThan(self, newFileSizeGreaterThan):
        self.fileSizeGreaterThan = newFileSizeGreaterThan

    def getLastWorkerRemoteEqual(self):
        return self.lastWorkerRemoteEqual

    def setLastWorkerRemoteEqual(self, newLastWorkerRemoteEqual):
        self.lastWorkerRemoteEqual = newLastWorkerRemoteEqual

    def getSchedulerIdEqual(self):
        return self.schedulerIdEqual

    def setSchedulerIdEqual(self, newSchedulerIdEqual):
        self.schedulerIdEqual = newSchedulerIdEqual

    def getSchedulerIdIn(self):
        return self.schedulerIdIn

    def setSchedulerIdIn(self, newSchedulerIdIn):
        self.schedulerIdIn = newSchedulerIdIn

    def getSchedulerIdNotIn(self):
        return self.schedulerIdNotIn

    def setSchedulerIdNotIn(self, newSchedulerIdNotIn):
        self.schedulerIdNotIn = newSchedulerIdNotIn

    def getWorkerIdEqual(self):
        return self.workerIdEqual

    def setWorkerIdEqual(self, newWorkerIdEqual):
        self.workerIdEqual = newWorkerIdEqual

    def getWorkerIdIn(self):
        return self.workerIdIn

    def setWorkerIdIn(self, newWorkerIdIn):
        self.workerIdIn = newWorkerIdIn

    def getWorkerIdNotIn(self):
        return self.workerIdNotIn

    def setWorkerIdNotIn(self, newWorkerIdNotIn):
        self.workerIdNotIn = newWorkerIdNotIn

    def getBatchIndexEqual(self):
        return self.batchIndexEqual

    def setBatchIndexEqual(self, newBatchIndexEqual):
        self.batchIndexEqual = newBatchIndexEqual

    def getBatchIndexIn(self):
        return self.batchIndexIn

    def setBatchIndexIn(self, newBatchIndexIn):
        self.batchIndexIn = newBatchIndexIn

    def getBatchIndexNotIn(self):
        return self.batchIndexNotIn

    def setBatchIndexNotIn(self, newBatchIndexNotIn):
        self.batchIndexNotIn = newBatchIndexNotIn

    def getLastSchedulerIdEqual(self):
        return self.lastSchedulerIdEqual

    def setLastSchedulerIdEqual(self, newLastSchedulerIdEqual):
        self.lastSchedulerIdEqual = newLastSchedulerIdEqual

    def getLastSchedulerIdIn(self):
        return self.lastSchedulerIdIn

    def setLastSchedulerIdIn(self, newLastSchedulerIdIn):
        self.lastSchedulerIdIn = newLastSchedulerIdIn

    def getLastSchedulerIdNotIn(self):
        return self.lastSchedulerIdNotIn

    def setLastSchedulerIdNotIn(self, newLastSchedulerIdNotIn):
        self.lastSchedulerIdNotIn = newLastSchedulerIdNotIn

    def getLastWorkerIdEqual(self):
        return self.lastWorkerIdEqual

    def setLastWorkerIdEqual(self, newLastWorkerIdEqual):
        self.lastWorkerIdEqual = newLastWorkerIdEqual

    def getLastWorkerIdIn(self):
        return self.lastWorkerIdIn

    def setLastWorkerIdIn(self, newLastWorkerIdIn):
        self.lastWorkerIdIn = newLastWorkerIdIn

    def getLastWorkerIdNotIn(self):
        return self.lastWorkerIdNotIn

    def setLastWorkerIdNotIn(self, newLastWorkerIdNotIn):
        self.lastWorkerIdNotIn = newLastWorkerIdNotIn

    def getDcEqual(self):
        return self.dcEqual

    def setDcEqual(self, newDcEqual):
        self.dcEqual = newDcEqual

    def getDcIn(self):
        return self.dcIn

    def setDcIn(self, newDcIn):
        self.dcIn = newDcIn

    def getDcNotIn(self):
        return self.dcNotIn

    def setDcNotIn(self, newDcNotIn):
        self.dcNotIn = newDcNotIn


class KalturaControlPanelCommandBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            createdByIdEqual=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            targetTypeEqual=NotImplemented,
            targetTypeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.createdByIdEqual = createdByIdEqual

        # @var KalturaControlPanelCommandType
        self.typeEqual = typeEqual

        # @var string
        self.typeIn = typeIn

        # @var KalturaControlPanelCommandTargetType
        self.targetTypeEqual = targetTypeEqual

        # @var string
        self.targetTypeIn = targetTypeIn

        # @var KalturaControlPanelCommandStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'createdByIdEqual': getXmlNodeInt, 
        'typeEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandType"), 
        'typeIn': getXmlNodeText, 
        'targetTypeEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandTargetType"), 
        'targetTypeIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaControlPanelCommandBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaControlPanelCommandBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("createdByIdEqual", self.createdByIdEqual)
        kparams.addIntEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntEnumIfDefined("targetTypeEqual", self.targetTypeEqual)
        kparams.addStringIfDefined("targetTypeIn", self.targetTypeIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
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

    def getCreatedByIdEqual(self):
        return self.createdByIdEqual

    def setCreatedByIdEqual(self, newCreatedByIdEqual):
        self.createdByIdEqual = newCreatedByIdEqual

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getTargetTypeEqual(self):
        return self.targetTypeEqual

    def setTargetTypeEqual(self, newTargetTypeEqual):
        self.targetTypeEqual = newTargetTypeEqual

    def getTargetTypeIn(self):
        return self.targetTypeIn

    def setTargetTypeIn(self, newTargetTypeIn):
        self.targetTypeIn = newTargetTypeIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaMailJobBaseFilter(KalturaBaseJobFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaBaseJobFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMailJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaMailJobBaseFilter")
        return kparams


class KalturaNotificationBaseFilter(KalturaBaseJobFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaBaseJobFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaNotificationBaseFilter")
        return kparams


class KalturaBatchJobFilter(KalturaBatchJobBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            jobTypeEqual=NotImplemented,
            jobTypeIn=NotImplemented,
            jobTypeNotIn=NotImplemented,
            jobSubTypeEqual=NotImplemented,
            jobSubTypeIn=NotImplemented,
            jobSubTypeNotIn=NotImplemented,
            onStressDivertToEqual=NotImplemented,
            onStressDivertToIn=NotImplemented,
            onStressDivertToNotIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            abortEqual=NotImplemented,
            checkAgainTimeoutGreaterThanOrEqual=NotImplemented,
            checkAgainTimeoutLessThanOrEqual=NotImplemented,
            progressGreaterThanOrEqual=NotImplemented,
            progressLessThanOrEqual=NotImplemented,
            updatesCountGreaterThanOrEqual=NotImplemented,
            updatesCountLessThanOrEqual=NotImplemented,
            priorityGreaterThanOrEqual=NotImplemented,
            priorityLessThanOrEqual=NotImplemented,
            priorityEqual=NotImplemented,
            priorityIn=NotImplemented,
            priorityNotIn=NotImplemented,
            twinJobIdEqual=NotImplemented,
            twinJobIdIn=NotImplemented,
            twinJobIdNotIn=NotImplemented,
            bulkJobIdEqual=NotImplemented,
            bulkJobIdIn=NotImplemented,
            bulkJobIdNotIn=NotImplemented,
            parentJobIdEqual=NotImplemented,
            parentJobIdIn=NotImplemented,
            parentJobIdNotIn=NotImplemented,
            rootJobIdEqual=NotImplemented,
            rootJobIdIn=NotImplemented,
            rootJobIdNotIn=NotImplemented,
            queueTimeGreaterThanOrEqual=NotImplemented,
            queueTimeLessThanOrEqual=NotImplemented,
            finishTimeGreaterThanOrEqual=NotImplemented,
            finishTimeLessThanOrEqual=NotImplemented,
            errTypeEqual=NotImplemented,
            errTypeIn=NotImplemented,
            errTypeNotIn=NotImplemented,
            errNumberEqual=NotImplemented,
            errNumberIn=NotImplemented,
            errNumberNotIn=NotImplemented,
            fileSizeLessThan=NotImplemented,
            fileSizeGreaterThan=NotImplemented,
            lastWorkerRemoteEqual=NotImplemented,
            schedulerIdEqual=NotImplemented,
            schedulerIdIn=NotImplemented,
            schedulerIdNotIn=NotImplemented,
            workerIdEqual=NotImplemented,
            workerIdIn=NotImplemented,
            workerIdNotIn=NotImplemented,
            batchIndexEqual=NotImplemented,
            batchIndexIn=NotImplemented,
            batchIndexNotIn=NotImplemented,
            lastSchedulerIdEqual=NotImplemented,
            lastSchedulerIdIn=NotImplemented,
            lastSchedulerIdNotIn=NotImplemented,
            lastWorkerIdEqual=NotImplemented,
            lastWorkerIdIn=NotImplemented,
            lastWorkerIdNotIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            dcNotIn=NotImplemented):
        KalturaBatchJobBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual,
            entryIdEqual,
            jobTypeEqual,
            jobTypeIn,
            jobTypeNotIn,
            jobSubTypeEqual,
            jobSubTypeIn,
            jobSubTypeNotIn,
            onStressDivertToEqual,
            onStressDivertToIn,
            onStressDivertToNotIn,
            statusEqual,
            statusIn,
            statusNotIn,
            abortEqual,
            checkAgainTimeoutGreaterThanOrEqual,
            checkAgainTimeoutLessThanOrEqual,
            progressGreaterThanOrEqual,
            progressLessThanOrEqual,
            updatesCountGreaterThanOrEqual,
            updatesCountLessThanOrEqual,
            priorityGreaterThanOrEqual,
            priorityLessThanOrEqual,
            priorityEqual,
            priorityIn,
            priorityNotIn,
            twinJobIdEqual,
            twinJobIdIn,
            twinJobIdNotIn,
            bulkJobIdEqual,
            bulkJobIdIn,
            bulkJobIdNotIn,
            parentJobIdEqual,
            parentJobIdIn,
            parentJobIdNotIn,
            rootJobIdEqual,
            rootJobIdIn,
            rootJobIdNotIn,
            queueTimeGreaterThanOrEqual,
            queueTimeLessThanOrEqual,
            finishTimeGreaterThanOrEqual,
            finishTimeLessThanOrEqual,
            errTypeEqual,
            errTypeIn,
            errTypeNotIn,
            errNumberEqual,
            errNumberIn,
            errNumberNotIn,
            fileSizeLessThan,
            fileSizeGreaterThan,
            lastWorkerRemoteEqual,
            schedulerIdEqual,
            schedulerIdIn,
            schedulerIdNotIn,
            workerIdEqual,
            workerIdIn,
            workerIdNotIn,
            batchIndexEqual,
            batchIndexIn,
            batchIndexNotIn,
            lastSchedulerIdEqual,
            lastSchedulerIdIn,
            lastSchedulerIdNotIn,
            lastWorkerIdEqual,
            lastWorkerIdIn,
            lastWorkerIdNotIn,
            dcEqual,
            dcIn,
            dcNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBatchJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBatchJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobFilter")
        return kparams


class KalturaControlPanelCommandFilter(KalturaControlPanelCommandBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            createdByIdEqual=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            targetTypeEqual=NotImplemented,
            targetTypeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaControlPanelCommandBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            createdByIdEqual,
            typeEqual,
            typeIn,
            targetTypeEqual,
            targetTypeIn,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaControlPanelCommandBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaControlPanelCommandFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaControlPanelCommandBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaControlPanelCommandFilter")
        return kparams


class KalturaMailJobFilter(KalturaMailJobBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaMailJobBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMailJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMailJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMailJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMailJobFilter")
        return kparams


class KalturaNotificationFilter(KalturaNotificationBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented):
        KalturaNotificationBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaNotificationBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaNotificationBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaNotificationFilter")
        return kparams


class KalturaBatchJobFilterExt(KalturaBatchJobFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idGreaterThanOrEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            partnerIdNotIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            processorExpirationGreaterThanOrEqual=NotImplemented,
            processorExpirationLessThanOrEqual=NotImplemented,
            executionAttemptsGreaterThanOrEqual=NotImplemented,
            executionAttemptsLessThanOrEqual=NotImplemented,
            lockVersionGreaterThanOrEqual=NotImplemented,
            lockVersionLessThanOrEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            jobTypeEqual=NotImplemented,
            jobTypeIn=NotImplemented,
            jobTypeNotIn=NotImplemented,
            jobSubTypeEqual=NotImplemented,
            jobSubTypeIn=NotImplemented,
            jobSubTypeNotIn=NotImplemented,
            onStressDivertToEqual=NotImplemented,
            onStressDivertToIn=NotImplemented,
            onStressDivertToNotIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            abortEqual=NotImplemented,
            checkAgainTimeoutGreaterThanOrEqual=NotImplemented,
            checkAgainTimeoutLessThanOrEqual=NotImplemented,
            progressGreaterThanOrEqual=NotImplemented,
            progressLessThanOrEqual=NotImplemented,
            updatesCountGreaterThanOrEqual=NotImplemented,
            updatesCountLessThanOrEqual=NotImplemented,
            priorityGreaterThanOrEqual=NotImplemented,
            priorityLessThanOrEqual=NotImplemented,
            priorityEqual=NotImplemented,
            priorityIn=NotImplemented,
            priorityNotIn=NotImplemented,
            twinJobIdEqual=NotImplemented,
            twinJobIdIn=NotImplemented,
            twinJobIdNotIn=NotImplemented,
            bulkJobIdEqual=NotImplemented,
            bulkJobIdIn=NotImplemented,
            bulkJobIdNotIn=NotImplemented,
            parentJobIdEqual=NotImplemented,
            parentJobIdIn=NotImplemented,
            parentJobIdNotIn=NotImplemented,
            rootJobIdEqual=NotImplemented,
            rootJobIdIn=NotImplemented,
            rootJobIdNotIn=NotImplemented,
            queueTimeGreaterThanOrEqual=NotImplemented,
            queueTimeLessThanOrEqual=NotImplemented,
            finishTimeGreaterThanOrEqual=NotImplemented,
            finishTimeLessThanOrEqual=NotImplemented,
            errTypeEqual=NotImplemented,
            errTypeIn=NotImplemented,
            errTypeNotIn=NotImplemented,
            errNumberEqual=NotImplemented,
            errNumberIn=NotImplemented,
            errNumberNotIn=NotImplemented,
            fileSizeLessThan=NotImplemented,
            fileSizeGreaterThan=NotImplemented,
            lastWorkerRemoteEqual=NotImplemented,
            schedulerIdEqual=NotImplemented,
            schedulerIdIn=NotImplemented,
            schedulerIdNotIn=NotImplemented,
            workerIdEqual=NotImplemented,
            workerIdIn=NotImplemented,
            workerIdNotIn=NotImplemented,
            batchIndexEqual=NotImplemented,
            batchIndexIn=NotImplemented,
            batchIndexNotIn=NotImplemented,
            lastSchedulerIdEqual=NotImplemented,
            lastSchedulerIdIn=NotImplemented,
            lastSchedulerIdNotIn=NotImplemented,
            lastWorkerIdEqual=NotImplemented,
            lastWorkerIdIn=NotImplemented,
            lastWorkerIdNotIn=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            dcNotIn=NotImplemented,
            jobTypeAndSubTypeIn=NotImplemented):
        KalturaBatchJobFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idGreaterThanOrEqual,
            partnerIdEqual,
            partnerIdIn,
            partnerIdNotIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            processorExpirationGreaterThanOrEqual,
            processorExpirationLessThanOrEqual,
            executionAttemptsGreaterThanOrEqual,
            executionAttemptsLessThanOrEqual,
            lockVersionGreaterThanOrEqual,
            lockVersionLessThanOrEqual,
            entryIdEqual,
            jobTypeEqual,
            jobTypeIn,
            jobTypeNotIn,
            jobSubTypeEqual,
            jobSubTypeIn,
            jobSubTypeNotIn,
            onStressDivertToEqual,
            onStressDivertToIn,
            onStressDivertToNotIn,
            statusEqual,
            statusIn,
            statusNotIn,
            abortEqual,
            checkAgainTimeoutGreaterThanOrEqual,
            checkAgainTimeoutLessThanOrEqual,
            progressGreaterThanOrEqual,
            progressLessThanOrEqual,
            updatesCountGreaterThanOrEqual,
            updatesCountLessThanOrEqual,
            priorityGreaterThanOrEqual,
            priorityLessThanOrEqual,
            priorityEqual,
            priorityIn,
            priorityNotIn,
            twinJobIdEqual,
            twinJobIdIn,
            twinJobIdNotIn,
            bulkJobIdEqual,
            bulkJobIdIn,
            bulkJobIdNotIn,
            parentJobIdEqual,
            parentJobIdIn,
            parentJobIdNotIn,
            rootJobIdEqual,
            rootJobIdIn,
            rootJobIdNotIn,
            queueTimeGreaterThanOrEqual,
            queueTimeLessThanOrEqual,
            finishTimeGreaterThanOrEqual,
            finishTimeLessThanOrEqual,
            errTypeEqual,
            errTypeIn,
            errTypeNotIn,
            errNumberEqual,
            errNumberIn,
            errNumberNotIn,
            fileSizeLessThan,
            fileSizeGreaterThan,
            lastWorkerRemoteEqual,
            schedulerIdEqual,
            schedulerIdIn,
            schedulerIdNotIn,
            workerIdEqual,
            workerIdIn,
            workerIdNotIn,
            batchIndexEqual,
            batchIndexIn,
            batchIndexNotIn,
            lastSchedulerIdEqual,
            lastSchedulerIdIn,
            lastSchedulerIdNotIn,
            lastWorkerIdEqual,
            lastWorkerIdIn,
            lastWorkerIdNotIn,
            dcEqual,
            dcIn,
            dcNotIn)

        # @var string
        self.jobTypeAndSubTypeIn = jobTypeAndSubTypeIn


    PROPERTY_LOADERS = {
        'jobTypeAndSubTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBatchJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobFilterExt.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBatchJobFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobFilterExt")
        kparams.addStringIfDefined("jobTypeAndSubTypeIn", self.jobTypeAndSubTypeIn)
        return kparams

    def getJobTypeAndSubTypeIn(self):
        return self.jobTypeAndSubTypeIn

    def setJobTypeAndSubTypeIn(self, newJobTypeAndSubTypeIn):
        self.jobTypeAndSubTypeIn = newJobTypeAndSubTypeIn


class KalturaAssetParamsOutputBaseFilter(KalturaAssetParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            assetParamsIdEqual=NotImplemented,
            assetParamsVersionEqual=NotImplemented,
            assetIdEqual=NotImplemented,
            assetVersionEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaAssetParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual)

        # @var int
        self.assetParamsIdEqual = assetParamsIdEqual

        # @var string
        self.assetParamsVersionEqual = assetParamsVersionEqual

        # @var string
        self.assetIdEqual = assetIdEqual

        # @var string
        self.assetVersionEqual = assetVersionEqual

        # @var KalturaContainerFormat
        self.formatEqual = formatEqual


    PROPERTY_LOADERS = {
        'assetParamsIdEqual': getXmlNodeInt, 
        'assetParamsVersionEqual': getXmlNodeText, 
        'assetIdEqual': getXmlNodeText, 
        'assetVersionEqual': getXmlNodeText, 
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutputBaseFilter")
        kparams.addIntIfDefined("assetParamsIdEqual", self.assetParamsIdEqual)
        kparams.addStringIfDefined("assetParamsVersionEqual", self.assetParamsVersionEqual)
        kparams.addStringIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addStringIfDefined("assetVersionEqual", self.assetVersionEqual)
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        return kparams

    def getAssetParamsIdEqual(self):
        return self.assetParamsIdEqual

    def setAssetParamsIdEqual(self, newAssetParamsIdEqual):
        self.assetParamsIdEqual = newAssetParamsIdEqual

    def getAssetParamsVersionEqual(self):
        return self.assetParamsVersionEqual

    def setAssetParamsVersionEqual(self, newAssetParamsVersionEqual):
        self.assetParamsVersionEqual = newAssetParamsVersionEqual

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetVersionEqual(self):
        return self.assetVersionEqual

    def setAssetVersionEqual(self, newAssetVersionEqual):
        self.assetVersionEqual = newAssetVersionEqual

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual


class KalturaFlavorAssetBaseFilter(KalturaAssetFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
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
            deletedAtLessThanOrEqual)

        # @var KalturaFlavorAssetStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.statusNotIn = statusNotIn


    PROPERTY_LOADERS = {
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaFlavorAssetStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetBaseFilter")
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        return kparams

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn


class KalturaMediaFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaFlavorParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsBaseFilter")
        return kparams


class KalturaMediaFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaFlavorParamsOutputFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutputBaseFilter")
        return kparams


class KalturaThumbAssetBaseFilter(KalturaAssetFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
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
            deletedAtLessThanOrEqual)

        # @var KalturaThumbAssetStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.statusNotIn = statusNotIn


    PROPERTY_LOADERS = {
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaThumbAssetStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetBaseFilter")
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        return kparams

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn


class KalturaAssetParamsOutputFilter(KalturaAssetParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            assetParamsIdEqual=NotImplemented,
            assetParamsVersionEqual=NotImplemented,
            assetIdEqual=NotImplemented,
            assetVersionEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaAssetParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            assetParamsIdEqual,
            assetParamsVersionEqual,
            assetIdEqual,
            assetVersionEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutputFilter")
        return kparams


class KalturaFlavorAssetFilter(KalturaFlavorAssetBaseFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaFlavorAssetBaseFilter.__init__(self,
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
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetFilter")
        return kparams


class KalturaMediaFlavorParamsFilter(KalturaMediaFlavorParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented):
        KalturaMediaFlavorParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsFilter")
        return kparams


class KalturaMediaFlavorParamsOutputFilter(KalturaMediaFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            flavorParamsIdEqual=NotImplemented,
            flavorParamsVersionEqual=NotImplemented,
            flavorAssetIdEqual=NotImplemented,
            flavorAssetVersionEqual=NotImplemented):
        KalturaMediaFlavorParamsOutputBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            flavorParamsIdEqual,
            flavorParamsVersionEqual,
            flavorAssetIdEqual,
            flavorAssetVersionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutputFilter")
        return kparams


class KalturaThumbAssetFilter(KalturaThumbAssetBaseFilter):
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
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaThumbAssetBaseFilter.__init__(self,
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
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetFilter")
        return kparams


class KalturaLiveStreamAdminEntryBaseFilter(KalturaLiveStreamEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaLiveStreamEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntryBaseFilter")
        return kparams


class KalturaLiveStreamAdminEntryFilter(KalturaLiveStreamAdminEntryBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            adminTagsLike=NotImplemented,
            adminTagsMultiLikeOr=NotImplemented,
            adminTagsMultiLikeAnd=NotImplemented,
            categoriesMatchAnd=NotImplemented,
            categoriesMatchOr=NotImplemented,
            categoriesIdsMatchAnd=NotImplemented,
            categoriesIdsMatchOr=NotImplemented,
            statusEqual=NotImplemented,
            statusNotEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented,
            moderationStatusEqual=NotImplemented,
            moderationStatusNotEqual=NotImplemented,
            moderationStatusIn=NotImplemented,
            moderationStatusNotIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            groupIdEqual=NotImplemented,
            searchTextMatchAnd=NotImplemented,
            searchTextMatchOr=NotImplemented,
            accessControlIdEqual=NotImplemented,
            accessControlIdIn=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            startDateLessThanOrEqual=NotImplemented,
            startDateGreaterThanOrEqualOrNull=NotImplemented,
            startDateLessThanOrEqualOrNull=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqualOrNull=NotImplemented,
            endDateLessThanOrEqualOrNull=NotImplemented,
            referenceIdEqual=NotImplemented,
            referenceIdIn=NotImplemented,
            replacingEntryIdEqual=NotImplemented,
            replacingEntryIdIn=NotImplemented,
            replacedEntryIdEqual=NotImplemented,
            replacedEntryIdIn=NotImplemented,
            replacementStatusEqual=NotImplemented,
            replacementStatusIn=NotImplemented,
            partnerSortValueGreaterThanOrEqual=NotImplemented,
            partnerSortValueLessThanOrEqual=NotImplemented,
            rootEntryIdEqual=NotImplemented,
            rootEntryIdIn=NotImplemented,
            tagsNameMultiLikeOr=NotImplemented,
            tagsAdminTagsMultiLikeOr=NotImplemented,
            tagsAdminTagsNameMultiLikeOr=NotImplemented,
            tagsNameMultiLikeAnd=NotImplemented,
            tagsAdminTagsMultiLikeAnd=NotImplemented,
            tagsAdminTagsNameMultiLikeAnd=NotImplemented,
            freeText=NotImplemented,
            isRoot=NotImplemented,
            durationLessThan=NotImplemented,
            durationGreaterThan=NotImplemented,
            durationLessThanOrEqual=NotImplemented,
            durationGreaterThanOrEqual=NotImplemented,
            msDurationLessThan=NotImplemented,
            msDurationGreaterThan=NotImplemented,
            msDurationLessThanOrEqual=NotImplemented,
            msDurationGreaterThanOrEqual=NotImplemented,
            durationTypeMatchOr=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaDateGreaterThanOrEqual=NotImplemented,
            mediaDateLessThanOrEqual=NotImplemented,
            flavorParamsIdsMatchOr=NotImplemented,
            flavorParamsIdsMatchAnd=NotImplemented):
        KalturaLiveStreamAdminEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            freeText,
            isRoot,
            durationLessThan,
            durationGreaterThan,
            durationLessThanOrEqual,
            durationGreaterThanOrEqual,
            msDurationLessThan,
            msDurationGreaterThan,
            msDurationLessThanOrEqual,
            msDurationGreaterThanOrEqual,
            durationTypeMatchOr,
            mediaTypeEqual,
            mediaTypeIn,
            mediaDateGreaterThanOrEqual,
            mediaDateLessThanOrEqual,
            flavorParamsIdsMatchOr,
            flavorParamsIdsMatchAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamAdminEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamAdminEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntryFilter")
        return kparams


class KalturaAdminUserBaseFilter(KalturaUserFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            screenNameLike=NotImplemented,
            screenNameStartsWith=NotImplemented,
            emailLike=NotImplemented,
            emailStartsWith=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            isAdminEqual=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            loginEnabledEqual=NotImplemented):
        KalturaUserFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            screenNameLike,
            screenNameStartsWith,
            emailLike,
            emailStartsWith,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            isAdminEqual,
            idEqual,
            idIn,
            loginEnabledEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdminUserBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserFilter.toParams(self)
        kparams.put("objectType", "KalturaAdminUserBaseFilter")
        return kparams


class KalturaAdminUserFilter(KalturaAdminUserBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            screenNameLike=NotImplemented,
            screenNameStartsWith=NotImplemented,
            emailLike=NotImplemented,
            emailStartsWith=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            isAdminEqual=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            loginEnabledEqual=NotImplemented):
        KalturaAdminUserBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            screenNameLike,
            screenNameStartsWith,
            emailLike,
            emailStartsWith,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            isAdminEqual,
            idEqual,
            idIn,
            loginEnabledEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAdminUserBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdminUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAdminUserBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAdminUserFilter")
        return kparams


class KalturaGoogleVideoSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeedBaseFilter")
        return kparams


class KalturaGoogleVideoSyndicationFeedFilter(KalturaGoogleVideoSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaGoogleVideoSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGoogleVideoSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGoogleVideoSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeedFilter")
        return kparams


class KalturaITunesSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeedBaseFilter")
        return kparams


class KalturaITunesSyndicationFeedFilter(KalturaITunesSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaITunesSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaITunesSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaITunesSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeedFilter")
        return kparams


class KalturaTubeMogulSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeedBaseFilter")
        return kparams


class KalturaTubeMogulSyndicationFeedFilter(KalturaTubeMogulSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaTubeMogulSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTubeMogulSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTubeMogulSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeedFilter")
        return kparams


class KalturaYahooSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeedBaseFilter")
        return kparams


class KalturaYahooSyndicationFeedFilter(KalturaYahooSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaYahooSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaYahooSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYahooSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeedFilter")
        return kparams


class KalturaApiActionPermissionItemBaseFilter(KalturaPermissionItemFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaPermissionItemFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemFilter.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItemBaseFilter")
        return kparams


class KalturaApiParameterPermissionItemBaseFilter(KalturaPermissionItemFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaPermissionItemFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemFilter.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItemBaseFilter")
        return kparams


class KalturaApiActionPermissionItemFilter(KalturaApiActionPermissionItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaApiActionPermissionItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaApiActionPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaApiActionPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItemFilter")
        return kparams


class KalturaApiParameterPermissionItemFilter(KalturaApiParameterPermissionItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaApiParameterPermissionItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            typeEqual,
            typeIn,
            partnerIdEqual,
            partnerIdIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaApiParameterPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaApiParameterPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItemFilter")
        return kparams


class KalturaGenericSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaBaseSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeedBaseFilter")
        return kparams


class KalturaGenericSyndicationFeedFilter(KalturaGenericSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaGenericSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeedFilter")
        return kparams


class KalturaGenericXsltSyndicationFeedBaseFilter(KalturaGenericSyndicationFeedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaGenericSyndicationFeedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeedBaseFilter")
        return kparams


class KalturaGenericXsltSyndicationFeedFilter(KalturaGenericXsltSyndicationFeedBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented):
        KalturaGenericXsltSyndicationFeedBaseFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericXsltSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericXsltSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeedFilter")
        return kparams


class KalturaClipAttributes(KalturaOperationAttributes):
    """Clip operation attributes"""

    def __init__(self,
            offset=NotImplemented,
            duration=NotImplemented):
        KalturaOperationAttributes.__init__(self)

        # Offset in milliseconds
        # @var int
        self.offset = offset

        # Duration in milliseconds
        # @var int
        self.duration = duration


    PROPERTY_LOADERS = {
        'offset': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaOperationAttributes.fromXml(self, node)
        self.fromXmlImpl(node, KalturaClipAttributes.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaOperationAttributes.toParams(self)
        kparams.put("objectType", "KalturaClipAttributes")
        kparams.addIntIfDefined("offset", self.offset)
        kparams.addIntIfDefined("duration", self.duration)
        return kparams

    def getOffset(self):
        return self.offset

    def setOffset(self, newOffset):
        self.offset = newOffset

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration


class KalturaAssetParamsResourceContainer(KalturaResource):
    def __init__(self,
            resource=NotImplemented,
            assetParamsId=NotImplemented):
        KalturaResource.__init__(self)

        # The content resource to associate with asset params
        # @var KalturaContentResource
        self.resource = resource

        # The asset params to associate with the reaource
        # @var int
        self.assetParamsId = assetParamsId


    PROPERTY_LOADERS = {
        'resource': (KalturaObjectFactory.create, KalturaContentResource), 
        'assetParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsResourceContainer.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaResource.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsResourceContainer")
        kparams.addObjectIfDefined("resource", self.resource)
        kparams.addIntIfDefined("assetParamsId", self.assetParamsId)
        return kparams

    def getResource(self):
        return self.resource

    def setResource(self, newResource):
        self.resource = newResource

    def getAssetParamsId(self):
        return self.assetParamsId

    def setAssetParamsId(self, newAssetParamsId):
        self.assetParamsId = newAssetParamsId


class KalturaAssetResource(KalturaContentResource):
    """Used to ingest media that is already ingested to Kaltura system as a different flavor asset in the past, the new created flavor asset will be ready immediately using a file sync of link type that will point to the existing file sync of the existing flavor asset."""

    def __init__(self,
            assetId=NotImplemented):
        KalturaContentResource.__init__(self)

        # ID of the source asset
        # @var string
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaAssetResource")
        kparams.addStringIfDefined("assetId", self.assetId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


class KalturaAssetsParamsResourceContainers(KalturaResource):
    def __init__(self,
            resources=NotImplemented):
        KalturaResource.__init__(self)

        # Array of resources associated with asset params ids
        # @var array of KalturaAssetParamsResourceContainer
        self.resources = resources


    PROPERTY_LOADERS = {
        'resources': (KalturaObjectFactory.createArray, KalturaAssetParamsResourceContainer), 
    }

    def fromXml(self, node):
        KalturaResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetsParamsResourceContainers.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaResource.toParams(self)
        kparams.put("objectType", "KalturaAssetsParamsResourceContainers")
        kparams.addArrayIfDefined("resources", self.resources)
        return kparams

    def getResources(self):
        return self.resources

    def setResources(self, newResources):
        self.resources = newResources


class KalturaDataCenterContentResource(KalturaContentResource):
    def __init__(self):
        KalturaContentResource.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataCenterContentResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaDataCenterContentResource")
        return kparams


class KalturaEntryResource(KalturaContentResource):
    """Used to ingest media that is already ingested to Kaltura system as a different entry in the past, the new created flavor asset will be ready immediately using a file sync of link type that will point to the existing file sync of the existing entry."""

    def __init__(self,
            entryId=NotImplemented,
            flavorParamsId=NotImplemented):
        KalturaContentResource.__init__(self)

        # ID of the source entry
        # @var string
        self.entryId = entryId

        # ID of the source flavor params, set to null to use the source flavor
        # @var int
        self.flavorParamsId = flavorParamsId


    PROPERTY_LOADERS = {
        'entryId': getXmlNodeText, 
        'flavorParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaEntryResource")
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        return kparams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId


class KalturaFileSyncResource(KalturaContentResource):
    """Used to ingest media that is already ingested to Kaltura system as a different file in the past, the new created flavor asset will be ready immediately using a file sync of link type that will point to the existing file sync."""

    def __init__(self,
            fileSyncObjectType=NotImplemented,
            objectSubType=NotImplemented,
            objectId=NotImplemented,
            version=NotImplemented):
        KalturaContentResource.__init__(self)

        # The object type of the file sync object
        # @var int
        self.fileSyncObjectType = fileSyncObjectType

        # The object sub-type of the file sync object
        # @var int
        self.objectSubType = objectSubType

        # The object id of the file sync object
        # @var string
        self.objectId = objectId

        # The version of the file sync object
        # @var string
        self.version = version


    PROPERTY_LOADERS = {
        'fileSyncObjectType': getXmlNodeInt, 
        'objectSubType': getXmlNodeInt, 
        'objectId': getXmlNodeText, 
        'version': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFileSyncResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaFileSyncResource")
        kparams.addIntIfDefined("fileSyncObjectType", self.fileSyncObjectType)
        kparams.addIntIfDefined("objectSubType", self.objectSubType)
        kparams.addStringIfDefined("objectId", self.objectId)
        kparams.addStringIfDefined("version", self.version)
        return kparams

    def getFileSyncObjectType(self):
        return self.fileSyncObjectType

    def setFileSyncObjectType(self, newFileSyncObjectType):
        self.fileSyncObjectType = newFileSyncObjectType

    def getObjectSubType(self):
        return self.objectSubType

    def setObjectSubType(self, newObjectSubType):
        self.objectSubType = newObjectSubType

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getVersion(self):
        return self.version

    def setVersion(self, newVersion):
        self.version = newVersion


class KalturaOperationResource(KalturaContentResource):
    """A resource that perform operation (transcoding, clipping, cropping) before the flavor is ready."""

    def __init__(self,
            resource=NotImplemented,
            operationAttributes=NotImplemented,
            assetParamsId=NotImplemented):
        KalturaContentResource.__init__(self)

        # Only KalturaEntryResource and KalturaAssetResource are supported
        # @var KalturaContentResource
        self.resource = resource

        # @var array of KalturaOperationAttributes
        self.operationAttributes = operationAttributes

        # ID of alternative asset params to be used instead of the system default flavor params
        # @var int
        self.assetParamsId = assetParamsId


    PROPERTY_LOADERS = {
        'resource': (KalturaObjectFactory.create, KalturaContentResource), 
        'operationAttributes': (KalturaObjectFactory.createArray, KalturaOperationAttributes), 
        'assetParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOperationResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaOperationResource")
        kparams.addObjectIfDefined("resource", self.resource)
        kparams.addArrayIfDefined("operationAttributes", self.operationAttributes)
        kparams.addIntIfDefined("assetParamsId", self.assetParamsId)
        return kparams

    def getResource(self):
        return self.resource

    def setResource(self, newResource):
        self.resource = newResource

    def getOperationAttributes(self):
        return self.operationAttributes

    def setOperationAttributes(self, newOperationAttributes):
        self.operationAttributes = newOperationAttributes

    def getAssetParamsId(self):
        return self.assetParamsId

    def setAssetParamsId(self, newAssetParamsId):
        self.assetParamsId = newAssetParamsId


class KalturaUrlResource(KalturaContentResource):
    """Used to ingest media that is available on remote server and accessible using the supplied URL, media file will be downloaded using import job in order to make the asset ready."""

    def __init__(self,
            url=NotImplemented):
        KalturaContentResource.__init__(self)

        # Remote URL, FTP, HTTP or HTTPS
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUrlResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaUrlResource")
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


class KalturaRemoteStorageResource(KalturaUrlResource):
    """Used to ingest media that is available on remote server and accessible using the supplied URL, the media file won't be downloaded but a file sync object of URL type will point to the media URL."""

    def __init__(self,
            url=NotImplemented,
            storageProfileId=NotImplemented):
        KalturaUrlResource.__init__(self,
            url)

        # ID of storage profile to be associated with the created file sync, used for file serving URL composing.
        # @var int
        self.storageProfileId = storageProfileId


    PROPERTY_LOADERS = {
        'storageProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUrlResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemoteStorageResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUrlResource.toParams(self)
        kparams.put("objectType", "KalturaRemoteStorageResource")
        kparams.addIntIfDefined("storageProfileId", self.storageProfileId)
        return kparams

    def getStorageProfileId(self):
        return self.storageProfileId

    def setStorageProfileId(self, newStorageProfileId):
        self.storageProfileId = newStorageProfileId


class KalturaRemoteStorageResources(KalturaContentResource):
    """Used to ingest media that is available on remote server and accessible using the supplied URL, the media file won't be downloaded but a file sync object of URL type will point to the media URL."""

    def __init__(self,
            resources=NotImplemented):
        KalturaContentResource.__init__(self)

        # Array of remote stoage resources
        # @var array of KalturaRemoteStorageResource
        self.resources = resources


    PROPERTY_LOADERS = {
        'resources': (KalturaObjectFactory.createArray, KalturaRemoteStorageResource), 
    }

    def fromXml(self, node):
        KalturaContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRemoteStorageResources.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaContentResource.toParams(self)
        kparams.put("objectType", "KalturaRemoteStorageResources")
        kparams.addArrayIfDefined("resources", self.resources)
        return kparams

    def getResources(self):
        return self.resources

    def setResources(self, newResources):
        self.resources = newResources


class KalturaServerFileResource(KalturaDataCenterContentResource):
    """Used to ingest media file that is already accessible on the shared disc."""

    def __init__(self,
            localFilePath=NotImplemented):
        KalturaDataCenterContentResource.__init__(self)

        # Full path to the local file
        # @var string
        self.localFilePath = localFilePath


    PROPERTY_LOADERS = {
        'localFilePath': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDataCenterContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaServerFileResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataCenterContentResource.toParams(self)
        kparams.put("objectType", "KalturaServerFileResource")
        kparams.addStringIfDefined("localFilePath", self.localFilePath)
        return kparams

    def getLocalFilePath(self):
        return self.localFilePath

    def setLocalFilePath(self, newLocalFilePath):
        self.localFilePath = newLocalFilePath


class KalturaSshUrlResource(KalturaUrlResource):
    """Used to ingest media that is available on remote SSH server and accessible using the supplied URL, media file will be downloaded using import job in order to make the asset ready."""

    def __init__(self,
            url=NotImplemented,
            privateKey=NotImplemented,
            publicKey=NotImplemented,
            keyPassphrase=NotImplemented):
        KalturaUrlResource.__init__(self,
            url)

        # SSH private key
        # @var string
        self.privateKey = privateKey

        # SSH public key
        # @var string
        self.publicKey = publicKey

        # Passphrase for SSH keys
        # @var string
        self.keyPassphrase = keyPassphrase


    PROPERTY_LOADERS = {
        'privateKey': getXmlNodeText, 
        'publicKey': getXmlNodeText, 
        'keyPassphrase': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaUrlResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSshUrlResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUrlResource.toParams(self)
        kparams.put("objectType", "KalturaSshUrlResource")
        kparams.addStringIfDefined("privateKey", self.privateKey)
        kparams.addStringIfDefined("publicKey", self.publicKey)
        kparams.addStringIfDefined("keyPassphrase", self.keyPassphrase)
        return kparams

    def getPrivateKey(self):
        return self.privateKey

    def setPrivateKey(self, newPrivateKey):
        self.privateKey = newPrivateKey

    def getPublicKey(self):
        return self.publicKey

    def setPublicKey(self, newPublicKey):
        self.publicKey = newPublicKey

    def getKeyPassphrase(self):
        return self.keyPassphrase

    def setKeyPassphrase(self, newKeyPassphrase):
        self.keyPassphrase = newKeyPassphrase


class KalturaUploadedFileTokenResource(KalturaDataCenterContentResource):
    """Used to ingest media that uploaded to the system and represented by token that returned from upload.upload action or uploadToken.add action."""

    def __init__(self,
            token=NotImplemented):
        KalturaDataCenterContentResource.__init__(self)

        # Token that returned from upload.upload action or uploadToken.add action.
        # @var string
        self.token = token


    PROPERTY_LOADERS = {
        'token': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDataCenterContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadedFileTokenResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataCenterContentResource.toParams(self)
        kparams.put("objectType", "KalturaUploadedFileTokenResource")
        kparams.addStringIfDefined("token", self.token)
        return kparams

    def getToken(self):
        return self.token

    def setToken(self, newToken):
        self.token = newToken


class KalturaWebcamTokenResource(KalturaDataCenterContentResource):
    """Used to ingest media that streamed to the system and represented by token that returned from media server such as FMS or red5."""

    def __init__(self,
            token=NotImplemented):
        KalturaDataCenterContentResource.__init__(self)

        # Token that returned from media server such as FMS or red5.
        # @var string
        self.token = token


    PROPERTY_LOADERS = {
        'token': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDataCenterContentResource.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWebcamTokenResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataCenterContentResource.toParams(self)
        kparams.put("objectType", "KalturaWebcamTokenResource")
        kparams.addStringIfDefined("token", self.token)
        return kparams

    def getToken(self):
        return self.token

    def setToken(self, newToken):
        self.token = newToken


class KalturaAssetParamsOutput(KalturaAssetParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            assetParamsId=NotImplemented,
            assetParamsVersion=NotImplemented,
            assetId=NotImplemented,
            assetVersion=NotImplemented,
            readyBehavior=NotImplemented,
            format=NotImplemented):
        KalturaAssetParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions)

        # @var int
        self.assetParamsId = assetParamsId

        # @var string
        self.assetParamsVersion = assetParamsVersion

        # @var string
        self.assetId = assetId

        # @var string
        self.assetVersion = assetVersion

        # @var int
        self.readyBehavior = readyBehavior

        # The container format of the Flavor Params
        # @var KalturaContainerFormat
        self.format = format


    PROPERTY_LOADERS = {
        'assetParamsId': getXmlNodeInt, 
        'assetParamsVersion': getXmlNodeText, 
        'assetId': getXmlNodeText, 
        'assetVersion': getXmlNodeText, 
        'readyBehavior': getXmlNodeInt, 
        'format': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutput")
        kparams.addIntIfDefined("assetParamsId", self.assetParamsId)
        kparams.addStringIfDefined("assetParamsVersion", self.assetParamsVersion)
        kparams.addStringIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("assetVersion", self.assetVersion)
        kparams.addIntIfDefined("readyBehavior", self.readyBehavior)
        kparams.addStringEnumIfDefined("format", self.format)
        return kparams

    def getAssetParamsId(self):
        return self.assetParamsId

    def setAssetParamsId(self, newAssetParamsId):
        self.assetParamsId = newAssetParamsId

    def getAssetParamsVersion(self):
        return self.assetParamsVersion

    def setAssetParamsVersion(self, newAssetParamsVersion):
        self.assetParamsVersion = newAssetParamsVersion

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getAssetVersion(self):
        return self.assetVersion

    def setAssetVersion(self, newAssetVersion):
        self.assetVersion = newAssetVersion

    def getReadyBehavior(self):
        return self.readyBehavior

    def setReadyBehavior(self, newReadyBehavior):
        self.readyBehavior = newReadyBehavior

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat


class KalturaMediaFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented,
            flavorParamsId=NotImplemented,
            commandLinesStr=NotImplemented,
            flavorParamsVersion=NotImplemented,
            flavorAssetId=NotImplemented,
            flavorAssetVersion=NotImplemented,
            readyBehavior=NotImplemented):
        KalturaFlavorParamsOutput.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance,
            flavorParamsId,
            commandLinesStr,
            flavorParamsVersion,
            flavorAssetId,
            flavorAssetVersion,
            readyBehavior)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutput")
        return kparams


class KalturaMediaFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            videoCodec=NotImplemented,
            videoBitrate=NotImplemented,
            audioCodec=NotImplemented,
            audioBitrate=NotImplemented,
            audioChannels=NotImplemented,
            audioSampleRate=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            frameRate=NotImplemented,
            gopSize=NotImplemented,
            conversionEngines=NotImplemented,
            conversionEnginesExtraParams=NotImplemented,
            twoPass=NotImplemented,
            deinterlice=NotImplemented,
            rotate=NotImplemented,
            operators=NotImplemented,
            engineVersion=NotImplemented,
            format=NotImplemented,
            aspectRatioProcessingMode=NotImplemented,
            forceFrameToMultiplication16=NotImplemented,
            videoConstantBitrate=NotImplemented,
            videoBitrateTolerance=NotImplemented):
        KalturaFlavorParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            videoCodec,
            videoBitrate,
            audioCodec,
            audioBitrate,
            audioChannels,
            audioSampleRate,
            width,
            height,
            frameRate,
            gopSize,
            conversionEngines,
            conversionEnginesExtraParams,
            twoPass,
            deinterlice,
            rotate,
            operators,
            engineVersion,
            format,
            aspectRatioProcessingMode,
            forceFrameToMultiplication16,
            videoConstantBitrate,
            videoBitrateTolerance)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParams")
        return kparams


class KalturaApiActionPermissionItem(KalturaPermissionItem):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            partnerId=NotImplemented,
            tags=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            service=NotImplemented,
            action=NotImplemented):
        KalturaPermissionItem.__init__(self,
            id,
            type,
            partnerId,
            tags,
            createdAt,
            updatedAt)

        # @var string
        self.service = service

        # @var string
        self.action = action


    PROPERTY_LOADERS = {
        'service': getXmlNodeText, 
        'action': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItem")
        kparams.addStringIfDefined("service", self.service)
        kparams.addStringIfDefined("action", self.action)
        return kparams

    def getService(self):
        return self.service

    def setService(self, newService):
        self.service = newService

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


class KalturaApiParameterPermissionItem(KalturaPermissionItem):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            partnerId=NotImplemented,
            tags=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            object=NotImplemented,
            parameter=NotImplemented,
            action=NotImplemented):
        KalturaPermissionItem.__init__(self,
            id,
            type,
            partnerId,
            tags,
            createdAt,
            updatedAt)

        # @var string
        self.object = object

        # @var string
        self.parameter = parameter

        # @var KalturaApiParameterPermissionItemAction
        self.action = action


    PROPERTY_LOADERS = {
        'object': getXmlNodeText, 
        'parameter': getXmlNodeText, 
        'action': (KalturaEnumsFactory.createString, "KalturaApiParameterPermissionItemAction"), 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItem")
        kparams.addStringIfDefined("object", self.object)
        kparams.addStringIfDefined("parameter", self.parameter)
        kparams.addStringEnumIfDefined("action", self.action)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject

    def getParameter(self):
        return self.parameter

    def setParameter(self, newParameter):
        self.parameter = newParameter

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


class KalturaGenericSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            feedDescription=NotImplemented,
            feedLandingPage=NotImplemented):
        KalturaBaseSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId)

        # feed description
        # @var string
        self.feedDescription = feedDescription

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = feedLandingPage


    PROPERTY_LOADERS = {
        'feedDescription': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeed")
        kparams.addStringIfDefined("feedDescription", self.feedDescription)
        kparams.addStringIfDefined("feedLandingPage", self.feedLandingPage)
        return kparams

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage


class KalturaGenericXsltSyndicationFeed(KalturaGenericSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            feedDescription=NotImplemented,
            feedLandingPage=NotImplemented,
            xslt=NotImplemented,
            itemXpathsToExtend=NotImplemented):
        KalturaGenericSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId,
            feedDescription,
            feedLandingPage)

        # @var string
        self.xslt = xslt

        # This parameter determines which custom metadata fields of type related-entry should be
        # expanded to contain the kaltura MRSS feed of the related entry. Related-entry fields not
        # included in this list will contain only the related entry id.
        # This property contains a list xPaths in the Kaltura MRSS.
        # @var array of KalturaString
        self.itemXpathsToExtend = itemXpathsToExtend


    PROPERTY_LOADERS = {
        'xslt': getXmlNodeText, 
        'itemXpathsToExtend': (KalturaObjectFactory.createArray, KalturaString), 
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeed")
        kparams.addStringIfDefined("xslt", self.xslt)
        kparams.addArrayIfDefined("itemXpathsToExtend", self.itemXpathsToExtend)
        return kparams

    def getXslt(self):
        return self.xslt

    def setXslt(self, newXslt):
        self.xslt = newXslt

    def getItemXpathsToExtend(self):
        return self.itemXpathsToExtend

    def setItemXpathsToExtend(self, newItemXpathsToExtend):
        self.itemXpathsToExtend = newItemXpathsToExtend


class KalturaGoogleVideoSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            adultContent=NotImplemented):
        KalturaBaseSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId)

        # @var KalturaGoogleSyndicationFeedAdultValues
        self.adultContent = adultContent


    PROPERTY_LOADERS = {
        'adultContent': (KalturaEnumsFactory.createString, "KalturaGoogleSyndicationFeedAdultValues"), 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeed")
        kparams.addStringEnumIfDefined("adultContent", self.adultContent)
        return kparams

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent


class KalturaITunesSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            feedDescription=NotImplemented,
            language=NotImplemented,
            feedLandingPage=NotImplemented,
            ownerName=NotImplemented,
            ownerEmail=NotImplemented,
            feedImageUrl=NotImplemented,
            category=NotImplemented,
            adultContent=NotImplemented,
            feedAuthor=NotImplemented):
        KalturaBaseSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId)

        # feed description
        # @var string
        self.feedDescription = feedDescription

        # feed language
        # @var string
        self.language = language

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = feedLandingPage

        # author/publisher name
        # @var string
        self.ownerName = ownerName

        # publisher email
        # @var string
        self.ownerEmail = ownerEmail

        # podcast thumbnail
        # @var string
        self.feedImageUrl = feedImageUrl

        # @var KalturaITunesSyndicationFeedCategories
        # @readonly
        self.category = category

        # @var KalturaITunesSyndicationFeedAdultValues
        self.adultContent = adultContent

        # @var string
        self.feedAuthor = feedAuthor


    PROPERTY_LOADERS = {
        'feedDescription': getXmlNodeText, 
        'language': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
        'ownerName': getXmlNodeText, 
        'ownerEmail': getXmlNodeText, 
        'feedImageUrl': getXmlNodeText, 
        'category': (KalturaEnumsFactory.createString, "KalturaITunesSyndicationFeedCategories"), 
        'adultContent': (KalturaEnumsFactory.createString, "KalturaITunesSyndicationFeedAdultValues"), 
        'feedAuthor': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeed")
        kparams.addStringIfDefined("feedDescription", self.feedDescription)
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("feedLandingPage", self.feedLandingPage)
        kparams.addStringIfDefined("ownerName", self.ownerName)
        kparams.addStringIfDefined("ownerEmail", self.ownerEmail)
        kparams.addStringIfDefined("feedImageUrl", self.feedImageUrl)
        kparams.addStringEnumIfDefined("adultContent", self.adultContent)
        kparams.addStringIfDefined("feedAuthor", self.feedAuthor)
        return kparams

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage

    def getOwnerName(self):
        return self.ownerName

    def setOwnerName(self, newOwnerName):
        self.ownerName = newOwnerName

    def getOwnerEmail(self):
        return self.ownerEmail

    def setOwnerEmail(self, newOwnerEmail):
        self.ownerEmail = newOwnerEmail

    def getFeedImageUrl(self):
        return self.feedImageUrl

    def setFeedImageUrl(self, newFeedImageUrl):
        self.feedImageUrl = newFeedImageUrl

    def getCategory(self):
        return self.category

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getFeedAuthor(self):
        return self.feedAuthor

    def setFeedAuthor(self, newFeedAuthor):
        self.feedAuthor = newFeedAuthor


class KalturaTubeMogulSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            category=NotImplemented):
        KalturaBaseSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId)

        # @var KalturaTubeMogulSyndicationFeedCategories
        # @readonly
        self.category = category


    PROPERTY_LOADERS = {
        'category': (KalturaEnumsFactory.createString, "KalturaTubeMogulSyndicationFeedCategories"), 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeed")
        return kparams

    def getCategory(self):
        return self.category


class KalturaYahooSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self,
            id=NotImplemented,
            feedUrl=NotImplemented,
            partnerId=NotImplemented,
            playlistId=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            landingPage=NotImplemented,
            createdAt=NotImplemented,
            allowEmbed=NotImplemented,
            playerUiconfId=NotImplemented,
            flavorParamId=NotImplemented,
            transcodeExistingContent=NotImplemented,
            addToDefaultConversionProfile=NotImplemented,
            categories=NotImplemented,
            storageId=NotImplemented,
            category=NotImplemented,
            adultContent=NotImplemented,
            feedDescription=NotImplemented,
            feedLandingPage=NotImplemented):
        KalturaBaseSyndicationFeed.__init__(self,
            id,
            feedUrl,
            partnerId,
            playlistId,
            name,
            status,
            type,
            landingPage,
            createdAt,
            allowEmbed,
            playerUiconfId,
            flavorParamId,
            transcodeExistingContent,
            addToDefaultConversionProfile,
            categories,
            storageId)

        # @var KalturaYahooSyndicationFeedCategories
        # @readonly
        self.category = category

        # @var KalturaYahooSyndicationFeedAdultValues
        self.adultContent = adultContent

        # feed description
        # @var string
        self.feedDescription = feedDescription

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = feedLandingPage


    PROPERTY_LOADERS = {
        'category': (KalturaEnumsFactory.createString, "KalturaYahooSyndicationFeedCategories"), 
        'adultContent': (KalturaEnumsFactory.createString, "KalturaYahooSyndicationFeedAdultValues"), 
        'feedDescription': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeed")
        kparams.addStringEnumIfDefined("adultContent", self.adultContent)
        kparams.addStringIfDefined("feedDescription", self.feedDescription)
        kparams.addStringIfDefined("feedLandingPage", self.feedLandingPage)
        return kparams

    def getCategory(self):
        return self.category

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage


########## services ##########

class KalturaAccessControlService(KalturaServiceBase):
    """Add & Manage Access Controls"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, accessControl):
        """Add new Access Control Profile"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("accessControl", accessControl)
        self.client.queueServiceActionCall("accesscontrol", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def get(self, id):
        """Get Access Control Profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("accesscontrol", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def update(self, id, accessControl):
        """Update Access Control Profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("accessControl", accessControl)
        self.client.queueServiceActionCall("accesscontrol", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def delete(self, id):
        """Delete Access Control Profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("accesscontrol", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Access Control Profiles by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("accesscontrol", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControlListResponse)


class KalturaAdminUserService(KalturaServiceBase):
    """Manage details for the administrative user"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def updatePassword(self, email, password, newEmail = "", newPassword = ""):
        """Update admin user password and email
        DEPRECATED"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("email", email)
        kparams.addStringIfDefined("password", password)
        kparams.addStringIfDefined("newEmail", newEmail)
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("adminuser", "updatePassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAdminUser)

    def resetPassword(self, email):
        """Reset admin user password and send it to the users email address"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("email", email)
        self.client.queueServiceActionCall("adminuser", "resetPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def login(self, email, password, partnerId = NotImplemented):
        """Get an admin session using admin email and password (Used for login to the KMC application)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("email", email)
        kparams.addStringIfDefined("password", password)
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("adminuser", "login", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def setInitialPassword(self, hashKey, newPassword):
        """Set initial users password"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("hashKey", hashKey)
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("adminuser", "setInitialPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaBaseEntryService(KalturaServiceBase):
    """Base Entry Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entry, type = NotImplemented):
        """Generic add entry, should be used when the uploaded entry type is not known"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("entry", entry)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("baseentry", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def addContent(self, entryId, resource):
        """Generic add entry, should be used when the uploaded entry type is not known"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("resource", resource)
        self.client.queueServiceActionCall("baseentry", "addContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def addFromUploadedFile(self, entry, uploadTokenId, type = NotImplemented):
        """Generic add entry using an uploaded file, should be used when the uploaded entry type is not known"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("entry", entry)
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("baseentry", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def get(self, entryId, version = -1):
        """Get base entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("baseentry", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getRemotePaths(self, entryId):
        """Get remote storage existing paths for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "getRemotePaths", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRemotePathListResponse)

    def update(self, entryId, baseEntry):
        """Update base entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("baseEntry", baseEntry)
        self.client.queueServiceActionCall("baseentry", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def updateContent(self, entryId, resource, conversionProfileId = NotImplemented):
        """Update base entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("resource", resource)
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        self.client.queueServiceActionCall("baseentry", "updateContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getByIds(self, entryIds):
        """Get base entry by comma separated entry ids."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryIds", entryIds)
        self.client.queueServiceActionCall("baseentry", "getByIds", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def delete(self, entryId):
        """Delete an entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List base entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("baseentry", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntryListResponse)

    def count(self, filter = NotImplemented):
        """Count base entries by filter."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("baseentry", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def upload(self, fileData):
        """Upload a file to Kaltura, that can be used to create an entry.
        DEPRECATED - use upload.upload or uploadToken.add instead"""

        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("baseentry", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateThumbnailJpeg(self, entryId, fileData):
        """Update entry thumbnail using a raw jpeg file"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("baseentry", "updateThumbnailJpeg", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def updateThumbnailFromUrl(self, entryId, url):
        """Update entry thumbnail using url"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("baseentry", "updateThumbnailFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def updateThumbnailFromSourceEntry(self, entryId, sourceEntryId, timeOffset):
        """Update entry thumbnail from a different entry by a specified time offset (In seconds)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("sourceEntryId", sourceEntryId)
        kparams.addIntIfDefined("timeOffset", timeOffset);
        self.client.queueServiceActionCall("baseentry", "updateThumbnailFromSourceEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def flag(self, moderationFlag):
        """Flag inappropriate entry for moderation"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("moderationFlag", moderationFlag)
        self.client.queueServiceActionCall("baseentry", "flag", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reject(self, entryId):
        """Reject the entry and mark the pending flags (if any) as moderated (this will make the entry non playable)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "reject", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def approve(self, entryId):
        """Approve the entry and mark the pending flags (if any) as moderated (this will make the entry playable)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "approve", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listFlags(self, entryId, pager = NotImplemented):
        """List all pending flags for the entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("baseentry", "listFlags", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaModerationFlagListResponse)

    def anonymousRank(self, entryId, rank):
        """Anonymously rank an entry, no validation is done on duplicate rankings"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("rank", rank);
        self.client.queueServiceActionCall("baseentry", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getContextData(self, entryId, contextDataParams):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("contextDataParams", contextDataParams)
        self.client.queueServiceActionCall("baseentry", "getContextData", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryContextDataResult)


class KalturaBulkUploadService(KalturaServiceBase):
    """Bulk upload service is used to upload & manage bulk uploads using CSV files"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, conversionProfileId, csvFileData, bulkUploadType = NotImplemented, uploadedBy = NotImplemented):
        """Add new bulk upload batch job
        Conversion profile id can be specified in the API or in the CSV file, the one in the CSV file will be stronger.
        If no conversion profile was specified, partner's default will be used"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        kfiles = KalturaFiles()
        kfiles.put("csvFileData", csvFileData);
        kparams.addStringIfDefined("bulkUploadType", bulkUploadType)
        kparams.addStringIfDefined("uploadedBy", uploadedBy)
        self.client.queueServiceActionCall("bulkupload", "add", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUpload)

    def get(self, id):
        """Get bulk upload batch job by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("bulkupload", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUpload)

    def list(self, pager = NotImplemented):
        """List bulk upload batch jobs"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("bulkupload", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUploadListResponse)

    def serve(self, id):
        """serve action returan the original file."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall('bulkupload', 'serve', kparams)
        return self.client.getServeUrl()

    def serveLog(self, id):
        """serveLog action returan the original file."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall('bulkupload', 'serveLog', kparams)
        return self.client.getServeUrl()

    def abort(self, id):
        """Aborts the bulk upload and all its child jobs"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("bulkupload", "abort", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUpload)


class KalturaCategoryService(KalturaServiceBase):
    """Add & Manage Categories"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, category):
        """Add new Category"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("category", category)
        self.client.queueServiceActionCall("category", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def get(self, id):
        """Get Category by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("category", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def update(self, id, category):
        """Update Category"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("category", category)
        self.client.queueServiceActionCall("category", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def delete(self, id):
        """Delete a Category"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("category", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented):
        """List all categories"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("category", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategoryListResponse)


class KalturaConversionProfileAssetParamsService(KalturaServiceBase):
    """Manage the connection between Conversion Profiles and Asset Params"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Lists asset parmas of conversion profile by ID"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("conversionprofileassetparams", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfileAssetParamsListResponse)

    def update(self, conversionProfileId, assetParamsId, conversionProfileAssetParams):
        """Update asset parmas of conversion profile by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        kparams.addIntIfDefined("assetParamsId", assetParamsId);
        kparams.addObjectIfDefined("conversionProfileAssetParams", conversionProfileAssetParams)
        self.client.queueServiceActionCall("conversionprofileassetparams", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfileAssetParams)


class KalturaConversionProfileService(KalturaServiceBase):
    """Add & Manage Conversion Profiles"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def setAsDefault(self, id):
        """Set Conversion Profile to be the partner default"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("conversionprofile", "setAsDefault", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def getDefault(self):
        """Get the partner's default conversion profile"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("conversionprofile", "getDefault", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def add(self, conversionProfile):
        """Add new Conversion Profile"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("conversionProfile", conversionProfile)
        self.client.queueServiceActionCall("conversionprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def get(self, id):
        """Get Conversion Profile by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("conversionprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def update(self, id, conversionProfile):
        """Update Conversion Profile by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("conversionProfile", conversionProfile)
        self.client.queueServiceActionCall("conversionprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def delete(self, id):
        """Delete Conversion Profile by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("conversionprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Conversion Profiles by filter with paging support"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("conversionprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfileListResponse)


class KalturaDataService(KalturaServiceBase):
    """Data service lets you manage data content (textual content)"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, dataEntry):
        """Adds a new data entry"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("dataEntry", dataEntry)
        self.client.queueServiceActionCall("data", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def get(self, entryId, version = -1):
        """Get data entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("data", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def update(self, entryId, documentEntry):
        """Update data entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        self.client.queueServiceActionCall("data", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def delete(self, entryId):
        """Delete a data entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("data", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List data entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("data", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataListResponse)

    def serve(self, entryId, version = -1, forceProxy = False):
        """serve action returan the file from dataContent field."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        kparams.addBoolIfDefined("forceProxy", forceProxy);
        self.client.queueServiceActionCall('data', 'serve', kparams)
        return self.client.getServeUrl()


class KalturaDocumentService(KalturaServiceBase):
    """Document service
    DEPRECATED"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def addFromUploadedFile(self, documentEntry, uploadTokenId):
        """Add new document entry after the specific document file was uploaded and the upload token id exists"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("document", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromEntry(self, sourceEntryId, documentEntry = NotImplemented, sourceFlavorParamsId = NotImplemented):
        """Copy entry into new entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceEntryId", sourceEntryId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        kparams.addIntIfDefined("sourceFlavorParamsId", sourceFlavorParamsId);
        self.client.queueServiceActionCall("document", "addFromEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def addFromFlavorAsset(self, sourceFlavorAssetId, documentEntry = NotImplemented):
        """Copy flavor asset into new entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceFlavorAssetId", sourceFlavorAssetId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document", "addFromFlavorAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def convert(self, entryId, conversionProfileId = NotImplemented, dynamicConversionAttributes = NotImplemented):
        """Convert entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        kparams.addArrayIfDefined("dynamicConversionAttributes", dynamicConversionAttributes)
        self.client.queueServiceActionCall("document", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def get(self, entryId, version = -1):
        """Get document entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("document", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def update(self, entryId, documentEntry):
        """Update document entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("documentEntry", documentEntry)
        self.client.queueServiceActionCall("document", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentEntry)

    def delete(self, entryId):
        """Delete a document entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("document", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List document entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("document", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDocumentListResponse)

    def upload(self, fileData):
        """Upload a document file to Kaltura, then the file can be used to create a document entry.
        DEPRECATED - use upload.upload or uploadToken.add instead"""

        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("document", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def convertPptToSwf(self, entryId):
        """This will queue a batch job for converting the document file to swf
        Returns the URL where the new swf will be available"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("document", "convertPptToSwf", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def serve(self, entryId, flavorAssetId = NotImplemented, forceProxy = False):
        """Serves the file content"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("flavorAssetId", flavorAssetId)
        kparams.addBoolIfDefined("forceProxy", forceProxy);
        self.client.queueServiceActionCall('document', 'serve', kparams)
        return self.client.getServeUrl()

    def serveByFlavorParamsId(self, entryId, flavorParamsId = NotImplemented, forceProxy = False):
        """Serves the file content"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("flavorParamsId", flavorParamsId)
        kparams.addBoolIfDefined("forceProxy", forceProxy);
        self.client.queueServiceActionCall('document', 'serveByFlavorParamsId', kparams)
        return self.client.getServeUrl()


class KalturaEmailIngestionProfileService(KalturaServiceBase):
    """EmailIngestionProfile service lets you manage email ingestion profile records"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, EmailIP):
        """EmailIngestionProfile Add action allows you to add a EmailIngestionProfile to Kaltura DB"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("EmailIP", EmailIP)
        self.client.queueServiceActionCall("emailingestionprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def getByEmailAddress(self, emailAddress):
        """Retrieve a EmailIngestionProfile by email address"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("emailAddress", emailAddress)
        self.client.queueServiceActionCall("emailingestionprofile", "getByEmailAddress", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def get(self, id):
        """Retrieve a EmailIngestionProfile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("emailingestionprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def update(self, id, EmailIP):
        """Update an existing EmailIngestionProfile"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("EmailIP", EmailIP)
        self.client.queueServiceActionCall("emailingestionprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def delete(self, id):
        """Delete an existing EmailIngestionProfile"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("emailingestionprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def addMediaEntry(self, mediaEntry, uploadTokenId, emailProfId, fromAddress, emailMsgId):
        """add KalturaMediaEntry from email ingestion"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        kparams.addIntIfDefined("emailProfId", emailProfId);
        kparams.addStringIfDefined("fromAddress", fromAddress)
        kparams.addStringIfDefined("emailMsgId", emailMsgId)
        self.client.queueServiceActionCall("emailingestionprofile", "addMediaEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)


class KalturaFlavorAssetService(KalturaServiceBase):
    """Retrieve information and invoke actions on Flavor Asset"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, flavorAsset):
        """Add flavor asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("flavorAsset", flavorAsset)
        self.client.queueServiceActionCall("flavorasset", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAsset)

    def update(self, id, flavorAsset):
        """Update flavor asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("flavorAsset", flavorAsset)
        self.client.queueServiceActionCall("flavorasset", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAsset)

    def setContent(self, id, contentResource):
        """Update content of flavor asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("contentResource", contentResource)
        self.client.queueServiceActionCall("flavorasset", "setContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAsset)

    def get(self, id):
        """Get Flavor Asset by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("flavorasset", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAsset)

    def getByEntryId(self, entryId):
        """Get Flavor Assets for Entry
        DEPRECATED - Use thumbAsset.list instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAsset)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Flavor Assets by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("flavorasset", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAssetListResponse)

    def getWebPlayableByEntryId(self, entryId):
        """Get web playable Flavor Assets for Entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getWebPlayableByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAsset)

    def convert(self, entryId, flavorParamsId):
        """Add and convert new Flavor Asset for Entry with specific Flavor Params"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("flavorParamsId", flavorParamsId);
        self.client.queueServiceActionCall("flavorasset", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reconvert(self, id):
        """Reconvert Flavor Asset by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("flavorasset", "reconvert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def delete(self, id):
        """Delete Flavor Asset by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("flavorasset", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getUrl(self, id, storageId = NotImplemented):
        """Get download URL for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addIntIfDefined("storageId", storageId);
        self.client.queueServiceActionCall("flavorasset", "getUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getRemotePaths(self, id):
        """Get remote storage existing paths for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("flavorasset", "getRemotePaths", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRemotePathListResponse)

    def getDownloadUrl(self, id, useCdn = False):
        """Get download URL for the Flavor Asset
        DEPRECATED - use getUrl instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addBoolIfDefined("useCdn", useCdn);
        self.client.queueServiceActionCall("flavorasset", "getDownloadUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getFlavorAssetsWithParams(self, entryId):
        """Get Flavor Asset with the relevant Flavor Params (Flavor Params can exist without Flavor Asset & vice versa)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getFlavorAssetsWithParams", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAssetWithParams)


class KalturaFlavorParamsService(KalturaServiceBase):
    """Add & Manage Flavor Params"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, flavorParams):
        """Add new Flavor Params"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("flavorParams", flavorParams)
        self.client.queueServiceActionCall("flavorparams", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def get(self, id):
        """Get Flavor Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("flavorparams", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def update(self, id, flavorParams):
        """Update Flavor Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("flavorParams", flavorParams)
        self.client.queueServiceActionCall("flavorparams", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def delete(self, id):
        """Delete Flavor Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("flavorparams", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Flavor Params by filter with paging support (By default - all system default params will be listed too)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("flavorparams", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParamsListResponse)

    def getByConversionProfileId(self, conversionProfileId):
        """Get Flavor Params by Conversion Profile ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        self.client.queueServiceActionCall("flavorparams", "getByConversionProfileId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorParams)


class KalturaLiveStreamService(KalturaServiceBase):
    """Live Stream service lets you manage live stream channels"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, liveStreamEntry, sourceType = NotImplemented):
        """Adds new live stream entry.
        The entry will be queued for provision."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("liveStreamEntry", liveStreamEntry)
        kparams.addStringIfDefined("sourceType", sourceType)
        self.client.queueServiceActionCall("livestream", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamAdminEntry)

    def get(self, entryId, version = -1):
        """Get live stream entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("livestream", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)

    def update(self, entryId, liveStreamEntry):
        """Update live stream entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("liveStreamEntry", liveStreamEntry)
        self.client.queueServiceActionCall("livestream", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamAdminEntry)

    def delete(self, entryId):
        """Delete a live stream entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("livestream", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List live stream entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("livestream", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamListResponse)

    def updateOfflineThumbnailJpeg(self, entryId, fileData):
        """Update live stream entry thumbnail using a raw jpeg file"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("livestream", "updateOfflineThumbnailJpeg", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)

    def updateOfflineThumbnailFromUrl(self, entryId, url):
        """Update entry thumbnail using url"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("livestream", "updateOfflineThumbnailFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)


class KalturaMediaInfoService(KalturaServiceBase):
    """Media Info service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List media info objects by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("mediainfo", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaInfoListResponse)


class KalturaMediaService(KalturaServiceBase):
    """Media service lets you upload and manage media files (images / videos & audio)"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entry):
        """Add entry"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("entry", entry)
        self.client.queueServiceActionCall("media", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addContent(self, entryId, resource = NotImplemented):
        """Add content to entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("resource", resource)
        self.client.queueServiceActionCall("media", "addContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromUrl(self, mediaEntry, url):
        """Adds new media entry by importing an HTTP or FTP URL.
        The entry will be queued for import and then for conversion.
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("media", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromSearchResult(self, mediaEntry = NotImplemented, searchResult = NotImplemented):
        """Adds new media entry by importing the media file from a search provider. 
        This action should be used with the search service result.
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addObjectIfDefined("searchResult", searchResult)
        self.client.queueServiceActionCall("media", "addFromSearchResult", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromUploadedFile(self, mediaEntry, uploadTokenId):
        """Add new entry after the specific media file was uploaded and the upload token id exists
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("media", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromRecordedWebcam(self, mediaEntry, webcamTokenId):
        """Add new entry after the file was recored on the server and the token id exists
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addStringIfDefined("webcamTokenId", webcamTokenId)
        self.client.queueServiceActionCall("media", "addFromRecordedWebcam", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromEntry(self, sourceEntryId, mediaEntry = NotImplemented, sourceFlavorParamsId = NotImplemented):
        """Copy entry into new entry
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceEntryId", sourceEntryId)
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        kparams.addIntIfDefined("sourceFlavorParamsId", sourceFlavorParamsId);
        self.client.queueServiceActionCall("media", "addFromEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromFlavorAsset(self, sourceFlavorAssetId, mediaEntry = NotImplemented):
        """Copy flavor asset into new entry
        DEPRECATED - use media.add instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("sourceFlavorAssetId", sourceFlavorAssetId)
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        self.client.queueServiceActionCall("media", "addFromFlavorAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def convert(self, entryId, conversionProfileId = NotImplemented, dynamicConversionAttributes = NotImplemented):
        """Convert entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        kparams.addArrayIfDefined("dynamicConversionAttributes", dynamicConversionAttributes)
        self.client.queueServiceActionCall("media", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def get(self, entryId, version = -1):
        """Get media entry by ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("media", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def update(self, entryId, mediaEntry):
        """Update media entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("mediaEntry", mediaEntry)
        self.client.queueServiceActionCall("media", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def updateContent(self, entryId, resource, conversionProfileId = NotImplemented):
        """Replace media content of the entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("resource", resource)
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        self.client.queueServiceActionCall("media", "updateContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def delete(self, entryId):
        """Delete a media entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("media", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def approveReplace(self, entryId):
        """Approves media replacement"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("media", "approveReplace", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def cancelReplace(self, entryId):
        """Cancels media replacement"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("media", "cancelReplace", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List media entries by filter with paging support."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("media", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaListResponse)

    def count(self, filter = NotImplemented):
        """Count media entries by filter."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("media", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def upload(self, fileData):
        """Upload a media file to Kaltura, then the file can be used to create a media entry.
        DEPRECATED - use upload.upload or uploadToken.add instead"""

        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("media", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateThumbnail(self, entryId, timeOffset, flavorParamsId = NotImplemented):
        """Update media entry thumbnail by a specified time offset (In seconds)
        If flavor params id not specified, source flavor will be used by default
        DEPRECATED"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("timeOffset", timeOffset);
        kparams.addIntIfDefined("flavorParamsId", flavorParamsId);
        self.client.queueServiceActionCall("media", "updateThumbnail", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def updateThumbnailFromSourceEntry(self, entryId, sourceEntryId, timeOffset, flavorParamsId = NotImplemented):
        """Update media entry thumbnail from a different entry by a specified time offset (In seconds)
        If flavor params id not specified, source flavor will be used by default
        DEPRECATED"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("sourceEntryId", sourceEntryId)
        kparams.addIntIfDefined("timeOffset", timeOffset);
        kparams.addIntIfDefined("flavorParamsId", flavorParamsId);
        self.client.queueServiceActionCall("media", "updateThumbnailFromSourceEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def updateThumbnailJpeg(self, entryId, fileData):
        """Update media entry thumbnail using a raw jpeg file
        DEPRECATED"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("media", "updateThumbnailJpeg", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def updateThumbnailFromUrl(self, entryId, url):
        """Update entry thumbnail using url
        DEPRECATED"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("media", "updateThumbnailFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def requestConversion(self, entryId, fileFormat):
        """Request a new conversion job, this can be used to convert the media entry to a different format"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("fileFormat", fileFormat)
        self.client.queueServiceActionCall("media", "requestConversion", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def flag(self, moderationFlag):
        """Flag inappropriate media entry for moderation"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("moderationFlag", moderationFlag)
        self.client.queueServiceActionCall("media", "flag", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reject(self, entryId):
        """Reject the media entry and mark the pending flags (if any) as moderated (this will make the entry non playable)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("media", "reject", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def approve(self, entryId):
        """Approve the media entry and mark the pending flags (if any) as moderated (this will make the entry playable)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("media", "approve", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listFlags(self, entryId, pager = NotImplemented):
        """List all pending flags for the media entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("media", "listFlags", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaModerationFlagListResponse)

    def anonymousRank(self, entryId, rank):
        """Anonymously rank a media entry, no validation is done on duplicate rankings"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("rank", rank);
        self.client.queueServiceActionCall("media", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaMixingService(KalturaServiceBase):
    """A Mix is an XML unique format invented by Kaltura, it allows the user to create a mix of videos and images, in and out points, transitions, text overlays, soundtrack, effects and much more...
    Mixing service lets you create a new mix, manage its metadata and make basic manipulations."""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, mixEntry):
        """Adds a new mix.
        If the dataContent is null, a default timeline will be created."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("mixEntry", mixEntry)
        self.client.queueServiceActionCall("mixing", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def get(self, entryId, version = -1):
        """Get mix entry by id."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("mixing", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def update(self, entryId, mixEntry):
        """Update mix entry. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("mixEntry", mixEntry)
        self.client.queueServiceActionCall("mixing", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def delete(self, entryId):
        """Delete a mix entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("mixing", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List entries by filter with paging support.
        Return parameter is an array of mix entries."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("mixing", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixListResponse)

    def count(self, filter = NotImplemented):
        """Count mix entries by filter."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("mixing", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def clone(self, entryId):
        """Clones an existing mix."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("mixing", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def appendMediaEntry(self, mixEntryId, mediaEntryId):
        """Appends a media entry to a the end of the mix timeline, this will save the mix timeline as a new version."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("mixEntryId", mixEntryId)
        kparams.addStringIfDefined("mediaEntryId", mediaEntryId)
        self.client.queueServiceActionCall("mixing", "appendMediaEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def requestFlattening(self, entryId, fileFormat, version = -1):
        """Request a new flattening job, flattening is used to convert a video mix to a video file."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("fileFormat", fileFormat)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("mixing", "requestFlattening", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def getMixesByMediaId(self, mediaEntryId):
        """Get the mixes in which the media entry is included"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("mediaEntryId", mediaEntryId)
        self.client.queueServiceActionCall("mixing", "getMixesByMediaId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaMixEntry)

    def getReadyMediaEntries(self, mixId, version = -1):
        """Get all ready media entries that exist in the given mix id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("mixId", mixId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("mixing", "getReadyMediaEntries", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaMediaEntry)

    def anonymousRank(self, entryId, rank):
        """Anonymously rank a mix entry, no validation is done on duplicate rankings"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("rank", rank);
        self.client.queueServiceActionCall("mixing", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaNotificationService(KalturaServiceBase):
    """Notification Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getClientNotification(self, entryId, type):
        """Return the notifications for a specific entry id and type"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("type", type);
        self.client.queueServiceActionCall("notification", "getClientNotification", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaClientNotification)


class KalturaPartnerService(KalturaServiceBase):
    """partner service allows you to change/manage your partner personal details and settings as well"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def register(self, partner, cmsPassword = ""):
        """Register to Kaltura's partner program"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("partner", partner)
        kparams.addStringIfDefined("cmsPassword", cmsPassword)
        self.client.queueServiceActionCall("partner", "register", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def update(self, partner, allowEmpty = False):
        """Update details and settings of you existing partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("partner", partner)
        kparams.addBoolIfDefined("allowEmpty", allowEmpty);
        self.client.queueServiceActionCall("partner", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getSecrets(self, partnerId, adminEmail, cmsPassword):
        """Retrieve partner secret and admin secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("adminEmail", adminEmail)
        kparams.addStringIfDefined("cmsPassword", cmsPassword)
        self.client.queueServiceActionCall("partner", "getSecrets", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getInfo(self):
        """Retrieve all info about partner
        This service gets no parameters, and is using the KS to know which partnerId info should be returned"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("partner", "getInfo", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getUsage(self, year = "", month = 1, resolution = "days"):
        """Get usage statistics for a partner
        Calculation is done according to partner's package
        Additional data returned is a graph points of streaming usage in a timeframe
        The resolution can be "days" or "months" """

        kparams = KalturaParams()
        kparams.addIntIfDefined("year", year);
        kparams.addIntIfDefined("month", month);
        kparams.addStringIfDefined("resolution", resolution)
        self.client.queueServiceActionCall("partner", "getUsage", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartnerUsage)


class KalturaPermissionItemService(KalturaServiceBase):
    """PermissionItem service lets you create and manage permission items"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, permissionItem):
        """Allows you to add a new KalturaPermissionItem object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("permissionItem", permissionItem)
        self.client.queueServiceActionCall("permissionitem", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def get(self, permissionItemId):
        """Retrieve a KalturaPermissionItem object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("permissionItemId", permissionItemId);
        self.client.queueServiceActionCall("permissionitem", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def update(self, permissionItemId, permissionItem):
        """Update an existing KalturaPermissionItem object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("permissionItemId", permissionItemId);
        kparams.addObjectIfDefined("permissionItem", permissionItem)
        self.client.queueServiceActionCall("permissionitem", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def delete(self, permissionItemId):
        """Mark the KalturaPermissionItem object as deleted"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("permissionItemId", permissionItemId);
        self.client.queueServiceActionCall("permissionitem", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaPermissionItem objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("permissionitem", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItemListResponse)


class KalturaPermissionService(KalturaServiceBase):
    """Permission service lets you create and manage user permissions"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, permission):
        """Allows you to add a new KalturaPermission object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("permission", permission)
        self.client.queueServiceActionCall("permission", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def get(self, permissionName):
        """Retrieve a KalturaPermission object by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("permissionName", permissionName)
        self.client.queueServiceActionCall("permission", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def update(self, permissionName, permission):
        """Update an existing KalturaPermission object"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("permissionName", permissionName)
        kparams.addObjectIfDefined("permission", permission)
        self.client.queueServiceActionCall("permission", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def delete(self, permissionName):
        """Mark the KalturaPermission object as deleted"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("permissionName", permissionName)
        self.client.queueServiceActionCall("permission", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaPermission objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("permission", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionListResponse)

    def getCurrentPermissions(self):
        """Return a list of current sessions's allowed permission names"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("permission", "getCurrentPermissions", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


class KalturaPlaylistService(KalturaServiceBase):
    """Playlist service lets you create,manage and play your playlists
    Playlists could be static (containing a fixed list of entries) or dynamic (baseed on a filter)"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, playlist, updateStats = False):
        """Add new playlist
        Note that all entries used in a playlist will become public and may appear in KalturaNetwork"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("playlist", playlist)
        kparams.addBoolIfDefined("updateStats", updateStats);
        self.client.queueServiceActionCall("playlist", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def get(self, id, version = -1):
        """Retrieve a playlist"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("playlist", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def update(self, id, playlist, updateStats = False):
        """Update existing playlist
        Note - you cannot change playlist type. updated playlist must be of the same type."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("playlist", playlist)
        kparams.addBoolIfDefined("updateStats", updateStats);
        self.client.queueServiceActionCall("playlist", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def delete(self, id):
        """Delete existing playlist"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("playlist", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def clone(self, id, newPlaylist = NotImplemented):
        """Clone an existing playlist"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("newPlaylist", newPlaylist)
        self.client.queueServiceActionCall("playlist", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List available playlists"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("playlist", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylistListResponse)

    def execute(self, id, detailed = ""):
        """Retrieve playlist for playing purpose"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addStringIfDefined("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "execute", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def executeFromContent(self, playlistType, playlistContent, detailed = ""):
        """Retrieve playlist for playing purpose, based on content"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("playlistType", playlistType);
        kparams.addStringIfDefined("playlistContent", playlistContent)
        kparams.addStringIfDefined("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "executeFromContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def executeFromFilters(self, filters, totalResults, detailed = ""):
        """Revrieve playlist for playing purpose, based on media entry filters"""

        kparams = KalturaParams()
        kparams.addArrayIfDefined("filters", filters)
        kparams.addIntIfDefined("totalResults", totalResults);
        kparams.addStringIfDefined("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "executeFromFilters", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def getStatsFromContent(self, playlistType, playlistContent):
        """Retrieve playlist statistics"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("playlistType", playlistType);
        kparams.addStringIfDefined("playlistContent", playlistContent)
        self.client.queueServiceActionCall("playlist", "getStatsFromContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)


class KalturaReportService(KalturaServiceBase):
    """api for getting reports data by the report type and some inputFilter"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getGraphs(self, reportType, reportInputFilter, dimension = NotImplemented, objectIds = NotImplemented):
        """report getGraphs action allows to get a graph data for a specific report."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("reportType", reportType);
        kparams.addObjectIfDefined("reportInputFilter", reportInputFilter)
        kparams.addStringIfDefined("dimension", dimension)
        kparams.addStringIfDefined("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getGraphs", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaReportGraph)

    def getTotal(self, reportType, reportInputFilter, objectIds = NotImplemented):
        """report getTotal action allows to get a graph data for a specific report."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("reportType", reportType);
        kparams.addObjectIfDefined("reportInputFilter", reportInputFilter)
        kparams.addStringIfDefined("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getTotal", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportTotal)

    def getTable(self, reportType, reportInputFilter, pager, order = NotImplemented, objectIds = NotImplemented):
        """report getTable action allows to get a graph data for a specific report."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("reportType", reportType);
        kparams.addObjectIfDefined("reportInputFilter", reportInputFilter)
        kparams.addObjectIfDefined("pager", pager)
        kparams.addStringIfDefined("order", order)
        kparams.addStringIfDefined("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getTable", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportTable)

    def getUrlForReportAsCsv(self, reportTitle, reportText, headers, reportType, reportInputFilter, dimension = NotImplemented, pager = NotImplemented, order = NotImplemented, objectIds = NotImplemented):
        """will create a Csv file for the given report and return the URL to access it"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("reportTitle", reportTitle)
        kparams.addStringIfDefined("reportText", reportText)
        kparams.addStringIfDefined("headers", headers)
        kparams.addIntIfDefined("reportType", reportType);
        kparams.addObjectIfDefined("reportInputFilter", reportInputFilter)
        kparams.addStringIfDefined("dimension", dimension)
        kparams.addObjectIfDefined("pager", pager)
        kparams.addStringIfDefined("order", order)
        kparams.addStringIfDefined("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getUrlForReportAsCsv", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def execute(self, id, params = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addArrayIfDefined("params", params)
        self.client.queueServiceActionCall("report", "execute", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportResponse)

    def getCsv(self, id, params = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addArrayIfDefined("params", params)
        self.client.queueServiceActionCall('report', 'getCsv', kparams)
        return self.client.getServeUrl()


class KalturaSchemaService(KalturaServiceBase):
    """Expose the schema definitions for syndication MRSS, bulk upload XML and other schema types."""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def serve(self, type):
        """Serves the requested XSD according to the type and name."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall('schema', 'serve', kparams)
        return self.client.getServeUrl()


class KalturaSearchService(KalturaServiceBase):
    """Search service allows you to search for media in various media providers
    This service is being used mostly by the CW component"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def search(self, search, pager = NotImplemented):
        """Search for media in one of the supported media providers"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("search", search)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("search", "search", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResultResponse)

    def getMediaInfo(self, searchResult):
        """Retrieve extra information about media found in search action
        Some providers return only part of the fields needed to create entry from, use this action to get the rest of the fields."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchResult", searchResult)
        self.client.queueServiceActionCall("search", "getMediaInfo", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResult)

    def searchUrl(self, mediaType, url):
        """Search for media given a specific URL
        Kaltura supports a searchURL action on some of the media providers.
        This action will return a KalturaSearchResult object based on a given URL (assuming the media provider is supported)"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("mediaType", mediaType);
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("search", "searchUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResult)

    def externalLogin(self, searchSource, userName, password):
        kparams = KalturaParams()
        kparams.addIntIfDefined("searchSource", searchSource);
        kparams.addStringIfDefined("userName", userName)
        kparams.addStringIfDefined("password", password)
        self.client.queueServiceActionCall("search", "externalLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchAuthData)


class KalturaSessionService(KalturaServiceBase):
    """Session service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def start(self, secret, userId = "", type = 0, partnerId = NotImplemented, expiry = 86400, privileges = NotImplemented):
        """Start a session with Kaltura's server.
        The result KS is the session key that you should pass to all services that requires a ticket."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("secret", secret)
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("type", type);
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("expiry", expiry);
        kparams.addStringIfDefined("privileges", privileges)
        self.client.queueServiceActionCall("session", "start", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def end(self):
        """End a session with the Kaltura server, making the current KS invalid."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("session", "end", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def impersonate(self, secret, impersonatedPartnerId, userId = "", type = 0, partnerId = NotImplemented, expiry = 86400, privileges = NotImplemented):
        """Start an impersonated session with Kaltura's server.
        The result KS is the session key that you should pass to all services that requires a ticket."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("secret", secret)
        kparams.addIntIfDefined("impersonatedPartnerId", impersonatedPartnerId);
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("type", type);
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("expiry", expiry);
        kparams.addStringIfDefined("privileges", privileges)
        self.client.queueServiceActionCall("session", "impersonate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def startWidgetSession(self, widgetId, expiry = 86400):
        """Start a session for Kaltura's flash widgets"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("widgetId", widgetId)
        kparams.addIntIfDefined("expiry", expiry);
        self.client.queueServiceActionCall("session", "startWidgetSession", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStartWidgetSessionResponse)


class KalturaStatsService(KalturaServiceBase):
    """Stats Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def collect(self, event):
        """Will write to the event log a single line representing the event
        KalturaStatsEvent $event"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("event", event)
        self.client.queueServiceActionCall("stats", "collect", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def kmcCollect(self, kmcEvent):
        """Will collect the kmcEvent sent form the KMC client"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("kmcEvent", kmcEvent)
        self.client.queueServiceActionCall("stats", "kmcCollect", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reportKceError(self, kalturaCEError):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("kalturaCEError", kalturaCEError)
        self.client.queueServiceActionCall("stats", "reportKceError", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCEError)


class KalturaStorageProfileService(KalturaServiceBase):
    """Storage Profiles service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, storageProfile):
        """Adds a storage profile to the Kaltura DB."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("storageProfile", storageProfile)
        self.client.queueServiceActionCall("storageprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

    def updateStatus(self, storageId, status):
        kparams = KalturaParams()
        kparams.addIntIfDefined("storageId", storageId);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("storageprofile", "updateStatus", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, storageProfileId):
        """Get storage profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("storageProfileId", storageProfileId);
        self.client.queueServiceActionCall("storageprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

    def update(self, storageProfileId, storageProfile):
        """Update storage profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("storageProfileId", storageProfileId);
        kparams.addObjectIfDefined("storageProfile", storageProfile)
        self.client.queueServiceActionCall("storageprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfile)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("storageprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStorageProfileListResponse)


class KalturaSyndicationFeedService(KalturaServiceBase):
    """Add & Manage Syndication Feeds"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, syndicationFeed):
        """Add new Syndication Feed"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("syndicationFeed", syndicationFeed)
        self.client.queueServiceActionCall("syndicationfeed", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def get(self, id):
        """Get Syndication Feed by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("syndicationfeed", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def update(self, id, syndicationFeed):
        """Update Syndication Feed by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("syndicationFeed", syndicationFeed)
        self.client.queueServiceActionCall("syndicationfeed", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def delete(self, id):
        """Delete Syndication Feed by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("syndicationfeed", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Syndication Feeds by filter with paging support"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("syndicationfeed", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeedListResponse)

    def getEntryCount(self, feedId):
        """get entry count for a syndication feed"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("feedId", feedId)
        self.client.queueServiceActionCall("syndicationfeed", "getEntryCount", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSyndicationFeedEntryCount)

    def requestConversion(self, feedId):
        """request conversion for all entries that doesnt have the required flavor param
        returns a comma-separated ids of conversion jobs
        @action requestConversion
        @param string $feedId
        @return string"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("feedId", feedId)
        self.client.queueServiceActionCall("syndicationfeed", "requestConversion", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


class KalturaSystemService(KalturaServiceBase):
    """System service is used for internal system helpers & to retrieve system level information"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def ping(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("system", "ping", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


class KalturaThumbAssetService(KalturaServiceBase):
    """Retrieve information and invoke actions on Thumb Asset"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, thumbAsset):
        """Add thumbnail asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("thumbAsset", thumbAsset)
        self.client.queueServiceActionCall("thumbasset", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def setContent(self, id, contentResource):
        """Update content of thumbnail asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("contentResource", contentResource)
        self.client.queueServiceActionCall("thumbasset", "setContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def update(self, id, thumbAsset):
        """Update thumbnail asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("thumbAsset", thumbAsset)
        self.client.queueServiceActionCall("thumbasset", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def serveByEntryId(self, entryId, thumbParamId = NotImplemented):
        """Serves thumbnail by entry id and thumnail params id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("thumbParamId", thumbParamId);
        self.client.queueServiceActionCall('thumbasset', 'serveByEntryId', kparams)
        return self.client.getServeUrl()

    def serve(self, thumbAssetId):
        """Serves thumbnail by its id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall('thumbasset', 'serve', kparams)
        return self.client.getServeUrl()

    def setAsDefault(self, thumbAssetId):
        """Tags the thumbnail as DEFAULT_THUMB and removes that tag from all other thumbnail assets of the entry.
        Create a new file sync link on the entry thumbnail that points to the thumbnail asset file sync."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "setAsDefault", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def generateByEntryId(self, entryId, destThumbParamsId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("destThumbParamsId", destThumbParamsId);
        self.client.queueServiceActionCall("thumbasset", "generateByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def generate(self, entryId, thumbParams, sourceAssetId = NotImplemented):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("thumbParams", thumbParams)
        kparams.addStringIfDefined("sourceAssetId", sourceAssetId)
        self.client.queueServiceActionCall("thumbasset", "generate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def regenerate(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "regenerate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def get(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def getByEntryId(self, entryId):
        """DEPRECATED - Use thumbAsset.list instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("thumbasset", "getByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaThumbAsset)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Thumbnail Assets by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("thumbasset", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAssetListResponse)

    def addFromUrl(self, entryId, url):
        """DEPRECATED - use thumbAsset.add and thumbAsset.setContent instead"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("url", url)
        self.client.queueServiceActionCall("thumbasset", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def addFromImage(self, entryId, fileData):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("thumbasset", "addFromImage", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def delete(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getUrl(self, id, storageId = NotImplemented):
        """Get download URL for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addIntIfDefined("storageId", storageId);
        self.client.queueServiceActionCall("thumbasset", "getUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getRemotePaths(self, id):
        """Get remote storage existing paths for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("thumbasset", "getRemotePaths", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRemotePathListResponse)


class KalturaThumbParamsService(KalturaServiceBase):
    """Add & Manage Thumb Params"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, thumbParams):
        """Add new Thumb Params"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("thumbParams", thumbParams)
        self.client.queueServiceActionCall("thumbparams", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def get(self, id):
        """Get Thumb Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("thumbparams", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def update(self, id, thumbParams):
        """Update Thumb Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("thumbParams", thumbParams)
        self.client.queueServiceActionCall("thumbparams", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def delete(self, id):
        """Delete Thumb Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("thumbparams", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Thumb Params by filter with paging support (By default - all system default params will be listed too)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("thumbparams", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParamsListResponse)

    def getByConversionProfileId(self, conversionProfileId):
        """Get Thumb Params by Conversion Profile ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("conversionProfileId", conversionProfileId);
        self.client.queueServiceActionCall("thumbparams", "getByConversionProfileId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaThumbParams)


class KalturaUiConfService(KalturaServiceBase):
    """UiConf service lets you create and manage your UIConfs for the various flash components
    This service is used by the KMC-ApplicationStudio"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uiConf):
        """UIConf Add action allows you to add a UIConf to Kaltura DB"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("uiConf", uiConf)
        self.client.queueServiceActionCall("uiconf", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def update(self, id, uiConf):
        """Update an existing UIConf"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("uiConf", uiConf)
        self.client.queueServiceActionCall("uiconf", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def get(self, id):
        """Retrieve a UIConf by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("uiconf", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def delete(self, id):
        """Delete an existing UIConf"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("uiconf", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def clone(self, id):
        """Clone an existing UIConf"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("uiconf", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def listTemplates(self, filter = NotImplemented, pager = NotImplemented):
        """retrieve a list of available template UIConfs"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("uiconf", "listTemplates", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfListResponse)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Retrieve a list of available UIConfs"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("uiconf", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfListResponse)

    def getAvailableTypes(self):
        """Retrieve a list of all available versions by object type"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("uiconf", "getAvailableTypes", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaUiConfTypeInfo)


class KalturaUploadService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def upload(self, fileData):
        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        self.client.queueServiceActionCall("upload", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getUploadedFileTokenByFileName(self, fileName):
        kparams = KalturaParams()
        kparams.addStringIfDefined("fileName", fileName)
        self.client.queueServiceActionCall("upload", "getUploadedFileTokenByFileName", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadResponse)


class KalturaUploadTokenService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uploadToken = NotImplemented):
        """Adds new upload token to upload a file"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("uploadToken", uploadToken)
        self.client.queueServiceActionCall("uploadtoken", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def get(self, uploadTokenId):
        """Get upload token by id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("uploadtoken", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def upload(self, uploadTokenId, fileData, resume = False, finalChunk = True, resumeAt = -1):
        """Upload a file using the upload token id, returns an error on failure (an exception will be thrown when using one of the Kaltura clients)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData);
        kparams.addBoolIfDefined("resume", resume);
        kparams.addBoolIfDefined("finalChunk", finalChunk);
        kparams.addIntIfDefined("resumeAt", resumeAt);
        self.client.queueServiceActionCall("uploadtoken", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def delete(self, uploadTokenId):
        """Deletes the upload token by upload token id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("uploadtoken", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List upload token by filter with pager support. 
        When using a user session the service will be restricted to users objects only."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("uploadtoken", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadTokenListResponse)


class KalturaUserRoleService(KalturaServiceBase):
    """UserRole service lets you create and manage user roles"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, userRole):
        """Allows you to add a new KalturaUserRole object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("userRole", userRole)
        self.client.queueServiceActionCall("userrole", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def get(self, userRoleId):
        """Retrieve a KalturaUserRole object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("userRoleId", userRoleId);
        self.client.queueServiceActionCall("userrole", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def update(self, userRoleId, userRole):
        """Update an existing KalturaUserRole object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("userRoleId", userRoleId);
        kparams.addObjectIfDefined("userRole", userRole)
        self.client.queueServiceActionCall("userrole", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def delete(self, userRoleId):
        """Mark the KalturaUserRole object as deleted"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("userRoleId", userRoleId);
        self.client.queueServiceActionCall("userrole", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List user roles"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("userrole", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRoleListResponse)

    def clone(self, userRoleId):
        """Clone role"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("userRoleId", userRoleId);
        self.client.queueServiceActionCall("userrole", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)


class KalturaUserService(KalturaServiceBase):
    """Manage partner users on Kaltura's side
    The userId in kaltura is the unique Id in the partner's system, and the [partnerId,Id] couple are unique key in kaltura's DB"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, user):
        """Adds a user to the Kaltura DB.
        Input param $id is the unique identifier in the partner's system"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("user", user)
        self.client.queueServiceActionCall("user", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def update(self, userId, user):
        """Update existing user, it is possible to update the user id too"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addObjectIfDefined("user", user)
        self.client.queueServiceActionCall("user", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def get(self, userId):
        """Get user by user ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("user", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def getByLoginId(self, loginId):
        """Get user by user's login ID and partner ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("loginId", loginId)
        self.client.queueServiceActionCall("user", "getByLoginId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def delete(self, userId):
        """Mark the user as deleted"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("user", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List users (When not set in the filter, blocked and deleted users will be returned too)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("user", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserListResponse)

    def notifyBan(self, userId):
        """Notify about user ban"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("user", "notifyBan", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def login(self, partnerId, userId, password, expiry = 86400, privileges = "*"):
        """Get a session using user id and password"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("userId", userId)
        kparams.addStringIfDefined("password", password)
        kparams.addIntIfDefined("expiry", expiry);
        kparams.addStringIfDefined("privileges", privileges)
        self.client.queueServiceActionCall("user", "login", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def loginByLoginId(self, loginId, password, partnerId = NotImplemented, expiry = 86400, privileges = "*"):
        """Get a session using user's kaltura id and password"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("loginId", loginId)
        kparams.addStringIfDefined("password", password)
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("expiry", expiry);
        kparams.addStringIfDefined("privileges", privileges)
        self.client.queueServiceActionCall("user", "loginByLoginId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateLoginData(self, oldLoginId, password, newLoginId = "", newPassword = "", newFirstName = NotImplemented, newLastName = NotImplemented):
        """Update user password and email"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("oldLoginId", oldLoginId)
        kparams.addStringIfDefined("password", password)
        kparams.addStringIfDefined("newLoginId", newLoginId)
        kparams.addStringIfDefined("newPassword", newPassword)
        kparams.addStringIfDefined("newFirstName", newFirstName)
        kparams.addStringIfDefined("newLastName", newLastName)
        self.client.queueServiceActionCall("user", "updateLoginData", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def resetPassword(self, email):
        """Reset admin user password and send it to the users email address"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("email", email)
        self.client.queueServiceActionCall("user", "resetPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def setInitialPassword(self, hashKey, newPassword):
        """Set initial users password"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("hashKey", hashKey)
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("user", "setInitialPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def enableLogin(self, userId, loginId, password = NotImplemented):
        """Enable the user to login with a loginId (email) and password."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addStringIfDefined("loginId", loginId)
        kparams.addStringIfDefined("password", password)
        self.client.queueServiceActionCall("user", "enableLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def disableLogin(self, userId = NotImplemented, loginId = NotImplemented):
        """Disallow user to login with an id/password.
        Passing either a loginId or a userId is allowed."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addStringIfDefined("loginId", loginId)
        self.client.queueServiceActionCall("user", "disableLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)


class KalturaWidgetService(KalturaServiceBase):
    """widget service for full widget management"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, widget):
        """Add new widget, can be attached to entry or kshow
        SourceWidget is ignored."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("widget", widget)
        self.client.queueServiceActionCall("widget", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def update(self, id, widget):
        """Update exisiting widget"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("widget", widget)
        self.client.queueServiceActionCall("widget", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def get(self, id):
        """Get widget by id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("widget", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def clone(self, widget):
        """Add widget based on existing widget.
        Must provide valid sourceWidgetId"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("widget", widget)
        self.client.queueServiceActionCall("widget", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Retrieve a list of available widget depends on the filter given"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("widget", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidgetListResponse)


class KalturaXInternalService(KalturaServiceBase):
    """Internal Service is used for actions that are used internally in Kaltura applications and might be changed in the future without any notice."""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def xAddBulkDownload(self, entryIds, flavorParamsId = ""):
        """Creates new download job for multiple entry ids (comma separated), an email will be sent when the job is done
        This sevice support the following entries: 
        - MediaEntry
        - Video will be converted using the flavor params id
        - Audio will be downloaded as MP3
        - Image will be downloaded as Jpeg
        - MixEntry will be flattend using the flavor params id
        - Other entry types are not supported
        Returns the admin email that the email message will be sent to"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryIds", entryIds)
        kparams.addStringIfDefined("flavorParamsId", flavorParamsId)
        self.client.queueServiceActionCall("xinternal", "xAddBulkDownload", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaCoreClient(KalturaClientPlugin):
    # KalturaCoreClient
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaCoreClient
    @staticmethod
    def get(client):
        if KalturaCoreClient.instance == None:
            KalturaCoreClient.instance = KalturaCoreClient(client)
        return KalturaCoreClient.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'accessControl': KalturaAccessControlService,
            'adminUser': KalturaAdminUserService,
            'baseEntry': KalturaBaseEntryService,
            'bulkUpload': KalturaBulkUploadService,
            'category': KalturaCategoryService,
            'conversionProfileAssetParams': KalturaConversionProfileAssetParamsService,
            'conversionProfile': KalturaConversionProfileService,
            'data': KalturaDataService,
            'document': KalturaDocumentService,
            'EmailIngestionProfile': KalturaEmailIngestionProfileService,
            'flavorAsset': KalturaFlavorAssetService,
            'flavorParams': KalturaFlavorParamsService,
            'liveStream': KalturaLiveStreamService,
            'mediaInfo': KalturaMediaInfoService,
            'media': KalturaMediaService,
            'mixing': KalturaMixingService,
            'notification': KalturaNotificationService,
            'partner': KalturaPartnerService,
            'permissionItem': KalturaPermissionItemService,
            'permission': KalturaPermissionService,
            'playlist': KalturaPlaylistService,
            'report': KalturaReportService,
            'schema': KalturaSchemaService,
            'search': KalturaSearchService,
            'session': KalturaSessionService,
            'stats': KalturaStatsService,
            'storageProfile': KalturaStorageProfileService,
            'syndicationFeed': KalturaSyndicationFeedService,
            'system': KalturaSystemService,
            'thumbAsset': KalturaThumbAssetService,
            'thumbParams': KalturaThumbParamsService,
            'uiConf': KalturaUiConfService,
            'upload': KalturaUploadService,
            'uploadToken': KalturaUploadTokenService,
            'userRole': KalturaUserRoleService,
            'user': KalturaUserService,
            'widget': KalturaWidgetService,
            'xInternal': KalturaXInternalService,
        }

    def getEnums(self):
        return {
            'KalturaAccessControlOrderBy': KalturaAccessControlOrderBy,
            'KalturaAdminUserOrderBy': KalturaAdminUserOrderBy,
            'KalturaApiActionPermissionItemOrderBy': KalturaApiActionPermissionItemOrderBy,
            'KalturaApiParameterPermissionItemAction': KalturaApiParameterPermissionItemAction,
            'KalturaApiParameterPermissionItemOrderBy': KalturaApiParameterPermissionItemOrderBy,
            'KalturaAssetOrderBy': KalturaAssetOrderBy,
            'KalturaAssetParamsOrderBy': KalturaAssetParamsOrderBy,
            'KalturaAssetParamsOrigin': KalturaAssetParamsOrigin,
            'KalturaAssetParamsOutputOrderBy': KalturaAssetParamsOutputOrderBy,
            'KalturaAssetStatus': KalturaAssetStatus,
            'KalturaAudioCodec': KalturaAudioCodec,
            'KalturaBaseEntryOrderBy': KalturaBaseEntryOrderBy,
            'KalturaBaseJobOrderBy': KalturaBaseJobOrderBy,
            'KalturaBaseSyndicationFeedOrderBy': KalturaBaseSyndicationFeedOrderBy,
            'KalturaBatchJobErrorTypes': KalturaBatchJobErrorTypes,
            'KalturaBatchJobOrderBy': KalturaBatchJobOrderBy,
            'KalturaBatchJobStatus': KalturaBatchJobStatus,
            'KalturaBatchJobType': KalturaBatchJobType,
            'KalturaBitRateMode': KalturaBitRateMode,
            'KalturaBulkUploadAction': KalturaBulkUploadAction,
            'KalturaBulkUploadResultObjectType': KalturaBulkUploadResultObjectType,
            'KalturaBulkUploadType': KalturaBulkUploadType,
            'KalturaCategoryOrderBy': KalturaCategoryOrderBy,
            'KalturaCommercialUseType': KalturaCommercialUseType,
            'KalturaContainerFormat': KalturaContainerFormat,
            'KalturaControlPanelCommandOrderBy': KalturaControlPanelCommandOrderBy,
            'KalturaControlPanelCommandStatus': KalturaControlPanelCommandStatus,
            'KalturaControlPanelCommandTargetType': KalturaControlPanelCommandTargetType,
            'KalturaControlPanelCommandType': KalturaControlPanelCommandType,
            'KalturaConversionProfileAssetParamsOrderBy': KalturaConversionProfileAssetParamsOrderBy,
            'KalturaConversionProfileOrderBy': KalturaConversionProfileOrderBy,
            'KalturaConversionProfileStatus': KalturaConversionProfileStatus,
            'KalturaCountryRestrictionType': KalturaCountryRestrictionType,
            'KalturaDataEntryOrderBy': KalturaDataEntryOrderBy,
            'KalturaDirectoryRestrictionType': KalturaDirectoryRestrictionType,
            'KalturaDurationType': KalturaDurationType,
            'KalturaEditorType': KalturaEditorType,
            'KalturaEmailIngestionProfileStatus': KalturaEmailIngestionProfileStatus,
            'KalturaEntryModerationStatus': KalturaEntryModerationStatus,
            'KalturaEntryReplacementStatus': KalturaEntryReplacementStatus,
            'KalturaEntryStatus': KalturaEntryStatus,
            'KalturaEntryType': KalturaEntryType,
            'KalturaFileSyncObjectType': KalturaFileSyncObjectType,
            'KalturaFlavorAssetOrderBy': KalturaFlavorAssetOrderBy,
            'KalturaFlavorAssetStatus': KalturaFlavorAssetStatus,
            'KalturaFlavorParamsOrderBy': KalturaFlavorParamsOrderBy,
            'KalturaFlavorParamsOutputOrderBy': KalturaFlavorParamsOutputOrderBy,
            'KalturaFlavorReadyBehaviorType': KalturaFlavorReadyBehaviorType,
            'KalturaGender': KalturaGender,
            'KalturaGenericSyndicationFeedOrderBy': KalturaGenericSyndicationFeedOrderBy,
            'KalturaGenericXsltSyndicationFeedOrderBy': KalturaGenericXsltSyndicationFeedOrderBy,
            'KalturaGoogleSyndicationFeedAdultValues': KalturaGoogleSyndicationFeedAdultValues,
            'KalturaGoogleVideoSyndicationFeedOrderBy': KalturaGoogleVideoSyndicationFeedOrderBy,
            'KalturaITunesSyndicationFeedAdultValues': KalturaITunesSyndicationFeedAdultValues,
            'KalturaITunesSyndicationFeedCategories': KalturaITunesSyndicationFeedCategories,
            'KalturaITunesSyndicationFeedOrderBy': KalturaITunesSyndicationFeedOrderBy,
            'KalturaIpAddressRestrictionType': KalturaIpAddressRestrictionType,
            'KalturaLanguage': KalturaLanguage,
            'KalturaLanguageCode': KalturaLanguageCode,
            'KalturaLicenseType': KalturaLicenseType,
            'KalturaLiveStreamAdminEntryOrderBy': KalturaLiveStreamAdminEntryOrderBy,
            'KalturaLiveStreamEntryOrderBy': KalturaLiveStreamEntryOrderBy,
            'KalturaMailJobOrderBy': KalturaMailJobOrderBy,
            'KalturaMediaEntryOrderBy': KalturaMediaEntryOrderBy,
            'KalturaMediaFlavorParamsOrderBy': KalturaMediaFlavorParamsOrderBy,
            'KalturaMediaFlavorParamsOutputOrderBy': KalturaMediaFlavorParamsOutputOrderBy,
            'KalturaMediaInfoOrderBy': KalturaMediaInfoOrderBy,
            'KalturaMediaType': KalturaMediaType,
            'KalturaMixEntryOrderBy': KalturaMixEntryOrderBy,
            'KalturaModerationFlagStatus': KalturaModerationFlagStatus,
            'KalturaModerationFlagType': KalturaModerationFlagType,
            'KalturaModerationObjectType': KalturaModerationObjectType,
            'KalturaNotificationOrderBy': KalturaNotificationOrderBy,
            'KalturaNotificationType': KalturaNotificationType,
            'KalturaNullableBoolean': KalturaNullableBoolean,
            'KalturaPartnerGroupType': KalturaPartnerGroupType,
            'KalturaPartnerOrderBy': KalturaPartnerOrderBy,
            'KalturaPartnerStatus': KalturaPartnerStatus,
            'KalturaPartnerType': KalturaPartnerType,
            'KalturaPermissionItemOrderBy': KalturaPermissionItemOrderBy,
            'KalturaPermissionItemType': KalturaPermissionItemType,
            'KalturaPermissionOrderBy': KalturaPermissionOrderBy,
            'KalturaPermissionStatus': KalturaPermissionStatus,
            'KalturaPermissionType': KalturaPermissionType,
            'KalturaPlayableEntryOrderBy': KalturaPlayableEntryOrderBy,
            'KalturaPlaylistOrderBy': KalturaPlaylistOrderBy,
            'KalturaPlaylistType': KalturaPlaylistType,
            'KalturaReportOrderBy': KalturaReportOrderBy,
            'KalturaReportType': KalturaReportType,
            'KalturaSchemaType': KalturaSchemaType,
            'KalturaSearchConditionComparison': KalturaSearchConditionComparison,
            'KalturaSearchOperatorType': KalturaSearchOperatorType,
            'KalturaSearchProviderType': KalturaSearchProviderType,
            'KalturaSessionType': KalturaSessionType,
            'KalturaSiteRestrictionType': KalturaSiteRestrictionType,
            'KalturaSourceType': KalturaSourceType,
            'KalturaStatsEventType': KalturaStatsEventType,
            'KalturaStatsKmcEventType': KalturaStatsKmcEventType,
            'KalturaStorageProfileDeliveryStatus': KalturaStorageProfileDeliveryStatus,
            'KalturaStorageProfileOrderBy': KalturaStorageProfileOrderBy,
            'KalturaStorageProfileProtocol': KalturaStorageProfileProtocol,
            'KalturaStorageProfileStatus': KalturaStorageProfileStatus,
            'KalturaStorageServePriority': KalturaStorageServePriority,
            'KalturaSyndicationFeedStatus': KalturaSyndicationFeedStatus,
            'KalturaSyndicationFeedType': KalturaSyndicationFeedType,
            'KalturaThumbAssetOrderBy': KalturaThumbAssetOrderBy,
            'KalturaThumbAssetStatus': KalturaThumbAssetStatus,
            'KalturaThumbCropType': KalturaThumbCropType,
            'KalturaThumbParamsOrderBy': KalturaThumbParamsOrderBy,
            'KalturaThumbParamsOutputOrderBy': KalturaThumbParamsOutputOrderBy,
            'KalturaTubeMogulSyndicationFeedCategories': KalturaTubeMogulSyndicationFeedCategories,
            'KalturaTubeMogulSyndicationFeedOrderBy': KalturaTubeMogulSyndicationFeedOrderBy,
            'KalturaUiConfCreationMode': KalturaUiConfCreationMode,
            'KalturaUiConfObjType': KalturaUiConfObjType,
            'KalturaUiConfOrderBy': KalturaUiConfOrderBy,
            'KalturaUploadErrorCode': KalturaUploadErrorCode,
            'KalturaUploadTokenOrderBy': KalturaUploadTokenOrderBy,
            'KalturaUploadTokenStatus': KalturaUploadTokenStatus,
            'KalturaUserAgentRestrictionType': KalturaUserAgentRestrictionType,
            'KalturaUserLoginDataOrderBy': KalturaUserLoginDataOrderBy,
            'KalturaUserOrderBy': KalturaUserOrderBy,
            'KalturaUserRoleOrderBy': KalturaUserRoleOrderBy,
            'KalturaUserRoleStatus': KalturaUserRoleStatus,
            'KalturaUserStatus': KalturaUserStatus,
            'KalturaVideoCodec': KalturaVideoCodec,
            'KalturaWidgetOrderBy': KalturaWidgetOrderBy,
            'KalturaWidgetSecurityType': KalturaWidgetSecurityType,
            'KalturaYahooSyndicationFeedAdultValues': KalturaYahooSyndicationFeedAdultValues,
            'KalturaYahooSyndicationFeedCategories': KalturaYahooSyndicationFeedCategories,
            'KalturaYahooSyndicationFeedOrderBy': KalturaYahooSyndicationFeedOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaBaseRestriction': KalturaBaseRestriction,
            'KalturaAccessControl': KalturaAccessControl,
            'KalturaSearchItem': KalturaSearchItem,
            'KalturaFilter': KalturaFilter,
            'KalturaAccessControlBaseFilter': KalturaAccessControlBaseFilter,
            'KalturaAccessControlFilter': KalturaAccessControlFilter,
            'KalturaFilterPager': KalturaFilterPager,
            'KalturaAccessControlListResponse': KalturaAccessControlListResponse,
            'KalturaUser': KalturaUser,
            'KalturaAdminUser': KalturaAdminUser,
            'KalturaDynamicEnum': KalturaDynamicEnum,
            'KalturaOperationAttributes': KalturaOperationAttributes,
            'KalturaBaseEntry': KalturaBaseEntry,
            'KalturaResource': KalturaResource,
            'KalturaRemotePath': KalturaRemotePath,
            'KalturaRemotePathListResponse': KalturaRemotePathListResponse,
            'KalturaBaseEntryBaseFilter': KalturaBaseEntryBaseFilter,
            'KalturaBaseEntryFilter': KalturaBaseEntryFilter,
            'KalturaBaseEntryListResponse': KalturaBaseEntryListResponse,
            'KalturaModerationFlag': KalturaModerationFlag,
            'KalturaModerationFlagListResponse': KalturaModerationFlagListResponse,
            'KalturaEntryContextDataParams': KalturaEntryContextDataParams,
            'KalturaEntryContextDataResult': KalturaEntryContextDataResult,
            'KalturaBulkUploadPluginData': KalturaBulkUploadPluginData,
            'KalturaBulkUploadResult': KalturaBulkUploadResult,
            'KalturaBulkUpload': KalturaBulkUpload,
            'KalturaBulkUploadListResponse': KalturaBulkUploadListResponse,
            'KalturaCategory': KalturaCategory,
            'KalturaCategoryBaseFilter': KalturaCategoryBaseFilter,
            'KalturaCategoryFilter': KalturaCategoryFilter,
            'KalturaCategoryListResponse': KalturaCategoryListResponse,
            'KalturaConversionProfileAssetParamsBaseFilter': KalturaConversionProfileAssetParamsBaseFilter,
            'KalturaConversionProfileBaseFilter': KalturaConversionProfileBaseFilter,
            'KalturaConversionProfileFilter': KalturaConversionProfileFilter,
            'KalturaAssetParamsBaseFilter': KalturaAssetParamsBaseFilter,
            'KalturaAssetParamsFilter': KalturaAssetParamsFilter,
            'KalturaConversionProfileAssetParamsFilter': KalturaConversionProfileAssetParamsFilter,
            'KalturaConversionProfileAssetParams': KalturaConversionProfileAssetParams,
            'KalturaConversionProfileAssetParamsListResponse': KalturaConversionProfileAssetParamsListResponse,
            'KalturaCropDimensions': KalturaCropDimensions,
            'KalturaConversionProfile': KalturaConversionProfile,
            'KalturaConversionProfileListResponse': KalturaConversionProfileListResponse,
            'KalturaDataEntry': KalturaDataEntry,
            'KalturaDataEntryBaseFilter': KalturaDataEntryBaseFilter,
            'KalturaDataEntryFilter': KalturaDataEntryFilter,
            'KalturaDataListResponse': KalturaDataListResponse,
            'KalturaConversionAttribute': KalturaConversionAttribute,
            'KalturaEmailIngestionProfile': KalturaEmailIngestionProfile,
            'KalturaPlayableEntry': KalturaPlayableEntry,
            'KalturaMediaEntry': KalturaMediaEntry,
            'KalturaAsset': KalturaAsset,
            'KalturaFlavorAsset': KalturaFlavorAsset,
            'KalturaContentResource': KalturaContentResource,
            'KalturaAssetBaseFilter': KalturaAssetBaseFilter,
            'KalturaAssetFilter': KalturaAssetFilter,
            'KalturaFlavorAssetListResponse': KalturaFlavorAssetListResponse,
            'KalturaString': KalturaString,
            'KalturaAssetParams': KalturaAssetParams,
            'KalturaFlavorParams': KalturaFlavorParams,
            'KalturaFlavorAssetWithParams': KalturaFlavorAssetWithParams,
            'KalturaFlavorParamsBaseFilter': KalturaFlavorParamsBaseFilter,
            'KalturaFlavorParamsFilter': KalturaFlavorParamsFilter,
            'KalturaFlavorParamsListResponse': KalturaFlavorParamsListResponse,
            'KalturaLiveStreamBitrate': KalturaLiveStreamBitrate,
            'KalturaLiveStreamEntry': KalturaLiveStreamEntry,
            'KalturaLiveStreamAdminEntry': KalturaLiveStreamAdminEntry,
            'KalturaPlayableEntryBaseFilter': KalturaPlayableEntryBaseFilter,
            'KalturaPlayableEntryFilter': KalturaPlayableEntryFilter,
            'KalturaMediaEntryBaseFilter': KalturaMediaEntryBaseFilter,
            'KalturaMediaEntryFilter': KalturaMediaEntryFilter,
            'KalturaLiveStreamEntryBaseFilter': KalturaLiveStreamEntryBaseFilter,
            'KalturaLiveStreamEntryFilter': KalturaLiveStreamEntryFilter,
            'KalturaLiveStreamListResponse': KalturaLiveStreamListResponse,
            'KalturaMediaInfoBaseFilter': KalturaMediaInfoBaseFilter,
            'KalturaMediaInfoFilter': KalturaMediaInfoFilter,
            'KalturaMediaInfo': KalturaMediaInfo,
            'KalturaMediaInfoListResponse': KalturaMediaInfoListResponse,
            'KalturaSearch': KalturaSearch,
            'KalturaSearchResult': KalturaSearchResult,
            'KalturaMediaListResponse': KalturaMediaListResponse,
            'KalturaMixEntry': KalturaMixEntry,
            'KalturaMixEntryBaseFilter': KalturaMixEntryBaseFilter,
            'KalturaMixEntryFilter': KalturaMixEntryFilter,
            'KalturaMixListResponse': KalturaMixListResponse,
            'KalturaClientNotification': KalturaClientNotification,
            'KalturaKeyValue': KalturaKeyValue,
            'KalturaPartner': KalturaPartner,
            'KalturaPartnerUsage': KalturaPartnerUsage,
            'KalturaPermissionItem': KalturaPermissionItem,
            'KalturaPermissionItemBaseFilter': KalturaPermissionItemBaseFilter,
            'KalturaPermissionItemFilter': KalturaPermissionItemFilter,
            'KalturaPermissionItemListResponse': KalturaPermissionItemListResponse,
            'KalturaPermission': KalturaPermission,
            'KalturaPermissionBaseFilter': KalturaPermissionBaseFilter,
            'KalturaPermissionFilter': KalturaPermissionFilter,
            'KalturaPermissionListResponse': KalturaPermissionListResponse,
            'KalturaMediaEntryFilterForPlaylist': KalturaMediaEntryFilterForPlaylist,
            'KalturaPlaylist': KalturaPlaylist,
            'KalturaPlaylistBaseFilter': KalturaPlaylistBaseFilter,
            'KalturaPlaylistFilter': KalturaPlaylistFilter,
            'KalturaPlaylistListResponse': KalturaPlaylistListResponse,
            'KalturaReportInputFilter': KalturaReportInputFilter,
            'KalturaReportGraph': KalturaReportGraph,
            'KalturaReportTotal': KalturaReportTotal,
            'KalturaReportTable': KalturaReportTable,
            'KalturaReportResponse': KalturaReportResponse,
            'KalturaSearchResultResponse': KalturaSearchResultResponse,
            'KalturaSearchAuthData': KalturaSearchAuthData,
            'KalturaStartWidgetSessionResponse': KalturaStartWidgetSessionResponse,
            'KalturaStatsEvent': KalturaStatsEvent,
            'KalturaStatsKmcEvent': KalturaStatsKmcEvent,
            'KalturaCEError': KalturaCEError,
            'KalturaStorageProfile': KalturaStorageProfile,
            'KalturaStorageProfileBaseFilter': KalturaStorageProfileBaseFilter,
            'KalturaStorageProfileFilter': KalturaStorageProfileFilter,
            'KalturaStorageProfileListResponse': KalturaStorageProfileListResponse,
            'KalturaBaseSyndicationFeed': KalturaBaseSyndicationFeed,
            'KalturaBaseSyndicationFeedBaseFilter': KalturaBaseSyndicationFeedBaseFilter,
            'KalturaBaseSyndicationFeedFilter': KalturaBaseSyndicationFeedFilter,
            'KalturaBaseSyndicationFeedListResponse': KalturaBaseSyndicationFeedListResponse,
            'KalturaSyndicationFeedEntryCount': KalturaSyndicationFeedEntryCount,
            'KalturaThumbAsset': KalturaThumbAsset,
            'KalturaThumbParams': KalturaThumbParams,
            'KalturaThumbAssetListResponse': KalturaThumbAssetListResponse,
            'KalturaThumbParamsBaseFilter': KalturaThumbParamsBaseFilter,
            'KalturaThumbParamsFilter': KalturaThumbParamsFilter,
            'KalturaThumbParamsListResponse': KalturaThumbParamsListResponse,
            'KalturaUiConf': KalturaUiConf,
            'KalturaUiConfBaseFilter': KalturaUiConfBaseFilter,
            'KalturaUiConfFilter': KalturaUiConfFilter,
            'KalturaUiConfListResponse': KalturaUiConfListResponse,
            'KalturaUiConfTypeInfo': KalturaUiConfTypeInfo,
            'KalturaUploadResponse': KalturaUploadResponse,
            'KalturaUploadToken': KalturaUploadToken,
            'KalturaUploadTokenBaseFilter': KalturaUploadTokenBaseFilter,
            'KalturaUploadTokenFilter': KalturaUploadTokenFilter,
            'KalturaUploadTokenListResponse': KalturaUploadTokenListResponse,
            'KalturaUserRole': KalturaUserRole,
            'KalturaUserRoleBaseFilter': KalturaUserRoleBaseFilter,
            'KalturaUserRoleFilter': KalturaUserRoleFilter,
            'KalturaUserRoleListResponse': KalturaUserRoleListResponse,
            'KalturaUserBaseFilter': KalturaUserBaseFilter,
            'KalturaUserFilter': KalturaUserFilter,
            'KalturaUserListResponse': KalturaUserListResponse,
            'KalturaWidget': KalturaWidget,
            'KalturaWidgetBaseFilter': KalturaWidgetBaseFilter,
            'KalturaWidgetFilter': KalturaWidgetFilter,
            'KalturaWidgetListResponse': KalturaWidgetListResponse,
            'KalturaPartnerBaseFilter': KalturaPartnerBaseFilter,
            'KalturaPartnerFilter': KalturaPartnerFilter,
            'KalturaPartnerListResponse': KalturaPartnerListResponse,
            'KalturaUserLoginDataBaseFilter': KalturaUserLoginDataBaseFilter,
            'KalturaUserLoginDataFilter': KalturaUserLoginDataFilter,
            'KalturaUserLoginData': KalturaUserLoginData,
            'KalturaUserLoginDataListResponse': KalturaUserLoginDataListResponse,
            'KalturaFlavorParamsOutputBaseFilter': KalturaFlavorParamsOutputBaseFilter,
            'KalturaFlavorParamsOutputFilter': KalturaFlavorParamsOutputFilter,
            'KalturaFlavorParamsOutput': KalturaFlavorParamsOutput,
            'KalturaThumbParamsOutputBaseFilter': KalturaThumbParamsOutputBaseFilter,
            'KalturaThumbParamsOutputFilter': KalturaThumbParamsOutputFilter,
            'KalturaThumbParamsOutput': KalturaThumbParamsOutput,
            'KalturaReport': KalturaReport,
            'KalturaReportBaseFilter': KalturaReportBaseFilter,
            'KalturaReportFilter': KalturaReportFilter,
            'KalturaReportListResponse': KalturaReportListResponse,
            'KalturaCountryRestriction': KalturaCountryRestriction,
            'KalturaDirectoryRestriction': KalturaDirectoryRestriction,
            'KalturaIpAddressRestriction': KalturaIpAddressRestriction,
            'KalturaSessionRestriction': KalturaSessionRestriction,
            'KalturaPreviewRestriction': KalturaPreviewRestriction,
            'KalturaSiteRestriction': KalturaSiteRestriction,
            'KalturaUserAgentRestriction': KalturaUserAgentRestriction,
            'KalturaSearchCondition': KalturaSearchCondition,
            'KalturaSearchComparableCondition': KalturaSearchComparableCondition,
            'KalturaSearchOperator': KalturaSearchOperator,
            'KalturaBaseJobBaseFilter': KalturaBaseJobBaseFilter,
            'KalturaBaseJobFilter': KalturaBaseJobFilter,
            'KalturaBatchJobBaseFilter': KalturaBatchJobBaseFilter,
            'KalturaControlPanelCommandBaseFilter': KalturaControlPanelCommandBaseFilter,
            'KalturaMailJobBaseFilter': KalturaMailJobBaseFilter,
            'KalturaNotificationBaseFilter': KalturaNotificationBaseFilter,
            'KalturaBatchJobFilter': KalturaBatchJobFilter,
            'KalturaControlPanelCommandFilter': KalturaControlPanelCommandFilter,
            'KalturaMailJobFilter': KalturaMailJobFilter,
            'KalturaNotificationFilter': KalturaNotificationFilter,
            'KalturaBatchJobFilterExt': KalturaBatchJobFilterExt,
            'KalturaAssetParamsOutputBaseFilter': KalturaAssetParamsOutputBaseFilter,
            'KalturaFlavorAssetBaseFilter': KalturaFlavorAssetBaseFilter,
            'KalturaMediaFlavorParamsBaseFilter': KalturaMediaFlavorParamsBaseFilter,
            'KalturaMediaFlavorParamsOutputBaseFilter': KalturaMediaFlavorParamsOutputBaseFilter,
            'KalturaThumbAssetBaseFilter': KalturaThumbAssetBaseFilter,
            'KalturaAssetParamsOutputFilter': KalturaAssetParamsOutputFilter,
            'KalturaFlavorAssetFilter': KalturaFlavorAssetFilter,
            'KalturaMediaFlavorParamsFilter': KalturaMediaFlavorParamsFilter,
            'KalturaMediaFlavorParamsOutputFilter': KalturaMediaFlavorParamsOutputFilter,
            'KalturaThumbAssetFilter': KalturaThumbAssetFilter,
            'KalturaLiveStreamAdminEntryBaseFilter': KalturaLiveStreamAdminEntryBaseFilter,
            'KalturaLiveStreamAdminEntryFilter': KalturaLiveStreamAdminEntryFilter,
            'KalturaAdminUserBaseFilter': KalturaAdminUserBaseFilter,
            'KalturaAdminUserFilter': KalturaAdminUserFilter,
            'KalturaGoogleVideoSyndicationFeedBaseFilter': KalturaGoogleVideoSyndicationFeedBaseFilter,
            'KalturaGoogleVideoSyndicationFeedFilter': KalturaGoogleVideoSyndicationFeedFilter,
            'KalturaITunesSyndicationFeedBaseFilter': KalturaITunesSyndicationFeedBaseFilter,
            'KalturaITunesSyndicationFeedFilter': KalturaITunesSyndicationFeedFilter,
            'KalturaTubeMogulSyndicationFeedBaseFilter': KalturaTubeMogulSyndicationFeedBaseFilter,
            'KalturaTubeMogulSyndicationFeedFilter': KalturaTubeMogulSyndicationFeedFilter,
            'KalturaYahooSyndicationFeedBaseFilter': KalturaYahooSyndicationFeedBaseFilter,
            'KalturaYahooSyndicationFeedFilter': KalturaYahooSyndicationFeedFilter,
            'KalturaApiActionPermissionItemBaseFilter': KalturaApiActionPermissionItemBaseFilter,
            'KalturaApiParameterPermissionItemBaseFilter': KalturaApiParameterPermissionItemBaseFilter,
            'KalturaApiActionPermissionItemFilter': KalturaApiActionPermissionItemFilter,
            'KalturaApiParameterPermissionItemFilter': KalturaApiParameterPermissionItemFilter,
            'KalturaGenericSyndicationFeedBaseFilter': KalturaGenericSyndicationFeedBaseFilter,
            'KalturaGenericSyndicationFeedFilter': KalturaGenericSyndicationFeedFilter,
            'KalturaGenericXsltSyndicationFeedBaseFilter': KalturaGenericXsltSyndicationFeedBaseFilter,
            'KalturaGenericXsltSyndicationFeedFilter': KalturaGenericXsltSyndicationFeedFilter,
            'KalturaClipAttributes': KalturaClipAttributes,
            'KalturaAssetParamsResourceContainer': KalturaAssetParamsResourceContainer,
            'KalturaAssetResource': KalturaAssetResource,
            'KalturaAssetsParamsResourceContainers': KalturaAssetsParamsResourceContainers,
            'KalturaDataCenterContentResource': KalturaDataCenterContentResource,
            'KalturaEntryResource': KalturaEntryResource,
            'KalturaFileSyncResource': KalturaFileSyncResource,
            'KalturaOperationResource': KalturaOperationResource,
            'KalturaUrlResource': KalturaUrlResource,
            'KalturaRemoteStorageResource': KalturaRemoteStorageResource,
            'KalturaRemoteStorageResources': KalturaRemoteStorageResources,
            'KalturaServerFileResource': KalturaServerFileResource,
            'KalturaSshUrlResource': KalturaSshUrlResource,
            'KalturaUploadedFileTokenResource': KalturaUploadedFileTokenResource,
            'KalturaWebcamTokenResource': KalturaWebcamTokenResource,
            'KalturaAssetParamsOutput': KalturaAssetParamsOutput,
            'KalturaMediaFlavorParamsOutput': KalturaMediaFlavorParamsOutput,
            'KalturaMediaFlavorParams': KalturaMediaFlavorParams,
            'KalturaApiActionPermissionItem': KalturaApiActionPermissionItem,
            'KalturaApiParameterPermissionItem': KalturaApiParameterPermissionItem,
            'KalturaGenericSyndicationFeed': KalturaGenericSyndicationFeed,
            'KalturaGenericXsltSyndicationFeed': KalturaGenericXsltSyndicationFeed,
            'KalturaGoogleVideoSyndicationFeed': KalturaGoogleVideoSyndicationFeed,
            'KalturaITunesSyndicationFeed': KalturaITunesSyndicationFeed,
            'KalturaTubeMogulSyndicationFeed': KalturaTubeMogulSyndicationFeed,
            'KalturaYahooSyndicationFeed': KalturaYahooSyndicationFeed,
        }

    # @return string
    def getName(self):
        return ''

