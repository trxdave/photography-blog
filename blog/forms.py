from django import forms
from .models import Photo, Category
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
        return confirm_password

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class PhotoForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('wildlife', 'Wildlife'),
        ('street', 'Street'),
        ('macro', 'Macro'),
    ]

    category = forms.ChoiceField(choices=Category.CATEGORY_CHOICES)

    class Meta:
        model = Photo
        fields = ('title', 'description', 'image', 'category')

class LandscapeImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

class PortraitImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

class WildlifeImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

class StreetImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

class MacroImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }