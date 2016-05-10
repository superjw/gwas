line = 'gene	no_of_asso	no_of_m_trait	r_trait_lst	m_trait_lst'
line2 = line.strip().split('\t', 1)
print(line2[1])
l = line2[1].split('\t')
print(l[2])

def build_no_of_mapped_trait():
    d = {}
    with open('no_of_mapped_trait.tsv', 'r') as f:
        next(f)
        for l in f:
            lst = l.strip().split('\t')
            d[lst[0]] = lst[2]
    return d


def build_maf_dict():
    d = {}
    with open('../avg_maf_kb.tsv', 'r') as f:
        next(f)
        for l in f:
            lst = l.strip().split('\t', 2)
            d[lst[1]] = lst[2]
    return d


with open('mart_export_gid_gname_37.txt', 'r') as f:
    next(f)
    print('gene_id\tgene_name\tno_mapped_traits\tMAF/kb_EAS\tAMR\tAFR\tEUR\tSAS')
    d_m_trait = build_no_of_mapped_trait()
    d_maf = build_maf_dict()
    for l in f:
        l_lst = l.strip().split('\t')
        gene_id = l_lst[0]
        gene_name = l_lst[1]
        # new_line = l.strip() + '\t' + d_m_trait.get(gene_name) + '\t' + d_maf.get(gene_id)
        # print(l.strip())
        print(gene_id, end='\t')
        print(gene_name, end = '\t')
        print(d_m_trait.get(gene_name), end='\t')
        print(d_maf.get(gene_id))
        # print(new_line)