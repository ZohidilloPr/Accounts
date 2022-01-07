from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm

UserByPhoneNumber = get_user_model()

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = UserByPhoneNumber


    list_display = ('phone_number', 'get_full_name', 'age', 'joined_date')
    list_filter = ('phone_number', 'age', 'first_name', 'staff', 'superuser')

    fieldsets = (
        (None, {
            "fields": (
                'first_name', 'last_name', 'phone_number', 'address', 'age','password',
            ),
        }),
        ('Permisssions',{
            "fields":(
                'is_active','staff', 'superuser',
            )
        })
    )
    readonly_fields = ('joined_date',)
    add_fieldsets = (
        (None, {
            "classes":('wide',),
            "fields":('phone_number', 'password', 'password2', 'is_active', 'staff', 'superuser'),
        }),
    ) #bu yerga "," qo'yma
 
    search_fields = ('phone_number', 'age', 'first_name', 'last_name', 'address', 'staff', 'superuser',)
    ordering = ('-joined_date',)

admin.site.unregister(Group)
admin.site.register(UserByPhoneNumber, CustomUserAdmin)
