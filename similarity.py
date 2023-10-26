# DNA dizileri benzerlik skoru ve hizalama

from Bio import pairwise2
from Bio.Seq import Seq

# İki örnek DNA dizisi
sequence1 = Seq("ATCGTACGTAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG")
sequence2 = Seq("ATCGTACGTAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG")

# Benzerlik skorunu hesapla
alignments = pairwise2.align.globalxx(sequence1, sequence2, one_alignment_only=True)
best_alignment = alignments[0]
score = best_alignment[2]

print("Benzerlik Skoru:", score)

# Hizalama sonuçlarını göster
print("Hizalama 1:", best_alignment[0])
print("Hizalama 2:", best_alignment[1])
