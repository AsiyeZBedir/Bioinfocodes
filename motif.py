# DNA dizisi üzerinde motif arama

import re

# Örnek bir DNA dizisi
dna_sequence = "ATCGTACGTAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"

# Aranacak motif
motif = "CTAG"

# Motifin pozisyonlarını bul
motif_positions = [match.start() for match in re.finditer(motif, dna_sequence)]

if motif_positions:
    print("Motif '{}' DNA dizisinde şu pozisyonlarda bulunuyor: {}".format(motif, motif_positions))
else:
    print("Motif '{}' DNA dizisinde bulunamadı.".format(motif))
