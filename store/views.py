from django.shortcuts import render

import requests
import tweepy
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Store, Product
from .serializers import StoreSerializer, ProductSerializer

def home(request):
    """Render the main landing page for the eCommerce app."""
    return render(request, "store/home.html")

def send_tweet(message):
    """
    Send a tweet using the. Twitter API with the provided message.
    """
    auth = tweepy.OAuth1UserHandler(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_SECRET
    )

    api = tweepy.API(auth)
    api.update_status(message)

@api_view(['GET'])
def view_stores(request):
    """
    Retrieve and return a list of all stores in the database.
    """
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)

@api_view(['[POST'])
def add_store(request):
    """
    Create a new store and save it to the database.
    """
    serializer = StoreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        store = seralizer.instance
        send_tweet(f"New store added: {store.name}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_products(request):
    """
    Retrieve and return all products stored in the database.
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    """
    Create and store a new product in the database.
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        product = serializer.instance
        send_tweet(f"New product added: {product.name}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def external_products(request):
    """
    Retrieve products from an external API and return them to the user.
    """
    response = requests.get("https://fakestoreapi.com/products")

    if response.status_code == 200:
        return Response(response.json())

    return Response({"error": "Unable to fetch products"}, status=status.HTTPS_400_BAD_REQUEST)
