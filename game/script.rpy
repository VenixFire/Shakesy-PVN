# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Test character from template
#define e = Character("Eileen")

image curtain_background = "curtain.jpg"

define t = Character("Game Show Host:")
# define female characters
define g = Character("Goneril") #King Lear
    # Expressions: basic, talking, angry, smug

image Goneril smug = "Goneril_Smug.png"
image Goneril talking = "Goneril_talking.png"
image Goneril angry = "Goneril_upset.png"

define i = Character("Isabella") #Measure for Measure
    # Expressions: basic, talking, smile

define r = Character("Rosalind") #As You Like It
    # EXpressions: basic, talking, yell, smile, upset

image Rosalind smile = "Rosalind smile.png"
image Rosalind talking = "Rosalind talking.png"
image Rosalind yell = "Rosalind yell.png"
image Rosalind upset = "Rosalind upset.png"

define gany = Character("Ganymeade") #Rosalind
    # Expressions: talking, smile, upset, yell

image Ganymeade smile = "Ganymeade smile.png"
image Ganymeade talking = "Ganymeade talking.png"
image Ganymeade yell = "Ganymeade yell.png"
image Ganymeade upset = "Ganymeade upset.png" 

#define male characters
define h = Character("Hamlet") #Hamlet
    # Expressions: basic, talking, dramatic, freaked, smile

image Hamlet talking = "Hamlet_talking.png"
image Hamlet dramatic = "Hamlet_Dramatic.png"
image Hamlet freaked = "Hamlet_freaked.png"
image Hamlet smile = "Hamlet_smile.png"


define a = Character("Iago") #Othello
    # Expressions: basic, talking, winking, annoyed, smug

image Iago smug = "Iago_smug.png"
image Iago talking = "Iago_talking.png"
image Iago winking = "Iago_smug.png"
image Iago annoyed = "Iago_annoyed.png"

define b = Character("Bassanio") #Merchant of Venice
    # Expressions: basic, talking, yurr, unimpressed

image Bassanio talking = "Bassanio_talking_nobg.png"
image Bassanio unimpressed = "Bassanio_unimpressed.png"
image Bassanio yurr = "Bassanio_yurr_nobg.png"

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

    "Welcome to our project! This game is a demo/prototype using the Ren'Py Visual Novel Engine. If you want to play this game pass the team your email and we'll send you download instructions!"

    "This game is in an incomplete state and is missing assets and may contain bugs."

    "Ok! Time to play!"

    "......"

    scene curtain_background

    t "Welcome to the world's most dubious, wild, raunchy, and spiciest dating show: The Greatest Shakespeare Off!!!!!"

    t "Tonight we are visited by a most valuable cast, one I'm sure you have all seen before."

    t "For that purpose, to make matters interseting, they've hidden behind a curtain ready to answer your questions."

    t "Might our guests introduce themselves?"

    #Guest introductions


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
        "What's the most important thing in your life?":
            jump Answers8
        "No more questions...":
            jump AfterQuestions

#Question Answers Section ////////////////////

label Answers1:
    #Question: What's your occupation?


    g "I'm the eldest daughter of the king of Britain."

    g "Going to be the queen. Looking for a man to stand beside me… or behind me."


    h "Just a student; A senior at Wittenberg."

    h "It's a shame I haven't seen you around though, would have made school less boring."


    i "I'm practicing to be a nun in the Order of Saint Clare."
    
    i "I hope to fully join by the end of the year."


    a "I'm in the military. I can't say much else but let's just say it's important"
    

    a "I might tell you later tonight."


    b "Ex-soldier, ex-scholar, now I'm just having fun."

    b "You can slide if you want."


    r "Fleeing my country and looking for a long term situationship this vacay."

    
    jump QuestionTime


label Answers2: 
    #Question: Where are you from?


    g "I'm a pure blood British royal, living it up in the most ostentatious, luxurious castle."

    g "We have a lot of spare beds, dear."


    h "Amidst this world's vilest wards and dungeons, I live in tis worst prison, Denmark."

    h "It sucks but perhaps you can make it heaven"


    i "In a nunnery."


    a "Currently in Venice, but I have been all over the world and still haven't seen your bed, love"


    b "Venice! The biggest party city in the world and I'm looking for a fine shyt to party by my side."


    r "I'm hiding in the woods..."
    
    r "It's a nice place though, I love the natural lighting and the greenery."

    r "Many fun hideouts to explore."

    jump QuestionTime

label Answers3:
    #Question: What do you look for in a partner?


    g "Submissive, easily manipulated charmers who stand at my beck and call"


    h "A person who I can trust above all else. Such a trait is rare in modern society."


    i "A frequent church goer. Strong morals and piety are also good."


    a "A good listener who is non-opinionated and soft spoken. A pretty face couldn't hurt."


    b "A rich fellow who doesn't hide their looks and knows how to have a good time."


    r "Gentle, goody, respectable folk who can totally win a fight when needed to."

    
    jump QuestionTime

label Answers4:
    #Question: Do you have hobbies?


    g "I have a thing for rare fragrances. I collect vials with all kinds of oils, some deadly alluring."


    h "The uses of this world all feel so stale and flat to me. Everything grows to be a bore."


    i "My sole devotion is prayer to our lord and savior Jesus Christ. He is the only man I'm on my knees for."


    a "I adore the banter of a crowded night in the tavern. My fellows are bound to do no good on such a day."

    a "Trouble tends to follow them, quite entertaining trouble."


    b "I have many hobbies, and you could be one of them. But, besides you, I do love hitting the town with my buddies a good ol'wrestle never hurt nobody,"
    
    b "and of course I enjoy cracking open a couple of brewskys with my most inner circle."


    r "I love diving into a good book, especially poetry."
    
    r "A former lover of mine made sure that I'd be awakened to an ocean of romantic poems covering the forest's bark."

    jump QuestionTime


label Answers5:
    #Question: Describe yourself with one word


    g "Powerful, exemplary, a diva, the fairest, hottest, richest woman in Britain. I could go on though."


    h "I'm naught but a rogue and peasant slave."


    i "Pure."


    a "My friends call me honest but I prefer the term ambitious..."

    b "I'm an alpha, bro."


    r "Articulate. That's my favorite word, by the way."

    jump QuestionTime


label Answers6: 
    #Question: What's your dream date? 
    

    g "We have a private dinner with exotic spices, a couple glasses of wine, and a long night ahead of us."


    h "Let's watch a play and go on a late night stroll. Plays are my fgavorite way to lay people bare."

    h "They can be quite revealing"


    i "Attending church service. Brushing hands if we're dating."


    a "I bring you along for one of my work trips."

    a "Picture it: A private boat, two glasses of sctoch, and the open sea."


    b "A wild masquerade party with no one to keep track of the mischief behind the mask and the sheets."


    r "A forest picnic. I bring the bottle, you bring the log- I mean logs..."

    jump QuestionTime


label Answers8: 
    #Question What's the most important thing in your life?


    g "Bending people to my will, including you."


    h "I cannot reveal it at this time but it's a commandment that has wiped off all other matters within my mind, one I abide by my sword to follow"


    i "The keys to my chastity belt."


    a "My work. As anyone can tell, I am the most fit to gain ranks, especially with you by my side."


    b "A potential influc of finances, specifically in my directoion... if you catch my drift ;)"


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
        "Isabella (Unfinished Art)":
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

show Goneril smile

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

    "You answered below Goneril's interest level, I must ask you to say your goodbyes and leave. (If she'll give you any more time.)"

    jump StoryEndLose

# END GONERIL SECTION /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

label HamletDate:

    show Hamlet smile

    "A young man leaves the curtains. His face is handsome and yet weary; his eyes are particulary tired, darkly adorned by eyebags."

    "He gazes at the audience paranoically until his eyes turn to you. His mouth turns into coy smile as he greets you."

    show Hamlet talking

    h "It's pleasure to meet you. The name is Hamlet."

    h "I suppose it's time for me to understand whether or not it's worth it for me to ally myself to your person."

label HamletQ1:

    h "Are you in any way affilated with the current king of Denmark?"

    menu:
        "His eyes tighten as he waits for your answer?"

        "King Claudius? I would never affiliate myself with that geezer. (+10)":
            $ LoveScore += 10
            jump HamletQ1_1
        "Denmark?? I never heard of her. (-10)":
            $ LoveScore -= 10            
            jump HamletQ1_2
        "I don't know what you are talking about, the only things I want to affiliate myself with are your pants haha.":
            $ LoveScore += 5
            jump HamletQ1_3

label HamletQ1_1:

    show Hamlet talking

    h "He is a wretch. Our temperaments align in that matter."
    
    "His smile feels more trusting than it was before."

    jump HamletQ2

label HamletQ1_2:

    show Hamlet dramatic

    h "You are obviously lying. There is a kind of confession in your looks which your modesties have not craft enough to color"

    jump HamletQ2

label HamletQ1_3:

    show Hamlet talking

    h "Your response is much too avoidant for my liking. Still, there is some value in your words, despite their bashfulness... "

    jump HamletQ2

label HamletQ2:

    h "Wait."

    h "Do you hear it? The cries of my father? His bellowing voice demanding revenge?"

    menu:
        h "Swear by my sword! You won't tell anyone about what you hear tonight, right? You hear the voice right??"

        "The ghost of your father? I see... I'll swear, just stop screaming. (+0)":
            # LoveScore Unchanged.
            jump HamletQ2_1
        "Oh I'll touch your sword all right. (+10)":
            $ LoveScore += 10 #no fucking way lmfaoooo
            jump HamletQ2_2
        "What voice? (-10)":
            $ LoveScore -= 10
            jump HamletQ2_3

label HamletQ2_1:

    show Hamlet freaked

    h "You doubt me? I vow to you that this apparition is real. You can rest easy as you swear, I promise."

    jump HamletQ3

label HamletQ2_2:

    show Hamlet talking

    h "Good. It is done. Rest, rest,  perturbèd spirit, they have sworn."

    h "I express my love toward thy gesture"

    jump HamletQ3

label HamletQ2_3:

    show Hamlet dramatic

    h "Swear! You hear it do you not? It resounds so strongly over our stage..."

    jump HamletQ3

label HamletQ3:

    show Hamlet talking

    h "I pologize for the outburst." 
    
    h "This is a pressing matter and there are too many eyes watching us at the moment."

    "Hamlet approaches you, leaning his face toward your ears. He whispers."

    h "The truth is I'm pretending to be crazy. My uncle mustn't know I plan on killing him!"

    h "My father's ghost has told me he was poisoned by my uncle! I must take revenge!!"

    h "And for that reason, you need to go along with this."

    h "As I pretend to be crazy on the game show, I'll lead the cronies of the court astray! I'm just pretending! Trust me!"

    menu:
        "trust him?"

        "I'm calling the cops (+0)":
            #LoveScore unchanges
            jump HamletQ3_1
        "Oh so you are not actually crazy, you are just pretending to be crazy because your dead dad's ghost has told you that your uncle killed him and now you need to avenge him... That makes perfect sense! (+10)":
            $ LoveScore += 10
            jump HamletQ3_2
        "So you're crazy and hot, the night couldn't get better. (-5)":
            $ LoveScore -= 5
            jump HamletQ3_3

label HamletQ3_1:

    show Hamlet freaked

    h "No! We can't let them know about Claudis' plan yet. Call them after I figure out more about it"

    jump HamletQ4

label HamletQ3_2:

    show Hamlet talking 

    h "Yeah, that's it!"

    jump HamletQ4

label HamletQ3_3:

    show Hamlet freaked

    h "I'm just pretending! I'm not crazy!!!"

label HamletQ4:

    h "So… You come here often?" 

    menu:
        "Hamlet tries to play along to the show and fails miserably. He looks at you expecting a reply."

        "No. (-5)":
            $ LoveScore -= 5
            jump HamletQ4_1
        "Yeah, going to dating shows is something I do on a regular basis.":
            # LoveScore Unchanged
            jump HamletQ4_2
        "Hamlet, doubt thou the stars are fire, doubt that the sun doth move, doubt truth to be a liar, but never doubt I love (+10)":
            $ LoveScore += 10
            jump HamletQ4_3


label HamletQ4_1:
    
    show Hamlet dramatic

    h "Oh, I see." 

    "Hamlet looks down to the ground."

    jump HamletQ5

label HamletQ4_2:

    show Hamlet talking

    h "Huh, I didn't peg you as the type."

    jump HamletQ5

label HamletQ4_3:

    show Hamlet smile

    h "I am smitten! Your words ignite a fire within my heart."

    jump HamletQ5

label HamletQ5:

    h "This dating show thing has been fun and all but there is one question that holds most valuable."

    h "My one chief task, the only one I must take, one I have engraved upon my mind above all else must be accomplished. Will you help me or stand in my way?"

    menu: 

        "Let's kill that old man. (+10)":
            $ LoveScore += 10
            jump HamletQ5_1
        "Dude killing people is not cool. You are sick in the head, this is not what you should be doing. Hamlet you need a psychologist. (-10)":
            $ LoveScore -= 30
            jump HamletQ5_2
        "Don't make me a part of this. We can still kiss though. (+5)":
            $ LoveScore += 5
            jump HamletQ5_3

label HamletQ5_1:

    show Hamlet smile

    h "You get it! Let's do it!!"

    jump HamletEndQuestions

label HamletQ5_2:

    show Hamlet dramatic

    h "So you really don't believe me...? I guess this will never work out..."

    jump HamletEndQuestions

label HamletQ5_3:

    show Hamlet talking

    h "Your neutral non-chalant approach toward this matter is not wholly unpleasant to me."

    jump HamletEndQuestions

# HAMLET END QUESTIONS /-/-/-/-/-/-/--//-/-/-/-/-/--/-/-/-/-//---///-/-/--/-

label HamletEndQuestions:

    h "I have made my choice. I know whether or not you shall come with me to Denmark tonight"

    if LoveScore >= 30:
        jump HamletSuccess
    else:
        jump HamletFailure


label HamletSuccess:

    show Hamlet smile

    h "I have grown fond of you. Your smile, your humour, your trust upon mine vengeance, they shall propel me forward."

    h " Let us move toward Denmark posthaste!"

    "Hamlet holds your hand as the two of you run out of the show. Soon enough the two of you take a boat toward Denmark."

    "Throughout the journey you spend long, frisky nights together on the boat. Some pirates hijack the trip and they join in on the fun. It was an amazing pleasure filled ride"

    "When you get to Denmark, Hamlet finds out his ex is dead and the mood immediately plummets"

    "The whole thing devolves into a brawl between Hamlet and the ex’ brother in a court audience with the king."

    "Hamlet and the brother stab themselves, the queen dies from poison and you find out king Claudius had plotted all of this. "

    "Before dying, Hamlet performs a beautiful soliloquy and kisses you in the mouth. Tragic. At least you got to kill the king. "

    jump StoryEndWin

label HamletFailure:

    show Hamlet talking

    h "You have proven to be most untrustworthy"

    "Hamlet brandishes his sword. It glistens through the show’s lighting, He glares at you with a threatening scowl."

    show Hamlet freaked
    
    h "Leave now or I shall treat you as an enemy. We should not meet ever again."

    "Hamlet seriosity preemptively empties the show. No one desires to see him having a mental breakdown and you soon quit it too."

    "You live the rest of your days in the same manner you had ever done. Your meeting with Hamlet was but a fleeting moment in your life, one you would rather forget."

    "Later on, you read about a bloodbath that happened in Denmark. Hamlet and many others have died in a tragic accident."

    "Perhaps it was good that you never started dating him. Tragedy would have soon taken you too. "
        
    jump StoryEndLose

# END HAMLET



# START ISABELLA
label IsabellaDate:

    show Isabella smile

    "The curtain draws to reveal a younger woman dressed head to toe in a black nun outfit, white outlining her face as an undergarment."

    "Her eyes shine bright as her defining feature standing out in contrast to the black that wraps around her."

    "Her face is more serious with a slight upturn of her lips, as she greets you for the first time..."

    show Isabella talking

    i "Hello, I'm Isabella. It's nice to put face to the voice I've been listening to. I do have a couple questions to ask you to see if we'd be a good fit."

    i "One thing you must know is that I cherish honesty and moral integrity, with that being said..."


label IsabellaQ1:

    i "I hold dear to me my sense of honor and nobility, have you ever gone against your own honor/beliefs for someone you loved?"

    i " I once was asked to do so and my opinion on them was changed."

    menu:
        "Have you ever gone against your own honor/beliefs for someone you loved?"

        "I'm sorry that was asked of you, and yes I have had someone ask the same. I followed my beliefs and honor and stayed true to myself. (+5)":
            $ LoveScore += 5
            jump IsabellaQ1_1
        "If I loved them enough I would, I mean my sense of honor isn't above those I love":
            # LoveScore Unchanged
            jump IsabellaQ1_2
        "It would have to depend on what's asked of me, but honestly that's too deep of a question and I'm not going to reveal something like that to you":
            $ LoveScore -= 5
            jump IsabellaQ1_3

label IsabellaQ1_1:

    show Isabella smile

    i "Thank you, yes it was a challenge but I overcame it."

    i " I like the sense of honor and believing in yourself to be who you are rather than change for another... Wondering if you'd ever change for me though?"

    jump IsabellaQ2

label IsabellaQ1_2:

    show Isabella upset 

    i "What if it was something that ran deeper than you'd want? Something that would change you for good? Not a bad answer but not an amazing one either"

    jump IsabellaQ2

label IsabellaQ1_3:

    show Isabella upset

    i "It's deep but important. If you can't answer honestly, I don't think we'll see eye to eye..."

    jump IsabellaQ2


label IsabellaQ2:

    show Isabella talking

    i "Well, that was a good look into who you are, I feel like I just scratched the surface and definitely want to know more about your thoughts.. and a few other things ;)"

    menu: 
        i "How much is physical attraction necessary for you? Say if passion was second in line to integrity and chastity?"

        "If they aren't up to my standards, goodbye! (-10)":
            $ LoveScore -= 10
            jump IsabellaQ2_1
        "I mean beauty can't hurt, but the respect one must hold to look within and strive for their moral compass is a good quality to have (+5)":
            $ LoveScore += 5
            jump IsabellaQ2_2
        "Physical attraction is surface level, what matters is what they have within. If they pride themselves on their moral compass and chastity and continue to hold true to themselves that is all I'd want. (+10)":
            $ LoveScore += 10
            jump IsabellaQ2_3

label IsabellaQ2_1:

    show Isabella upset

    i "Oh, so say then this person you love deeply and has all your dream qualities yet isn't up to your standards, you'd send them away? How unfortunate, it must be hard being alone all the time then."

    jump IsabellaQ3

label IsabellaQ2_2:

    show Isabella talking

    i "True beauty is easily appreciated but one's respect for themselves is clearly more important, at least you can try and understand."

    jump IsabellaQ3

label IsabellaQ2_3:

    show Isabella smile

    i "wow, your honesty is mesmerizing me"

    jump IsabellaQ3

label IsabellaQ3:

    show Isabella talking 

    i "I'm glad we can get a few of my more serious questions out of the way, now to ask you some more meaningful questions. Remember all I ask is honesty from you."

    menu:
        i "How thin is your line in perception of sin vs. passion?... Asking for a friend of course!"

        "Good question, that line will be extremely thick and passion will clearly stay on one side and sin will stay far away from my soul and body. (+5)":
            $ LoveScore += 5
            jump IsabellaQ3_1
        "There is no line, and that line will be crossed without a second thought. (-10)":
            $ LoveScore -= 10
            jump IsabellaQ3_2
        "There of course is a line, but if I were given the keys to your chastity belt.. things could get a smidge hazy. (+10)":
            $ LoveScore += 10
            jump IsabellaQ3_3

label IsabellaQ3_1:

    show Isabella talking

    i "I'm glad you understand the line and give space for said line. So there's no way around that thick line you just drew?"

    jump IsabellaQ4

label IsabellaQ3_2:

    show Isabella upset

    i "I see, you don't exactly fit my thoughts on this line."

    jump IsabellaQ4

label IsabellaQ3_3:

    show Isabella smile 
    
    i "Your candor is appreciated, I will take that into consideration.. ;)"

    jump IsabellaQ4

label IsabellaQ4:

    show Isabella talking

    i "I will have to say, you have to keep this between us of course but if you continue to or start answering my questions correctly, you'd have the keys to my chastity (It's not gonna be locked for that long.. potentially)"

    menu:
        i "Do you have any siblings, if so how far would you go for them? Would you go against them?"

        "I do have a sibling, and I would go pretty far for them as long as I stay within reach of my morals which I stand strong for. (+10)":
            $ LoveScore += 10
            jump IsabellaQ4_1
        "I  would go kinda far, but honestly I'd rather just let them solve things for themselves, love them but it can be a lot. (+0)":
            $ LoveScore += 0
            jump IsabellaQ4_2
        "I don't have any siblings, and if I did I'd only look out for myself honestly. (-5)":
            $ LoveScore -= 5
            jump IsabellaQ4_3

label IsabellaQ4_1:

    show Isabella smile

    i "hmm I find myself agreeing with you, glad we can agree and stay on the same page... my keys are getting closer to being yours."

    jump IsabellaQ5

label IsabellaQ4_2:

    show Isabella talking

    i "I can understand what you're saying, they should try and figure it out themselves, but sometimes you must lean on those around you or those above in the heavens..."

    jump IsabellaQ5

label isabellaQ4_3:

    show Isabella upset

    i "So an only child, if that wasn't obvious before it certainly is now, quite self centered if I must say."

    jump IsabellaQ5

label IsabellaQ5:

    show Isabella talking

    i "I have one final question for you, I feel like I've slowly started to open your doors and see within. I must say I’ve learned a lot and maybe just maybe you’ll get lucky and we can spend a lovely evening walking the gardens outside my church."

    menu:
        i "When you think of taking me out, where would you take me? (are the keys with us potentially?"

        "I would have to take you to this tavern that I love! The music is insane, the vibe inside is immaculate, and you might for once find yourself letting loose. (-10)":
            $ LoveScore -= 10
            jump IsabellaQ5_1
        "Hmm I have this spot I like to go to when I'm thinking, no one's ever been there before, you'd be the first girl I'd take there.. (-5)":
            $ LoveScore += 5
            jump IsabellaQ5_2
        "I know these beautiful statues we can look at near a church you may love, and we can end the evening sharing a delicious meal with a view of the surrounding mountains. It will be a slight walk from the church so we can keep things away from any moral issues. (+10)":
            $ LoveScore += 10
            jump isabellaQ5_3

label IsabellaQ5_1:

    show Isabella upset

    i "Unfortunately I would have to disagree with that idea, sounds like my kind of nightmare."

    jump IsabellaEndQuestions

label IsabellaQ5_2:

    show Isabella talking

    i "At least you're trying to make me feel special. Though how can I believe you?"

    jump IsabellaEndQuestions

label IsabellaQ5_3:

    show Isabella smile

    i "That sounds like quite a lovely evening, I can easily see this working."

    jump IsabellaEndQuestions

label IsabellaEndQuestions:

    if LoveScore >= 30:
        jump IsabellaSuccess
    else:
        jump IsabellaFailure

label IsabellaSuccess:

    show Isabella smile

    "You answered enough questions correctly to peak Isabella's interest!"

    i "I'm really happy we are going to speak, I'd love you to accompany me to these lovely gardens where we can continue to discuss our morals and beliefs."

    jump StoryEndWin

label IsabellaFailure:

    show Isabella upset

    "Unfortunately Isabella does not see this as a match."

    i "Thank you for your time, but I don't see us working out. I have more standards in myself than I’d trust to be around you, I think you could use a little growth before we'd even begin to work out."

    jump StoryEndLose





# END ISABELLA
        
label IagoDate:

    show Iago smug

    "An older man with a  tall and muscular build. He wears his long hair in a clean and sophisticated bun. His face is constantly in an etiquette yet question manner, as if constantly thinking of his next move."

    " A clean attire and almost completely shaven face, with a sharp mustache and goatee framing his jaw. The clothes loosely fit his frame while still allowing others to see his strength, garnished with a delicate flower."


    show Iago talking
    menu: 
        a "Would you stand by my side no matter what?"

        "Of course, you always stand with those you love. (+10)":
            $ LoveScore += 10
            jump IagoQ1_1
        "Depends on what it is. (-10)":
            $ LoveScore -= 10
            jump IagoQ1_2
        "Only if you stand by mine. (0)":
            $ LoveScore += 0
            jump IagoQ1_3

label IagoQ1_1:

    show Iago smug

    a "Good, smart answer."
    jump IagoQ2

label IagoQ1_2:

    show Iago annoyed

    a " You seem too hesitant, I don't like that."
    jump IagoQ2

label IagoQ1_3:

    show Iago talking

    a "You're clever, maybe too clever."

    jump IagoQ2

label IagoQ2:

    show Iago talking

    menu: 
        a "Are people still good, if they commit heinous acts for good reasons?"

        "Only if those acts are equivalent to what they are against. (0)":
            $ LoveScore += 0
            jump IagoQ2_1
        "No, people are only good if they become the bigger person. (-10)":
            $ LoveScore -= 10
            jump IagoQ2_2
        "If someone wrongs you, then you have the right to get them back. (+10)":
            $ LoveScore += 10
            jump IagoQ2_3


label IagoQ2_1:

    show Iago talking

    a "That is all up to opinion, is it not?"

    jump IagoQ1_3

label IagoQ2_2:

    show Iago annoyed

    a "That mindset is weak."

    jump IagoQ1_3

label IagoQ2_3:

    show Iago smug

    a "A true leader's understanding."

    jump IagoQ3

label IagoQ3:

    show Iago talking

    menu: 
        a "Do you think love is about connection, or control?"

        "It is always about connection, if you are controlling them, then that isn't real love. (-10)":
            $ LoveScore -= 10
            jump IagoQ3_1
        "If you control them in a matter that helps them, then I say that it is both. (0)":
            $ LoveScore += 0
            jump IagoQ3_2
        "If you can't control them, then they don't trust you, and a relationship is all about trust.":
            $ LoveScore  += 10
            jump IagoQ3_3

label IagoQ3_1:

    show Iago annoyed

    a "What do you truly know about love then?"

    jump IagoQ4

label IagoQ3_2:

    show Iago talking

    a "I am a very helpful man."

    jump IagoQ4

label IagoQ3_3:

    show Iago smug

    a "Exactly, if you trust me, then let me lead."

    jump IagoQ4

label IagoQ4:

    show Iago talking

    menu:
        a "How much of yourself would you give up, if it meant you would be chosen?"

        "I wouldn't give anything about myself up, if I did, then who would I even be. (0)":
            jump IagoQ4_1
        "Everything, I want to be seen. (-10)":
            $ LoveScore -= 10
            jump IagoQ4_2
        "Only what I can live without. (+10)":
            $ LoveScore += 10
            jump IagoQ4_3

label IagoQ4_1:

    show Iago talking

    a "Dire circumstances cause dire sacrifices."
    jump IagoQ5

label IagoQ4_2:

    show Iago annoyed

    a "Weakness isn't cute."
    jump IagoQ5

label IagoQ4_3:

    show Iago smug

    a "I like that you can wage for power."
    jump IagoQ5

label IagoQ5:

    show Iago talking

    menu: 
        a "When people look at me, they see a man who's simple. Do you fall for people's images or what lies beneath?"

        "I never fall for either as someone's true character will always shine through in the end. (-10)":
            $ LoveScore -= 10
            jump IagoQ5_1
        "Those who fall for someone's image, are right where they belong. (+10)":
            $ LoveScore += 10
            jump IagoQ5_2
        "I try to look past their faces, but sometimes I can become stuck. (0)":
            jump IagoQ5_3

label IagoQ5_1:

    show Iago annoyed

    a "You are very confident, aren't you?"
    jump IagoEndQuestions

label IagoQ5_2:

    show Iago smug

    a "I can tell you have a lot of layers to yourself."
    jump IagoEndQuestions

label IagoQ5_3:

    show Iago talking

    a "Just like a fly in honey."
    jump IagoEndQuestions


label IagoEndQuestions:

    if LoveScore >= 30:
        jump IagoSuccess
    else:
        jump IagoFailure


label IagoFailure:

    show Iago upset

    "You failed to romance Iago. Once the timer for questions dings Iago leaves the room."

    "You're left standing alone in your spot, feeling almost better than you did before knowing Iago is going to leave and you'll never see him again."

    jump StoryEndLose
label IagoSuccess:

    show Iago smug

    "As the question period ends Iago approaches you and takes your hand, leading you behind the stage."

    "You have successfully romanced Iago"
    jump StoryEndWin


# END IAGO

# START BASSANIO


label BassanioDate:

    show Bassanio smile

    "A tall man, with a muscular build. Not too many thoughts behind his eyes, but a spark of fiery life. A 24/7 smirk lies across his face as he stands shirtless, showing off his best assets. His brown messy hair lays across his face, framing just enough, so you can never see the full picture."

label BassanioQ1: 

    show Bassanio talking
    menu:
        b "Would you still love me if I lost my 6-pack?"

        "Absolutely not, your personality means more than abs ever could. (- 10)":
            $ LoveScore -= 10
            jump BassQ1_3
        "Lowkey... Yeah. (0)":
            $ LoveScore -= 0
            jump BassQ1_2
        "Trick question, you'll never lose your abs. (+ 10)":
            $ LoveScore += 10
            jump BassQ1_1

label BassQ1_1: 

    show Bassanio unimpressed

    b "Ahhh, I love that...not."

    jump BassQ2

label BassQ1_2:

    show Bassanio talking

    b "Understandable, me too."

    jump BassQ2

label BassQ1_3:

    show Bassanio smile

    b "Ding Ding, you are smart as you are pretty."

    jump BassQ2

label BassQ2:

    show Bassanio talking

    menu: 
        b "Wouldst thou be impressed if my horse were, how do you say, metaphorical?"

        "Soooo, you're broke. (0)":
            jump BassQ2_1
        "Wouldst thou care if I then became a Harlet? (-10)":
            $ LoveScore -= 10
            jump BassQ2_2
        "Nah, I got daddy's money. (+ 10)":
            $ LoveScore += 10
            jump BassQ2_3

label BassQ2_1:

    show Bassanio talking

    b "They say money doesn't buy you happiness, and they are hitting that from every angle, because I'm happy as shit."

    jump BassQ3
label BassQ2_2:

    show Bassanio unimpressed

    b "Um, duh... whore"

    jump BassQ3
label BassQ2_3:

    show Bassanio yurr

    b "You mean, we got daddy's money."

    jump BassQ3

label BassQ3:

    show Bassanio talking

    menu:
        b "Lets say you have to hypothetically be a third wheel all the time with my boy Antonio and I, you cool with that?"

        "As long as all your attention isn't on him. (- 10)":
            $ LoveScore -= 10
            jump BassQ3_1
        "The more the merrier. (0)":
            jump BassQ3_2

        "Why third wheel, you two can just hangout and have fun all the time! (+ 10)":
            $ LoveScore += 10
            jump BassQ3_3

label BassQ3_1:

    show Bassanio unimpressed

    b "*cough cough* center of attention much (or needy bitch) *cough cough*"
    jump BassQ4

label BassQ3_2:

    show Bassanio talking

    b "Eh okay, you can tag along"
    jump BassQ4

label BassQ3_3:

    show Bassanio yurr

    b "As we should"
    jump BassQ4

label BassQ4:

    show Bassanio talking

    menu: 
        b "Are you familiar with the courting process?"

        "I am not a common courter. (0)":
            $ LoveScore += 0
            jump BassQ4_1
        "Yes, many men try to court me. (- 10)":
            $ LoveScore -= 10
            jump BassQ4_2
        " You seem like you are. (+ 10)":
            $ LoveScore += 10
            jump BassQ4_3

label BassQ4_1:

    show Bassanio talking

    b "I see, so is it by choice or..."
    jump BassQ5

label BassQ4_2:

    show Bassanio unimpressed

    b "You look the type for that."
    jump BassQ5

label BassQ4_3:

    show Bassanio yurr

    b "You callin me hot? ;)"
    jump BassQ5

label BassQ5:

    show Bassanio talking

    menu: 
        b "Do you think we'd argue over real stuff, or pretend to hate each other for tension?"

        "That all depends on if we truly love each other. (0)":
            jump BassQ5_1
        "Duh, real arguments are dumb. (-10)":
            $ LoveScore -= 10
            jump BassQ5_2
        "Both, the only right answer. (+ 10)":
            $ LoveScore += 10
            jump BassQ5_3

label BassQ5_1:

    show Bassanio talking

    b "Woah there, that's a little deep don't ya think?"

    jump BassQuestionsEnd

label BassQ5_2:

    show Bassanio unimpressed

    b "You're a problem."
    jump BassQuestionsEnd

label BassQ5_3:

    show Bassanio yurr

    b "See? You get it."
    jump BassQuestionsEnd


label BassQuestionsEnd:

    if LoveScore >= 30:
        jump BassSuccess
    else:
        jump BassFailure

label BassSuccess:

    show Bassanio Yurr

    "You succeeded in romancing Bassanio!"
    jump StoryEndWin

label BassFailure:

    show Bassanio unimpressed

    "You failed to romace Bassanio."
    jump StoryEndLose



#END BASSANIO


label RosalindDate:

    show Rosalind talking

    r "So I am your final choice? A wise one but I'm not about to give myself to you easily."

    r "Turn around."

    "Her voice is forceful. She waits to see you turn the other way. As you do so, you hear the sound of clothes being shuffled frantically."

    hide Rosalind

    "A new voice can be heard from the same direction. It's similar to the girl's voice but much deeper, gruffer."

    show Ganymeade smile

    "Turning around, you can see a boyish man. His attire hides most of his body. His face is adorned by shining auburn hair. He smiles confidently at you."

    show Ganymeade talking

    gany "My name is Ganymede. I am an acquaintance of the girl you desire to court."

    menu:
        gany "I'll be testing to see if you are worthy to attain her hand."

        "This is too much work. There's no way I'm doing this for a girl I haven't even met. (-10)":
            $ LoveScore -= 20
            jump RQ1_1
        "Ohh okay that's fun, I'll play along I guess. (+5)":
            $ LoveScore += 5
            jump RQ1_2
        "You are so hot… Let's make out. (+10)":
            $ LoveScore += 10
            jump RQ1_3

label RQ1_1:

    show Ganymeade upset

    gany "I see you are not willing to pursue her..." #This line was unfinished...
    jump RQ2

label RQ1_2:

    show Ganymeade smile

    gany "Good! I'll teach you everything you need to know about love."
    jump RQ2

label RQ1_3:

    show Ganymeade yell

    gany "No!!! You are supposed to wanna make out with the girl, not me!"

    "Ganymede's cheeks blush. It doesn't seem like he entirely dislikes the idea."

    jump RQ2

label RQ2:

    show Ganymeade talking

    gany "It is an unusual situation but I am here for one reason and one reason only, to understand whether you truly are in love or not."

    gany "Love is merely a madness, and, I tell you, deserves as well a dark house and a whip as madmen do; and the reason why they are not so punished and cured is that the lunacy is so ordinary that the whippers are in love too."

    gany "profess we may cure it by counsel. I have cured one person before through pretending to be his mistress, that's what I'll do to you."

    menu: 
        gany "From now on call me Rosalind. That's the name of the woman you desire. Act with me in the same manner you would act with her."

        "I really don't think my love for you can be cured. My fair Rosalind, this love will last until the end of time. (+10)":
            $ LoveScore += 10
            jump RQ2_1
        "Okay… So I'll call you Rosalind. Wanna make out now? (+5)":
            $ LoveScore += 5
            jump RQ2_2
        "Can't we just be done with this and move on to the part where I meet the real Rosalind? (-5)":
            $ LoveScore -= 5
            jump RQ2_3

label RQ2_1:

    show Ganymeade smile

    gany "That's so cheesy!!"

    "Ganymede is clearly blushing."

    jump RQ3

label RQ2_2:

    show Ganymeade yell

    gany "Wait!! I'm not the real Rosalind, remember? I like your passion but don't kiss me yet!"

    jump RQ3

label RQ2_3:

    show Ganymeade upset

    gany "But I am the real Rosalind! Consider me her."

    jump RQ3

label RQ3:

    show Ganymeade talking

    gany "Come on! Show some enthusiasm. Woo me, woo me! What would you say to me now if I were your very, very Rosalind?"

    menu:

        "I would kiss before I spoke. (+5)":
            $ LoveScore += 5
            jump RQ3_1
        "Recite bad poetry. (+10)":
            $ LoveScore += 10
            jump RQ3_2
        "Rosalind you are so pretty haha (+0)":
            $ LoveScore += 0
            jump RQ3_3

label RQ3_1:

    show Ganymeade talking

    gany "Nay, you were better to speak first, and when you were gravelled for lack of matter, you might take occasion to kiss. For lovers lacking—God warn us—matter, the cleanliest shift is to kiss."

    jump RQ4

label RQ3_2:

    show Ganymeade smile

    gany "Your enthusiasm is noted… I do enjoy poetry from time to time, even when there are more feet than the verses could bear."

    jump RQ4

label RQ3_3:

    show Ganymeade surprised

    gany "Wait, really?"

    show Ganymeade yell

    gany "No! Compliment my personality before my appearance!"

label RQ4:

    show Ganymeade talking

    "This really isn't working out as intented..."

    gany "Enough! I'll reveal who I am."

    hide Ganymeade

    "Ganymede takes off his boyish clothes. He, or she, takes a wholly different appearance, with a humble woman's outfit and a face still androgynous but much tender."

    show Rosalind talking

    r "I have been your suitor all along. I'm Rosalind."

    menu:

        "So I'm not leaving this place kissing a hot twink? Disappointing… (+0)":
            $ LoveScore += 0
            jump RQ4_1
        "Woahh you are even better than Ganymede. (+5)":
            $ LoveScore += 5
            jump RQ4_2
        "Wait, you were lying to me so you could test if I was a good match??? Not cool, not cool. (-10)":
            $ LoveScore -= 10
            jump RQ4_3

label RQ4_1:

    show Rosalind yell

    r "Wait, wait! I still have the costume, don't leave yet!"

    jump RQ5

label RQ4_2:

    show Rosalind smile

    r "I sure do hope so!"

    jump RQ5

label RQ4_3:

    show Rosalind upset

    r "It's not that bad!! Come on…"

    jump RQ5

label RQ5:

    show Rosalind talking

    r "I vow to you you won't regret this, I have found you to be an interesting suitor but one question holds most importance."

    r "I believe in what I said earlier. Love is madness. Why should we court each other when love is only appearance, lasts much less than forever, and won't ever hold true?"

    menu:

        "We are both attracted to each other, we want to make this work. Is that not more than enough? (+10)":
            $ LoveScore += 10
            jump RQ5_1
        "I'll give you as much money and power as you need. You'll never have to worry about that ever again! (-10)":
            $ LoveScore -= 10
            jump RQ5_2
        "I don't really care about that, I just wanna make out with you while you are dressed up as a dude. (+0)":
            $ LoveScore += 0
            jump RQ5_3

label RQ5_1:

    show Rosalind smile

    r "Perhaps they are."

    jump RosalindENDQUESTIONS

label RQ5_2:

    show Rosalind upset

    r "I don’t care about those. They only corrupt human nature."

    jump RosalindENDQUESTIONS

label RQ5_3:

    show Rosalind talking

    r "You know what? Fair enough."

    jump RosalindENDQUESTIONS

label RosalindENDQUESTIONS:

    show Rosalind talking

    r "This is it. I know what I shall do with you."

    if LoveScore >= 30:
        jump RosalindSuccess
    else:
        jump RosalindFailure

label RosalindSuccess:

    show Rosalind upset

    r "You have a certain charm about you. Your flirtyness, your jokes, they entertain me and I can't say I don't find you attractive."

    r "Run away with me! Come to the forest of Arden! We can live a nice happy life away from the troubles of society and the dude who wants to kill me!"

    "You say yes with no doubt in your mind. Rosalind and you move to the forest where you pretend to be simple pastors."

    "Her dad gives the blessing to your marriage and you spend the rest of your life living in a cozy cottage in the middle of the woods alongside Rosalind. What a beautiful end!"

    jump StoryEndWin

label RosalindFailure:

    show Rosalind smile

    r "You’re dumped. Sorry, but we just didn’t really have any chemistry together"

    r "Don’t worry! Love isn’t real anyways so it’s fine that this happened, it only means you get to go after someone else like all of the other beautiful people that were in this show."

    r "As for me, I gotta run away! My uncle wants to kill me so I need to hide in the forest!"

    hide Rosalind

    "You never see Rosalind again. Apparently, as she hid in the forest her uncle converted to Christianity and decided to give her father back the throne. She became rich, married a hot dude, and never had any problem in her life."

    "You can’t say you are not jealous but unfortunately, there’s nothing you can do."

    jump StoryEndLose


label StoryEndWin:

    return #end game.

label StoryEndLose:

#End Character Dates ////////////////////////////

    return #end game.
