import json
from datetime import datetime

from django.db.models import Q
from django.http import JsonResponse

from error import ErrorInformation
from user.models import UserProfile
from util.login_util import login_require
from util.method_util import request_method_check
from util.model_util import get_result_by_query_page, str_page_to_int, from_id_get_object, error_return
from .models import Activity, ActivityCategory


@request_method_check('GET')
def get_activities(request):
    query = request.GET.get('query')
    if query:
        query = Q(title__contains=query) | Q(end_time__gt=datetime.now())
    else:
        query = Q(end_time__gt=datetime.now())
    return JsonResponse(get_result_by_query_page(Activity, query, str_page_to_int(request.GET.get('page'))))


@request_method_check('POST')
@login_require
def add_activity(request):
    data = json.loads(request.body)
    user = request.user
    if not isinstance(user, UserProfile):
        return JsonResponse(error_return(ErrorInformation.no_such_topic))
    sponsor = data.get('sponsor')
    title = data.get('title')
    place = data.get('place')
    poster = data.get('poster')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    description = data.get('description')
    categories_id = data.get('categories')
    start_time = datetime.fromtimestamp(int(start_time))
    end_time = datetime.fromtimestamp(int(end_time))
    activity = Activity.objects.create(sponsor=sponsor, title=title, place=place, poster=poster, start_time=start_time,
                                       end_time=end_time, sender=user, description=description)
    if not activity:
        return JsonResponse(error_return(ErrorInformation.create_fail))
    for i in categories_id:
        category = from_id_get_object(i, ActivityCategory)
        if category:
            activity.categories.add(category)

    return JsonResponse({'status': True})
