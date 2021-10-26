
import pandas as pd
import statistics


def question5to13(f_, index_, list_, summarize_):
    avarage = 0
    num = 0
    min_ = 100000  # just setting initial value
    max_ = -100000  # just setting initial value
    l = []
    country_ = 0
    i = 0
    for i in range(len(list_) - 1):
        temp = list_[i][2]
        if not pd.isna(temp):
            if not pd.isna(list_[i][index_]):
                avarage = avarage + list_[i][index_]
                num = num + 1
                l.append(list_[i][index_])
                if (not pd.isna(list_[i + 1][index_])):
                    if (min_ > list_[i + 1][index_]):
                        min_ = list_[i + 1][index_]
                    if (max_ < list_[i + 1][index_]):
                        max_ = list_[i + 1][index_]
                else:
                    if (not pd.isna(list_[i][index_])):
                        if (min_ > list_[i][index_]):
                            min_ = list_[i][index_]
                        if (max_ < list_[i][index_]):
                            max_ = list_[i][index_]
            if (temp != list_[i + 1][2]):
                f_.write(temp + " ")
                var = 0
                if (len(l) > 1):
                    var = statistics.variance(l)
                if (num != 0):
                    avarage = avarage / num
                if (max_ == -100000 and min_ == 100000):
                    f_.write("               " + "\n")
                    summarize_[country_].append(" ")
                    summarize_[country_].append(" ")
                    summarize_[country_].append(" ")
                    summarize_[country_].append(" ")
                else:
                    f_.write(str(min_) + " , " + str(max_) + " , " + str(avarage) + " , " + str(var) + "\n")
                    summarize_[country_].append(str(min_))
                    summarize_[country_].append(str(max_))
                    summarize_[country_].append(str(avarage))
                    summarize_[country_].append(str(var))
                country_ = country_ + 1
                avarage = 0
                num = 0
                min_ = 100000
                max_ = -100000
                l.clear()
    temp = list_[i + 1][2]
    if (not pd.isna(temp)):
        f_.write(temp + " ")
        var = 0
        if (len(l) > 1):
            var = statistics.variance(l)
        if (num != 0):
            avarage = avarage / num
        if (max_ == -100000 and min_ == 100000):
            f_.write("               " + "\n")
            summarize_[country_].append(" ")
            summarize_[country_].append(" ")
            summarize_[country_].append(" ")
            summarize_[country_].append(" ")
        else:
            f_.write(str(min_) + " , " + str(max_) + " , " + str(avarage) + " , " + str(var) + "\n")
            summarize_[country_].append(str(min_))
            summarize_[country_].append(str(max_))
            summarize_[country_].append(str(avarage))
            summarize_[country_].append(str(var))


def question14_15(f, index, list, summarize):
    res = 0
    check = 0
    country = 0
    i = 0
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (not pd.isna(list[i][index])):
                res = list[i][index]
                check = 1
            if (temp != list[i + 1][2]):
                if (check == 1):
                    f.write(temp + " , " + str(res) + "\n")
                    summarize[country].append(str(res))
                else:
                    f.write(temp + "               " + "\n")
                    summarize[country].append(" ")
                country = country + 1
                res = 0
                check = 0
    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        f.write(temp + " , " + str(res) + "\n")
        summarize[country].append(str(res))



if __name__ == '__main__':
    df = pd.read_excel("owid-covid-data.xlsx", index_col=None)
    f = open("output.txt", "w")
    i = 0
    summarize = []
    only_country = pd.notnull(df["continent"])
    list = df[only_country].values.tolist()

    country = 0
    f.write("\nQuestion 1 \n")
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (temp != list[i + 1][2]):
                # f.write(temp + "\n")
                summarize.append([temp])
                country = country + 1
    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        country = country + 1
        summarize.append([temp])
        # f.write(temp + "\n")
    f.write(str(country) + "\n")



    # question2
    f.write("\nQuestion 2 \n")
    min = list[0][3]
    index = 0
    for i in range(len(list) - 1):
        if (not pd.isna(list[i + 1][3])):
            if (min > list[i + 1][3]):
                min = list[i + 1][3]
                index = i + 1
    for i in range(len(list)):
        if (not pd.isna(list[i][3])):
            if (min == list[i][3]):
                f.write(list[i][3] + " , " + list[i][2] + "\n")
    # question 3
    f.write("\nQuestion 3 \n")
    country = 0
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (temp != list[i + 1][2]):
                f.write(temp + " , ")
                if (not pd.isna(list[i][4])):
                    f.write(str(list[i][4]) + "\n")
                    summarize[country].append(str(list[i][4]))
                else:
                    f.write(" \n")
                    summarize[country].append(" ")
                country = country + 1
    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        f.write(temp + " , ")
        if (not pd.isna(list[i + 1][4])):
            f.write(str(list[i + 1][4]) + "\n")
            summarize[country].append(str(list[i][4]))
        else:
            f.write(" \n")
            summarize[country].append(" ")

    f.write("\n")

    # question 4
    f.write("\nQuestion 4 \n")
    country = 0
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (temp != list[i + 1][2]):
                f.write(temp + " , ")
                if (not pd.isna(list[i][7])):
                    f.write(str(list[i][7]) + "\n")
                    summarize[country].append(str(list[i][7]))
                else:
                    f.write(" \n")
                    summarize[country].append(" ")
                country = country + 1
    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        f.write(temp + " , ")
        if (not pd.isna(list[i + 1][7])):
            f.write(str(list[i + 1][7]) + "\n")
            summarize[country].append(str(list[i][7]))
        else:
            f.write(" \n")
            summarize[country].append(" ")

    f.write("\nQuestion 5\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 16, list, summarize)
    f.write("\nQuestion 6\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 17, list, summarize)
    f.write("\nQuestion 7\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 19, list, summarize)
    f.write("\nQuestion 8\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 21, list, summarize)
    f.write("\nQuestion 9\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 23, list, summarize)
    f.write("\nQuestion 10\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 25, list, summarize)

    f.write("\nQuestion 11\n")
    if (not pd.isna(list[0][26])):
        max = list[0][26]
    else:
        max = -100000
    country = 0
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (not pd.isna(list[i][26])):
                if (not pd.isna(list[i + 1][26])):
                    if (max < list[i + 1][26]):
                        max = list[i + 1][26]
                else:
                    if (not pd.isna(list[i][26])):
                        if (max < list[i][26]):
                            max = list[i][26]

            if (temp != list[i + 1][2]):
                f.write(temp + " , ")
                if (max == -100000):
                    f.write("       " + "\n")
                    summarize[country].append(" ")
                else:
                    f.write(str(max) + "\n")
                    summarize[country].append(str(max))
                country = country + 1
                max = -100000
    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        f.write(temp + " , ")
        if (max != -100000):
            f.write(str(max) + "\n")
            summarize[country].append(str(max))
        else:
            f.write(" \n")
            summarize[country].append(" ")

    f.write("\n")

    f.write("\nQuestion 12\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 31, list, summarize)
    f.write("\nQuestion 13\n")
    f.write("Country , minimum , maximum , average , variation\n")
    question5to13(f, 32, list, summarize)
    f.write("\nQuestion 14\n")
    question14_15(f, 35, list, summarize)
    f.write("\nQuestion 15\n")
    question14_15(f, 36, list, summarize)
    f.write("\nQuestion 16\n")
    question14_15(f, 34, list, summarize)

    f.write("\nQuestion 17\n")
    f.write(
        "                            Country ,   population , median age , # of people aged 65 older , # of people aged 70 older , "
        "economic performance , death rates due to heart disease , diabetes prevalence , # of female smokers , # of male smokers , "
        "handwashing facilities , hospital beds per thousand people , life expectancy , human development index.\n")
    country = 0
    for i in range(len(list) - 1):
        temp = list[i][2]
        if (not pd.isna(temp)):
            if (temp != list[i + 1][2]):
                f.write("%35s , " % temp)
                if (not pd.isna(list[i][44])):
                    f.write("%12s , " % str(list[i][44]))
                    summarize[country].append(str(list[i][44]))
                else:
                    f.write("%12s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][46])):
                    f.write("%10s , " % str(list[i][46]))
                    summarize[country].append(str(list[i][46]))
                else:
                    f.write("%10s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][47])):
                    f.write("%25s , " % str(list[i][47]))
                    summarize[country].append(str(list[i][47]))
                else:
                    f.write("%25s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][48])):
                    f.write("%25s , " % str(list[i][48]))
                    summarize[country].append(str(list[i][48]))
                else:
                    f.write("%25s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][49])):
                    f.write("%20s , " % str(list[i][49]))
                    summarize[country].append(str(list[i][49]))
                else:
                    f.write("%20s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][51])):
                    f.write("%32s , " % str(list[i][51]))
                    summarize[country].append(str(list[i][51]))
                else:
                    f.write("%32s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][52])):
                    f.write("%19s , " % str(list[i][52]))
                    summarize[country].append(str(list[i][52]))
                else:
                    f.write("%19s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][53])):
                    f.write("%19s , " % str(list[i][53]))
                    summarize[country].append(str(list[i][53]))
                else:
                    f.write("%19s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][54])):
                    f.write("%17s , " % str(list[i][54]))
                    summarize[country].append(str(list[i][54]))
                else:
                    f.write("%17s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][55])):
                    f.write("%22s , " % str(list[i][55]))
                    summarize[country].append(str(list[i][55]))
                else:
                    f.write("%22s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][56])):
                    f.write("%33s , " % str(list[i][56]))
                    summarize[country].append(str(list[i][56]))
                else:
                    f.write("%33s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][57])):
                    f.write("%15s , " % str(list[i][57]))
                    summarize[country].append(str(list[i][57]))
                else:
                    f.write("%15s , " % " ")
                    summarize[country].append(" ")
                if (not pd.isna(list[i][58])):
                    f.write("%23s." % str(list[i][58]))
                    summarize[country].append(str(list[i][58]))
                else:
                    f.write("%23s " % " ")
                    summarize[country].append(" ")
                f.write("\n")
                country = country + 1

    temp = list[i + 1][2]
    if (not pd.isna(temp)):
        f.write("%35s , " % temp)
        if (not pd.isna(list[i][44])):
            f.write("%12s , " % str(list[i][44]))
            summarize[country].append(str(list[i][44]))
        else:
            f.write("%12s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][46])):
            f.write("%10s , " % str(list[i][46]))
            summarize[country].append(str(list[i][46]))
        else:
            f.write("%10s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][47])):
            f.write("%25s , " % str(list[i][47]))
            summarize[country].append(str(list[i][47]))
        else:
            f.write("%25s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][48])):
            f.write("%25s , " % str(list[i][48]))
            summarize[country].append(str(list[i][48]))
        else:
            f.write("%25s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][49])):
            f.write("%20s , " % str(list[i][49]))
            summarize[country].append(str(list[i][49]))
        else:
            f.write("%20s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][51])):
            f.write("%32s , " % str(list[i][51]))
            summarize[country].append(str(list[i][51]))
        else:
            f.write("%32s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][52])):
            f.write("%19s , " % str(list[i][52]))
            summarize[country].append(str(list[i][52]))
        else:
            f.write("%19s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][53])):
            f.write("%19s , " % str(list[i][53]))
            summarize[country].append(str(list[i][53]))
        else:
            f.write("%19s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][54])):
            f.write("%17s , " % str(list[i][54]))
            summarize[country].append(str(list[i][54]))
        else:
            f.write("%17s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][55])):
            f.write("%22s , " % str(list[i][55]))
            summarize[country].append(str(list[i][55]))
        else:
            f.write("%22s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][56])):
            f.write("%33s , " % str(list[i][56]))
            summarize[country].append(str(list[i][56]))
        else:
            f.write("%33s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][57])):
            f.write("%15s , " % str(list[i][57]))
            summarize[country].append(str(list[i][57]))
        else:
            f.write("%15s , " % " ")
            summarize[country].append(" ")
        if (not pd.isna(list[i][58])):
            f.write("%23s." % str(list[i][58]))
            summarize[country].append(str(list[i][58]))
        else:
            f.write("%23s " % " ")
            summarize[country].append(" ")
        f.write("\n")

    f.write("\nQuestion 18\n")
    f.write("                            Country ,                       q#3 ,                       q#4 ,                   q#5 min , ")
    f.write("                  q#5 max ,                   q#5 avg ,                   q#5 var , ")
    f.write("                  q#6 min ,                   q#6 max ,                   q#6 avg ,                   q#6 var , ")
    f.write("                  q#7 min ,                   q#7 max ,                   q#7 avg ,                   q#7 var , ")
    f.write("                  q#8 min ,                   q#8 max ,                   q#8 avg , ")
    f.write("                  q#8 var ,                   q#9 min ,                   q#9 max ,                   q#9 avg ,")
    f.write("                   q#9 var , ")
    f.write("                 q#10 min ,                  q#10 max ,                  q#10 avg ,                  q#10 var , ")
    f.write("                     q#11 , ")
    f.write("                 q#12 min ,                  q#12 max ,                  q#12 avg ,                  q#12 var , ")
    f.write("                 q#13 min ,                  q#13 max ,                  q#13 avg ,                  q#13 var , ")
    f.write("                      q#14 ,                      q#15 ,                      q#16 , ")
    f.write("                 q#17 pop ,                  q#17 med ,                q#17 age65 ,                q#17 age70 ,                  q#17 eco ,                q#17 heart ,                 q#17 diab , ")
    f.write("            q#17 m_smoker , ")
    f.write("            q#17 f_smoker ,                 q#17 hand ,                 q#17 hosp ,                 q#17 life ,                q#17 human\n")
    i = 0
    j = 0
    for i in range(len(summarize)):
        for j in range(len(summarize[i])):
            if (j == 0):
                f.write("%35s , " % summarize[i][j])
            elif (j == len(summarize[i]) - 1):
                f.write("%25s " % summarize[i][j])
            else:
                f.write("%25s , " % summarize[i][j])
        f.write("\n")


