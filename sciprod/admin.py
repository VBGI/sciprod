from django.contrib import admin

from .models import ScientificWork, WorkType, Journal, Author, ComputationRule


class PermissionMixin:

    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        return ScientificWork.objects.filter(user=request.user)

    def _common_permission_manager(self, request, obj):
        if request.user.is_superuser:
            return True
        if obj:
            if obj.user == request.user:
                return True
            else:
                return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.public:
                return False
        return self._common_permission_manager(request, obj)

    def has_change_permission(self, request, obj=None):
         return self._common_permission_manager(request, obj)

    def save_model(self, request, obj, form, change):
        if obj:
            if not obj.user:
                obj.user = request.user
        obj.save()


class ScientificWorkAdmin(PermissionMixin, admin.ModelAdmin):
    pass




admin.site.register(ScientificWork, ScientificWorkAdmin)