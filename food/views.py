from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FoodListSerializer
from .models import FoodCategory

class FoodListView(APIView):
    def get(self, request):
        food_categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        serializer = FoodListSerializer(food_categories, many=True)
        return Response(serializer.data)
