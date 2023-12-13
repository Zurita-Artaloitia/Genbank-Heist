Genbank-Heist is a small program written in Python. It extracts the genomic context of a certain gene from a Genbank file.

The output will still be a Genbank file, but with the defined set of genes.
It allows the user to define the number of upstream or downstream genes it prints, relative to the target ID.
The ID can be either the LOCUS_TAG or the PROTEIN ID.
The output is named: ("LOCUS_TAG or PROTEIN ID" + .gbk). It will be saved in the same directory as the input file.
You just need to run the program with Python3, all the user input is introduced as it runs.

Zurita-Artaloitia
