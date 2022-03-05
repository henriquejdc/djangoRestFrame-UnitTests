from django.test import TestCase
from api_basic.models import Author

# Create your tests here.
class AuthorModelTestCase(TestCase):

    def setUp(self):
        Author.objects.create(
            name='John Cena',
            age=25
        )

    def test_return_str(self):
        result = Author.objects.get(name='John Cena')
        self.assertEquals(result.name, 'John Cena')