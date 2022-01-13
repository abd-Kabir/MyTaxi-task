from django.db import models


class Driver(models.Model):
    username = models.CharField(max_length=50)


class Client(models.Model):
    username = models.CharField(max_length=50)


class Order(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    datetime = models.DateTimeField(null=True, auto_now=True)
