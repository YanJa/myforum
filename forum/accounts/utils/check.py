# coding: utf-8


__all__ = [
    'check_email'
]


def check_email(email):
    """
    检测是否为邮箱
    :param email:
    :return:
    """
    if "@" in email:
        return True
    return False
