# doctorj_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Store, Category, Machine, Order, OrderItem, ShoppingOrder, ShoppingItem, ShoppingOrderItem, Transaction, Notification
from .serializers import UserSerializer, StoreSerializer, CategorySerializer, MachineSerializer, OrderSerializer, OrderItemSerializer, ShoppingOrderSerializer, ShoppingItemSerializer, ShoppingOrderItemSerializer, TransactionSerializer, NotificationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ShoppingOrderViewSet(viewsets.ModelViewSet):
    queryset = ShoppingOrder.objects.all()
    serializer_class = ShoppingOrderSerializer

class ShoppingItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

class ShoppingOrderItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingOrderItem.objects.all()
    serializer_class = ShoppingOrderItemSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def index(request):
    return render(request,'base.html',locals())

def intro(request):
    return render(request, 'intro.html',locals())
