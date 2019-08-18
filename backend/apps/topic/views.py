from django.db.models import Q
from django.http import JsonResponse

from error import ErrorInformation
from topic.models import Topic, TopicComment
from util.method_util import request_method_check
from util.model_util import get_result_by_query_page, str_page_to_int, error_return, model_to_dict, from_id_get_object


@request_method_check('GET')
def get_topics(request):
    query = request.GET.get('query')
    if query:
        query = Q(title__contains=query)
    return JsonResponse(get_result_by_query_page(Topic, query, str_page_to_int(request.GET.get('page'))))


@request_method_check('GET')
def get_topic_comments(request):
    topic_id = request.GET.get('topic_id')
    query = request.GET.get('query')
    topic = from_id_get_object(topic_id, Topic)
    if not topic:
        return JsonResponse(error_return(ErrorInformation.no_such_topic))
    if query:
        query = Q(content__contains=query) & Q(topic=topic)
    else:
        query = Q(topic=topic)
    result = get_result_by_query_page(TopicComment, query, str_page_to_int(request.GET.get('page')),
                                      ['id', ('sender', model_to_dict, ['nickname', 'avatar', 'id']),
                                       ('content', "to_python"), 'refer_comment', 'root'])
    for i in result['data']:
        i['has_reply'] = i['root'] or len(TopicComment.objects.filter(root=TopicComment.objects.get(i['id']))) != 0
    return JsonResponse(result)
