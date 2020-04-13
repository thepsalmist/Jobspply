from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class JobPageNumberPagination(PageNumberPagination):
    page_size = 6

