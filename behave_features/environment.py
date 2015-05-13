import logging

import simplejson

import server


server.app.config['TESTING'] = True
app_test_client = server.app.test_client()

# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)

def after_step(context, step):
    if context.config.userdata.getbool("behave_debug_on_error") and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        import pdb
        pdb.post_mortem(step.exc_traceback)


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()
    # -- ALTERNATIVE: Setup logging with a configuration file.
    # context.config.setup_logging(configfile="behave_logging.ini")

    logging.warning("Debug on error: %s"
                    % context.config.userdata.getbool("behave_debug_on_error"))
    logging.warning("Debug on error: %s"
                    % context.config.userdata.getbool("BEHAVE_DEBUG_ON_ERROR"))

    context.app = app_test_client
    
    context.kaltura_id = int(context.config.userdata['use_kaltura_id'])
    logging.warning('Using kaltura id %s (to change, edit behave.ini or '
                    'add the flag "-D use_kaltura_id=SOME_NUMBER"'
                    % context.kaltura_id)
    logging.info(context.config.userdata['behave_debug_on_error'])


def before_tag(context, tag):
    if tag == 'uploads':
        context.uploads = []


def after_tag(context, tag):
    if tag == 'uploads':
        logging.info('Scenario caused uploads: %s' % context.uploads)
        for entry_id in context.uploads:
            try:
                logging.info('Deleting uploaded entry %s' % entry_id)
                r = context.app.get('/service/del_media/?entry_id=%s&kaltura_id=%s'
                                    % (entry_id, context.kaltura_id))
                if simplejson.loads(r.data)['success']:
                    context.uploads.remove(entry_id)
            except Exception as e:
                logging.exception(e)
                continue
        if context.uploads:
            logging.warning('Un-deleted uploads: %s' % context.uploads)
