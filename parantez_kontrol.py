
"""
cümlelerde () , [] , {} açma ve kapatma girişi kontrolü

"""



def kapali_mi(S):
    ayrac = list()
    acik_ayrac = set({"(","{","["})
    kapali_ayrac = set({")","}","]"})
    acik_kapali = dict({"{": "}", "[": "]", "(": ")"})


    for i in range(len(S)):
        if S[i] in acik_ayrac:
            ayrac.append(S[i])

        elif S[i] in kapali_ayrac:
            if len(ayrac) == 0 or acik_kapali[ayrac.pop()] != S[i]:
                return False

    return len(ayrac) == 0


def main():
    s= input("enter : ")
    if kapali_mi(s):
        print(s,"kapali")
    else:
        print("kapalı değil")


main()



























