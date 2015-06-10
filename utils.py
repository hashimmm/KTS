import logging
import shutil
import os
import sys
from logging.handlers import RotatingFileHandler
from functools import update_wrapper
from datetime import timedelta
import chardet
from flask import make_response, request, current_app


if sys.version_info[0] > 2:
    base_string_type = str
    rangegen = range
    def maybe_cast_to_unicode(s):
        return s
    import urllib.parse
    def urlencode(*args, **kwargs):
        return urllib.parse.urlencode(*args, **kwargs).encode('utf8')
else:
    base_string_type = basestring
    rangegen = xrange
    def maybe_cast_to_unicode(s):
        return unicode(s)
    from urllib import urlencode


def addFileLogger(logger_object, log_name, level=2):
    rotating_file_handler = RotatingFileHandler(log_name)
    rotating_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    logger_object.addHandler(rotating_file_handler)
    logger_object.level = level


def convert_file_to_unicode(filepath):
    utext = None
    with open(filepath, 'r') as fp:
        text = fp.read()
        encoding = chardet.detect(text)['encoding']
        utext = text.decode(encoding)
    if encoding.lower() == 'utf-8' or encoding.lower() == 'utf8':
        return
    shutil.copy(filepath, filepath + ".bu")
    try:
        with open(filepath, 'w') as fp:
            fp.write(utext.encode('utf8'))
    except:
        print ("Warning: Error during conversion to unicode!")
        os.remove(filepath)
        shutil.copy(filepath + ".bu", filepath)
    finally:
        os.remove(filepath + ".bu")


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, base_string_type):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, base_string_type):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
