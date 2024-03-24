from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    respone = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    print(exception_class)

    if exception_class == 'AuthenticationFailed':
        respone.data = {
            'error': 'Invalid Email or Password. Please try again.'
        }

    if exception_class == 'NotAuthenticated':
        respone.data = {
            'error': 'Login first to access this resource.'
    }

    if exception_class == 'InvalidToken':
        respone.data = {
            'error': 'Your authetication token is expired. Please login again.'
    }

    return respone