import pandas
import openpyxl

FILE_NAME = "f_255643fda14249d7.txt"

ACW = []
NUM = []
ARTICLE = []
WIDTH = []
COLOR = []
NAME = []
WEIGHT = []
METERS = []
EURMETER = []
EURITOG = []
ECOSBOR = []
ROLLCOUNT = []
METERROLL = []
Dict = {"ACW": ACW, "NUM": NUM, "ARTICLE": ARTICLE, "NAME": NAME, "COLOR": COLOR, "WIDTH": WIDTH,
        "METERROLL": METERROLL, "ROLLCOUNT": ROLLCOUNT,
        "METERS": METERS, "WEIGHT": WEIGHT, "EURMETER": EURMETER, "EURITOG": EURITOG, "ECOSBOR": ECOSBOR}


def Append(a):
    NUM.append(a[0])
    ARTICLE.append(a[1])
    WIDTH.append(a[2])
    COLOR.append(a[4])
    NAME.append(a[5])
    WEIGHT.append(a[7])
    ACW.append(a[1] + "/" + a[4] + "/" + a[7])

    if "x" in a:
        ROLLCOUNT.append(a[9])
        METERROLL.append(a[11])
        METERS.append(a[12])
        EURMETER.append(a[13])
        EURITOG.append(a[15])
    else:
        ROLLCOUNT.append(None)
        METERROLL.append(None)
        METERS.append(a[9])
        EURMETER.append(a[10])
        EURITOG.append(a[12])

    if len(a) == 16 or len(a) == 19:
        ECOSBOR.append(a[-2])
    else:
        ECOSBOR.append(None)


def clear_data(new_list):
    for l in new_list:
        if l:
            while "m" in l:
                l.remove("m")
            while len(l[6]) > 1:
                l.pop(6)
            if l[-1] != "EUR":
                l.pop(-1)
            print(l, len(l))
            Append(l)


big_list = []

with open(file=FILE_NAME) as f:
    ans = []
    for line in f.readlines():
        if line[-3:].rstrip() == "kg":
            ans = line.split()
        if line.rstrip()[-3:] == "EUR":
            ans.extend(line.split())
        if line.rstrip()[-1:] == "m":
            ans.extend(line.split())
        if len(big_list) > 1 and set(big_list[-1]).issubset(ans):
            big_list.pop(-1)
        big_list.append(ans)

print(big_list)

clear_data(big_list)

df = pandas.DataFrame(Dict)
print(df)
