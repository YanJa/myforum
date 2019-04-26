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
    # 实例化一个分页对象
    res = Paginator(objs, ONE_PAGE_CNT)
    # 可以分的页数
    num_pages = res.num_pages

    try:
        page = res.page(page_no)
    except PageNotAnInteger:  # 如果页码不是整数
        page = res.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，或没有相应的记录
        page = res.page(num_pages)  # 取最后一页的记录

    # 指定页的数据
    page_objs = page.object_list
    # 是否有上一页的规则跟标准的规则不一样所以不适用标准的方法
    # has_previous = page.has_previous()
    # 是否有下一页
    has_next = page.has_next()
    # 标页列表
    page_links = [i for i in range(page_no-5, page_no+6) if 0 < i <= num_pages]
    # 前一页
    previous_link = page_links[0] - 1
    # 自定义是否有前一页
    has_previous = previous_link > 0
    response = {
        "num_pages": num_pages,  # 分页页数
        "page_no": page_no,  # 当前页码
        "articles": page_objs,  # 指定页码的数据列表
        "page_links": page_links,  # 标页列表
        "has_previous": has_previous,  # 是否有前一页
        "previous_link": previous_link,  # 前一页
        "has_next": has_next,  # 是否后一页
        "next_link": int(page_links[-1]) + 1,  # 后一页
        }
    return response
