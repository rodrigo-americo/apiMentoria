from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pc
from .serializers import PcSerializer


class PcCreateListView(generics.ListCreateAPIView):
    queryset = Pc.objects.all()
    serializer_class = PcSerializer


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