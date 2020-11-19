from django.test import TestCase
from restapi import models


# Create your tests here.
class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=200, merchant="amazon", description="headphones", category="music"
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(200, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)
