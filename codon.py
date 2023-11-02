def codon_frequency(dna_sequence):
    codon_dict = {}
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        codon_dict[codon] = codon_dict.get(codon, 0) + 1
    return codon_dict

# Test the function
if __name__ == "__main__":
    dna_sequence = "ATGCGTACGTACGATGCTAGTAGCTAGTCGATGC"
    codon_counts = codon_frequency(dna_sequence)
    print("Codon Frequencies:")
    for codon, count in codon_counts.items():
        print(f"{codon}: {count}")
