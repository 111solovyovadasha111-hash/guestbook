import pytest

pytestmark = pytest.mark.django_db


def test_review_creation():
    from tasks.models import Review

    review = Review.objects.create(author="Эдвард", text="хоухоухоухоу")
    assert review.author == "Эдвард"
    assert review.text == "хоухоухоухоу"
    assert Review.objects.count() == 1


def test_valid_form():
    from tasks.forms import ReviewForm

    form_data = {"author": "Эдвард", "text": "хоухоухоухоу"}
    form = ReviewForm(data=form_data)
    assert form.is_valid()

    review = form.save()
    assert review.author == "Эдвард"


def test_empty_fields():
    from tasks.forms import ReviewForm

    form_data = {"author": "", "text": ""}
    form = ReviewForm(data=form_data)
    assert not form.is_valid()
    assert "author" in form.errors
    assert "text" in form.errors


def test_whitespace_fields_():
    from tasks.forms import ReviewForm

    form_data = {"author": "   ", "text": "\t \n "}
    form = ReviewForm(data=form_data)
    assert not form.is_valid()
    assert "author" in form.errors
    assert "text" in form.errors