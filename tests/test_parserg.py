import parserg

def test_answer():
    assert parserg.from_string('{"test": ["one", "two"]}') == {'test': ['one', 'two']}
