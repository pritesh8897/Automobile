from django.shortcuts import render,redirect
from django.http import HttpResponse
from Verna.models import OwnerInformation,CarInformation
from Verna.forms import OwnerInformationForm,CarInformationForm,ContactForm,SignupForm
import datetime
from django.contrib.auth.models import User

#*** for class based crud operation *****
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,FormView,RedirectView)

#***** for validation of login ***********
from django.contrib.auth.decorators import login_required #for functions based views
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin #for class based views

# ******* for logout *********
from django.contrib.auth import logout


# Create your views here.
def Form(request):
    return render(request,'base.html',{'title':'java'},)

@login_required(login_url='/')
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
# @method_decorator(login_required,name='car_list')
class carlistclassbasedview(LoginRequiredMixin,ListView):
    model = CarInformation
    paginate_by = 20
    template_name = 'Verna_temp_class/carlist.html'
    context_object_name = 'car'
    login_url = '/'

    # def get_queryset(self):
    #     query = CarInformation.objects.filter(price='1200000')
    #     return query



    # def get_context_data(self,**kwargs):
    #     context={}
    #     context = super().get_context_data(**kwargs)
    #     context['car'] = CarInformation.objects.all()
    #     context['current_time'] = datetime.datetime.now().time()
    #     context['current_date'] = datetime.datetime.now().date()
    #     return context

#******** classbased detail view ***********
class cardetailview(DetailView,LoginRequiredMixin):
    model = CarInformation
    template_name = 'Verna_temp_class/cardetail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    login_url = '/'

#******** classbased create view **************
class carinfocreateview(CreateView):
    model = CarInformation
    #fields = ['name','details','price','design','Date']
    form_class = CarInformationForm
    template_name = 'Verna_temp_class/car_create.html'
    success_url = '/'

#********** class based update view *********
class careditview(UpdateView):
    model = CarInformation
    form_class = CarInformationForm
    template_name = 'Verna_temp_class/car_edit.html'
    #pk_url_kwarg = 'car_id'
    success_url = '/Verna'

#********* class Delete view ****************
class cardeleteview(DeleteView):
    model = CarInformation
    template_name = 'Verna_temp_class/car_delete.html'
    pk_url_kwarg = 'car_id'
    success_url = '/Verna'

# ********* Template view ************
class welcome(TemplateView):
    template_name = 'base.html'

# ***** Formview *********
class contactview(FormView):
    template_name = "Verna_temp/contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        #print(form.cleaned_data)

        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')

        # print(username)

        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email )


        user_obj.save()
        return super().form_valid(form)

# *** for signupview *********
class signupview(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/Verna' ##if you want to redirect home or listing page of Verna after fillup signup form.. use this url
    # success_url = '/' #if you want to redirect login page after fillup signup form.. use this url



# *** function based logout view ****
def LogoutfunView(request):
    logout = (request)
    return redirect ('/')

#*** class based logout view ***
class LogoutfunView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutfunView,self).get_redirect_url(self, *args, **kwargs)