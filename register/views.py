from django.views.generic import CreateView
from django.shortcuts import reverse
from django.forms import inlineformset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Team, Contestant
# from .

class TeamCreateView(CreateView):
    template_name = 'register/form.html'
    # form_class = TeamForm
    # success = reverse('register.registered')

def formset_dd(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    ContestantFormSet = inlineformset_factory(Team, Contestant, fields='__all__',
                                              max_num=3, min_num=1, can_delete=False)
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        contestant_formset = ContestantFormSet(request.POST, request.FILES)
        if not team_form.is_valid():
            return render(request, 'register/form.html', {'contestant_formset': contestant_formset,
                                                          'team_form': team_form})
        # try:
        #     Team.objects.get(name=team_form.cleaned_data['name'])
        # except ObjectDoesNotExist:
        #     team_form.add_error('name', 't')
        else:
            if not contestant_formset.is_valid():
                return render(request, 'register/form.html', {
                    'contestant_formset': contestant_formset,
                    'team_form': team_form})
            else:
                team = team_form.save()
                contestant_formset.instance = team
                contestant_formset.save()
        return HttpResponseRedirect(reverse('base:index'))
    else:
        team_form = TeamForm()
        contestant_formset = ContestantFormSet()
    return render(request, 'register/form.html', {'contestant_formset': contestant_formset,
                                                  'team_form': team_form})
