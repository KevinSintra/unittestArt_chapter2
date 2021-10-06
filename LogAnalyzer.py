class LogAnalyzer:
    def isValidLogFileName(self, fileName):
        if fileName.endswith('.SLF') or fileName.endswith('.slf'):
            return True
        else:
            return False