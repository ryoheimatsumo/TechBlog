from django.contrib import admin
from login_app.models import User,UserProfileInfo,Relationship

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfileInfo)
admin.site.register(Relationship)
