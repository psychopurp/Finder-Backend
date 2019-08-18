from django.http import JsonResponse

from address.models import Province, City, School, Major
from error import ErrorInformation
from util.method_util import request_method_check, no_request_arg
from util.model_util import query_set_to_list, from_id_get_object


@request_method_check('GET')
@no_request_arg
def get_provinces():
    return JsonResponse({'data': query_set_to_list(Province.objects.all()), 'status': True})


@request_method_check('GET')
def get_cities(request):
    province_id = request.GET.get('province_id')
    return JsonResponse({'data': query_set_to_list(
        City.objects.filter(province=Province.objects.filter(id=province_id).first()), ['id', 'name']), 'status': True})


@request_method_check('GET')
def get_schools(request):
    school_id = request.GET.get('school_id')
    if school_id:
        return JsonResponse({'data': query_set_to_list(
            School.objects.filter(id=school_id).first()), 'status': True})
    else:
        city_id = request.GET.get('city_id')
        if not city_id:
            return JsonResponse({'status': False, 'error': ErrorInformation.param_lost})
        city = from_id_get_object(city_id, City)
        return JsonResponse(
            {'data': query_set_to_list(School.objects.filter(city=city)),
             'status': True})


@request_method_check('GET')
@no_request_arg
def get_majors():
    return JsonResponse({'data': query_set_to_list(Major.objects.all()), 'status': True})
