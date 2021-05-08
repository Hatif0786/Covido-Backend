from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from rest_framework import status

@api_view(["GET"])
def News_List(request):
    obj = News.objects.all()
    serializer = NewsSerializer(obj, many=True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)
