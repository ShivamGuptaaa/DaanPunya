from django.contrib import admin
from .models import medicine,rq_medicine,org_update,dnr_update,applied_medicine

admin.site.register(medicine)
admin.site.register(rq_medicine)
admin.site.register(org_update)
admin.site.register(dnr_update)
admin.site.register(applied_medicine)
