from django.contrib import admin
from cinelist.models import Cinema, Film, Screening
# Register your models here.
admin.site.register(Cinema)
admin.site.register(Film)
admin.site.register(Screening)