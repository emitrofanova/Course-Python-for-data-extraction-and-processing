from urllib.request import urlopen

answ = urlopen("https://online.hse.ru/pluginfile.php/604906/question/questiontext/1881240/1/789274/task_7_2_2.html")
html = answ.read().decode('utf-8')
c_P = html.count('Python')
c_C = html.count('C++')
if c_P > c_C:
    print("Python")
else:
    print("C++")
