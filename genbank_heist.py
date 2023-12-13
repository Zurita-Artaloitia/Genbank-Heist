#VARIABLES DEFINITION
inputfile0 = input('Your Genbank file location PATH:')
query = input('Locus_tag or Protein ID:')
upgenes = int(input('Number of UPstream genes:'))
downgenes = int(input('Number of DOWNstream genes:'))
filename = "%s.gbk" % query
#INDEX SET
with open (inputfile0 , 'r') as input_genbankfile:
    input_genbankfile2 = input_genbankfile.read()
    splited = input_genbankfile2.split('     gene            ')
    for i, line in enumerate(splited):
        if query in line:
            target1 = i
            break
#RESULTS
    if target1 is not None:
        startindex = max(0, target1 - upgenes)
        endindex = min(len(splited), target1 + downgenes + 1)

        results = '     gene            '.join(splited[startindex:endindex])
        print (f'{splited[0]}     gene            {results}\n//', file=open(filename, 'w'))
    else:
        print (f'Locus tag or Protein ID: {query} not found')