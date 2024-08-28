from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','status', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Prenom'}),
            'last_name': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Nom'}),
            'username': forms.TextInput(attrs={'class': 'common__login__input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'common__login__input', 'placeholder': 'Votre Email'}),
            'status': forms.Select(attrs={'class': 'common__login__input','placeholder': 'Your Status'}),
            'password1': forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': 'Mot de passe'}),
            'password2': forms.PasswordInput(attrs={'class': 'common__login__input', 'placeholder': 'Retapez votre mot de passe'}),
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
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Aucun utilisateur avec cet email.")
        return email

class CustomSetPasswordForm(SetPasswordForm):
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password1
 





class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
        help_text='Optional'
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
        help_text='Optional'
    )
    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'johndoe'}),
        help_text='Required'
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1-202-555-0174'}),
        help_text='Optional'
    )
    occupation = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Stack Developer'}),
        help_text='Optional'
    )
    display_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
        help_text='Optional'
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about yourself', 'rows': 10}),
        help_text='Optional'
    )

    # Champs pour les réseaux sociaux
    facebook = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        help_text='Facebook profile URL'
    )
    twitter = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        help_text='Twitter profile URL'
    )
    linkedin = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        help_text='LinkedIn profile URL'
    )
    instagram = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        help_text='Instagram profile URL'
    )
    
    
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}),
        help_text='Required. Provide a valid email address.'
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}),
        help_text='Leave blank if you do not want to change your password.'
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'password', 
            'phone_number', 'occupation', 'display_name', 'bio',
            'facebook', 'twitter', 'linkedin', 'instagram'
        ]
        
        
        

    def save(self, commit=True):
        user = self.instance.user  # Assuming Profile has a `user` OneToOneField
        
        # Mise à jour des champs User
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        # Mettre à jour le mot de passe seulement si un nouveau mot de passe a été fourni
        password = self.cleaned_data['password']
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
            self.instance.save()  # Sauvegarde le Profile

            # Mise à jour des profils de réseaux sociaux
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'facebook': self.cleaned_data['facebook'],
                    'twitter': self.cleaned_data['twitter'],
                    'linkedin': self.cleaned_data['linkedin'],
                    'instagram': self.cleaned_data['instagram']
                }
            )
        
        return user

   