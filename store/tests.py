from django.test import TestCase
from .models import Store, Product
from django.contrib.auth.models import User


class StoreModelTest(TestCase):
    """Tests for the Store model."""

    def setUp(self):
        """Create a test user and store."""
        self.user = User.objects.create(username="testuser")
        self.store = Store.objects.create(
            vendor=self.user,
            name="Test Store",
            description="Test description"
        )

    def test_store_creation(self):
        """Test that a store can be created correctly."""
        self.assertEqual(self.store.name, "Test Store")


class ProductModelTest(TestCase):
    """Tests for the Product model."""

    def setUp(self):
        """Create a test user and product."""
        self.user = User.objects.create(username="testuser")
        self.product = Product.objects.create(
            name="Test Product",
            price=10.00,
            owner=self.user
        )

    def test_product_creation(self):
        """Test that a product can be created correctly."""
        self.assertEqual(self.product.name, "Test Product")
