import itertools
import collections
import json
def aggregate_authors(pubmed_set):
    author_combos = []
    authors_list = []
    # Make list all occurences of author so can be counted and used as a filter for downstream

    for article in pubmed_set:
        # Get all authors and assign them an integer ID
        authors = pubmed_set[article]["authors"]
        authors.sort()
        for author in authors:
            if author not in authors_list:
                authors_list.append(author)
    authors_list.sort()
    author_ids = {}
    for idx, name in enumerate(authors_list):
        author_ids[name] = idx

    # Iterate over articles again, but this time replacing author names with ID
    for article in pubmed_set:
        authors = pubmed_set[article]["authors"]
        authors.sort()
        authors = [author_ids[author] for author in authors]
        author_combos.append(itertools.combinations(authors, 2))
    with open("data/author_ids.txt", "w+") as f:
        for name, id in author_ids.items():
            f.write(f"{name}\t{id}\n")
    
    return collections.Counter(itertools.chain(*author_combos))