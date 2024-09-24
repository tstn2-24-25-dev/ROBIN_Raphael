def main():
    tab = [4,8,2,10,2,1,2,9,7,6,3,5]
    print(tab)
    tab = triRapide(tab)
    print(tab)
    return tab


def triRapide(tab):
    if len(tab)>1:
        pivot = tab[0]
        indexLess = 1
        indexMore = len(tab)-1
        sorting = True
        while sorting:
            while indexLess < len(tab) and tab[indexLess]<=pivot :
                indexLess +=1
            while indexMore > 0 and tab[indexMore]>pivot :
                indexMore -=1
            if indexLess < indexMore:
                swap(tab,indexMore,indexLess)
            else:
                sorting = False
        less = triRapide(tab[1:indexLess])
        more = triRapide(tab[indexMore+1:])
        tab = less + [pivot] + more
    return tab

def swap(tab,i1,i2):
    tab[i2],tab[i1] = tab[i1],tab[i2]


if __name__ == "__main__":
    main()