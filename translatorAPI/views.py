from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api_functions import get_correct_word, get_synonyms, get_parts_of_speech, get_trans, get_all, languages_dict
from APIRegistration.models import user
# Create your views here.


def is_valid_key(key):
    u = user.objects.filter(token=key)
    if u:
        return True
    return False


@api_view(['POST'])
def all(request):
    if request.method == 'POST':
        '''
        # key = request.META.get('HTTP_KEY')
        # if not is_valid_key(key):
        #     return Response({'status': 403, 'message': 'key not valid!'})
        '''
        try:
            data = request.data
            res = get_all(data['text'], data['from'], data['to'])
            return Response({'status': 200, 'payload': res, 'message': 'api working'})
        except Exception as e:
            print(e)
            return Response({'status': 503, 'error': 'Something went wrong!'})
    return Response({'status': 405, 'message': 'Method not allowed!'})


@api_view(['POST'])
def parts_of_speech(request):
    if request.method == 'POST':
        try:
            data = request.data
            res = get_parts_of_speech(data['text'])
            return Response({'status': 200, 'payload': res, 'message': 'api working'})
        except Exception as e:
            print(e)
            return Response({'status': 503, 'error': 'Something went wrong!'})
    return Response({'status': 405, 'message': 'Method not allowed!'})


@api_view(['POST'])
def synonyms(request):
    if request.method == 'POST':
        try:
            data = request.data
            res = get_synonyms(data['text'])

            return Response({'status': 200, 'payload': res, 'message': 'api working'})
        except Exception as e:
            print(e)
            return Response({'status': 503, 'error': 'Something went wrong!'})
    return Response({'status': 405, 'message': 'Method not allowed!'})


@api_view(['POST'])
def parts_of_speech(request):
    if request.method == 'POST':
        try:
            data = request.data
            res = get_parts_of_speech(data['text'])
            return Response({'status': 200, 'payload': res, 'message': 'api working'})
        except Exception as e:
            print(e)
            return Response({'status': 503, 'error': 'Something went wrong!'})
    return Response({'status': 405, 'message': 'Method not allowed!'})


@api_view(['POST'])
def translation(request):
    if request.method == 'POST':
        try:
            data = request.data
            res = get_trans(data['text'], data['from'], data['to'])
            return Response({'status': 200, 'payload': res, 'message': 'api working'})
        except Exception as e:
            print(e)
            return Response({'status': 503, 'error': 'Something went wrong!'})
    return Response({'status': 405, 'message': 'Method not allowed!'})


@api_view(['GET'])
def languages(request):
    try:
        return Response({'status': 200, 'payload': languages_dict, 'messsage': 'api working'})
    except Exception as e:
        print(e)
        return Response({'status': 503, 'error': 'Something went wrong!'})
