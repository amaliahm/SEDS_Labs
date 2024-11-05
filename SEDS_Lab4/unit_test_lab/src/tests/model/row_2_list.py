def row_2_list(s):
    return list(s.split())

def test_for_clean_row():
    assert row_2_list("2,081\t314,942\n") == ["2,081", "314,942"]


def test_for_missing_area():
    assert row_2_list("\t293,410\n") is None


def test_for_missing_tab():
    assert row_2_list("314,942,281\n") is None
