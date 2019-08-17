from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
import json

# class StatusApiList(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

def json_data(data):
    try:
        return json.loads(data)
    except ValueError:
        return False

# class StatusApi(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     id_query= None
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q', None)
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def get_object(self):
#         print(f'id_query------{self.id_query}')
#         obj = None
#         if self.id_query is not None:
#             obj = get_object_or_404(self.get_queryset(), id=self.id_query)
#             self.check_object_permissions(self.request, obj)
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         id_from_url = request.GET.get('id', None)
#         id_from_json_data = None
#
#         json_request_data = json_data(request.body)
#         if json_request_data:
#             id_from_json_data = json_request_data.get('id', None)
#
#         id_query = id_from_url or id_from_json_data or None
#
#         self.id_query = id_query
#         if id_query is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         id_from_url = request.GET.get('id', None)
#         id_from_json_data = None
#
#         json_request_data = json_data(request.body)
#         if json_request_data:
#             id_from_json_data = json_request_data.get('id', None)
#
#         id_query = id_from_url or id_from_json_data or None
#
#         self.id_query = id_query
#         return self.destroy(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         id_from_url = request.GET.get('id', None)
#         id_from_json_data = None
#         json_request_data = json_data(request.body)
#         if json_request_data:
#             id_from_json_data = json_request_data.get('id', None)
#         id_from_request_data = request.data.get('id', None)
#         id_query = id_from_url or id_from_json_data or id_from_request_data or None
#         print('in put')
#         self.id_query = id_query
#         return self.update(request, *args, **kwargs)

class StatusApiList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        print(self.request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StatusApiDetail(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        print(123)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class StatusApiCreate(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     queryset = Status.objects.all()
#
# class StatusApiDetail(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#     def get_queryset(self):
#         return Status.objects.all()
#
#
# class StatusApiUpdate(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#     queryset = Status.objects.all()
#
# class StatusApiDelete(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#     queryset = Status.objects.all()