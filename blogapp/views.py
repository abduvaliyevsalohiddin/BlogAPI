from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from .serializers import *
from .models import *


class MaqolalarAPIView(APIView):
    # authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        maqolalar = Maqola.objects.all()
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        maqola = request.data
        serializer = MaqolaSerializer(data=maqola)
        if serializer.is_valid():
            serializer.save(muallif=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class MaqolaAPIView(APIView):
    def get(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        korishlar_soni = maqola.korish_soni
        maqola.korish_soni = korishlar_soni + 1
        maqola.save()
        serializer = MaqolaSerializer(maqola)
        return Response(serializer.data)

    def update(self, request, pk):
        yangi = request.data
        maqola = Maqola.objects.get(id=pk)
        serializer = MaqolaSerializer(maqola, data=yangi)
        if maqola.muallif != request.user:
            return Response({"xabar": "Maqola o'zingizga tegishli emas"}, status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
