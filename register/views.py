from django.shortcuts import reverse
from django.forms import inlineformset_factory, modelform_factory, TextInput
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Team, Contestant

def team_create(request):
    team_widgets = {'name': TextInput(attrs={'placeholder': 'Team Name'}),
                    'school': TextInput(attrs={'placeholder': 'School'})}
    contestant_widgets = {'first_name': TextInput(attrs={'placeholder': 'First Name'}),
                          'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
                          'email': TextInput(attrs={'placeholder': 'Email'})}
    TeamForm = modelform_factory(Team, fields='__all__', widgets=team_widgets)
    ContestantFormSet = inlineformset_factory(Team, Contestant, fields='__all__',
                                              max_num=3, min_num=1, can_delete=False,
                                              widgets=contestant_widgets)
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        contestant_formset = ContestantFormSet(request.POST, request.FILES)
        if not team_form.is_valid():
            return render(request, 'register/form.html', {'contestant_formset': contestant_formset,
                                                          'team_form': team_form})
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
