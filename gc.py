n=0
while n==0:
    sekans_dna = input("bir dizi girin").upper()
    CountC = sekans_dna.count("C")
    CountG = sekans_dna.count("G")
    GC = (100*(CountC + CountG)/float(len(sekans_dna)))
    n +=1

    print("GC oran : %.2f" %GC)
