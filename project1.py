# DNA dizileri üzerinde işlemler

def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_bases = len(dna_sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

def transcribe(dna_sequence):
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence

def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna_sequence))
    return reverse_comp

# Örnek bir DNA dizisi
input_dna_sequence = "ATCGTACGTAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"

# GC içeriğini hesapla
gc_content = calculate_gc_content(input_dna_sequence)
print("GC İçeriği: {:.2f}%".format(gc_content))

# RNA transkriptini hesapla
rna_sequence = transcribe(input_dna_sequence)
print("RNA Sekansı: " + rna_sequence)

# Ters tamamlayıcıyı hesapla
reverse_comp_sequence = reverse_complement(input_dna_sequence)
print("Ters Tamamlayıcı: " + reverse_comp_sequence)
