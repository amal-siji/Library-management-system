from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth.forms import SetPasswordForm
from django.forms import FileInput

# LIBRARIAN

class li_registerForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    age = forms.IntegerField(max_value=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(li_registerForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['name', 'email', 'username',
                  'age', 'password1', 'password2', 'image']

    def save(self, commit=True):
        user = super(li_registerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            lr_profile.objects.create(
                image=self.cleaned_data["image"], name=self.cleaned_data["name"], age=self.cleaned_data["age"], user=user)
            return user


class li_LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class lr_addbookForm(forms.ModelForm):
    class Meta:
        model = lr_addbook
        fields = ['bookname','author','bookDescription','image']
        widgets = {
            'image': FileInput(),
        }

        def __init__(self, *args, **kwargs):
            super(lr_addbookForm, self).__init__(*args, **kwargs)
            self.fields['image'].widget.attrs = {'id':'selectedFile'} 


class lr_StPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = None


class MessageForm(forms.ModelForm):
    reciever = forms.CharField(max_length=255)
    message_content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = li_message
        fields = ['reciever', 'message_content']

# READER

class cu_registerForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    age = forms.IntegerField(max_value=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(cu_registerForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['name', 'email', 'username',
                  'age', 'password1', 'password2', 'image']

    def save(self, commit=True):
        user = super(cu_registerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            cu_profile.objects.create(email=self.cleaned_data["email"],
                                      image=self.cleaned_data["image"], name=self.cleaned_data["name"], age=self.cleaned_data["age"], user=user)
            return user


class cu_LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class cu_StPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = None


class Cu_Rentbookform(forms.ModelForm):
    class Meta:
        model = book_rent
        fields = "__all__"

# ADMIN


class ad_LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].help_text = None


class ad_StPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = None
