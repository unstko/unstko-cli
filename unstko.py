#!/usr/bin/env python3

from plumbum import cli

class Unstko(cli.Application):
    PROGNAME = "unstko"
    VERSION = "0.1"
    DESCRIPTION = "The command line interface (CLI) with Applications from @unstko"

    def main(self, *args):
        if args:
            print("Unknown command {0!r}".format(args[0]))
            return 1
        if not self.nested_command:
            print("No command given")
            return 1

if __name__ == "__main__":
    Unstko.run()
