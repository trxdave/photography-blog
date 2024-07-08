from django import forms
from .models import Post, LandscapeImage, Category
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
            raise forms.ValidationError("Passwords do not match")
        return confirm_password

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LandscapeImageForm(forms.ModelForm):
    class Meta:
        model = LandscapeImage
        fields = ('image',)

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category')