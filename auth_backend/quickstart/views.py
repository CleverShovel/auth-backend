from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def authenticate(request):
    return Response(None, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    return Response(None, status=status.HTTP_200_OK)