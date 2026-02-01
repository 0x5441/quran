import datetime, tempfile, os
import requests, gdown

WEBHOOK = os.environ["https://discord.com/api/webhooks/1435547750161973308/af3RL4kxXCGxfG4-jEYlAWMGC4Pdg8eVfiXylBA0JJQAaJeMuAhONOkrD9ag7pivRpHi"]

lines = [x.strip() for x in open("videos.txt") if x.strip()]
i = datetime.date.today().toordinal() % len(lines)
url = lines[i]

tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
tmp.close()
gdown.download(url, tmp.name, quiet=True, fuzzy=True)

with open(tmp.name, "rb") as f:
    r = requests.post(WEBHOOK, files={"file": f})

if r.status_code >= 300:
    requests.post(WEBHOOK, json={"content": url})

os.remove(tmp.name)
