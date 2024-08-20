from django import forms
from .models import Photo, Comment
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    """
    A form for creating new users. Includes fields for first name, last name, email, Username,
    password, and confirm password. Validates that the two password fields match.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def clean_confirm_password(self):
        """
        Validates that the password and confirm_password fields match.
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
        return confirm_password

    def save(self, commit=True):
        """
        Saves the user with the hashed password.
        """
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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
    """
    A form for creating and editing photos. Includes fields for title, content, description,
    category image, and the photo image itself.
    """
    class Meta:
        model = Photo
        fields = ('title', 'content', 'description', 'categoryimage', 'image')
        labels = {
            'title': 'Photo Title',
            'content': 'Photo Content',
            'description': 'Photo Description',
            'image': 'Upload Image',
            'categoryimage': 'Photo Category Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'categoryimage': forms.Select(attrs={'class': 'form-control'}),
        }

class ImageForm(forms.ModelForm):
    """
    A form for uploading images. Includes only the image field with a file input widget that
    accepts only image files.
    """
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

    def __init__(self, *args, **kwargs):
        """
        Custom initialization to ensure the image field is required.
        """
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

class ContactForm(forms.Form):
    """
    A simple contact form with fields for the user's name, email, and message.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    """
    A form for submitting comments on photos. Includes only the text field.
    """
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a comment...', 'rows': 3}),
        }