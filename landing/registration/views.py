from django.shortcuts import render, redirect
from .models import *
from .forms import RegisterForm
from .handlers import bot



def index(request):

    if request.method == 'POST':
        cap_name = request.POST['captain']
        cap_pro_potok = request.POST['captain-group']

        mem2 = request.POST['member-2']
        mem2_pro_potok = request.POST['member-2-group']
        mem3 = request.POST['member-3']
        mem3_pro_potok = request.POST['member-3-group']
        mem4 = request.POST['member-4']
        mem4_pro_potok = request.POST['member-4-group']
        mem5 = request.POST['member-5']
        mem5_pro_potok = request.POST['member-5-group']
        mem6 = request.POST['member-6']
        mem6_pro_potok = request.POST['member-6-group']
        main_text = 'Новая команда\n'

        main_text += f'Капитан\nИмя: {cap_name}\nСпециальность и поток: {cap_pro_potok}\n\n'
        main_text += f'Второй участник: {mem2}, {mem2_pro_potok}\n' \
                     f'Третий участник: {mem3}, {mem3_pro_potok}\n' \
                     f'Четвёртый участник: {mem4}, {mem4_pro_potok}\n' \
                     f'Пятый участник: {mem5}, {mem5_pro_potok}\n' \
                     f'Шестой участник: {mem6}, {mem6_pro_potok}'
        bot.send_message(-1001892934814, main_text)
        return redirect('done')


    return render(request, 'index.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            global cap1
            global cap2
            global cap3
            global cap4

            cap1 = request.POST.get('name')
            cap2 = request.POST.get('surname')
            cap3 = request.POST.get('pro')
            cap4 = request.POST.get('potok')


            return redirect('done')
        else:
            error = 'Неверно'


    form = RegisterForm()
    context = {'form': form, 'error': error}

    return render(request, 'index.html', context)


# def create_team(request):
#     error = ''
#     if request.method == 'POST':
#         form_team = Register_TeamForm(request.POST)
#         if form_team.is_valid():
#             form_team.save()
#
#             p = Member.objects.all()
#             u = Captain.objects.all()
#             for e in u:
#                 cap = f'Капитан\nИмя: {e.surname} {e.name}\nСпециальность: {e.pro}\nПоток: {e.potok}\n\n'
#             i = request.POST.get('member_name1')
#             i1 = request.POST.get('member_surname1')
#             i2 = request.POST.get('member_name2')
#             i3 = request.POST.get('member_surname2')
#             i4 = request.POST.get('member_name3')
#             i5 = request.POST.get('member_surname3')
#             i6 = request.POST.get('member_name4')
#             i7 = request.POST.get('member_surname4')
#             i8 = request.POST.get('member_name5')
#             i9 = request.POST.get('member_surname5')
#             for m in p:
#                 o1 = f'{m.pro1}'
#                 o3 = f'{m.pro2}'
#                 o5 = f'{m.pro3}'
#                 o7 = f'{m.pro4}'
#                 o9 = f'{m.pro5}'
#
#             o2 = request.POST.get('potok1')
#             o4 = request.POST.get('potok2')
#             o6 = request.POST.get('potok3')
#             o8 = request.POST.get('potok4')
#             o10 = request.POST.get('potok5')
#
#
#             main_text = 'Новая команда\n'
#
#             main_text += cap
#
#             main_text += f'Второй участник\n{i1} {i}\n{o1}, {o2}\n\n' \
#                              f'Третий участник\n{i3} {i2}\n{o3}, {o4}\n\n'\
#                              f'Четвертый участник\n{i5} {i4}\n{o5}, {o6}\n\n' \
#                              f'Пятый участник\n{i7} {i6}\n{o7}, {o8}\n\n' \
#                              f'Шестой участник\n{i9} {i8}\n{o9}, {o10}\n'
#             bot.send_message(-1001892934814, main_text)
#             return redirect('done')
#         else:
#             error = 'Неверно'
#
#
#     form_team = Register_TeamForm()
#     context = {'form': form_team, 'error': error}
#
#     return render(request, 'members.html', context)


def done(request):
    return render(request, 'done.html')


