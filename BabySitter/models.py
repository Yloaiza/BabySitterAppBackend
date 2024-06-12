from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=150)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
       return self.name
    
class Nanny(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=150)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
       return self.name
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='name')
    nanny = models.ForeignKey(Nanny, on_delete=models.CASCADE, to_field='name')
    dateStart = models.DateField()
    dateEnd = models.DateField()
    # Puedes agregar más campos según sea necesario para tu aplicación

    def __str__(self):
        return f"{self.user} - {self.nanny} - {self.dateStart} - {self.dateEnd}"
