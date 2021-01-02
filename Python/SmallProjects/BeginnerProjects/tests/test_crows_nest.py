from ..crows_nest import CrowsNest


def test_capitalization():
    assert CrowsNest()._cap("wow") == "wow".capitalize()


def test_functionality():
    assert CrowsNest().run(
        ["__main__", "person"]) == "Ahow, Captain, a Person off the landboard bow!"
    assert CrowsNest()._vowelCheck("i") == "an"
    assert CrowsNest()._vowelCheck("I") == "an"
    assert CrowsNest()._vowelCheck("x") == "a"
    assert CrowsNest()._vowelCheck("X") == "a"
