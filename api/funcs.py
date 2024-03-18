def filter_post(request):
    result = {}
    for key, value in request.GET.items():
        result[key] = value
    return result