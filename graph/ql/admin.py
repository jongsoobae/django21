from django.contrib import admin
from ql.models import School, Classs, Student


class SchoolAdmin(admin.ModelAdmin):
    pass


class ClasssAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)
admin.site.register(Classs, ClasssAdmin)
admin.site.register(Student, StudentAdmin)
