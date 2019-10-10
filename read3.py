
'''with open('referat2.txt', 'r', encoding='utf-8') as my_save1:
    d = my_save1.read()
with open('referat2.txt', 'w', encoding='utf-8') as my_save2:
    for line in my_save2:
        my_save1.write(line.replace('.', '!'))'''

#print(li2)
"""with open('referat2.txt', 'r', encoding='utf-8') as my_save2:
    for li2 in my_save2:
        li2 = li2.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(li2)"""

f1 = open('referat.txt', 'r', encoding='utf-8')
f2 = open('referat2.txt', 'w', encoding='utf-8')
for line in f1:
    f2.write(line.replace('.', '!'))
f1.close()
f2.close()

with open('referat.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
with open('referat2.txt', 'w', encoding='utf-8') as my_save:
    d = my_save.write(str(content))

"""with open('referat2.txt', 'r', encoding='utf-8') as my_save2:
    for li2 in my_save2:
        li2 = li2.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(li2)"""


    #with open('referat2.txt', 'w', encoding='utf-8') as my_save:
        #d = my_save.write(str(content))

    #with open('referat2.txt', 'w', encoding='utf-8') as my_saverep:
            #print(d)





    #line = (f.readlines())
    #line = set
    #print(content)
    #print(len(content))
    #print(len(line))
    #print(len(line1))

with open('referat.txt', 'r', encoding='utf-8') as myreferat:
    long_line = 0
    num_line = 0
    for li in myreferat:
        line = li.split()
        li = li.replace('.', '!')
        long_line += len(li)
        num_line += len(line)



    print(long_line)
    print(num_line)
    #with open('referat2.txt', 'w', encoding='utf-8') as my_save:






