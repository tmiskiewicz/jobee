from django_filters import rest_framework as filters 
from .models import Job

class JobsFilter(filters.FilterSet):

    min_salary = filters.NumberFilter(field_name='salary' or 0, lookup_expr='gte') #gte znaczy equals to 
    max_salary = filters.NumberFilter(field_name='salary' or 1000000, lookup_expr='lte') #gte znaczy equals to 
    keyword = filters.CharFilter(field_name='title', lookup_expr = 'icontains') #wyglada na to, ze to pozwala szukac po key wordach, wystaczy icontains
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')

    class Meta:

        model = Job
        fields = ('Education', 'jobType', 'Experience','min_salary', 'max_salary', 'keyword', 'location')