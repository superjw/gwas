# with open('/home/j/Desktop/gwas_catalog/gwas_catalog_v1.0.1-associations_e84_r2016-04-24.tsv', 'r') as f:
#     # header = next(f)
#     # lst = header.split('\t')
#     # print(type(lst))
#     # print(lst)
#     # i = 0
#     # for e in lst:
#     #     print('[' + str(i) + ']' + e)
#     #     i += 1
#     # print('done!')
#
#
#     for line in f:
#         sub_line = line.strip().split('\t')
#         sub_line_string = sub_line[2] + '\t' + sub_line[4] \
#                           + '\t' + sub_line[6] + '\t' + sub_line[7] \
#                           + '\t' + sub_line[8] + '\t' + sub_line[9] \
#                           + '\t' + sub_line[13] + '\t' + sub_line[14] \
#                           + '\t' + sub_line[17]
#         if 'foxo3' in sub_line_string:
#             print(line.strip())
#         elif 'FOXO3' in sub_line_string:
#             print(line.strip())
import re


def build_all_gene_list(mart_export_file_name):
    """
    37 biomart export
    :param mart_export_file:GRCh37 export file name
    :return:list of all genes based on GRCh37 assembly
    """
    with open(mart_export_file_name) as f:
        gene_list = []
        next(f)
        for line in f:
            gene_name = line.strip().split('\t')[1]
            # gene_id = line.strip().split('\t')[0]
            gene_list.append(gene_name)
        return gene_list


def search_file(gene_name, association_file_obj):
    """
    return match results of gene searching
    :param gene_name:
    :param association_file_obj: GWAS-Catalog association file
    :return: number of associations, a list of reported traits
    """
    # print(next(association_file_obj)) # ignore header line
    reported_traits_lst = []
    i = 0   # add a counter for number of associations
    for line in association_file_obj:
        sub_line = line.strip().split('\t')


        match_check_string = sub_line[2] + '\t' + sub_line[4] \
                          + '\t' + sub_line[6] + '\t' + sub_line[7] \
                          + '\t' + sub_line[8] + '\t' + sub_line[9] \
                          + '\t' + sub_line[13] + '\t' + sub_line[14] \
                          + '\t' + sub_line[17]
        # files need to be checked based on the GWAS-Catalog team communication email
        # print(match_check_string)
        if gene_name.lower() in match_check_string.lower():
            # print(line)
            reported_traits = sub_line[7]
            reported_traits_lst.append(reported_traits)
            # print('========')
            # print(reported_traits)
            i += 1  # counter add 1 when there is a match
            # return reported traits if there is a match in the line
        # else:
        #     pass
    reported_traits_lst = list(set(reported_traits_lst))
    return reported_traits_lst, i


def efo_mapping_dict(mapping_file_name):
    with open(mapping_file_name, 'r') as f:
        next(f)
        dict = {}
        # expr = r'\s*\b(\S+)\b\t\s*\b(\S+)\b\t\S+\t\S+\n'
        expr = r'^\s*(.+)\s*\t\s*(.+)\s*\t.+\t.+\t.+$'
        i = 0
        for line in f:
            # print(line)
            m = re.search(expr, line)
            # print(m)
            dict[m.group(1)] = m.group(2)
            i += 1
            # print(i)
        return dict


def r_to_m_trait(reported_trait_lst, mapping_dict):
    m_trait_lst = []
    for r_trait in reported_trait_lst:
        m_trait_lst.append(mapping_dict.get(r_trait))
        # print(mapping_dict.get(r_trait))
    m_trait_lst = list(set(m_trait_lst))
    return m_trait_lst, len(m_trait_lst)


def main():
    gene_lst = build_all_gene_list('mart_export_gid_gname_37.txt')
    asso_file_obj = open('/home/j/Desktop/gwas/gwas_catalog_v1.0.1-associations_e84_r2016-04-24.tsv', 'r')
    map_dict = efo_mapping_dict('gwas_catalog_trait-mappings_r2016-04-24.tsv')
    # for k, v in map_dict.items():
    # #     print(k + ' : ' + v)
    r_trait_lst, no_of_asso = search_file('PRUNEP1', asso_file_obj)
    print(r_trait_lst)
    reported_trait = ','.join(r_trait_lst)
    print(reported_trait)
    print('====')
    m_trait_lst, no_of_r_trait = r_to_m_trait(r_trait_lst, map_dict)
    print(m_trait_lst)
    mapped_trait = ','.join(m_trait_lst)
    print(no_of_r_trait)
    print(mapped_trait)
    #
    # for r in r_trait_lst:
    #     # print(r)
    #     m_trait_lst, no_of_r_trait = r_to_m_trait(r_trait_lst, map_dict)
    #     print(r_trait_lst)
    #     m_trait_lst, no_of_r_trait = r_to_m_trait(r_trait_lst, map_dict)
    #     print(m_trait_lst)
    #

    # for gene in ['FOXO3', 'APOE', 'BCL3']:
    #     print(gene)   # work
    #     r_trait_lst, no_of_asso = search_file(gene, asso_file_obj)
    #     print(r_trait_lst)
    #     print(no_of_asso)
    #     m_trait_lst, no_of_r_trait = r_to_m_trait(r_trait_lst, map_dict)
    #     print(m_trait_lst)
    #     print(no_of_r_trait)

        # print(r_trait_lst)
        # for r in r_trait_lst:
        #     print(r)
        # m_trait_lst, no_of_r_trait = r_to_m_trait(r_trait_lst, map_dict)
        # print(gene + '\t' + str(no_of_r_trait))
    asso_file_obj.close()


main()
# print(gene_lst)
# print(len(gene_lst))




# str = '2009-09-28	18403759	Ober C	2008-04-09	N Engl J Med	www.ncbi.nlm.nih.gov/pubmed/18403759	Effect of variation in CHI3L1 on serum YKL-40 level, risk of asthma, and lung function.	YKL-40 levels	632 Hutterite individuals	443 European ancestry cases, 491 European ancestry controls, 206 European ancestry individuals	1q32.1	1	203186754	CHI3L1	CHI3L1			1116			rs4950928-G	rs4950928		4950928	upstream_gene_variant	0	0.29	1.0E-13	13.0		0.3	[NR]ng/ml decrease	Affymetrix [290325]	N	YKL40 measurement	http://www.ebi.ac.uk/efo/EFO_0004869
# '
#
# expr = expr = r'^\s*\d\S+\t\d+\t(.+)\b\s*\t\s*\b(.+)\b\s*\t.+\t.+\t.+'
# m = re.search(expr, str)
# print(m.group(1))
# print(m.group(2))



# dict = efo_mapping_dict('gwas_catalog_trait-mappings_r2016-04-24.tsv')
# for k,v in dict.items():
#     print(k + ' : ' + v)

# in_gene = 'foxo3'
# with open('/home/j/Desktop/gwas/gwas_catalog_v1.0.1-associations_e84_r2016-04-24.tsv', 'r') as f:
#     lst, counter = search_file(in_gene, f)
#     for i in lst:
#         print(i)
#     # print('========')
#     print(str(counter))
#     print('job done!')