from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods

from tasks.forms import ReviewForm
from tasks.models import Review

@require_GET
def index(request):
    return redirect("tasks:review_list")

@require_http_methods(["GET", "POST"])
def review_list(request):
    status = 200
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:review_list")
        status = 400
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(
        request,
        'tasks/review_list.html',
        {'reviews': reviews, "form": form},)

