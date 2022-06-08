from django.contrib import admin
from profile_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.AccountToFeedBookmark)

