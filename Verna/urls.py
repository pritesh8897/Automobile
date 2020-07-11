from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Verna'

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',views.Form,name='verna'),
    path('',views.PurchaseInformation,name='sector'),
    path('customer/<int:customer_id>/',views.ownerdetails,name='owner_detail'),
    path('ownerinformation/create',views.OwnerInformationcreateview,name='owner_view'),
    path('carinformation/create',views.CarInformationcreateview,name='car_view'),
    path('owner/Edit/<int:customer_id>',views.OwnerEditview,name='owner_Edit'),
    path('owner/Delete/<int:customer_id>',views.OwnerDeleteview,name='owner_Delete'),



    # path('',views.carlistclassbasedview.as_view()),
    # path('cardetail/<int:pk>/',views.cardetailview.as_view(),name='car_detail'),

]