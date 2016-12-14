# -*- coding: utf-8 -*-

import click
import os
import sys

from datetime import datetime

from helpers import slugify, fetchJSON
from models import AsynkDownloader, DebianLinux


@click.command()
@click.option('--ok',
              prompt='This program must only be run in live environments as it may '
                     'permanently screw up your system. Are you sure you want to continue?',
              default='yes')
@click.option('--bundle',
              prompt='What bundle do you want to use:',
              help='The bundle to configure your system after',
              default='flat-dark')
def main(bundle, ok):
    """
    Console script for i3asap
    """
    startTime = datetime.now()

    if ok != 'yes':
        sys.exit()

    linux = DebianLinux()
    if not linux.verifyOS():
        click.echo("Currently this program only supports Kali Linux. Exiting..")
        sys.exit()

    bundle = slugify(bundle)
    pwd = linux.home_dir() + "/.i3asap/" + bundle + "/"
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
    if "purge" in manifest and len(manifest["uninstall"]) > 1:
        linux.uninstall(manifest["uninstall"])

    # Install specified programs
    if "install" in manifest and len(manifest["install"]) > 1:
        linux.install(manifest["install"])

    # Install i3
    linux.install(linux.i3_base_packages())

    # todo Create new user
    # Wait until downloads are complete
    downloads.join()

    # todo Move dotfiles, wallpapers etc to proper paths
    # todo Set wallpaper if specified

    click.echo("Done! Time elapsed: " + str(datetime.now() - startTime))
    # todo Switch user to new user


if __name__ == "__main__":
    main()
