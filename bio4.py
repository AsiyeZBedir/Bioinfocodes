# DNA
dna_sequence1 = "ATGCGTACGTACGATGCTAGTAGCTAGTCGATGC"
dna_sequence2 = "TACGATCGTAGCTACGTACGATCGTAGCATGCTA"

# Function to calculate the melting temperature
def calculate_tm(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Sequence lengths do not match.")
    
    dna1 = dna1.upper()
    dna2 = dna2.upper()

    gc_count = 0
    at_count = 0

    for base1, base2 in zip(dna1, dna2):
        if (base1 == 'G' and base2 == 'C') or (base1 == 'C' and base2 == 'G'):
            gc_count += 1
        elif (base1 == 'A' and base2 == 'T') or (base1 == 'T' and base2 == 'A'):
            at_count += 1

    tm = (gc_count * 4) + (at_count * 2)

    return tm

# Test 
if __name__ == "__main__":
    print("DNA Sequence 1:", dna_sequence1)
    print("DNA Sequence 2:", dna_sequence2)
    tm = calculate_tm(dna_sequence1, dna_sequence2)
    print(f"Melting Temperature (Tm): {tm}°C")
