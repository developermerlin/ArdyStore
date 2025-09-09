from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control shadow-none',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control shadow-none',
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '(+232)-79-123-000',
        'class': 'form-control shadow-none',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'ardymerlin@gmail.com',
        'class': 'form-control shadow-none',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Merlin',
        'class': 'form-control shadow-none',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Rahman',
        'class': 'form-control shadow-none',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
    #     self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'
