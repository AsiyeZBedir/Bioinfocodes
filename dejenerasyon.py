protein_sekans = input("protein sekans:").upper()
amino_asit_sayisi = {"A":4,"C":2,"D":2,"E":2,"F:2",
                     "G":4,"P":4,"Q":5}
segment_valur =[]
segment_sekans =[]
segment = protein_sekans[:15]
a=0
while len(segment)==15
dejenerasyon=0
for x in segment:
    "sözlükle amino asitin değeri yoksa 4.8 alınsın diye x,4.8"
    dejenerasyon += aminoasit_kodon_sayisi.get(c,4.8)
    segment_valur.append(dejenerasyon)
    segment_sekans.append(segment)
    a+= 1 
    segment = protein_sekans[a:a+15]
    
print(segment_sekans[segment_valur.index(min(segment_valur))])
