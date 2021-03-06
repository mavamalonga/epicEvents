from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffAccessPermission(BasePermission):
    message = 'Permission only to the staff member.'

    def has_permission(self, request, view):
        return request.user.is_staff == True


class UserAccessPermission(BasePermission):
     message = 'Permission only to the gestion contact'

     def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-gestion').exists() == True


class ClientAccessPermission(BasePermission):
    message = 'Permission only to the sales contact'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists() == True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return obj.sales_contact_id.id == request.user.id or \
            request.user.groups.filter(name='team-gestion').exists() == True


class EventAccessPermission(BasePermission):
    message = 'Permission only to project managers'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists() == True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return obj.support_contact_id.id == request.user.id or \
            request.user.groups.filter(name='team-gestion').exists() == True


class ContractAccessPermission(BasePermission):
    message = 'Permission only to the sales contact'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.groups.filter(name='team-vente').exists() == True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return obj.sales_contact_id.id == request.user.id or \
            request.user.groups.filter(name='team-gestion').exists() == True




