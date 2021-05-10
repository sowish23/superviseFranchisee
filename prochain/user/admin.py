from django.contrib import admin

from .models import UploadVideo
from .models import UploadImgMenu

admin.site.register(UploadVideo)
admin.site.register(UploadImgMenu)