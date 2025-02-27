from risparse import risparse
from author_aggr import aggregate_authors
import json

with open("./data/pubmed-39786682-set.txt", "r") as f:
    raw_text = f.read()


#for article in pmid_entries:

articles = risparse(raw_text)
count, res = aggregate_authors(articles)
res = dict((' | '.join(k), v) for k,v in dict(res.most_common()).items())
count = dict(count.most_common())
with open("data/count.json", "w+") as f:
    f.write(json.dumps(count, indent=4, ensure_ascii=False))
with open("data/res.json", "w+") as f:
    f.write(json.dumps(res, indent=4, ensure_ascii=False))
#print(json.dumps(articles, indent=4))