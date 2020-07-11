from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Discription(request):
    return HttpResponse('The Hyundai Verna has 1 Diesel Engine and 2 Petrol Engine on offer. The Diesel engine is 1493 cc while the Petrol engine is 1497 cc and 998 cc. It is available with the Manual and Automatic transmission. Depending upon the variant and fuel type the Verna has a mileage of 17.7 to 25.0 kmpl. The Verna is a 5 seater Sedan and has a length of 4440mm, width of 1729mm and a wheelbase of 2600mm.')
def car_price(request):
    return HttpResponse('Huyndai verna price is appprox 14,00,000.')