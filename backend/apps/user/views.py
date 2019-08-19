import json
import os
import time
from datetime import datetime

from django.http import JsonResponse

from address.models import School, Major
from error import ErrorInformation
from project.settings import MEDIA_ROOT, BASE_DIR, MEDIA_URL
from user.models import UserProfile, Login
from util.log_util import log
from util.login_util import login_require
from util.method_util import request_method_check
from util.model_util import model_to_dict, error_return, generate_random_str


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


@login_require
def upload_image(request):
    img = request.FILES.get('image')
    name_list = img.name.split('.')
    if len(name_list) <= 1:
        return JsonResponse(error_return(ErrorInformation.unsupported_type))
    if name_list[-1].lower() not in ['jpg', 'png', 'jpeg']:
        return JsonResponse(error_return(ErrorInformation.unsupported_type))
    img_name = str(int(time.time() * 1000)) + generate_random_str(3) + '.' + name_list[-1]
    file = open(os.path.join(BASE_DIR, MEDIA_ROOT, img_name), 'wb')
    try:
        for chunk in img.chunks(chunk_size=1024):
            file.write(chunk)
    except IOError as error:
        log(error)
        return JsonResponse(error_return(ErrorInformation.image_fail))
    finally:
        file.close()
    return JsonResponse({'url': MEDIA_URL + img_name, 'status': True})


@request_method_check("POST")
def login(request):
    data = json.load(request.body)
    phone = data.get("phone")
    password = data.get("password")
    try:
        user = UserProfile.objects.get(phone=phone)
    except UserProfile.DoesNotExist:
        return JsonResponse(error_return(ErrorInformation.login_fail))
    if not user.check_password(password):
        return JsonResponse(error_return(ErrorInformation.login_fail))
    Login.objects.filter(user=user).delete()
    token = generate_random_str()
    Login.objects.create(user=user, token=token)
    return JsonResponse({"status": True, "token": token})
