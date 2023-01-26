from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    with raises(TypeError):
        encrypt_message(1, 1)
        encrypt_message("lorena", 1)

    assert encrypt_message("lorena", -1) == "anerol"
    assert encrypt_message("lorena", 3) == "rol_ane"
    assert encrypt_message("lorena", 4) == "an_erol"
    assert encrypt_message("lorena", 5) == "nerol_a"
