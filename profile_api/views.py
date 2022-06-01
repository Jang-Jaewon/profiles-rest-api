from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request):
        """Return a list of APIView features"""
        an_apiview = [
            "Use HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Give you the most control over you application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

