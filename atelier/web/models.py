from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.CharField(max_length=10)
    project_size = models.CharField(max_length=50)
    project_location = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    requirements = models.TextField()

    def __str__(self):
        return self.name
    
class IndexFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name