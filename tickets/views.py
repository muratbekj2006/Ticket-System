from django.views.generic import CreateView, ListView

from .models import *


class JourneyListView(ListView):
    model = Journey
    template_name = "tickets/transportation_list.html"
    context_object_name = "transportation"


class TicketCreateView(CreateView):
    model = Ticket
    template_name = "ticket/ticket_new.html"
    fields = ["transportation", "adult_ticket", "child_ticket"]
