# ==============================================================================
# StatisticsPrinter.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from FileStatistics import FileStatistics


# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class StatisticsPrinter(object):
    """
    Manages the printing of all source files analyzed.
    """

    def __init__(self):
        """
        Creates a printer manager.
        """
        self.stats = []
        self.not_analyzed = []
        self.analysis_failed = []


    def add_stats(self, file_stats):
        """
        Adds file statistics.

        Arguments:
            file_stats<FileStatistics> -- File stats for a source file.
        """
        if type(file_stats) != FileStatistics:
            raise Exception('File provided not of type FileStatistics. Was=%s' \
                % type(file_stats))

        if not file_stats.was_analyzed:
            self.not_analyzed.append(file_stats)
        elif file_stats.analysis_failed:
            self.analysis_failed.append(file_stats)
        else:
            self.stats.append(file_stats)


    def print_stats(self):
        """
        Prints the statistics for all source files.
        """
        self.print_successful()
        self.print_unanalyzed()
        self.print_unsuccessful()


    def print_successful(self):
        """
        Prints the statistics for all source files which were successfully
        analyzed.
        """
        longest_name = self.get_longest_name()
        total, code, comment, blank = self.get_max_digits()

        name = max(len('File'), len(longest_name))
        total = max(len('Total'), total)
        code = max(len('Code'), code)
        comment = max(len('Comment'), comment)
        blank = max(len('Blank'), blank)

        print '%s %s %s %s %s' % ('File'.ljust(name),
            'Total'.ljust(total),
            'Code'.ljust(code),
            'Comment'.ljust(comment),
            'Blank'.ljust(blank))

        for stat in self.stats:
            print '%s %s %s %s %s' % (stat.file_name.ljust(name),
                str(stat.total_lines).ljust(total),
                str(stat.code_lines).ljust(code),
                str(stat.comment_lines).ljust(comment),
                str(stat.blank_lines).ljust(blank))


    def print_unanalyzed(self):
        """
        Prints files which were unanalyzed.
        """
        if len(self.not_analyzed) > 0:
            print '\nThe following files were never analyzed:'

            for unanalyzed_file in self.not_analyzed:
                print '\t%s' % unanalyzed_file.file_name
        

    def print_unsuccessful(self):
        """
        Prints files that could not successfully be analyzed.
        """
        if len(self.analysis_failed) > 0:
            print '\nThe following files could not be found or opened:'

            for failed_file in self.analysis_failed:
                print '\t%s' % failed_file.file_name


    def get_longest_name(self):
        """
        Finds the file with the longest name.

        Returns:
            File name of the longest length file name.
        """
        longest_name, longest_length = None, 0

        for file_stats in self.stats:
            name = file_stats.file_name
            length = len(name)

            if length > longest_length:
                longest_length = length
                longest_name = name

        return longest_name


    def get_max_digits(self):
        """
        Finds number of digits in total, code, comment, and blank line count of
        files with most total, code, comment, and blank lines.

        Returns:
            Number of digits in highest digit total, code, comment, and blank
            lines as a tuple: (total, code, comment, blank).
        """
        total_digits, code_digits, comment_digits, blank_digits = 0, 0, 0, 0

        for file_stats in self.stats:
            total_length = len(str(file_stats.total_lines))
            code_length = len(str(file_stats.code_lines))
            comment_length = len(str(file_stats.code_lines))
            blank_length = len(str(file_stats.code_lines))

            if total_length > total_digits:
                total_digits = total_length
            if code_length > code_digits:
                code_digits = code_length
            if comment_length > comment_digits:
                comment_digits = comment_length
            if blank_length > blank_digits:
                blank_digits = blank_length

        return (total_digits, code_digits, comment_digits, blank_digits)
