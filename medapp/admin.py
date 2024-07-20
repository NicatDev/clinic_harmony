from django.contrib import admin
from medapp.models import *

admin.site.register(Tag)
admin.site.register(Category)

# Register your models here.
class BlogModelInline(admin.StackedInline):  
    model = BlogSection
    extra = 0

class BlogModelAdmin(admin.ModelAdmin):
    inlines = [BlogModelInline]

admin.site.register(Blog,BlogModelAdmin)

class ServiceModelInline(admin.StackedInline):  
    model = ServiceSection
    extra = 0

class ServiceModelAdmin(admin.ModelAdmin):
    inlines = [ServiceModelInline]

admin.site.register(Service,ServiceModelAdmin)

class MessageModelInline(admin.StackedInline):  
    model = DoctorMessage
    extra = 0

class AwardModelInline(admin.StackedInline):
    model = Award
    extra = 0

class DoctorModelAdmin(admin.ModelAdmin):
    inlines = [MessageModelInline,AwardModelInline]

admin.site.register(Doctor,DoctorModelAdmin)

admin.site.register(HomeSlider)

admin.site.register(Comment)

