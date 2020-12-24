# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    user = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    interval = models.IntegerField(default=30)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    @property
    def get_status(self):
        if self.status not in [None, 0]:
            return f'{self.status}'
        return ''

    @property
    def get_status_color(self):
        if not self.get_status:
            return '#fc0909'
        else:
            return '#3efc05'

    def sync(self):
        if not self.active:
            print('not active')
            return

        try:
            r = requests.get(self.url, timeout=5)
            print(f'req: {self.url}')
            self.status = r.status_code
            self.save()
        except requests.exceptions.ConnectTimeout:
            print('ConnectTimeout')

    def __str__(self):
        verbose_name = self.url[:30]
        return f'[{self.get_status}] <{self.user.username}> <{verbose_name}>'
