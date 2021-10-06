from MemCalculator import MemCalculator


class TestMemCalculator:

    def test_Sum_ByDefault_ReturnZero(self):
        calculator = self.__makeCalculator()
        result = calculator.sum()
        assert result == 0

    def test_Sum_WhenCalled_ChangesSum(self):
        calculator = self.__makeCalculator()
        calculator.add(1)
        result = calculator.sum()
        assert result == 1

    # factory
    @staticmethod
    def __makeCalculator():
        return MemCalculator()
