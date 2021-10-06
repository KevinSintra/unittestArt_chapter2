class LogAnalyzer:
    wasLastFileNameValid = False

    def isValidLogFileName(self, fileName):
        self.wasLastFileNameValid = False
        if not fileName:
            raise Exception("fileName 檔名不能為空")

        if fileName.endswith('.SLF') or fileName.endswith('.slf'):
            self.wasLastFileNameValid = True
            return True
        else:
            return False