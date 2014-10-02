# ==============================================================================
# FileAnalyzer.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from FileStatistics import FileStatistics


# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class FileAnalyzer(object):
    """
    Opens and analyzes a Python source file, creating a FileStatistics object
    with the results.
    """

    def __init__(self, file_name):
        """
        Creates a file analyzer and gathers statistics on the given file.

        Arguments:
            file_name<string> -- Name of file to open and analyze.
        """
        self.stats = None
        self.file_name = file_name
        self.was_analyzed = False
        self.analysis_succeeded = False

        self.analyze()


    def analyze(self):
        """
        Opens and analyzes the source file.
        """
        self.was_analyzed = True
        total, code, comment, blank = 0, 0, 0, 0

        source_file = None

        try:
            source_file = open(self.file_name)
        except IOError:
            self.stats = FileStatistics(self.file_name,
                total,
                code,
                comment,
                blank,
                self.was_analyzed,
                self.analysis_succeeded)
            return

        in_multiline = False

        for line in source_file:
            cleaned = line.strip()

            if in_multiline:
                if self.ends_multiline(cleaned):
                    in_multiline = False

                comment += 1
            else:
                if self.is_blank(cleaned):
                    blank += 1
                elif self.is_singleline_comment(cleaned):
                    comment += 1
                elif self.starts_multiline(cleaned):
                    in_multiline = True
                    comment += 1
                else:
                    code += 1

            total += 1

        source_file.close()

        self.analysis_succeeded = True
        self.stats = FileStatistics(self.file_name,
            total,
            code,
            comment,
            blank,
            self.was_analyzed,
            self.analysis_succeeded)


    def is_blank(self, line):
        """
        Returns true if the given line is a blank line, i.e. whitespace.

        Arguments:
            line<string> -- Whitespace trimmed, singe line.

        Returns:
            True if the line is blank, i.e. whitespace, else False.
        """
        return len(line) == 0


    def is_singleline_comment(self, line):
        """
        Returns true if the given line is a single line comment.

        Arguments:
            line<string> -- Whitespace trimmed, singe line.

        Returns:
            True if the line is a single line comment, else False.
        """
        return line[0] == '#'


    def starts_multiline(self, line):
        """
        Returns true if the given line begins a multiline comment.

        Arguments:
            line<string> -- Whitespace trimmed, singe line.

        Returns:
            True if the given line begins a multiline comment, else False.
        """
        result = False

        if len(line) >= 3 and \
                line[0] == line[1] and \
                line[1] == line[2] and \
                (line[0] == '"' or \
                 line[0] == '\''):
            result = True

        return result


    def ends_multiline(self, line):
        """
        Returns true if the given line ends a multiline comment.

        Arguments:
            line<string> -- Whitespace trimmed, singe line.

        Returns:
            True if the given line ends a multiline comment, else False.
        """
        if len(line) < 3:
            return False

        result = False

        end = len(line) - 1
        if line[end] == line[end - 1] and \
                line[end - 1] == line[end - 2] and \
                (line[end] == '"' or \
                 line[end] == '\''):
            result = True

        return result
