from django.contrib import admin
from django import forms
# Register your models here.
from AdminSystem.models import Admin,User
from .utils.encrypt import md5

class MyUserForm(forms.ModelForm):
    def clean_password(self):
    # do something that validates your data
        return md5(self.cleaned_data["password"])



class Adminmodel(admin.ModelAdmin):
    form = MyUserForm



class Usermodel(admin.ModelAdmin):
    list_display = ('name','is_vip',)
    list_filter = ('is_vip',)
    search_fields = ('name',)
    list_per_page = 10
    form = MyUserForm




admin.site.register(Admin, Adminmodel)
admin.site.register(User,Usermodel)