import os

import simplejson
from behave import given, when, then


def caption_add(caption_file_and_name, caption_name, caption_language,
                entry_id, kid, app):
    resp = app.post('/service/add_caption/',
                    data={'entry_id': entry_id, 'file': caption_file_and_name,
                          'kaltura_id': kid, 'name': caption_name,
                          'language': caption_language})
    resp_json = simplejson.loads(resp.data)
    assert resp_json.get('success'), 'Failed while trying to add caption'
    assert resp_json.get('caption_id'), 'Response must contain caption_id'
    return resp_json['caption_id']


@given(u'a caption file at path {path}')
def given_caption_file(context, path):
    context.caption_file = open(path, 'rb')
    context.caption_file_name = os.path.basename(path)


@when(u'this caption file is applied to file')
def upload_caption_to_file(context):
    context.caption_id = caption_add(
        (context.caption_file, context.caption_file_name), "testcaption",
        "French", context.entry_id, context.kaltura_id, context.app
    )
    context.caption_file.close()


@when(u'caption list is requested')
def request_caption_list(context):
    r = context.app.get('/service/list_captions/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    context.captions_list = simplejson.loads(r.data)


@then(u'the caption list contains uploaded caption')
def caption_list_includes_new_caption(context):
    cap_format = os.path.splitext(context.caption_file_name)[-1].lstrip('.')
    cap_format = 'srt' if cap_format == 'srt' else 'dfxp'
    assert context.captions_list[0]['language'] == "French", \
        "expected language 'French', got %s" % context.captions_list[0]['language']
    assert context.captions_list[0]['name'] == "testcaption", \
        "expected name 'testcaption', got %s" % context.captions_list[0]['name']
    assert context.captions_list[0]['format'] == cap_format, \
        "expected format '%s', got %s" % (cap_format, context.captions_list[0]['format'])


@given(u'the file has captions')
def given_file_has_captions(context):
    # it SHOULD, since it's the same file as last scenario.
    r = context.app.get('/service/list_captions/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    context.captions_list = simplejson.loads(r.data)
    assert context.captions_list
    context.caption = context.captions_list[0]


@when(u'a caption is updated')
def request_update_caption(context):
    r = context.app.get('/service/update_caption/?kaltura_id=%s&caption_id=%s%s'
                         % (context.kaltura_id, context.caption['id'],
                            '&name=foobar&language=Malay'))
    assert simplejson.loads(r.data)['success'], "Update failed"


@then(u'the caption list contains updated details')
def caption_list_contains_updated_caption(context):
    r = context.app.get('/service/list_captions/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    context.captions_list = simplejson.loads(r.data)
    assert context.captions_list
    context.caption = context.captions_list[0]
    assert context.captions_list[0]['language'] == "Malay", \
        "expected language 'Malay', got %s" % context.captions_list[0]['language']
    assert context.captions_list[0]['name'] == "foobar", \
        "expected name 'foobar', got %s" % context.captions_list[0]['name']


@when(u'a caption is deleted')
def request_caption_delete(context):
    r = context.app.get('/service/remove_caption/?kaltura_id=%s&caption_id=%s'
                         % (context.kaltura_id, context.caption['id']))
    assert simplejson.loads(r.data)['success'], "Delete failed"


@then(u'the caption list no longer contains it')
def step_impl(context):
    r = context.app.get('/service/list_captions/?id=%s:%s'
                         % (context.kaltura_id, context.entry_id))
    captions_list = simplejson.loads(r.data)
    caption_ids = [x['id'] for x in captions_list]
    assert context.caption['id'] not in caption_ids, \
        "caption id still in caption list"
