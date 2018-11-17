# TEST FILE
import pytest
from bowling import Game, Frame

def test_givenOpenFrame_whenGetScore_thenReturnVanillaScore():
    game = Game()
    game.addRoll(5)
    game.addRoll(4)
    
    gameScore = game.getScore()

    assert 9 == gameScore

def test_givenSpare_whenGetScore_thenAddNextRollToCurrentFrameScore():
    game = Game()
    game.addRoll(9)
    game.addRoll(1)
    game.addRoll(5)

    gameScore = game.getScore()

    assert 20 == gameScore

def test_givenSpareWithoutNextRoll_whenGetScore_thenScoreUnknown():
    game = Game()
    game.addRoll(9)
    game.addRoll(1)

    gameScore = game.getScore()

    assert 10 == gameScore

def test_givenSpares_whenGetScore_thenAddNextRollToEachFrameScore():
    game = Game()
    game.addRoll(9)
    game.addRoll(1)
    game.addRoll(5)
    game.addRoll(5)
    game.addRoll(7)

    gameScore = game.getScore()

    assert 39 == gameScore

if __name__ == '__main__':
    test_givenOpenFrame_whenGetScore_thenReturnVanillaScore()
    test_givenSpare_whenGetScore_thenAddNextRollToCurrentFrameScore()
