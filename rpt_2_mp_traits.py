

def trait_mapping(r_trait):
    with open('gwas_catalog_trait-mappings_r2016-04-24.tsv', 'r') as f:
        next(f)
        # lst = []
        for line in f:
            sp_line = line.strip().split('\t')
            if r_trait.lower() == sp_line[1].lower():
                print(line.strip())

                # lst.append(sp_line[1])
                # return lst

# outfile = open('tmp', 'w')
with open('foxo3_mapped_traits.txt', 'r') as f:
    for line in f:
        l = line.strip()
        trait_mapping(l)

    # print('job done!')



