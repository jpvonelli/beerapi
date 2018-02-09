import beerapi


def test_root_give_hello_word():
    beerapi.app.testing = True
    app = beerapi.app.test_client()

    result = app.get('/')
    assert b"Hello World" in result.data