from django.contrib import admin
from Verna.models import Cars
from Verna.models import final_selected_car
from Verna.models import selected_car_colour
from Verna.models import Owner

#**********************************************
from Verna.models import CarInformation
from Verna.models import OwnerInformation


# Register your models here.
admin.site.register(Cars)
admin.site.register(final_selected_car)
admin.site.register(selected_car_colour)
admin.site.register(Owner)

#********************************************

admin.site.register(CarInformation)
admin.site.register(OwnerInformation)