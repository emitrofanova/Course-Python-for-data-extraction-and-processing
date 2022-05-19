'''Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость
 с начисленной зарплатой. К счастью, у него сохранились расчётные листки 
 всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную 
 ведомость.

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО 
сотрудника и, через пробел, его зарплата. Сотрудники должны быть упорядочены по алфавиту.
'''
import openpyxl
from openpyxl import load_workbook
fout = open('13out.txt', 'w', encoding='utf-8')
vedom = []
for i in range(1,1001):
    wb = load_workbook('rogaikopyta_6_4_2/' + str(i) + '.xlsx')
    sheet = wb["Sheet"]
    vedom.append((sheet['B2'].value, sheet['D2'].value))
for i in sorted(vedom):
    print(*i, file=fout)
