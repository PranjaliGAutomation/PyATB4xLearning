#create booking test case
#verify that booking is not null
#status code
#Create booking test case

#Request module - requests
import pytest
import allure
import requests

@allure.title("Get Test Request -Restful booker API Project #1")
@allure.description("TC#1->Verify that Get Request with ID works")
@allure.tag("Regression","P0","smoke")
#@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
#@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TC-#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responceData = requests.get(url)
    print(responceData.text)
    print(responceData.headers)
    print(responceData.json())
    assert responceData.status_code==200


# Negative test case
@allure.title("Get Test Request -Restful booker API Project #2")
@allure.description("TC#2->Verify that Get Request with ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    responceData = requests.get(url)
    print(responceData.text)
    assert responceData.status_code==404

@allure.title("Get Test Request -Restful booker API Project #3")
@allure.description("TC#3->Verify that Get Request with ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responceData = requests.get(url)
    print(responceData.text)
    assert responceData.status_code == 404
