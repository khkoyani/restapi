from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404

# class StatusApiList(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


class StatusApiList(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        obj = None
        id_query = self.request.GET.get('id', None)
        print(self.request.data)
        if id_query is not None:
            obj = get_object_or_404(self.get_queryset(), id=id_query)
            self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        id_query = self.request.GET.get('id', None)
        # print('body   --', self.request.body)
        # print('data  --', self.request.data)
        if id_query is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print('body   --', self.request.body)
        print('data  --', self.request.data)
        return self.update(request, *args, **kwargs)


class StatusApiCreate(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class StatusApiDetail(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Status.objects.all()


class StatusApiUpdate(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    lookup_field = 'id'
    queryset = Status.objects.all()

class StatusApiDelete(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    lookup_field = 'id'
    queryset = Status.objects.all()