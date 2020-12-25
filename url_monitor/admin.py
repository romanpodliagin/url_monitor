# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from url_monitor.models import Url
from django.contrib.admin.models import LogEntry


class UrlAdmin(admin.ModelAdmin):
    model = Url
    readonly_fields = ('created', 'updated')


class LogEntryAdmin(admin.ModelAdmin):
    model = LogEntry
    list_filter = ('user',)


admin.site.register(Url, UrlAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
