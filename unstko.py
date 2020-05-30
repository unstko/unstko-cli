#!/usr/bin/env python3

from plumbum import cli
from linux import unstko_linux


class Unstko(cli.Application):
    PROGNAME = "unstko"
    VERSION = "0.1"
    DESCRIPTION = "Python command line interface (CLI) \
        with applications from @unstko"

    def main(self, *args):
        if args:
            print("Unknown command {0!r}".format(args[0]))
            return 1
        if not self.nested_command:
            print("No command given")
            return 1


Unstko.subcommand("linux", "linux.unstko_linux.UnstkoLinux")
unstko_linux.UnstkoLinux.subcommand(
    "update-system", "linux.update_system.UpdateSystem")

if __name__ == "__main__":
    Unstko.run()
