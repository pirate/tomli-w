import tomli_w


def test_newline_before_table():
    actual = tomli_w.dumps({"table": {}})
    expected = "[table]\n"
    assert actual == expected

    actual = tomli_w.dumps({"table": {"nested": {}, "val3": 3}, "val2": 2, "val1": 1})
    expected = """\
val2 = 2
val1 = 1

[table]
val3 = 3

[table.nested]
"""
    assert actual == expected


def test_empty_doc():
    assert tomli_w.dumps({}) == ""


def test_dont_write_redundant_tables():
    actual = tomli_w.dumps({"tab1": {"tab2": {"tab3": {}}}})
    expected = "[tab1.tab2.tab3]\n"
    assert actual == expected
