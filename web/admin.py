from django.contrib import admin

# Register your models here.
from .models import HatData, LastSeenId, TeamMember

admin.site.register(HatData)
admin.site.register(LastSeenId)
admin.site.register(TeamMember)
