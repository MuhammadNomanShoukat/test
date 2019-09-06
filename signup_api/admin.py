from django.contrib import admin
from .models import SignUpModel
from django.contrib.auth.admin import UserAdmin


# ====================================== UserAdmin model class displaying the list ======================
class UserAdminClass(UserAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'semester',
        'cgpa',
        'uni',
        'phone',
        'address',
    ]

# here register the model to the admin site
admin.site.register(SignUpModel,UserAdminClass)

