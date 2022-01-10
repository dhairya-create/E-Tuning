from django.shortcuts import redirect
from home.models import Register

def artist_auth_middleware(get_response):

    def middleware(request):
        print("middleware")
        id = request.session.get('customer')
        cust = Register.objects.get(id = id)
        if cust.usertype == 'artist':
            return redirect('/register')
        else:
            response = get_response(request)
            return response
    
    return middleware