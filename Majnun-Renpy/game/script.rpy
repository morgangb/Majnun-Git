# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Unaligned characters
define attendant = Character("Attendant",
    who_color = "#ffffff")
define answeringmachine = Character("Answering Machine",
    who_color = "#ffffff")
define mrbloom = Character("Mr. Bloom",
    who_color = "#ffffff")
define mrsbloom = Character("Mrs. Bloom",
    who_color = "#ffffff")

# ACM Characters
define claragarcia = Character("Clara Garcia",
    who_color = "ffffb0")
define davidlee = Character("David Lee",
    who_color = "ffffb0")
define frankwilliams = Character("Frank Williams",
    who_color = "ffffb0")
define you = Character("You",
    who_color = "ffffb0")

# New Baptist Characters
define michaelbloom = Character("Michael Bloom",
    who_color = "a8734a")
define newbaptistwoman = Character("New Baptist Woman",
    who_color = "a8734a")

# The game starts here.
label start:

    # Set default values of variables

    $firstname = "Robin"
    $lastname = "Smith"

    $cremated = False

    $distracted = False

    $will = 3.0

    #### A debug menu for testing ####

    jump case1scene5

    scene black

    "This game is a work of fiction inspired by real people, movements, and events."

    "Its content may not be suitable for all players."

    #### Case 1 Scene 1 ####

    label case1scene1:

        scene black

        "Case 1: Genesis"

        "November 27 1978."

        scene case1scene1

        "Your apartment in Berkeley, California."

        answeringmachine "Hey, it's Doctor Anderson."

        answeringmachine "I just wanted to let you know that you can take as much time off as you need to for this."

        answeringmachine "Berkeley's here to support you."

        answeringmachine "We can postpone your thesis too, if you want."

        answeringmachine "Just let me know."

        answeringmachine "Take care of yourself."

        jump case1scene2

    #### Case 1 Scene 2 ####

    label case1scene2:

        scene black

        "November 28 1978."

        scene metalcrates

        "Dover Air Force Base, Delaware."

        "In the distance, metal crates are unloaded from a plane on the runway."

        scene case1scene2

        "You stand in line."

        attendant "Hello. Name, please."

        label .nameinput:
            $firstname = renpy.input("First name:")
            $lastname = renpy.input("Last name:")

            menu:
                attendant "[firstname] [lastname], is that right?"

                "Yes, that's right.":
                    # So, the player's happy with their name, and we can move on.
                    attendant "From Berkeley, California. And you're Anne [lastname]'s next-of-kin?"

                    you "I am, yes."

                    attendant "Okay. Now, I'm sure you're aware, but we need to know what to do with Anne's remains."

                    attendant "She passed away ten days ago, now."

                    label .cremationembalming:
                        # The player decides what to do with Anne's remains.

                        menu:
                            attendant "We can cremate her here, if you like."

                            "Didn't she leave a will?":
                                attendant "Not one in Guyana, or anywhere on public record that we could find."

                                jump .cremationembalming

                            "Well, what would she want?":
                                attendant "We hoped you might know."

                                jump .cremationembalming

                            "Can she be embalmed?":
                                attendant "I'm sorry. It's too late for that."

                                jump .cremationembalming

                            "Yes. Cremate her.":
                                $cremated = True

                                attendant "Okay, we'll bring you an urn in just a moment."

                                attendant "In the meantime, please wait over there."

                                "The attendant gestures to a crowded seating area."

                                label .sayinggoodbye:
                                    # The player says goodbye to the attendant to go sit down

                                    menu:
                                        attendant "I'm sorry for your loss, by the way."

                                        "Yeah. Sure.":
                                            attendant "Sorry, if I've been... abrasive..."
                                            attendant "I've been on the clock for a while. Please, have a seat."

                                            label .meetingclara:
                                                # The player meets Clara Garcia for the first time.

                                                "You sit down."

                                                show claragarcia

                                                "A woman takes a seat next to you."

                                                claragarcia "Do you have a moment?"

                                                menu:
                                                    "Yeah, sure.":
                                                        claragarcia "Thank you."

                                                    "I'm sorry. I'm not in the mood to chat.":
                                                        claragarcia "I'll only be a moment."

                                                claragarcia "My name's Clara. I lost my eldest, Sebastián, in Guyana."

                                                menu:
                                                    "I'm [firstname]. I lost my sister, Anne.":
                                                        claragarcia "It's nice to meet you, [firstname]. I'm sorry for your loss."

                                                    "I'm [firstname].":
                                                        claragarcia "It's nice to meet you, [firstname]."

                                                label .eavesdrop:
                                                    menu:
                                                        claragarcia "I overheard you speaking. You're from Berkeley?"

                                                        "You were eavesdropping?":
                                                            claragarcia "I'm sorry, I didn't mean to. It's quiet in here."

                                                            jump .eavesdrop

                                                        "Yes, I am.":
                                                            claragarcia "Good."

                                                            jump .supportgroup

                                                            label .supportgroup:
                                                                claragarcia "I'm from San Francisco. A lot of us are."

                                                                claragarcia "Some of us were talking about maybe meeting up soon."

                                                                claragarcia "That way we can share our stories."

                                                                claragarcia "You know... Be there for each other."

                                                                claragarcia "Would you join us?"

                                                                jump case1scene3

                                                        "Not originally. But I live there now.":
                                                            claragarcia "Okay, good."

                                                            jump .supportgroup

                                        "Thanks. I'm sure this isn't easy for you either.":
                                            attendant "I'm sure it's easier for me than it is for you."

                                            jump .meetingclara

                                        "It's alright. We were never that close.":
                                            attendant "That's a shame... I think..."

                                            jump .meetingclara

                            "No, don't cremate her.":
                                $cremated = False

                                attendant "Okay, a funeral, then."

                                label .burialplace:
                                    menu:
                                        attendant "Do you want a funeral in Berkeley, or in Dover?"

                                        "Berkeley.":
                                            attendant "Okay, someone will be over to arrange the specifics with you in a moment."

                                            attendant "Will you please wait over there in the meantime?"

                                            jump .sayinggoodbye

                                        "Dover. She shouldn't have to travel any more.":
                                            attendant "Alright - now, you understand that all the funeral homes here are busy, currently."

                                            attendant "We're doing our best to co-ordinate, and make arrangements for everybody."

                                            attendant "In the meantime, please wait over there. You'll be called when it's time."

                                            jump .sayinggoodbye

                                        "Can she be buried in Guyana?":
                                            attendant "Sorry. That's impossible to arrange."

                                            menu:
                                                "She should have been buried in Guyana.":
                                                    attendant "I'm sorry. We couldn't have known that."

                                                    jump .burialplace

                                                "Okay":
                                                    jump .burialplace

                "No, that's wrong.":
                    # Basically what we're doing here is jumping back to where we asked for the player's name. So we'll just do that again.
                    jump .nameinput

    #### Case 1 Scene 3 ####

    label case1scene3:
        scene black

        "December 6 1978."

        scene case1scene3

        "A Community Center in San Francisco, California."

        show claragarcia

        claragarcia "Hello, [firstname]. I'm glad you could make it."

        claragarcia "Please, have a seat. I'll give an introduction, and then we'll have a few speakers."

        "You sit down and listen."

        claragarcia "Hello everybody. Thank you for coming."

        claragarcia "It means a lot to me, that we can all be here to support each other."

        claragarcia "So, you all know me. My name is Clara Garcia."

        claragarcia "I lost my son, Sebastián, in Guyana."

        claragarcia "I thank God that I still have his brother with me."

        claragarcia "Jim Jones was a liar."

        claragarcia "He was a conman, and a fraud."

        claragarcia "It is one thing to take your own life, but to take hundreds of others with you..."

        claragarcia "He has left thousands of families bereaved."

        claragarcia "He said he believed in God, but we all know that he didn't."

        claragarcia "He said he believed in communism, but even that seems hollow."

        claragarcia "I think, in the end, he only believed in himself."

        claragarcia "He said he'd help black people, help women, help the poor, but he just took from them."

        claragarcia "He didn't love the people we loved when he took their lives."

        claragarcia "He doesn't deserve our forgiveness."

        claragarcia "But we have to move on."

        claragarcia "We lost friends and family in Guyana, but we do not have to lose ourselves."

        hide claragarcia

        "Several other speakers follow, telling their own stories of atrocity."

        "When it is over, people take refreshments."

        "Quiet conversations begin."

        "Clara approaches you, with a man beside her."

        show claragarcia at right

        show frankwilliams

        claragarcia "[firstname], this is Frank Williams. He's the reason I only lost one son in Guyana."

        hide claragarcia

        frankwilliams "Nice to meet you. Clara tells me you're from Berkeley. I'm looking for someone for a job."

        menu:
            frankwilliams "Nice to meet you. Clara tells me you're from Berkeley. I'm looking for someone for a job."

            "What's the job?":
                jump .deprogrammer

            "What's the pay?":
                jump .deprogrammer

            "I'm not interested.":
                frankwilliams "Not interested in doing the kind of thing that saved someone from what happened in Guyana?"

                jump .deprogrammer

        label .deprogrammer:
            frankwilliams "I'm what's called a deprogrammer. Families pay me to save people from cults."

            frankwilliams "I need someone who knows the Berkeley area for this case. In return, I cut you in."

            menu:
                frankwilliams "You'd be looking at $1,000, for just a few days of your time."

                "Seems like something you shouldn't be charging for.":
                    frankwilliams "Everyone's gotta eat, right?"

                    frankwilliams "Plus, the job carries certain risks."

                    menu:
                        frankwilliams "Plus, the job carries certain risks."

                        "'Risks'?":
                            jump .hereswhatido

                "Okay, but what do I need to do?":
                    frankwilliams "You're gonna drive around Berkeley and find the kid I'm trying to deprogram."

                    menu:
                        frankwilliams "You're gonna drive around Berkeley and find the kid I'm trying to deprogram."

                        "'Find'?'":
                            jump .hereswhatido

                "I'm really not interested.":
                    frankwilliams "Really? Not interested in doing the kind of thing that would have saved your sister?"

                    menu:
                        frankwilliams "Really? Not interested in doing the kind of thing that would have saved your sister?"

                        "Don't bring her into this.":
                            frankwilliams "You know that hundreds of people died in Guyana, right?"

                            frankwilliams "Well, they weren't special."

                            frankwilliams "Cults kill people every single day in America."

                            menu:
                                frankwilliams "Cults kill people every single day in America."

                                "There's no way that's true.":
                                    frankwilliams "No way?"

                                    frankwilliams "Seven dead in the Tate-LaBianca murders in '69."

                                    frankwilliams "Fifteen killed by the 'Death Angels' - so-called Black Muslims - from '73 to '74."

                                    frankwilliams "A satanist shot eight people in New York City from '76 to '77."

                                    frankwilliams "Countless more have been killed by the violence of the Ku Klux Klan."

                                    frankwilliams "Oh, and I shouldn't forget: Jonestown, Guyana. Almost a thousand dead in '78."

                                    menu:
                                        "Fine I get it.":
                                            frankwilliams "Good."

                                            jump .hereswhatido

                                        "That doesn't prove your point. You just listed examples.":
                                            frankwilliams "Sorry I don't have the precise statistics to hand, but you get my meaning."

                                            frankwilliams "People are dying. I stop that from happening."

                                            jump .hereswhatido

                        "Are you trying to make me feel guilty?":
                            frankwilliams "Not yet. I'm trying to help you do something."

                            frankwilliams "I'm trying to help you move on."

                            frankwilliams "I'm trying to stop you from losing yourself."

                            jump .hereswhatido

                        "Fuck off.":
                            frankwilliams "Fuck you."

                            frankwilliams "I'm offering you the chance to stop what happened to your sister from happening to you, and you tell me 'Fuck off'?"

                            frankwilliams "You're gonna hear me out and you're gonna listen."

                            jump .hereswhatido

            label .hereswhatido:
                frankwilliams "Here's what's happening."

                frankwilliams "Hundreds of people don't die in a single incident because they're in their right minds."

                frankwilliams "People don't just join cults because they see something the ordinary person doesn't."

                frankwilliams "They're brainwashed."

                frankwilliams "Someone's fucked with their heads, and now they'll happily give their time, their money, their lives, to a cause they hadn't heard about a year ago."

                frankwilliams "Now their friends and their family from before the cult got to them realize that something's happened."

                frankwilliams "Their son, or their daughter, or their sister, isn't who they used to be."

                frankwilliams "But they say everything is just fine."

                frankwilliams "They say they're happy now."

                frankwilliams "They say they don't want to leave."

                frankwilliams "When really, they're dying."

                frankwilliams "It may be slow or it may be quick but that cult is taking away their lives."

                frankwilliams "All things considered, I'm sure you see the need to do whatever it takes to save them. Right?"

                menu:
                    frankwilliams "All things considered, I'm sure you see the need to do whatever it takes to save them. Right?"

                    "Right.":
                        frankwilliams "Damn right."

                        jump .hereswhatsgoingon

                    "There's got to be a limit.":
                        frankwilliams "In saving a life? Shit..."

                        frankwilliams "Look at like this."

                        frankwilliams "If someone was trying to kill you, you'd fight back."

                        frankwilliams "If someone was trying to kill someone else, you'd stop them."

                        frankwilliams "And if you hurt the attacker, well then you'd be justified."

                        frankwilliams "It's reasonable force."

                        frankwilliams "It's proportional."

                        jump .hereswhatsgoingon

                    "If they say they're happy, no one should intervene with that?":
                        frankwilliams "Yeah? I bet your sister told you she was happy."

                        frankwilliams "Did you even try to get her out from under Jim Jones?"

                        menu:
                            frankwilliams "Did you even try to get her out from under Jim Jones?"

                            "I tried.":
                                frankwilliams "You tried. And it wasn't enough, was it?"

                                frankwilliams "I'm telling you, I've got a method that works."

                                frankwilliams "Clara will tell you that."

                                frankwilliams "A hundred other people will tell you that."

                                frankwilliams "I'm telling you that there's a way to stop what happened to your sister from happening to anyone else, and you're not interested?"

                                menu:
                                    frankwilliams "I'm telling you that there's a way to stop what happened to your sister from happening to anyone else, and you're not interested?"

                                    "I'm not interested.":
                                        frankwilliams "For real?"

                                        menu:
                                            frankwilliams "For real?"

                                            "For real. I'm not interested.":
                                                frankwilliams "I guess Clara misjudged you. I'll see you around."

                                                hide frankwilliams

                                                "Frank walks away."

                                                jump roaduntaken

                                            "Fine... I'm interested.":
                                                frankwilliams "Good. Now listen."

                                                jump .hereswhatsgoingon

                                    "I'm interested. Go on.":
                                        frankwilliams "Good. Now listen."

                                        jump .hereswhatsgoingon

                label .hereswhatsgoingon:
                    frankwilliams "The parents or the family or the friends of the kid, the cultist, the one that got brainwashed, they call me."

                    frankwilliams "They tell me what's happening."

                    frankwilliams "I put together a team. Maybe me and one other person, sometimes two."

                    frankwilliams "We get the kid somewhere that's safe and quiet and that they can't leave, whether they want to or not."

                    frankwilliams "We then sit down, and we talk to them."

                    frankwilliams "We make them snap out of it."

                    frankwilliams "We get them to see what's real and what isn't."

                    frankwilliams "And, after a little while, they snap back to reality."

                    frankwilliams "Sometimes it takes a day. Sometimes it takes a week. But we get them back."

                    frankwilliams "I make sure they're gonna be safe with their family again."

                    frankwilliams "I make sure that if anything else happens, they know who to call."

                    frankwilliams "Then I take my pay, and I go."

                    frankwilliams "Any questions?"

                    label .anyquestions:
                        menu:
                            frankwilliams "Any questions?"

                            "No more questions.":
                                frankwilliams "Good. You're in, then?"

                                menu:
                                    frankwilliams "Good. You're in, then?"

                                    "I'm in.":
                                        label .yourein:
                                            frankwilliams "Alright. Give me your address."

                                            "Frank hands you a notepad. You write your address, and hand it back."

                                            frankwilliams "Good. Your new colleague, David Lee, will pick you up tomorrow morning."

                                            frankwilliams "See you soon."

                                            "Frank stands up and leaves."

                                    "No. I don't think so.":
                                        frankwilliams "Come on, after all that? Are you sure?"

                                        menu:
                                            "I'm sure, Frank. I won't do it.":
                                                frankwilliams "Well... Alright, then."

                                                jump roaduntaken

                                            "Fuck it. I'm in.":
                                                frankwilliams "Glad to hear it, [firstname]."

                                                jump .yourein

                            "Abduction and false imprisonment seems... Legally dubious.":
                                frankwilliams "It is. Hence the paycheck."

                                frankwilliams "People have been to court for deprogramming, but never to prison."

                                frankwilliams "The jury knows that we're the good guys."

                                frankwilliams "If something goes wrong on this case, though, don't worry. I'll bail you out."

                                jump .anyquestions

                            "How do you make them 'snap' to reality?":
                                frankwilliams "You'll see. It's nothing special, once you get the knack for it."

                                frankwilliams "And it's nothing violent either, before you get that in your head."

                                frankwilliams "I talk, mostly."

                                frankwilliams "Sometimes I shout."

                                frankwilliams "Occasionally, I have to say some mean things."

                                frankwilliams "But I don't hit them."

                                frankwilliams "I don't even lay a finger on them during the deprogramming."

                                frankwilliams "Like I said, you'll see."

                                jump .anyquestions

                            "How much are you getting paid for this?":
                                frankwilliams "For this case?"

                                frankwilliams "$8,000."

                                frankwilliams "More than most people see in six months, I know, but I got expenses."

                                frankwilliams "You know I'm from Washington? I paid for my gas, I'm paying nightly for the motel."

                                frankwilliams "And, if it comes to it, I'm paying my lawyer."

                                frankwilliams "$8,000 is a pretty reasonable sum."

                                jump .anyquestions

    #### Case 1 Scene 4 ####

    label case1scene4:
        scene black

        "December 7 1978."

        scene case1scene1

        "Your apartment in Berkeley, California."

        "The doorbell buzzes."

        scene case1scene4

        "A man waits by an SUV."

        show davidlee

        davidlee "Are you [firstname]?"

        menu:
            davidlee "Are you [firstname]?"

            "Yeah, that's me.":
                davidlee "Good. Let's go. You're driving."

                jump .insidecar

            "Who's asking?":
                davidlee "Funny stuff. Get in. You're driving."

                jump .insidecar

        label .insidecar:
            scene suv

            "You get inside the SUV."

            show davidlee

            davidlee "We're looking for this man."

            scene black

            "David pulls out a photograph."

            show michaelbloom

            davidlee "His name is Michael Bloom."

            davidlee "Use to be a star student at UC Berkeley, until he heard that a man, claiming to be John the Baptist, was in the area."

            davidlee "He got curious and went along. Afterwards, he insisted everyone call him 'Levi'."

            davidlee "He dropped out of college. When his parents tried to step in, he cut them off. Barely speaks to them now."

            davidlee "He doesn't have a life outside of the Church."

            davidlee "It seems like, currently, he solicits for them, here in Berkeley."

            davidlee "You know the area. We'll drive around, find him, and take him to his family in Muir Beach."

            scene suv

            "David puts the photo on the dashboard."

            show davidlee

            davidlee "If you've got questions, ask them. But start driving. I don't want to waste time."

            menu:
                davidlee "If you've got questions, ask them. But start driving. I don't want to waste time."

                "Hold on. I've got some reservations.":
                    davidlee "Make this quick, then."

                    label .makethisquickthen:
                        menu:
                            davidlee "Make this quick, then."

                            "If Michael was a college student, isn't he an adult?":
                                davidlee "Yeah. So what?"

                                menu:
                                    davidlee "Yeah. So what?"

                                    "So, can't he make his own decisions?":
                                        davidlee "Sure he can, but that's not what he's doing."

                                        davidlee "He's been brainwashed. That's how cults work."

                                        menu:
                                            davidlee "He's been brainwashed. That's how cults work."

                                            "How?":
                                                davidlee "'How'?"

                                                davidlee "You go along to a baptism, or you get solicited in the streets, or whatever."

                                                davidlee "They say stuff you already agree with."

                                                davidlee "They say shit like, 'Doesn't it feel like the world could end any time now? The Russians could kill us all in a moment.'"

                                                davidlee "If you respond, they heap praise on you. Say, 'You know, you're smart. You're really brave.'"

                                                davidlee "If you criticize, they go on the offensive. 'Who told you that? Oh, sure, that's what they want you to think.'"

                                                davidlee "After a few hours of talking they have you enamoured."

                                                davidlee "Then they keep hold of you. 'Hey, we're having a get together this weekend. It'd be great if you could come.'"

                                                davidlee "Pretty soon they're like your friends. But they push you to take the next step."

                                                davidlee "'The world could end any time now, and you haven't been properly baptized.'"

                                                davidlee "'You'll go to Hell.'"

                                                davidlee "'Please, we don't want that for you.'"

                                                davidlee "Then they've got you for good."

                                                davidlee "Frank's gonna snap Michael out of it so he can make his own decisions and think for himself again."

                                                davidlee "Satisfied?"

                                                menu:
                                                    davidlee "Satisfied?"

                                                    "Sure. I'm satisfied.":
                                                        davidlee "Good."

                                                        jump .makethisquickthen

                                                    "No, I'm not.":
                                                        jump .leavethen

                                            "Alright. Fair enough.":
                                                jump .makethisquickthen

                                    "Forget about it.":
                                        jump .makethisquickthen

                            "I'm still not happy about the legal grayness of this.":
                                davidlee "Noted."

                                menu:
                                    davidlee "Noted."

                                    "That's it?":
                                        davidlee "What more do you want me to say?"

                                        jump .leavethen

                                    "Okay then.":
                                        jump .makethisquickthen

                            "Do we have a plan?":
                                davidlee "Like I said: drive around until we find Michael Bloom, then take him to Muir Beach."

                                menu:
                                    davidlee "Like I said: drive around until we find Michael Bloom, then take him to Muir Beach."

                                    "That seems like a pretty flimsy plan.":
                                        davidlee "It'll have to do."

                                        davidlee "We can't formulate anything else until we have a better understanding of the situation."

                                        davidlee "You know, where Michael is, how many people are around, if there's any other cultists with him."

                                        davidlee "Once we find him, we'll discuss more."

                                        menu:
                                            davidlee "Once we find him, we'll discuss more."

                                            "It won't get violent, will it?":
                                                davidlee "Hopefully not."

                                                menu:
                                                    davidlee "Hopefully not."

                                                    "'Hopefully'?":
                                                        davidlee "Like I said, there's lots of factors involved."

                                                        davidlee "But we'll do our best to make sure no one gets hurt, especially not Michael."

                                                        menu:
                                                            davidlee "But we'll do our best to make sure no one gets hurt, especially not Michael."

                                                            "I'm not sure if 'our best' is good enough.":
                                                                jump .leavethen

                                                            "Okay.":
                                                                jump .makethisquickthen

                                                    "Alright then.":
                                                        jump .makethisquickthen

                                            "Alright, we'll table this discussion then.":
                                                jump .makethisquickthen

                                    "I guess that's good enough.":
                                        jump .makethisquickthen

                            "That's it. Let's go.":
                                jump youstartdriving

                        label .leavethen:
                            davidlee "I'm not Frank. I won't sit here and give you a talk to convince you to stay."

                            davidlee "If you've got a problem, leave. I don't have time to wait around."

                            menu:
                                davidlee "If you've got a problem, leave. I don't have time to wait around."

                                "Alright. I'll go.":
                                    davidlee "See you around."

                                    jump roaduntaken

                                "No, I'm okay. Let's do this job.":
                                    jump .makethisquickthen

                "Alright, let's go.":
                    label youstartdriving:
                        "You start driving."

                        davidlee "If you've got questions, it's better to ask them now, before we find Michael."

                        label .ifyouvegotquestions:
                            menu:
                                davidlee "If you've got questions about the job, it's better to ask them now, before we find Michael."

                                "Who's this 'John the Baptist'?":
                                    davidlee "A man named Georgy Sokolov."

                                    davidlee "Born and raised in New York to White Russians, enlisted to fight in the Korean War."

                                    davidlee "When he came home, he says he had a dream where an angel told him that he was the New Baptist."

                                    davidlee "He believes he's making the way for the Apocalypse and the Second Coming."

                                    davidlee "He goes from place to place baptising people in public, while his family run his church from New York City."

                                    davidlee "Those baptized by him will apparently be 'saved' when World War 3 starts."

                                    menu:
                                        davidlee "Those baptized by him will apparently be 'saved' when World War 3 starts."

                                        "That's pretty wild.":
                                            davidlee "I guess it is."

                                            jump .ifyouvegotquestions

                                        "I can see how that interests people.":
                                            davidlee "Yeah. Me too."

                                            jump .ifyouvegotquestions

                                        "Alright then.":
                                            jump .ifyouvegotquestions

                                    jump .ifyouvegotquestions

                                "What's with Michael's new name, 'Levi'?":
                                    davidlee "Have you ever been baptized?"

                                    menu:
                                        davidlee "Have you ever been baptized?"

                                        "Yes.":
                                            davidlee "Well, it's like that."

                                            label .baptizedname:
                                                davidlee "When 'John' baptizes someone, they take a new name."

                                                davidlee "The name has to be found somewhere in the Bible, and can be chosen by the person being baptized or by someone else."

                                                davidlee "Sometimes people manage to get their names legally changed too."

                                                jump .ifyouvegotquestions

                                        "No.":
                                            davidlee "I guess you wouldn't know then."

                                            jump .baptizedname

                                "I'm out of questions.":
                                    davidlee "Well, I don't mind silence, but I find it easier to work with people if I know them."

                                    davidlee "Do you believe in God?"

                                    menu:
                                        davidlee "Do you believe in God?"

                                        "Yes.":
                                            davidlee "You sound pretty sure."

                                            menu:
                                                davidlee "You sound pretty sure."

                                                "I am sure.":
                                                    davidlee "Well, I was sure once."

                                                    jump .davidleebackstory

                                                "I'm not sure.":
                                                    davidlee "Yeah. Me neither."

                                                    jump .davidleebackstory

                                        "No.":
                                            davidlee "Did you used to believe in God?"

                                            menu:
                                                davidlee "Did you used to believe in God?"

                                                "Yeah. At some point I stopped.":
                                                    davidlee "Yeah. Me too."

                                                    jump .davidleebackstory

                                                "No. I never believed in God.":
                                                    davidlee "I used to."

                                                    jump .davidleebackstory

                                        "I don't know.":
                                            davidlee "Yeah. Me neither."

                                            jump .davidleebackstory

                                        "Let's keep this professional.":
                                            davidlee "I'm not trying to start a fight. But you don't have to say, if you don't want to."

                                            jump .davidleebackstory

                                    label .davidleebackstory:
                                        davidlee "Have you ever heard of Hong Xiuquan?"

                                        menu:
                                            davidlee "Have you ever heard of Hong Xiuquan?"

                                            "I've heard of him.":
                                                jump .hongxiuquan

                                            "No.":
                                                label .hongxiuquan:
                                                    davidlee "He lived in the 19th century."

                                                    davidlee "His family were middle class, local officials."

                                                    davidlee "Although they were well off, they could be even more powerful, if one of them could pass the imperial examination."

                                                    davidlee "Xiquan's parents paid for his education, and they paid for him to take the exam on four separate occasions."

                                                    davidlee "He never passed."

                                                    davidlee "After his third attempt, he had a vision, where he visited Heaven."

                                                    davidlee "After his fourth attempt, he consulted Christian pamphlets he had received from a missionary years prior."

                                                    davidlee "Interpreting his vision, he believed that he was the Second Son of God, the younger brother of Jesus Christ."

                                                    davidlee "He took it upon himself to rid the world of 'demon worship'."

                                                    davidlee "Every Confucian and Buddhist book or icon in his house was burned."

                                                    davidlee "His family were his first believers, and they founded the 'Society of God-Worshippers'."

                                                    davidlee "He gained more and more followers."

                                                    davidlee "Perhaps they followed because Imperial China was not a good place for many people to live."

                                                    davidlee "The Government panicked, and sent imperial troops to disperse them."

                                                    davidlee "Hong and his followers defeated them, and beheaded the Manchu commander."

                                                    davidlee "Hong declared 'The Heavenly Kingdom'."

                                                    davidlee "The Taiping Rebellion lasted fourteen years, until the Heavenly Kingdom fell."

                                                    davidlee "Hong Xiuquan had died months before of illness, but his remains were exhumed, cremated, and blasted from a cannon."

                                                    davidlee "His son, Tianguifu, was tortured to death."

                                                    davidlee "The process is called 'Lingchi'."

                                                    davidlee "They cut you apart slowly with a knife, removing body parts, but keeping you alive."

                                                    davidlee "You beg for death, until you eventually bleed out."

                                                    davidlee "Tianguifu was fourteen years old, when they did this to him."

                                                    davidlee "More people died in the Taiping Rebellion than in the whole of the First World War."

                                                    davidlee "My family came here after that."

                                                    davidlee "'John', his family came here after the Russian Revolution."

                                                    davidlee "I think I saw some of myself in him."

                                                    davidlee "I accepted baptism from 'John' when I was fourteen."

                                                    davidlee "Sure, Michael Bloom dropped out of college for 'John', but I dropped out of high school."

                                                    davidlee "It wasn't until Frank deprogrammed me when I was 18 that I finally saw clearly again."

                                                    davidlee "But, by then I had no prospects, no hope, no future outside of the cult."

                                                    davidlee "So, now I help Frank to save people, the same way he saved me."

                                                    davidlee "I know you probably still have some reservations about this, but take it from me."

                                                    davidlee "What we're doing is important."

                                                    davidlee "Even if it feels wrong, we've got to do it--"

                                                    davidlee "Keep driving, but that's  Michael on the sidewalk."

                                                    "You look out of the window."

                                                    scene case1scene5

                                                    show michaelbloom

                                                    "A man matching the photograph speaks with a couple on the street."

                                                    "A woman stands beside him, holding pamphlets."

                                                    scene suv

                                                    show davidlee

                                                    davidlee "Take us around the corner and pull over."

                                                    davidlee "Did you see the girl he was with? Probably another 'New Baptist'."

                                                    davidlee "You get out and go talk to them. Distract them."

                                                    davidlee "I'll take the car, drive around the block, come back."

                                                    davidlee "When I pass by, we'll grab Michael and get out."

                                                    davidlee "Any questions?"

                                                    label .anyquestionsbeforekidnapping:
                                                        menu:
                                                            davidlee "Any questions?"

                                                            "How do I distract them?":
                                                                davidlee "What they're doing is called 'soliciting' in the Church."

                                                                davidlee "There's lots of ways it can go, but their main goal is to get you to give them money."

                                                                davidlee "They'll talk to you about the Church and what they do, and make it seem like a worthy cause."

                                                                davidlee "Not all of it is a lie, but it's definitely not all true."

                                                                davidlee "Show interest. Keep them talking."

                                                                davidlee "Once you've got them going, they won't be able to help themselves."

                                                                davidlee "That's when I'll come back around."

                                                                jump .anyquestionsbeforekidnapping

                                                            "Why drive around the block?":
                                                                davidlee "Gives you time to get them talking, gives me time to get the car ready."

                                                                davidlee "There's stickers in the back. I'll put one over the number plate."

                                                                davidlee "It's the only thing that distinguishes this car from every other SUV on the roads of California."

                                                                davidlee "A few minutes after grabbing Michael, we'll remove the sticker."

                                                                davidlee "Basically makes us invisible."

                                                                jump .anyquestionsbeforekidnapping

                                                            "How do we 'grab' Michael?":
                                                                davidlee "In an ideal situation we wouldn't have to - we'd trick him into getting in the car himself."

                                                                davidlee "We don't have that luxury though."

                                                                davidlee "He's a scrawny kid, and I'm a 200 pound man."

                                                                davidlee "I'll grab him, shove him in the car, sit with him in the back."

                                                                davidlee "You'll climb in the front. Start driving."

                                                                davidlee "Don't worry. I've done this before."

                                                                jump .anyquestionsbeforekidnapping

                                                            "Why don't you distract them?":
                                                                davidlee "I told you, I've done this before."

                                                                davidlee "I don't recognize them, but they might recognize me."

                                                                davidlee "Maybe someone told them about this big Chinese kidnapper, or the Church got hold of pictures of me."

                                                                davidlee "Whatever. They'd bolt if they saw me."

                                                                davidlee "It's not worth the risk."

                                                                jump .anyquestionsbeforekidnapping

                                                            "Okay, no more questions.":
                                                                davidlee "Okay. Ready?"

                                                                menu:
                                                                    davidlee "Okay. Ready?"

                                                                    "I don't want to do this.":
                                                                        davidlee "Then get out and leave. There's no time for doubts right now."

                                                                        menu:
                                                                            davidlee "Then get out and leave. There's no time for doubts right now."

                                                                            "Nevermind. I can do this.":
                                                                                davidlee "Damn right you can. Let's go."

                                                                                jump case1scene5

                                                                            "I can't do this. I've got to go.":
                                                                                davidlee "You're sure?"

                                                                                menu:
                                                                                    davidlee "You're sure?"

                                                                                    "I'm sure.":
                                                                                        davidlee "I'll see you around, then."

                                                                                        jump roaduntaken

                                                                                    "No. Fuck it. Let's go. I'll get Michael.":
                                                                                        davidlee "See you in a few."

                                                                                        jump case1scene5

                                                                    "I'm ready. Let's go.":
                                                                        jump case1scene5

    #### Case 1 Scene 5 ####

    label case1scene5:
        scene black

        "You get out of the car and walk around the corner."

        scene case1scene5

        "You see Michael Bloom down the street, still speaking with the couple."

        "The other 'New Baptist' approaches you."

        newbaptistwoman "Hi! Do you have a moment? We're collecting for a Christian charitable organization, and need your help."

        menu:
            newbaptistwoman "Hi! Do you have a moment? We're collecting for a Christian charitable organization, and need your help."

            "Sure, I have a moment.":
                newbaptistwoman "Wonderful!"

                "She hands you a pamphlet, entitled 'Fate of the Unlearned'."

                newbaptistwoman "Doesn't it feel like the world could end any day now?"

                menu:
                    newbaptistwoman "Doesn't it feel like the world could end any day now?"

                    "Yes, it does.":
                        label .ourmission:
                            newbaptistwoman "And the Bible tells us how the world will end, doesn't it?"

                            menu:
                                newbaptistwoman "And the Bible tells us how the world will end, doesn't it?"

                                "Yes, it does.":
                                    label .takenup:
                                        newbaptistwoman "And won't the believers be saved from tribulation?"

                                        menu:
                                            newbaptistwoman "And won't the believers be saved from tribulation?"

                                            "Yes, they will.":
                                                label .proselytize:
                                                    newbaptistwoman "So, isn't it important to make sure as many people believe as possible so that they are spared?"

                                                    menu:
                                                        newbaptistwoman "So, isn't it important to make sure as many people believe as possible so that they are spared?"

                                                        "Yes, it is important.":
                                                            newbaptistwoman "Among other things, what we provide is a service called 'New Baptism'."

                                                            newbaptistwoman "Here, I think this might interest you."

                                                            "She hands you another pamphlet, this one entitled 'New Baptism'."

                                                            newbaptistwoman "For many people, it is a reaffirmation of faith in God before Christ's return."

                                                            newbaptistwoman "And for many people who have not been baptized before, it is a chance to accept God before it is too late."

                                                            newbaptistwoman "Would you perhaps be interested in donating?"

                                                            newbaptistwoman "Or even coming along to one of our baptisms?"

                                                            jump case1scene6

                                                        "No, it's not.":
                                                            newbaptistwoman "'Go your ways: behold, I send you forth as lambs among wolves.'"

                                                            newbaptistwoman "Luke 10:3."

                                                            jump case1scene6

                                            "No, they won't.":
                                                newbaptistwoman "The Bible says so!"

                                                newbaptistwoman "'Then we which are alive and remain shall be caught up together with them in the clouds, to meet the Lord in the air: and so shall we ever be with the Lord.'"

                                                newbaptistwoman "1 Thessalonian 4:17."

                                                jump .proselytize

                                            "I don't know.":
                                                jump .proselytize

                                "Not exactly.":
                                    newbaptistwoman "There can be no other interpretation!"

                                    newbaptistwoman "'There shall not be left here one stone upon another, that shall not be thrown down.'"

                                    newbaptistwoman "Matthew 24:2."

                                    jump .takenup

                                "I don't believe in the Bible.":
                                    newbaptistwoman "What do you believe in, then?"

                                    menu:
                                        newbaptistwoman "What do you believe in, then?"

                                        "I believe in other Books.":
                                            newbaptistwoman "'For verily I say unto you, Till heaven and earth pass, one jot or one tittle shall in no wise pass from the law, till all be fulfilled.'"

                                            newbaptistwoman "Matthew 5:18."

                                            newbaptistwoman "There is no Book but the Bible!"

                                            menu:
                                                newbaptistwoman "There is no Book but the Bible!"

                                                "The Quran came after it.":
                                                    newbaptistwoman "How could the Quran have been inspired by God when Heaven and Earth had not yet passed?"

                                                    menu:
                                                        newbaptistwoman "How could the Quran have been inspired by God when Heaven and Earth had not yet passed?"

                                                        "Is it possible that statement was a metaphor?":
                                                            newbaptistwoman "The scriptures are clear as day."

                                                            # End

                                                        "Do you refute the Prophet of Islam as others have refuted Christ?":
                                                            newbaptistwoman "The two are incomparable."

                                                            # End

                                                        "Perhaps the Bible erred.":
                                                            newbaptistwoman "The Bible is inerrant."

                                                            # End

                                                "The Tanakh came before it.":
                                                    newbaptistwoman "The Old Testament? Of course."

                                                    newbaptistwoman "It established everything that made Jesus Christ the Messiah."

                                                    newbaptistwoman "Wait, are you Jewish?"

                                                    menu:
                                                        newbaptistwoman "Wait, are you Jewish?"

                                                        "Yes, I'm Jewish.":
                                                            newbaptistwoman "'Then answered all the people, and said, His blood be on us, and on our children.'"

                                                            newbaptistwoman "Matthew 27:25."

                                                            newbaptistwoman "Then you know that you must accept Christ as the Messiah, or you will be cursed?"

                                                            #End

                                                        "No, I'm not Jewish.":
                                                            newbaptistwoman "Then you know that Jesus Christ is the Messiah and that He will return?"

                                                            #End

                                                        "I'd rather not say.":
                                                            jump case1scene6

                                                "But what books constitute that Book? What of the Books of Esdras and the Maccabees and the Wsidom of Solomon?":
                                                    newbaptistwoman "'All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness.'"

                                                    newbaptistwoman "2 Timothy 3:16."

                                                    newbaptistwoman "Do you mean to say you are a Gnostic?"

                                                    menu:
                                                        newbaptistwoman "Do you mean to say you are a Gnostic?"

                                                        "Yes, I am.":
                                                            newbaptistwoman "There are no Gnostics."

                                                            #End

                                                        "Gnostic, no. Agnostic, yes.":
                                                            newbaptistwoman "There can be no room for doubt when we are so close to the end."

                                                            #End

                                                "There are many other Books: the Tipitaka, Mahābhārata, the Guru Granth Sahib":
                                                    newbaptistwoman "Those were not inspired by God!"

                                                    newbaptistwoman "The Pentateuch was written by Moses, the Gospels were written by the disciples."

                                                    jump case1scene6

                                        "I believe in mind, body and spirit.":
                                            newbaptistwoman "But not God?"

                                            newbaptistwoman "Without God you would not have a mind, body, or spirit!"

                                            menu:
                                                newbaptistwoman "Without God you would not have a mind, body, or spirit!"

                                                "Perhaps we just came into being, through the Universe.":
                                                    newbaptistwoman "But how did the Universe come into being?"

                                                    menu:
                                                        newbaptistwoman "But how did the Universe come into being?"

                                                        "By itself.":
                                                            newbaptistwoman "And how is that different from God?"

                                                            newbaptistwoman "Aren't you just calling Him by another name?"

                                                            jump case1scene6

                                                        "The Big Bang.":
                                                            newbaptistwoman "And how did the material for the Big Bang get there in the first place?"

                                                            newbaptistwoman "Did it come from nowhere?"

                                                            jump case1scene6

                                                        "It's impossible to answer questions about the beginning of time.":
                                                            newbaptistwoman "But it's not impossible when we have the word of God!"

                                                            jump case1scene6

                                                "What about gods, plural?":
                                                    newbaptistwoman "We have no time for new age enthusiasms."

                                                    newbaptistwoman "I made it clear we're a Christian organization."

                                                    newbaptistwoman "Have a good day."

                                                    jump case1scene6

                                        "I believe in people.":
                                            newbaptistwoman "But people are tainted by sin."

                                            menu:
                                                newbaptistwoman "But people are tainted by sin."

                                                "I don't think all people are tainted.":
                                                    newbaptistwoman "'Behold, I was shapen in iniquity, and in sin did my mother conceive me.'"

                                                    newbaptistwoman "Psalms 51:5."

                                                "There is no such thing as sin.":
                                                    newbaptistwoman "I beg to differ."

                                        "I don't believe in anything, really.":
                                            newbaptistwoman "Okay then. Thank you for your time. Have a good day."

                                            jump case1scene6

                    "No, not really.":
                        label .ofcourseitdoes:
                            newbaptistwoman "Come on, of course it does!"

                            newbaptistwoman "We've come so close to a Third World War so many times."

                            newbaptistwoman "Korea, Berlin, Cuba, Israel..."

                            newbaptistwoman "Who knows when and where the next crisis will be, and if we'll survive it."

                            jump case1scene5.ourmission

                    "I don't know.":
                        jump .ofcourseitdoes

                    "I don't see how this connects to your organization.":
                        jump .ourmission

            "I actually wanted to speak to your friend.":
                newbaptistwoman "Oh, do you know Levi?"

                menu:
                    newbaptistwoman "Oh, do you know Levi?"

                    "I thought his name was Michael.":
                        newbaptistwoman "Perhaps it once was, but he's Levi now."

                        newbaptistwoman "Let me get him."

                        jump .letmegetleviforyou

                    "Not properly, but... I think I might have spoken to him before.":
                        newbaptistwoman "Alright, let me get him for you!"

                        jump .letmegetleviforyou

                    "He's a friend of a friend, I guess.":
                        newbaptistwoman "I'll get him for you, then!"

                        jump .letmegetleviforyou

        label .letmegetleviforyou:
            "The woman goes to 'Levi' and takes over speaking with the couple."

            "'Levi' approaches you."

            michaelbloom "Hi there... Do I know you?"

            menu:
                michaelbloom "Hi there... Do I know you?"

                "We were in Berkeley together. We never spoke though. I'm [firstname].":
                    michaelbloom "Oh wow, that's crazy!"

                    michaelbloom "My friend and I, we're collecting for a Christian charitable organization."

    #### Case 1 Scene 6 ####

    label case1scene6:
        "You see the SUV approach."

        "David quickly gets out and bundles Michael into the back seat."

        "You get in the front."

        scene suv

        show davidlee at left

        show michaelbloom at right

        if not distracted:
            "As you pull away, the woman yells."

            "You hear a loud scraping sound along the side of the car."

            davidlee "Fuck, she keyed the car."

            davidlee "That'll make our lives harder."

        michaelbloom "Who the fuck are you people?"

        "Michael yanks the door handle, but it doesn't budge."

        "David binds his hands behind his back."

        michaelbloom "Get the fuck off me!"

        davidlee "Shut the fuck up before I gag you."

        davidlee "Your parents want to see you, Michael."

        davidlee "Keep driving, [firstname]."

        davidlee "Get us onto the 580 interstate, then we'll switch around."

        "You drive for ten minutes until you get to the interstate."

        "You trade places with David, getting into the back alongside Michael."

        michaelbloom "You're deprogrammers, aren't you?"

        michaelbloom "You know, the Church warns us about you."

        michaelbloom "You're liars, deceivers, tempters."

        michaelbloom "If you think you'll break me, you've got another thing coming."

        jump case1scene7

    #### Case 1 Scene 7 ####

    label case1scene7:
        scene black

        "An hour passes."

        scene case1scene7

        "Muir Beach, California."

        show davidlee at left

        show michaelbloom at right

        davidlee "We're here. [firstname], stay behind Michael as we walk him in, and keep hold of him too."

        michaelbloom "What if I scream?"

        davidlee "You're welcome to. No one will care."

        "You get out of the car and walk Michael inside."

        scene black

        jump case1scene8

    #### Case 1 Scene 8 ####

    label case1scene8:
        scene case1scene8

        show michaelbloom at center

        show davidlee at left

        show frankwilliams at right

        "As you enter, a man and a woman watch from the other side of a kitchen as Frank greets you."

        frankwilliams "Good job you two. I got this from here."

        "He takes Michael from you and walks him into another room."

        mrsbloom "You must be David and [firstname]... Can I get you some coffee or something?"

        davidlee "Thank you Mrs. Bloom, but if it's the same to you I could do with some sleep. Mind if I take the couch?"

        mrsbloom "Sure, go ahead."

        "David lays down on the couch and soon begins to snore faintly."

        mrsbloom "How about you? Coffee?"

        menu:
            mrsbloom "How about you? Coffee?"

            "Yes, please.":
                "Soon there's a hot mug in front of you."

            "No, thanks.":
                "You sit down at the counter."

        mrsbloom "Sorry, there's not really an etiquette for this kind of thing, is there?"

        mrbloom "Frank says you're new at this. You must think we're awful people. Having our own son abducted."

        mrbloom "But we're worried about him. He's never been able to... fit in. Even with other Jewish kids."

        mrbloom "And that asshole, Georgy Sokolov, he might be exploiting that."

        if not distracted:
            "The doorbell rings."

            newbaptistwoman "Open up, before we call the cops! We know you have Michael in there."

            "David gets up."

            show davidlee at center

            davidlee "Shit, they must have followed us."

            mrbloom "What do we do?"

            davidlee "Mr. Bloom, wait here with your wife."

            davidlee "Come on, [firstname], let's deal with this."

            scene case1scene7

            show davidlee at center

            "The New Baptist woman that Michael was with earlier is now flanked by three others."

            newbaptistwoman "Ah, you're... David Lee, right?"

            newbaptistwoman "Yeah, we've been briefed on you. Is Frank Williams in there too?"

            "She turns to you."

            newbaptistwoman "You know what you're doing is illegal, right?"

            davidlee "What, you think you have the upper hand here?"

            davidlee "You're four crazy, anti-semitic cultists standing on the boundary of the private property of a Jewish family."

            davidlee "You're ringing the doorbell and demanding to be let in so you can take away a boy?"

            davidlee "The cops are not on your side right now."

            newbaptistwoman "We're good Christians, members of a church that does a lot of charity work, including with the Government of California."

            newbaptistwoman "You do not have the upper hand."

            davidlee "So call the cops, then. You won't take the risk."

            newbaptistwoman "Neither will you."

            "She looks at you again."

            newbaptistwoman "You seem reasonable. And young. I'm sure you've got prospects."

            newbaptistwoman "This was all a mistake."

            menu:
                newbaptistwoman "Let us in. We'll take Michael, and we can all be on our way."

                "Alright, come inside.":
                    newbaptistwoman "Good."

                    davidlee "What the fuck do you think you're doing?"

                    menu:
                        davidlee "What the fuck do you think you're doing?"

                        "I don't want this to ruin my life, David.":
                            davidlee "Then you're nothing but a selfish bastard."

                            label giveup:
                                "You lead the Church members inside, and they leave with Michael."

                                "Meanwhile, Frank, David, and the Blooms protest and scream at you."

                                "You take a taxi back to Berkeley."

                            jump roaduntaken

                        "This is more than I expected. I can't do this.":
                            davidlee "You're a fucking coward, [firstname]."

                            jump giveup

                "Not a chance.":
                    davidlee "If you lay a single fucking toe on this property, we will call the cops."

                    davidlee "Try and get into the house, and we shoot you."

                    davidlee "We're just standing our ground. Understand?"

                    "David turns and you both go back inside."

                    scene case1scene8

                    "Out of the window, you can see the Church members watching the house."

                    davidlee "Mr. Bloom, do you have a gun?"

                    mrbloom "Yes, I do... I've never fired it."

                    davidlee "Hopefully you won't have to. Get it, and keep it close."

        "Frank's voice booms from upstairs."

        frankwilliams "[firstname]! Get up here!"

        jump case1scene9

    #### Case 1 Scene 9 ####

    label case1scene9:
        scene case1scene9

        show michaelbloom at center

        show frankwilliams at left

        "As you enter the room, you see Frank stood over Michael."

        "Michael looks dishevelled, and his eyes are red."

        "Frank is breathing hard. When he speaks, his voice is hoarse."

        frankwilliams "Good, you're here."

        menu:
            frankwilliams "Good, you're here."

            "What do you need?":
                label .deprogramming:
                    frankwilliams "You're taking over from me."

                    frankwilliams "Michael here is almost done with the Church for good."

                    michaelbloom "No, I'm not."

                    frankwilliams "Yes, you are. Shut the fuck up before I gag you."

                    menu:
                        frankwilliams "Yes, you are. Shut the fuck up before I gag you."

                        "Is that really necessary, Frank?":
                            frankwilliams "Not yet it isn't."

                            jump .whatdoido

                        "What do I do?":
                            label .whatdoido:
                                frankwilliams "Keep the pressure on."

                                frankwilliams "Expose the Church for what it is."

                                frankwilliams "Expose him for what he is."

                                frankwilliams "Then he'll snap."

                                frankwilliams "I'll be here watching. Now go ahead."

                                hide frankwilliams

                                michaelbloom "Well...?"

                                label michaelbloomroot:
                                    michaelbloom "You cannot vanquish my love."

                                    show frankwilliams at right

                                    frankwilliams "Why do you love John so much?"

                                    michaelbloom "He has saved me."

                                    frankwilliams "Really? There's nothing more to it?"

                                    menu:
                                        frankwilliams "Really? There's nothing more to it?"

                                        "You know, your parents told me you never really fit in.":
                                            michaelbloom "You shut up. You don't know what you're talking about."

                                            frankwilliams "John never touched you?"

                                            michaelbloom "Only to baptize me!"

                                            frankwilliams "And you never wanted more?"

                                            michaelbloom "Who wouldn't!?"

                                            michaelbloom "With him I am loved. Unconditionally."

                                            frankwilliams "No, you're not."

                                            label .unconditionallove:
                                                menu:
                                                    michaelbloom "No, you're not."

                                                    "What happens if you stop 'volunteering'? You are hated and reviled!":
                                                        michaelbloom "And I would deserve it, too!"

                                                        jump .unconditionallove

                                                    "Georgy doesn't love you unconditionally, but your parents do.":
                                                        michaelbloom "Oh God... Oh God what have I done to them?"

                                                        "Michael puts his head in his hands, and begins to sob."

                                                        michaelbloom "Please, let me see them."

                                                        jump case1scene10

            "Are you okay?":
                frankwilliams "I'll be fine once I have some water."

                jump .deprogramming

            "Is he okay?":
                frankwilliams "He's never been better."

                jump .deprogramming

    #### Case 1 Scene 10 ####

    label case1scene10:
        scene case1scene8

        "As you come downstairs, Michael rushes to his parents."

        "They embrace, tearfully."

        show frankwilliams at center

        "Frank pulls you aside."

        frankwilliams "You did pretty good today, [firstname]."

        frankwilliams "The way I see it, cults aren't going anywhere. There's hundreds more kids like Michael out in the world."

        frankwilliams "I know you're a student but afterwards... I'll be in touch. If that's what you want."

        menu:
            frankwilliams "I know you're a student but afterwards... I'll be in touch. If that's what you want."

            "Yeah, I'd like that.":
                frankwilliams "Good. I'll see you soon."

                jump deprogrammer

            "No, thanks.":
                frankwilliams "Alright then. See you around."

                jump roaduntaken

    #### The ending where you do become a deprogrammer ####

    label deprogrammer:
        "A few months later, you complete your PhD, and head to the newly-bought headquarters of Anti-Cult Action."

        jump credits

    #### The ending where you simply do not become a deprogrammer ####

    label roaduntaken:
        scene black

        "After some time, your life goes back to normal."

        "You finish your PhD in 1979, and become a professor of psychology at UCLA."

        jump credits

    #### Credits ####

    label credits:
        "Thank you for playing."

        "Game by Morgan Brown."

        "Music by Theodora Angelidou."

        "Creative Consultancy by Alexander Ilderton and Cameron Yates."

        "Made using the Ren'Py game engine."

        "With font Silver by Poppy Works."
