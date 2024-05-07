#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.160.125.94", "100.25.164.205"]
env.user = "ubuntu"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not os.path.isfile(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        name = file_name.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name))
        run("rm /tmp/{}".format(file_name))
        run(
            "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
                name, name
            )
        )
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
