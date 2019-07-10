from django.shortcuts import render
from django.views.generic import View
from block.models import Block


class BLockInfo(View):
    template_name = "block/block_info.html"

    def get(self, request, block_id):
        print(block_id)
        block_obj = Block.objects.filter(status=0).order_by('-id')
        response = {"block_info": block_obj, "user": request.user}
        return render(request, self.template_name, response)

    def post(self, requset):
        pass


class BLockList(View):
    template_name = "block/block_list.html"

    def get(self, request):
        block_obj = Block.objects.filter(status=0).order_by('-id')
        response = {"block_info": block_obj, "user": request.user}
        return render(request, self.template_name, response)

    def post(self, requset):
        pass
