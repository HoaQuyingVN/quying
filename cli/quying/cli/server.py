def add_subcommand_hello(subparsers):
    parser = subparsers.add_parser('server')
    parser.set_defaults(func=server)


def server (args):
  print ('Sorry, Something went wrong with CLI!')
