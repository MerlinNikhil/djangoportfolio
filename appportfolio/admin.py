#admin.py

from django.contrib import admin
from .models import Profile, AboutMe, Projects, Education, Experience, Contact, Skill

# Register your models here.

admin.site.register(Profile)
admin.site.register(AboutMe)
admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Skill)