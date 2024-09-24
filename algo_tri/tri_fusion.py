def main():
    tab = [4,8,2,10,2,1,2,9,7,6,3,5]
    print(tab)
    tab = triFusion(tab)
    print(tab)
    return tab

def fusionner(tab1, tab2):
    index1,index2 = 0,0
    tab = []
    while index1 < len(tab1) and index2 < len(tab2):
        if tab1[index1] < tab2[index2]:
            tab.append(tab1[index1])
            index1+=1
        else:
            tab.append(tab2[index2])
            index2+=1
    while index1 < len(tab1):
        tab.append(tab1[index1])
        index1+=1
    while index2 < len(tab2):
        tab.append(tab2[index2])
        index2+=1
    return tab


def triFusion(tab):
    if len(tab) > 1:
        tab1,tab2 = tab[0:len(tab)//2],tab[len(tab)//2:len(tab)]
        tab1,tab2 = triFusion(tab1),triFusion(tab2)
        tab = fusionner(tab1,tab2)
    return tab
        

if __name__=="__main__":
    main()