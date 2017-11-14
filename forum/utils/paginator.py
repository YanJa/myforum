#!/usr/bin/env python
# encoding: utf-8

from django.core.paginator import
(
    Paginator,
    EmptyPage,
   PageNotAnInteger
)

def pagination(objs, num):
    if num:
        res = Paginator(objs, num)
    else:
        res = Paginator(objs, 1)
