
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# from math import sqrt
#
# nums = [-5, 47, 9, 24, 36, -18, 16]
# sr_nums = []
# for num in nums:
#     if num>=0 and sqrt(num).is_integer():
#         sr_nums.append(int(sqrt(num)))
# print(sr_nums)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days = {
    '01':'первое','02':'второе','03':'третье','04':'четвертое','05':'пятое','06':'шестое',
    '07':'седьмое','08':'восьмое','09':'девятое','10':'десятое','11':'одиннадцатое',
    '12':'двенадцатое','13':'тринадцатое','14':'четырнадцатое','15':'пятнадцатое',
    '16':'шестнадцатое','17':'семнадцатое','18':'восемнадцатое','19':'девятнадцатое',
    '20':'двадцатое','21':'двадцать первое','22':'двадцать второе','23':'двадцать третье',
    '24':'двадцать четвертое','25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое',
    '28':'двадцать восьмое','29':'двадцать девятое','30':'тридцатое','31':'тридцать первое'
    }
months = {
    '01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая','06':'июня','07':'июля',
    '08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'
    }
output=[]
tmp_data=str(input('Введите дату в формате dd.mm.yyyy\n'))
data = tmp_data.split('.')
#print(tmp_data[2:6:3]) - тест программы на наличие разделительных точек в строке даты
if len(tmp_data)!= 10 or tmp_data[2:6:3]!='..' or (data[0].isdigit()==False or data[1].isdigit()==False or data[2].isdigit()==False):
    print('Вы ввели дату в неправильном формате.')
else:
    #data = tmp_data.split('.')
    #if data[0].isdigit() or data[1].isdigit() or data[2].isdigit()==False:
        #print('Вы ввели дату в неправильном формате')
    years=int(data[2])
    #print(data) - проверка работы метода split в программе
    #output.append(days[data[0]])
    #output.append(months[data[1]])
    #output.append(int(data[2]))
    if data[1]=='02' and data[0]=='29' and years%4!=0:
        print('Этот год не високосный, в феврале 28 дней')
    elif data[1]=='02' and (data[0]=='30'or data[0]=='31'):
        print('В феврале не может быть столько дней. Вы ввели некорректные данные.')
    elif data[0]=='31' and (data[1]=='04'or data[1]=='06'or data[1]=='09'or data[1]=='11'):
        print('В этом месяце 30 дней, вы неправильно ввели день')
    else:
        print('{} {} {} года'.format(days[data[0]], months[data[1]], years))
        # print('{} {} {} года'.format(output[0],output[1],output[2]))