from mygene import MyGeneInfo

# Define your input list of mouse gene symbols
gene_symbols = [
    "A430089I19Rik",
    "A430089I19Rik",
    "A430089I19Rik",
    "Gm6902",
    "Gm10424",
    "Gm3147",
    "A430089I19Rik",
    "Gm12794",
    "Gm16429",
    "Gm7971",
    "Gm12800",
    "Gm6351",
    "Gm7982",
    "BC061212",
    "Gm6502",
    "Gm7647",
    "Gm6346",
    "Gm6523",
    "Gm7942",
    "Gm6348",
    "Gm6502",
    "Gm6468"
]

# Initialize the MyGeneInfo object
mg = MyGeneInfo()

# Initialize a list to store results
results = []

# Loop through each gene symbol
for symbol in gene_symbols:
    # Query MyGene.info for human homologs
    response = mg.query(symbol, fields="symbol,entrezgene", species="human", size=1)

    if response and "hits" in response and len(response["hits"]) > 0:
        hit = response["hits"][0]
        human_gene_symbol = hit.get("symbol", "Not available")
        entrez_id = hit.get("entrezgene", "Not available")

        results.append((symbol, human_gene_symbol, entrez_id))
    else:
        results.append((symbol, "No human homolog found", "Not available"))

# Print the results
for result in results:
    print("Mouse Gene Symbol:", result[0])
    print("Human Gene Symbol:", result[1])
    print("Human Entrez ID:", result[2])
    print("=" * 50)
