# DNA dizileri arasındaki uzaklık hesaplama

from Bio.Seq import Seq
from scipy.spatial import distance

# İki örnek DNA dizisi
sequence1 = Seq("ATCGTACGTAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG")
sequence2 = Seq("TTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAC")

# DNA dizilerini stringe dönüştür
seq1_str = str(sequence1)
seq2_str = str(sequence2)

# DNA dizilerini vektörlere dönüştür
seq1_vector = [ord(base) for base in seq1_str]
seq2_vector = [ord(base) for base in seq2_str]

# Uzaklığı hesapla
dna_distance = distance.hamming(seq1_vector, seq2_vector)

print("DNA Dizileri Arasındaki Uzaklık:", dna_distance)
