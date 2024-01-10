


label arrival_reception(char1):
    $ menu_active = True
    $ start_scene()

    call show_reception_image (i_zoom=1.0) from _call_show_reception_image
    t_unknown_girl "Hello [char1.playername] and welcome to the Island!"
    call show_reception_image (i_zoom=2.0) from _call_show_reception_image_1
    "Wow! Even the receptionist is beautiful."
    $ l_breast_size_text = char1.get_breast_size_text()
    "Just look at her half-exposed [l_breast_size_text]!"
    pl "Oh Hi...?"
    t_unknown_girl "Silly me. I'm [char1.fname]. *smiles*"
    pl "Hello [char1.fname]. It's really nice to meet you."
    pause 0.5
    pl "Oh wow! I mean how is it possible that such a beautiful girl as yourself has reception duty?"
    char1.talk "Thank you for the compliment [char1.playername]."
    $ char1.change_affection(5)

    char1.talk "Reception duty is shared among the island girls."
    char1.talk "I have the morning shift this week."
    char1.talk "But in the afternoon I'm free and all yours! *smiles*"
    pause 0.4
    pl "Ummm... Really?"
    "Did that just sound like a promise?"
    pause 0.6
    char1.talk "*giggles* {i}Really{/i} that I'm free in the afternoon or that I'm all yours?"
    pl "Er... Sorry, I was just a bit surprised."
    char1.talk "Don't worry about it. And yes, I meant both!"
    pause 0.4
    char1.talk "But before we engage in other activities..."
    char1.talk "...let me give you some information about the island's facilities."
    pl "Oh yes please."
    pause 0.5
    char1.talk "The island has a beautiful beach with a pavilion, where you can relax, take a swim or go jogging."
    char1.talk "The beach isn't closed at night.\n{w}But please be careful when you walk around in the dark."
    pause 0.4
    pl "Sure, thank you."
    char1.talk "We have a nice pool at the back of the hotel with a lot of sunbeds."
    char1.talk "You can use the pool and the sunbeds whenever you want."
    char1.talk "The girls will probably be at the pool mainly during daytime."
    pl "Great, I can't wait to see it. *smiling*"
    pause 0.5
    char1.talk "I bet. The beach and the pool are {i}swimwear areas{/i}."
    char1.talk "Same for the gym, which you can use in your swimwear too, as long as it's dry."
    char1.talk "Of course, you can also wear workout clothes if you prefer."
    pause 0.5
    char1.talk "The gym has all kinds of equipment and it isn't closed at night."
    char1.talk "The girls usually only train until 6 pm but there may be some exceptions."
    pause 0.6
    char1.talk "You should talk to Jennifer, the workout instructor. Suuuiiiiii"
    char1.talk "She's at the gym each morning and will explain all the equipment."
    char1.talk "She's an expert on how to get the most out of your training."
    pause 0.5
    char1.talk "There is also a spa, which I really love."
    char1.talk "It's open from 3 pm to 7 pm."
    char1.talk "You can get a relaxing massage there or if you're lucky even something more.. *smirks*"
    pause 0.5
    pl "Er...? Something more?"
    char1.talk "Just see for yourself and talk to the masseuse."
    char1.talk "If she likes you well enough. Who knows..."
    pl "Oh! Okay. *smiling*"
    char1.talk "Of course there is a restaurant as well."
    char1.talk "We couldn't have you starving now, could we. *smiles*"
    char1.talk "It's open for breakfast, lunch and dinner."
    pause 0.6
    char1.talk "We have a night bar, where you can enjoy a drink or just spend some time with the ladies."
    char1.talk "Some might even pole dance or play poker with you. *smiling*"
    char1.talk "The bar is open from 10 pm to 2 am."
    pause 0.4
    char1.talk "And we have a doctor on the island."
    char1.talk "Everyone should see her after arriving on the island."
    char1.talk "So please pay her a visit as soon as possible."
    char1.talk "The doctor's office will be open at 8 am."
    pause 0.5
    pl "Okay, sure. I'll do so."
    "Since she was referring to the doctor by {b}her{/b}..."
    "...so the doctor's a woman too."
    char1.talk "One more thing before I'll let you enjoy the island."
    char1.talk "Here's the key to your room."
    pl "Thanks."
    char1.talk "It's on the second floor. You can use the elevator or the stairs to get there."
    pause 0.6
    char1.talk "I know that was a lot to take in but do you have any other questions?"
    pl "No, not right now."
    char1.talk "If anything comes up, just ask the receptionist."
    char1.talk "Reception is open 24/7."
    pl "That's great, thank you [char1.fname]."
    pause 0.5
    char1.talk "Oh... there's one last thing which I almost forgot."
    char1.talk "To learn your way around the island, I have some tasks for you. *smiles*"
    pause 0.4
    "A little suspicious..."
    pl "What kind of {i}tasks{/i} are we talking about?"
    char1.talk "Just some things to help you learn how everything works around here."
    menu:
        "Play the intro quest line" if True:
            pl "That sounds great. Thank you."
            char1.talk "You're welcome."
            $ player.add_quest("Intro_main", reception, reception)
            $ player.add_quest("Intro_doctor", reception, doctor)
            $ player.add_quest("Intro_plane_girl", reception, plane_girl)
            $ player.add_quest("Intro_facilities", reception, reception)
            char1.talk "To check the progress on your quests, or if you need a hint on what to do next, open your phone and use the app labeled\n{b}Show task and quest list{/b}."
            pl "I'll do that. Thanks again."
        "You already know your way around the island" if True:

            pl "Thank you, but I don't think that will be necessary. I already know my way around here."
            char1.talk "That's fine too."
            $ player.add_quest("Intro_main", reception, reception)
            $ player.set_quest_state("Intro_main", reception, 100, True)
            $ player.add_quest("Intro_doctor", reception, doctor)
            $ player.set_quest_state("Intro_doctor", doctor, 100, True)
            $ player.add_quest("Intro_plane_girl", reception, plane_girl)
            $ player.set_quest_state("Intro_plane_girl", plane_girl, 100, True)
            $ player.add_quest("Intro_facilities", reception, reception)
            $ player.set_quest_state("Intro_facilities", reception, 100, True)

    pause 0.4
    char1.talk "See you around [char1.playername]."
    pl "Bye."

    label arrival_reception_end:
    call actions_used (1) from _call_actions_used_183
    $ char1.introduced = True
    "Before exploring the island, you walk to your room to get rid of your luggage."
    $ stop_scene()
    $ location = "player_room"
    $ menu_active = False
    return "nothing"





label show_reception_image(i_zoom=1.0, i_transition=dissolve, i_pause=0.6, i_clothes="reception2", i_focus="face", i_char=jobs.reception, i_base_image="", i_overlay_image="", i_xalign=0.5, i_use_ypos=False):
    $ l_zoom_char = 0.53
    $ l_char_ypos = 0
    $ l_yalign = 0.26
    $ l_clothes = i_clothes
    if unicode(i_clothes.startswith("reception")) and (g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar"):
        $ l_clothes = "restaurant"

    if l_clothes == "reception" or l_clothes == "reception1":
        $ l_char_image = im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_reception" + unicode(i_char.receptionwear) + "_base.webp", l_zoom_char*2.0)

    elif l_clothes == "reception2":
        $ l_char_image = im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_reception" + unicode(i_char.receptionwear) + "_base2.webp", l_zoom_char*2.0)

    elif l_clothes == "doctor":
        $ l_char_image = im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_doctor" + unicode(i_char.doctorwear) + "_base.webp", l_zoom_char*2.0*1.7)
        $ l_char_ypos = 350

    elif l_clothes == "night" or l_clothes == "swim" or l_clothes == "restaurant":
        if l_clothes == "night":
            $ l_x_size,l_y_size = renpy.image_size("characters/" + i_char.fname + "/" + i_char.fname + "_night" + unicode(i_char.nightwear) + "_base.webp")
        elif l_clothes == "swim":
            $ l_x_size,l_y_size = renpy.image_size("characters/" + i_char.fname + "/" + i_char.fname + "_swim" + unicode(i_char.swimwear) + "_base.webp")
        elif l_clothes == "restaurant":
            $ l_x_size,l_y_size = renpy.image_size("characters/" + i_char.fname + "/" + i_char.fname + "_night" + unicode(i_char.dinerwear) + "_base.webp")
        if i_char.id <> ivy.id:
            $ l_zoom_adjust = 2160.0 / float(l_y_size) * 0.89
            $ l_zoom_char *= l_zoom_adjust
        if i_char.id == yvette.id:
            $ l_char_ypos = 480
        elif i_char.height_type == 3:
            $ l_char_ypos = 330
        elif i_char.height_type == 2:
            $ l_char_ypos = 380
        elif i_char.height_type == 1:
            $ l_char_ypos = 450

        if l_clothes == "night":
            $ l_char_image = im.MatrixColor(im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_night" + unicode(i_char.nightwear) + "_base.webp", l_zoom_char*2.0), im.matrix.brightness(0.05)*im.matrix.saturation(1.05))
        elif l_clothes == "swim":
            $ l_char_image = im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_swim" + unicode(i_char.swimwear) + "_base.webp", l_zoom_char*2.0)
        elif l_clothes == "restaurant":
            $ l_char_image = im.MatrixColor(im.FactorScale("characters/" + i_char.fname + "/" + i_char.fname + "_night" + unicode(i_char.dinerwear) + "_base.webp", l_zoom_char*2.0), im.matrix.brightness(0.05)*im.matrix.saturation(1.05))

    $ l_image = Composite((5120,2880), (0,0), im.FactorScale("locations/loc_reception_layer1.webp",2.0), (2000,l_char_ypos), l_char_image, (0,0), im.FactorScale("locations/loc_reception_layer2.webp",2.0))

    if i_char.id == ivy.id:
        $ l_yalign = 0.1
    elif i_char.id == yvette.id:
        $ l_yalign = 0.5
    elif i_char.height_type == 1:
        $ l_yalign = 0.42
    elif i_char.height_type == 2:
        $ l_yalign = 0.3

    if i_base_image == "":
        scene expression l_image:
            zoom i_zoom * 0.25 align (0.5,l_yalign)
        with i_transition
    elif True:
        scene expression i_base_image:
            zoom 0.5
        if i_use_ypos == True:
            show expression l_char_image:
                zoom l_zoom_char * i_zoom * 0.5 xalign i_xalign ypos l_char_ypos
        elif True:
            show expression l_char_image:
                zoom l_zoom_char * i_zoom * 0.5 align (i_xalign,l_yalign+0.2)
        if i_overlay_image <> "":
            show expression i_overlay_image:
                zoom 0.5
        with i_transition
    pause 0.6
    return




label talk_reception:
    if current_action=="goto_wait" or current_action=="nothing" or current_action=="do_pl_watch_player" or current_action=="do_pl_watch_character":
        return "nothing"

    $ menu_active = True
    $ l_option1 = True
    $ l_option2 = True
    $ l_option3 = True
    $ l_option4 = True
    $ l_option5 = True
    $ l_option6 = True
    $ player.smart_watch_character = jobs.reception
    $ start_scene()

    call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_2

    if jobs.reception.introduced==True:
        if jobs.reception.receptionwear == 1 and jobs.reception.get_action_allowed("Reception_clothes1_reason") and g_receptionist_location <> "restaurant" and g_receptionist_location <> "nightbar":
            $ jobs.reception.add_action_cooldown("Reception_clothes1_reason", 40, "")
            pl "Oh wow [jobs.reception.fname]!"
            pl "That's really a super sexy outfit!"
            if jobs.reception.receptionwear1_reason == 1:
                jobs.reception.talk "*beams* So you like it?"
                pl "Yes, absolutely! It looks spectacular on you!"
                call change_char_max_affection (jobs.reception, 5) from _call_change_char_max_affection_62
                $ jobs.reception.change_affection(10)
                jobs.reception.talk "Thank you so much, you're sweet."
                jobs.reception.talk "You know, I'm wearing it just for you, because you were so nice to me this week!"
                jobs.reception.talk "Reception work can be boring when no one talks to you."
                pl "I suppose it can."
                if jobs.reception.get_action_icon_available("reception_undress") and jobs.reception.get_action_allowed("reception_undress"):
                    jobs.reception.talk "Psssst..."
                    pl "Yes?"
                    jobs.reception.talk "I know I look hot in this new top... *smiles*"
                    pause 0.5
                    jobs.reception.talk "Do you think I look even hotter out of it? *smirks*"
                    $ jobs.reception.add_pl_interaction("tease_talk")
                    pl "Umm wow [jobs.reception.fname]! I'm pretty sure you do!"
                    call action_reception_undress (jobs.reception, True, False) from _call_action_reception_undress
                    $ start_scene()
                    call show_reception_image (i_zoom=1.8) from _call_show_reception_image_13
                    jump talk_reception_menu
            elif True:

                jobs.reception.talk "So... You finally notice me this week..."
                jobs.reception.talk "Thought you were ignoring me altogether. *sulks*"
                $ jobs.reception.change_affection(-5)
                jobs.reception.talk "It can be quite lonely and boring at the reception desk when you don't get any visitors..."
                pl "I'm sorry [jobs.reception.fname]."
                pl "It was just such a busy week."
                pause 0.4
                pl "It wasn't my intention to ignore you."
                jobs.reception.talk "Anyway, I'm happy that I finally got your attention with this new outfit!"
                pause 0.7

        jobs.reception.talk "What can I do for you [jobs.reception.playername]?"
        call show_reception_image (i_zoom=2.0, i_clothes="reception2") from _call_show_reception_image_3

        if jobs.reception.receptionwear == 1 and jobs.reception.breast_size >= 2 and jobs.reception.get_action_allowed("Reception_stare_tits"):
            $ jobs.reception.add_action_cooldown("Reception_stare_tits", 80, "")
            $ breast_size_text = jobs.reception.get_breast_size_text()
            "Staring at her [breast_size_text]..."
            "...you can think of all kinds of naughty things she could do for you!"
            if jobs.reception.id == amy.id:
                pause 0.5
                jobs.reception.talk "Thinking about how the top looks unbuttoned? *smirks*"
                pause 0.3
                pl "Ummm ... No, how?"
                pause 0.4
                "Then you remember the picture from the envelope..."
                pl "Yes, that one was a nice touch! *smiles*"
                jobs.reception.talk "I knew you'd like it! *smiles back*"
    elif True:
        jobs.reception.talk "Hello [jobs.reception.playername], welcome to Holiday Island. I'm [jobs.reception.fname] How may I help you?"
        "Wow, they haven't promised too much. Even the receptionist is gorgeous..."

    label talk_reception_menu:
    menu:
        "Introduce yourself" if jobs.reception.introduced==False:
            pl "Hello [jobs.reception.fname], my name is [player.fname]. Pleased to meet you."
            jobs.reception.talk "I hope you are not offended if I call you [jobs.reception.playername] for now. At least until we know each other a little better."
            "Did that just sound like a promise?"
            pl "Okay [jobs.reception.fname], I understand. No problem."
            $ jobs.reception.introduced = True
            $ player.change_lust( -1 )
            jump talk_reception_menu

        "Stare at her chest" if jobs.reception.get_action_allowed("reception_stare_chest"):
            $ jobs.reception.add_action_cooldown("reception_stare_chest",20)
            call show_reception_image (i_zoom=3.0, i_clothes="reception2") from _call_show_reception_image_4
            "Really nice! *grinning*"
            $ player.change_lust(jobs.reception.sexiness-3)
            pause 0.7
            "You better watch your manners before you get caught."
            call show_reception_image (i_zoom=2.0, i_clothes="reception2") from _call_show_reception_image_5
            jump talk_reception_menu

        "Ask for a meeting with Joy to talk about Sara's experiments" if player.get_quest_state("Background_of_Sara_experiments", sara) == 1 and player.has_appointment(40,joy) == False:
            pl "Hey, how are things?"
            jobs.reception.talk "Things are fine around here. Thanks for asking."
            jobs.reception.talk "Can I help you with anything?"
            call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_33
            pl "I'd like to have another meeting with Joy."
            jobs.reception.talk "Is it urgent?"
            pause 0.4
            pl "I think it qualifies."
            pl "It's about Sara. She's doing some experiments down at the lab that might be dangerous."
            pause 0.4
            pl "Joy should know about that to decide for herself."
            pause 0.4
            jobs.reception.talk "Damn! This definitely sounds like an emergency to me."
            jobs.reception.talk "Let me check her schedule..."
            pause 0.6
            if actions_left <= 14:
                jobs.reception.talk "She has an open slot for emergencies this morning at 8."
            elif True:
                jobs.reception.talk "She has an open slot for emergencies tomorrow morning at 8."
            pause 0.4
            pl "That's great."
            jobs.reception.talk "Done. Meeting scheduled."
            $ player.add_appointment(40, joy, "office", 46, True)
            pl "Thank you so much [jobs.reception.fname]."
            jobs.reception.talk "Don't mention it."
            pause 0.5
            jobs.reception.talk "Is there anything else I can do for you?"
            call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_34
            jump talk_reception_menu

        "Ask if it's possible to meet with Joy to talk about Delizia's exam" if player.get_quest_state("Delizia_doctor_exam", delizia) == 0 and player.has_appointment(38,joy) == False:
            pl "Hey [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hello [jobs.reception.playername], I'm good. Thanks for asking."
            jobs.reception.talk "Do you need help with anything?"
            call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_23
            pl "Since you're asking, I could really use your help to have another meeting with Joy."
            jobs.reception.talk "Any problems?"
            pause 0.4
            pl "I don't think so. It's about Delizia."
            pl "She wants to become a doctor and she's studying a lot in her free time."
            pause 0.4
            jobs.reception.talk "Yes, she told me about it."
            jobs.reception.talk "But that's great, isn't it?"
            call show_reception_image (i_zoom=1.7, i_clothes="reception2") from _call_show_reception_image_24
            jobs.reception.talk "So why do you need to talk with Joy?"
            pause 0.4
            pl "The exam can only be done in a classroom, so She has to leave and isn't sure if Joy will allow it."
            jobs.reception.talk "So she asked you to have a word with her?"
            pause 0.4
            pl "Well, yeah. That's about it."
            jobs.reception.talk "Let me check her schedule..."
            pause 0.6
            jobs.reception.talk "She has an open slot for emergencies tomorrow morning at 10."
            pause 0.4
            pl "Ummm... I'm not sure if this qualifies as an emergency."
            jobs.reception.talk "I think it does. *smiles*"
            pl "Okay, if you say so."
            jobs.reception.talk "Yup, here we go. Meeting scheduled."
            $ player.add_appointment(38, joy, "office", 42, True)
            pl "Thanks a lot [jobs.reception.fname]."
            jobs.reception.talk "Don't mention it."
            pause 0.5
            jobs.reception.talk "Is there anything else I can do for you?"
            call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_25
            jump talk_reception_menu

        "Ask if it's possible to meet with Joy to talk about Sara's night out" if player.get_quest_state("Self_tan_lotion", miriam) == 3:
            pl "Hello [jobs.reception.fname], how's it going?"
            jobs.reception.talk "I'm good, although reception duty isn't really my favorite pastime."
            jobs.reception.talk "I'd rather hang out at the pool or the beach. *smiles*"
            pl "That's understandable."
            pause 0.4
            jobs.reception.talk "But I guess you didn't come here to listen to my complains.\nWhat can I do for you?"
            pause 0.5
            pl "It's about Sara."
            pl "I think she's developing a case of cabin fever and is getting a little itchy having to work at the lab all day."
            pl "She'd love to get out and visit the night bar once a week."
            call show_reception_image (i_zoom=2.0, i_clothes="reception1") from _call_show_reception_image_9
            jobs.reception.talk "Okay. So why doesn't she?"
            pause 0.4
            pl "Dr. Rosario isn't happy with it."
            jobs.reception.talk "Oh..."
            pause 0.4
            pl "If I could talk with Joy about the situation..."
            pl "...maybe she can put in a good word for Sara."
            pause 0.4
            pl "I mean, it's just once a week and Sara is a fun girl to have around."
            pause 0.4
            jobs.reception.talk "Let me check her schedule..."
            "[jobs.reception.fname] walks over to the computer and types on the keyboard."
            pause 0.6
            call show_reception_image (i_zoom=1.7, i_clothes="reception2") from _call_show_reception_image_10
            jobs.reception.talk "She has an open slot for emergencies tomorrow morning at 11."
            jobs.reception.talk "I think this qualifies for an emergency. *winks*"
            jobs.reception.talk "I mean {i}cabin fever{/i}, it sounds dangerous."
            pause 0.4
            pl "Thank you very much, [jobs.reception.fname]."
            jobs.reception.talk "You're welcome."
            jobs.reception.talk "And there's one more thing. Joy loves red roses. So if you want me to, I can have one delivered to her office before your meeting."
            jobs.reception.talk "It just might put her in a good mood."
            pl "Good to know. Yes, that would be great."
            pl "And thanks again."
            if player.company_favor >= 10:
                jobs.reception.talk "Since it's a present from you, you should pay for it. *smiles*"
                pl "Yes, of course."
                jobs.reception.talk "The rose is 10 company favor."
                $ player.change_company_favor(-10)
                pause 0.4
                jobs.reception.talk "Thanks. I'll make sure it's delivered in time."
            elif True:
                jobs.reception.talk "You're broke, [jobs.reception.playername]."
                jobs.reception.talk "Okay... Since it's for a good cause, just this once, I'll pay for you."
                pl "Oh wow! Thank you so much."
                jobs.reception.talk "Don't mention it. I'll make sure the rose is delivered in time."

            $ player.add_appointment(36, joy, "office", 40, True)
            $ joy.add_action_cooldown("Appointment_sara_night_out", 2*48)
            gameplayinfo "An appointment has been added to your calendar."
            $ player.inc_quest_state("Self_tan_lotion", miriam, True)
            jobs.reception.talk "Anything else I can do for you?"
            call show_reception_image (i_zoom=2.0, i_clothes="reception2") from _call_show_reception_image_11
            jump talk_reception_menu

        "Tell [jobs.reception.fname] that you have completed sub-quest about the island facilities" if player.get_quest_state("Intro_facilities", reception) == 5:
            pl "Hey [jobs.reception.fname], I just wanted to let you know, that I've finished the quest line about the island facilities."
            jobs.reception.talk "And you're telling me this because...?"
            pause 0.4
            pl "Ummm..."
            jobs.reception.talk "Haha! *laughs* I was just kidding. You're here for the reward, right?"
            pl "Yeah. *smiling sheepishly*"
            jobs.reception.talk "Okay. The fist thing I have for you are 20 company favor."
            $ player.change_company_favor(20)
            pause 0.4
            pl "Thanks!"
            pause 0.6
            jobs.reception.talk "The second part of the reward is a little more {i}personal{/i}. *smirks*"
            jobs.reception.talk "But we need a little more space."
            pl "Ummm... Okay."
            "You take a step back from the reception desk..."
            $ stop_scene()
            call main_game_background (location, location_detail, _return) from _call_main_game_background_144
            show screen main_game(location)
            pause 0.4
            "...while she walks around it towards you."
            call action_closeup (jobs.reception, location, False, False) from _call_action_closeup_33
            "Before she turns around, leans into you and guides your hand towards her breast..."
            call action_grope (jobs.reception, location, True, 0) from _call_action_grope_5
            show screen main_game(location)
            pl "Oh wow!"
            jobs.reception.talk "I knew you'd like that. *smiles*"
            pl "*gulp* Yeah... {w}I certainly did!"
            $ player.set_quest_state("Intro_facilities", reception, 100, True)
            $ start_scene()
            call show_reception_image (i_zoom=2.0) from _call_show_reception_image_6
            jobs.reception.talk "Is there anything else I can do for you? *grins*"
            pl "Ummm..."
            jump talk_reception_menu

        "Ask to have a meeting set up with Joy to get a new quest from the desires and wishes mailbox." if l_option5 == True and player.get_quest_state("Joy_mini_quests", joy) == 1:
            $ l_option5 = False
            pl "Hello [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hi [jobs.reception.playername], I'm good. Thanks for asking."
            jobs.reception.talk "Is there anything I can help you with?"
            pause 0.5
            pl "Yes, there is something."
            pl "Could you set up a meeting with Joy for me?"
            pl "I'd like to talk with her about the desires and wishes mailbox."
            pause 0.6
            jobs.reception.talk "Let me check her schedule..."
            pause 0.8
            "She walks to the computer and types on the keyboard."
            if player.get_action_allowed("Joy_mini_quests") == False:
                jobs.reception.talk "I'm really sorry, but Joy isn't available for meetings at the moment, except for emergencies."
                jobs.reception.talk "Is it an emergency?"
                pl "No, not really."
                jobs.reception.talk "Okay. In that case, please check back in a couple of days."
                pl "Okay, I'll do that."
                jobs.reception.talk "Anything else I can do for you, [jobs.reception.playername]?"
                jump talk_reception_menu
            elif True:
                jobs.reception.talk "She's available tomorrow at 9 am."
                jobs.reception.talk "Does this work for you?"
                pl "Yes, that should work."
                jobs.reception.talk "I'll send you an invite from her account."
                $ l_message = joy.create_message(19, 44, True)
                $ player.add_conversation(l_message)
                $ player.inc_quest_state("Joy_mini_quests", joy)
                pl "Many thanks."
                jobs.reception.talk "You're welcome."

        "Ask about the red underwear set for Alice" if player.get_quest_state("Lingerie_presents1_Alice", alice) == 3 and jobs.reception.id <> alice.id:
            pl "How's it going [jobs.reception.fname]?"
            jobs.reception.talk "Hey [jobs.reception.playername]. The very opposite of busy, so I'm happy you've dropped by. *smiles*"
            jobs.reception.talk "How can I assist you?"
            pause 0.5
            pl "I could use some help adding some underwear for Alice to my shopping app."
            jobs.reception.talk "Okay. Do you have the brand name?"
            pl "It's {i}sweet seduction{/i}."
            pause 0.4
            jobs.reception.talk "Nice! I know that one. Not cheap, but they have great stuff."
            jobs.reception.talk "Anything else to narrow down the search?"
            pause 0.4
            pl "Yes. It's a set with a bra, panties and stockings."
            pl "It's red and it has lace applications."
            pause 0.4
            jobs.reception.talk "Do you have more?"
            pause 0.4
            pl "Ummm... Yeah... {w}The bra is only available for D cups and bigger."
            jobs.reception.talk "No problem for Alice as far as I remember. *grins*"
            pause 0.4
            pl "Er... Yeah."
            pause 0.4
            "She types something on her computer..."
            pause 0.7
            jobs.reception.talk "Found it. There's just one matching your description."
            jobs.reception.talk "I have to say it does look great. And they used a model that fills out the bra quite nicely."
            pause 0.4
            jobs.reception.talk "Let me check what measurements I need to select."
            pause 0.4
            jobs.reception.talk "Here we go..."
            pause 0.4
            jobs.reception.talk "Bra size?"
            pl "It's {b}[alice.bra_size]{/b}."
            jobs.reception.talk "Hips size?"
            pl "It's {b}[alice.hips_size]{/b}."
            jobs.reception.talk "And they also need the height. Probably for the stockings."
            jobs.reception.talk "Do you know how tall Alice is?"
            pl "Yes. {b}[alice.body_height]{/b}."
            pause 0.3
            "She types some more on her computer..."
            pause 0.6
            jobs.reception.talk "That's all. I've added the set for Alice to your shopping app."
            call actions_used (1) from _call_actions_used_407
            $ player.set_quest_state("Lingerie_presents1_Alice", alice, 10, True)
            pl "That's great. Thanks a lot!"
            jobs.reception.talk "You're welcome. I'm here to help. *smiles*"
            jobs.reception.talk "Is there anything else you need?"
            jump talk_reception_menu

        "Ask about the light blue underwear for Yvette" if player.get_quest_state("Lingerie_presents1_Yvette", yvette) == 2 and jobs.reception.id <> yvette.id:
            pl "Hey [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hi [jobs.reception.playername], I'm fine. thanks for asking."
            pause 0.5
            jobs.reception.talk "Is there anything I can help you with?"
            pause 0.4
            pl "Since you're asking, there really is."
            pl "I wanted to get Yvette a present, a light blue lingerie she mentioned."
            jobs.reception.talk "What's the occasion?"
            pl "Nothing special, I just wanted to bring her a little joy."
            pause 0.4
            jobs.reception.talk "Oh wow! That's really nice of you. Yvette is a lucky girl."
            "Is she a bit jealous?"
            jobs.reception.talk "Don't give me that look! *grins*"
            jobs.reception.talk "What do you need me to do?"
            pause 0.4
            pl "Okay, here's what I have so far."
            pl "It's a set of a light blue bra and matching thong."
            pause 0.5
            pl "The bra isn't a push-up bra."
            jobs.reception.talk "Light blue? That's not something you see very often."
            jobs.reception.talk "Do you know the brand or the shop where she saw it?"
            pause 0.4
            pl "{i}Lucky guy{/i} or {i}happy boyfriend{/i} or something like that."
            pl "Does this tell you anything?"
            jobs.reception.talk "Hmmmm...."
            jobs.reception.talk "{i}Lucky boyfriend{/i} maybe?"
            jobs.reception.talk "It's a very expensive brand but fortunately they sell online."
            pl "Sounds good. Can you check their shop?"
            jobs.reception.talk "Sure."
            "She types something on her computer..."
            pause 0.8
            jobs.reception.talk "There are only three light blue underwear sets listed..."
            pause 0.4
            jobs.reception.talk "Two are with thongs..."
            pause 0.4
            jobs.reception.talk "One is only available up to cup size C and it's a push-up bra."
            pause 0.4
            jobs.reception.talk "The other one is not a push-up bra...{w}\n...and it's available up to J cups."
            pause 0.4
            pl "I hope that's the right one."
            jobs.reception.talk "It looks great in any case. I'm pretty sure she'll like it."
            jobs.reception.talk "Do you know her bra size?"
            pl "Yes, it's {b}[yvette.bra_size]{/b}."
            jobs.reception.talk "Oh wow! That's impressive on her small frame."
            pause 0.6
            jobs.reception.talk "Okay, and the hip size for the thong?"
            pl "Hip size is {b}[yvette.hips_size]{/b}."
            jobs.reception.talk "That should be all. I've added it to your shopping app."
            call actions_used (1) from _call_actions_used_408
            $ player.set_quest_state("Lingerie_presents1_Yvette", yvette, 10, True)
            pl "Thanks a lot!"
            jobs.reception.talk "Don't mention it. Anything else I can do for you?"
            jump talk_reception_menu

        "Ask to have an orange rose for Amy added to your shopping app" if player.get_quest_state("Affection_max_level5_A", amy) == 4 and jobs.reception.id <> amy.id:
            pl "Hi [jobs.reception.fname], how are you today?"
            jobs.reception.talk "Hello [jobs.reception.playername]."
            jobs.reception.talk "I'm fine, thanks for asking."
            jobs.reception.talk "Anything I can help you with?"
            pl "In fact, there really is."
            pl "I'd like to get a rose for Amy. An orange rose."
            pl "Unfortunately I can't get one with my shopping app."
            jobs.reception.talk "So you'd like me to add one for you?"
            pl "Yes, that'd be great."
            jobs.reception.talk "Let me check if I can find one for you."
            pause 0.6
            "She types something on her computer..."
            pause 0.8
            jobs.reception.talk "Here we go! This one looks nice."
            jobs.reception.talk "Oh damn! It's really expensive."
            pause 0.4
            pl "It's okay, I'd really love to have a nice one."
            jobs.reception.talk "Okay. I've added it to your shopping app."
            pl "Thank you, [jobs.reception.fname]"
            $ player.set_quest_state("Affection_max_level5_A", amy, 10, True)
            call actions_used (1) from _call_actions_used_212
            jobs.reception.talk "Anything else I can do for you?"
            jump talk_reception_menu

        "Ask to have the workout outfit for Amy added to your shopping app" if l_option4 and player.get_quest_state("Love_max_level3_A", amy) == 3 and jobs.reception.id <> amy.id:
            $ l_option4 = False
            pl "Hi [jobs.reception.fname], how was your day?"
            jobs.reception.talk "Hello [char1.playername]."
            jobs.reception.talk "Not a lot going on today. How may I help you?"
            pl "Jennifer sends me to have this outfit (you show her the picture on your phone) added to my shopping app."
            jobs.reception.talk "She mentioned something like that."
            jobs.reception.talk "Let me check if the measurement data has been transferred already..."
            pause 0.6
            "She types something on her computer..."
            pause 0.8
            if player.get_action_allowed("Amy_workout_outfit") == False:
                jobs.reception.talk "I'm sorry, but it's not there yet. Can you come back a little later?"
                pl "Sure, I can do that."
                pl "Do you know when it will be available?"
                jobs.reception.talk "Sorry, it doesn't say."
                pause 0.4
                pl "Mmm... *musing* {w}Thank you for the information."
            elif True:
                jobs.reception.talk "Yes, it's all there. I've added the outfit to your shopping app."
                jobs.reception.talk "I hope she's worth it, because it's quite expensive."
                pl "I think she is. *smiling*"
                jobs.reception.talk "*smiles back*"
                $ player.set_quest_state("Love_max_level3_A", amy, 10)
                call actions_used (1) from _call_actions_used_213
            pause 0.6
            jobs.reception.talk "Anything else I can do for you?"
            jump talk_reception_menu

        "Ask to get access to {b}Buymetons{/b}" if l_option1 and player.get_quest_state("Aly_breast_development",aly) == 4:
            $ l_option1 = False
            if jobs.reception.id == aly.id:
                "You didn't really want to ask [jobs.reception.fname] about the black rose now, did you?"
                "It would really spoil the surprise. Since she probably thinks you won't be able to get one."
                "Get back when someone else is at reception"
                jump talk_reception_menu

            pl "Hey [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "I'm fine. A bit bored, not much going on today."
            jobs.reception.talk "Can I help you with something?"
            pl "Since you ask, yes there really is something."
            pl "I'd like to have access to the shopping portal {b}Buymetons{/b} from my phone."
            pause 0.5
            pl "Would that be possible?"
            jobs.reception.talk "Ohh... to all of it? It's pretty huge. It would totally clutter the shopping app."
            jobs.reception.talk "Something specific you're looking for?"
            pl "Yes, I'm looking for a black rose."
            jobs.reception.talk "Great, that should make it easy."
            jobs.reception.talk "Let me just check in the system..."
            pause 1.5
            jobs.reception.talk "Here you go. You should have a nice black rose in your shopping app now."
            pause 0.4
            jobs.reception.talk "Oh shit! It's really expensive."
            jobs.reception.talk "Now I'm a bit jealous. Must be for someone really special..."
            pl "I hope so. *smiles*"
            pl "Thank you very much for helping me out."
            jobs.reception.talk "That's what I'm here for."
            pause 0.6
            jobs.reception.talk "Anything else I can do for you?"
            $ player.set_quest_state("Aly_breast_development", aly, 10)
            jump talk_reception_menu

        "Ask about a red stethoscope for Heather" if player.get_quest_state("Heather_sexy_nurse_outfit", heather) == 13:
            if jobs.reception.id == heather.id:
                "You didn't really want to ask [jobs.reception.fname] to help you get her own present?"
                "It would really spoil the surprise."
                "Ask when someone else is at reception."
                jump talk_reception_menu

            pl "Hello [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hey [char1.playername]."
            jobs.reception.talk "It's kind of a slow day, but I'm fine."
            jobs.reception.talk "What can I do for you?"
            pl "I was wondering if you could help me find a red stethoscope to be added to my shopping app."
            pause 0.5
            jobs.reception.talk "Ummm... What do you need a stethoscope for? And why does it have to be red?"
            pl "It's for Heather or more precisely to complete a cosplay nurse costume which she'd like to have."
            jobs.reception.talk "*chuckles* I bet you want to play doctor games with her."
            pause 0.5
            pl "Ummm... {b}No{/b}! {w}I mean it's Heather's wish. She put it on a letter in the {i}desires and wishes{/i} mailbox."
            jobs.reception.talk "I understand. So you don't want to play doctor games with her? *grinning*"
            pause 0.4
            pl "Haha, very funny. Can you help me?"
            jobs.reception.talk "Yes, I think so. Let me have a look in some of the cosplay shops."
            jobs.reception.talk "Red you said?"
            pl "Yes."
            "She types something on her computer..."
            pause 0.8
            call actions_used (1) from _call_actions_used_321
            jobs.reception.talk "I found one. It's 35 company favor."
            jobs.reception.talk "Would you like me to add it to your shopping app?"
            pause 0.4
            "35 isn't that expensive..."
            pl "Yes, please."
            jobs.reception.talk "Okay, there you go. *smiles*"
            $ player.inc_quest_state("Heather_sexy_nurse_outfit", heather, True)
            pl "Many thank."
            jobs.reception.talk "You're welcome. Have fun with it."
            jobs.reception.talk "is there anything else I can do for you?"
            jump talk_reception_menu

        "Ask if it is possible to get a battery charger or some batteries." if l_option2 and player.get_quest_state("Jessica_dildo_batteries",jessica) == 0:
            $ l_option2 = False
            if jobs.reception.id == jessica.id:
                "You didn't really want to ask [jobs.reception.fname] about the batteries, did you?"
                "Get back when someone else is at reception"
                jump talk_reception_menu
            pl "Hello [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hey [jobs.reception.playername]! I'm fine, thanks for asking."
            pause 0.4
            jobs.reception.talk "Anything I can help you with?"
            pl "Yes there is. I have a small request."
            pause 0.5
            pl "Is it possible to get a battery charger and some batteries?"
            jobs.reception.talk "Hmmm... let me think about it for a moment..."
            pause 0.4
            jobs.reception.talk "Unfortunately, we don't have any of those here."
            jobs.reception.talk "But I can add a charger and some batteries to your shopping app if you want."
            pause 0.5
            pl "That'd be great."
            jobs.reception.talk "Let me just check in the system..."
            pause 1.5
            "She types on her keyboard for a moment..."
            jobs.reception.talk "That's it. If you check your shopping app, you should be able to get a set with a charger and some batteries."
            pl "Thank you so much for the help."
            jobs.reception.talk "Don't mention it, that's what I'm here for."
            pause 0.6
            jobs.reception.talk "Anything else I can do for you?"
            $ player.set_quest_state("Jessica_dildo_batteries", jessica, 10)
            jump talk_reception_menu

        "Ask when Joy will be on the Island next time" if player.get_quest_state("Eva_breast_enhancement", eva) == 2 or player.get_quest_state("Natasha_breast_growth", natasha) == 1:
            pl "Hey [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hello [jobs.reception.playername]."
            jobs.reception.talk "I'm fine, thanks for asking."
            jobs.reception.talk "How may I help you?"
            pause 0.3
            pl "I'd like to talk with Joy."
            pl "Can you tell me when she's going to be on the island next time?"
            if player.get_quest_state("Eva_breast_enhancement", eva) == 2:
                jobs.reception.talk "Unfortunately she doesn't have a fixed schedule."
                jobs.reception.talk "But I will let her know that you want to talk to her."
                pl "Okay, great. Thank you [jobs.reception.fname]."
                $ player.inc_quest_state("Eva_breast_enhancement", eva, True)
                $ player.add_action_cooldown("joy_office3", 2*48)
            elif True:
                jobs.reception.talk "Let me check her schedule..."
                pause 0.6
                jobs.reception.talk "You're lucky, she'll be here tomorrow and she has a free slot at 10 am."
                pl "That's cool, can you make an appointment please?"
                jobs.reception.talk "Sure."
                "She types something on her computer..."
                pause 0.5
                jobs.reception.talk "Okay, all set. *smiles*"
                $ player.inc_quest_state("Natasha_breast_growth", natasha, True)
                $ player.add_appointment(19, joy, "office", 42, True)
                $ joy.add_action_cooldown("office4", 105, "")
                jobs.reception.talk "Next time you check, it should show up on your phone."

            jobs.reception.talk "Anything else I can do for you?"
            jump talk_reception_menu

        "Ask about the new room type" if player.get_quest_state("Player_room2", reception) == 2 and l_option6 == True:
            $ l_option6 = False
            pl "Hi [jobs.reception.fname], I have a question about that new room."
            jobs.reception.talk "Hi [jobs.reception.playername], so Jennifer gave you the tour?"
            pl "Yes she did. The room is incredible."
            jobs.reception.talk "And now you want to move in as quick as possible? *smiles*"
            pl "Definitely. *smiling*"
            if player.get_action_allowed("Player_room2_wait") == False:
                jobs.reception.talk "Since this is all brand new, I need to check back with Joy about that."
                jobs.reception.talk "Could you come back tomorrow. I hope to have it all clarified by then."
                pause 0.3
                pl "Oh... Okay, sure."
                "Damn! You're really curious!"
                pause 0.3
                jobs.reception.talk "Is there anything else I can do for you?"
                jump talk_reception_menu
            jobs.reception.talk "I've spoken with Joy and she said she's gonna leave it up to Jennifer, since the room was her idea."
            jobs.reception.talk "Best talk to her when she's in her room."
            jobs.reception.talk "Do you know her room number?"
            "Thinking for a moment..."
            pause 0.4
            if jennifer.room_number_known == False:
                pl "Ummm... No, I don't think so."
                jobs.reception.talk "She has room number [jennifer.room_number]."
                $ jennifer.room_number_known = True
            elif True:
                pl "Yes, I think I've got it. It's number [jennifer.room_number]."
                jobs.reception.talk "I guess I don't want to know why you have her room number... *smiles*"
                pl "Ummm..."
                jobs.reception.talk "Never mind."
            $ player.inc_quest_state("Player_room2", reception, True)
            pl "Thank you [jobs.reception.fname]."
            jobs.reception.talk "No problem."
            jobs.reception.talk "It's part of my job to answer questions. *smiles*"
            pl "*smiling back*"
            jobs.reception.talk "Anything else?"
            pause 0.3
            pl "Not right now, no."
            pl "Thanks again and bye [jobs.reception.fname]."
            jobs.reception.talk "See you later!"

        "Ask about the new room type" if (player.get_quest_state("Player_room2", reception) == 0 or player.get_quest_state("Player_room2", reception) == 1) and l_option6 == True:
            $ l_option6 = False
            pl "Hey [jobs.reception.fname], how are you doing?"
            jobs.reception.talk "Hello [jobs.reception.playername], I'm good, thank you."
            jobs.reception.talk "Is there anything I can do for you?"
            pause 0.3
            pl "Yes, I have a question concerning a letter I've received."
            pause 0.4
            jobs.reception.talk "Is it about the new room type?"
            pl "Yes, how did you know?"
            jobs.reception.talk "There are not that many letters sent out. So it was an easy guess."
            jobs.reception.talk "You'd like to have a tour?"
            pl "Yeah, that'd be pretty cool."
            if actions_left > 22 or actions_left < 14 or cl_functions.get_bartender() == jennifer:
                jobs.reception.talk "Sure, if you come back between 8 pm and midnight when Jennifer is not working in the bar, she can give you the tour."
                if player.get_quest_state("Player_room2", reception) < 1:
                    $ player.inc_quest_state("Player_room2", reception, True)
                pl "Okay, thank you [jobs.reception.fname]."
                jobs.reception.talk "You're welcome. Anything else I can do for you?"
                jump talk_reception_menu
            elif True:
                jobs.reception.talk "You're lucky, Jennifer is free right now and can give you the tour."
                jobs.reception.talk "Do you want me to tell her to come to reception and show you the room?"
                menu:
                    "Yes, please" if True:
                        pl "Yes, that'd be great."
                        pause 0.3
                        pl "How long do you think it's gonna take Jennifer to get here?"
                        jobs.reception.talk "Just a few minutes. I will contact her right away."
                        pl "Thank you."
                        "[jobs.reception.fname] types something into her keyboard..."
                        jobs.reception.talk "I've contacted her. She should be here any minute now."
                        pl "Great, thanks again."
                        if player.get_quest_state("Player_room2", reception) < 1:
                            $ player.inc_quest_state("Player_room2", reception, False)
                        "You take another look at [jobs.reception.fname] trying to start some small talk..."
                        "...but just then Jennifer comes down the stairs."
                        pl "Oh! She's already here."
                        pl "Bye [jobs.reception.fname]."
                        jobs.reception.talk "See you later [jobs.reception.playername]!"
                        call new_player_room_show_event (jennifer) from _call_new_player_room_show_event
                    "Maybe later" if True:

                        pl "Oh... I was just asking out of general curiosity."
                        pl "I will check back later for a tour, okay?"
                        jobs.reception.talk "Sure no problem."
                        jobs.reception.talk "Anything else I can do for you?"
                        jump talk_reception_menu

        "Ask for the keys to the new room" if player.get_quest_state("Player_room2", reception) == 5:
            pl "Hi [jobs.reception.fname]!"
            jobs.reception.talk "Hey [jobs.reception.playername]!"
            jobs.reception.talk "So you've come to get access to your new room?"
            pause 0.3
            pl "Yes, exactly. How did you know?"
            jobs.reception.talk "Jennifer contacted me and told me you're very excited to move in."
            jobs.reception.talk "I've already arranged to have all your luggage and personal things moved in."
            pause 0.3
            pl "Oh, so fast... That's great!"
            jobs.reception.talk "So here is the access card..."
            jobs.reception.talk "I've also arranged to unlock the door between your old room and the new one."
            $ player.room2 = True
            $ player.set_quest_state("Player_room2", reception, 100)
            $ joy.add_queued_sexting(501,512,6)
            jobs.reception.talk "You can use any one of them and move freely between the two whenever you feel like it."
            pl "That's cool too. There are so many memories you know..."
            jobs.reception.talk "*giggles* Yeah, I can believe that!"
            pause 0.3
            jobs.reception.talk "Oh and before I forget, there is one other thing."
            jobs.reception.talk "It's about the picture frames..."
            pause 0.3
            pl "Yes, what about them? Jennifer explained how they work..."
            pause 0.3
            jobs.reception.talk "Sorry, but there is an additional fee for the frames."
            jobs.reception.talk "To activate one will cost 150 company favor."
            pl "Hmmm... okay..."
            jobs.reception.talk "I'm really sorry, but Joy makes all these rules..."
            jobs.reception.talk "Just come back here if you want to have another frame activated."
            pl "Sure, I'll do that."
            jobs.reception.talk "And now... Don't let me keep you from checking out the room!"
            pl "Thanks, see you later [jobs.reception.fname]."
            jobs.reception.talk "Bye [jobs.reception.playername]!"

        "Ask to activate a picture frame in your new room" if player.get_quest_state("Player_room2", reception) == 100 and player.room2_pictures < 3:
            if player.room2_pictures == 0:
                pl "Hi [jobs.reception.fname], I'd like to get access to the first picture frame."
            elif player.room2_pictures == 1:
                pl "Hi [jobs.reception.fname], I'd like to get access to the second picture frame."
            elif True:
                pl "Hi [jobs.reception.fname], I'd like to get access to the last picture frame."
            if player.company_favor < 150:
                jobs.reception.talk "Unfortunately you don't have the necessary 150 company favor right now."
                pl "Ummm... Okay. I will check back later."
            elif True:
                jobs.reception.talk "Okay, the cost is still the same, 150 company favor."
                jobs.reception.talk "Do you wish to pay the 150 to enable it?"
                menu:
                    "Yes" if True:
                        pl "Yes please, that's why I came here. *smiling*"
                        jobs.reception.talk "Okay, let me just activate it."
                        "[jobs.reception.fname] types something on her computer..."
                        $ player.change_company_favor(-150)
                        $ player.room2_pictures += 1
                        jobs.reception.talk "It's done. You have access now."
                        pl "Great, thank you."
                        jobs.reception.talk "You're welcome."
                        jobs.reception.talk "See you around."
                        pause 0.3
                        pl "Sure, bye [jobs.reception.fname]!"
                    "No" if True:

                        pl "I'm not sure yet, maybe later."
                        jobs.reception.talk "Sure no problem."
                        jobs.reception.talk "Anything else I can do for you?"
                        jump talk_reception_menu

        "Ask for information about island locations" if l_option3:
            $ l_option3 = False
            pl "Can you tell me something more about the Island?"
            jobs.reception.talk "Certainly, that's what I'm here for. Among other things. *smiles*"
            jobs.reception.talk "This is the schedule for our restaurants:\nBreakfast is from 07:00 to 09:00 \nLunch is from 12:00 to 14:00 \nDinner is from 18:00 to 21:00"
            jobs.reception.talk "The bar is open between 22:00 and 02:00"
            jobs.reception.talk "Morning yoga at the beach is at 09:00 each Monday and Thursday.\nBut it's girls only, so don't expect to be welcomed."
            jobs.reception.talk "The spa is open from 15:00 to 20:00."
            if player.get_action_allowed("Sauna_unknown") == False and mercedes.active == True:
                jobs.reception.talk "The sauna is inside the spa and open from 15:00 to 20:00 every day."
                jobs.reception.talk "Only Tuesdays and Fridays are mixed sauna days. All other days, you won't be allowed in since it's girls only."
            jobs.reception.talk "Then there is the pool area. There aren't any closing hours, so you can go there whenever you want."
            jobs.reception.talk "Same holds true for the beach and the gym. Both are also always open."
            if yumiko.active == False:
                jobs.reception.talk "When it's not raining, the beach bar will be open from 14:00 to 18:00, once the bartender has arrived."
            elif True:
                jobs.reception.talk "We have a beach bar that is open from 14:00 to 18:00 except when it's raining."
            jobs.reception.talk "And last but not least, the doctor's office is open daily from 08:00 to 16:00."
            pause 0.6
            jobs.reception.talk "Is there anything else you'd like to know?"
            jump talk_reception_menu

        "Ask her to remove her top for you" if jobs.reception.get_action_icon_available("reception_undress") and jobs.reception.get_action_allowed("reception_undress") and g_receptionist_location <> "restaurant" and g_receptionist_location <> "nightbar":
            call action_reception_undress (jobs.reception) from _call_action_reception_undress_1
            $ start_scene()
            call show_reception_image (i_zoom=1.8) from _call_show_reception_image_14
            jump talk_reception_menu

        "Ask for a new girl to be invited to the island" if gameday >= 10 and len(list_of_characters) < get_max_chars_on_island() and len(player.chars_invited) == 0:
            pl "I would like to invite a girl of my choosing to the island.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Inviting a girl of your choosing will cost 100 company favor."
            if player.company_favor < 100:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "Here's the list of girls. Once you select a girl,\nwe will remove 100 company favor from your balance."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_1
                show screen main_game(location)
                call invite_specific_girl_to_island ("reception") from _call_invite_specific_girl_to_island_1
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-100)
                    $ l_char_invited = player.chars_invited[len(player.chars_invited)-1]
                    jobs.reception.talk "[l_char_invited.char.fname] should arrive tomorrow."
                    pl "Thank you very much [jobs.reception.fname]."
                    if player.get_quest_state("Yvette_worry_about_sister", yvette) == 1 and l_char_invited.char.id == yvette.id:
                        $ player.inc_quest_state("Yvette_worry_about_sister", yvette, True)
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."

        "Ask for a girl to be sent home, away from the island" if (gameday >= 10 and len(list_of_characters) >= 9) or player.get_quest_state("Yvette_worry_about_sister", yvette) == 0:
            pl "I would like to send a girl home.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Sending a girl of your choice home will cost 50 company favor."
            if player.company_favor < 50:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "This is the list of girls. Once you select a girl,\nwe will remove 50 company favor from your balance."
                jobs.reception.talk "Here's a warning. Most of the girls probably won't like to be send home."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_3
                show screen main_game(location)
                call remove_specific_girl_from_island ("reception") from _call_remove_specific_girl_from_island
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-50)
                    jobs.reception.talk "Your selected girl will be send home.

                    She might still perform some duties but won't disturb you otherwise."
                    pl "Thank you very much [jobs.reception.fname]."
                    if player.get_quest_state("Yvette_worry_about_sister", yvette) == 0:
                        $ player.inc_quest_state("Yvette_worry_about_sister", yvette, True)
                        $ player.add_action_cooldown("Yvette_worry_about_sister_come_back", 7*48)
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."
        "Why I can't send a girl home?" if len(list_of_characters) < 9:#Ja uz salas ir mazāk par 9 dalībniekie, tad paŗādās dotā izvēle jautājumu sarakstā pie administrācijas
            pl "I would like to send a girl home.\nIs that possible?"
            $ num_of_girls = len(list_of_characters)
            $ max_char = get_max_chars_on_island()
            $ subtr_char = get_max_chars_on_island()-len(list_of_characters)#mainīgais parāda cik var uzaicināt meitenes 
            jobs.reception.talk "Sorry, but you can't send anyone because the minimum number of girls has been exceeded: 9 girls, but now on the island : [num_of_girls] girls"
            jobs.reception.talk "You can invite [subtr_char] girls"
        "Why I can't invite a girl on island?" if len(list_of_characters) == get_max_chars_on_island():#Ja uz salas ir maksimālais dalībnieku skaits, tad paŗādās dotā izvēle jautājumu sarakstā pie administrācijas
            pl "I would like to invite a girl.\nIs that possible?"
            $ num_of_girls = len(list_of_characters)
            $ max_char = get_max_chars_on_island()
            jobs.reception.talk "Sorry, but you can't invite anyone because the maximum number of girls has been exceeded: [max_char] girls, and  now on the island : [num_of_girls] girls"
        "What option can you offer for quick earnings?" if player.company_favor< 101:##Ja spēlētājam ir mazāk par 101 monētu, tad paŗādās dotā izvēle jautājumu sarakstā pie administrācijas
            $num_of_girls2 = len(list_of_characters)
            $num_of_girls3 = (len(list_of_characters)-1)
            $max_char = get_max_chars_on_island()
            menu:#Spēlētājs izvēlnē var izvēlēties cik viņš grib nopelnīt naudas
                "Answer the question and get 100 company favor":
                    $answer1=0
                    $answer2=0
                    $answer3=0
                    $answer4=0
                    $answer5=0
                    $attempts = 0
                    $correct_answers = 0
                    while attempts < 5 and correct_answers < 3:#spēle turpinās kāmer nav izmantotas 5 iespējas vai nav uzminēts 3 reizes
                        $girl_name = renpy.input("Enter a girl's name: ")#Spēlētājs ievada meitenes vārdu
                        #Tiek pārbaudīts vai ir spēle meitene ar tādu vārdu
                        if girl_name.lower() == "alice" or girl_name.lower() == "aly" or girl_name.lower() == "amy" or girl_name.lower() == "brenda" or girl_name.lower() == "delizia" or girl_name.lower() == "desire" or girl_name.lower() == "eva" or girl_name.lower() == "faye" or girl_name.lower() == "heather" or girl_name.lower() == "Ivy" or girl_name.lower() == "jessica" or girl_name.lower() == "lacey" or girl_name.lower() == "natasha" or girl_name.lower() == "renee" or girl_name.lower() == "sara" or girl_name.lower() == "yvette":
                            $attempts+=1
                            #Tiek pārbaudīts vai nav atkartoti ievadīts meitenes vārds
                            if answer1 == girl_name or answer2 == girl_name or answer3 == girl_name or answer4 == girl_name or answer5 == girl_name: 
                                jobs.reception.talk"You've already mentioned"
                            else:    
                                $correct_answers += 1
                        else:
                            $attempts+=1
                        jobs.reception.talk"You have [attempts]/5 and [correct_answers]/3."
                        #Meitenes vārds tiek padots mainīgajam attiecīgi secībai kurā tika ievadīti
                        if attempts==1:
                            $answer1 = girl_name
                        if attempts==2:
                            $answer2 = girl_name
                        if attempts==3:
                            $answer3 = girl_name
                        if attempts==4:
                            $answer4 = girl_name
                        if attempts==5:
                            $answer5 = girl_name
                            
                    if correct_answers == 3:
                        jobs.reception.talk"Congratulations!!! You win 100"
                        $player.change_company_favor(100)#Spēlētājam tiek ieskaitītas 100 monētas
                        jobs.reception.talk"Unfortunately you have not earned anything"
                    elif attempts == 5:
                        jobs.reception.talk"Unfortunately you have not earned anything"
                "Answer the question and get 200 company favor":#spēlētājam ir iespēja nopelnīt 200 monētas
                    jobs.reception.talk "How many girls are on the island now?"
                    menu:
                        "I know":
                            $ num_input = renpy.input("How many girls are on the island now?", length=3)#spēlētājs ievada skaitli, cik meitenes viņuprāt ir uz salas
                            while not num_input.isdigit():#Tiek pārbaudīts vai ievadītais simbols ir skaitlis
                                "Please enter a number"
                                $ num_input = renpy.input("How many girls are on the island now?", length=3)
                            if num_input.isdigit():
                                $num_input = int(num_input)
                                if  num_input == len(list_of_characters)-1:
                                    jobs.reception.talk"You are absolutely RIGHT!!!"
                                    jobs.reception.talk"Congratulations!!! You win 200"
                                    $ player.change_company_favor(200)
                                else:
                                    jobs.reception.talk"You are WRONG!!!"
                                    jobs.reception.talk"Unfortunately you have not earned anything"    
                        "I do not know, can I get an answers?":#Spēlētājs nezina cik ir meitenes uz salas
                            menu:#Spēlētājam tiek piedāvāti atbilžu varianti
                                "A) [num_of_girls3] girls. ":
                                    jobs.reception.talk"You are absolutely RIGHT!!!"
                                    jobs.reception.talk"Congratulations!!! You win 200"
                                    $ player.change_company_favor(200)#Spēlētājs nopelna 200 monētas
                                "B) [num_of_girls2] girls.":
                                    jobs.reception.talk"You are WRONG!!!"
                                    jobs.reception.talk"Unfortunately you have not earned anything"
                                "C) [max_char] girls.":
                                    jobs.reception.talk"You are WRONG!!!"
                                    jobs.reception.talk"Unfortunately you have not earned anything"
                                    
        "Ask for job reassignment of the doctor" if player.get_action_allowed("job_reassignment") == False:
            pl "I would like to have someone else performing doctor's duty.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Reassigning the doctor until the end of the week will cost you 20 company favor."
            if player.company_favor < 20:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "Here is the list of girls. Once you select a girl,\nwe will remove 20 company favor from your balance."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_5
                show screen main_game(location)
                call change_girl_job_rotation ("reception", "doctor") from _call_change_girl_job_rotation
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-20)
                    pl "Thank you very much [jobs.reception.fname]."
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."

        "Ask for job reassignment of room service" if player.get_action_allowed("job_reassignment") == False:
            pl "I would like to have someone else doing room service.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Reassigning a maid until the end of the week will cost you 20 company favor."
            if player.company_favor < 20:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "Here is the list of girls. Once you select a girl,\nwe will remove 20 company favor from your balance."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_7
                show screen main_game(location)
                call change_girl_job_rotation ("reception", "roomservice") from _call_change_girl_job_rotation_1
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-20)
                    pl "Thank you very much [jobs.reception.fname]."
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."

        "Ask for job reassignment of early reception shift" if player.get_action_allowed("job_reassignment") == False:
            pl "I would like to have someone else at the reception in the morning.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Reassigning a receptionist until the end of the week will cost you 20 company favor."
            if player.company_favor < 20:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "Here is the list of girls. Once you select a girl,\nwe will remove 20 company favor from your balance."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_9
                show screen main_game(location)
                call change_girl_job_rotation ("reception", "reception_early") from _call_change_girl_job_rotation_2
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-20)
                    pl "Thank you very much [jobs.reception.fname]."
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."

        "Ask for job reassignment of late reception shift" if player.get_action_allowed("job_reassignment") == False:
            pl "I would like to have someone else at the reception in the afternoon.\nIs that possible?"
            jobs.reception.talk "Sure [jobs.reception.playername], if you have the necessary company favor."
            jobs.reception.talk "Reassigning a receptionist until the end of the week will cost you 20 company favor."
            if player.company_favor < 20:
                jobs.reception.talk "Unfortunately you don't have the necessary company favor right now."
            elif True:
                jobs.reception.talk "Here is the list of girls. Once you select a girl,\nwe will remove 20 company favor from your balance."
                call main_game_background (location, location_detail, _return) from _call_main_game_background_11
                show screen main_game(location)
                call change_girl_job_rotation ("reception", "reception_late") from _call_change_girl_job_rotation_3
                $ stop_scene()
                show screen main_game(location)
                if _return == True:
                    $ player.change_company_favor(-20)
                    pl "Thank you very much [jobs.reception.fname]."
                elif True:
                    jobs.reception.talk "If you change your mind, just drop by any time."
                    pl "I will, thank you [jobs.reception.fname]."
        "That's all for now" if True:

            pl "I can't think of anything else that I need right now."
            pl "Have a nice day and see you later [jobs.reception.fname]."
            jobs.reception.talk "You too!"
            jump talk_reception_end

    label talk_reception_end:
    $ stop_scene()
    show screen main_game(location)
    $ menu_active = False
    return "nothing"





label action_reception_undress(char1, auto_succeed=False, intro=True):
    $ char1.add_action_cooldown("reception_undress", 48, "You just asked me to remove my top!")
    if intro == True:
        pl "Ummm... [jobs.reception.fname], would you remove your top for me... and give me a peek at your incredible breasts?"

    if auto_succeed == False and char1.check_tease_sexual(3) == False:
        char1.talk "Absolutely not!"
        char1.talk "How dare you even ask something like that?"
        pause 0.5
        pl "Ummm sorry, I just thought..."
        char1.talk "The answer is still no!"
        return "nothing"

    if char1.id == yvette.id:
        call action_reception_undress_yvette (char1) from _call_action_reception_undress_yvette

    return "nothing"





label action_reception_undress_yvette(char1):
    $ char1.add_pl_interaction("tease_boobs")
    $ menu_active = True
    $ start_scene()

    call show_reception_image (i_zoom=1.7) from _call_show_reception_image_7
    char1.talk "Since you are such a cute guy..."
    scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress1.jpg") with dissolve
    pause 1.0
    char1.talk "...here you go!"
    "You are a bit astonished that [char1.fname] of all girls is willing to expose her breasts at the reception area..."
    "...not that there is any reason to complain about it!"
    char1.talk "I think you already know that they are really huge... *giggles*"
    "After having opened the two front buttons, she raises her arms over her head..."
    scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress2.jpg") with dissolve
    pause 1.0
    "...which lets her top slide back and expose her incredible knockers!"
    $ player.change_lust(char1.sexiness)
    char1.talk "Do you like them? *smiles*"
    pause 0.5
    pl "Uhhh wow! {b}Yes!{/b} What an incredible view!"
    char1.talk "*smirks*"
    char1.talk "Since they are out in the open now, I might as well get rid of the top... *giggles*"
    "With appreciation you watch her remove the top and place it on the counter in front of her."
    scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress3.jpg") with dissolve
    pause 1.0
    char1.talk "Mmmmm yes, standing here all day makes me quite stiff..."
    pause 0.3
    char1.talk "... stretching a bit really helps to remove the stiffness! *smirks*"
    $ player.change_lust(char1.sexiness + 2)
    "The removing stiffness part may work for her..."
    "...but the amazing sight of her thrust out bare chest has quite the opposite effect on you."
    pause 0.8
    char1.talk "Do you like huge breasts [char1.playername]?"
    menu:
        "Yes!" if True:
            pl "Absolutely! I love them and cannot get enough!"
            pl "The bigger the better!"
            char1.talk "So you won't mind if I squeeze them for you, which makes them look even bigger... *smirks*"
            pause 0.5
            pl "Ummm no..."
            scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress4.jpg") with dissolve
            pause 1.0
            $ player.change_lust(char1.sexiness + 4)
            "Her knockers look really gigantic on her small frame."
            "You'd love to touch them..."
            "...too bad that huge desk is in between you and [char1.fname]!"
            char1.talk "*giggles* I can see it in your eyes..."
            char1.talk "...you really want to touch and squeeze them! *giggles some more*"
            scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress3.jpg") with dissolve
            pause 0.7
            char1.talk "I can squeeze them some more for you if you want! *smirks*"
            pause 0.5
            "Well... it's not as good as squeezing them yourself, but they look great when she's squeezing them..."
            pl "Ummmm okay... Yes please?"
            char1.talk "Okay, so one last squeeze before I put them back inside the top!"
            scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress5.jpg") with dissolve
            pause 1.0
            pl "Oh my God [char1.fname]! What cleavage!"
            $ player.change_lust(char1.sexiness + 4)
            $ char1.add_pl_interaction("tease_talk")
            char1.talk "Despite their size, they are very sensitive."
            char1.talk "The cold from the air conditioning is really tickling... *giggles*"
            pause 0.5
            char1.talk "Look, my nipples are getting hard... *giggles some more*"
            scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress6.jpg") with dissolve
            pause 1.0
            $ player.change_lust(char1.sexiness)
            $ player.add_effect("erection")
            "It seems her nipples are not the only thing getting hard..."
            "Fortunately, your boner is hidden behind the huge desk."
            char1.talk "And now it's time to put them back in!"
        "You love breasts of all sizes!" if True:

            pl "Ummm I love breasts of all sizes!"
            $ char1.change_affection(-5)
            char1.talk "Sooo... Huge knockers like mine aren't really your thing..."
            pause 0.5
            char1.talk "That's okay. I hope you still enjoyed getting a peek..."
            pause 0.4
            char1.talk "...and now it's time to put them back in!"

    scene expression ("scenes/[jobs.reception.fname]/[jobs.reception.fname]_reception[jobs.reception.receptionwear]_undress1.jpg") with dissolve
    pause 0.7
    call show_reception_image (i_zoom=1.7) from _call_show_reception_image_8
    "Too bad the show's over now..."
    "...she really has an amazing pair of knockers!"
    pl "Wow [char1.fname]! That was an amazing sight!"
    pl "Thank you very much for doing that for me."
    pause 0.3
    char1.talk "It was my pleasure [char1.playername]!"
    char1.talk "When I'm in the right mood, I can be a naughty girl too. *smiles"
    pause 0.4
    pl "I can see that. *smiles back*"
    $ char1.add_scene_seen("Reception_undress")
    pause 0.6
    char1.talk "Is there anything else I can do for you?"
    $ stop_scene()

    return "nothing"





label action_reception_ring_bell(char1):
    $ menu_active = True

    play sound "sounds/reception_bell1.mp3"
    "*bing* *bing* *bing*"
    if char1.locations[actions_left-1] <> "reception":
        $ tts2(t_female_computer_voice, "The receptionist has been informed and will arrive shortly.")
        if player.knows_about_lisa == False:
            $ player.knows_about_lisa = True
            "Holy... {w}What was that?"
            pause 1.3
            "Before you have time to think about what just happened, [char1.fname] arrives at reception."
        elif True:
            pl "Ummm... Lisa? You're here as well?"
            $ tts2(t_female_computer_voice, "I'm everywhere on this island, [player.fname].")
            pl "Wow!"
            pause 0.5
            "Before you can talk further with the AI, [char1.fname] arrives at reception."

        $ g_receptionist_location = char1.locations[actions_left-1]
        $ char1.locations[actions_left-1] = "reception"
        char1.talk "Hello [char1.playername]."
        char1.talk "I hope you have a good reason to interrupt my well earned break."
        $ char1.change_anger(3)
        if g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar":
            pl "You're not wearing your reception uniform today?"
            pause 0.4
            if g_receptionist_location == "restaurant":
                char1.talk "Yeah well, a certain someone made me come running from the restaurant..."
            elif g_receptionist_location == "nightbar":
                char1.talk "Yeah well, a certain someone made me come running from the bar..."
            pause 0.4
        pl "Oh... I'm really sorry."
    elif True:
        if char1.get_action_allowed("reception_ring_bell") == True:
            $ char1.add_action_cooldown("reception_ring_bell", 8)
            char1.talk "Is it really necessary to do that when I'm already here?"
            pl "Ummm..."
            char1.talk "Please don't do it again."
        elif True:
            char1.talk "I've already told you not to do that when I'm already here."
            char1.talk "You're starting to make me angry..."
            $ char1.change_anger(10)
            if char1.id == ivy.id and char1.get_action_allowed("reception_crush_bell") == True and g_receptionist_location <> "restaurant" and g_receptionist_location <> "nightbar":
                "You blink for a moment when...she grabs the bell from under your hand."
                scene expression ("scenes/[char1.fname]/reception/[char1.fname]_reception[char1.receptionwear]_ring_bell1.webp"):
                    zoom 0.5
                $ start_scene()
                with fade
                "And stuffs it between her huge knockers."
                pause 1.2
                char1.talk "If you do that again, I'll do to you what I'm about to do to this bell."
                pl "Ohhhmmm, uhmmmm.... What?"
                "Then she pushes her mighty breasts together with her muscular arms."
                scene expression ("scenes/[char1.fname]/reception/[char1.fname]_reception[char1.receptionwear]_ring_bell2.webp") with dissolve:
                    zoom 0.5
                pause 0.6
                "*ping!* *screeeek!* You hear the sound of bell metal under great pressure..."
                "...before parts go flying everywhere..."
                scene expression ("scenes/[char1.fname]/reception/[char1.fname]_reception[char1.receptionwear]_ring_bell3.webp") with dissolve:
                    zoom 0.5
                pause 0.6
                "...and the remains of the bell nearly vanish inside her deep cleavage."
                char1.talk "You see, you really shouldn't make me angry."
                "You're a at a loss for words at the display of her strength."
                pl "Ummm... okay [char1.fname], I won't do it again."
                "She throws the damaged bell into the garbage can, pulls a new one from under her table and places it on the desk."
                call show_reception_image (i_zoom=1.5, i_clothes="reception2") from _call_show_reception_image_26
                char1.talk "Haha, I really got you, didn't I?"
                char1.talk "One of the girls had the idea and I couldn't resist."
                char1.talk "I was only joking. I'd never hurt you."
                pause 0.4
                pl "Puhhh... *smiles*"
                pause 0-4
                char1.talk "And I'm not really angry with you. It was all for show. *giggles*"
                $ char1.change_anger(-10)
                $ char1.add_action_cooldown("reception_crush_bell", 96)
                $ stop_scene()
                char1.talk "But enough of the bell ringing now, okay?"
                pl "Ummm... Yeah, sure."
                call add_hidden_image (char1, "reception") from _call_add_hidden_image
                $ char1.add_scene_seen("reception_ring_bell")

            call main_game_background (location, location_detail, _return) from _call_main_game_background_14
    $ menu_active = False
    return "nothing"





screen char_reception:
    if location_detail == "":
        if location == "reception" and jobs.reception.locations[actions_left-1] == "reception":
            $ selected_char = jobs.reception
            $ l_zoom = 0.5 * 0.53
            $ l_xalign = 0.5
            $ l_ypos = 570

            if g_receptionist_location == "restaurant" or g_receptionist_location == "nightbar":
                if jobs.reception.id <> ivy.id:
                    $ l_x_size,l_y_size = renpy.image_size("characters/" + jobs.reception.fname + "/" + jobs.reception.fname + "_night" + unicode(jobs.reception.dinerwear) + "_base.webp")
                    $ l_zoom_char = 2160.0 / float(l_y_size) * 0.89
                    $ l_zoom *= l_zoom_char
                if jobs.reception.id == yvette.id:
                    $ l_ypos += 65
                elif jobs.reception.height_type == 3:
                    $ l_ypos += 25
                elif jobs.reception.height_type == 2:
                    $ l_ypos += 35
                elif jobs.reception.height_type == 1:
                    $ l_ypos += 55

                $ l_image = im.MatrixColor("characters/" + jobs.reception.fname + "/" + jobs.reception.fname + "_night" + unicode(jobs.reception.dinerwear) + "_base.webp", im.matrix.brightness(0.05)*im.matrix.saturation(1.05))
            else:
                $ l_image = "characters/" + jobs.reception.fname + "/" + jobs.reception.fname + "_reception" + unicode(jobs.reception.receptionwear) + "_base.webp"

            add l_image zoom l_zoom xalign l_xalign yanchor 1.0 ypos l_ypos
            if menu_active == True:
                imagebutton idle im.Alpha(im.FactorScale(l_image,l_zoom),0.1) xalign l_xalign yanchor 1.0 ypos l_ypos hovered SetVariable("player.smart_watch_character", jobs.reception) unhovered SetVariable("player.smart_watch_character", no_char) tooltip ("03_Talk to [jobs.reception.fname]") focus_mask True
                add "locations/loc_reception_layer2.webp" zoom 0.5
            else:
                imagebutton idle im.Alpha(im.FactorScale(l_image,l_zoom),0.01) action Return("talkto") xalign l_xalign yanchor 1.0 ypos l_ypos hovered SetVariable("player.smart_watch_character", jobs.reception) unhovered SetVariable("player.smart_watch_character", no_char) tooltip ("03_Talk to [jobs.reception.fname]") focus_mask True
                add "locations/loc_reception_layer2.webp" zoom 0.5
                imagebutton idle im.Alpha(im.FactorScale("locations/loc_reception_bell_idle.webp",0.5),0.01) hover im.Alpha(im.FactorScale("locations/loc_reception_bell_hover.webp",0.5),0.65) action Return("reception_ring_bell") xpos 1108 ypos 591 tooltip ("03_Ring the bell") focus_mask True

        elif location == "reception":
            imagebutton idle im.Alpha(im.FactorScale("locations/loc_reception_bell_idle.webp",0.5),0.01) hover im.Alpha(im.FactorScale("locations/loc_reception_bell_hover.webp",0.5),0.65) action Return("reception_ring_bell") xpos 1108 ypos 591 tooltip ("03_Ring the bell") focus_mask True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
