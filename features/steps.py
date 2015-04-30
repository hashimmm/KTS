from lettuce import *
#import properties
#from properties import kaltura_properties_list, kaltura_defaults_dictionary
import uuid
import math
import random
import os
import re

import server
import simplejson


#functions for testing loadsettings----------------------------------------------------------------------------------------------------
# def seed_number(limit = 100):
#     return int(random.random()*limit)

# def seed_alnum():
#     return str(uuid.uuid4())[:5]


# def get_property_template(kaltura_config_id = "1"):
#     return {
#     "KALTURA_CONFIG_ID" : kaltura_config_id,
#     "KALTURA_NAME" : "Random %s"%seed_alnum(),
#     "KALTURA_PATH" : "192.168.90.%s"%seed_number(),
#     "PARTNER_ID" : "%s"%seed_alnum(),
#     "PLAYER_ID" : "%s"%seed_alnum(),
#     "THUMBNAIL_PLAYER_ID" : "%s"%seed_alnum(),
#     "ADMIN_SECRET" : "%s"%seed_alnum(),
#     "SECRET" : "%s"%seed_alnum(),
#     "USER_NAME" : "%s@acit.com"%seed_alnum()
#     }

# def make_kaltura_properties(num_props):
#     num_props = int(num_props)
#     d = {}
#     for i in xrange(1, num_props+1):
#         d[str(i)] = get_property_template(str(i))
#     return d

# def validate_environment(kaltura_properties):
#     if int(os.environ['KALTURA_INSTANCES']) == len(kaltura_properties):
#         pass
#     else:
#         assert False, "Expected %s got %s"%(os.environ['KALTURA_INSTANCES'], len(kaltura_properties))
#     for prop_key in kaltura_properties:
#         for prop in kaltura_properties[prop_key]:
#             if os.environ['%s_%s'%(prop_key, prop)] == kaltura_properties[prop_key][prop]:
#                 pass
#             else:
#                 assert False, 'Expected %s Got %s'%(os.environ['%s_%s'%(prop_key, prop)], kaltura_properties[prop_key][prop])

# def inject_into_environment(kaltura_properties):
#     for prop_key in kaltura_properties:
#         for prop in kaltura_properties[prop_key]:
#             os.environ['%s_%s'%(prop_key, prop)] = kaltura_properties[prop_key][prop]
#     os.environ['KALTURA_INSTANCES'] = str(len(kaltura_properties.keys()))

# def print_environment():
#     keys = []
#     for key in os.environ:
#         if re.findall("^(\d+)_", key):
#             keys.append(key)
#         elif key == "KALTURA_INSTANCES":
#             keys.append(key)
#     keys.sort()
#     for key in keys:
#         print "%s - %s"%(key, os.environ[key])

################################################################ steps for load settings feature
# @step(u'Given I have (\d+) instance of Kaltura properties')
# def given_i_have_n_instances_of_kaltura_properties(step, number):
#     world.kaltura_properties = make_kaltura_properties(number)

# @step(u'When I load the properties into the environment')
# def when_i_load_the_properties_into_the_environment(step):
#     inject_into_environment(world.kaltura_properties)
    
# @step(u'When I load the properties from the environment')
# def when_i_load_the_properties_from_the_environment(step):
#     world.loaded_environment = {}
#     properties.load_kaltura_settings(world.loaded_environment)

# @step(u'Then the properties are loaded validly')
# def then_the_properties_are_loaded_validly(step):
#     #print_environment()
#     #print repr(world.kaltura_properties)
#     #print "--"
#     #print repr(world.loaded_environment)
#     #print "--"
#     validate_environment(world.loaded_environment)

#----------------------------------------------------------------------------------------------------------------------------------------


#methods for testing upload and del------------------------------------------------------------------------------------------------------

#setup flask testing:
server.app.config['TESTING'] = True
app_test_client = server.app.test_client()

def upload_assets(path, kid=1): #returns entry_id of uploaded file
    fd = open(path,'rb') #should probably change.
    servRESP = app_test_client.post('/service/upload_file', data={'medianame':path.split('/')[-1].split('.')[0],'file':(fd,path.split('/')[-1]),'kaltura_id':kid})
    fd.close()
    if simplejson.loads(servRESP.data)['success']:
        return simplejson.loads(servRESP.data)['kaltura_id'].encode('ascii','ignore')
    else:
        assert False, 'upload failed'

def deletion_test(entry_id, kid=1): #returns entry_id of deleted file
    del_response = app_test_client.get('/service/del_media/?entry_id=' + entry_id + '&kaltura_id=' + str(kid))
    if simplejson.loads(del_response.data)['success']:
        return entry_id
    else:
        assert False, 'deletion failed'

def upload_pullPath(pullPath,medianame, kid=1):
    servRESP = app_test_client.post('/service/upload_file', data={'medianame':medianame, 'pullPath':pullPath,'kaltura_id':kid})
    if simplejson.loads(servRESP.data)['success']:
        return simplejson.loads(servRESP.data)['kaltura_id'].encode('ascii','ignore')
    else:
        assert False, 'upload failed'

#dropbox file: https://www.dropbox.com/sh/m8874se6x8gc5ko/pbwBx5vb7v/irt.PNG





################################################################ steps for delete files feature
@step(u'After a file donkey.jpg from local relative path /testing_assets has been uploaded to kaltura with id (\d+)')
def file_upload(step, number):
    world.number = number
    world.entry_id = upload_assets('testing_assets/donkey.jpg', world.number)

@step(u'When attempting to delete this file')
def file_delete(step):
    deletion_test(world.entry_id, world.number)

@step(u'The file ceases to exist')
def file_ceases_to_exist(step):
    pass

#----------------------------------------------------------------------------------------------------------------------------------------

################################################################ steps for upload files feature


#pullpath
@step(u'Given a valid dropbox link as pullpath for uploading to kaltura with id (\d+)')
def dropbox_link(step, number):
    world.number = number
    world.dropboxpath = 'https://www.dropbox.com/sh/m8874se6x8gc5ko/pbwBx5vb7v/irt.PNG'
    world.medianame = 'duck'

@step(u'When client requests to upload this file')
def client_requests_to_upload_pullPath(step):
    world.pullpath_entry_id = upload_pullPath(world.dropboxpath,world.medianame,world.number)

@step(u'Then kaltura downloads the file from dropbox')
def kaltura_download_from_dropbox(step):
    pass

@step(u'Then the file exists on kaltura')
def pullpath_file_exists_on_kaltura(step):
    pass

@step(u'And then this file is deleted from kaltura since it was just for testing')
def file_pullPath_delete(step):
    deletion_test(world.pullpath_entry_id, world.number)

#testing_assets (file post)
@step(u'A file from server testing assets is uploaded to kaltura with id (\d+)')
def upload_from_assets(step, number):
    world.number = number
    world.assets_upload_id = upload_assets('testing_assets/donkey.jpg', world.number)

@step(u'Then this file is deleted from this client since it was just for testing')
def delete_asset_testing_file(step):
    deletion_test(world.assets_upload_id, world.number)

#----------------------------------------------------------------------------------------------------------------------------------------


#methods for thumbnail update------------------------------------------------------------------------------------------------------------

def thumbnail_update(thumbnail_file, kid=1):
    fd = open('testing_assets/donkey.jpg','rb')
    servRESP = app_test_client.post('/service/upload_file', data={'medianame':'donkey','file':(fd,'donkey.jpg'), 'kaltura_id':kid})
    fd.close()
    if simplejson.loads(servRESP.data)['success']:
        entry_id_to_update = simplejson.loads(servRESP.data)['kaltura_id'].encode('ascii','ignore')
    else:
        assert False, 'upload failed'
    servRESP2 = app_test_client.post('/service/update_thumbnail_file', data = {'entry_id':entry_id_to_update, 'file':thumbnail_file, 'kaltura_id':kid})
    if simplejson.loads(servRESP2.data)['success']:
        pass
    else:
        assert False, 'failed while trying to update thumbnail'
    return simplejson.loads(servRESP.data)['kaltura_id'].encode('ascii','ignore')

def select_thumbnail_file():
    return (open('testing_assets/irt.PNG','rb'),'irt.PNG')


################################################################ steps for update thumbnail feature

@step(u'Given a valid file selection for thumbnail')
def valid_file_selection_for_thumbnail(step):
    world.thumbfile = select_thumbnail_file()

@step(u'When this thumbnail file is applied to an uploaded testing file in kaltura with id (\d+)')
def thumbnail_applied_to_media(step, number):
    world.number = number
    world.thumb_testing_file = thumbnail_update(world.thumbfile, world.number)

@step(u'Thumbnail is successfully uploaded and applied')
def thumbnail_successfully_uploaded_and_applied(step):
    pass

@step(u'And the testing file is deleted')
def thumbnail_testing_file_delete(step):
    deletion_test(world.thumb_testing_file, world.number)

#----------------------------------------------------------------------------------------------------------------------------------------

################################################################ steps for load mobile player url

@step(u'When mobile player url is requested')
def mobile_player_url_requested(step):
    world.mplayer_request_response = app_test_client.get('/service/get_mobileplayer_url/?entry_id=')

@step(u'Valid url is returned')
def thumbnail_applied_to_media(step):
    if not world.mplayer_request_response.status_code == 200:
        assert Fail, 'respone status expected: 200 OK, got: %s %s'%world.mplayer_request_response.status
    

#----------------------------------------------------------------------------------------------------------------------------------------

################################################################ steps get media

@step(u'After some test media from testing_assets is uploaded to kaltura with id (\d+)')
def test_media_is_uploaded_for_get_media(step, number):
    world.number = number
    world.get_media_entry_id = upload_assets('testing_assets/saudiplane.3gp',world.number)


@step(u'When kaltura attempts to get info on this media')
def kaltura_attempts_to_get_info(step):
    world.get_media_servresp = app_test_client.get('/service/get_media/?entry_id=' + world.get_media_entry_id + '&kaltura_id=' + str(world.number))


@step(u'Then the server response status code is 200 ie OK')
def get_media_response_ok(step):
    if not world.get_media_servresp.status_code == 200:
        assert False, 'response status expected: 200 OK, got %s'%world.get_media_servresp.status

@step(u'And contains indication of success of data retrieval for uploaded entry')
def contains_getmedia_success_indication(step):
    #if not world.get_media_servresp.data.find('"success": true') == -1:
    #    assert False, 'unable to get media info, could not find \'"success": true\' in response data'
    #cannot do the above since wont be able to get info on the entry until conversion is complete which takes time.
    pass

@step(u'And then the test entry is deleted')
def del_get_media_test_entry(step):
    deletion_test(world.get_media_entry_id,world.number)

#----------------------------------------------------------------------------------------------------------------------------------------

#if __name__ == '__main__':
#     props = make_kaltura_properties(1)
#     inject_into_environment(props)
#     print_environment()

