def main():
    tab = [4,8,2,10,1,9,7,6,3,5]
    triInsertion(tab)
    print(tab)

def triInsertion(tab):
    if len(tab)>1:
        for pivot in range(1,len(tab)):
            # print(tab[:pivot])
            inserted = False
            index = pivot
            while not inserted and index > 0 :
                if tab[index]<tab[index-1]:
                    tab[index], tab[index-1] = tab[index-1], tab[index]
                    # print(tab)
                index -= 1
            


    return tab


if __name__ == "__main__":
    main()