def test_test_remove_name(user):
    user.name = ""
    assert user.name == "" 

def test_name(user):
    assert user.name == "Pavlo"

def test_second_name(user):
    assert user.second_name == "Znak"