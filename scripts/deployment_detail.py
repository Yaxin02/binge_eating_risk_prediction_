import json
import os
import sys
import urllib.request

endpoint = os.environ.get("APPWRITE_ENDPOINT", "https://nyc.cloud.appwrite.io/v1").rstrip("/")
project = os.environ.get("APPWRITE_PROJECT_ID", "69d8f483003b02a74713")
key = os.environ["APPWRITE_API_KEY"]

dep_id = sys.argv[1] if len(sys.argv) > 1 else ""
if not dep_id:
    lst = urllib.request.Request(f"{endpoint}/functions/predict/deployments")
    lst.add_header("X-Appwrite-Project", project)
    lst.add_header("X-Appwrite-Key", key)
    with urllib.request.urlopen(lst) as r:
        data = json.load(r)
    for dep in data.get("deployments", []):
        if dep.get("status") == "ready":
            dep_id = dep.get("$id") or dep.get("id") or ""
            break
    if not dep_id:
        raise SystemExit("No ready deployment; pass deployment_id as argument.")
url = f"{endpoint}/functions/predict/deployments/{dep_id}"
req = urllib.request.Request(url)
req.add_header("X-Appwrite-Project", project)
req.add_header("X-Appwrite-Key", key)
with urllib.request.urlopen(req) as r:
    data = json.load(r)
print("status:", data.get("status"))
logs = data.get("buildLogs") or ""
tail = (logs[-3000:] if logs else "(empty)").encode("ascii", errors="replace").decode("ascii")
print("logs (tail):", tail)
