from risparse import risparse
from author_aggr import aggregate_authors
import json
from data_clean import clean_data_for_network_analysis
import subprocess

with open("./data/pubmed-39786682-set.txt", "r") as f:
    raw_text = f.read()

# TODO - rewrite aggregate_authors function to handle assigning the IDs to each author. 
# sort authors first then assign an ID followed by counting occurences
# export file with ID assignments and the file of combinations and counts with IDs instead of names
articles = risparse(raw_text)
res = aggregate_authors(articles)
tdt = clean_data_for_network_analysis(res)
subprocess.call(['java', '-cp', 'src/networkanalysis-1.3.0.jar', 'nl.cwts.networkanalysis.run.RunNetworkLayout', 
                 '-o', 'layout.txt', 'data/edgelist.txt'])
