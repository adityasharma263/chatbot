# -*- coding: utf-8 -*-
__author__ = 'aditya_sharma'

# 2xx Success
return_200 = {'content': {'result': {},
                          'message': 'Success', 'error': False}, 'status': 200}
return_201 = {'content': {'result': {},
                          'message': 'Successfully Created', 'error': False}, 'status': 201}
return_204 = {'content': {'result': {},
                          'message': 'No Content', 'error': False}, 'status': 204}

# 3xx No changes
return_304 = {'content': {'result': {},
                          'message': 'No Modified', 'error': True}, 'status': 304}

# 4xx Client Error
return_400 = {'content': {'result': {},
                          'message': 'Bad Request', 'error': True}, 'status': 400}
return_401 = {'content': {'result': {},
                          'message': 'Unauthorized Access', 'error': True}, 'status': 401}
return_402 = {'content': {'result': {},
                          'message': 'Something is Missing', 'error': True}, 'status': 402}
return_403 = {'content': {'result': {},
                          'message': 'Forbidden', 'error': True}, 'status': 403}
return_404 = {'content': {'result': {},
                          'message': 'Not Found', 'error': True}, 'status': 404}
return_405 = {'content': {'result': {},
                          'message': 'Method Not Allowed', 'error': True}, 'status': 405}
return_409 = {'content': {'result': {},
                          'message': 'Conflict Occurred', 'error': True}, 'status': 409}

# 5xx Server/Database Error
return_500 = {'content': {'result': {},
                          'message': 'Internal Server Error', 'error': True}, 'status': 500}
return_502 = {'content': {'result': {},
                          'message': 'Bad Gateway', 'error': True}, 'status': 502}
return_503 = {'content': {'result': {},
                          'message': 'Service Unavailable', 'error': True}, 'status': 503}


class ReturnObj(object):

    @staticmethod
    def ret(x):
        return {
            200: {'content': {'result': {},
                              'message': 'Success', 'error': False}, 'status': 200},
            201: {'content': {'result': {},
                              'message': 'Successfully Created', 'error': False}, 'status': 201},
            204: {'content': {'result': {},
                              'message': 'No Content', 'error': False}, 'status': 204},
            304: {'content': {'result': {},
                              'message': 'No Modified', 'error': True}, 'status': 304},
            400: {'content': {'result': {},
                              'message': 'Bad Request', 'error': True}, 'status': 400},
            401: {'content': {'result': {},
                              'message': 'Unauthorized Access', 'error': True}, 'status': 401},
            402: {'content': {'result': {},
                              'message': 'Something is Missing', 'error': True}, 'status': 402},
            403: {'content': {'result': {},
                              'message': 'Forbidden', 'error': True}, 'status': 403},
            404: {'content': {'result': {},
                              'message': 'Not Found', 'error': True}, 'status': 404},
            405: {'content': {'result': {},
                              'message': 'Method Not Allowed', 'error': True}, 'status': 405},
            409: {'content': {'result': {},
                              'message': 'Conflict Occurred', 'error': True}, 'status': 409},
            500: {'content': {'result': {},
                              'message': 'Internal Server Error', 'error': True}, 'status': 500},
            502: {'content': {'result': {},
                              'message': 'Bad Gateway', 'error': True}, 'status': 502},
            503: {'content': {'result': {},
                              'message': 'Service Unavailable', 'error': True}, 'status': 503},
        }[x]
