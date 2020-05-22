#!/usr/bin/env python3

from plumbum import cli

class UnstkoLinux(cli.Application):
    PROGNAME = "unstko_linux"
    VERSION = "0.1"
    DESCRIPTION = "Linux commands"

    def main(self):
        print("Linux")

if __name__ == "__main__":
    UnstkoLinux().run()
