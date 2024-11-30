from django.contrib import admin

# Register your models here.
from .models import Hive, Topic, Message, User, HiveMember

admin.site.register(User)
admin.site.register(Hive)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(HiveMember)

