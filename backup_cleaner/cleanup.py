import requests
import os

bearer_token = f'Bearer: {os.environ.get("SUPERVISOR_TOKEN")}'
headers = {"Authorization": bearer_token}

print("[backup_cleaner_script] Script starting...")
# 0. Load all the backups
r = requests.get("http://supervisor/backups", headers=headers)
backups = r.json()['data']['backups']

# 1. Ignore anything that's not a full backup
backups = [x for x in backups if x["type"] == "full"]
full_slugs = [x["slug"] for x in backups]

if not full_slugs:
  print("[backup_cleaner_script] There are no backups, so none will be deleted")
else:
  # 2. Ignore the most recent full backup
  most_recent = max(backups, key=lambda b: b["date"] )
  latest_slug = most_recent["slug"]
  print(f'[backup_cleaner_script] Backup {latest_slug} is the most recent and will not be deleted.')

  # 3. If anything is left, remove it with the slug
  to_delete = set(full_slugs) - set([latest_slug])
  for slug in to_delete:
    requests.delete(f'http://supervisor/backups/{slug}', headers=headers)
    print(f'[backup_cleaner_script] Deleted backup {slug}')
  if not to_delete:
    print("[backup_cleaner_script] Nothing to delete")

print("[backup_cleaner_script] Script ended")