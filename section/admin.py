from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Member)
admin.site.register(Xtreme)
admin.site.register(Society)
admin.site.register(Event)
admin.site.register(Team)