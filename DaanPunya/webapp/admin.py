from django.contrib import admin
from .models import medicine,rq_medicine,org_update,dnr_update,applied_medicine,dnr_address,extUser,reg_org
from .forms import extUserCreationForm
from django.contrib.auth.admin import UserAdmin

class extUserAdmin(UserAdmin):
    model = extUser
    add_form = extUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Type',
            {
                'fields':(
                    'is_org',
                    'reg_num',
                    'cert_num',
                    'phNum',
                    'address',
                )
            }
        )

    )
    
admin.site.register(medicine)
admin.site.register(rq_medicine)
admin.site.register(org_update)
admin.site.register(dnr_update)
admin.site.register(dnr_address)
admin.site.register(applied_medicine)
admin.site.register(reg_org)
admin.site.register(extUser,extUserAdmin)
