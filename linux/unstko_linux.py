#!/usr/bin/env python3

from plumbum import cli

class UnstkoLinux(cli.Application):
    PROGNAME = "unstko_linux"
    VERSION = "0.1"
    DESCRIPTION = "Linux commands"

    def main(self):
        print("Linux")

UnstkoLinux.subcommand("update-system", "update_system.UpdateSystem")

if __name__ == "__main__":
    UnstkoLinux().run()
