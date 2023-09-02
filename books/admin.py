from django.contrib import admin
from .models import Books, Lease

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    pass

class LeaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Books, BooksAdmin)
admin.site.register(Lease, LeaseAdmin)
