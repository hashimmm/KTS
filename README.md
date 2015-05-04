KTS
===

KTS is an HTTP API that abstracts out the complexity of Kaltura's own API
 when dealing with common use cases such as getting an embeddable player for
 an entry id, getting metadata for a given entry id, CRUD for thumbnails and 
 captions, and a few more things.


## Quickstart #

To install dependencies, run `pip install -r requirements.txt`.
To run, `python server.py`.

`app` in server.py is a WSGI application, so any server that can work
  with WSGI applications will work with this too.
 For example, this may be started via gunicorn:
 `gunicorn --access-logfile='kts_access.log' --error-logfile='kts_error.log' -b 0.0.0.0:5000 server:app`

To configure KTS to work with your Kaltura account/server, you'll need to
 provide KTS with your Kaltura account integration settings. This can be done
 via an admin interface provided in KTS. The user name and password for it
 may be configured by setting the environment variables `KTS_ADMIN_USER` and
 `KTS_ADMIN_PWD` before starting KTS.

Also set the environment variable `UPLOAD_FOLDER` to a valid location before
 starting.

- Open up /login (eg. 127.0.0.1:5000/login) and log in with the username
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


## API #

### Usage #

Any API call pertaining to particular entries will accept "entry\_id" as
 a URL query parameter. It will also accept it as a form parameter for
 POST requests.

If multiple Kalturas have been defined, a "kaltura_id" may be specified
 in the same way as "entry\_id". Not specifying a "kaltura\_id" will always
 default to id 1.

POST API calls that were made to perform some action (upload file,
 thumbnail/caption CRUD) will return JSON with a field named "success"
 to indicate success.


### Endpoints #

- `/service/upload_file`  
   Upload any file. (via file post or from URL)  
   POST a file with its form parameter named "file". KTS will
    attempt to autodetect the media type.  
   Alternatively, provide a form or URL query parameter named "pullPath" and 
    KTS will communicate with Kaltura to obtain the media at the given URL.
    Media type can be either autodetected, or indicated as the "mediatype" 
    parameter -- image, video or audio. Defaults to video on failed autodetection.

- `/service/get_media/`  
   Get metadata for given entry id. Returned as JSON. 
   Also contains thumbnail URL. If "width" and "height" parameters are provided,
    thumbnail URL will be constructed for specified width and height.

- `/service/del_media/`  
   Delete an entry.

- `/service/get_player/`  
   Get embeddable player for entry.

- `/service/get_thumbnail_player/`  
   Get thumbnail selector player for entry. (Useful for old Kaltura servers).

- `/service/thumbnail_list/`  
   Returns list of thumbnails related to entry as JSON.  
   Returns a list of objects containing id, width, height, created\_at, default and 
    status per object.

- `/service/thumbnail_set_default/`  
   Set given thumbnail (specified by its id, provided as parameter "thumbnail\_id")
    as default for given entry.

- `/service/remove_thumbnail/`  
   Remove given thumbnail (specified by its id, provided as parameter "thumbnail\_id").

- `/service/update_thumbnail_file`  
   Update thumbnail for given entry by file. Provide file as form data for the 
    parameter "file". To set the uploaded file as default as well, provide
    the parameter "default" as a non-empty string.

- `/service/add_thumbnail_from_url/`  
   Add a thumbnail for given entry from URL specified as the "url" parameter.

- `/service/update_thumbnail_from_player`  
   Update thumbnail for videos by providing an offset. Also used internally by 
    the thumbnail selector player.  
   Given an entry id, and a query parameter "offset" in seconds, sets the
    thumbnail for the video to the frame at given time (offset).

- `/service/list_captions/`  
   Returns list of captions related to entry as JSON.  
   Returns a list of objects containing id, language, created\_at, default, 
    name, format and status.

- `/service/add_caption/`  
   Add caption for given entry by file. Provide file as form data for the 
    parameter "file". To set the uploaded file as default as well, provide
    the parameter "default" as a non-empty string. KTS will attempt to
    auto-detect caption format. Also, specify language as the parameter 
    "language", eg. English. May be specified as "auto" to attempt language 
    auto-detection.

- `/service/remove_caption/`  
   Remove given caption (specified by its id, provided as parameter "caption\_id").

- `/service/set_caption_as_default/`  
   Set given caption (specified by its id, provided as parameter "caption\_id")
    as default for given entry.


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
