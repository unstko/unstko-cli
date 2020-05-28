#!/usr/bin/env python3

from plumbum import cli

class UpdateSystem(cli.Application):
    PROGNAME = "update-system"
    VERSION = "0.1"
    DESCRIPTION = "Update linux system"

    _distro = False

    @cli.switch(["-d", "--distro"], cli.Set("arch", "debian", case_sensitive = True), mandatory = True)
    def distro(self, distro):
        self._distro = distro

    def update_arch(self):
        print("Update arch system")

    def update_debian(self):
        print("Update debian system")

    def main(self):
        print("Update linux system")
        method_name = 'update_' + self._distro
        method = getattr(self, method_name, lambda: "Invalid distro")
        method()

if __name__ == "__main__":
    UpdateSystem().run()
