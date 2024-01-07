from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,FormView,DetailView,UpdateView,TemplateView
from Restocafe.models import User,Category,Subcategory,Items,Offers
from Restocafe.forms import RegistrationForm,LoginForm,CategoryCreateForm,SubCategoryCreateForm,ItemsAddForm,ItemOfferForm
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 


# Create your views here.

class SignUpView(CreateView):
 
    template_name="signup.html"
    form_class=RegistrationForm
   
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.success(self.request,"failed to create")
        return super().form_invalid(form)
    
class SignInView(FormView):
    template_name="signin.html"
    form_class=LoginForm
    # success_url=reverse_lazy('index')

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            else:
                messages.error(request,"invalid")
                return render(request,self.template_name,{"form":form})
            
class CategoryCreateView(CreateView,ListView):
    template_name="category_add.html"
    form_class=CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("category-add")

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
    
def remove_category(request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.filter(id=id).update(is_active=False)
        messages.success(request,"category removed")
        return redirect("category-add")
    
    
class SubCategoryCreateView(CreateView,ListView):
    template_name="subcategory_add.html"
    form_class=SubCategoryCreateForm
    model=Subcategory
    context_object_name="subcategories"
    success_url=reverse_lazy("subcategory-add")

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)

def remove_subcategory(request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.filter(id=id).update(is_active=False)
        messages.success(request,"subcategory removed")
        return redirect("subcategory-add")    
    
class ItemAddCategoryCreateView(CreateView):
    template_name="items_add.html"
    form_class=ItemsAddForm
    model=Items
    success_url=reverse_lazy("items-list")

    def form_valid(self, form):
        messages.success(self.request,"Item added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Item adding failed")
        return super().form_invalid(form)  

def remove_item(request,*args,**kwargs):
        id=kwargs.get("pk")
        Items.objects.filter(id=id).delete()
        messages.success(request,"item removed")
        return redirect("items-add")         

class CategoryListView(ListView):
    template_name="category_list.html"
    model=Category
    context_object_name="categories"

class CategoryDetailView(DetailView):
    template_name="category_detail.html"
    model=Category
    context_object_name="categories"    

class SubcategoryListView(ListView):
    template_name="subcategory_list.html"
    model=Category
    context_object_name="categories"

class SubcategoryDetailView(DetailView):
    template_name="subcategory_detail.html"
    model=Category
    context_object_name="categories"  

class ItemListView(ListView):
    template_name="items_list.html"
    model=Items
    context_object_name="items"    

class ItemUpdateView(UpdateView):
    template_name="items_edit.html"
    model=Items
    form_class=ItemsAddForm
    success_url=reverse_lazy("items-list")
    def form_valid(self,form):
        messages.success(self.request,"item updated successfully")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"item updated unsuccessfully")
        return super().form_invalid(form)

def remove_itemview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Items.objects.filter(id=id).delete()
    return redirect("items-list")

class ItemDetailView(DetailView):
    template_name="items_detail.html"
    model=Items
    context_object_name="categories"

class OfferCreateView(CreateView):

    template_name="offer_add.html"
    form_class=ItemOfferForm
    model=Offers
    success_url=reverse_lazy("item-list")
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Items.objects.get(id=id)
        form.instance.items=obj
        
        messages.success(self.request,"offer added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"offer added failed")
        return super().form_invalid(form)        
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        items_object=Items.objects.get(id=id)
        items_id=items_object.items.id

        return reverse("items-detail",kwargs={"pk":items_id})
    
def offer_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    offer_object=Offers.objects.get(id=id)
    cloth_id=offer_object.items.id
    offer_object.delete()

    return redirect("items-detail",pk=cloth_id)

class IndexView(TemplateView):
    template_name="index.html  "