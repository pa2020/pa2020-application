import pytest
from main.src.utils.tweet import clearTweet


def test_clearTweet():
    text = 'We have NOT all the sameeeeeeeeeee ! 😂 ;) https://www.google.fr/ @Tino'
    assert clearTweet(text) == 'we have not all the samee smiley'
