import json
from collections import Counter

log_file = "/app/access.log"
output_file = "/app/report.json"

total_requests = 0
ips = set()
paths = []

with open(log_file, "r") as f:
    for line in f:
        if line.strip():
            total_requests += 1
            parts = line.split()
            ips.add(parts[0])
            paths.append(parts[6])

top_path = Counter(paths).most_common(1)[0][0]

report = {
    "total_requests": total_requests,
    "unique_ips": len(ips),
    "top_path": top_path
}

with open(output_file, "w") as f:
    json.dump(report, f)
