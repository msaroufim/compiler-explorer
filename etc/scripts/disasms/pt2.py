import torch
import os
import sys
import dis
import argparse
import traceback

from dis import dis, disassemble, distb, _have_code, _disassemble_bytes, _try_compile

parser = argparse.ArgumentParser(description='Disassembles Python source code given by an input file and writes the output to a file')
parser.add_argument('-i', '--inputfile', type=str,
                    help='Input source code file (*.py)')
parser.add_argument('-o', '--outputfile', type=str,
                    help='Optional output file to write output (or error message if syntax error).',
                    default='')
parser.add_argument('-O', action='store_true', dest='optimize_1',
                    help="Enable Python's -O optimization flag (remove assert and __debug__-dependent statements)")
parser.add_argument('-OO', action='store_true', dest='optimize_2',
                    help="Enable Python's -OO optimization flag (do -O changes and also discard docstrings)")


def _disassemble_recursive(co, depth=None):
    disassemble(co)
    if depth is None or depth > 0:
        if depth is not None:
            depth = depth - 1
        for x in co.co_consts:
            if hasattr(x, 'co_code'):
                print()
                print("Disassembly of %r:" % (x,))
                _disassemble_recursive(x, depth=depth)


def _disassemble_str(source, **kwargs):
    """Compile the source string, then disassemble the code object."""
    _disassemble_recursive(_try_compile(source, '<dis>'), **kwargs)


nif __name__ == '__main__':
    args = parser.parse_args()

    if not args.inputfile:
        parser.print_help(sys.stderr)
        sys.exit(1)

    with open(args.inputfile, 'r', encoding='utf8') as fp:
        source = fp.read()

    name = os.path.basename(args.inputfile)

    optimize=0
    if args.optimize_1:
        optimize = 1
    if args.optimize_2:
        optimize = 2

    try:
        code = compile(source, name, 'exec', optimize=optimize)
    except Exception as e:
        # redirect any other by compile(..) to stderr in order to hide traceback of this script
        sys.stderr.write(''.join(traceback.format_exception_only(type(e), e)))
        sys.exit(255)

    if args.outputfile:
        sys.stdout = open(args.outputfile, 'w', encoding='utf8')

    import base64
    encoded = base64.b64encode(code.co_code).decode('utf-8')
    print(encoded)
