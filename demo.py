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

def search_file(gene_name, association_file_obj):
    """
    return match results of gene searching
    :param gene_name:
    :param association_file_obj: GWAS-Catalog association file
    :return: number of associations, a list of reported traits
    """
    print(next(association_file_obj)) # ignore header line
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
    return reported_traits_lst, i

in_gene = 'foxo3'
with open('/home/j/Desktop/gwas_catalog/gwas_catalog_v1.0.1-associations_e84_r2016-04-24.tsv', 'r') as f:
    lst, counter = search_file(in_gene, f)
    for i in lst:
        print(i)
    print('========')
    print(str(counter))
    print('job done!')