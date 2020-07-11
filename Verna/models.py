from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cars(models.Model):
    WHITE = 'WH'
    BLACK = 'BL'
    YELLOW = 'YW'
    BROWN = 'BR'
    COLOUR_OPTION = [(WHITE, 'white'),
                     (BLACK, 'black'),
                     (YELLOW, 'yellow'),
                     (BROWN,'brown')]

    PETROL = 'PE'
    DIESEL = 'DI'
    VARIENTS = [(PETROL,'petrol'),
                (DIESEL,'diesel')]

    car_name = models.CharField(max_length=30)
    Discription = models.TextField(blank=True,null=True)
    price = models.IntegerField(help_text='filled with integer',verbose_name='car price')
    colour_options = models.CharField(max_length=2, choices=COLOUR_OPTION, default='white')
    Lunching_Date = models.DateTimeField(auto_now_add=True)
    Updated_version = models.DateTimeField(auto_now=True)
    varients = models.TextField(choices=VARIENTS)

    def __str__(self):
        return self.car_name

    #def get_full_name(self):
        #return self.FIRST_NAME + self.LAST_NAME

#class User is already available in Django.
#from django.contrib.auth.models import User

class final_selected_car(models.Model):
    name = models.CharField(max_length=30,verbose_name='car name')

    def __str__(self):
        return self.name

class selected_car_colour(models.Model):
    colour = models.TextField(verbose_name='car colour')

    def __str__(self):
        return self.colour

class Owner(models.Model):
    owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.ManyToManyField(final_selected_car,null=True,blank=True)
    car_colour = models.ForeignKey(selected_car_colour,on_delete=models.CASCADE)

    def __str__(self):
        return self.owner_name.username


#*************************************************************************************************
#(How to show records in the HTML form -- from database)

class CarInformation(models.Model):
    name = models.CharField(max_length=25,verbose_name='car name')
    details = models.TextField(null=True,blank=True,verbose_name='car details')
    price = models.IntegerField()
    design = models.TextField(verbose_name='Designed By')
    Date = models.DateField(auto_now_add=False,verbose_name='Launching date')

    def __str__(self):
        return self.name

class OwnerInformation(models.Model):
    owner = models.ForeignKey(User,verbose_name='owner name',on_delete=models.CASCADE)
    car_info = models.ForeignKey(CarInformation,on_delete=models.CASCADE)
    Booking_Date = models.DateTimeField(auto_now_add=True)
    Delivery_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.first_name