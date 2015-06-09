from KalturaCoreClient import KalturaMediaType
import magic  # python-magic library for mime type checking.
import os
import urllib

image_types = [
    'JPEG',
    'JPG',
    'PNG',
    'TIFF',
    'GIF',
    'JP2',
    'JPX',
    'JPF',
    'JPC',
    'J2K',
    'J2C',
    'DNG',
    'CRW',
    'CR2',
    'ZVI',
    'SVG',
    'BMP',
    'XIF'
]
audio_types = [
    'MP3',
    'WMA',
    'FLAC',
    'AIFF',
    'AAC',
    'WEBA',

]
video_types = [
    'AVI',
    'SWF',
    'FLV',
    'WMV',
    'MPEG',
    'ASF',
    '3GP',
    '3G2',
    'MOV',
    'MP4',
    'M4V',
    'OGG',
    'OGV',
    'F4V',
    'MKV',
    'WEBM'
]


def image_type(ext):
    for name in image_types:
        if ext.lower() == name.lower():
            return name
    return None


def video_type(ext):
    for name in video_types:
        if ext.lower() == name.lower():
            return name
    return None


def audio_type(ext):
    for name in audio_types:
        if ext.lower() == name.lower():
            return name
    return None


def check_type(ext):
    if video_type(ext):
        return 'VIDEO'
    elif audio_type(ext):
        return 'AUDIO'
    elif image_type(ext):
        return 'IMAGE'
    else:
        return None


def get_KalturaMediaType_from_pull_url(purl, default):
    '''
    will try to read first 10kb of stream and guess mime type,
    if can't, returns default.

    '''
    uo = urllib.urlopen(purl)
    try:
        magic_type = magic.from_buffer(
            uo.read(10240), mime=True).split('/')[0].upper()
        uo.close()
    except:
        print ('couldn\'t find type via magic, using ext...')
        magic_type = check_type(os.path.splitext(purl)[1].lstrip('.'))
    if magic_type == 'APPLICATION':
        print ('magic returned arbitrary type (application/x-octet-stream thingy), tryna use ext instead')
        magic_type = check_type(os.path.splitext(purl)[1].lstrip('.'))
    if magic_type == 'VIDEO':
        return KalturaMediaType.VIDEO
    elif magic_type == 'AUDIO':
        return KalturaMediaType.AUDIO
    elif magic_type == 'IMAGE':
        return KalturaMediaType.IMAGE
    elif default.lower() == 'video':
        print ('failed to get type, using default.')
        return KalturaMediaType.VIDEO
    elif default.lower() == 'audio':
        print ('failed to get type, using default.')
        return KalturaMediaType.AUDIO
    elif default.lower() == 'image':
        print ('failed to get type, using default.')
        return KalturaMediaType.IMAGE


def get_KalturaMediaType_from_file(path):
    ext = os.path.splitext(path)[1].lstrip('.')
    typename = check_type(ext)
    magic_type = magic.from_file(path, mime=True).split('/')[0].upper()
    if not typename:
        if magic_type == 'VIDEO':
            return KalturaMediaType.VIDEO
        elif magic_type == 'AUDIO':
            return KalturaMediaType.AUDIO
        elif magic_type == 'IMAGE':
            return KalturaMediaType.IMAGE
    elif typename == 'VIDEO':
        return KalturaMediaType.VIDEO
    elif typename == 'AUDIO':
        return KalturaMediaType.AUDIO
    elif typename == 'IMAGE':
        return KalturaMediaType.IMAGE


def get_specified_type(s):
    s = s[0].lower() if s else ''
    t = None
    if s == 'v':
        t = KalturaMediaType.VIDEO
    elif s == 'a':
        t = KalturaMediaType.AUDIO
    elif s == 'i':
        t = KalturaMediaType.IMAGE
    return t
