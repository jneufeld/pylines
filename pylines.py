# ==============================================================================
# pylines.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from sys import argv

from FileAnalyzer import FileAnalyzer
from StatisticsPrinter import StatisticsPrinter


# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    files = argv[1:]
    printer = StatisticsPrinter()

    for source_file in files:
        analyzer = FileAnalyzer(source_file)
        printer.add_stats(analyzer.stats)

    printer.print_stats()
