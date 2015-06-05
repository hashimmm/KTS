import os
import sqlite3
import simplejson
from pprint import pprint

try:
    import fcntl
except ImportError:
    class FCNTL(object):
        LOCK_EX = None

        def lockf(*args, **kwargs):
            pass

    fcntl = FCNTL()

DEFAULT_PORT = 6500
DEFAULT_UPLOAD_FOLDER = ""
DEFAULT_KALTURA_PATH = ""
DEFAULT_PARTNER_ID = ""
DEFAULT_PLAYER_ID = ""
DEFAULT_THUMBNAIL_PLAYER_ID = ""
DEFAULT_ADMIN_SECRET = ""
DEFAULT_SECRET = ""
DEFAULT_USER_NAME = ""
DEFAULT_SERVICE_URL = "http://127.0.0.1:%s" % DEFAULT_PORT
DEFAULT_KTS_ADMIN_USER = 'ktsadmin'
DEFAULT_KTS_ADMIN_PWD = 'ktsadmin'
DEFAULT_DEBUG_MODE = ''
DEFAULT_MOBILE_PLAYER_FLAVOR = ''
DEFAULT_KALTURA_DEFINITIONS_DB = 'kaldefs.db'

kaldefsfile = os.environ.get('KALTURA_DEFINITIONS_DB',
                             DEFAULT_KALTURA_DEFINITIONS_DB)
kaldefsdb = None

kaltura_defaults_dictionary = {
    "KALTURA_NAME": "Anonymous monkey",
    "KALTURA_PATH": "www.example.com",
    "PARTNER_ID": "99",
    "PLAYER_ID": "6709454",
    "THUMBNAIL_PLAYER_ID": "6709455",
    "ADMIN_SECRET": "a5c1cb2c9bcd66b825db68533c3ec792",
    "SECRET": "8e81fdce8808cbf71b8dc6c8ee258842",
    "USER_NAME": "foo@example.com",
    "KALTURA_INSTANCES": 1,
    "MOBILE_PLAYER_FLAVOR": ""
}

# the order of the follwing is important.
config_table_creation_query = """
    CREATE TABLE configurations (KALTURA_CONFIG_ID INTEGER PRIMARY KEY,
                                 KALTURA_NAME text,
                                 KALTURA_PATH text,
                                 PARTNER_ID int,
                                 PLAYER_ID int,
                                 THUMBNAIL_PLAYER_ID int,
                                 ADMIN_SECRET text,
                                 SECRET text,
                                 USER_NAME text,
                                 MOBILE_PLAYER_FLAVOR text
                                 )
    """

"""
Loading Scheme

Makes a map of id => Settings Map
"""

# the order of the following is important.
kaltura_properties_list = ['KALTURA_CONFIG_ID', 'KALTURA_NAME', 'KALTURA_PATH',
                           'PARTNER_ID', 'PLAYER_ID', 'THUMBNAIL_PLAYER_ID',
                           'ADMIN_SECRET', 'SECRET', 'USER_NAME',
                           'MOBILE_PLAYER_FLAVOR']


def load_kals_from_env(SETTINGS, cur):
    kaltura_count = int(os.environ.get("KALTURA_INSTANCES", "1"))
    if kaltura_count >= 1:
        for counter in xrange(1, kaltura_count + 1):
            accessors = ['k_%d_%s' % (counter, kal_prop)
                         for kal_prop in kaltura_properties_list]
            # Because the Global Dictionary will be populated with this guy
            config_id = 'k_%d_%s' % (counter, 'KALTURA_CONFIG_ID')
            temp_kaltura_config_map = {}
            for (accessor_term, accessor_accessor) in \
                    zip(kaltura_properties_list, accessors):
                temp_kaltura_config_map[accessor_term] = os.environ.get(
                    accessor_accessor,
                    kaltura_defaults_dictionary.get(accessor_term)
                )
            # temp_kaltura_config_map['SERVICE_URL'] = "Donkey"
            temp_kaltura_config_map['SERVICE_URL'] = \
                "http://" + temp_kaltura_config_map.get(
                    'KALTURA_PATH', DEFAULT_KALTURA_PATH
                )
            SETTINGS[config_id.split("_")[1]] = temp_kaltura_config_map
            values = [config_id.split("_")[1]] + \
                     [temp_kaltura_config_map.get(kaltura_properties_list[j])
                      for j in xrange(1, len(kaltura_properties_list))]
            cur.execute(
                "insert into configurations values(?,?,?,?,?,?,?,?,?,?)",
                values)
    else:
        raise Exception(
            "Kaltura Count Must be Positive, got %d" % kaltura_count
        )
    return SETTINGS


def load_kaltura_settings(SETTINGS=None):
    lockfile = open('kts-config.lock', 'w')
    fcntl.lockf(lockfile, fcntl.LOCK_EX)
    if SETTINGS is None:
        SETTINGS = {}
    kaldefsdb = sqlite3.connect(kaldefsfile)
    cur = kaldefsdb.cursor()
    cur.execute(
        "select count(*) from sqlite_master "
        "where type='table' and name='configurations'")
    existence = cur.fetchall()[0][0]
    if existence == 1:
        cur.execute("""select KALTURA_CONFIG_ID,
                                 KALTURA_NAME,
                                 KALTURA_PATH,
                                 PARTNER_ID,
                                 PLAYER_ID,
                                 THUMBNAIL_PLAYER_ID,
                                 ADMIN_SECRET,
                                 SECRET,
                                 USER_NAME,
                                 MOBILE_PLAYER_FLAVOR from configurations""")
        for row in cur:
            kal_id = str(row[0])
            SETTINGS[kal_id] = {kaltura_properties_list[i]: str(row[i]) for i in
                                xrange(1, len(row))}
            # a.k.a dict( zip( kaltura_properties_list[1:], row[1:] ) )
            SETTINGS[kal_id]['SERVICE_URL'] = "http://" + SETTINGS[kal_id][
                'KALTURA_PATH']

    elif existence == 0:
        cur.execute(config_table_creation_query)
        SETTINGS = load_kals_from_env(SETTINGS, cur)
        kaldefsdb.commit()

    cur.close()
    kaldefsdb.close()
    lockfile.close()
    return SETTINGS


def add_kaltura(values):
    try:
        lockfile = open('kts-config.lock', 'w')
        fcntl.lockf(lockfile, fcntl.LOCK_EX)

        kaldefsdb = sqlite3.connect(kaldefsfile)
        cur = kaldefsdb.cursor()

        cur.execute("select count(*) from configurations")
        count = cur.fetchall()[0][0]
        if count == 0:
            cur.execute(
                "insert into configurations values(1,?,?,?,?,?,?,?,?,?)",
                values)
        else:
            cur.execute(
                "insert into configurations values(NULL,?,?,?,?,?,?,?,?,?)",
                values)

        kaldefsdb.commit()
        kaltura_id = cur.lastrowid
        cur.close()
        kaldefsdb.close()
        lockfile.close()

        return simplejson.dumps({'success': True, 'kaltura_id': kaltura_id})
    except Exception as e:
        return simplejson.dumps(
            {'success': False, 'messages': [repr(e), str(e)]})


def rem_kaltura(kaltura_id):
    try:
        msgs = []
        success = True
        if kaltura_id is None or kaltura_id == '':
            success = False
            msgs.append('KALTURA_CONFIG_ID must be provided')
        lockfile = open('kts-config.lock', 'w')
        fcntl.lockf(lockfile, fcntl.LOCK_EX)

        kaldefsdb = sqlite3.connect(kaldefsfile)
        cur = kaldefsdb.cursor()

        cur.execute("delete from configurations where KALTURA_CONFIG_ID = ?",
                    (kaltura_id,))

        kaldefsdb.commit()
        cur.close()
        kaldefsdb.close()
        lockfile.close()

        return simplejson.dumps({'success': success, 'messages': msgs})
    except Exception as e:
        return simplejson.dumps(
            {'success': False, 'messages': [repr(e), str(e)]})


def update_kaltura(kaltura_id, values):
    try:
        lockfile = open('kts-config.lock', 'w')
        fcntl.lockf(lockfile, fcntl.LOCK_EX)

        kaldefsdb = sqlite3.connect(kaldefsfile)
        cur = kaldefsdb.cursor()

        upd_query = """update configurations set
                            KALTURA_NAME = ?,
                            KALTURA_PATH = ?,
                            PARTNER_ID = ?,
                            PLAYER_ID = ?,
                            THUMBNAIL_PLAYER_ID = ?,
                            ADMIN_SECRET = ?,
                            SECRET = ?,
                            USER_NAME = ?,
                            MOBILE_PLAYER_FLAVOR = ?
                            WHERE KALTURA_CONFIG_ID = ?"""

        cur.execute(upd_query, (list(values) + [kaltura_id]))

        kaldefsdb.commit()
        cur.close()
        kaldefsdb.close()
        lockfile.close()

        return simplejson.dumps({'success': True, 'messages': None})
    except Exception as e:
        return simplejson.dumps(
            {'success': False, 'messages': [repr(e), str(e)]})


def load_server_settings(SETTINGS={}):
    SETTINGS['PORT'] = os.environ.get('PORT', DEFAULT_PORT)
    SETTINGS['UPLOAD_FOLDER'] = os.environ.get(
        'UPLOAD_FOLDER', DEFAULT_UPLOAD_FOLDER)
    SETTINGS['KTS_ADMIN_USER'] = os.environ.get('KTS_ADMIN_USER',
                                                DEFAULT_KTS_ADMIN_USER)
    SETTINGS['KTS_ADMIN_PWD'] = os.environ.get('KTS_ADMIN_PWD',
                                               DEFAULT_KTS_ADMIN_PWD)
    SETTINGS['DEBUG_MODE'] = os.environ.get('DEBUG_MODE',
                                            DEFAULT_DEBUG_MODE)
    SETTINGS['KALTURA_DEFINITIONS_DB'] = os.environ.get(
        'KALTURA_DEFINITIONS_DB',
        DEFAULT_KALTURA_DEFINITIONS_DB)
    return SETTINGS


if __name__ == "__main__":
    print 'KTS server settings: '
    settings = load_server_settings()
    pprint(settings)
    print ''
    print 'Kaltura definitions: '
    kaldefs = load_kaltura_settings()
    pprint(kaldefs)
