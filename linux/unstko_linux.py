#!/usr/bin/env python3

from plumbum import cli


class UnstkoLinux(cli.Application):
    PROGNAME = "unstko linux"
    VERSION = "0.1"
    DESCRIPTION = "Linux commands"

    def main(self, *args):
        if args:
            print("Unknown command {0!r}".format(args[0]))
            return 1
        if not self.nested_command:
            print("No command given")
            return 1


UnstkoLinux.subcommand("update-system", "update_system.UpdateSystem")

if __name__ == "__main__":
    UnstkoLinux().run()
