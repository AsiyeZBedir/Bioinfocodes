dna_sequence = "ATCGATCGTAGCTACGTACGATCGTAGCATGCTACGTA"

# count
def count_base_pairs(dna):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in dna:
        if base in base_counts:
            base_counts[base] += 1
    return base_counts

# GC ratio
def calculate_gc_ratio(dna):
    gc_count = dna.count('G') + dna.count('C')
    total_count = len(dna)
    gc_ratio = gc_count / total_count
    return gc_ratio

# reverse
def reverse_sequence(dna):
    return dna[::-1]

# Test
if __name__ == "__main__":
    print("DNA Sequence:", dna_sequence)
    print("Base Pairs:", count_base_pairs(dna_sequence))
    print("GC Ratio:", calculate_gc_ratio(dna_sequence))
    print("Reverse DNA Sequence:", reverse_sequence(dna_sequence))
