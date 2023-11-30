from django.contrib import admin

# Register your models here.
from .models import User, Attainment, Memorandum, SpecialOrder, CommLetter, Moau, MoauParties, MoauSignatories, Event, EventAgencies, Agency

admin.site.register(User)
admin.site.register(Attainment)
admin.site.register(Memorandum)
admin.site.register(SpecialOrder)
admin.site.register(CommLetter)
admin.site.register(Moau)
admin.site.register(MoauParties)
admin.site.register(MoauSignatories)
admin.site.register(Event)
admin.site.register(Agency)
admin.site.register(EventAgencies)