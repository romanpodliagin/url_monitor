# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from url_monitor.models import Url


class UrlAdmin(admin.ModelAdmin):
    model = Url
    readonly_fields = ('created', 'updated')


admin.site.register(Url, UrlAdmin)
