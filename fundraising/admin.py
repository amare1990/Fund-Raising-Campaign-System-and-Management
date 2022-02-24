from django.contrib import admin

# Register your models here.
from fundraising.models import Promise, Pay, Worker


#admin.site.register(Worker)

#from django.contrib import admin
#admin.site.register(User, UserAdmin)


@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):
    list_display = ('user','full_name_promise','amount_in_ETB', 'on_behalf_of','created_on')
    #list_filter = ('on_behalf_of',)
    #search_fields = ['on_behalf_of']
    #sprepopulated_fields = {'slug': ('name',)}
  
#admin.site.register(Post, PostAdmin)

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name_pay', 'amount_in_ETB', 'on_behalf_of','created_on', 'upload_receit')
    #list_filter = ('on_behalf_of',)
    #search_fields = ['on_behalf_of']
    #sprepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Worker._meta.get_fields()]
    list_display = ('user','full_name' ,'place_of_birth', 'job','city', 'country')
    #list_filter = ("status", 'on_behalf_of',)
    search_fields = ['user', 'full_name']
    #sprepopulated_fields = {'slug': ('name',)}   
    
