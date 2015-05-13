from behave import given, when, then

from testutils import upload_assets, upload_pullPath, delete


@given(u'some valid media file at {upload_method} {uri} of type {media_type}')
def given_upload_details(context, upload_method, uri, media_type):
    if upload_method == "path":
        context.upload_method = upload_assets
    elif upload_method == "URL":
        context.upload_method = upload_pullPath
    else:
        assert False, "upload_method ('file at X') must be one of URL or path."
    context.uri = uri
    context.media_type = media_type


@given(u'a medianame {media_name}')
def set_medianame(context, media_name):
    context.media_name = media_name

@when(u'client requests to upload this file')
def send_upload_request(context):
    context.entry_id = context.upload_method(
        context.uri, context.media_name, context.kaltura_id, context.app
    )
    context.uploads.append(context.entry_id)

@then(u'the entry exists on kaltura')
def entry_exists(context):
    # check if entry with id context.entry_id exists
    assert True

@then(u'entry is of type {type}')
def entry_type(context, type):
    # check entry type
    assert True

@when(u'client requests file metadata')
def get_media_meta(context):
    context.resp = context.app.get('/service/get_media/?entry_id=%s&kaltura_id=%s'
                                   % (context.entry_id, context.kaltura_id))

@when(u'attempting to delete this file')
def request_delete(context):
    delete(context.entry_id, context.kaltura_id, context.app)

@then(u'the file ceases to exist')
def entry_does_not_exist(context):
    context.uploads.remove(context.entry_id)
    # TODO: actually check if context.entry_id exists in kaltura
