def main():
    tab = [4,8,2,10,1,9,7,6,3,5]
    triInsertion(tab)
    print (tab)

def triInsertion(tab):
    if len(tab)>1:
        for i in range(1,len(tab)):
            index = i
            while tab[index]<tab[index-1] and index > 0 :
                tab[index], tab[index-1] = tab[index-1], tab[index]
                index -= 1
    return tab

if __name__ == "__main__":
    main()