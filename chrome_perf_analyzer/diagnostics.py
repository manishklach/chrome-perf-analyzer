
def interpret(trace, heap):

    insights = []
    fixes = []

    total_js = sum(trace.get("cpu",{}).values())
    if total_js > 500:
        insights.append("Heavy JavaScript execution detected.")
        fixes.append("Reduce bundle size, lazy load scripts, minimize JSON parsing.")

    if trace.get("long_tasks",0) > 10:
        insights.append("Frequent long main-thread tasks causing UI blocking.")
        fixes.append("Break work into async chunks or web workers.")

    if sum(trace.get("render",{}).values()) > 100:
        insights.append("Rendering pipeline pressure detected.")
        fixes.append("Reduce DOM size, virtualize lists, simplify layouts.")

    for k,v in heap.items():
        if "ExternalStringData" in k and v > 20:
            insights.append("Large text/blob retention in memory.")
            fixes.append("Limit chat history and discard old responses.")

        if "Array" in k and v > 10:
            insights.append("Large JS array retention.")
            fixes.append("Paginate results and prune datasets.")

    return insights, fixes
