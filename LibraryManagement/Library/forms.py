from django import forms
from django.core import validators
from Library import models
from django.contrib.auth.models import User

class UserFormmain(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class userFormnot(forms.ModelForm):
    class Meta():
        model = models.UserInfo
        fields = ('facebook_id','profile_pic')

class user_Form(forms.Form):
    user_name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    user_email = forms.EmailField()
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = "__all__"
class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }
class TrackForm(forms.ModelForm):
    class Meta:
        model = models.Track
        fields = "__all__"
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'})
        }