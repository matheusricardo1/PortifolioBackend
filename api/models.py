from django.db import models

class PortifolioOwner(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    your_stack = models.CharField(max_length=120)
    image = models.ImageField(upload_to='owner/')
    linkedin = models.URLField()
    github = models.URLField()
    whatsapp = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    
    about_me = models.TextField()
    contact_me = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Service(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='services/')
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0, editable=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    
class Project(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='projects/')
    description = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    
    demo = models.URLField()
    github = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    