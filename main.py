from datasets.dataset import get_s1, get_s2, get_s3, to_dataframe
from utils.utils import calculate_f1,calculate_true_relationship
import pandas as pd
import os


def set_weight(lst1, lst2, mean):
    ret = 0
    for i in range(len(lst1)):
        j = 1
        while j <= 5 :
            if lst1[i] > mean[i] * j and lst2[i] > mean[i] * j:
                ret += 1
            j += 1
    return ret


def main():

    if not os.path.isfile("dataframes/df_s1_s2.csv"):
        to_dataframe("s1_s2")
    if not os.path.isfile("dataframes/df_s1_s3.csv"):
        to_dataframe("s1_s3")
    if not os.path.isfile("dataframes/df_s2_s3.csv"):
        to_dataframe("s2_s3")

    df_s12 = pd.read_csv("dataframes/df_s1_s2.csv")
    print(df_s12.shape)

    df_s13 = pd.read_csv("dataframes/df_s1_s3.csv")
    print(df_s13.shape)

    df_s23 = pd.read_csv("dataframes/df_s2_s3.csv")
    print(df_s23.shape)

    dataframes = {}

    if not os.path.isfile("output/associazioni_s1_s2.txt"):
        dataframes["s1_s2"] = df_s12
    if not os.path.isfile("output/associazioni_s2_s3.txt"):
        dataframes["s2_s3"] = df_s23
    if not os.path.isfile("output/associazioni_s1_s3.txt"):
        dataframes["s1_s3"] = df_s13



    for k in dataframes.keys():
        df = dataframes.get(k)
        list_averages = df.mean()

        f = open("output/associazioni_" + k + ".txt", "a")
        #f_pesi = open("output/pesi_" + k + ".txt", "a")

        if k.rsplit('_')[0] == "s1" and k.rsplit('_')[1] == "s2":
            s_sx = get_s1()
            s_dx = get_s2()
        elif k.rsplit('_')[0] == "s1" and k.rsplit('_')[1] == "s3":
            s_sx = get_s1()
            s_dx = get_s3()
        else:
            s_sx = get_s2()
            s_dx = get_s3()

        for i in range(len(s_sx)):
            l1 = list(df.iloc[i])
            max = 0
            index = -1
            for j in range(len(s_dx)):
                l2 = list(df.iloc[len(s_sx) + j])
                weight = set_weight(l1, l2, list_averages)
                if weight > max:
                    max = weight
                    index = j
            if index != -1:
                _i = i + 1
                _index = index + 1
                print("P " + k.rsplit('_')[0][1] + " " + str(_i) + " associata a P" + k.rsplit('_')[1][1] + " " + str(
                    _index) + " con cardinalità " + str(max))
                f.write("P " + k.rsplit('_')[0][1] + " " + str(_i) + " P " + k.rsplit('_')[1][1] + " " + str(_index))
                f.write("\n")
                #f_pesi.write(str(max))
                #f_pesi.write("\n")
        f.close()

    calculate_f1("s1_s2")
    calculate_f1("s1_s3")
    calculate_f1("s2_s3")


if __name__ == '__main__':
    main()
