from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
