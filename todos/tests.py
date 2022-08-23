from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title='title',
            body='body'
        )
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, "title")
        self.assertEqual(self.todo.body, "body")
        self.assertEqual(str(self.todo), "title")

class TodoViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title='title',
            body='body'
        )

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), len(response.json()))
        self.assertContains(response, self.todo)
    
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "title")
