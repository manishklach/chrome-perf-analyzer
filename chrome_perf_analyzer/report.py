
import argparse
from chrome_perf_analyzer.trace import analyze_trace
from chrome_perf_analyzer.heap import analyze_heap
from chrome_perf_analyzer.diagnostics import interpret

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--trace")
    ap.add_argument("--heap")
    args=ap.parse_args()

    trace = analyze_trace(args.trace) if args.trace else {}
    heap  = analyze_heap(args.heap) if args.heap else {}

    insights, fixes = interpret(trace, heap)

    print("\n=== RAW TRACE METRICS ===\n")
    print("Long tasks:", trace.get("long_tasks"))
    print("CPU:", trace.get("cpu"))
    print("Render:", trace.get("render"))

    print("\n=== RAW HEAP TOP CONSUMERS (MB) ===\n")
    for k,v in heap.items():
        print(k, ":", round(v,2), "MB")

    print("\n=== PERFORMANCE DIAGNOSTICS ===\n")
    for i in insights:
        print("INSIGHT:", i)

    print("\n=== RECOMMENDED FIXES ===\n")
    for f in fixes:
        print("FIX:", f)
