from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Activity)
admin.site.register(models.ActivityField)
admin.site.register(models.Field)
admin.site.register(models.Media)
admin.site.register(models.MediaType)
admin.site.register(models.Report)
admin.site.register(models.ReportActivityField)


