import django_filters
from job.models import Job

class Jobfilter(django_filters.FilterSet):
    class Meta:
        title = django_filters.CharFilter(lookup_expr='icontains')
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']