
import json, gzip
from collections import defaultdict

def load_trace(path):
    if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    with open(path) as f:
        return json.load(f)

def analyze_trace(path):
    trace = load_trace(path)
    events = trace.get("traceEvents", [])

    long_tasks = 0
    cpu = defaultdict(float)
    render = defaultdict(float)

    for e in events:
        if e.get("ph") == "X":
            dur = e.get("dur", 0)/1000
            name = e.get("name")

            if name == "RunTask" and dur > 50:
                long_tasks += 1

            if name in ["EvaluateScript","FunctionCall"]:
                cpu[name]+=dur

            if name in ["Layout","Paint"]:
                render[name]+=dur

    return {
        "long_tasks": long_tasks,
        "cpu": dict(cpu),
        "render": dict(render)
    }
