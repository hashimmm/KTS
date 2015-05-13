import simplejson


def upload_assets(path, medianame, kid, app):
    """Upload file and return entry id."""
    fd = open(path, 'rb')  # should probably change.
    servRESP = app.post(
        '/service/upload_file', 
        data={'medianame': path.split('/')[-1].split('.')[0],
              'file': (fd, path.split('/')[-1]),
              'kaltura_id': kid}
    )
    fd.close()
    if simplejson.loads(servRESP.data)['success']:
        return simplejson.loads(servRESP.data)['kaltura_id']#\
            #.encode('ascii', 'ignore')
    else:
        assert False, 'upload failed'


def upload_pullPath(pullPath, medianame, kid, app):
    """Upload file and return entry id."""
    servRESP = app.post(
        '/service/upload_file',
        data={'medianame': medianame,
              'pullPath': pullPath,
              'kaltura_id': kid}
    )
    if simplejson.loads(servRESP.data)['success']:
        return simplejson.loads(servRESP.data)['kaltura_id']#\
            #.encode('ascii', 'ignore')
    else:
        assert False, 'upload failed'


def delete(entry_id, kid, app):  # returns entry_id of deleted file
    del_response = app.get(
        '/service/del_media/?entry_id=%s&kaltura_id=%s' % (entry_id, kid))
    if simplejson.loads(del_response.data)['success']:
        return entry_id
    else:
        assert False, 'deletion failed'

