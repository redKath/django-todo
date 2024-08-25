from django.test import TestCase
from django.urls import reverse

class TodoListViewTest(TestCase):
    def test_todo_list_view_has_form(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
