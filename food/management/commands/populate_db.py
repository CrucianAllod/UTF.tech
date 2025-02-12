from django.core.management.base import BaseCommand
from food.models import FoodCategory, Food

class Command(BaseCommand):
    help = 'Populates database with test data'

    def handle(self, *args, **options):
        Food.objects.all().delete()
        FoodCategory.objects.all().delete()

        main_courses = FoodCategory.objects.create(
            name_ru="Основные блюда",
            name_en="Main courses",
            order_id=1
        )

        drinks = FoodCategory.objects.create(
            name_ru="Напитки",
            name_en="Drinks",
            order_id=2
        )

        Food.objects.create(
            category=main_courses,
            name_ru="Стейк из лосося",
            description_ru="Свежий норвежский лосось с овощами",
            cost=1200.00,
            code=1001,
            internal_code=2001,
            is_vegan=False
        )

        Food.objects.create(
            category=drinks,
            name_ru="Смузи из манго",
            description_ru="Свежий манго с йогуртом",
            cost=450.00,
            code=1002,
            internal_code=2002,
            is_vegan=True
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
