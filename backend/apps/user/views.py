from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from util.method_util import request_method_check, no_request_arg
from user.models import UserProfile
import json
from util.model_util import query_set_to_list, model_to_dict
from address.models import Province, City, School, Major
from error_dictionary import ErrorInformation
from datetime import datetime


# Create your views here.
@request_method_check('GET')
@no_request_arg
def get_user_profile(request):
    user = request.user
    profile = UserProfile.objects.filter(id=user.id)
    if not profile:
        return JsonResponse({'status': False, 'error': ErrorInformation.user_not_found})
    profile = model_to_dict(profile[0])
    profile['major'] = profile['major'].name
    profile['school'] = profile['school'].name
    return JsonResponse({'data': profile, 'status': True})


@request_method_check('POST')
@no_request_arg
def modify_profile(request):
    data = json.loads(request.body)
    user = request.user
    profile = UserProfile.objects.filter(id=user.id)
    if not profile:
        return JsonResponse({'status': False, 'error': ErrorInformation.user_not_found})
    profile.nickname = data.get('nickname')
    profile.avatar = data.get('avatar')
    profile.introduction = data.get('introduction')
    profile.birthday = datetime.fromtimestamp(data.get('birthday'))
    majors = Major.objects.filter(name=data.get('major'))
    if not majors:
        return JsonResponse({'status': False, 'error': ErrorInformation.major_not_found})
    profile.major = majors[0]
    schools = School.objects.filter(name=data.get('school'))
    if not schools:
        return JsonResponse({'status': False, 'error': ErrorInformation.school_not_found})
    profile.school = schools[0]
    profile.save()
    return JsonResponse({'status': True})
