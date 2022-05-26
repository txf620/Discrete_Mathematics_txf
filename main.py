import pandas as pd
import itertools
import copy

def Deal_data():
    df = pd.read_csv('data4.csv')
    ans = {}
    for i, j in enumerate(list(df.columns[1:-1])):
        one_class_label = list(set(df[j].values))
        set1 = []
        for b in one_class_label:
            set1.append(set(df[df[j] == b].ID.values))
        ans[str(i)] = set1

    decision = {}
    one_class_label = list(set(df[df.columns[-1]].values))
    set1 = []
    for b in one_class_label:
        set1.append(set(df[df[df.columns[-1]] == b].ID.values))
    decision['0'] = set1
    return ans, decision


def liang_zu_guan_xi_de_deng_jia_lei(list_a, list_b):
    ans = []
    for A in list_a:
        for B in list_b:
            temp = A & B
            if temp != set():
                ans.append(temp)
    return ans


def Pos_2_attributes(C, D):
    ans = []
    for A in C:
        for B in D:
            if A.issubset(B):
                ans.append(A)
    if ans != []:
        union = ans[0]
        for a in ans:
            union = union | a
    else:
        union = set()
    return union


if __name__ == '__main__':
    set1, set2 = Deal_data()
    equivalence_class_count = len(set1)
    for level in range(2, equivalence_class_count + 2):
        for class_combination in itertools.combinations(range(equivalence_class_count), level):
            combination_id = "".join([str(o) for o in class_combination])
            previous_equivalence_class_id = combination_id[:-1]
            latter_equivalence_class_id = combination_id[-1]
            set1[combination_id] = \
                liang_zu_guan_xi_de_deng_jia_lei( \
                    set1[previous_equivalence_class_id], \
                    set1[latter_equivalence_class_id])
    #print(set1)
    for key in set1:
        if len(set1[key]) == len(
                set1["".join([str(o) for o in range(equivalence_class_count)])]):
            set_equ_flag = True
            for a in set1[key]:
                if a not in set1["".join([str(o) for o in range(equivalence_class_count)])]:
                    set_equ_flag = False
                    break
            for a in set1["".join([str(o) for o in range(equivalence_class_count)])]:
                if a not in set1[key]:
                    set_equ_flag = False
                    break
            if set_equ_flag:
                a = copy.deepcopy(key)
                a = a.replace('2','')
                print(a)
