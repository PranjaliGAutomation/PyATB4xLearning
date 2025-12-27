import pytest
import allure

@allure.title("verify that 4 - 3 == 1")
@allure.description("This is a smoke TC, which checks 4 - 3 == 1")
@pytest.mark.smoke
def test_test_sub0():
    assert 4 - 3 == 1

@allure.title("verify that 6 - 4 == 2")
@allure.description("This is a smoke TC, which checks 6 - 4 == 2")
@pytest.mark.smoke
def test_test_sub1():
    assert 6 - 4 == 2

@allure.title("verify that 7 + 2 == 5")
@allure.description("This is a smoke TC, which checks 7 + 2 == 5")
@pytest.mark.smoke
def test_test_sub2():
    assert 7 - 2 == 5

@allure.title("verify that 3 - 2 == 1")
@allure.description("This is a smoke TC, which checks 3 - 2 == 1")
@pytest.mark.smoke
def test_test_sub3():
    assert 3 - 2 == 1
