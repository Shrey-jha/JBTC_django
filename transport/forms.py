from django import forms
from .models import LoadInfo, Feedback

class LoadInfoForm(forms.ModelForm):
    class Meta:
        model = LoadInfo
        fields = ['name', 'weight', 'size', 'pickup_location', 'drop_location', 'date', 'mobile_number', 'time_of_pickup']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



class GetQuoteForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    details = forms.CharField(widget=forms.Textarea)