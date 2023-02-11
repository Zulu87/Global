import pytest

from modules.ui.page_objects.sign_in_page import SignInPage

@pytest.mark.ui
def test_incorrect_username():

    sign_in_page = SignInPage()

    sign_in_page.go_to()

    #знаходимо поле для вводу пошти
    sign_in_page.try_login ("pavlo@wrongmail.com","Admin")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub" )

    sign_in_page.close()

  
    