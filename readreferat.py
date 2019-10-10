with open('referat.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
    print(content)

    #print(len(content))


with open('referat.txt', 'r', encoding='utf-8') as myreferat:
    long_line = 0
    num_line = 0
    for li in myreferat:
        line = li.split()
        long_line += len(li)
        num_line += len(line)


    print(long_line)
    print(num_line)







