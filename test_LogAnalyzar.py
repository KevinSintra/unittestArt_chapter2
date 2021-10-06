from LogAnalyzer import LogAnalyzer
import pytest

class TestLogAnalyzer:

    # parametrize 可設定多種參數, 達到減少測試方法的數量並增加可讀性. (也可用於設定 assert)
    @pytest.mark.parametrize("fileName, expected",
        [("fileName.slf", True), ("fileName.SLF", True), ("fileName.off", False)],
        ids=["testLower", "testUpper", "testErrName"])
    def test_IsValidLogFileName_VariousExtensions_ChecksThem(self, fileName, expected):
        logAnalyzar = LogAnalyzer()
        result = logAnalyzar.isValidLogFileName(fileName)
        assert result == expected
    
    def test_IsValidLogFileName_EmptyFileName_ThrowsExpection(self):
        logAnalyzar = LogAnalyzer()
        with pytest.raises(Exception):
            logAnalyzar.isValidLogFileName("")