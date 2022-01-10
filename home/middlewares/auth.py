from django.shortcuts import redirect
def auth_middleware(get_response):

    def middleware(request):
        print("middleware")
        if not request.session.get('customer'):
            return redirect('/login')
        else:
            response = get_response(request)
            return response
    
    return middleware