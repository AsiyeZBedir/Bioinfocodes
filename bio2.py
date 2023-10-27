# DNA 
dna_sequence = "ATGCGTACGTACGATGCTAGTAGCTAGTCGATGC"

# find genes
def find_genes(dna):
    genes = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    i = 0

    while i < len(dna):
        if dna[i:i+3] == start_codon:
            for j in range(i+3, len(dna), 3):
                codon = dna[j:j+3]
                if codon in stop_codons:
                    genes.append((i, j+3))
                    i = j+3
                    break
        else:
            i += 1

    return genes

# Test 
if __name__ == "__main__":
    print("DNA Dizisi:", dna_sequence)
    genes = find_genes(dna_sequence)
    if genes:
        for gene_start, gene_end in genes:
            print(f"Gen Başlangıç: {gene_start}, Gen Bitiş: {gene_end}")
    else:
        print("Herhangi bir gen bulunamadı.")
