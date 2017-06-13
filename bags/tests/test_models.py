from django.test import TestCase
from bags.models import Category


class CategoryTest(TestCase):

    def test_category_handbag(self):
        Category.objects.create(name='handbag', thumbnail='http://s3.aws.com/image.png')

        self.assertEqual(1, Category.objects.count())
        self.assertEqual('handbag', Category.objects.get(name='handbag').name)
