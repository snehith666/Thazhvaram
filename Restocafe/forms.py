from django import forms
from django.contrib.auth.forms import UserCreationForm
from Restocafe.models import User,Category,Subcategory,Offers,Items

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]

class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)   

class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Category
        fields=["category_name"]  

class SubCategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Subcategory
        fields=["Subcategory_name","category"]          

class ItemsAddForm(forms.ModelForm):
   
    class Meta:
        model=Items 
        fields="__all__"     

class ItemsVarientForm(forms.ModelForm):

    class Meta:
        model=Items
        exclude=("__all__",) 
        #fields=["price","sixe","color"] no updation needed


class ItemOfferForm(forms.ModelForm):   

    class Meta:
        model=Offers
        fields=["items","price","start_date","due_date"]
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"}),
        }
            
        
        

