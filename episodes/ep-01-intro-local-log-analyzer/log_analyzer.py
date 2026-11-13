from pathlib import Path

log_path = Path("sample_security.log")

failed_count = 0
failed_by_user = {}

for line in log_path.read_text(encoding="utf-8").splitlines():

    fields = dict(
        item.split("=", 1)
        for item in line.split()
        if "=" in item
    )

    if fields.get("event") == "LOGIN_FAILED":

        failed_count += 1

        user = fields.get("user", "unknown")

        failed_by_user[user] = (
            failed_by_user.get(user, 0) + 1
        )

print(f"Failed login events: {failed_count}")

for user, count in sorted(failed_by_user.items()):
    print(f"  {user}: {count}")