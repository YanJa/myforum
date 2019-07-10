from django.conf.urls import url
from .views import BLockList, BLockInfo

urlpatterns = [
    url('^block_list$', BLockList.as_view(), name="block_list"),
    url('^block_info/(?P<block_id>\d+)$', BLockInfo.as_view(), name="block_info")

]