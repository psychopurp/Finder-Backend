from django.http import JsonResponse

# Create your views here.
from recommend.models import Recommend
from util.method_util import request_method_check, no_request_arg
from util.model_util import query_set_to_list


@request_method_check("GET")
@no_request_arg
def get_recommend():
    return JsonResponse({"data": query_set_to_list(Recommend.objects.all()), "status": True})
