from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'sharlotka': {
        'мука, ст.': 0.5,
        'сахар, ст.': 0.5,
        'яйцо, шт.': 3
    }
}

def get_context(dish, servings):
    items = {f'{dish} кол-во, шт': servings}
    for i in DATA[dish]:
        items[i] = DATA[dish][i] * int(servings)
    context = {'recipe': items}
    return context


def omlet(request):
    context = get_context('omlet', request.GET.get('servings', '1'))
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = get_context('pasta', request.GET.get('servings', '1'))
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = get_context('buter', request.GET.get('servings', '1'))
    return render(request, 'calculator/index.html', context)

def sharlotka(request):
    context = get_context('sharlotka', request.GET.get('servings', '1'))
    return render(request, 'calculator/index.html', context)
