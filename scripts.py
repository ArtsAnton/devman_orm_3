import logging
import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Mark, Commendation, Chastisement, Lesson, Schoolkid


def fix_marks(schoolkid, new_mark=5):
    neg_marks = Mark.objects.filter(schoolkid=schoolkid.id, points__lte=3)
    for mark in neg_marks:
        mark.points = new_mark
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    chastisements.delete()


def create_commendation(name, subject):
    commendations = ["Молодец!", "Отлично!", "Хорошо!"]
    commendation = random.choice(commendations)
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name.title())
        last_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                              group_letter=schoolkid.group_letter,
                              subject__title=subject.capitalize()).order_by("-date")[0]
        Commendation.objects.create(text=commendation,
                                     created=last_lesson.date,
                                     schoolkid=schoolkid,
                                     subject=last_lesson.subject,
                                     teacher=last_lesson.teacher)
    except ObjectDoesNotExist as error:
        logging.error(error)
    except MultipleObjectsReturned as error:
        logging.error(error)


