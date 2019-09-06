from django.contrib import admin
from .models import Expense


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'password']
#
#
# admin.site.register(User, UserAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'amount', 'types']


admin.site.register(Expense, ExpenseAdmin)


