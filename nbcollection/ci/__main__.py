import sys
import argparse

from nbcollection.ci.commands import install, uninstall, venv, replicate

commands = {
  'install': install,
  'uninstall': uninstall,
  'venv': venv,
  'replicate': replicate,
}

DESCRIPTION = """Type `nbcollection-ci <command> -h` for help.

The allowed commands are:

    nbcollection-ci install
    nbcollection-ci uninstall
    nbcollection-ci env
    nbcollection-ci replicate
"""

def parse_options(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                 formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("command",
            help=f"The command you'd like to run. Allowed commands: {list(commands.keys())}")

    args = args or sys.argv
    return parser.parse_args(args[1:2])

def main(args=None):
    parsed = parse_options(args)
    if parsed.command not in commands:
        parser.print_help()
        raise ValueError(f'Unrecognized command: {parsed.command}\n See the '
                         'help above for usage information')

    # Run the command
    commands[parsed.command].convert(args)


if __name__ == "__main__":
    main()