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

        self.NAME_HEADER = 'File'
        self.CODE_HEADER = 'Code'
        self.COMMENT_HEADER = 'Comment'
        self.BLANK_HEADER = 'Blank'
        self.TOTAL_HEADER = 'Total'
        self.PERCENT_HEADER = '%'


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
        nm_len, cd_len, cm_len, bl_len, tl_len, pc_len = self.get_max_len()

        print '%s %s %s %s %s %s %s %s' % (self.NAME_HEADER.ljust(nm_len),
            self.CODE_HEADER.ljust(cd_len),
            self.PERCENT_HEADER.ljust(pc_len),
            self.COMMENT_HEADER.ljust(cm_len),
            self.PERCENT_HEADER.ljust(pc_len),
            self.BLANK_HEADER.ljust(bl_len),
            self.PERCENT_HEADER.ljust(pc_len),
            self.TOTAL_HEADER.ljust(tl_len))

        for stat in self.stats:
            code_percent = str('%.1f' % stat.percent_code)
            comment_percent = str('%.1f' % stat.percent_comment)
            blank_percent = str('%.1f' % stat.percent_blank)

            print '%s %s %s %s %s %s %s %s' % (stat.file_name.ljust(nm_len),
                str(stat.code_lines).ljust(cd_len),
                code_percent.ljust(pc_len),
                str(stat.comment_lines).ljust(cm_len),
                comment_percent.ljust(pc_len),
                str(stat.blank_lines).ljust(bl_len),
                blank_percent.ljust(pc_len),
                str(stat.total_lines).ljust(tl_len))


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


    def get_max_len(self):
        """
        Find the string length necessary for each header and statistic column.

        Returns:
            String length for each header column in a tuple, like so:
            (filename, code, comment, blank, total, percent)
        """
        longest_name = self.get_longest_name()
        total, code, comment, blank = self.get_max_digits()

        name = max(len(self.NAME_HEADER), len(longest_name))
        total = max(len(self.TOTAL_HEADER), total)
        code = max(len(self.CODE_HEADER), code)
        comment = max(len(self.COMMENT_HEADER), comment)
        blank = max(len(self.BLANK_HEADER), blank)
        percent = len('100.0%')

        return (name, code, comment, blank, total, percent)


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
