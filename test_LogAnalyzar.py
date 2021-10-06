from LogAnalyzer import LogAnalyzer

class TestLogAnalyzer:
    def test_IsValidFileName_badExtension_RetunrFalse(self):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName("fileName.foo")
        assert result == False

    def test_IsValidLogFileName_GoodExtensionLowercase_ReturnTrue(self):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName("fileName.slf")
        assert result == True
    
    def test_IsValidLogFileName_GoodExtensionUppercase_ReturnTrue(self):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName("fileName.SLF")
        assert result == True