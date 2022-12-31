from django.contrib import admin

from users.models.option import Option
from users.models.user import Profile

admin.site.register(Profile)
admin.site.register(Option)

