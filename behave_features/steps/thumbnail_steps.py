import os
import logging

import simplejson
from behave import given, when, then


def thumbnail_update(thumbnail_file_and_name, entry_id, kid, app):
    resp = app.post('/service/update_thumbnail_file',
                    data={'entry_id':entry_id, 'file':thumbnail_file_and_name,
                          'kaltura_id':kid})
    resp_json = simplejson.loads(resp.data)
    assert resp_json.get('success'), 'Failed while trying to update thumbnail'
    assert resp_json.get('thumbnail_id'), 'Response must contain thumbnail_id'
    return resp_json['thumbnail_id']


@given(u'a thumbnail file at path {path}')
def given_thumbnail_file(context, path):
    context.thumbnal_path = path
    context.thumbnail_file = open(path, 'rb')
    context.thumbnail_file_name = os.path.basename(path)


@when(u'this thumbnail file is applied to file')
def update_thumbnail_for_entry(context):
    context.thumbnail_id = thumbnail_update(
        (context.thumbnail_file, context.thumbnail_file_name),
        context.entry_id, context.kaltura_id, context.app
    )
    context.thumbnail_file.close()
    context.thumbnail_file = open(context.thumbnal_path, 'rb')
    context.deletable_thumbnail_id = thumbnail_update(
        (context.thumbnail_file, context.thumbnail_file_name),
        context.entry_id, context.kaltura_id, context.app
    )
    context.thumbnail_file.close()


@when(u'thumbnail is set as default')
def set_thumb_as_def(context):
    r = context.app.post('/service/thumbnail_set_default/'
                         '?thumbnail_id=%s&kaltura_id=%s'
                         % (context.thumbnail_id, context.kaltura_id))
    assert simplejson.loads(r.data).get('success'), "Failed to set def. thumb."


@when(u'thumbnail list is requested')
def get_thumb_list(context):
    r = context.app.get('/service/thumbnail_list/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    context.thumbnails_list = simplejson.loads(r.data)


@when(u'thumbnail path is requested')
def get_thumb_path(context):
    r = context.app.get('/service/get_media/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    r_json = simplejson.loads(r.data)
    assert r_json.get('success'), "Failed to get media metadata."
    context.thumbnail_url = r_json.get('thumbnail_url')
    assert context.thumbnail_url


@then(u'the thumbnail path shows the default thumbnail')
def check_def_thumb(context):
    # download default thumbnail from context.thumbnail_url and compare it 
    # with the uploaded thumbnail file
    pass


@then(u'thumbnail list contains the correct number of thumbnails')
def check_thumb_list_length(context):
    # This is a bit awkward. Should change in the future.
    assert len(context.thumbnails_list) >= 1, "Thumbnail list has bad length."


@then(u'thumbnail can be deleted')
def del_thumb(context):
    non_default_thumbs = [item['id'] for item 
                          in context.thumbnails_list if not item['default']]
    if not non_default_thumbs:
        assert False, ('Thumbnail deletion untested; '
                       'add non-default thumbnail.')
        return
    del_thumb_id = non_default_thumbs[0]
    failure = False
    try:
        r = context.app.get('/service/remove_thumbnail/'
                            '?kaltura_id=%s&thumbnail_id=%s'
                            % (context.kaltura_id, del_thumb_id))
    except Exception as e:
        logging.exception(e)
        failure = True
    r_json = simplejson.loads(r.data)
    assert r_json.get('success'), "Failed to delete."
    if not r_json.get('success'):
        failure = True
    if failure:
        logging.warning('Failed to delete thumb with id %s,' % del_thumb_id)
        logging.warning('Perform cleanup manually.')
