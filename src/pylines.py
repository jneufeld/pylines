#!/usr/bin/python

# ==============================================================================
# pylines.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from sys import argv, exit

from FileAnalyzer import FileAnalyzer
from StatisticsPrinter import StatisticsPrinter

# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) < 2:
        print 'Usage: pylines <python source file>+'
        exit()

    files = argv[1:]
    printer = StatisticsPrinter()

    for source_file in files:
        analyzer = FileAnalyzer(source_file)
        printer.add_stats(analyzer.stats)

    printer.print_stats()
