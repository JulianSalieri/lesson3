f1 = open('referat.txt', 'r', encoding='utf-8')
f2 = open('referat2.txt', 'w', encoding='utf-8')
for line in f1:
    f2.write(line.replace('.', '!'))
f1.close()
f2.close()

