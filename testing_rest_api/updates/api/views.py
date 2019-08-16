from updates.models import Update
from updates.forms import UpdateForm
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from testapi.mixins import CSRFExemptMixin, HttpResponseMixin
import json
from .utils import json_data


class UpdateJsonDetailView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get_object(self, id):
        try:
            return Update.serializeobj.get(id=id)
        except Update.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        if obj is None:
            error_message = json.dumps({'message': 'Item does not exist'})
            return self.render_to_response(error_message, status=404)
        else:
            data = obj.serialize()
            return self.render_to_response(data, status=200)

    def put(self, request, id, *args, **kwargs):
        new_data = json_data(request.body)  #returns converted json data or False if other datatype submitted
        if not new_data:
            error_message = json.dumps({'message': 'Only send json data'})
            return self.render_to_response(error_message, status=400)

        obj = self.get_object(id)
        if obj is None:
            error_message = json.dumps({'message': 'Item does not exist'})
            return self.render_to_response(error_message, status=404)

        if obj is not None and new_data:

            old_data = json.loads(obj.serialize())
            for k,v in new_data.items():
                old_data[k] = v
            form = UpdateForm(old_data, instance=obj)

            if form.is_valid():
                form.save(commit=True)
                data = json.dumps(old_data)
                return self.render_to_response(data, status=201)
            if form.errors:
                error_data = json.dumps(form.errors)
                return self.render_to_response(error_data, status=400)
            data = json.dumps({'message': 'exists'})
            return self.render_to_response(data, status=400)


    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        if obj is None:
            error_message = json.dumps({'message': 'Item does not exist'})
            return self.render_to_response(error_message, status=404)
        if obj:
            items_deleted, dictionary = obj.delete()
            if items_deleted > 0:
                message = json.dumps({'message': 'Successfully deleted'})
                return self.render_to_response(message, status=200)


class UpdateJsonListView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        json_list = Update.serializeobj.all().serialize()
        return self.render_to_response(json_list)

    def post(self, request, *args, **kwargs):
        new_data = json_data(request.body)
        if not new_data:
            error_message = json.dumps({'message': 'Only send json data'})
            return self.render_to_response(error_message, status=400)

        if new_data:
            form = UpdateForm(new_data)
            if form.is_valid():
                data = form.save(commit=True).serialize()
                return self.render_to_response(data, status=201)
            if form.errors:
                error_data = json.dumps(form.errors)
                return self.render_to_response(error_data, status=400)

        error_message = json.dumps({'message': 'No post data'})
        return self.render_to_response(error_message, status=400)

    def delete(self, request, *args, **kwargs):
        error_message = json.dumps({'message': 'Stop trying to delete the entire list'})
        return self.render_to_response(error_message, status=403)