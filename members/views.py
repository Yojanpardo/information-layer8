from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Member
from .forms import MemberForm

# class MemberCreate(LoginRequiredMixin, CreateView):
#     model = Member
#     success_url = reverse_lazy('members:home')
#     fields = ['name', 'last_name', 'phone', 'email', 'address',
#               'personal_skills', 'team_skills', 'weakness',
#               'under_presure',]

class MemberList(ListView):
    model = Member

class MemberDetail(LoginRequiredMixin, DetailView):
    model = Member

# class MemberUpdate(LoginRequiredMixin, UpdateView):
#     model = Member
#     success_url = reverse_lazy('members:home')
#     fields = ['name', 'last_name', 'phone', 'email', 'address',
#               'personal_skills', 'team_skills', 'weakness',
#               'under_presure',]
#
# class MemberDelete(LoginRequiredMixin, DeleteView):
#     model = Member
#     success_url = reverse_lazy('members:home')
