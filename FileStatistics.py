# ==============================================================================
# FileStatistics.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class FileStatistics(object):
    """
    Stores statistics of the source file, like total lines of code, percentage
    of lines that are comments, etc..
    """

    def __init__(self, file_name, total, code, comment, blank):
        """
        Create a file statistics object. Percentage statistics are calculated
        from the given values.

        Arguments:
            file_name<string> -- Name of the file. 
            total<int>        -- Total lines in file.
            code<int>         -- Number of code lines in file.
            comment<int>      -- Number of comment lines in file.
            blank<int>        -- Number of blank/whitespace lines in file.
        """
        self.file_name = file_name

        self.total_lines = total
        self.code_lines = code
        self.comment_lines = comment
        self.blank_lines = blank

        self.calculate_percentages()


    def calculate_percentages(self):
        """
        Calculate the percentage of code, comment, and blank lines for this
        file.
        """
        if self.total_lines == 0:
            self.percent_code = 0.0
            self.percent_comment = 0.0
            self.percent_blank = 0.0
        else:
            self.percent_code = (float(self.code_lines) / \
                self.total_lines) * 100
            self.percent_comment = (float(self.comment_lines) / \
                 self.total_lines) * 100
            self.percent_blank = (float(self.blank_lines) / \
                self.total_lines) * 100
