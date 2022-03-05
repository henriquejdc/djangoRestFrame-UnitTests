from django.test import TestCase
from api_basic.forms import AuthorForm

# Create your tests here.
class AuthorFormTestCase(TestCase):

    def test_author_form_valid(self):
        form = AuthorForm(data={
            'name': 'John Cena',
            'age': 25
        })
        self.assertTrue(form.is_valid())

    def test_author_form_invalid(self):
        form = AuthorForm(data={
            'name': 11,
            'age': 'zxa'
        })
        self.assertFalse(form.is_valid())

