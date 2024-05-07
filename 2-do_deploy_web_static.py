#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import isfile

env.hosts = ["54.160.125.94", "100.25.164.205"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not isfile(archive_path):
        return False

    try:
        # Extract the file name from the archive path
        file_name = archive_path.split("/")[-1]
        # Remove the extension from the file name
        name = file_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Uncompress the archive to the folder on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move the content out of the web_static folder
        run(
            "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
                name, name
            )
        )
        # Remove the empty folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))

        print("New version deployed!")
        return True
    except:
        return False


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        do_deploy(argv[1])
