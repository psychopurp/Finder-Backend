import json
from datetime import datetime

from django.http import JsonResponse

from address.models import School, Major
from error import ErrorInformation
from user.models import UserProfile
from util.login_util import login_require
from util.method_util import request_method_check
from util.model_util import model_to_dict, error_return


@request_method_check('GET')
@login_require
def get_user_profile(request):
    user = request.user
    if not isinstance(user, UserProfile):
        return JsonResponse(error_return(ErrorInformation.no_such_topic))
    return JsonResponse(
        {'data': model_to_dict(user, ['nickname', 'phone', 'avatar', 'introduction', 'birthday', ('major', 'name'),
                                      ('school', 'name')]), 'status': True})


@request_method_check('POST')
def modify_profile(request):
    data = json.loads(request.body)
    user = request.user
    user = request.user
    if not isinstance(user, UserProfile):
        return JsonResponse(error_return(ErrorInformation.no_such_topic))
    user.nickname = data.get('nickname')
    user.avatar = data.get('avatar')
    user.introduction = data.get('introduction')
    user.birthday = datetime.fromtimestamp(data.get('birthday'))
    majors = Major.objects.filter(name=data.get('major'))
    if not majors:
        return JsonResponse({'status': False, 'error': ErrorInformation.major_not_found})
    user.major = majors[0]
    schools = School.objects.filter(name=data.get('school'))
    if not schools:
        return JsonResponse({'status': False, 'error': ErrorInformation.school_not_found})
    user.school = schools[0]
    user.save()
    return JsonResponse({'status': True})
