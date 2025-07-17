from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance

@api_view(['GET'])
def get_attendance_records(request):
    user_id = request.GET.get('user_id')
    class_name = request.GET.get('class_name')
    month = request.GET.get('month')
    year = request.GET.get('year')

    filters = {}

    if user_id:
        filters['user__id'] = user_id
    if class_name:
        filters['class_name__iexact'] = class_name
    if month:
        filters['date__month'] = int(month)
    if year:
        filters['date__year'] = int(year)

    records = Attendance.objects.filter(**filters).values(
        'user__username', 'class_name', 'date', 'status'
    )

    return Response(records)


