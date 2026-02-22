
import json
from collections import defaultdict

def analyze_heap(path):
    with open(path) as f:
        data=json.load(f)

    nodes=data["nodes"]
    strings=data["strings"]
    meta=data["snapshot"]["meta"]

    fields=meta["node_fields"]
    types=meta["node_types"][0]

    t_i=fields.index("type")
    n_i=fields.index("name")
    s_i=fields.index("self_size")

    step=len(fields)
    usage=defaultdict(int)

    for i in range(0,len(nodes),step):
        t=types[nodes[i+t_i]]
        n=strings[nodes[i+n_i]]
        s=nodes[i+s_i]
        usage[f"{t}::{n}"]+=s

    top=sorted(usage.items(),key=lambda x:x[1],reverse=True)[:10]

    return {k:v/1024/1024 for k,v in top}
