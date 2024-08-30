from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': 'Mot de passe'}),
        label="Mot de passe")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': ' Confirmer Mot de passe'}),
        label="Mot de passe")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','status', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Prenom'}),
            'last_name': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Nom'}),
            'username': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Email'}),
            'status': forms.Select(attrs={'class': 'common','placeholder': 'Your Status'}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'common__login__input',
            'placeholder': 'Your username',
            
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'common__login__input',
            'placeholder': 'Password',
            
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=username).exists() or User.objects.filter(username=username).exists():
            return username
        raise forms.ValidationError("Username or email not found.")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'common__login__input', 'placeholder': 'Email'}),
        label="Adresse email"
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Aucun utilisateur avec cet email.")
        return email

class CustomSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': ' Nouveau mot de passe'}),
        label="Nouveau mot de passe"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': 'Confirmer le nouveau mot de passe'}),
        label="Confirmer le nouveau mot de passe"
    )
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password1
 





from django import forms
from django.contrib.auth.models import User

class CustomUserUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Que voulez-vous dire sur vous-même'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    twitter = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    occupation = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    display_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    linkedin = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone_number',
            'occupation', 'display_name', 'bio', 'facebook', 'twitter', 
            'linkedin', 'image'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }
