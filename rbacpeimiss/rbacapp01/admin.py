from django.contrib import admin

# Register your models here.
from rbacapp01 import models
class PermissonAdmin(admin.ModelAdmin):
    list_display = ['pk','title','url']
    ordering = ['pk',]
admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Permisson,PermissonAdmin)