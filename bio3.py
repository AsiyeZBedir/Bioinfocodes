# DNA
dna_sequence = "ATGCGTACGTACGATGCTAGTAGCTAGTCGATGC"

# codon-aminos acid
def codon_to_amino_acid(codon):
    codon_table = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    
    return codon_table.get(codon, "Unknown")

# DNA to aminoacid
  def dna_to_protein(dna):
    protein = ""
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        amino_acid = codon_to_amino_acid(codon)
        protein += amino_acid
    return protein

# Test
if __name__ == "__main__":
    print("DNA Dizisi:", dna_sequence)
    protein_sequence = dna_to_protein(dna_sequence)
    print("Amino Asit Dizisi:", protein_sequence)
