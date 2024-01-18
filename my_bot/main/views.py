from django.shortcuts import render
from django.http import HttpResponse
from .models import Test, Levels

def main(request, level_m):

    levels_model = Levels.objects.all()
    level_name = levels_model[level_m-1]


    all_datas = Test.objects.filter(level=level_m)

    # for i in all_datas:
    #     print(i.text_content)
    #     print(i.image_file)
    #     print(i.voice_file)
    return render(request, "main.html", {'all_data': all_datas, 'level_name': level_name})

def choose_level(request):
    levels_model = Levels.objects.all()

    return render(request, "level.html", {'levels': levels_model})