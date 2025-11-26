import json, subprocess, pathlib, sys, time
from datetime import datetime, timezone

# Where your paper markdowns live (update if different)
GLOB = "_publications/*.markdown"

def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def iso(ts):
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).isoformat()

def first_added(path):
    # First commit that added this file
    # %at = author date (unix)
    cmd = f'git log --diff-filter=A --follow --format=%at -- "{path}" | tail -n 1'
    out = sh(cmd)
    return iso(out) if out else None

def last_modified(path):
    # Most recent commit touching this file
    cmd = f'git log -1 --format=%at -- "{path}"'
    out = sh(cmd)
    return iso(out) if out else None

def main():
    files = [str(p) for p in pathlib.Path(".").glob(GLOB) if p.is_file()]
    items = {}
    latest_added_ts = 0

    for f in files:
        fa = first_added(f)
        lm = last_modified(f)
        key = pathlib.Path(f).stem.lower()  # e.g. use the filename (no extension) as your page key

        items[key] = {
            "path": f,
            "first_added": fa,
            "last_modified": lm
        }
        if fa:
            ts = int(datetime.fromisoformat(fa).timestamp())
            latest_added_ts = max(latest_added_ts, ts)

    manifest = {
        "generated_at": iso(time.time()),
        "latest_added": iso(latest_added_ts) if latest_added_ts else None,
        "items": items
    }

    pathlib.Path("assets").mkdir(exist_ok=True, parents=True)
    with open("assets/paper-history.json", "w") as fp:
        json.dump(manifest, fp, indent=2, sort_keys=True)

if __name__ == "__main__":
    main()
