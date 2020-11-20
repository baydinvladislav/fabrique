from django.shortcuts import render, get_object_or_404
from .models import Poll, Question
from django.views import generic
from django.http import Http404

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls_list'

    def get_queryset(self):
        return Poll.objects.all()


def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
        questions = poll.question_set.all
    except Poll.DoesNotExist:
        raise Http404('Такого опроса не существует')
    return render(request, 'polls/detail.html', {'poll': poll, 'questions': questions})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
