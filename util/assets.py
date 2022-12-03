import time


def assert_equal(actualResult, expected):
    assert actualResult == expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)


def assert_not_equal(actualResult, expected):
    assert actualResult != expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)


def assert_in(actualResult, expected):
    assert actualResult in expected, "实际结果为:{0}, 预期结果为:{1}".format(actualResult, expected)
