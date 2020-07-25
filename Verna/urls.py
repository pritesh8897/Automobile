from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Verna'

urlpatterns = [
    path('admin/', admin.site.urls),
   ##############path('',views.Form,name='verna'),
    # path('',views.PurchaseInformation,name='sector'),
    # path('/customer/<int:customer_id>/',views.ownerdetails,name='owner_detail'),
    # path('/ownerinformation/create',views.OwnerInformationcreateview,name='owner_view'),
    # path('/carinformation/create',views.CarInformationcreateview,name='car_view'),
    # path('/owner/Edit/<int:customer_id>',views.OwnerEditview,name='owner_Edit'),
    # path('/owner/Delete/<int:customer_id>',views.OwnerDeleteview,name='owner_Delete'),
    #  path('/contact',views.contactview.as_view(),name='contact_page'),




    path('',views.carlistclassbasedview.as_view(),name='car_list'),
    path('/cardetail/<int:car_id>/',views.cardetailview.as_view(),name='car_detail'),
    path('/car/create',views.carinfocreateview.as_view(),name='create' ),
    path('/caredit/<int:pk>/',views.careditview.as_view(),name='car_edit'),
    path('/cardelete/<int:car_id>/', views.cardeleteview.as_view(), name='car_delete'),
    path('/contact',views.contactview.as_view(),name='contact_page'),
    #####path('',views.welcome.as_view(),name = 'welcome')

]