#!/usr/bin/env python3

from plumbum import cli, local, FG
from plumbum.cmd import sudo


class UpdateSystem(cli.Application):
    PROGNAME = "update-system"
    VERSION = "0.1"
    DESCRIPTION = "Update linux system"

    _distro = False

    @cli.switch(["-d", "--distro"],
                cli.Set("arch", "debian", case_sensitive=True),
                mandatory=True)
    def distro(self, distro):
        """Distribution to update"""
        self._distro = distro

    def update_arch(self):
        print("Update arch system")
        pacman = local['pacman']
        pacman_update_cmd = pacman['-Syu']
        sudo[pacman_update_cmd] & FG

    def update_debian(self):
        print("Update debian system")
        apt_cmd = local['apt']
        apt_full_upgrade_cmd = apt_cmd['full-upgrade']
        sudo[apt_full_upgrade_cmd] & FG

    def main(self):
        method_name = 'update_' + self._distro
        method = getattr(self, method_name, lambda: "Invalid distro")
        method()


if __name__ == "__main__":
    UpdateSystem().run()
