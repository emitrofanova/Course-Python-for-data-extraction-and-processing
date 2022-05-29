from urllib.request import urlopen

fout = open('4.txt','w',encoding='utf-8')
answ = urlopen("https://online.hse.ru/pluginfile.php/604906/question/questiontext/1881125/1/789276/task_7_2_1.html")
html = answ.read().decode('utf-8')
print(html, file=fout)
fout.close()
