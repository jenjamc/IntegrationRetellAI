from wtforms import fields
from wtforms import form
from wtforms import validators


class LoginAdminForm(form.Form):
    username = fields.StringField(validators=[validators.DataRequired('Login is required!')])
    password = fields.PasswordField(validators=[validators.DataRequired('Password is required!')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.username.data:
            self.username.data = self.username.data.strip()
