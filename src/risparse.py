import re
from itertools import combinations
# Input file is the exported data from PubMed collection in RIS format
regex = {
    "pmid" : r"(?sm)(^PMID[\s]*[-][\s]*[\d]*)(?=[\r\n][A-Za-z]*[\s]*[-]{1}[\s]*|\Z)",
    "all_authors" : r"(?sm)(^FAU[\s]*[-]{1}[\s]*.*?)(?=[\r\n]LA[\s]*[-]{1}[\s]*|\Z)",
    "author" : r"(?sm)(^FAU[\s]*[-]{1}[\s]*.*?)(?=[\r\n]FAU[\s]*[-]{1}[\s]*|\Z)",
    "title" : r"(?sm)(^TI[\s]*[-]{1}[\s]*.*?)(?=[\r\n][a-zA-Z]*[\s]*[-]{1}[\s]*|\Z)",
    "journal" : r"(?sm)(^JT[\s]*[-]{1}[\s]*.*?)(?=[\r\n][a-zA-Z]*[\s]*[-]{1}[\s]*|\Z)"
}
def risparse(entry_set):
    # Parse Title
    pmid_entries = entry_set.split("\n\n")
    articles = {}
    for pmid_entry in pmid_entries:
        try:
            title = re.sub(r"TI[\s]*[-]{1}[\s]*", "", " ".join(re.search(regex["title"], pmid_entry).group(0).split()))
            pmid = int(re.sub(r"PMID[\s]*[-]{1}[\s]*", "", re.search(regex["pmid"], pmid_entry).group(0)))


            # Parse Journal Name
            j = re.search(regex["journal"], pmid_entry).group(0)
            journal = re.sub(r"JT[\s]*[-]{1}[\s]*", "", j)

            # Parse Authors
            all_authors = re.search(regex["all_authors"], pmid_entry).group(0)

            author_list = re.findall(regex["author"], all_authors)
            authors = []
            for a in author_list:
                author_record = re.search(r"(?sm)(^FAU[\s]*[-]{1}[\s]*.*?)(?=[\r\n]LA[\s]*[-]{1}[\s]*|\Z)", a)
                fau = re.search(r"(?sm)(^FAU[\s]*[-]{1}[\s]*.*?)(?=[\r\n]AU[\s]*[-]{1}[\s]*|\Z)", author_record.group(0))
                
                split_name = re.sub(r"^FAU[\s]*[-]{1}[\s]*", "", fau.group(0)).split(", ")
                lastname = split_name[0]
                try:
                    first_middle_name = split_name[1].split()
                    firstname = first_middle_name[0]
                    try:
                        middlename = first_middle_name[1]
                    except IndexError:
                        middlename = ""
                except IndexError:
                    firstname = ""
                    middlename = ""
                
                authors.append(f"{lastname}, {firstname} {middlename}".strip().lower())


            articles[pmid] = {
                "title": title,
                "journal": journal,
                "authors": authors
                }
        except AttributeError as e:
            continue

    return articles



