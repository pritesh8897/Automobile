from django.shortcuts import render,redirect
from django.http import HttpResponse
from Verna.models import OwnerInformation,CarInformation
from Verna.forms import OwnerInformationForm,CarInformationForm
import datetime
from django.views.generic import ListView,DetailView #*** for class based crud operation *****

# Create your views here.
def Form(request):
    return render(request,'base.html',{'title':'java'},)

def PurchaseInformation(request):
    purchase_list = OwnerInformation.objects.all()
    #purchase_list = OwnerInformation.objects.filter(car_info__design = 'pooja kumari')
    return render(request,'Verna_temp/purchase.html',{'purchase':purchase_list},)

# ************ create function for get details of owner ******************
def ownerdetails(request,customer_id):
    #owner_object = OwnerInformation.objects.filter(id=customer_id).first()
    owner_object = OwnerInformation.objects.get(id=customer_id)
    return render(request,'Verna_temp/owner_details.html',{'owner':owner_object})

#**********create function for forms*****************************

def OwnerInformationcreateview(request):
    context = {}
    form = OwnerInformationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form
    return render(request,'Verna_temp/create_owner_information.html',context)


def CarInformationcreateview(request):

    form = CarInformationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'Verna_temp/create_owner_information.html', {'form':form})

#********** create function for edit or update records *******************

def OwnerEditview(request,customer_id):
    owner_object = OwnerInformation.objects.get(id=customer_id)
    form = OwnerInformationForm(request.POST or None ,instance=owner_object)

    if form.is_valid():
        form.save()
        return redirect("/")


    return render(request, 'Verna_temp/Owner_Edit.html',{'form':form})


#*************** create function for delete records of owner
def OwnerDeleteview(request,customer_id):
    owner_object = OwnerInformation.objects.get(id=customer_id)

    if request.method == 'POST':
        owner_object.delete()
        return redirect('/')

    return render(request, 'Verna_temp/owner_Delete.html',{})

#************ class based crud operation *************

#*** List view **********

class carlistclassbasedview(ListView):
    model = CarInformation
    paginate_by = 5
    template_name = 'Verna_temp_class/carlist.html'
    context_object_name = 'car'

    # def get_queryset(self):
    #     query = CarInformation.objects.filter(name='suzuki swift')
    #     return query



    # def get_context_data(self,**kwargs):
    #     context={}
    #     context = super().get_context_data(**kwargs)
    #     # context['car'] = CarInformation.objects.all()
    #     # context['current_time'] = datetime.datetime.now().time()
    #     # context['current_date'] = datetime.datetime.now().date()
    #     return context

#******** classbased detail view ***********
class cardetailview(DetailView):
    model = CarInformation
    template_name = 'Verna_temp_class/cardetail.html'
    context_object_name = 'car'