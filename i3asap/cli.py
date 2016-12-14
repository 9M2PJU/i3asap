# -*- coding: utf-8 -*-

import click
from os.path import expanduser
import os, sys

from datetime import datetime

from helpers import slugify, fetchJSON
from models import AsynkDownloader, KaliLinux


@click.command()
@click.option('--bundle',
              prompt='What bundle do you want to use:',
              help='The bundle to configure your system after',
              default='flat-dark')
def main(bundle):
    """
    Console script for i3asap
    """
    startTime = datetime.now()

    nix = KaliLinux()
    if not nix.verifyOS():
        click.echo("Currently this program only supports Kali Linux. Exiting..")
        sys.exit()

    bundle = slugify(bundle)
    pwd = nix.home_dir() + "/.i3asap/" + bundle + "/"
    repository = "https://raw.githubusercontent.com/SteveTabernacle/i3asap/"

    if not os.path.exists(pwd):
        os.makedirs(pwd)

    # Download manifest to get started
    click.echo("Downloading " + bundle)

    manifest = fetchJSON(repository + "master/bundles/" + bundle + "/manifest.json")

    # Download all specified files, e.g. dotfiles and wallpaper
    downloads = AsynkDownloader(manifest["files"], pwd, repository + "master/bundles/" + bundle + "/bundle/")
    downloads.start()

    # Purge specified programs
    if "purge" in manifest and len(manifest["purge"]) > 1:
        click.echo("apt-get purge " + manifest["purge"])

    # Install specified programs
    if "install" in manifest and len(manifest["install"]) > 1:
        click.echo("apt-get install " + manifest["install"])

    # Install i3
    click.echo("apt-get install " + nix.i3_base_packages())

    # todo Create new user
    # Wait until downloads are complete
    downloads.join()

    # todo Move dotfiles, wallpapers etc to proper paths
    # todo Set wallpaper if specified

    click.echo("Done! Time elapsed: " + str(datetime.now() - startTime))
    # todo Switch user to new user


if __name__ == "__main__":
    main()
