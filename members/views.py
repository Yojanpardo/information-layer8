from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Member
from .forms import MemberForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Member
from .forms import MemberForm

import os
from datetime import date
from io import BytesIO
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Image

# class MemberCreate(LoginRequiredMixin, CreateView):
#     model = Member
#     success_url = reverse_lazy('members:home')
#     fields = ['name', 'last_name', 'phone', 'email', 'address',
#               'personal_skills', 'team_skills', 'weakness',
#               'under_presure',]

class MemberList(LoginRequiredMixin, ListView):
    model = Member

class MemberDetail(LoginRequiredMixin, DetailView):
    model = Member

# class MemberUpdate(LoginRequiredMixin, UpdateView):
#     model = Member
#     success_url = reverse_lazy('members:home')
#     fields = ['name', 'last_name', 'phone', 'email', 'address',
#               'personal_skills', 'team_skills', 'weakness',
#               'under_presure', 'illness']
#
# class MemberDelete(LoginRequiredMixin, DeleteView):
#     model = Member
#     success_url = reverse_lazy('members:home')

@login_required()
def reportPDF(request):
    members = Member.objects.order_by('id')


    #Create The HttpResponse headers with PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="MemberLog.pdf"'

    #Create the PDF object, using the BytesIO object as it's "file."
    buffer = BytesIO()
    fecha = date.today()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Information Layer 8')
    c.setFont('Helvetica', 10)
    c.drawString(60, 735, 'Notes and information')
    c.setFont('Helvetica', 10)
    c.drawString(75, 720, 'about your team')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, fecha.__str__())
    c.line(460,747,560,747)

    for member in members:
        this_member = [member.name,
                        member.last_name,
                        member.phone,
                        member.email,
                        member.address,
                        member.personal_skills,
                        member.team_skills,
                        member.weakness,
                        member.under_presure,
                        member.illness]

    c.setFont('Helvetica-Bold', 16)
    c.line(30,700,560,700)

    #Name
    c.setFont('Helvetica', 28)
    c.drawString(30, 670, this_member[0])
    c.setFont('Helvetica', 28)
    c.drawString(120, 670, this_member[1])
    #Email
    c.setFont('Helvetica', 14)
    c.drawString(30, 652, this_member[3])

    c.setFont('Helvetica-Bold', 16)
    c.line(30,614,560,614)

    #Information
    c.setFont('Helvetica', 20)
    c.drawString(30, 580, 'Personal Skill: ')
    c.setFont('Helvetica', 18)
    c.drawString(250, 580, this_member[5])

    c.setFont('Helvetica', 20)
    c.drawString(30, 560, 'Team Skill: ')
    c.setFont('Helvetica', 18)
    c.drawString(250, 560, this_member[6])

    c.setFont('Helvetica', 20)
    c.drawString(30, 540, 'Weakness: ')
    c.setFont('Helvetica', 18)
    c.drawString(250, 540, this_member[7])

    c.setFont('Helvetica', 20)
    c.drawString(30, 520, 'Work Skill: ')
    c.setFont('Helvetica', 18)
    c.drawString(250, 520, this_member[8])

    c.setFont('Helvetica', 20)
    c.drawString(30, 500, 'Illness: ')
    c.setFont('Helvetica', 18)
    c.drawString(250, 500, this_member[9])

    c.setFont('Helvetica-Bold', 16)
    c.line(30,480,560,480)
    
    lorems = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    		  'Phasellus vitae placerat libero, quis tincidunt neque. ',
    		  'Fusce non nunc facilisis, ullamcorper enim sit amet, ',
    		  'dictum enim. Quisque justo orci, tincidunt a erat congue, ',
    		  'faucibus aliquet mauris. Duis ullamcorper facilisis blandit. ',
    		  'Vivamus suscipit nisl dolor, ut auctor mauris fermentum quis. ',
    		  'Duis sagittis velit neque, vitae finibus ante cursus a. Integer',
    		  'in velit vulputate, sollicitudin leo id, lobortis quam.',
    		  'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    		  'Phasellus vitae placerat libero, quis tincidunt neque. ',
    		  'Fusce non nunc facilisis, ullamcorper enim sit amet, ',
    		  'dictum enim. Quisque justo orci, tincidunt a erat congue, ',
    		  'faucibus aliquet mauris. Duis ullamcorper facilisis blandit. ',
    		  'Vivamus suscipit nisl dolor, ut auctor mauris fermentum quis. ',
    		  'Duis sagittis velit neque, vitae finibus ante cursus a. Integer',
    		  'in velit vulputate, sollicitudin leo id, lobortis quam.',]

    space = 450

    for lorem in lorems:
    	c.setFont('Helvetica', 16)
    	space = space-20
    	c.drawString(85, space, lorem)

    c.setFont('Helvetica-Bold', 16)
    c.line(30,100,560,100)

    #PDF Size
    c.showPage() #Save Page

    #Save PDF
    c.save()

    #Get the value of BytesIO buffer and write response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response