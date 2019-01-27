from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View


from .models import Lunch
from .models import Location


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        available_lunches = Lunch.objects.all()

        context = {
            "lunches" : available_lunches
        }

        return context


class Details(TemplateView):
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        available_locations = Location.objects.all()

        # The contest primary key is included on the url: locahost:8000/5/
                # We use value capturing in our urls.py to get the # 5 and save it to pk
                # The pk variable is in the dictionary self.kwargs, and we can use .get() on
                # the self.kwargs dict.
        lunch_pk = self.kwargs.get('pk')

                # Now that we have the primary key for the contest, use the ORM to get the
                # object from the database
        lunch= Lunch.objects.get(pk=lunch_pk)

        context = {
                "location" : available_locations
        }

        return context


class Results(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs):

        lunch_pk = self.kwargs.get('pk')
        lunch = Lunch.objects.get(pk=contest_pk)

            # Create a context dictionary that will be sent to our template
        context = {
                'lunch': lunch
        }


# This view will not be a template view since we won't actually show a screen.
# Once a user submits to this screen we will redirect.
class Vote(View):


    # We are going to receive a POST request with this view, so we're going to create a method called post.
    def post(self, request, **kwargs):

        lunch_pk = self.kwargs.get('pk')

        # Now that we have the primary key for the contest, use the ORM to get the
        # object from the database
        lunch = Lunch.objects.get(pk=contest_pk)

        # The user selected a picture that they wanted to vote for in the contest.
        # They selected one of the radio buttons: <input name="photo" value="2" .../>
        # When they submitted the form, the name of the input got sent to the server with the value in the input.
        # We can use the input name get the value from the POST dictionary.
        location_voted_for_id = self.request.POST.get('location ')

        # Now we want to take our contest and lookup the photo object that the user selected
        selected_location = lunch.photo_set.get(pk=location_voted_for_id)

        selected_location.votes += 1
        selected_location.save()

        # Now get the URL for our results screen using the route name from urls.py
        results_url = reverse('location:results', args=(lunch.pk,))

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(results_url)
