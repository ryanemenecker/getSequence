# code for pulling down uniprot sequence for predictions
# currently using this code as is in Metapredict. 
from getSequence.getsequence_exceptions import RetreiveSequenceError
import requests

def parse_input(user_input):
    '''
    function to parse
    out info that the user is trying
    to search and formats it for the uniprot
    query
    '''

    # first split the user input
    user_input_list = user_input.split(' ')

    #now make it all lowercase
    lower_input = []
    for i in user_input_list:
        lower_input.append(i.lower())

    # list of vals to strip out of the name.
    strip_list = ['maize', 'zea', 'corn', 'arath', 'arabidopsis', 'thaliana', 'mus', 'musculus', 'mouse', 'zebrafish', 'zebra', 'fish', 'danio', 'rerio', 'candida', 'albicans', 'fruit', 'fly', 'drosophila', 'melanogaster', 'plasmodium', 'falciparum', 'malaria', 'caenorhabditis', 'elegans', 'nematode', 'nematodes', 'dictyostelium', 'discoideum', 'slime', 'mold', 'dictyo', 'saccharomyces', 'cerevisiae', 'budding', 'bakers', 'schizosaccharomyces', 'pombe', 'fission', 'rattus', 'norvegicus', 'rat', 'homo', 'sapiens', 'sapien', 'human', 'humans', 'leishmania', 'infantum', 'glycine', 'max', 'soy', 'soybean', 'bean', 'oryza', 'sativa', 'rice']

    # strip out names
    non_organismal = []
    for i in lower_input:
        if i not in strip_list:
            non_organismal.append(i)

    taxid=''

    # now go through it to get out the useful components
    organism_ids = {'4577':['maize', 'zea', 'corn'], '3702':['arath', 'arabidopsis', 'thaliana'], '10090':['mus', 'musculus', 'mouse'], '7955':['zebrafish', 'zebra', 'fish', 'danio', 'rerio'], '5476':['candida', 'albicans'], '7227': ['fruit', 'fly', 'drosophila', 'melanogaster'], '5833':['plasmodium', 'falciparum', 'malaria'], '6239':['caenorhabditis', 'elegans', 'nematode', 'nematodes', 'worm'], '44689':['dictyostelium', 'discoideum', 'slime', 'mold', 'dictyo'], '559292':['saccharomyces', 'cerevisiae', 'budding', 'bakers'], '4896':['schizosaccharomyces', 'pombe', 'fission'], '10116':['rattus', 'norvegicus', 'rat'], '9606':['homo', 'sapiens', 'sapien', 'human', 'humans'], '5671':['leishmania', 'infantum'], '3847':['glycine', 'max', 'soy','soybean', 'bean'], '4530':['oryza', 'sativa', 'rice']}
    for i in organism_ids.keys():
        for usrinput in user_input_list:
            if usrinput in organism_ids[i]:
                taxid = i

    return {'taxid': taxid, 'gene_info': non_organismal}


def seq_from_uniprot(name):
    '''
    Function to get the uniprot_id of a protein from the name. 

    Parameters
    ----------
    name: string
        A string that carries the details fo the protein to search for. Can 
        contain the name of the protein as well as the name of the organims.
            ex. ARF19
                Arabidopsis ARF19
                p53
                Human p53
                Homo sapiens p53

    Returns
    -------
    top_hit : string
        Returns the amino acid sequence of the top hit on uniprot
        website.
    '''

    # first format name into a url
    # uses only reviewed
    split_name = name.split(' ')
    query_keywords = split_name[0]
    if len(split_name) == 1:
        use_url=f'https://rest.uniprot.org/uniprotkb/search?size=15&format=fasta&query={split_name[0]}%20AND%20%28reviewed%3Atrue%29'
    else:
        split_name = parse_input(name)
        if split_name['taxid']=='':
            add_vals = split_name['gene_info']
            query_keywords = split_name['gene_info']
            add_str = ''
            for i in add_vals:
                add_str += i
                add_str += '%20'
            add_str = add_str[0:len(add_str)-3]
            # one below filters for the reviewed proteins.
            use_url = f'https://rest.uniprot.org/uniprotkb/search?format=fasta&size=15&query={add_str}%20AND%20%28reviewed%3Atrue%29'
        else:
            add_vals = split_name['gene_info']
            query_keywords = split_name['gene_info']
            add_str = ''
            for i in add_vals:
                add_str += i
                add_str += '%20'
            add_str = add_str[0:len(add_str)-3]
            # one below filters for the reviewed proteins.
            use_url = f"https://rest.uniprot.org/uniprotkb/search?format=fasta&size=15&query={add_str}%20AND%20%28reviewed%3Atrue%29%20AND%20%28model_organism%3A{split_name['taxid']}%29"

    # pull top 5 fastas
    top_five = requests.get(use_url).text

    # do general query if top 5 fails
    if top_five == '':
        add_vals = name.split(' ')
        query_keywords = name.split(' ')
        add_str = ''
        for i in add_vals:
            add_str += i
            add_str += '%20'
        add_str = add_str[0:len(add_str)-3]
        # one below filters for the reviewed proteins.
        use_url = f'https://rest.uniprot.org/uniprotkb/search?format=fasta&size=15&query={add_str}%20AND%20%28reviewed%3Atrue%29'
    
    top_five = requests.get(use_url).text

 

    # header placeholder
    header = ''
    final_vals = []
    # now try to get right fasta
    fastas_split = top_five.split('>')[1:]
    
    most_matches = 0
    best_seq=''

    for header_seq in fastas_split:
        temp_seq = ''
        split_by_lines = header_seq.split('\n')
        header = split_by_lines[0].lower()
        temp_header = ''
        for i in header:
            if i == '_':
                temp_header += ' '
            else:
                temp_header += i
        header=temp_header

        if type(query_keywords) == str:

            if query_keywords in header:
                for chars in split_by_lines[1:]:
                    temp_seq+=chars
                final_vals = [header, temp_seq]
                return final_vals
        
        else:
            gene_name = header.split('gn=')[1].split(' ')[0]
            organism_name = header.split('ox=')[1].split(' ')[0]
            cur_matches=0
            for i in query_keywords:
                if i in header:
                    cur_matches += 1
                    if i == gene_name:
                        cur_matches += 2
                    if parse_input(name)['taxid'] != '':
                        if i == parse_input(name)['taxid']:
                            cur_matches += 1
            if cur_matches > most_matches:
                temp_seq=''
                most_matches = cur_matches
                for chars in split_by_lines[1:]:
                    temp_seq+=chars
                best_seq = temp_seq
                final_vals = [header, best_seq]
    
    if final_vals != []:
        return final_vals

    else:
        seq_to_use = fastas_split[0]
        split_by_lines = seq_to_use.split('\n')
        header = split_by_lines[0].lower()
        for chars in split_by_lines[1:]:
            temp_seq+=chars
        final_vals = [header, temp_seq]
        return final_vals

    raise Exception('Unable to find sequence.')



