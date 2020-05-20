with open('report.txt') as file:
    f1 = file.readlines()
    #分割，添加表头
    lst1 = f1[0].split()
    lst1.insert(0,'序号')
    lst1.extend(['总分','平均分'])
    #print(lst1)

    # 计算每个人的总分和平均分，并添加到列表最后一项
    array = []
    for i in f1[1:]:
        lst2 = i.split()
        sum = 0
        subject = 0
        for score in lst2[1:]:
            sum += int(score)
            subject += 1
        avgscore ='%.1f'% (sum / subject)
        lst2.append(sum)
        lst2.append(avgscore)
        # 把每个人的成绩放入一个新列表中
        array.append(lst2)
    #print(array)

    # 计算科目平均分，放入新建列表avg_lst
    avg_lst = []
    for m in range(1,12):
        all = 0
        count = 0
        for n in range(len(array)):
            all += float(array[n][m])
            count += 1
        avg ='%.1f'% (all / count)
        avg_lst.append(avg)
    avg_lst.insert(0,0)
    avg_lst.insert(1,'平均')
    # print(avg_lst)

    # 替换60分以下的成绩
    for row in array:
        for s in range(1,len(row)):
            if float(row[s]) < 60:
                row[s] = '不及格'
    # print(array)

    #按总分进行排序
    array.sort(key = lambda x:x[-2],reverse = True)
    # print(array)

    #添加序号
    for j in range(len(array)):
        array[j].insert(0,j+1)
    # print(array)

    # 把表头和科目平均分插入到array的第1，2行
    array.insert(0,lst1)
    array.insert(1,avg_lst)
    # print(array)

# 把列表array写入新的txt文件中
with open('report_new.txt', 'w') as f:
    for line in range(len(array)):
        s = str(array[line]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',',' ')+'\n'
        f.write(s)








