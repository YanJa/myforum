#!/usr/bin/env python
# encoding: utf-8
# 分页公共模块

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
    )

# 每页显示条数默认10条
ONE_PAGE_CNT = 10

def pagination(objs, page_no=1):

    res = Paginator(objs, ONE_PAGE_CNT)
    # 可以分的页数
    num_pages = res.num_pages
    # 指定页的数据
    page = res.page(page_no)
    page_objs = page.object_list

    response = {
        "page_objs": page_objs, # 指定页码的数据列表
        "num_pages": num_pages  # 分页页数
    }
    return response
