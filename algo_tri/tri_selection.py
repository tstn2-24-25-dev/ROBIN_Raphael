def main():
    l = [5,4,1,6,3,2]
    print(f"unsorted: {l}")
    sortedL = tri_selection(l)
    print(f"sorted:   {sortedL}")

# def selectSort(l):
#     if len(l)>1:
#         for minIndex in range(0,len(l)-1):
#             for i in range(minIndex+1,len(l)):
#                 if l[i]<l[minIndex]:
#                     l[i],l[minIndex] = l[minIndex],l[i]
#     return l


def indiceMin(tab, j):
    indice_Min = j
    for indice in range (j+1,len(tab)):
        if tab[indice]<tab[indice_Min]:
            indice_Min = indice
    return indice_Min

def tri_selection(tab):
    for indice in range (len(tab)):
        indice_Min = indiceMin(tab,indice)
        tab[indice], tab[indice_Min] = tab[indice_Min], tab[indice]
    return tab

if __name__=="__main__":
    main()