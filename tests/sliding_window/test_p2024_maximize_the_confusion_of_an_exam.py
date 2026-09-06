from solutions.sliding_window.p2024_maximize_the_confusion_of_an_exam import Solution


def test_all_flippable():
    assert Solution().maxConsecutiveAnswers("TTFF", 2) == 4


def test_one_flip():
    assert Solution().maxConsecutiveAnswers("TFFT", 1) == 3


def test_longer():
    assert Solution().maxConsecutiveAnswers("TTFTTFTT", 1) == 5
