import json
def clean_data_for_network_analysis(data):
    i = 0
    author_idx = {}
    for combo in data:
        try:
            if len(combo) == 2:
                
                if combo[0] not in author_idx:
                    author_idx[combo[0]] = i
                    i = i + 1
                if combo[1] not in author_idx:
                    author_idx[combo[1]] = i
                    i = i + 1
            #new_combos.append([author_idx[combo[0]], author_idx[combo[0][1]]])
        except IndexError:
            pass
    with open("data/author_ids.json", "w+") as f:
        f.write(json.dumps(author_idx, indent=4, ensure_ascii=False))
    with open("data/edgelist.txt", "w+") as f:
        for combo in data:
            f.write(f"{author_idx[combo[0]]}\t{author_idx[combo[1]]}\n")