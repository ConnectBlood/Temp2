# from django.contrib import admin
# from .models import blood_details
# # Register your models here.
# # admin.site.register(blood_details)

# class blooddetailsAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.hospital:
#             obj.hospital = request.hospital
#         obj.save()

# admin.site.register(blood_details, blooddetailsAdmin)


from django.contrib import admin
from .models import blood_details,hospital_details,FriendList,FriendRequest

class BloodDetailsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.hospital:
            obj.hospital = request.user.profile.hospital
        obj.save()

admin.site.register(blood_details, BloodDetailsAdmin)

class HospitalDetailsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.hospital:
            obj.hospital = request.user.profile.hospital
        obj.save()

admin.site.register(hospital_details, HospitalDetailsAdmin)

# class bloodrequestAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.hospital:
#             obj.hospital = request.user.profile.hospital
#         obj.save()

# admin.site.register(bloodrequest, bloodrequestAdmin)

class FriendListAdmin(admin.ModelAdmin):
    list_filter=['user']
    list_display=['user']
    search_fields=['user']
    readonly_fields=['user']

    class Meta:
        model=FriendList

admin.site.register(FriendList, FriendListAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_filter=['sender','receiver']
    list_display=['sender','receiver']
    search_fields=['sender__username','sender__email','receiver__email','receiver__username']

    class Meta:
        model=FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)

