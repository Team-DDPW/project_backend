from django.urls import path
from .views import PackageRequestList, PackageRequestDetail

urlpatterns = [
    path("", PackageRequestList.as_view(), name="PackageRequest_list"),
    path("<int:pk>/", PackageRequestDetail.as_view(), name="PackageRequest_detail"),
]
