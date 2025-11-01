# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Test character from template
#define e = Character("Eileen")

define t = Character("Game Show Host:")
# define female characters
define g = Character("Goneril") #King Lear
    # Expressions: basic, talking, angry, smug

define i = Character("Isabella") #Measure for Measure
    # Expressions: basic, talking
define r = Character("Rosalind") #As You Like It
    # EXpressions: basic, talking

#define male characters
define h = Character("Hamlet") #Hamlet
    # Expressions: basic, talking, dramatic

define a = Character("Iago") #Othello
    # Expressions: basic, talking, winking

define b = Character("Bassanio") #Merchant of Venice
    # Expressions: basic, talking

$ LoveScore




# The game starts here.

label start:

    # Script here for the beginning of the dating show... also game mode selection... 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #displays a scene.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    #scene: Introduction to characters...

    #menu:
        
     #   "This is a menu test."

      #  "Click button 1":

       #     jump button1

        #"Click button 2":

         #   jump button2
label Introduction: 

    t "Welcome to the world's most dubious, wild, raunchy, and spiciest dating show: The Greatest Shakespeare Off!!!!!"

    t "Tonight we are visited by a most valuable cast, one I'm sure you have all seen before."

    t "For that purpose, to make matters interseting, they've hidden behind a curtain ready to answer your questions."

    t "Might our guests introduce themselves?"

    #Guest introductions

    scene curtain_background

    t "Good! Now we move onto the first phase of the game. You may ask questions all of our quests will answer."

    t "Afterwards, you'll pick your favorite, the one you desire most."

    t "With them you'll spend the rest of the nigt on a date, where they shall decide whether they wanna be with you."

    t "With no further ado; let the games begin!"





label QuestionTime:

    menu: 
        "Ask your questions to the contestants!"

        "What's your occupation?":
            jump Answers1
        "Where are you from?":
            jump Answers2
        "What do you look for in a partner?":
            jump Answers3
        "Do you have hobbies?":
            jump Answers4
        "Describe yourself with one word.":
            jump Answers5
        "What's your dream date?":
            jump Answers6
        "What's your biggest turn on?":
            jump Answers7
        "What's the most important thing in your life?":
            jump Answers8
        "No more questions...":
            jump AfterQuestions

#Question Answers Section ////////////////////

label Answers1:
    #Question: What's your occupation?

    scene CloseToCharacter

    show Goneril talking

    g "I'm the eldest daughter of the king of Britain."

    g "Going to be the queen. Looking for a man to stand beside me… or behind me."

    show Hamlet talking

    h "Just a student; A senior at Wittenberg."

    h "It's a shame I haven't seen you around though, would have made school less boring."

    show Isabella talking

    i "I'm practicing to be a nun in the Order of Saint Clare."
    
    i "I hope to fully join by the end of the year."

    show Iago talking

    a "I'm in the military. I can't say much else but let's just say it's important"
    
    show Iago winking

    a "I might tell you later tonight."

    show Bassanio talking

    b "Ex-soldier, ex-scholar, now I'm just having fun."

    b "You can slide if you want."

    show Rosalind talking

    r "Fleeing my country and looking for a long term situationship this vacay."

    
    jump QuestionTime


label Answers2: 
    #Question: Where are you from?

    show Goneril talking

    g "I'm a pure blood British royal, living it up in the most ostentatious, luxurious castle."

    g "We have a lot of spare beds, dear."

    show Hamlet talking

    h "Amidst this world's vilest wards and dungeons, I live in tis worst prison, Denmark."

    h "It sucks but perhaps you can make it heaven"

    show Isabella talking

    i "In a nunnery."

    show Iago talking

    a "Currently in Venice, but I have been all over the world and still haven't seen your bed, love"

    show Bassanio talking

    b "Venice! The biggest party city in the world and I'm looking for a fine shyt to party by my side."

    show Rosalind talking

    r "I'm hiding in the woods..."
    
    r "It's a nice place though, I love the natural lighting and the greenery."

    r "Many fun hideouts to explore."

    jump QuestionTime

label Answers3:
    #Question: What do you look for in a partner?

    show Goneril talking

    g "Submissive, easily manipulated charmers who stand at my beck and call"

    show Hamlet talking

    h "A person who I can trust above all else. Such a trait is rare in modern society."

    show Isabella talking

    i "A frequent church goer. Strong morals and piety are also good."

    show Iago talking

    a "A good listener who is non-opinionated and soft spoken. A pretty face couldn't hurt."

    show Bassanio talking

    b "A rich fellow who doesn't hide their looks and knows how to have a good time."

    show Rosalind talking

    r "Gentle, goody, respectable folk who can totally win a fight when needed to."

    
    jump QuestionTime

label Answers4:
    #Question: Do you have hobbies?

    show Goneril talking

    g "I have a thing for rare fragrances. I collect vials with all kind of oils, some deadly alluring."

    show Hamlet talking

    h "The uses of this world all feel so stale and flat to me. Everything grows to be a bore."

    show Isabella talking

    I "My sole devotion is prayer to our lord and savior Jesus Christ. He is the only man I'm on my knees for."

    show Iago talking

    a "I adore tha banter of a crowded night in the tavern. My fellows are bound to do no good on such a day."

    a "Trouble tends to follow them, quite entertaining trouble."

    show Bassanio talking

    b "I have many hobbies, and you could be one of them. But, besides you, I do love hitting the town with my buddies a good ol'wrestle never hurt nobody,"
    
    b "and of course I enjoy cracking open a couple of brewskys with my most inner circle."

    show Rosalind talking

    r "I love diving into a good book, especially poetry."
    
    r "A former lover of mine made sure that I'd be awakened to an ocean of romantic poems covering the forest's bark."

    jump QuestionTime


label Answers5:
    #Question: Describe yourself with one word

    show Goneril talking

    g "Powerful, exemplary, a diva, the fairest, hottest, richest woman in Britain. I could go on though."

    show Hamlet talking

    h "I'm naught but a rogue and peasant slave."

    show Isabella talking

    i "Pure."

    show Iago talking

    a "My friends call me honest but I prefer the term ambitious..."

    show Bassanio talking

    b "I'm an alpha, bro."

    show Rosalind talking

    r "Articulate. That's my favorite word, by the way."

    jump QuestionTime


label Answers6: 
    #Question: What's your dream date? 
    
    show Goneril talking

    g "We have a private dinner with exotic spices, a couple glasses of wine, and a long night ahead of us."

    show Hamlet talking

    h "Let's watch a play and go on a late night stroll. Plays are my fgavorite way to lay people bare."

    h "They can be quite revealing"

    show Isabella talking

    i "Attending church service. Brushing hands if we're dating."

    show Iago talking

    a "I bring you along for one of my work trips."

    a "Picture it: A private boat, two glasses of sctoch, and the open sea."

    show Bassanio talking

    b "A wild masquerade party with no one to keep track of the mischief behind the mask and the sheets."

    show Rosalind talking

    r "A forest picnic. I bring the bottle, you bring the log- I mean logs..."

    jump QuestionTime

label Answers7:
    #Question: What's your biggest turn on?

    jump QuestionTime

label Answers8: 
    #Question What's the most important thing in your life?

    show Goneril talking

    g "Bending people to my will, including you."

    show Hamlet talking

    h "I cannot reveal it at this time but it's a commandment that has wiped off all other matters within my mind, one I abide by my sword to follow"

    show Isabella talking

    i "The keys to my chastity belt."

    show Iago talking

    a "My work. As anyone can tell, I am the most fit to gain ranks, especially with you by my side."

    show Bassanio talking

    b "A potential influc of finances, specifically in my directoion... if you catch my drift ;)"

    show Rosalind talking

    r "Freedom, the ability to do as I please with whomever I choose."

    jump QuestionTime


# Question Answers Over ////////////////////

label AfterQuestions:

    menu: 
        "Are you ready to complete the question portion of the show?"

        "Yes, let's continue.":
            jump PickYourPartner

        "No, I have more questions":
            jump QuestionTime

label PickYourPartner:

    t "Questions are over! It's time to..."

    t "PICK"

    t "YOUR"

    t "DATE!!!"
    $ LoveScore = 0

    menu:

        "Choose the person you want to spend the rest of the night with."

        "Goneril":
            jump DateGoneril
        "Hamlet": 
            jump DateHamlet
        "Isabella":
            jump DateIsabella
        "Iago":
            jump DateIago
        "Bassanio":
            jump DateBassanio
        "Rosalind":
            jump DateRosalind

# Character Date Confirmation //////////

label DateGoneril:

    menu: 
        "Are you sure?"

        "Yes.":
            jump GonerilDate
            
        "No.":
            jump PickYourPartner

label DateHamlet:

    menu:
        "Are you sure?"

        "Yes.":
            jump HamletDate
        "No.":
            jump PickYourPartner

label DateIsabella:

    menu:
        "Are you sure?"

        "Yes.":
            jump IsabellaDate
        "No.":
            jump PickYourPartner

label DateIago:

    menu:
        "Are you sure?.... Like really sure?"

        "Yes.":
            jump IagoDate
        "No.":
            jump PickYourPartner

label DateBassanio:

    menu:
        "Are you sure?"

        "Yes.":
            jump BassanioDate
        "No.":
            jump PickYourPartner

label DateRosalind:

    menu:
        "Are you sure?"

        "Yes.":
            jump RosalindDate
        "No.":
            jump PickYourPartner

# End Character Date Confirmation /////////////////////


#Character Dates /////////////////////


# START GONERIL SECTION /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
label GonerilDate:

show Goneril basic

"A young woman walks around the curtain, head held high, nose prominent yet in a unique but intense beauty."

"Her eyes lock onto you in a sharp manner, raditating power; yet glistening with intrigue."

show Goneril talking

g "I suppose I'm supposed to introduce myself, I'm Goneril, future ruler of Britain."

g "You chose me obviously, so now I get see if I will choose you."

"Her eyes are daring you to speak against her words."

g "If given the opportunity, what would you do when faced with a choice between be and another, let's just say another person held high in the court?"

menu:
    
    "I would pick the future ruler of Britain- So you, obviously. ;) (+10)":
        $ LoveScore += 10
        jump GonerilQ1_1
    "It depends, what's in it for me? Would there potentially be another future ruler at your side? (+5)":
        $ LoveScore += 5
        jump GonerilQ1_2
    "If they were more attractive, then my eyes might slide to the next... (-10)":
        $ LoveScore -= 10
        jump GonerilQ1_3
        
label GonerilQ1_1:

    show Goneril smug

    g "Right choice, I better be the first in your eyes always."
    
    jump GonerilQ2

label GonerilQ1_2:

    show Goneril talking

    g "Hmm, I do admire your hunger for power, maybe... just maybe."
    
    jump GonerilQ2

label GonerilQ1_3:
    
    show Goneril angry

    g "A pigeon brain like yours wouldn't be able to keep up with myself even if you tried."
    
    jump GonerilQ2

label GonerilQ2:

    g "I see some potential in you, but I can't guarantee you anything. I have demands that must be met."

    g "So let's see if you can continue to meet them; or fail, to no one's surprise."

    menu:
        g "If I were to tell you I'm currently in a marriage while still gracing you with my presence, where would your mind stray?"

        "I must know more about this other lover who may take you away from me (0)":
            
            jump GonerilQ2_1
        "Why would you betray another who already loves you? I find that repulsive (-5)":
            $ LoveScore -= 5
            jump GonerilQ2_2
        "I like a woman who can play the board a little, but once you pick me I know you'll be satisfied. (+5)":
            $ LoveScore += 5
            jump GonerilQ2_3

label GonerilQ2_1:
    g "Don't fret, they will not be in the picture much longer."
    jump GonerilQ3

label GonerilQ2_2:
    g "I don't have to respond to you, I make my choices and don't have to defend myself."
    jump GonerilQ3

label GonerilQ2_3:
    g "I like your thinking, the power I hold filled of secrets would blow your mind"
    jump GonerilQ3

label GonerilQ3:
    g "If you can't get onboard with my chess game I have at play, you will be left behind a crumpled mess pushed off my board."
        
    g "I had... I mean I have a large family but a tragedy struck when a bottle of poison slipped into my sister's wine glass,"
        
    g "and my father passed due to the death of another sister and my powerful binding choices I made as a sacrifice to save myself."
 
    menu:
        g "I've been through a lot and I deserve the power to- I mean the opportunity to feel loved by another... what say you?"
            
        "I say you're out of your mind and need to seek some help. (-10)":
            $ LoveScore -= 10
            jump GonerilQ3_1
        "Who needs a whole family when you'd have me? (0)":
            # LoveScore no adjustment
            jump GonerilQ3_2
        "I find that quite attractive, you strive for ambition, that's the type of woman I need. (+10)":
            $ LoveScore += 10
            jump GonerilQ3_3

label GonerilQ3_1:

    show Goneril angry

    g "How dare you!"

    g "You better watch what you drink, I might just let a little something slip..."
    
    jump GonerilQ4

label GonerilQ3_2:

    show Goneril talking

    g "Hmm... I see your point, but I do love being admired by them."
    
    jump GonerilQ4

label GonerilQ3_3:

    show Goneril smug

    g "Glad we're on the same page... Could be good for my future..."

    "Goneril whispers under her breath, 'if you last that long...' "
    jump GonerilQ4

label GonerilQ4:
    g "You're giving me a lot to think about. I might need to hear more from you before I can trust you to enter my castle."

    menu:
        g "When I say I like control, does that scare you away? Or tug you closer to my side?"

        "I don't know, you in control doesn't scare me, but I don't see myself running towards it (0)":
            # LoveScore no adjustment
            jump GonerilQ4_1

        "I run from women in control, I believe I have to be in control, never the other way around. (-10)":
            $ LoveScore -= 10
            jump GonerilQ4_2

        "I wouldn't mind the idea of you in control; I could use someone telling me what to do. (+5)":
            $ LoveScore += 5
            jump GonerilQ4_3

label GonerilQ4_1:

    show Goneril talking

    g "Running towards me is the best choice and you shoudl know it."
    jump GonerilQ5

label GonerilQ4_2:

    show Goneril angry

    g "You should be scqared, who are you to think you'd be in control, I have the money AND the power."
    jump GonerilQ5

label GonerilQ4_3:

    show Goneril smug

    g "That's the right answer, good to see you thinking the right way."
    jump GonerilQ5

label GonerilQ5:   
    
    show Goneril talking

    g "I have one final quesiton for you, answer it correctly and who knows- maybe you'll get to take me out to the most lavish restaurant in Britain."

    menu:
        g "There is a lot of others with potential who have piqued my interest, what makes you worthy of my time?"
        
        "How do I know you're worth my time? I'm how stuff you know, you're lucky to speak to me (-5)":
            $ LoveScore -= 5
            jump GonerilQ5_1
        "I'm nice, I can listen, I love women who have money (so I don't have to buy anything), and I have a few party tricks up my sleeve. (0)":
            # LoveScore no adjustment
            jump GonerilQ5_2
        "I can easily bend to your wants and needs, I'll listen to you without complaining, I can offer all the time in the world to you, what else coudl you want from a partner? (+5)":
            $ LoveScore += 5
            jump GonerilQ5_3

label GonerilQ5_1:

    show Goneril angry

    g "You're crazy! Anyone in my presene should be counting the stars with how lucky they are to be around me,"
    
    g "I could have you thrown out for speaking to me that way."
    jump GonerilEndQuestions

label GonerilQ5_2:

    show Goneril talking

    g "Hmm a nice guy isn't awful but don't think I'll spoil you, it will always be the other way around, I don't have time for the poor."
    jump GonerilEndQuestions

label GonerilQ5_3:

    show Goneril smug

    g "You know exactly what I like to hear, you're a good smooth talking, I like that about you. (+5)"
    jump GonerilEndQuestions

label GonerilEndQuestions:


    if LoveScore >= 30:
        jump GonerilSuccess
    else:
        jump GonerilFailure


label GonerilSuccess:

    show Goneril smug

    g "Congratulations, I find myself tempted to welcome you into my presence and speak to me again."

    g "I'm ready to be wined and dined with the finest wine there is, I have a specialist coming to my castle to show me the finest poisons."

    "Since you won your date! (lucky you), You'll join Goneril at her castle concocting her most famous poisons and perfumes,"

    "with a private chef at your beck and call. Better follow her or you may be left behind..."
    
    jump StoryEndWin

label GonerilFailure:

    show Goneril angry

    g "I would thank you for your time but you just wasted mine."

    g "I wish to never see you again, and if I do you better watch what you drink... You're lucky to have spent this time with me,"

    g "I'll easily find another who actually has something to offer."

    jump StoryEndLose

# END GONERIL SECTION /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

label HamletDate:

label IsabellaDate:

label IagoDate:

label BassanioDate:

label RosalindDate:




label StoryEndWin:

    return #end game.

label StoryEndLose:

#End Character Dates ////////////////////////////

    return #end game.
