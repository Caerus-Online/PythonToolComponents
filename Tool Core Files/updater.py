import requests
import os
import hashlib
import shutil
from plyer import notification
import logging

# Configure logging
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "updater.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def check_for_updates():
    owner = "Caerus-Online"
    repo = "ChangeMe"
    branch = "main"
    files_to_update = ["main.py", "install.bat"]  # List of files to update
    PAT = "placeholder use env environment"

    for file_to_update in files_to_update:
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_to_update}"

        try:
            headers = {"Authorization": f"token {PAT}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            latest_content = response.content
            latest_hash = hashlib.sha256(latest_content).hexdigest()
            local_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), file_to_update
            )

            if os.path.exists(local_file_path):
                with open(local_file_path, "rb") as f:
                    local_content = f.read()
                    local_hash = hashlib.sha256(local_content).hexdigest()

                if latest_hash != local_hash:
                    backup_file_path = local_file_path + ".bak"
                    shutil.copy2(local_file_path, backup_file_path)

                    with open(local_file_path, "wb") as f:
                        f.write(latest_content)

                    logging.info(
                        f"Updated {file_to_update} successfully! Backup created at {backup_file_path}"
                    )
                    notification.notify(
                        title="File Merger and Transformer Updater",
                        message=f"Updated {file_to_update} successfully!",
                        app_name="File Merger and Transformer",
                        timeout=5,
                    )
            else:
                with open(local_file_path, "wb") as f:
                    f.write(latest_content)
                logging.info(f"Created {file_to_update}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking for updates for {file_to_update}: {e}")


if __name__ == "__main__":
    check_for_updates()
