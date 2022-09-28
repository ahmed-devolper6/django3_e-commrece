
from .models import Proflie

def get_user(request):
    if request.user.is_authenticated:
        proflie = Proflie.objects.get(user = request.user)
        return {'user_proflie':proflie}
    else:
        return {}