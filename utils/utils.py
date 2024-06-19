from rest_framework import status
from rest_framework.response import Response


def handle_serialization(serializer, success_status, error_status):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=success_status)
    return Response(serializer.errors, status=error_status)
