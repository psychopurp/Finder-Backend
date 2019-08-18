from django.db.models import Q
from django.http import JsonResponse

from .models import Avtivity
from util.method_util import request_method_check
from util.model_util import get_result_by_query_page, str_page_to_int


@request_method_check("GET")
def get_activities(request):
    query = Q(title__contains=request.GET.get("query"))
    return JsonResponse(get_result_by_query_page(Avtivity, query, str_page_to_int(request.GET.get("page"))))
