import six
class User():
    i_id = None

    def __init__(self,uid):
        self.i_id = uid
        if uid is None:
            return None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return isinstance(self.i_id,six.text_type)

    def __repr__(self):
        return '<User with id %r>' % (self.i_id)
