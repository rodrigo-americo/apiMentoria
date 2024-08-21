from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pc
from .serializers import PcSerializer


class PcCreateListView(generics.ListCreateAPIView):
    queryset = Pc.objects.all().order_by('id')
    serializer_class = PcSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class PcRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pc.objects.all()
    serializer_class = PcSerializer


class PcSsdCountView(APIView):
    def get(self, request):
        pcs_with_ssd = Pc.objects.filter(ssd=True).count()
        pcs_without_ssd = Pc.objects.filter(ssd=False).count()

        return Response({
            "pcs_with_ssd": pcs_with_ssd,
            "pcs_without_ssd": pcs_without_ssd
        })
