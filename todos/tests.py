from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ToDo

# Create your tests here.


class ToDoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = ToDo.objects.create(
            title="Take over the world", body="do it swiftly"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Take over the world")
        self.assertEqual(self.todo.body, "do it swiftly")
        self.assertEqual(str(self.todo), "Take over the world")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertContains(response, self.todo)
