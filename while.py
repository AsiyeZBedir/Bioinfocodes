List = [("AUG,UAG"),("CCU","GGA"),
        ("GUA","CAU"),("UAA","STOP")]
kodon = "GUA"
sayi=0
"İlk sradaki kodona eşleşinceye kadar listede arayacak bulunca antikodonunu yazdıracak"
while kodon!=List[sayi][0]:
    sayi+=1
    Antikodon=list[sayi][1]
    print(Antikodon)
