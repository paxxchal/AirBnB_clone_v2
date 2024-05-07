#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the directory versions if it doesn't exist
        local("mkdir -p versions")

        # Create a timestamped archive name
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(time_stamp)

        # Archive the contents of web_static to the archive_path
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except:
        return None


if __name__ == "__main__":
    do_pack()
