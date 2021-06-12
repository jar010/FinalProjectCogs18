"""A collection of function for doing my project."""

# https://youtu.be/myJ36xIR7Yg - this video sparked my interest and gave me ideas of what to implement in my code, such as making a quiz that was speciically multiple choice.

# https://youtu.be/yriw5Zh406s - this video helped me start the project and get familiar with the struture of how my project should run, along with the appropiate functions to use. I took great inspiration from their code written and implemented it in my project, such as the structure and methods, but I modified it to be my own game/quiz with my own questions and topics written.

# Overview - I used four def functions and I took inspiration from this from the youtube URL's above (https://youtu.be/yriw5Zh406s), as it helped me envision how my quiz should run smoothy with function first, then questions + answers afterwards.

'''I used primarily this video (https://youtu.be/yriw5Zh406s) to help me structure the code below with the methods they provided, I just modified it to be a finish the lyrics game'''

def finish_lyrics_quiz():
    
    attempts = []
    correct_attempts = 0
    lyrics_var = 1
    
    for key in music_quest:
        
        print("---------------")
        print(key)
        
        for mus in a_choices[lyrics_var - 1]:
            
            print(mus)
            
        #for this code below, its function is to provide answer choices and iterate between the choices and you input your response.
            
        guess = input("CHOOSE (A, B, or C): ")
        guess = guess.upper()
        attempts.append(guess)
        
        #this function below is so that the code adds a pointfor every time the answer is guessed correctly and checks it as correct or not
        
        correct_attempts += check_answer(music_quest.get(key), guess)  
        lyrics_var += 1
        
    show_score(correct_attempts, attempts)
        
def check_answer(answer, guess):
    
    if answer == guess:
        
        #the function below is essentially the player getting 1 or 0 points depending if they got it right, using if and else statements.
        
        print("YAY, YOU GUESSED RIGHT!")
        return 1
    
    else:
        print("SORRY, LETS TRY AGAIN :)")
        return 0
    
    
    
def show_score(correct_attempts, attempts):
    print("-------------")
    print("RESULTS")
    print("-------------")
    
    
    print("Answers: ", end="")
                  
    for musi in music_quest:
        
        print(music_quest.get(musi), end=" ")
    print()
    
    
    print("Attempts: ", end="")
    
    for music in attempts:
        print(music, end=" ")
    print()
    
    #This code below calculates the final score and displays the result from 1-100% (int) depending on how well the player did on the quiz.
    
    score = int((correct_attempts/len(music_quest))*100)
    
    print("Your Score Is: "+str(score)+"%")
    
    """I thought the concept of using the play again part of my quiz would be a good idea and this video as cited before (https://youtu.be/yriw5Zh406s) gave me the idea to implement it, just as a real fun and cool game would!"""

def start_over():
    
    response = input("Would You Like To PLay Again? (Y or N): ")
    response = response.upper()
    
    if response == "Y":
        return True
    else: 
        return False

music_quest = {
    
"Finish the lyric! >>> And I watched as you fled the scene, doe-eyed as you buried me...?: ": "B",
    
"Finish the lyric! >>> And I'm highly suspicious that everyone who sees you wants you-I've loved you...?: ": "A",
    
"Finish the lyric! >>> Look up, out of your window-see snow, won't let it in though, leave home, feel the...?: ": "C",
 
"Finish the lyric! >>> I just miss your accent and your friends, did you know I stll...?: ": "A",

"Finish the lyric! >>> Is it alright to feel this way so early? and in my blood, all the sweet nothings fallin' in love...?: ": "C",

"Finish the lyric! >>> Man, I hate this part of Texas,-- close my eyes, fantasize...?: ": "A",

"Finish the lyric! >>> Because ours are the moments I play int he dark, we were wild and...?: ": "B",
    
"Finish the lyric! >>> Pass around the lampshade, there'll be plenty enough room in...?: ": "A",

"Finish the lyric! >>> I think I'll pace my apt a few times, and fall asleep on the couch--wake up early to...?: ": "C",
 
"Finish the lyric! >>> 'cause there's nothing like it, locking my eyes with you--I can't fight it, splitting my...?: ": "C"
    
}

a_choices = [["A. one heart broke, two hands bloody", "B. one heart broke, four hands bloody", "C. my heart broke, for you honey"],
          ["A. three summers now honey, but I want 'em all", "B. every summer now honey, but I want 'em all", "C. all summer now honey, but I want 'em all"],
          ["A. wind go", "B. wind know", "C. wind blow"],
          ["A. talk to them", "B. walk with them", "C. hang with them"],
          ["A. every night", "B. with you feel right", "C. overnight"],
          ["A. three clicks and I'm home", "B. one call and I'm home", "C. two clicks and I'm home"],
          ["A. aggressive, come home to my heart", "B. fluorescent, come home to my heart", "C. adjacent, come home to my heart"],
          ["A. jail", "B. hell", "C. the well"],
          ["A. bird chriping", "B. music playing loud", "C. black and white re-runs"],
          ["A. heart in two", "B. soul in two", "C. mind in two"]]


finish_lyrics_quiz()

while start_over():
     
    music_game()
    
print("C YA LATER!:")