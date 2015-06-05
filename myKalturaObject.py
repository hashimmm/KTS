import sys
from urllib import urlencode
import logging
import re
import time
import difflib
import xml.etree.ElementTree as ET

#from httplib2 import Http
from KalturaClient import *
from KalturaMetadataClientPlugin import *
from KalturaCaptionClientPlugin import *
from KalturaCoreClient import KalturaThumbAsset, KalturaUrlResource, KalturaEntryStatus, KalturaThumbParams, KalturaNullableBoolean
# to handle some particular kaltura exceptions:
from KalturaClientBase import KalturaException

import properties
from utils import convert_file_to_unicode



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    stream=sys.stdout)


SETTINGS = {}
properties.load_kaltura_settings(SETTINGS)

KALTURA_REQUEST_TIMEOUT = 60
KS_EXPIRY = 600

DEFAULT_SEARCH_FIELD_LIST = [
                  'id',
                  'name',
                  'status',
                  'description',
                  'tags',
                  'url',
                  'thumbnail_url',
                  'media_type',
                  'plays',
                  'views',
                  'rank',
                  'width',
                  'height',
                  'duration',
                  'views',
                  'updated',
                  'created',
                  'searchtext',
                  'startDate',
                  'endDate',
                  'partner_id',
                  'user_id',
                  'download_url',
                  'source_type',
                  'mediaDate',
                  'flavorParamsId',
                  'conversionQuality',
                  'creditUserName',
                  'creditUrl'
                  ]


LANGUAGE_LIST = [
    "Abkhazian",
    "Afar",
    "Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Assamese",
    "Aymara",
    "Azerbaijani",
    "Bashkir",
    "Basque",
    "Bengali (Bangla)",
    "Bhutani",
    "Bihari",
    "Bislama",
    "Breton",
    "Bulgarian",
    "Burmese",
    "Byelorussian (Belarusian)",
    "Cambodian",
    "Catalan",
    "Chinese",
    "Corsican",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Esperanto",
    "Estonian",
    "Faeroese",
    "Farsi",
    "Fiji",
    "Finnish",
    "French",
    "Frisian",
    "Galician",
    "Gaelic (Scottish)",
    "Gaelic (Manx)",
    "Georgian",
    "German",
    "Greek",
    "Greenlandic",
    "Guarani",
    "Gujarati",
    "Hausa",
    "Hebrew",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "Indonesian",
    "Interlingua",
    "Interlingue",
    "Inuktitut",
    "Inupiak",
    "Irish",
    "Italian",
    "Japanese",
    "Javanese",
    "Kannada",
    "Kashmiri",
    "Kazakh",
    "Kinyarwanda (Ruanda)",
    "Kirghiz",
    "Kirundi (Rundi)",
    "Korean",
    "Kurdish",
    "Laothian",
    "Latin",
    "Latvian (Lettish)",
    "Limburgish ( Limburger)",
    "Lingala",
    "Lithuanian",
    "Macedonian",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Maori",
    "Marathi",
    "Moldavian",
    "Mongolian",
    "Nauru",
    "Nepali",
    "Norwegian",
    "Occitan",
    "Oriya",
    "Oromo (Afan, Galla)",
    "Pashto (Pushto)",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Quechua",
    "Rhaeto-Romance",
    "Romanian",
    "Russian",
    "Samoan",
    "Sangro",
    "Sanskrit",
    "Serbian",
    "Serbo-Croatian",
    "Sesotho",
    "Setswana",
    "Shona",
    "Sindhi",
    "Sinhalese",
    "Siswati",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spanish",
    "Sundanese",
    "Swahili (Kiswahili)",
    "Swedish",
    "Tagalog",
    "Tajik",
    "Tamil",
    "Tatar",
    "Telugu",
    "Thai",
    "Tibetan",
    "Tigrinya",
    "Tonga",
    "Tsonga",
    "Turkish",
    "Turkmen",
    "Twi",
    "Uighur",
    "Ukrainian",
    "Urdu",
    "Uzbek",
    "Vietnamese",
    "Volapuk",
    "Welsh",
    "Wolof",
    "Xhosa",
    "Yiddish",
    "Yoruba",
    "Zulu"
]


kts_mobile_flavor_payload = {
    "ks": "",
    "clientTag": "testme",
    "service": "flavorParams",
    "action": "add",
    "flavorParams:objectType": "KalturaFlavorParams",
    "flavorParams:partnerId": "99",
    "flavorParams:name": "kts_ipad",
    "flavorParams:systemName": "kts_ipad",
    "flavorParams:description": "Mobile/iPad friendly flavor added by KTS.",
    "flavorParams:tags": "web,ipad,mobile,kts",
    "flavorParams:videoCodec": "h264",
    "flavorParams:videoBitrate": "1500",
    "flavorParams:audioCodec": "aac",
    "flavorParams:audioBitrate": "160",
    "flavorParams:audioChannels": "2",
    "flavorParams:audioSampleRate": "4800",
    "flavorParams:width": "1024",
    "flavorParams:height": "0",
    "flavorParams:frameRate": "25",
    "flavorParams:gopSize": "50",
    "flavorParams:conversionEngines": "2,99",
    "flavorParams:conversionEnginesExtraParams": "-flags +loop+mv4 -cmp 256 -partitions +parti4x4+partp8x8+partb8x8 -trellis 1 -refs 1 -me_range 16 -keyint_min 20 -sc_threshold 40 -i_qfactor 0.71 -bt 800k -maxrate 1200k -bufsize 1200k -rc_eq 'blurCplx^(1-qComp)' -level 30 -async 2  -vsync 2 | -flags +loop+mv4 -cmp 256 -partitions +parti4x4+partp8x8+partb8x8 -trellis 1 -refs 1 -me_range 16 -keyint_min 20 -sc_threshold 40 -i_qfactor 0.71 -bt 800k -maxrate 1200k -bufsize 1200k -rc_eq 'blurCplx^(1-qComp)' -level 30 -async 2 -vsync 2",
    "flavorParams:twoPass": "0",
    "flavorParams:deinterlice": "0",
    "flavorParams:rotate": "0",
    "flavorParams:operators": "",
    "flavorParams:engineVersion": "0",
    "flavorParams:format": "mp4",
    "flavorParams:aspectRatioProcessingMode": "0",
    "flavorParams:forceFrameToMultiplication16": "1",
    "flavorParams:videoConstantBitrate": "0",
    "flavorParams:videoBitrateTolerance": "0",
    "flavorParams:requiredPermissions:item1:objectType": "KalturaString",
    "flavorParams:requiredPermissions:item1:value": "FEATURE_MOBILE_FLAVORS"
}


def sort_by_field(l, field, ascending=True):
    sorted_values = sorted([item[field] for item in l], reverse=not ascending)
    keyed_objects = {item[field]: item for item in l}
    sorted_list = [keyed_objects[value] for value in sorted_values]
    return sorted_list


# The above needs to be replaced by something like the following:
# li = [{"time": 1},{"time":3},{"time":2}]
# li.sort(cmp= lambda x, y: 1 if x["time"] > y["time"] else (0 if x["time"] == y["time"] else -1))


def parse_caption_language(capfile, capformat):
    if capformat == 'srt':
        fname = os.path.basename(capfile)
        parts = fname.split('.')
        language = parts[-2] if len(parts) > 2 else parts[0]
    else:
        tree = ET.parse(capfile)
        root = tree.getroot()
        langcode = ''
        for k, v in root.attrib.items():
            if k.endswith('lang'):
                langcode = v
        if not langcode:
            langcode = "en"
            logging.info('no language found in xml, defaulting to English.')
        langcode = langcode.upper()
        print langcode
        try:
            language = KalturaLanguage.__dict__[langcode]
        except:
            language = "English"
            logging.warning('Unsupported language "{}" in xml, '
                            'defaulting to English'.format(langcode))
    return language



class KalturaLogger(IKalturaLogger):

    def log(self, msg):
        logging.info(msg)


def GetConfig(settings):
    if not settings:
        raise Exception("Settings not set in GetConfig")
    partner_id = int(settings.get('PARTNER_ID'))
    service_url = settings.get('SERVICE_URL')
    print "-> GetConfig", partner_id, service_url
    config = KalturaConfiguration(partner_id)
    config.serviceUrl = service_url
    config.setLogger(KalturaLogger())
    config.requestTimeout = KALTURA_REQUEST_TIMEOUT
    return config


def get_new_session_key(settings):
    if not settings:
        raise Exception("Settings not set in get_new_session_key")
    partner_id = settings.get('PARTNER_ID')
    admin_secret = settings.get('ADMIN_SECRET')
    user_name = settings.get('USER_NAME')
    client = KalturaClient(GetConfig(settings))
    print "-> get_new_session_key", admin_secret, user_name, partner_id
    return client.session.start(admin_secret,
                                user_name,
                                KalturaSessionType.ADMIN,
                                partner_id, KS_EXPIRY, "")


def create_session(kaltura_id, ks=None):
    settings = properties.load_kaltura_settings().get(kaltura_id)
    if not settings:
        raise Exception("Kaltura ID %s Settings %s" % (kaltura_id, settings))
    client = KalturaClient(GetConfig(settings))
    if not settings:
        raise Exception("Kaltura ID %s not in session %s" % (
            kaltura_id, repr(settings)))
    if not ks:
        ks = get_new_session_key(settings)
    client.setKs(ks)
    return client


def count(client, mediafilter=None):
    ''' need to implement the filter, currently only gives total count
    '''
    try:
        if client is None:
            raise Exception("Client can not be None")
        count = client.media.count(mediafilter)
        return (True, count)
    except Exception as e:
        return (False,
                "Unexpected error:" + "<p>" + repr(sys.exc_info()) +
                "<br>Exception: " + str(e) + "</p>")


def pullVideo(pull_path,
              media_name,
              media_tags=None,
              media_description=None,
              client=None,
              media_type=None):
    try:
    # if True:
        # create session
        if client is None:
            raise Exception("Client can not be None")
        # Add Media Entry anf
        mediaEntry = KalturaMediaEntry()
        mediaEntry.setName(media_name)
        if media_tags:
            mediaEntry.setTags(media_tags)
        if media_description:
            mediaEntry.setDescription(media_description)
        if not media_type:
            media_type = KalturaMediaType(KalturaMediaType.VIDEO)
        mediaEntry.setMediaType(media_type)
        mediaEntry = client.media.addFromUrl(mediaEntry, pull_path)
        return (True, mediaEntry.id)
    except:
        return (False,
                "Unexpected error:" + "<p>" + repr(sys.exc_info()) + "</p>")


def uploadVideo(file_path,
                media_name,
                media_tags=None,
                media_description=None,
                client=None,
                media_type=None):
    try:
    # if True:
        # create session
        if client is None:
            raise Exception("Client can not be None")
        # add media
        uploadTokenId = client.media.upload(file(file_path, 'rb'))
        # Add Media Entry anf
        mediaEntry = KalturaMediaEntry()
        mediaEntry.setName(media_name)
        if media_tags:
            mediaEntry.setTags(media_tags)
        if media_description:
            mediaEntry.setDescription(media_description)
        if not media_type:
            mediaEntry.setMediaType(KalturaMediaType(KalturaMediaType.VIDEO))
        else:
            mediaEntry.setMediaType(KalturaMediaType(media_type))
        mediaEntry = client.media.addFromUploadedFile(
            mediaEntry, uploadTokenId)
        return (True, mediaEntry.id)
    except Exception as e:
        return (False,
                "Unexpected error:" + "<p>" + str(e) + "</p>")


def updateThumbnail(file_path, entry_id, client=None, set_default=False):
    try:
     # create session
        if client is None:
            raise Exception("Client can not be None")
        thumbnail_asset_service = KalturaThumbAssetService(client)
        thumb_asset = KalturaThumbAsset()
        thumb_asset = thumbnail_asset_service.addFromImage(entry_id, file(file_path, 'rb'))
        if set_default:
            thumbnail_set_default(client, thumb_asset.getId())
        #mediaEntry = client.baseEntry.updateThumbnailJpeg(
        #    entry_id, file(file_path, 'rb'))
        return (True, thumb_asset.getId())
    except:
        return (False,
                "Unexpected error:" + "<p>" + repr(sys.exc_info()) + "</p>")


def updateThumbnailFromPlayer(offset, entry_id, client=None):
    try:
        if client is None:
            raise Exception("Client can not be None")
        thumbnail_asset_service = KalturaThumbAssetService(client)
        thumb_params = KalturaThumbParams()
        thumb_params.setVideoOffset(round(offset))
        source_asset_id = None
        thumbasset = thumbnail_asset_service.generate(entry_id, thumb_params, source_asset_id)
        thumbnail_set_default(client, thumbasset.id)
        # mediaEntry = client.baseEntry.updateThumbnailFromSourceEntry(
        #     entry_id, entry_id, round(offset))
        return (True, thumbasset.id)
    except:
        return (False,
                "Unexpected error:" + "<p>" + repr(sys.exc_info()) + "</p>")


def thumbnail_delete(client, thumbnail_id):
    msgs = []
    try:
        thumbnail_asset_service = KalturaThumbAssetService(client)
        thumbnail_asset_service.delete(thumbnail_id)
        msgs.append('Thumbnail with id %s deleted' % thumbnail_id)
        returncontent = {'success': True, 'message': msgs}
    except KalturaException as ke:
        if ke.code == 'THUMB_ASSET_IS_DEFAULT':
            returncontent = {'success': False,
                             'messages': ke.message,
                             'error': 'thumbnail is default'}
        else:
            msgs.append('Deletion failed for thumbnail with ID %s' % thumbnail_id)
            msgs.append('Exception: ' + str(ke))
            returncontent = {'success': False, 'message': msgs}
    except Exception as e:
        msgs.append('Deletion failed for thumbnail with ID %s' % thumbnail_id)
        msgs.append('Exception: ' + str(e))
        returncontent = {'success': False, 'message': msgs}
    return returncontent


def thumbnail_list(client, entry_id, in_dict=True):
    try:
    # if True:
        thumb_asset_service = KalturaThumbAssetService(client)
        kfilter = KalturaAssetFilter()
        kfilter.entryIdEqual = entry_id
        pager = None
        response = thumb_asset_service.list(kfilter, pager)
        thumbnail_list = []
        for thumbnail in response.objects:
            if in_dict:
                thumbinfo = thumbnail_dictify(thumbnail)
                thumbinfo['url'] = thumb_asset_service.getUrl(thumbinfo['id'], None)
                thumbnail_list.append(thumbinfo)
            else:
                thumbnail_list.append(thumbnail)
        thumbnail_list = sort_by_field(thumbnail_list,
                                       "created_at", ascending=False)
        return thumbnail_list
    except:
        return (False,
                "Unexpected error retrieving thumbnail list:" + "<p>" + repr(sys.exc_info()) + "</p>")


def thumbnail_set_default(client, thumbnail_id):
    msgs = []
    try:
        thumbnail_asset_service = KalturaThumbAssetService(client)
        thumbnail_asset_service.setAsDefault(thumbnail_id)
        msgs.append('Thumbnail with id ' + thumbnail_id + ' set as default')
        return {'success': True, 'message': msgs}
    except Exception as e:
        msgs.append('setAsDefault failed for thumbnail with ID %s' % thumbnail_id)
        msgs.append('Exception: ' + str(e))
        return {'success': False, 'message': msgs}


def thumbnail_get_default(client, entry_id, in_dict=True):
    msgs = []
    try:
        thumb_asset_service = KalturaThumbAssetService(client)
        kfilter = KalturaAssetFilter()
        kfilter.entryIdEqual = entry_id
        pager = None
        response = thumb_asset_service.list(kfilter, pager)
        thumbnail_list = []
        for thumbnail in response.objects:
            if in_dict:
                thumbinfo = thumbnail_dictify(thumbnail)
                thumbinfo['url'] = thumb_asset_service.getUrl(thumbinfo['id'], None)
                thumbnail_list.append(thumbinfo)
            else:
                thumbnail_list.append(thumbnail)
        default_thumb = None
        for item in thumbnail_list:
                if item.get('default', False) == True:
                    default_thumb = item
        return default_thumb
    except:
        return (False,
                "Unexpected error retrieving thumbnail list:" + "<p>" + repr(sys.exc_info()) + "</p>")


def thumbnail_add_from_url(client, entry_id, thumburl):
    msgs = []
    try:
        thumbnail_asset_service = KalturaThumbAssetService(client)
        thumb_asset = KalturaThumbAsset()
        thumb_asset = thumbnail_asset_service.add(entry_id, thumb_asset)
        thumb_id = thumb_asset.getId()
        msgs.append('ThumbAsset added to entry, id %s' % thumb_id)
        content_resource = KalturaUrlResource(url=thumburl)
        thumbnail_asset_service.setContent(thumb_id, content_resource)
        msgs.append('url %s applied to thumbnail with id %s' % (thumburl, thumb_id))
        return {'success': True, 'message': msgs}
    except Exception as e:
        msgs.append('Failed to add thumbnail from %s to media with entry_id %s' % (entry_id, thumburl))
        msgs.append('Exception: ' + str(e))
        return {'success': False, 'message': msgs}


def add_kts_mobile_flavor(client, kaltura_id):
    payload = kts_mobile_flavor_payload.copy()
    payload['ks'] = client.getKs()
    settings = properties.load_kaltura_settings().get(kaltura_id)
    url = "%s/api_v3/" % settings['SERVICE_URL']
    data = urlencode(payload)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req).read()
    contentxml = ET.fromstring(response)
    flavor_id = contentxml.find('./result/id').text
    return flavor_id


def add_flavor_to_default_conversion_profile(client, flavor_id, kaltura_id):
    def_cp = client.conversionProfile.getDefault()
    settings = properties.load_kaltura_settings().get(kaltura_id)
    cp_id = def_cp.id
    cp_flavorParamsIds = def_cp.flavorParamsIds + u',{}'.format(flavor_id)
    url = "{}/api_v3/?service=conversionProfile&action=update".format(
        settings['SERVICE_URL'])
    payload = {}
    payload['ks'] = client.getKs()
    payload['id'] = cp_id
    payload['conversionProfile:flavorParamsIds'] = cp_flavorParamsIds
    data = urlencode(payload)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req).read()
    if "<error>" in response:
        raise Exception(response)


def searchVideos(client,
                kaltura_id=None,
                composite=False,
                page_size=None,
                page_index=None):
    # Setup a pager and search to use
    # pager = KalturaFilterPager()
    # pager.setPageSize(5)
    # pager.setPageIndex(1)
    pager = None
    if page_size:
        pager = KalturaFilterPager()
        pager.setPageSize(page_size)
        if page_index:
            pager.setPageIndex(page_index)
    search = KalturaMediaEntryFilter()
    search.setOrderBy(KalturaMediaEntryOrderBy.CREATED_AT_ASC)
    # search.setMediaTypeEqual(KalturaMediaType.VIDEO)  # Video only
    print "List videos, get the first one..."
    # Get 10 video entries, but we'll just use the first one returned
    entries = client.media.list(search, pager).objects
    entriesData = []
    for entry in entries:
        entryData = {}
        # Status
        status_codes = {
            KalturaEntryStatus.ERROR_IMPORTING: "ERROR_IMPORTING",
            KalturaEntryStatus.ERROR_CONVERTING: "ERROR_CONVERTING",
            KalturaEntryStatus.IMPORT: "IMPORT",
            KalturaEntryStatus.PRECONVERT: "PRECONVERT",
            KalturaEntryStatus.READY: "READY",
            KalturaEntryStatus.DELETED: "DELETED",
            KalturaEntryStatus.PENDING: "PENDING",
            KalturaEntryStatus.MODERATE: "MODERATE",
            KalturaEntryStatus.BLOCKED: "BLOCKED",
            KalturaEntryStatus.NO_CONTENT: "NO_CONTENT",
            KalturaEntryStatus.INFECTED: "virusScan.Infected",
            KalturaEntryStatus.SCAN_FAILURE: "virusScan.ScanFailure"
        }
        entryData['status'] = status_codes.get(entry.getStatus().getValue(), 'UNKNOWN')
        # Urls/Accessors
        entryData['url'] = entry.getDataUrl()
        entryData['download_url'] = entry.getDownloadUrl()
        entryData['thumbnail_url'] = entry.getThumbnailUrl()
        # Type (media type and source type)
        typelist = {
            KalturaMediaType.VIDEO: 'VIDEO',
            KalturaMediaType.IMAGE: 'IMAGE',
            KalturaMediaType.AUDIO: 'AUDIO',
            KalturaMediaType.LIVE_STREAM_FLASH: 'LIVE_STREAM_FLASH',
            KalturaMediaType.LIVE_STREAM_WINDOWS_MEDIA:
                'LIVE_STREAM_WINDOWS_MEDIA',
            KalturaMediaType.LIVE_STREAM_REAL_MEDIA: 'LIVE_STREAM_REAL_MEDIA',
            KalturaMediaType.LIVE_STREAM_QUICKTIME: 'LIVE_STREAM_QUICKTIME'
        }
        sourcetypelist = {
            KalturaSourceType.FILE : "FILE",
            KalturaSourceType.WEBCAM : "WEBCAM",
            KalturaSourceType.URL : "URL",
            KalturaSourceType.SEARCH_PROVIDER : "SEARCH_PROVIDER",
            KalturaSourceType.AKAMAI_LIVE : "AKAMAI_LIVE",
            KalturaSourceType.MANUAL_LIVE_STREAM : "MANUAL_LIVE_STREAM"
        }
        entryData['media_type'] = typelist.get(entry.getMediaType().getValue(), 'UNKNOWN')
        entryData['source_type'] = sourcetypelist.get(entry.getSourceType().getValue(), 'UNKNOWN')
        # ViewData
        entryData['plays'] = entry.getPlays()
        entryData['views'] = entry.getViews()
        entryData['rank'] = '%s, %s' % (entry.getRank(), entry.getTotalRank())
        # Video Properties
        entryData['width'] = entry.getWidth()
        entryData['height'] = entry.getHeight()
        entryData['duration'] = entry.getDuration()
        entryData['created'] = entry.getCreatedAt()
        entryData['updated'] = entry.getUpdatedAt()
        # Video Data
        entryData['name'] = entry.getName()
        entryData['description'] = entry.getDescription()
        entryData['tags'] = entry.getTags()
        # Search Text
        entryData['searchtext'] = entry.getSearchText()
        # Control
        entryData['startDate'] = entry.getStartDate()
        entryData['endDate'] = entry.getEndDate()
        # Extra KalturaMediaEntry data
        entryData['conversionQuality'] = entry.getConversionQuality()
        entryData['creditUrl'] = entry.getCreditUrl()
        entryData['creditUserName'] = entry.getCreditUserName()
        entryData['flavorParamsId'] = entry.getFlavorParamsIds()
        entryData['mediaDate'] = entry.getMediaDate()
        # Identifiers
        entryData['partner_id'] = entry.getPartnerId()
        entryData['user_id'] = entry.getUserId()
        if kaltura_id:
            if composite:
                entryData['id'] = 'kal:' + str(kaltura_id) + ':' + entry.getId()
            else:
                entryData['kaltura_id'] = str(kaltura_id)
                entryData['entry_id'] = entry.getId()
        else:
            entryData['id'] = entry.getId()
        entriesData.append(entryData)
    return entriesData


def get_entry(media_id, kaltura_id, client=None, width=120, height=120):
    settings = properties.load_kaltura_settings().get(kaltura_id)
    error = False
    error_message = None
    entry = None
    try:
        entry = client.media.get(media_id)
    except Exception as inst:
        error_message = str(inst)
        error = True
    entryData = {}
    if error:
        entryData['success'] = False
        entryData['message'] = error_message
    else:
        entryData['success'] = True
        typelist = {
            KalturaMediaType.VIDEO: 'VIDEO',
            KalturaMediaType.IMAGE: 'IMAGE',
            KalturaMediaType.AUDIO: 'AUDIO',
            KalturaMediaType.LIVE_STREAM_FLASH: 'LIVE_STREAM_FLASH',
            KalturaMediaType.LIVE_STREAM_WINDOWS_MEDIA:
                'LIVE_STREAM_WINDOWS_MEDIA',
            KalturaMediaType.LIVE_STREAM_REAL_MEDIA: 'LIVE_STREAM_REAL_MEDIA',
            KalturaMediaType.LIVE_STREAM_QUICKTIME: 'LIVE_STREAM_QUICKTIME'
        }
        entryData['media_type'] = typelist[entry.getMediaType().getValue()]
        # Urls/Accessors
        entryData['url'] = entry.getDataUrl()
        entryData['thumbnail_url_old'] = entry.getThumbnailUrl()
        url = "%s/api_v3/?service=thumbasset&action=list" % settings[
            'SERVICE_URL']
        data = urlencode({"filter:entryIdEqual": media_id, "action": "list"})
        req = urllib2.Request(url, data)
        content = urllib2.urlopen(req).read()
        entryData['ks'] = client.getKs()
        contentxml = ET.fromstring(content)
        thumb_id = ''
        for item in contentxml.findall('./result/objects/item'):
            tags = item.find('tags').text
            if tags and 'default_thumb' in tags:
                thumb_id = item.find('id').text
        thumbnail_url = "%s/p/%s/thumbnail/entry_id/%s" % (
            settings['SERVICE_URL'], settings['PARTNER_ID'], media_id)
        entryData['thumbnail_url'] = thumbnail_url + \
            "/width/%s/height/%s?%s" % (width, height, int(time.time()) )
        entryData['download_url'] = entry.getDownloadUrl()
        entryData['thumb_id'] = thumb_id
        # ViewData
        entryData['plays'] = entry.getPlays()
        entryData['views'] = entry.getViews()
        entryData['rank'] = (entry.getRank(), entry.getTotalRank())
        # Video Properties
        entryData['width'] = entry.getWidth()
        entryData['height'] = entry.getHeight()
        entryData['duration'] = entry.getDuration()
        entryData['created'] = entry.getCreatedAt()
        entryData['updated'] = entry.getUpdatedAt()
        # Video Data
        entryData['name'] = entry.getName()
        entryData['description'] = entry.getDescription()
        entryData['tags'] = entry.getTags()
        # Search Text
        entryData['searchtext'] = entry.getSearchText()
        # Control
        entryData['startDate'] = entry.getStartDate()
        entryData['endDate'] = entry.getEndDate()
        #entryData['status'] = entry.getStatus()
    return entryData


def del_entry(media_id, client=None):
    #error = False
    error_message = None
    try:
        client.media.delete(media_id)
        return {"success": True, "message": "MEDIA_DELETED"}
    except Exception as inst:
        error_message = str(inst)
        #error = True
    return {"success": False, "message": error_message}


def add_caption(captionfile,
                entry_id,
                capformat,
                label=None,
                language=None,
                default=False,
                client=None):
    '''Add caption and get the caption asset ID.
    Returns id used to identify the caption in kaltura.
    Language can be "auto" to attempt auto-detection.
    SRT file encoding is guessed and the file re-encoded to unicode.
    '''
    if client is None:
        raise Exception('Client cannot be None')
    # 0: ensure srt file is unicode-encoded
    if capformat == 'srt':
        convert_file_to_unicode(captionfile)
    # 1: set parameters for caption_asset
    caption_asset = KalturaCaptionAsset()
    if default:
        caption_asset.setIsDefault(KalturaNullableBoolean(KalturaNullableBoolean.TRUE_VALUE))
    if language == 'auto':
        suggested_lang = parse_caption_language(captionfile, capformat)
        autolang = difflib.get_close_matches(suggested_lang,
                                             LANGUAGE_LIST, n=1, cutoff=0.8)
        autolang = KalturaLanguage.EN if not autolang else autolang[0]
        caption_asset.setLanguage(KalturaLanguage(autolang))
    elif not language:
        caption_asset.setLanguage(KalturaLanguage(KalturaLanguage.EN))
    else:
        caption_asset.setLanguage(KalturaLanguage(language.capitalize()))
    # this might have to change to something like
    # KalturaLanguage.EN
    if label:
        caption_asset.setLabel(label)
    if capformat == 'srt':
        caption_asset.setFormat(KalturaCaptionType(KalturaCaptionType.SRT))
    elif capformat == 'dfxp':
        caption_asset.setFormat(KalturaCaptionType(KalturaCaptionType.DFXP))
    else:
        raise Exception('bad format %s' % capformat)
    # 2: attach the caption_asset to a media entry. Later we'll attach a file
    # to the caption_asset.
    caption_asset_service = KalturaCaptionAssetService(client)
    caption_asset = caption_asset_service.add(entry_id, caption_asset)
    # 3: upload file using uploadtoken, and get its token and then its
    # resource object
    upload_token = client.uploadToken.add()
    upload_token_detailed = client.uploadToken.upload(
        upload_token.getId(), file(captionfile, 'rb'))
    uploaded_resource = KalturaUploadedFileTokenResource(
        upload_token_detailed.getId())
    # 4: attach file to caption entry
    caption_asset = caption_asset_service.setContent(
        caption_asset.getId(), uploaded_resource)
    return caption_asset.getId()


def caption_dictify(caption_asset):
    caption_details = {}
    caption_details['id'] = caption_asset.getId()
    caption_details['language'] = caption_asset.getLanguage().getValue()
    caption_details['created_at'] = caption_asset.getCreatedAt()
    defval = caption_asset.getIsDefault()
    if 'getValue' in dir(defval):
        if defval.getValue() == KalturaNullableBoolean.TRUE_VALUE:
            caption_details['default'] = True
        else:
            caption_details['default'] = False
    else:
        if defval == KalturaNullableBoolean.TRUE_VALUE:
            caption_details['default'] = True
        else:
            caption_details['default'] = False
    # raise Exception, 'breaking bad'
    caption_details['name'] = caption_asset.getLabel()
    if caption_asset.getFormat().getValue() == KalturaCaptionType.SRT:
        caption_details['format'] = 'srt'
    elif caption_asset.getFormat().getValue() == KalturaCaptionType.DFXP:
        caption_details['format'] = 'dfxp'
    cap_stat = caption_asset.getStatus().getValue()
    stat_codes = {
        -1: 'ERROR',
        0: 'QUEUED',
        2: 'READY',
        3: 'DELETED',
        7: 'IMPORTING'
    }
    caption_details['status'] = stat_codes.get(cap_stat, 'UNKNOWN')
    return caption_details


def thumbnail_dictify(thumbasset):
    thumb_details = {}
    thumb_details['id'] = thumbasset.getId()
    thumb_details['width'] = thumbasset.getWidth()
    thumb_details['height'] = thumbasset.getHeight()
    thumb_details['size'] = thumbasset.getSize()
    thumb_details['created_at'] = thumbasset.getCreatedAt()
    thumb_details['default'] = True if thumbasset.getTags() == 'default_thumb' else False
    status_codes = {
         -1: 'ERROR',
         0: 'QUEUED',
         2: 'READY',
         3: 'DELETED',
         7: 'IMPORTING'
         }
    thumb_details['status'] = status_codes.get(thumbasset.getStatus().getValue(), 'UNKNOWN')
    return thumb_details


def get_caption(caption_id, client, url=True):
    caption_asset_service = KalturaCaptionAssetService(client)
    if url:
        return caption_asset_service.getUrl(caption_id)
    caption_asset = caption_asset_service.get(caption_id)
    return caption_dictify(caption_asset)


def get_entry_captions(entry_id, client, in_dict=True):
    caption_asset_service = KalturaCaptionAssetService(client)
    listfilter = KalturaAssetFilter()
    listfilter.entryIdEqual = entry_id
    pager = None
    response = caption_asset_service.list(listfilter, pager)
    caption_list = []
    for caption in response.objects:
        if in_dict:
            caption_entry = caption_dictify(caption)
            caption_entry['url'] = caption_asset_service.getUrl(caption.getId())
            caption_list.append(caption_entry)
        else:
            caption_list.append(caption)
    caption_list = sort_by_field(caption_list, "created_at", ascending=False)
    return caption_list


def update_caption(caption_id, language, capformat, name, default, client):
    caption_asset_service = KalturaCaptionAssetService(client)
    msgs = []
    caption_asset = KalturaCaptionAsset()
    if language:
        if True:
        # try:
            caption_asset.setLanguage(KalturaLanguage(language.capitalize()))
            msgs.append('language is ' + language)
        # except:
         #   msgs.append('unable to set language. ')
    if capformat:
        if capformat.lower() == 'srt':
            capformat = KalturaCaptionType.SRT
            msgs.append('format is srt')
        elif capformat.lower() == 'dfxp':
            capformat = KalturaCaptionType.DFXP
            msgs.append('format is dfxp')
        else:
            raise Exception('Unsupported format')
        caption_asset.setFormat(capformat)
    if name:
        caption_asset.setLabel(name)
        msgs.append('label (name) is ' + name)
    if default:
        msgs.append('default is true')
        caption_asset.setIsDefault(KalturaNullableBoolean(KalturaNullableBoolean.TRUE_VALUE))
    if True:
    # try:
        caption_asset_service.update(caption_id, caption_asset)
    # except Exception as e:
        # return {'success':False, 'messages':str(e)}
    return {'success': True, 'messages': msgs}


def del_caption(caption_id, client):
    caption_asset_service = KalturaCaptionAssetService(client)
    msgs = []
    try:
        caption_asset_service.delete(caption_id)
        msgs.append('Caption with id ' + caption_id + 'deleted')
        return {'success': True, 'message': msgs}
    except Exception as e:
        msgs.append('Deletion failed for caption with ID ' + caption_id)
        msgs.append('Exception: ' + str(e))
        return {'success': False, 'message': msgs}


def caption_set_default(caption_id, client):
    caption_asset_service = KalturaCaptionAssetService(client)
    msgs = []
    try:
        caption_asset_service.setAsDefault(caption_id)
        msgs.append('Caption with id ' + caption_id + 'set as default')
        return {'success': True, 'message': msgs}
    except Exception as e:
        msgs.append('setAsDefault failed for caption with ID ' + caption_id)
        msgs.append('Exception: ' + str(e))
        return {'success': False, 'message': msgs}


def remote_thumbs(client, thumb_id):
    if client is None:
            raise Exception("Client can not be None")
    thumbnail_asset_service = KalturaThumbAssetService(client)
    remote_paths = thumbnail_asset_service.getRemotePaths(thumb_id)
    return {"success": True, "paths": remote_paths}


if __name__ == '__main__':
    pass
