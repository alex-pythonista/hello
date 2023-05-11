from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class HelloAPI(APIView):

    def get(self, request):

        return Response({
            'message': 'Hello World!',
        }, status=status.HTTP_200_OK)
