# -*- coding: utf-8 -*-

import click
import os
import sys

from datetime import datetime

from helpers import slugify, fetchJSON
from models import AsynkDownloader, DebianLinux
import logging


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

    # check if it is reasonable to start at all
    if ok != 'yes':
        sys.exit()
    linux = DebianLinux()
    if not linux.verifyOS():
        click.echo("Currently this program only supports Kali Linux. Exiting..")
        sys.exit()

    # Setup properties
    repository = "https://raw.githubusercontent.com/SteveTabernacle/i3asap/"
    bundle = slugify(bundle)
    pwd = linux.home_dir() + "/.i3asap/" + bundle + "/"

    if not os.path.exists(pwd):
        os.makedirs(pwd)

    # Init logging
    LOG_FILENAME = pwd+'debug.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.debug("Started new instance "+str(startTime))

    # Download manifest
    click.echo("* Downloading " + bundle)

    manifest = fetchJSON(repository + "master/bundles/" + bundle + "/manifest.json")

    # Download all specified files, e.g. dotfiles and wallpaper
    downloads = AsynkDownloader(manifest["files"], pwd, repository + "master/bundles/" + bundle + "/bundle/")
    downloads.start()

    click.echo("* Uninstalling " + manifest["uninstall"])
    # Purge specified programs
    if "purge" in manifest and len(manifest["uninstall"]) > 1:
        logging.debug(linux.uninstall(manifest["uninstall"]))

    click.echo("* Installing " + manifest["install"])
    # Install specified programs
    if "install" in manifest and len(manifest["install"]) > 1:
        logging.debug(linux.install(manifest["install"]))

    # Install i3
    click.echo("* Installing " + linux.i3_base_packages())
    linux.install(linux.i3_base_packages())

    # todo Create new user
    # Wait until downloads are complete
    downloads.join()
    click.echo("* Download finished ")

    # todo Move dotfiles, wallpapers etc to proper paths
    # todo Set wallpaper if specified

    click.echo("* Done! Time elapsed: " + str(datetime.now() - startTime))
    # todo Switch user to new user


if __name__ == "__main__":
    main()
