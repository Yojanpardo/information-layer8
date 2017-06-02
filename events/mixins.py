from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

class LoginRequiredMixin(object):
	@method_decorator(staff_member_required())
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request,
			*args, **kwargs)
