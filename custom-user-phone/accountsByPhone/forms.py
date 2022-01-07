from django import forms
from .models import UserByPhoneNumber
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegisterUser(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirim Password', widget=forms.PasswordInput())

    class Meta:
        model = UserByPhoneNumber
        fields = ('first_name', 'last_name','phone_number', 'address', 'age')
    
    def clean_phone_number(self):
        ph_num = self.cleaned_data['phone_number']
        qs = UserByPhoneNumber.objects.filter(phone_number=ph_num)
        if qs.exists():
            raise forms.ValidationError('Bu Telefon Raqam allaqochon olingan')
        return ph_num

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password2 is not None and password != password2:
            raise forms.ValidationError('password2 da hatolik bolishi mumkun tekshirib qayta urinib koring!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirim Password', widget=forms.PasswordInput())

    class Meta:
        model = UserByPhoneNumber
        fields = ('first_name', 'last_name','phone_number', 'address', 'age')
    
    def clean_phone_number(self):
        ph_num = self.cleaned_data['phone_number']
        qs = UserByPhoneNumber.objects.filter(phone_number=ph_num)
        if qs.exists():
            raise forms.ValidationError('Bu Telefon Raqam allaqochon olingan')
        return ph_num

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password2 is not None and password != password2:
            raise forms.ValidationError('password2 da hatolik bolishi mumkun tekshirib qayta urinib koring!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = UserByPhoneNumber
        fields = ('phone_number', 'password', 'is_active', 'superuser')
    def clean_password(self):
        return self.initial['password']