from rest_framework import serializers
from .models import Food, FoodCategory

class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        foods = Food.objects.filter(category=instance, is_publish=True)
        food_serializer = FoodSerializer(foods, many=True)
        data['foods'] = food_serializer.data
        return data