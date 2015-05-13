import simplejson
from behave import given, then

from testutils import upload_assets


@given(u'some uploaded file')
def given_kaltura_media(context):
    if not 'uploads' in context.tags:
        assert False, "Step requires scenario/feature to have 'uploads' tag."
    if context.uploads:
        context.entry_id = context.uploads[0]
    else:
        context.entry_id = upload_assets('testing_assets/saudiplane.3gp',
                                         'testing_file', context.kaltura_id,
                                         context.app)
        context.uploads.append(context.entry_id)

@then(u'the server response status code is 200')
def status_code_OK(context):
    assert context.resp.status_code == 200

@then(u'the response contains \'success\': true')
def response_success_true(context):
    context.resp_json = simplejson.loads(context.resp.data)
    assert context.resp_json.get('success') == True
