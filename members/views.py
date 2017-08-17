from django.views.generic import ListView

from .models import Member

class MemberListView(ListView):
    template_name = 'members/members.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        return Member.objects.order_by('last_name')[:]