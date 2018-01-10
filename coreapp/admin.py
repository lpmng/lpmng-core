from django.contrib import admin
from . import models


"""
class LDAPUserAdmin(admin.ModelAdmin):
    exclude = ['dn', 'objectClass']
    list_display = ['uid', 'surname', 'commonname', 'password', 'mail', 'tel']


admin.site.register(models.LdapUser, LDAPUserAdmin)"""
