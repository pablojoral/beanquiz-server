from django.http import JsonResponse

def test(request):
    message = 'grande cabeza'
    data = {
        'message': message
    }
    return JsonResponse(data)