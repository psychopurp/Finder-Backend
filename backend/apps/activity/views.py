import json
from datetime import datetime

from django.db.models import Q
from django.http import JsonResponse

from error import ErrorInformation
from user.models import UserProfile
from .models import Activity, ActivityCategory
from util.method_util import request_method_check
from util.model_util import get_result_by_query_page, str_page_to_int, from_id_get_object, error_return


@request_method_check('GET')
def get_activities(request):
    query = Q(title__contains=request.GET.get('query')) | Q(end_time__gt=datetime.now())
    return JsonResponse(get_result_by_query_page(Activity, query, str_page_to_int(request.GET.get('page'))))


@request_method_check('POST')
def add_activity(request):
    data = json.loads(request.body)
    sponsor = data.get('sponsor')
    title = data.get('title')
    place = data.get('place')
    poster = data.get('poster')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    description = data.get('description')
    categories_id = data.get('categories')
    author_id = data.get('author_id')
    start_time = datetime.fromtimestamp(int(start_time))
    end_time = datetime.fromtimestamp(int(end_time))
    author = from_id_get_object(author_id, UserProfile)
    if not author:
        return JsonResponse(error_return(ErrorInformation.no_such_user))
    activity = Activity.objects.create(sponsor=sponsor, title=title, place=place, poster=poster, start_time=start_time,
                                       end_time=end_time, sender=author, description=description)
    for i in categories_id:
        category = from_id_get_object(i, ActivityCategory)
        if category:
            activity.categories.add(category)

    return JsonResponse({'status': True})
