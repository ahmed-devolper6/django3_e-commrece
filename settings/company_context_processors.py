from .models import Company

def get_company_info(request):
    company = Company.objects.last()
    return {'info':company}