"""Test for my functions.
"""

from functions import *

## the tests below check to see if the code checks the answers and adds point or none at all depending on the response.

def test_finish_lyrics_quiz(): 

    assert callable(music_quest)
    assert callable(a_choices)

def test_check_answer():

    assert callable(check_answer(1))
    assert callable(check_answer(0))
    assert callable("YAY, YOU GUESSED RIGHT!") == check_answer(2)
    assert callable("SORRY, LETS TRY AGAIN :)") == check_answer(10)
    
## the functions below returns a start over option and shows the ability to play again or not; as well as the number of correctness from the questions answered.
    
def test_show_score():

    assert (correct_attempts(10))
    assert (correct_attempts(50))
    assert (correct_attempts(100))
    assert "Your Score Is: "+str(score)+"%" == correct_attempts(10)
    
def test_start_over():

    assert start_over
    assert a_choices
    assert ("C YA LATER!:") == finish_lyrics_quiz()
    



                 
    