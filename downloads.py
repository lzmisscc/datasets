from pathlib import Path
import uuid
import os

root = Path("images")
root.mkdir(exist_ok=True)


nums = 0
S = ""
for i in Path("photos.tsv000").read_text().splitlines()[1:]:
    nums += 1
    id, _, url, _ = i.split("\t", 3)
    (root / str(nums//1000)).mkdir(exist_ok=True)
    S += f"wget -c -O {root/str(nums//1000)/str(nums)}.jpg {url} & \n" 
        
    if nums % 1000 == 0:
        with os.popen(S + f"echo Download {nums//1000} Finish!") as f:
            print("Dowanload status:\n", f.read())
        S = ""