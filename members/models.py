from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    personal_skills= models.CharField(max_length=500)
    team_skills= models.CharField(max_length=500)
    weakness= models.CharField(max_length=500)
    illness= models.CharField(max_length=500)
    under_presure= models.CharField(max_length=500)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
