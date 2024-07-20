from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['full_name','subject','email','message','phone']
    
        
    def __init__(self,*args,**kvargs):
        super(Messageform,self).__init__(*args,**kvargs)

class DoctorMessageform(forms.ModelForm):

    class Meta:
        model = DoctorMessage
        fields = ['full_name','subject','email','message','phone_number','doctor']
    
        
    def __init__(self,*args,**kvargs):
        super(DoctorMessageform,self).__init__(*args,**kvargs)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
            
    def __init__(self,*args,**kvargs):
        super(CommentForm,self).__init__(*args,**kvargs)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'search-field',
        'placeholder': 'Axtar'
    }))

# class Subscriberform(forms.ModelForm):

#     class Meta:
#         model = Subscriber
#         fields = ['email']
    
        
#     def __init__(self,*args,**kvargs):
#         super(Subscriberform,self).__init__(*args,**kvargs)