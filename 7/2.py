fout = open('2.html', 'w', encoding='utf-8')
print("<html>","<body>","<table>", file=fout)
for i in range(1,11):
    print("<tr>", file=fout)
    for j in range(1,11):
        print("<td>",i*j,"</td>", sep='',end='', file=fout)
    print("</tr>", file=fout)
print("</table>","</body>","</html>", file=fout)
fout.close()
