﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Unaligned characters
define attendant = Character("Attendant",
    who_color = "#ffffff")
define answeringmachine = Character("Answering Machine",
    who_color = "#ffffff")

# ACM Characters
define claragarcia = Character("Clara Garcia",
    who_color = "ffffb0")
define frankwilliams = Character("Frank Williams",
    who_color = "ffffb0")
define you = Character("You",
    who_color = "ffffb0")

# The game starts here.
label start:

    # Set default values of variables

    $firstname = "Taylor"
    $lastname = "Smith"

    $cremated = False

    #### A debug menu for testing ####

    scene black

    menu:
        "Select scene."

        "Case 1, Scene 1":
            jump case1scene1

        "Case 1, Scene 2":
            jump case1scene2

        "Case 1, Scene 3":
            jump case1scene3

        "Case 1, Scene 4":
            jump case1scene4

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

                                    frankwilliams "Malcolm X, shot to death in '65."

                                    frankwilliams "Seven dead in the Tate-LaBianca murders in '69."

                                    frankwilliams "Fifteen killed by the 'Death Angels' - so-called Black Muslims - from '73 to '74."

                                    frankwilliams "A satanist shot eight people in New York City from '76 to '77."

                                    frankwilliams "Countless more have been killed by the violence of the Ku Klux Klan."

                                    frankwilliams "Oh, and I shouldn't forget: Jonestown, Guyana. Almost a thousand dead in '78."

                                    menu:
                                        "That doesn't prove your point. You just listed examples.":
                                            frankwilliams "Sorry I don't have the precise statistics to hand, but you get my meaning."

                                            frankwilliams "People are dying. I stop that from happening."

                        "Are you trying to make me feel guilty?":
                            frankwilliams "No. I'm trying to help you do something."

                            frankwilliams "I'm trying to help you move on."

                            frankwilliams "I'm trying to stop you from losing yourself."

                        "Fuck off.":
                            frankwilliams "Fuck you."

                            frankwilliams "I'm offering you the chance to stop what happened to your sister from happening to you, and you tell me 'Fuck off'?"

                            frankwilliams "You're gonna hear me out and you're gonna listen."

                            #label .hereswhatido:


    label case1scene4:
        scene black

        "Somewhere in San Francisco, California."
