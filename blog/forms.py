from django import forms
from .models import Post, Photo, Category, LandscapeImage
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

class LandscapeImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', help_text='Select an image file less than 1MB in size.')

    class Meta:
        model = LandscapeImage
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image.size > 1024 * 1024:
            raise forms.ValidationError('Image size should not exceed 1MB. Please select a smaller image.')
        if not image.content_type.startswith('image/'):
            raise forms.ValidationError('Only image files are allowed. Please select a valid image file.')
        return image

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category", help_text='Select a category for your post.')

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category')