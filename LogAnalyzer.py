class LogAnalyzer:
    def isValidLogFileName(self, fileName):
        if not fileName:
            raise Exception("fileName 檔名不能為空")

        if fileName.endswith('.SLF') or fileName.endswith('.slf'):
            return True
        else:
            return False