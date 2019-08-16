from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from .models import Update
from django.views.generic import View
from testapi.mixins import JsonResponseMixin
from django.core import serializers


def detail_view(request):
    obj = Update.objects.filter(id=1).filter()
    context = {'count': 1000,
               'content': 'randomwords'}
    return JsonResponse(context)


class UpdateJsonDetailView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'count': 1250,
                   'content': 'randomwords'}
        print(type(context))
        return self.render_to_json_response(context)

class UpdateJsonListView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = Update.serializeobj.all().serialize()
        print(type(context))
        print(context)
        return HttpResponse(content=context, content_type='application/json')

