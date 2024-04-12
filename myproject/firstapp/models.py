from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100, default='no address')
    date_registration = timezone.now()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, Phone: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(default=0,max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    date_registration = timezone.now()

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, description: {self.description}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def calculate_total_amount(self):
        total = sum(product.price *
                    product.quantity for product in self.products.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f'order: {self.id},' \
               f' product: {self.products}, ' \
               f'date: {self.date_ordered}, ' \
               f'total_price: {self.total_price}'
