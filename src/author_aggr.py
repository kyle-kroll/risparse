import itertools
import collections
def aggregate_authors(pubmed_set):
    author_combos = []
    authors_list = []
    for article in pubmed_set:
        authors = pubmed_set[article]["authors"]
        authors_list.append(authors)
        authors.sort()
        author_combos.append(list(itertools.combinations(authors, 2)))
    return collections.Counter(itertools.chain(*authors_list)), collections.Counter(itertools.chain(*author_combos))
    