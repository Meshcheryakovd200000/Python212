from django.shortcuts import render
from .models import Profile


# Create your views here.

# Все профили пользовател
def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


# Профиль конкретного пользователя
def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skill = prof.skill_set.exclude(
        description__exact="")  # получаем доступ к классу Skill обращаемся к классу Skill "skill_set"
    # в нижнем регистре (т.к. таблицы в БД в нижнем регистре), и исключаем элементы если description пустой "exclude()"

    other_skills = prof.skill_set.filter(description="") # берем элементы у которых дескрипшин пустой

    context = {
        'profile': prof,
        'top_skills': top_skill,
        'other_skills': other_skills,
    }
    return render(request, 'users/profile.html', context)



















