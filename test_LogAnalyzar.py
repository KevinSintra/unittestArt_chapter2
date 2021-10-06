from LogAnalyzer import LogAnalyzer
import pytest

class TestLogAnalyzer:
    def test_IsValidFileName_badExtension_RetunrFalse(self):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName("fileName.foo")
        assert result == False

    # parametrize 可設定多種參數, 達到減少測試方法的數量並增加可讀性.
    @pytest.mark.parametrize("fileName", ["fileName.slf", "fileName.SLF"], ids=["testLower", "testUpper"])
    def test_IsValidLogFileName_ValidExtension_ReturnTrue(self, fileName):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName(fileName)
        assert result == True
    