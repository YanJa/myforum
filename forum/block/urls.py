from django.conf.urls import url
from .views import BLockInfo

urlpatterns = [
    url('^block_list/$', BLockInfo.as_view(), name="block_list")
]