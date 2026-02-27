from healthcare.common.exceptions import NotFoundException, BadRequestException, ExternalServiceException
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, NotFoundException):
        return Response(
            {
                'success': False,
                'error': str(exc)
            },
            status=status.HTTP_404_NOT_FOUND
        )
        
    if isinstance(exc, BadRequestException):
        return Response(
            {
                'success': False,
                'error': str(exc)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if isinstance(exc, ExternalServiceException):
        return Response(
            {
                'success': False,
                'error': str(exc)
            },
            status = status.HTTP_503_SERVICE_UNAVAILABLE
        )
        
    if response is not None:
        if isinstance(response.data, dict):
            return Response(
                {
                    'success': False,
                    'errors': response.data
                },
                status = response.status_code
            )
    
    return Response(
        {
            'success': False,
            'error': 'Internal Server Error'
        },
        status = status.HTTP_500_INTERNAL_SERVER_ERROR
    )