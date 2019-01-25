import allure
class Test_001:
    @allure.step(title="我是测试步骤1")
    def test_001_01(self):
        print("test_001_01步骤")
        assert True

    @allure.step(title="test_002_02步骤")
    def test_001_02(self):
        print("test_002_02步骤")
        assert False
