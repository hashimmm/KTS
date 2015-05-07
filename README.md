KTS
===

KTS is an HTTP API that abstracts out the complexity of Kaltura's own API
 when dealing with common use cases such as getting an embeddable player for
 an entry id, getting metadata for a given entry id, CRUD for thumbnails and 
 captions, uploading media from file or uploading media from a URL.

It includes helpful default behavior like auto-detecting media type during
 upload, auto-detecting caption type during upload, and even optionally
 auto-detecting caption language.


## Quickstart #

To install dependencies, run `pip install -r requirements.txt`.
To run, `python server.py`.

`app` in server.py is a WSGI application, so any server that can work
  with WSGI applications will work with this too.
 For example, this may be started via gunicorn:
 `gunicorn --access-logfile='kts_access.log' --error-logfile='kts_error.log' -b 0.0.0.0:6500 server:app`

To configure KTS to work with your Kaltura account/server, you'll need to
 provide KTS with your Kaltura account integration settings. This can be done
 via an admin interface provided in KTS. The user name and password for it
 may be configured by setting the environment variables `KTS_ADMIN_USER` and
 `KTS_ADMIN_PWD` before starting KTS.

Also set the environment variable `UPLOAD_FOLDER` to a valid location before
 starting.

- Open up /login (eg. 127.0.0.1:6500/login) and log in with the username
   and password.
- Go to Manage Configurations > Add new Kaltura instance
- Enter any relevant name, the path to your Kaltura server (www.kaltura.com
   works for kaltura.com users), the player ID you wish to use as your player
   and your account integration settings as well as your email address (username).
- For thumbnail selector player, set up any player to have a custom button
   (custom button 1 in the custom buttons section in the flash player creation
   studio) and give it some relevant text (eg. Capture Thumbnail). This may
   be redundant for users of newer versions of Kaltura since that has such an
   option for the player already provided in the "Universal" player studio.
- To find your integration settings in to the Kaltura Management Console '
  on your Kaltura server and go to Settings -> Integration Settings.
  "Administrator Secret" corresponds to the field of the same name, "User Secret"
  corresponds to "Secret".
  
That's it; with this done, you can use the KTS API to work with Kaltura.

### API #

*Usage notes*:

- For API calls that require an entry id, specify it as `kaltura_id:entry_id` as a
   form parameter or url query parameter called `id` where `kaltura_id` is the integer
   ID of the kaltura instance at `http://your_kts_server:port/view_configs/`.
- For API calls that refer only to the kaltura server but do not require an entry id
   (eg. uploading a file, or updating caption/thumbnail in which case the caption or
   thumbnail id is required), specify the kaltura id as `kaltura_id` in a form parameter
   or url query parameter.
- POST API calls that were made to perform some action (upload file,
   thumbnail/caption CRUD) will return JSON with a field named "success"
   to indicate success.

**Upload via url**  
```
$ curl -X POST -F "pullPath=http://upload.wikimedia.org/wikipedia/commons/5/5b/Image_placeholder_upright.png" "http://localhost:6500/service/upload_file?medianame=arbitrary_image&kaltura_id=1"
```  
```
{"kaltura_id": "0_s4cdprj6", "messages": ["Kaltura will now pull and process the video"], "success": true}
```  

**Upload file**  
```
$ curl -X POST -F file=@something.3gp "http://localhost:6500/service/upload_file?medianame=arbitrary_video&kaltura_id=1"
```  
```
{"kaltura_id": "0_6516k95g", "messages": ["File Uploaded locally", "Uploaded to Kaltura"], "success": true}
```  

**Get embeddable player**  
```
$ curl "http://localhost:6500/service/get_player/?id=1:0_mebfxjnh"
```  
(returns html)

**Get embeddable thumbnail selector player**  
```
$ curl "http://localhost:6500/service/get_thumbnail_player/?id=1:0_mebfxjnh"
```  
(returns html)

**Get media metadata**  
```
$ curl "http://localhost:6500/service/get_media/?id=1:0_mebfxjnh"
```  
```
{"startDate": null, "endDate": null, "rank": [0.0, 0], "height": 144, "duration": 25, "plays": 0, "tags": "", "download_url": "http://media2.stage.artstor.org/p/99/sp/9900/raw/entry_id/0_mebfxjnh/version/0", "width": 176, "media_type": "VIDEO", "updated": 1430991226, "searchtext": "  something ", "description": "", "views": 0, "thumb_id": "0_j0k95rmz", "name": "something", "success": true, "created": 1422339281, "url": "http://media2.stage.artstor.org/p/99/sp/9900/flvclipper/entry_id/0_mebfxjnh/version/0", "ks": "ZDY4MzM3ZmIwYmRhNmYwNGJhZTQzNmE5MWI0MDNiZmM4ZjIxNDAxNHw5OTs5OTsxNDMxMDgwNTIwOzI7MTQzMDk5NDEyMC40O2l0YWxhYXRAYWNpdC5jb207Ozs=", "thumbnail_url_old": "http://media2.stage.artstor.org/p/99/sp/9900/thumbnail/entry_id/0_mebfxjnh/version/100001", "thumbnail_url": "http://media2.stage.artstor.org/p/99/thumbnail/entry_id/0_mebfxjnh/width/120/height/120?1430994122"}
```  

**Delete media**  
```
$ curl -X POST "http://localhost:6500/service/del_media/?id=1:0_s4cdprj6"
```  
```
{"message": "MEDIA_DELETED", "success": true}
```  

**Add caption**  
```
$ curl -F file=@sample.srt -F id=1:0_mebfxjnh -F name=testcaption http://localhost:6500/service/add_caption/
```  
```
{"messages": ["File Uploaded locally", "caption added, id: 0_c8lcdomn"], "success": true}
```  

**List captions**  
```
$ curl -F id=1:0_mebfxjnh http://localhost:6500/service/list_captions/
```  
```
[{"status": "READY", "name": "testcaption", "language": "English", "format": "srt", "default": false, "created_at": 1430990289, "url": "http://media2.stage.artstor.org/api_v3/index.php/service/caption_captionAsset/action/serve/captionAssetId/0_c8lcdomn/ks/MzNhYTgzMmRlMjE3ZThjZjE1MTFmZmNiMmFhM2UyNzc3NmYzNmU5OXw5OTs5OTsxNDMxMDc2NzI2OzA7MTQzMDk5MDMyNi4zOztkb3dubG9hZDowX21lYmZ4am5oOzs=", "id": "0_c8lcdomn"}]
```  

**Set caption as default**  
```
$ curl -F caption_id=0_c8lcdomn -F kaltura_id=1 http://localhost:6500/service/set_caption_as_default/
```  
```
{"message": ["Caption with id 0_c8lcdomnset as default"], "success": true}
```  

**Update caption**  
```
$ curl -F caption_id=0_c8lcdomn -F kaltura_id=1 -F default=true -F language=Arabic -F name=changedfortesting http://localhost:6500/service/update_caption/
```  
```
{"messages": ["language is Arabic", "label (name) is changedfortesting", "default is true"], "success": true}
```  

**Delete caption**  
```
$ curl -F caption_id=0_c8lcdomn -F kaltura_id=1 http://localhost:6500/service/remove_caption/
```  
```
{"message": ["Caption with id 0_c8lcdomndeleted"], "success": true}
```  

**List thumbnails**  
```
$ curl http://localhost:6500/service/thumbnail_list/?id=1:0_mebfxjnh
```  
```
[{"status": "READY", "default": true, "created_at": 1422339963, "height": 144, "width": 176, "url": "http://media2.stage.artstor.org/api_v3/index.php/service/thumbAsset/action/serve/thumbAssetId/0_v6riwr89/ks/M2E0MGZjYzE2ZTNmMGRjMDA2ZjdlNGNkNDFjNjIxMTY4ZDM3ZGVlZXw5OTs5OTsxNDMxMDc3MzEyOzA7MTQzMDk5MDkxMi4xNzs7ZG93bmxvYWQ6MF9tZWJmeGpuaDs7", "id": "0_v6riwr89", "size": 4633}]
```  

**Add thumbnail from url**  
```
$ curl "http://localhost:6500/service/add_thumbnail_from_url/?id=1:0_mebfxjnh&url=http%3A//upload.wikimedia.org/wikipedia/commons/5/5b/Image_placeholder_upright.png"
```  
```
{"message": ["ThumbAsset added to entry, id 0_j0k95rmz", "url http://upload.wikimedia.org/wikipedia/commons/5/5b/Image_placeholder_upright.png applied to thumbnail with id 0_j0k95rmz"], "success": true}
```  

**Set thumbnail as default**  
```
$ curl "http://localhost:6500/service/thumbnail_set_default/?kaltura_id=1&thumbnail_id=0_j0k95rmz"
```  
```
{"message": ["Thumbnail with id 0_j0k95rmz set as default"], "success": true}
```  

**Add thumbnail from file**  
```
$ curl -F file=@irt.PNG http://localhost:6500/service/update_thumbnail_file?id=1:0_mebfxjnh
```  
```
{"messages": [], "kaltura_id": "0_qj22c05k", "success": true}
```  

**Delete thumbnail**  
```
$ curl "http://localhost:6500/service/remove_thumbnail/?kaltura_id=1&thumbnail_id=0_qj22c05k"
```  
```
{"message": ["Thumbnail with id 0_qj22c05k deleted"], "success": true}
```  


## In progress #
- All player endpoints will be modified to accept flavor ids. Otherwise eg.
   the mobileplayer url endpoint is somewhat of limited use.
- API autodocs as well as a /help endpoint to obtain API docs.
- Replacing deprecated API calls with newer versions.
- Searching
- Allowing user to specify filters/sort ordering in things like thumbnail list 
   instead of just having some default.


## Acknowledgments #
Thanks to the following people for a ton of help with this, otherwise KTS 
 wouldn't even have existed.

- [Iqbal Bhatti](https://github.com/afrobeard)
