from django.db import models

class Supplier(models.Model):
    sup_id = models.TextField(primary_key=True)
    sup_name = models.CharField(max_length=50)
    sup_email = models.CharField(max_length=50)
    sup_contact=models.CharField(max_length=11)

