from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(Edition)
admin.site.register(Person)
admin.site.register(Institution)
admin.site.register(Period)
admin.site.register(SyncLog)

# Register your models here.
