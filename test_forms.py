from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.test_item_name_is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0])