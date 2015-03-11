from app import create_app, db
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell

from flask.ext.login import current_user, logout_user
from flask.ext.admin import Admin, expose, BaseView, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView

from flask import redirect, url_for
from app.main.models import User

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#Create custom models view
class UserModelView(ModelView):
    can_edit = False
    can_delete = False
    def is_accessible(self):
                return current_user.is_authenticated()

    def on_model_change(self, form, User, is_created=False):
        User.password = form.password_hash.data

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('main.login'))
        return super(MyAdminIndexView, self).index()


admin = Admin(index_view=MyAdminIndexView(), base_template='my_master.html')
#admin.add_view(UserView())
admin.add_view(UserModelView(User, db.session))
admin.init_app(app)

if __name__ == '__main__':
        manager.run()
