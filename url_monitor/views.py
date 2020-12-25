# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response

from url_monitor.models import Url


class Base(View):

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')

        context = {}
        context.update(csrf(request))
        url_list = Url.objects.filter(user=user)
        context['url_list'] = url_list
        return render(request, 'base.html', context=context)


class SyncUrl(generics.CreateAPIView):

    def post(self, request, url_obj_id):
        url_object = Url.objects.get(id=url_obj_id)
        url_object.sync()
        return Response({'status': url_object.status}, status=status.HTTP_200_OK)


class SyncActive(generics.CreateAPIView):

    def post(self, request, url_obj_id):
        if request.POST['active'] == 'true':
            active = True
        else:
            active = False
        print(f'set active [{url_obj_id}] to {active}')
        url_object = Url.objects.get(id=url_obj_id)
        url_object.active = active
        url_object.save()
        return Response({'status': url_object.active}, status=status.HTTP_200_OK)
