# chrome-perf-analyzer (Diagnostics + Raw Output Edition)

## Turn Chrome DevTools output into engineering decisions.

Analyzes Chrome DevTools traces and heap snapshots.

Now outputs:

• Raw trace metrics  
• Raw heap top consumers  
• Diagnostics insights  
• Fix recommendations  

---

## Run

python -m chrome_perf_analyzer.report --trace Trace.json.gz --heap Heap.heapsnapshot
