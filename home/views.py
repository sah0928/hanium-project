from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
from .forms import PersonForm

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    msg = 'Welcome!'
    all_people = Person.objects.all()
    form = PersonForm()

    # ### person 추가 코드 ###
    # new_person = Person(id="201809011530301", label="person1", position_x="10", position_y="10", width="", height="", color_upper="", color_lower="")
    # new_person.save()

    return render(request, 'home/index.html', {'message': msg, 'people': all_people, 'form': form})
    # context안에 있는 Post 정보를 index.html로 전달


def search(request):
    colorUpper = request.GET.get('colorUpper', '')
    colorLower = request.GET.get('colorLower', '')

    all_people = Person.objects.all()

    if colorUpper:
        all_people = all_people.filter(colorUpper__icontains=colorUpper)
    else:
        colorUpper = 'not select'

    if colorLower:
        all_people = all_people.filter(colorLower__icontains=colorLower)
    else:
        colorLower = 'not select'

    return render(request, 'home/search.html',
                  {'people': all_people, 'colorUpper': colorUpper, 'colorLower': colorLower})


def video(request):
    return render(request, 'home/video.html')


def cctv(request):
    id = request.GET.get('id', '')
    label = request.GET.get('label', '')

    date = id[:-1]
    count = 0
    cctvList = []

    while True:
        try:
            person = Person.objects.get(id__startswith=date, label=label)
            if person is not None:
                cctvList.append(person.id)
                count = count + 1
            else:
                break

            date = str(int(date) + 1)

        except ObjectDoesNotExist:
            print('Does Not Exist!')
            break

    # while True:
    #     try:
    #         person = Person.objects.get(id__startswith=date, label=label)
    #         if person is not None:
    #             list.append(person.id)
    #             date = str(int(date) + 1)
    #             count = count + 1
    #         else:
    #             break
    #     except Person.DoesNotExist:
    #         person = None

    return render(request, 'home/cctv.html',
                  {'id': id, 'label': label, 'count': count, 'list': cctvList, 'person': person})
