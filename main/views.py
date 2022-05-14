import datetime
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
time = datetime.datetime.now().replace(second=0, microsecond=0)

def test(request):
    return HttpResponse('<h1 style="color:blue;">Добро пожаловать в кинотеатр Broadway!</h1>')

def test1(request):
    dict_ = {
        'title': 'О кинотеатре',
        'text': 'КИНОТЕАТР «Broadway» - один из самых больших кинокомплексов Кыргызстана!'
                ' Новый, современный кинотеатр, 7 кинозалами, рассчитанный на 805 мест,'
                ' также вы можете насладиться первым VIP залом отличающимся своей комфортабельностью. '
                'Кресла укомплектованы механизмами трансформации и столиками! Нажав на кнопку вы можете '
                'наслаждаться просмотром фильма в лежачем положении. Кинотеатр оснащен самым современным '
                'кинопроекционным оборудованием в индустрии от мирового лидера систем визуализации Barco,'
                ' звуком от Dolby Digital .'
    }
    return render(request, "hello.html", context=dict_)

def test2(request):
    dict_ = {
        'title': 'Акции и скидки',
        'text': 'Волшебство бывает! По вторникам предоставляется единая цена билетов на фильмы в кинотеатре'
                ' «Broadway» Стоимость одного билета по акции «Волшебный вторник» составляет 170 сом Обращаем '
                'внимание гостей кинотеатра, что действие акции «Волшебный вторник» не распространяется на'
                ' сеансы фильмов, находящиеся под меморандумом кинопрокатной компании *Проведи вторник в '
                'кинотеатре Бродвей!'
    }
    return render(request, "hello.html", context=dict_)

def test3(request):
    dict_ = {
        'title': 'Сеансы на сегодня',
        'text': '17:35 "Доктор Стрэндж: В мультивселенной безумия"\n\n'
                '17:55 "Рецепт счастья"\n\n'
                '18:10 "Отряд "Призрак"',
        'data': f'{time}'
    }

    return render(request, "hello.html", context=dict_)