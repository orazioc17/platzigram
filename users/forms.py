"""User forms"""


# Django
from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import EmailInput

# Models
from django.contrib.auth.models import User
from users.models import Profile


# class ProfileForm(forms.Form):
#     """Profile form"""

#     website = forms.URLField(max_length=200, required=True)
#     biography = forms.CharField(max_length=500, required=False)
#     phone = forms.CharField(max_length=20, required=False)
#     picture = forms.ImageField()


class SignupForm(forms.Form):
    """Sign up form"""

    username = forms.CharField(
        label=False,
        min_length=4, 
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username', 
                'class':'form-control', 
                'required':True
            }
        )
    )
    password = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control',
                'required':True
            }
        )
    )
    password_confirmation = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repeat Password',
                'class':'form-control',
                'required':True
            }
        )
    )

    first_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control',
                'required':True
            }
        )
    )
    last_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control',
                'required':True
            }
        )
    )

    email = forms.CharField(
        label=False,
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control',
                'required':True
            }
        )
    )

    def clean_username(self):
        """Username must be unique"""

        username = self.cleaned_data['username']

        #De esta forma y para no estar buscando todos los datos, el exist es para saber si ese query existe, y si existe pues se puede validar
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            # Con esto, django se encarga de generar el error y llevarlo hasta el HTML, sin tener que hacerlo nosotros
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match"""

        # Ya que estamos sobreescribiendo el metodo clean de django
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords does not match')

        return data

    def save(self):
        """Create User and Profile"""

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()