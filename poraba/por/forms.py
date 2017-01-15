from django import forms
from .models import Profile, Car, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=100)
	password = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserForm(UserCreationForm):
	firstName=forms.CharField(required=True,max_length=100)
	lastName=forms.CharField(required=True, max_length=100)
	email=email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=['firstName','lastName','email', 'username','password1', 'password2']
		
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["firstName"]		
		user.last_name = self.cleaned_data["lastName"]
		if commit:
			user.save()
		return user
		
class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		exclude = ['user']

class CarAddForm(forms.ModelForm):
	class Meta:
		model=Car
		fields=['brand', 'car_model', 'year', 'kilometers', 'rotation_speed','fuel_consumption','image']
		
class CommentAddForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=['comment']
