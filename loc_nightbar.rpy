


screen nightbar_actions:
    if selected_char.id <> 999:
        text "Nightbar [selected_char.fname]" size 15 color "#66c1e0" xpos 1093 ypos 425
        $ xpos_new = 1093
        if menu_active == True:
            if selected_char.get_action_icon_available("nightbar_poker"):
                imagebutton auto "gui/action_nightbar_poker_%s.png" xpos xpos_new ypos 445
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_drink"):
                imagebutton auto "gui/action_nightbar_cocktail_%s.png" xpos xpos_new ypos 445 focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_poledance"):
                imagebutton auto "gui/action_nightbar_poledance_%s.png" xpos xpos_new ypos 445 focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_hotshots"):
                imagebutton auto "gui/action_nightbar_hotshots_%s.png" xpos xpos_new ypos 445 focus_mask True
            $ xpos_new = 1093
            if selected_char.get_action_icon_available("nightbar_arm_wrestling"):
                imagebutton auto "gui/action_arm_wrestling_%s.png" xpos xpos_new ypos 445+45 focus_mask True
                $ xpos_new += 45


        else:
            if selected_char.get_action_icon_available("nightbar_poker"):
                if player.has_item("poker cards") == True or player.has_item("marked poker cards") == True:
                    imagebutton auto "gui/action_nightbar_poker_%s.png" action Return("do_nightbar_poker") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to play strip poker with you.") focus_mask True
                else:
                    imagebutton auto "gui/action_nightbar_poker_%s.png" action NullAction() xpos xpos_new ypos 445 hovered tt.Action ("You need to buy a deck of cards to play strip poker with [selected_char.fname]!") focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_drink"):
                imagebutton auto "gui/action_nightbar_cocktail_%s.png" action Return("do_nightbar_drink") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to have a drink with you.") focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_poledance"):
                imagebutton auto "gui/action_nightbar_poledance_%s.png" action Return("do_nightbar_poledance") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to pole dance for you.") focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("nightbar_hotshots"):
                if jobs.bartender.id == yumiko.id:
                    imagebutton auto "gui/action_nightbar_hotshots_%s.png" action Return("do_nightbar_hotshots") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to play\n{b}HotShots{/b}\nwith you.") focus_mask True
                else:
                    imagebutton auto "gui/action_nightbar_hotshots_%s.png" action NullAction() xpos xpos_new ypos 445 hovered tt.Action ("You can only play {b}HotShots{/b} when Yumiko is the bartender!") focus_mask True
                    text "X" size 30 color "#cc0000" xpos xpos_new+10 ypos 448
            $ xpos_new = 1093
            if selected_char.get_action_icon_available("nightbar_arm_wrestling"):
                imagebutton auto "gui/action_arm_wrestling_%s.png" action Return("do_nightbar_arm_wrestling") hovered tt.Action ("Ask [selected_char.fname] to arm wrestle against you") xpos xpos_new ypos 445+45 focus_mask True
                $ xpos_new += 45







screen nightbar_pl_actions:
    if selected_char.id == 999 and location == "nightbar":
        text "Player night bar actions" size 15 color "#66c1e0" xpos 1093 ypos 310
        if menu_active == True:
            imagebutton idle "gui/action_nightbar_cocktail_hover.png" xpos 1093 ypos 330
            imagebutton idle "gui/action_nightbar_talk_security_hover.png" xpos 1138 ypos 330
            imagebutton idle im.Alpha(im.Scale("gui/action_present_hover.png",33,33),0.65) xpos 1093 ypos 375
            imagebutton idle im.Alpha(im.Scale("gui/action_hug_hover.png",33,33),0.65) xpos 1129 ypos 375
            imagebutton idle im.Alpha(im.Scale("gui/action_kiss_mouth_hover.png",33,33),0.65) xpos 1165 ypos 375 focus_mask True
            imagebutton idle im.Alpha(im.Scale("gui/action_grope_hover.png",33,33),0.65) xpos 1201 ypos 375 focus_mask True
            imagebutton idle im.Alpha(im.Scale("gui/action_flash_breasts_hover.png",33,33),0.65) xpos 1237 ypos 375 focus_mask True
        else:
            imagebutton auto "gui/action_nightbar_cocktail_%s.png" action Return("do_pl_drink") xpos 1093 ypos 330 hovered tt.Action ("Have a drink at the bar") focus_mask True
            if g_game_version >= "0.1.7.0" and miriam.get_event_seen("Arrival") == True:
                if player.get_action_allowed("nightbar_security_chat"):
                    imagebutton auto "gui/action_nightbar_talk_security_%s.png" action Return("do_pl_chat_nightbar_security") xpos 1138 ypos 330 hovered tt.Action ("Chat with the security guard") focus_mask True
                else:
                    imagebutton auto "gui/action_nightbar_talk_security_%s.png" action NullAction() xpos 1138 ypos 330 hovered tt.Action ("You've spoken with nightbar security recently, give her a break.") focus_mask True
                    text "X" size 30 color "#cc0000" xpos 1148 ypos 333

            imagebutton hover im.Scale("gui/action_present_hover.png",33,33) idle im.Alpha(im.Scale("gui/action_present_hover.png",33,33),0.65) action Return("do_give_present_jennifer") xpos 1093 ypos 375 hovered tt.Action ("Give " + jobs.bartender.fname + " the bartender a present.") focus_mask True
            imagebutton hover im.Scale("gui/action_hug_hover.png",33,33) idle im.Alpha(im.Scale("gui/action_hug_hover.png",33,33),0.65) action Return("do_hug_jennifer") xpos 1129 ypos 375 hovered tt.Action ("Hug " + jobs.bartender.fname + " the bartender.") focus_mask True
            imagebutton hover im.Scale("gui/action_kiss_mouth_hover.png",33,33) idle im.Alpha(im.Scale("gui/action_kiss_mouth_hover.png",33,33),0.65) action Return("do_kiss_jennifer") xpos 1165 ypos 375 hovered tt.Action ("Kiss " + jobs.bartender.fname + " the bartender on the mouth.") focus_mask True
            imagebutton hover im.Scale("gui/action_grope_hover.png",33,33) idle im.Alpha(im.Scale("gui/action_grope_hover.png",33,33),0.65) action Return("do_grope_jennifer") xpos 1201 ypos 375 hovered tt.Action ("Grope " + jobs.bartender.fname + " the bartender and fondle her breasts.") focus_mask True
            imagebutton hover im.Scale("gui/action_flash_breasts_hover.png",33,33) idle im.Alpha(im.Scale("gui/action_flash_breasts_hover.png",33,33),0.65) action Return("do_flash_breasts_jennifer") xpos 1237 ypos 375 hovered tt.Action ("Ask " + jobs.bartender.fname + " the bartender to flash her breasts.") focus_mask True





screen nightbar_jennifer:
    if location == "nightbar" and jobs.bartender.id == jennifer.id and (location_detail=="" or location_detail=="intimate"):
        if g_game_version < "0.3.4.9" or g_intimate_char.id <> jennifer.id:
            $ image_name = "characters/Jennifer/Jennifer_nightbar_hover.webp"
            add image_name zoom 0.3334
            if menu_active == False and (selected_char.id == 999 or (selected_char.id <> 999 and selected_char.id <> jennifer.id)):
                if persistent.ui_show_open_achievements <> True or len(jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")) == 0:
                    imagebutton hover im.Alpha(im.MatrixColor(im.FactorScale(image_name, 0.3334), im.matrix.brightness(0.1)), 0.1) idle im.Alpha(im.FactorScale(image_name, 0.3334), 0.1) action Return("do_pl_drink") tooltip ("03_Have a drink at the bar" + jobs.bartender.get_scenes_not_seen_text("nightbar_bartender_talk")) hovered SetVariable("player.smart_watch_character", jobs.bartender) unhovered SetVariable("player.smart_watch_character", no_char) focus_mask True
                    if len(jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")) == 0:
                        add "gui/action_frame_green.png" alpha 0.7 xpos -43
                        null width -46
                elif persistent.ui_show_open_achievements == True:
                    imagebutton hover im.Alpha(im.MatrixColor(im.FactorScale(image_name, 0.3334), im.matrix.brightness(0.1)), 0.1) idle im.Alpha(im.FactorScale(image_name, 0.3334), 0.1) action Return("do_pl_drink") tooltip ("03_Have a drink at the bar") hovered [SetVariable("player.smart_watch_character", jobs.bartender), SetVariable("g_achievements_hover", jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")), Show("show_achievements")] unhovered [SetVariable("player.smart_watch_character", no_char), Hide("show_achievements")] focus_mask True





screen nightbar_yumiko:
    if location == "nightbar" and jobs.bartender.id == yumiko.id  and (location_detail=="" or location_detail=="intimate"):
        if g_game_version < "0.3.4.9" or g_intimate_char.id <> yumiko.id:
            $ image_name = "characters/Yumiko/Yumiko_nightbar_hover.webp"
            add image_name zoom 0.3334
            if menu_active == False and (selected_char.id == 999 or (selected_char.id <> 999 and selected_char.id <> yumiko.id)):
                if persistent.ui_show_open_achievements <> True or len(jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")) == 0:
                    imagebutton hover im.Alpha(im.MatrixColor(im.FactorScale(image_name, 0.3334), im.matrix.brightness(0.1)), 0.1) idle im.Alpha(im.FactorScale(image_name, 0.3334), 0.1) action Return("do_pl_drink") tooltip ("03_Have a drink at the bar" + jobs.bartender.get_scenes_not_seen_text("nightbar_bartender_talk")) hovered SetVariable("player.smart_watch_character", jobs.bartender) unhovered SetVariable("player.smart_watch_character", no_char) focus_mask True
                    if len(jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")) == 0:
                        add "gui/action_frame_green.png" alpha 0.7 xpos -43
                        null width -46
                elif persistent.ui_show_open_achievements == True:
                    imagebutton hover im.Alpha(im.MatrixColor(im.FactorScale(image_name, 0.3334), im.matrix.brightness(0.1)), 0.1) idle im.Alpha(im.FactorScale(image_name, 0.3334), 0.1) action Return("do_pl_drink") tooltip ("03_Have a drink at the bar") hovered [SetVariable("player.smart_watch_character", jobs.bartender), SetVariable("g_achievements_hover", jobs.bartender.get_scenes_not_seen("nightbar_bartender_talk")), Show("show_achievements")] unhovered [SetVariable("player.smart_watch_character", no_char), Hide("show_achievements")] focus_mask True





label nightbar_last_call():
    $ menu_active = True
    $ l_bartender = jobs.bartender
    $ set_watch_characters(jobs.bartender)
    $ start_scene()

    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call0.webp"):
        zoom 0.5
    with dissolve
    pause 0.4
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call1.webp") with dissolve:
        zoom 0.5
    pause 0.5
    call create_list_of_chars_display () from _call_create_list_of_chars_display_10
    $ l_bartender.add_action_cooldown("nightbar_last_call", 40)
    "Checking your watch you notice that it's already 01:30 in the morning."
    l_bartender.talk "Hello [l_bartender.playername]!"
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call2.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Hi [l_bartender.fname]!"
    l_bartender.talk "Just wanted to let you know that the bar closes in half an hour..."
    l_bartender.talk "So if there is {i}anything{/i} I can do for you, let me know."
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call3.webp") with dissolve:
        zoom 0.5
    pause 0.4
    "Ohh! That sounds intriguing."
    "What are you going to do?"
    menu:
        "Thank her for the information." if True:
            pl "Thank you for letting me know [l_bartender.fname]."
            l_bartender.talk "My pleasure. I'm back behind the bar. If you need anything, you know where to find me..."
            pl "Sure thing!"
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call5.webp") with dissolve:
                zoom 0.5
            pause 0.7
            "You admire her strong butt and thighs for a moment, before she disappears behind the bar..."
            $ l_bartender.add_scene_seen("Bartender_nightbar_last_call")
        "Take a closer look at her cleavage." if True:

            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call6.webp") with dissolve:
                zoom 0.5
            pause 0.7
            if l_bartender.check_tease_sexual(2, 0, False) == False and player.check_looks(4) == False:
                $ l_rand_answer = renpy.random.randint(1,4)
                if l_rand_answer == 1:
                    l_bartender.talk "Do you think they'll start speaking if you stare hard enough?"
                    pause 0.7
                elif l_rand_answer == 2:
                    l_bartender.talk "Wow, are you seriously staring at my tits for a whole minute?"
                    pause 0.7
                elif l_rand_answer == 3:
                    l_bartender.talk "Hey [l_bartender.playername]! It would be nice if you could talk to my face for a moment!"
                    pause 0.7
                elif l_rand_answer == 4:
                    l_bartender.talk "Is there something wrong with my dress?"
                    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call4.webp") with dissolve:
                        zoom 0.5
                    pause 1.2
                    pl "Er... No!"
                    pause 0.5
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call3.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                $ l_bartender.change_anger(10)
                if player.check_charm(4) == True:
                    pl "Sorry [l_bartender.fname], you just look far too amazing not to stare for a moment. *smiles*"
                    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call2.webp") with dissolve:
                        zoom 0.5
                    pause 0.7
                    $ l_bartender.change_anger(-5)
                    l_bartender.talk "It's okay, but please don't be too obvious about it..."
                    l_bartender.talk "...and now if you'll excuse me, I've got to go back to the bar."
                    pl "Yes sure."
                elif True:
                    pl "Ummm... I'm really sorry, didn't mean to be rude... *lamely*"
                    l_bartender.talk "I think I'd better go back to the bar..."
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call5.webp") with dissolve:
                    zoom 0.5
                pause 1.0
                "She takes her time to walk back to the bar."
                $ l_bartender.add_scene_seen("Bartender_nightbar_last_call")
                jump nightbar_last_call_end

            $ l_bartender.add_scene_seen("Bartender_nightbar_last_call")
            if l_bartender.id == yumiko.id:
                call nightbar_last_call_yumiko (l_bartender) from _call_nightbar_last_call_yumiko
                if _return == "goto_player_room":
                    $ location = "player_room"
                    $ location_old = location
                    $ menu_active = False
                    $ stop_scene()
                    "Wow! what a night!"
                    return "goto_player_room"
            elif True:
                call nightbar_last_call_jennifer (l_bartender) from _call_nightbar_last_call_jennifer
            jump nightbar_last_call_end
        "Ask her what is included in {i}anything{/i}." if True:

            pl "Uhmm [l_bartender.fname], what exactly is included in {i}anything{/i}?"
            l_bartender.talk "Were you thinking dirty thoughts [l_bartender.playername]?"
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call2.webp") with dissolve:
                zoom 0.5
            pause 0.7
            pl "Ummm... No, just asking..."
            l_bartender.talk "Well you know, drinks, talking to a sexy barmaid..."
            pause 0.3
            l_bartender.talk "...or maybe even play strip poker against her."
            l_bartender.talk "Unfortunately I've still got some work to do. I'm behind the bar if you need me."
            pl "Sure thing and thanks."
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_last_call5.webp") with dissolve:
                zoom 0.5
            pause 0.7
            "You admire her strong butt and thighs for a moment, before she disappears behind the bar..."
            $ l_bartender.add_scene_seen("Bartender_nightbar_last_call")

    label nightbar_last_call_end:
    $ menu_active = False
    $ stop_scene()
    return "do_return"





label nightbar_last_call_yumiko(char1):
    "Surprising you, she takes a quick step forward..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call7.webp") with dissolve:
        zoom 0.65 align (0.85,0.7)
    pause 0.2
    "...almost burying your face between her tits."
    pl "Ohhh!"
    char1.talk "*giggles* You okay?"
    char1.talk "Hit your head on something soft? *giggles some more*"
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Did you like the close-up view *smiles*?"
    "Since she doesn't seem to be angry...\n...You decide to play along."
    pl "Absolutely. It was really a big surprise."
    pl "You breasts are even more impressive from up close. *smiling*"
    $ player.change_lust(char1.sexiness)
    if len(list_of_chars_display_3) > 0:
        jump nightbar_last_call_yumiko_not_alone

    label nightbar_last_call_yumiko_alone:
    pause 0.4
    char1.talk "Well... since everyone else has left already..."
    char1.talk "Would you like to get a better look without the bunny body in the way?"
    pl "I'd love to!"
    "She moves her costume down to expose her breasts..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call9.webp") with fade:
        zoom 0.5
    pause 0.7
    char1.talk "Here you go! *smiles*"
    pl "{b}Wow{/b}!"
    pause 0.4
    char1.talk "You like?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call9.webp"):
        subpixel True zoom 0.5 align (0.7,0.3)
        ease 1.4 zoom 0.75
    $ renpy.pause(1.6, hard=True)
    pl "Yeah, it's an amazing view!"
    pause 0.5
    pl "Let's have a drink and talk a bit, shall we?"
    pause 0.3
    char1.talk "Sure, I'd love to."
    "She turns around and walks back towards the bar..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call10.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Ummm... Do you mind if I leave them exposed like this?"
    pause 0.4
    pl "Er... No... I guess not... *smiling*"
    "What kind of question is that???"
    "You could stare at her incredible boobs all night..."
    $ player.change_lust(char1.sexiness + 2)
    char1.talk "You coming?"
    pl "I'm right behind you!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call10.webp"):
        subpixel True zoom 0.5 align (0.7,0.1)
        ease 1.8 zoom 0.75
    $ renpy.pause(2.1,hard=True)
    "Standing behind her, you take a good look at her firm round ass..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call10.webp"):
        subpixel True zoom 0.75 align (0.7,0.1)
        ease 2.0 zoom 1.3 align (0.7,0.5)
    $ renpy.pause(2.2,hard=True)
    "...before looking back at her face."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call10.webp"):
        subpixel True zoom 1.3 align (0.7,0.5)
        ease 1.6 zoom 1.05 align (0.7,0.05)
    $ renpy.pause(1.9,hard=True)
    char1.talk "Please have a seat while I fetch us something to drink."
    pl "Thanks."
    "You sit down on one of the bar stools, and watch [char1.fname] walk behind the counter..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call11.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "...and prepares the drinks."
    char1.talk "What do you want to have?"
    pl "Hmmm..."
    pl "Surprise me."
    char1.talk "Okay, sure. *smiles*"
    "Glasses in hand and with her sizable tits still hanging out..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call12.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "...she walks around the counter to the stool right beside yours."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call13.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Here's your drink, [char1.playername]."
    "With her exposed knockers, it's really hard to concentrate on her face..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call13.webp"):
        subpixel True zoom 0.5 align (0.7,0.7)
        ease 1.7 zoom 1.0
    $ renpy.pause(2.0,hard=True)
    "...but after a casual glance, you manage."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call13.webp"):
        subpixel True zoom 1.0 align (0.7,0.7)
        ease 1.7 zoom 1.0 align (0.7,0.1)
    $ renpy.pause(2.0,hard=True)
    pl "Thanks [char1.fname] and cheers."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call14.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Cheers!"
    "After a savoring sip, she sits down on the stool beside you."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call18.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "Placing her glass on the counter."
    char1.talk "How do you like it on the island [char1.playername]?"
    "You put your glass down before you answer."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call19.webp") with dissolve:
        zoom 0.5
    pause 0.7
    menu:
        "Tell her it's great, you love it" if True:
            pl "I really love it."
            pl "It's a great island all by itself."
            pl "And all the girls are great!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "I can imagine that. All of them are quite sexy."
        "Tell her it's even better now that she's here" if True:

            pl "I've loved it from the moment I arrived."
            pl "You know with all these sexy girls..."
            pause 0.4
            pl "Now since you're here it's even better. *smiles*"
            char1.talk "You're a real charmer."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Thank you! *smiles back*"
            call change_char_max_affection (char1, 5) from _call_change_char_max_affection_77
            $ char1.change_affection(10)

    pause 0.6
    char1.talk "Ummm... Can I ask you something?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    "Between the sound of her sexy voice and her exposed tits, it's not easy to concentrate."
    $ player.change_lust(char1.sexiness + 2)
    pl "Sure! What is it?"
    char1.talk "Which one of the girls currently on the island do you like the most?"
    char1.talk "Don't say it's me. That doesn't count."
    char1.talk "Jennifer and Joy also don't count!"
    "Waiting for your answer, you both take another sip from her glasses."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call17.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    $ l_list_of_characters = list_of_characters[:]
    call screen select_girl(l_list_of_characters, "Tell her it's", "Which girl do you like the most?", False)
    $ l_girl = _return
    call change_char_sexiness (l_girl, 2) from _call_change_char_sexiness
    pl "You know, I think it's [l_girl.fname]."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    if l_girl.breast_size == player.bust_size_pref:
        $ l_breast_size_text = l_girl.get_breast_size_text()
        char1.talk "I bet it's because of her [l_breast_size_text]!"
    elif l_girl.body_type == player.figure_pref1 or l_girl.body_type == player.figure_pref2:
        $ l_body_type_text = l_girl.get_body_type_text()
        char1.talk "I bet it's because of her [l_body_type_text] body!"
    elif l_girl.height_type == player.height_pref:
        char1.talk "I bet it's because of her height!"
    elif True:
        char1.talk "I guess you just like her type?"
    pl "Ummm... How did you know that?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") at zoom_c(0.5)
    with dissolve
    pause 0.7
    char1.talk "Just guessing... *giggles*"
    char1.talk "So who's second?"
    pl "Hmmm... let me think about it for a moment."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call20.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Do you need help {i}thinking{/i} about it? *giggles*"
    pl "Ummm... No... A little less distraction should work well enough. *smiling*"
    char1.talk "I don't know why, but I'm pretty sure you'll pick one with nice breasts. *smirks*"
    "You cannot help it, but stare are her exposed tits for a moment..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call20.webp"):
        subpixel True zoom 0.5 align (0.7,0.7)
        pause 0.4
        ease 1.6 zoom 1.0
    $ renpy.pause(1.9,hard=True)
    "...before thinking about your second girl."
    $ l_list_of_characters.remove(l_girl)
    call screen select_girl(l_list_of_characters, "Tell her it's", "Which girl is your second choice?", False)
    $ l_girl = _return
    call change_char_sexiness (l_girl, 1) from _call_change_char_sexiness_1
    pl "I think my second choice is [l_girl.fname]."
    "Before answering, you lift your glasses again..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call17.webp"):
        zoom 0.5
    with dissolve
    pause 0.7
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call18.webp") with dissolve:
        zoom 0.5
    pause 0.7
    if l_girl.breast_size == player.bust_size_pref:
        $ l_breast_size_text = l_girl.get_breast_size_text()
        char1.talk "I bet it's because of her [l_breast_size_text]!"
    elif l_girl.body_type == player.figure_pref1 or l_girl.body_type == player.figure_pref2:
        $ l_body_type_text = l_girl.get_body_type_text()
        char1.talk "I bet it's because of her [l_body_type_text] body!"
    elif l_girl.height_type == player.height_pref:
        char1.talk "I bet it's because of her height!"
    elif True:
        char1.talk "I guess you just like her type?"
    pl "How did you...?"
    pl "Nah, just forget I asked. *smiles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5)
    with dissolve
    pause 0.7
    char1.talk "Just one last question regarding the girls."
    pause 0.2
    char1.talk "Which one of the girls currently on the island do you like the least?"
    pl "Ummm... I'm not sure..."
    char1.talk "Oh c'mon, please. I won't tell her or anyone else."
    char1.talk "I promise!"
    pl "Okay, I believe you."
    $ l_list_of_characters.remove(l_girl)
    call screen select_girl(l_list_of_characters, "Tell her it's", "Which girl do you like the least?", False)
    $ l_girl = _return
    call change_char_sexiness (l_girl, -2) from _call_change_char_sexiness_2
    pl "The girl I find the least attractive is [l_girl.fname]."
    char1.talk "Thank you for trusting me with that information."
    "She leans forward and gives you one of her little girl smiles..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call21.webp") at zoom_c(0.5)
    with dissolve
    pause 0.7
    char1.talk "That wasn't so bad, was it? *smiles*"
    "Damn she's hot!"
    $ player.change_lust(char1.sexiness + 4)
    pl "You know that it's kind of hard talking with a topless bombshell about how much you like other girls..."
    "[char1.fname] is pointedly looking down at your crotch."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call22.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    $ char1.add_scene_seen("Bartender_nightbar_last_call_alone")
    call actions_used (1) from _call_actions_used_75
    if player.get_effect_state("erection") > 0:
        jump nightbar_last_call_yumiko_blowjob

    char1.talk "Hmmm... It looks like it could be harder..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    $ char1.change_affection(-5)
    "She sounds a little disappointed..."
    if player.get_action_allowed("picture_minigame_proposed") == True and yumiko.get_scene_seen("Bartender_nightbar_last_call_story") == True:
        "You decide it's a good time to change the subject."
        "But, before any useful idea comes to your mind, a cute smile forms on her pretty face.."
        char1.talk "*smiles* Do you consider yourself an observant person?"
        menu:
            "You think so" if True:
                pl "Yes, I think so."
                "Her expression changes to a huge, adorable smile..."
                char1.talk "That's great! I love observant people!"
            "Hmmm... Not sure how to answer that question" if True:

                pl "Hmmm... I'm not really sure..."
                char1.talk "Don't be scared, I've just got an interesting idea. *smiles*"
            "I don't think so" if True:

                pl "Ummm... No, I don't really think so."
                char1.talk "Yeah I see, but, We can actually work on that! *smiles*"

        char1.talk "Do you want to play a game?"
        pause 0.4
        pl "It depends... What kind of game?"
        char1.talk "It'll test your observation skills. You'll see, it's going to be fun!"
        char1.talk "I'll send you a part of a picture of a girl and you have to guess who it is."
        char1.talk "So, what do you say? Would you like to play?"
        $ player.add_action_cooldown("picture_minigame_proposed", 999)
        menu:
            "Okay, great, let's play!" if True:
                pl "Okay cool, let's play a bit!"
                char1.talk "Yeah! That's the spirit! *laughing*"
                $ char1.change_affection(5)
            "Still not sure... but, let's do it" if True:

                pl "Ummm... Okay, let's try it and see how it goes..."
                char1.talk "Great! No need to worry. You're going to have fun! *smiles*"
            "Not right now" if True:

                pl "Ummm... Maybe later, okay?"
                $ player.add_action_cooldown("picture_minigame", 999)
                char1.talk "What a pity *a bit sad*"
                char1.talk "Well... If you change your mind, you know where to find me. *smiles*"

        if player.get_action_allowed("picture_minigame"):
            pl "So, what do you want me to do?"
            char1.talk "Nothing at the moment. I will text you soon. *winks*"
            pause 0.4
            pl "Oh! Okay..."

    elif player.get_action_allowed("yumiko_joy_story") == True:
        $ char1.add_scene_seen("Bartender_nightbar_last_call_story")
        $ player.add_action_cooldown("yumiko_joy_story", 7*48)
        "You decide it's a good time to change the subject and ask how she came to the island."
        pl "Since you know all about my favorite girls..."
        pl "...why don't you tell me something about the beautiful [char1.fname]?"
        pause 0.3
        pl "How did you end up on the island?"
        "Her face lightens up and her mood changes."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call23a.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "I was working in a coffee shop not far away from the HI Inc. headquarter."
        char1.talk "It was a day like any other...\nPretty busy during lunch break and after office hours."
        pause 0.4
        char1.talk "Just before my shift ended, it must have been almost 8pm, a stunning woman walked in."
        char1.talk "Bronze skin, maybe 30 years old, with killer legs and really big breasts."
        "Speaking of legs..."
        "...you just notice the cute girl in front of you probably has great legs too."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call23b.webp") with dissolve:
            zoom 0.5
        pause 0.7
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call23c.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        "It takes [char1.fname] a moment to register that you're a bit {i}distracted{/i}..."
        pause 0.5
        char1.talk "*giggles* You like mine?"
        pl "Ummm... What?"
        char1.talk "I'm talking about my legs. You like them? *smiles*"
        pl "Yes, they look great! *sheepishly*"
        char1.talk "Just wanted to make sure you were still listening..."
        pl "Sorry. I'm all eyes and ears again!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call23a.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Okay, so the mysterious sexy lady walked into the coffee shop."
        char1.talk "Some of the guys almost fell from their chairs looking after her..."
        pause 0.3
        char1.talk "...probably staring at her butt. *giggles*"
        pl "I can imagine that. *smiles*"
        pause 0.4
        pl "So the woman was Joy?"
        char1.talk "Yes, but I didn't know her name or who she was at that time."
        pause 0.6
        char1.talk "I think I have a photo of the coffee shop on my phone."
        char1.talk "Do you want to see it?"
        pl "Sure!"
        char1.talk "Just give me a minute to find it..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call24.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Here it is!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call25.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        pl "Looks nice and cozy."
        char1.talk "Yeah well, I took it before opening hours."
        char1.talk "Once it's open, it's pretty busy most of the time."
        pause 0.5
        char1.talk "I've got some images of Joy as well."
        char1.talk "Want to see them?"
        pl "Sure, why not."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call24.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "One of the regulars took them and sent them to me... *giggles*"
        char1.talk "First one when she came in."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call26.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        pl "Yeah, that's definitely Joy!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call24.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Damn, she's really hot!"
        char1.talk "Here's the second when she left."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call27.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        "Although it's a bit hard to concentrate on Joy's photos with [char1.fname]'s exposed tits and nipples..."
        "...you totally agree."
        pl "Yes, she's super hot!"
        pl "But so are you, [char1.fname]."
        $ char1.change_affection(5)
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call23a.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Thanks [char1.playername]!"
        char1.talk "I've always thought so myself. But since being here on the island, I'm not so sure any more."
        if player.check_charm(4) == True:
            pl "You have what it takes..."
            pl "A sweet smile!"
            pl "Curves in all the right places."
            pl "Mixed with a great and fun personality."
            call change_char_max_affection (char1, 5) from _call_change_char_max_affection_78
            $ char1.change_affection(10)
            char1.talk "You're sweet!"
            char1.talk "And pretty hot yourself! *winks*"
        elif True:
            pl "You'd stand out anywhere else, I'm sure of it."
            char1.talk "Ummm... Okay."
            "Yeah well... That wasn't really a compliment!"
        char1.talk "Before I tell you the rest of the story..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call14.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Cheers!"
        pl "Cheers!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "It was one of those colder autumn days, when she came in to get a hot coffee."
        char1.talk "I turned around to get it for her, when somehow I felt her eyes on my back."
        pause 0.3
        char1.talk "You know, sometimes you can just feel it when someone stares at you."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "I was wearing my standard working attire, which is pretty tight around the chest... *giggles*"
        char1.talk "Had I stretched like this..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call20.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "I'd probably have blown off the buttons! *giggles some more*"
        "It's really distracting when she shows off like that..."
        $ player.change_lust(char1.sexiness)
        char1.talk "Well anyway, when I turned around to hand her the coffee. *smiles*"
        pause 0.5
        char1.talk "You okay?"
        pause 0.3
        pl "Yeah. Please go on. *smiling*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "She asked me if I'd be interested in a well paying job."
        char1.talk "On a fantastic island, doing basically the same I do in the coffee shop."
        char1.talk "When I asked her about details, she handed me her card..."
        pause 0.3
        char1.talk "...and told me to come to her office tomorrow in case I wanted to know some more details."
        char1.talk "CEO of HI Inc.\nJoy Resplandor"
        char1.talk "I was really intrigued. Not just by the job offer, but also by Joy."
        pause 0.5
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call17.webp") with dissolve:
            zoom 0.5
        pause 0.7
        "You both have another drink before she continues..."
        pause 1.0
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call18.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "So the next day I went into the huge building on the other side of the road."
        pl "It's quite impressive. I've been there too."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "Yes, it really is!"
        char1.talk "After waiting a couple of minutes, I was led into her office."
        char1.talk "She told me about the island, the lottery and the lottery winner! *smiles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "Then she asked my about my age and other stuff I don't recall exactly."
        char1.talk "The interesting part started with an innocent question."
        pause 0.5
        char1.talk "She asked me if I'd mind wearing a bikini working on the island."
        char1.talk "I told her that I wouldn't have a problem with that."
        char1.talk "Then she asked me if I'd be willing to wear it right now..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") with dissolve:
            zoom 0.5
        pause 0.6
        char1.talk "Well you know. Really???"
        char1.talk "On a cold autumn day in an office of a woman I had just met..."
        pause 0.4
        char1.talk "I wasn't very comfortable with it, but I agreed."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "She had her assistant, a cute 20 year old fetch the bikini."
        char1.talk "Had I known that her idea of a bikini was barely covering my nipples..."
        pause 0.4
        char1.talk "I'd probably have said no."
        char1.talk "But well... Here I was with that incredible job offer. I wasn't going to let a tiny bikini stop me from getting the job."
        pl "Ummm..."
        pause 0.5
        char1.talk "You're not going to ask if I have a picture, are you? *giggles*"
        pl "You know... It'd be nice to see it. *smiles*"
        char1.talk "Really? *giggles* I'm sitting topless in front of you!"
        pl "Please!?"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call21.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Okay... I think I have three of them."
        char1.talk "I'll send them to you. But later, okay?!"
        $ yumiko.add_queued_sexting(500,500,4)
        $ yumiko.add_queued_sexting(501,506,18)
        $ yumiko.add_queued_sexting(502,507,34)
        pl "Thanks! *smiling*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call28.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "I changed into the tiny little bikini and decided to give Joy a bit of a show!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call28.webp"):
            subpixel True zoom 0.5 align (0.7,0.4)
            ease 1.3 zoom 0.68
        $ renpy.pause(1.8,hard=True)
        char1.talk "[char1.playername], you're staring. *smirks*"
        pl "Ummm..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call28a.webp") with dissolve:
            zoom 0.65 align (0.7,0.42)
        pause 0.7
        pl "{b}Damn!{/b}"
        $ player.change_lust(char1.sexiness+2)
        char1.talk "I know, pushing them up makes them look really big. *chuckles*"
        pause 0.4
        char1.talk "Well anyway, I guess Joy liked my performance..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call28a.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "...or maybe the way I filled out the bikini. Who knows... *giggles*"
        char1.talk "In any case, as you already know. I got the job!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call16.webp") at zoom_c(0.5) with dissolve
        pause 0.7
        char1.talk "Sitting at the bar with you, wearing even less than the tiny bikini. *giggles*"
        pause 0.4
        pl "I'm very happy you're here now. *smiles*"
        char1.talk "Me too!"
        pause 1.0

    call actions_used (1) from _call_actions_used_76
    char1.talk "Oh wow! Time really flies when you're having fun. *smiles*"
    pause 1.0
    char1.talk "I think we should wrap it up for today and go to bed."
    "She starts putting her breasts back into the dress..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call29.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I hope you had a good time."
    pl "Sure! You were great company!"
    pl "And not just because of... {w}well, you know... {w}the exposed breasts..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I certainly hope not! *smiles*"
    char1.talk "But I guess you didn't mind having to look at them all the time... *giggles*"
    pl "Er... I don't really know how to answer that. *smiling*"
    char1.talk "You don't have to!"
    pause 0.4
    char1.talk "Let's finish the drinks before we call it a night..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call17.webp") with dissolve:
        zoom 1.0 align (0.7,0.0)
    pause 0.7
    pl "Cheers!"
    char1.talk "Cheers!"
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30a.webp") with dissolve:
        zoom 0.6 align (0.75,0.05)
    pause 0.7
    "She pulls you close for a kiss..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call31.webp"):
        zoom 0.5
    call action_kiss_mouth (char1, "nightbar_bar", True, 0, False) from _call_action_kiss_mouth_9
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30a.webp"):
        zoom 0.5
    with dissolve
    pause 1.0
    char1.talk "Good night and sweet dreams. *smiles*"
    pl "You too [char1.fname]."
    "[char1.fname] leaves the night bar and you head back to your room."
    call advance_time (actions_used) from _call_advance_time
    return "goto_player_room"

    label nightbar_last_call_yumiko_blowjob:
    $ char1.add_dream_image("1bar")
    $ char1.add_dream_image("2bar")
    char1.talk "Yes, I can see that it must be pretty hard... *smirks*"
    $ char1.change_lust(10)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call20.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    char1.talk "...and I really like that."
    pause 0.4
    "You just stare at her..."
    char1.talk "Don't look at me like that."
    char1.talk "I want some fun and eye candy too!"
    char1.talk "Since I've been sitting with you topless for some time now, don't you think it's only fair..."
    "Not really sure where this is going..."
    pl "Ummm..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call21.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    char1.talk "Please... I want to see it."
    char1.talk "May I...?"
    "Not really knowing how to say no to a beautiful busty girl sitting in front of you."
    pl "Yeah, I guess."
    char1.talk "Cool!"
    "She opens your pants expertly and grabs your dick with her left hand..."
    $ char1.add_pl_interaction("handjob")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call32.webp") with dissolve:
        zoom 0.5
    pause 0.6
    "...squeezing it a little."
    $ char1.change_lust(10)
    char1.talk "Yes! Pretty hard... *smirks*"
    char1.talk "You really have a nice big dick [char1.playername]!"
    pause 0.4
    pl "Er... Thanks!"
    pause 0.5
    char1.talk "It barely fits into my hand. *smiles*"
    "She gently squeezes your dick some more..."
    pause 0.4
    char1.talk "I know I said I only wanted to see it..."
    char1.talk "But you don't mind if I do some more with it?"
    pause 0.4
    pl "Not at all. *grinning*"
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_handjob_v1.webm")) at zoom_c(0.5)
    $ renpy.pause(1.8,hard=True)
    pl "Mmmm.... *moans*"
    $ player.change_lust(char1.sexiness+4)
    pause 0.4
    char1.talk "So I take it you like what I'm doing."
    pause 0.4
    pl "Yes, definitely. *grinning*"
    pause 0.6
    "You look up at her beautiful face."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call33.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    char1.talk "If you want me to stop, please tell me. Okay? *smiles*"
    pl "Mmmmmm... aaahhh... *moans*"
    call actions_used (1) from _call_actions_used_77
    char1.talk "I guess that means {i}please don't stop{/i}?"
    pl "No... I mean yes, please don't stop."
    "She even increases the pace a litte..."
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_handjob_v2.webm")) at zoom_c(0.5)
    $ renpy.pause(1.8,hard=True)
    char1.talk "You can look at my tits if you want while I stroke your dick!"
    char1.talk "I won't be offended... *giggles*"
    pause 0.5
    char1.talk "I might even like it! *smirks*"
    pause 0.6
    "You take a good look at her big tits with the erect nipples..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call34.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    $ player.change_lust(char1.sexiness * 2)
    "Looking at her swaying tits while she strokes your dick is almost too much to handle..."
    pause 0.4
    pl "Ahhhhh... Mmmmmmm... Yes! *moans*"
    pause 0.4
    pl "I'll cum any moment now!"
    char1.talk "Wait! Or we'll have quite a mess here!"
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_handjob_v1.webm")) at zoom_c(0.5)
    $ renpy.pause(1.8,hard=True)
    "She slowes down the pace, before she gets down on her knees."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call35.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "Looking at your huge dick in front of her small mouth..."
    char1.talk "Now that's going to be interesting! *smiles*"
    $ char1.add_pl_interaction("blowjob")
    "She licks your tip, before she swallows half of your shaft with her mouth..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call36.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Mmmmmpfff... *suck*"
    $ char1.change_lust(15)
    $ renpy.start_predict("*Yumiko_nightbar_blowjob*")
    "...and starts sucking on it."
    $ ll_cameras = []
    $ ll_cameras.append(cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_blowjob", {"face_x":1630, "face_y":950, "breasts_x":0, "breasts_y":0, "pussy_x":0, "pussy_y":0}))
    $ ll_sequence = [1,2,2,2,3,3,4,4,5,5,5,6,6,6,6,5,5,5,4,3,3,2,1,1,1]
    $ l_cum_control = {"cum_x":1630, "cum_y":950, "cum_fps":50, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":pl, "what":"{b}Oh my God{/b}! I'm almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"*slurp* *suck*", "pause":1.2})
    $ ll_speed_talk = [{"fast":"Yes, this is so good!", "faster":"*moans* You're incredible, Yumiko!", "slow":"Suck me harder! *moans*", "slower":"Please don't slow down!"}]
    call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 0.9, i_char=player) from _call_interactive_sex_81
    pl "Oh... Wow! It feels so good!"
    pause 2.5
    char1.talk "Mmmmmm... mmm... *slurp* *mppff*"
    pause 2.0
    "You almost cannot believe it!"
    "An incredibly busty asian cutie is kneeling in front of you, sucking your dick..."
    pl "Oh my God, [char1.fname]! Mmmmm.... aaaahhh..."
    char1.talk "Ey'mmmm gunnna make yooo cummm so harddd! *mumbling*"
    "[char1.fname] sucks on your dick like a mad woman..."
    pause 0.5
    pl "I'm cumming any moment now!"
    "She still doesn't stop her sucking and tongue licking..."
    char1.talk "*suck* *slurp* *suck* Mmmmmm..."
    pause 1.5
    pl "Cummmmmminnng noooowww..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call36.webp") with dissolve:
        zoom 0.7 xpos -512 ypos -288
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call36_cum.webp") with dissolve:
        zoom 0.7 xpos -512 ypos -288
    pause 0.3
    $ renpy.stop_predict("*Yumiko_nightbar_blowjob*")
    $ renpy.free_memory()
    "You shoot a heavy load of hot cum into her mouth."
    "She tries to swallow it all, but it's just too much..."
    $ player.change_lust(-50)
    $ player.change_endurance(-40)
    char1.talk "Ummm... *mppfff* *slurp*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call37.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "It didn't work without making some mess... *chuckles*"
    char1.talk "From the looks of it, you really needed it! *chuckles some more*"
    pl "You were incredible [char1.fname]!"
    pause 0.5
    char1.talk "Thanks! I'm glad you enjoyed it. *smiles*"
    char1.talk "Let me clean that up for you."
    "She almost swallows your whole dick..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call38.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "And sucks it dry!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call39.webp") with Dissolve(1.4):
        zoom 0.5
    pause 0.7
    char1.talk "Hmmmpfff..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call35.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    char1.talk "Yes, that's better! All cleaned up!"
    char1.talk "I really enjoyed that!"
    pause 0.5
    pl "Trust me, I enjoyed it more! *smiling*"
    char1.talk "I'm pretty sure of it. *giggles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call33.webp") at zoom_c(0.5) with dissolve
    pause 0.7
    char1.talk "Do you need help packing it back in? *smiles*"
    pause 0.4
    pl "Haha. *laughing* Thanks for the offer, but I think I can manage."
    pause 0.4
    char1.talk "Okay, so I guess I'll get decent as well."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call29.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I can't run around the hotel all exposed. *winks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "She looks at you for a moment, checking your progress..."
    char1.talk "All done?"
    pl "Yeah!"
    char1.talk "Me too."
    pause 0.6
    pl "I really enjoyed our evening [char1.fname]."
    pl "And not just the well you know... last part."
    char1.talk "I enjoyed it too [char1.playername]. All of it! *smiles*"
    call change_char_max_love (char1, 5) from _call_change_char_max_love_21
    $ char1.change_love(10)
    char1.talk "Time to get some sleep?"
    pl "Yes, I guess."
    char1.talk "Let's finish the drinks before we call it a night..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call17.webp") with dissolve:
        zoom 1.0 align (0.7,0.0)
    pause 0.7
    pl "Cheers!"
    char1.talk "Cheers!"
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30a.webp") with dissolve:
        zoom 0.6 align (0.75,0.05)
    pause 0.7
    "She stands up and pulls you close for a kiss..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call31.webp"):
        zoom 0.5
    call action_kiss_mouth (char1, "nightbar_bar", True, 0, False) from _call_action_kiss_mouth_35
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call30a.webp"):
        zoom 0.5
    with dissolve
    pause 1.0
    char1.talk "Good night and sweet dreams. *smiles*"
    pl "You too [char1.fname]."
    $ char1.add_scene_seen("Bartender_nightbar_last_call_blowjob")
    "[char1.fname] leaves the night bar and you head back to your room."
    call advance_time (actions_used) from _call_advance_time_7
    return "goto_player_room"

    label nightbar_last_call_yumiko_not_alone:
    pause 0.7
    char1.talk "Unfortunately the bar is still not empty..."
    char1.talk "I have to get back to work."
    pl "Sure, I understand [char1.fname]."
    pl "I hope we can continue this another time."
    char1.talk "Drop by any time. You know where to find me!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call3.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "She walks back to the counter."

    label nightbar_last_call_yumiko_end:
    call advance_time (actions_used) from _call_advance_time_10
    return "nothing"





label nightbar_last_call_jennifer(char1):
    "Shit, it seems she noticed you staring..."
    "But instead of getting mad, she takes a deep breath..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call7.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "Which makes her huge round knockers look even bigger..."
    "...They're almost ready to burst from her dress..."
    "You're still fantasizing about her tits when..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Hello you down there! *giggles*"
    char1.talk "Like what you see?"
    "Since she doesn't seem to be angry...\n...You decide to play along."
    pl "Yes, very much so! *smiling*"
    pl "I guess a bit too much since you caught me staring."
    if (len(list_of_chars_display_3) == 0 and char1.get_scene_seen("Bartender_nightbar_last_call_alone") and joy.get_event_seen("Office3") and char1.get_action_allowed("event_laboratory")):
        if char1.check_affection(3, 0, False) == True and l_bartender.check_love(2, 0, False) == True:
            if char1.get_event_seen("Jennifer_transformation") == False:
                pause 0.3
                char1.talk "*smiles* Since the bar is already empty except for the two of us, why don't we have a drink and talk for a bit?"
                pause 0.3
                pl "Sure, great idea."
                scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call2.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                char1.talk "Would you like to sit at the bar?"
                pause 0.4
                pl "Okay, lead the way."
                scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call5.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                "You follow her to the bar."
                call transformation_event_jennifer (char1) from _call_transformation_event_jennifer
                return "goto_player_room"
            elif True:
                $ char1.add_action_cooldown("event_laboratory", 48*3)
                char1.talk "I know I've told you the story about my gene therapy and body transformation already..."
                char1.talk "...but would you like to hear it again?"
                menu:
                    "Sure, why not" if True:
                        pl "Yes please, it was great, I'd love to hear it again!"
                        char1.talk "Cool!"
                        char1.talk "Let's have a drink at the bar while I tell you."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call2.webp") with dissolve:
                            zoom 0.5
                        pause 0.7
                        pl "Sure!"
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call5.webp") with dissolve:
                            zoom 0.5
                        pause 0.7
                        "You follow her to the bar."
                        call transformation_event_jennifer (char1) from _call_transformation_event_jennifer_1
                        return "goto_player_room"
                    "Maybe another time" if True:

                        pl "It was really interesting. Maybe we can do that another time?"
                        char1.talk "Sure, just tell me when you'd like to hear it again. I love telling it."
                        char1.talk "Well about your staring..."

    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call2.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "You were so obvious about it, there was no way I couldn't notice it. *giggles*"
    call create_list_of_chars_display (False) from _call_create_list_of_chars_display_9
    if len(list_of_chars_display_3) == 0:
        pause 0.7
        char1.talk "Hmmm, the bar is empty right now..."
        char1.talk "So here is something for you to dream about tonight!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call9.webp") with dissolve:
            zoom 0.5
        pause 1.0
        pl "Oh {b}wow{/b}!"
        pause 0.7
        char1.talk "Do they look as good as you imagined?"
        $ player.change_lust(char1.sexiness+2)
        pl "Oh no! They look even better!\nYou have incredible breasts Jennifer!"
        char1.talk "Thank you! I love them too! *smirks*"
        $ char1.add_pl_interaction("tease_boobs")
        char1.talk "Want me to squeeze them for you?"
        "Without waiting for an answer..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call10.webp") with dissolve:
            zoom 0.5
        pause 1.0
        $ player.change_lust(l_bartender.sexiness+4)
        if player.get_action_allowed("jennifer_titfight") == True and joy.get_event_seen("Office2") == True:
            $ char1.add_scene_seen("Bartender_nightbar_last_call_alone")
            $ player.add_action_cooldown("jennifer_titfight", 5*48)
            char1.talk "Did I tell you that these two..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call12.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "...won several titfight competitions?"
            pl "Umm no..."
            pl "...and ehmm Jennifer what's a titfight?"
            char1.talk "Ah yes, how could you know... *giggles*"
            char1.talk "...since you obviously cannot participate. *giggles some more*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call9.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Basically it's a contest where women with big breasts kinda fight with their goodies..."
            char1.talk "I guess that didn't explain it very well. Let me try again..."
            char1.talk "Girls get topless and press their enormous breasts together."
            char1.talk "Really smash and push until one of the girls gives up."
            char1.talk "My nipples can get so hard, that one time they pushed the other girls nipples more than half an inch into her breasts..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call13.webp") with dissolve:
                zoom 0.5
            pause 0.7
            $ player.change_lust(char1.sexiness)
            char1.talk "Most of the time one pair of breasts just cannot take the stress any more and really gets crushed."
            char1.talk "My breasts are so full and dense that they are almost never crushed. *smiles*"
            char1.talk "That's the reason, apart from my super hard nipples, that I won many titfights..."
            char1.talk "...also against girls with much bigger breasts..."
            char1.talk "Just like some on the island..."
            char1.talk "How I'd love to crush some of them with my tits and nipples..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call14.webp") with dissolve:
                zoom 0.5
            pause 0.7
            pl "Ummm... [char1.fname]... Your nipples..."
            char1.talk "Oh sorry, I got carried away for a moment..."
            char1.talk "They can get really huge and hard when I'm excited! *giggles*"
            char1.talk "Would you like to touch them?"
            pause 1.0
            "Thinking about touching her hard nipples and maybe even giving her tits a squeeze drives you crazy with lust..."
            $ player.change_lust(char1.sexiness)
            $ player.add_effect("erection")
            "...but since you are almost ready to blow you load inside your pants, you think it's better not to push your luck."
            pl "Er... Normally I'd really love to..."
            char1.talk "I hear a but coming."
            pl "Yeah... I don't know how to say that..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call15.webp") with dissolve:
                zoom 0.5
            pause 0.7
            "She takes a look between your legs and notices the huge bulge in your pants..."
            char1.talk "Oh! I'm really sorry!"
            char1.talk "I was so excited telling you the about the titfighting, that I forgot that I was topless all the time."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call14.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Parading my huge tits in front of your face..."
            char1.talk "I better put them back in before we have an accident. *smirks*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call2.webp") with dissolve:
                zoom 0.5
            pause 0.7
            "Well, you hadn't thought that you'd be relieved when a girl as hot as Jennifer puts her tits back into her dress..."
            pl "Thank you Jennifer."
            char1.talk "I think I'll have to talk to Joy about a titfight... *musing*"
            char1.talk "Did you know that she loves it too?"
            pl "Umm no..."
            char1.talk "Hmmmm, yes that's a great idea... *talking to herself*"
            pause 0.4
        elif True:
            char1.talk "Take another good look before I'll have to close the bar. *smiles*"
            char1.talk "So you have something to dream about tonight!"
            pause 1.0
            "Too bad she puts her dress back on..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call2.webp") with dissolve:
                zoom 0.5
            pause 0.7

        char1.talk "I've kept you long enough..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_last_call3.webp") with dissolve:
            zoom 0.5
        char1.talk "It's really time to close up now."
        char1.talk "Have a good night [char1.playername]."
        scene expression ("scenes/Jennifer/nightbar/Jennifer_nightbar_last_call2.webp") with dissolve:
            zoom 0.5
        char1.talk "...and sweet dreams! *smiles*"
        pl "You too Jennifer!"
        "{b}Wow{/b}! What an incredible girl!"
        call advance_time (1) from _call_advance_time_27
    elif True:
        pause 0.7
        char1.talk "Unfortunately we have to continue our discussing later."
        char1.talk "The bar's still busy and I have to get back to work."
        pl "I don't have to like it, but I understand [char1.fname]."
        char1.talk "Drop by any time. You know where to find me!"
        scene expression ("scenes/Jennifer/nightbar/Jennifer_nightbar_last_call5.webp") with dissolve:
            zoom 0.5
        pause 0.7
        "She walks back towards the bar."

    return "nothing"





label action_nightbar_poledance(char1, i_show_intro=True):
    $ l_shower = False
    $ l_special = False

    if i_show_intro == True:
        $ l_random = renpy.random.randint(1,3)
        if l_random == 1:
            pl "Hey [char1.fname], it'd be so sexy if you could pole dance for me."
        elif l_random == 2:
            pl "Hi [char1.fname], I'd really love to watch you pole dance. *smiles*"
        elif True:
            pl "[char1.fname], I was wondering if you'd pole dance for me?"

        if char1.get_action_allowed("poledance") == False:
            $ l_text = char1.get_action_not_allowed_text("poledance")
            char1.talk "[l_text]"
            return "do_return"

        if char1.get_action_allowed("anger_block") == False:
            call action_closeup (char1, location, False, False) from _call_action_closeup_28
            $ l_text = char1.get_action_not_allowed_text("anger_block")
            char1.talk "[l_text]"
            $ char1.change_anger(3)
            pl "Ummm... Yeah, sorry."
            hide screen closeup
            $ g_intimate_char = no_char
            $ location_detail = ""
            $ char1.add_action_cooldown("poledance", 4, "You just asked me the exact same thing not long ago and I already said no!")
            return "nothing"

        if char1.check_affection(2) == False or char1.check_love(1) == False:
            char1.talk "Sorry [char1.playername], but I'm really not in the mood right now.\nAsk me again when we know each other a little better."
            $ char1.add_action_cooldown("poledance", 40, "You've already asked me for a pole dance today.")
            return "do_return"

    if char1.id == alice.id:
        call action_nightbar_poledance_alice (char1) from _call_action_nightbar_poledance_alie
        if _return == "cum_in_pants":
            jump action_nightbar_poledance_end_cum_in_pants
        jump action_nightbar_poledance_end2

    elif char1.id == amy.id:
        call action_nightbar_poledance_amy (char1) from _call_action_nightbar_poledance_amy
        jump action_nightbar_poledance_end2

    elif char1.id == jessica.id:
        call action_nightbar_poledance_jessica (char1) from _call_action_nightbar_poledance_jessica
        return "goto_player_room"

    elif char1.id == yvette.id:
        call action_nightbar_poledance_yvette (char1) from _call_action_nightbar_poledance_yvette
        jump action_nightbar_poledance_end2

    if renpy.loadable("scenes/" + char1.fname + "/" + char1.fname + "_nightbar_poledance1_night" + unicode(char1.nightwear) + ".jpg"):
        $ lf_nightwear = "_night" + unicode(char1.nightwear)
        char1.talk "You can head over to the pole dance area. Give me a minute to get ready. I'll be there shortly."
        pl "Sure."
    elif True:
        $ lf_nightwear = ""
        char1.talk "You can head over to the pole dance area. I need to change first.\nWon't take that long, I promise."
        pl "Okay."

    $ start_scene()
    $ l_char_lust_check_ok = False
    $ menu_active = True
    scene expression ("locations/loc_nightbar_poledance.webp"):
        zoom 0.5
    with fade
    pause 1.5
    if lf_nightwear == "":
        call actions_used (1) from _call_actions_used_9
        "Not long in girls' terms..."
        "You've waited for almost half an hour!"
        if char1.id == amy.id:
            $ lf_nightwear = "_night2"

    if char1.id == lacey.id:
        call action_nightbar_poledance_lacey (char1) from _call_action_nightbar_poledance_lacey
        jump action_nightbar_poledance_end2

    elif char1.id == faye.id:
        call action_nightbar_poledance_faye (char1) from _call_action_nightbar_poledance_faye
        if _return == "cum_in_pants":
            jump action_nightbar_poledance_end_cum_in_pants
        $ char1.add_scene_seen("Nightbar_poledance")
        jump action_nightbar_poledance_end2

    elif char1.id == heather.id:
        call action_nightbar_poledance_heather (char1) from _call_action_nightbar_poledance_heather
        if _return == "cum_in_pants":
            jump action_nightbar_poledance_end_cum_in_pants
        $ stop_scene()
        return "do_return"

    $ char1.add_scene_seen("Nightbar_poledance")
    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance1[lf_nightwear].jpg") with dissolve
    char1.talk "So, here I am. Enjoy the show. *smiles*"
    pl "I'm pretty sure I will. You look spectacular [char1.fname]."
    char1.talk "Thank you [char1.playername]."
    $ player.change_lust(10)
    if player.cum_in_pants():
        jump action_nightbar_poledance_end_cum_in_pants
    "She is so incredibly sexy in that outfit."
    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance2[lf_nightwear].jpg") with dissolve
    pause 1.5
    char1.talk "This one is just for you [char1.playername]."
    "You get closer to get a better look at her incredible body."
    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance2[lf_nightwear].jpg"):
        zoom 1.0 xpos 0
        subpixel True
        linear 1.0 zoom 1.5 xpos -300 ypos -100
    pause 1.5
    $ player.change_lust(10)
    if player.cum_in_pants():
        jump action_nightbar_poledance_end_cum_in_pants
    "Wow, she sure knows what she's doing..."
    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance3[lf_nightwear].jpg") with dissolve
    $ player.change_lust(10)
    if player.cum_in_pants():
        jump action_nightbar_poledance_end_cum_in_pants
    pl "You look amazing [char1.fname]. I love this pose."
    char1.talk "Thank you [char1.playername]... and now enjoy the grand finale."
    if char1.id == alice.id:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg") with dissolve:
            zoom 0.5
        "{b}Damn{/b}, her costume is completely open now,\nexposing her magnificent tits."
        "You just have to get a closer look..."
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg"):
            zoom 0.5
            subpixel True
            linear 1.0 zoom 1.25 xpos -1000 ypos -200
        pause 1.4
        "All you can think about now is to play with her huge melons."
        pause 0.6
    elif True:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg") with dissolve
        "Every one of her moves is just so damn sexy."

    $ player.change_lust(10)
    if player.cum_in_pants():
        jump action_nightbar_poledance_end_cum_in_pants
    pl "Yeah, yeah, go [char1.fname], go."
    if char1.id == yvette.id:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg"):
            zoom 1.0 xpos 0
            subpixel True
            linear 1.0 zoom 1.75 xpos -100 ypos -200
        pause 1.4
        "Wow, she is damn sexy. Look at that cute face."
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg"):
            zoom 1.75 xpos -100 ypos -200
            subpixel True
            linear 0.6 zoom 1.75 xpos -300 ypos -400
        pause 1.0
        "...and her incredible boobs"
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance4[lf_nightwear].jpg"):
            zoom 1.75 xpos -300 ypos -400
            subpixel True
            linear 1.0 zoom 1.75 xpos -700 ypos -400
        pause 1.4
        "...not to forget her amazing ass and thighs."
        "Wow, just wow..."

    if char1.id == alice.id:
        if char1.check_lust(3, False) == True:
            $ l_char_lust_check_ok = True
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance6[lf_nightwear].jpg") with dissolve
        elif True:
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance5[lf_nightwear].jpg") with dissolve
    elif True:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance5[lf_nightwear].jpg") with dissolve
    pause 1.5
    char1.talk "I hope you enjoyed the show [char1.playername]. I sure did. *smiles*"
    "You are at a loss for words for a moment..."
    if l_char_lust_check_ok:
        "Still mesmerized by her exposed tits."
    pl "Uhmmm yes very much. *stammering*"
    "Man that was lame. Luckily she doesn't seem to mind."
    $ player.change_lust(10)
    if player.cum_in_pants():
        jump action_nightbar_poledance_end_cum_in_pants

    label action_nightbar_poledance_menu:
    char1.talk "So tell me [char1.playername], what did you enjoy the most?"
    $ menu_active = True
    menu:
        "Tell her you loved everything." if True:
            pl "I love everything about you [char1.fname], so it is very hard to say."
            char1.talk "Oh, you are sweet. Thank you."
            $ char1.change_affection(15)
        "Tell her you loved her powerful and sexy moves." if True:

            pl "You are so fit and all your moves look so powerful and sexy."
            char1.talk "I trained a lot to get that far. Great you noticed and it pays off."
            $ char1.change_affection(20)
        "Tell her you loved how she looked at you." if True:

            pl "I really enjoyed the way you were looking at me."
            if char1.check_tease_sexual(2, 0, False) == True:
                char1.talk "Wow, you noticed that with all that exposed flesh. *happy smile*"
                $ char1.change_affection(20)
                $ char1.change_love(10)
                if player.get_effect_state("blue pill") > 0:
                    char1.talk "Oh my God, is that all you in your pants? Is it always that huge?"
                    $ char1.change_lust(20)
                    pl "Ehmm, well no, not like that. *stammering*"
                elif True:
                    char1.talk "I can see that your little friend enjoyed it too."
                    $ char1.change_lust(10)
            elif True:
                char1.talk "You are always the gentleman. Thank you."
                $ char1.change_affection(10)
        "You did not enjoy it that much." if True:

            pl "Ummm [char1.fname], I'm really sorry, but I didn't enjoy it that much."
            char1.talk "You know what [char1.playername], you are an asshole. Next time you can dance for yourself."
            $ char1.change_affection(-20)
            $ char1.change_anger(20)

    jump action_nightbar_poledance_end

    label action_nightbar_poledance_end_cum_in_pants:
    "You could not hold it any longer and erupt in your pants."
    "Full of shame you flee to your room to clean yourself up."
    $ location = "player_room"
    $ location_detail = ""
    $ menu_active = False
    $ selected_char = no_char
    $ stop_scene()
    $ player.change_lust(-40)
    $ player.change_endurance(-30)
    call actions_used (1) from _call_actions_used_52
    jump action_nightbar_poledance_end2

    label action_nightbar_poledance_end:
    char1.talk "Enjoy the rest of your evening [char1.playername]. *smiles*"
    pl "You too [char1.fname]."
    if l_special == True:
        "With that she disappears behind the curtain."
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_poledance_sex17[lf_nightwear].jpg") with dissolve
        pause 1.0
        if l_shower == True:
            "You take another look at the now empty room, get dressed and go to your room to take a shower."
        elif True:
            "You take another look at the now empty room, get dressed and head back to the night bar."

    label action_nightbar_poledance_end2:
    $ char1.add_action_cooldown("poledance", 40, "I've already danced for you today.")
    call actions_used (1) from _call_actions_used_399
    $ char1.add_pl_interaction("tease_body")
    $ location_detail = ""
    $ menu_active = False
    $ stop_scene()
    if l_shower == True:
        $ location = "player_room"
        call pl_action_shower (location, ["", "", "After a long shower thinking about " + unicode(char1.fname) + ", you finally get out..." ]) from _call_pl_action_shower_3
        call main_game_background (location, location_detail, _return) from _call_main_game_background_94
        return "goto_player_room"
    elif True:
        show screen main_game(location)
        return "do_return"





label action_nightbar_drink(char1, i_auto_succeed=False, i_show_intro=True):
    $ l_masturbate = False
    $ l_lust_check = False
    $ l_bartender = jobs.bartender
    $ l_auto_succeed = i_auto_succeed

    if char1.id == sara.id and char1.nightwear == 2 and player.get_quest_state("Background_of_Sara_experiments", char1) == 7:
        $ l_auto_succeed = True

    if i_show_intro == True:
        pl "[char1.fname], would you like to have a drink with me?"

        if char1.get_action_allowed("nightbar_drink") == False and l_auto_succeed == False:
            $ l_text = char1.get_action_not_allowed_text("nightbar_drink")
            char1.talk "[l_text]"
            return "do_return"

        if char1.get_action_allowed("anger_block") == False and l_auto_succeed == False:
            call action_closeup (char1, location, False, False) from _call_action_closeup_29
            $ l_text = char1.get_action_not_allowed_text("anger_block")
            char1.talk "[l_text]"
            $ char1.change_anger(3)
            pl "Ummm... Yeah, sorry."
            hide screen closeup
            $ location_detail = ""
            $ char1.add_action_cooldown("nightbar_drink", 4, "You just asked me the exact same thing not long ago and I already said no!")
            return "do_return"

        if l_auto_succeed == False and char1.check_affection(1) == False:
            char1.talk "Sorry [char1.playername], but I'm not in the mood right now. Maybe another time."
            pl "That's a pity, but I understand."
            return "do_return"
        $ char1.change_lust(100)
        $ char1.change_affection(100)
        #$ char1.change_love_max(100)
        $ char1.change_love(100)
        char1.talk "I'd love to. I thought you'd never ask."
        char1.talk "What kind of my nightwear do you want to see?"
        menu:
            "1st nightwear":
                pl "1st nightwear"
                $char1.nightwear = 0
                char1.talk "Do you like it?"
            "2nd nightwear":
                pl "2nd nightwear"
                $char1.nightwear = 1
                char1.talk "Do you like it?"
                pl "Sure"
            "3rd nightwear" if char1.id != delizia.id:
                pl "3rd nightwear"
                $char1.nightwear = 2
            "4th nightwear" if char1.id == sara.id or char1.id == aly.id:
                pl "4th nightwear"
                $char1.nightwear = 3
        char1.talk "Do you want to know some very interesting information about me?"
        menu:
                "Yes, of course":
                    ###1-yes; 0,2-no
                    if char1.id ==alice.id: 
                        if char1.nightwear==1:
                            char1.talk "When I get drunk, I want a sequel"
                            pl "Okay"
                        elif char1.nightwear==0 or char1.nightwear==2:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                    if char1.id ==aly.id: 
                        if char1.nightwear==0:
                            char1.talk "When I get drunk, I want a sequel"
                            pl "Okay"
                        elif char1.nightwear==1 or char1.nightwear==2:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                        else:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                    ###0-yes; 1- yes ,2- no            
                    if char1.id ==amy.id: 
                        if char1.nightwear==0:
                            char1.talk "When I get drunk, I want a sequel"
                            pl "Okay"
                        elif char1.nightwear==1:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                        elif char1.nightwear==2:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    "..."
                                "No, that's not interesting":
                                    jump action_nightbar_drink_end
                    if char1.id == delizia.id or char1.id == desire.id or char1.id == eva.id or char1.id == heather.id:
                        char1.talk "If I get drunk, I'll want to sleep"
                        pl "Ohhh"
                        "Continue this scene?"
                        menu:
                            "Sure":
                                "..."
                            "No, that's not interesting":
                                jump action_nightbar_drink_end
                    if char1.id == renee.id or char1.id == faye.id:
                        char1.talk "A little surprise awaits you"
                        pl "Well"
                    if char1.id == sara.id:
                        if char1.nightwear == 0:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                        elif char1.nightwear == 1:
                            char1.talk "When I get drunk, I want to dance"
                        else:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                    if char1.id == jessica.id or char1.id == natasha.id:
                        if char1.nightwear == 2:
                            char1.talk "When I get drunk, I want a sequel"
                            pl "Okay"
                        elif (char1.id == lacey.id or char1.id == jessica.id) and (char1.nightwear == 0 or char1.nightwear == 1):
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    "..."
                                "No, that's not interesting":
                                    jump action_nightbar_drink_end
                                
                    
                    if char1.id ==lacey.id:
                        if char1.nightwear==2:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                        elif char1.nightwear==0 or char1.nightwear==1:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                    if char1.id == ivy.id:
                        if char1.nightwear ==1:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                        else:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                    if char1.id == yvette.id:
                        if char1.nightwear == 0:
                            char1.talk "If I get drunk, I'll want to sleep"
                            pl "Ohhh"
                            "Continue this scene?"
                            menu:
                                "Sure":
                                    char1.talk "Where we will sit?"
                                "No, that's not interesting ":
                                    jump action_nightbar_drink_end
                        else:
                            char1.talk "A little surprise awaits you"
                            pl "Well"
                "No, let's keep it a secret for now":
                    char1.talk "Really?"
                    
                
    $ l_inclination = 1
    $ menu_active = True
    $ green_pill_used = False
    $ pink_pill_used = False
    $ pink_pill2x_used = False
    $ purple_tablet_used = False

    $ char1.add_pl_interaction("others")

    if char1.id == alice.id and char1.nightwear == 0 or char1.id == alice.id and char1.nightwear == 2:
        call action_nightbar_drink_alice_dress0_2 (char1) from _call_action_nightbar_drink_alice_dress0_2
        jump action_nightbar_drink_end
    elif char1.id == alice.id and char1.nightwear == 1:
        call action_nightbar_drink_alice_dress1 (char1) from _call_action_nightbar_drink_alice_dress1
        jump action_nightbar_drink_end
    elif char1.id == amy.id and char1.nightwear == 0:
        call action_nightbar_drink_amy_dress0 (char1) from _call_action_nightbar_drink_amy_dress0
        jump action_nightbar_drink_end
    elif char1.id == amy.id and char1.nightwear == 1:
        call action_nightbar_drink_amy_dress1 (char1) from _call_action_nightbar_drink_amy_dress1
        jump action_nightbar_drink_end
    elif char1.id == amy.id and char1.nightwear == 3:
        call action_nightbar_drink_amy_dress3 (char1) from _call_action_nightbar_drink_amy_dress3
        jump action_nightbar_drink_end
    elif char1.id == faye.id and char1.nightwear == 0:
        call action_nightbar_drink_faye_dress0 (char1) from _call_action_nightbar_drink_faye_dress0
        jump action_nightbar_drink_end
    elif char1.id == faye.id and char1.nightwear == 1:
        call action_nightbar_drink_faye_dress1 (char1) from _call_action_nightbar_drink_faye_dress1
        jump action_nightbar_drink_end
    elif char1.id == faye.id and char1.nightwear == 2:
        call action_nightbar_drink_faye_dress2 (char1) from _call_action_nightbar_drink_faye_dress2
        jump action_nightbar_drink_end
    elif char1.id == heather.id and char1.nightwear == 3:
        call action_nightbar_drink_heather_dress3 (char1) from _call_action_nightbar_drink_heather_dress3
        jump action_nightbar_drink_end
    elif char1.id == ivy.id and char1.nightwear == 0:
        call action_nightbar_drink_ivy_dress0 (char1) from _call_action_nightbar_drink_ivy_dress0
        jump action_nightbar_drink_end
    elif char1.id == ivy.id and char1.nightwear == 1:
        call action_nightbar_drink_ivy_dress1 (char1) from _call_action_nightbar_drink_ivy_dress1
        jump action_nightbar_drink_end
    elif char1.id == ivy.id and char1.nightwear == 2:
        call action_nightbar_drink_ivy_dress2 (char1) from _call_action_nightbar_drink_ivy_dress2
        jump action_nightbar_drink_end
    elif char1.id == lacey.id:
        call action_nightbar_drink_lacey (char1) from _call_action_nightbar_drink_lacey
        jump action_nightbar_drink_end
    elif char1.id == sara.id and char1.nightwear == 0:
        call action_nightbar_drink_sara_dress0 (char1) from _call_action_nightbar_drink_sara_dress0
        jump action_nightbar_drink_end
    elif char1.id == sara.id and char1.nightwear == 1:
        call action_nightbar_drink_sara_dress1 (char1) from _call_action_nightbar_drink_sara_dress1
        jump action_nightbar_drink_end
    elif char1.id == sara.id and char1.nightwear == 2:
        call action_nightbar_drink_sara_dress2 (char1) from _call_action_nightbar_drink_sara_dress2
        jump action_nightbar_drink_end
    elif char1.id == sara.id and char1.nightwear == 3:
        call action_nightbar_drink_sara_dress3 (char1) from _call_action_nightbar_drink_sara_dress3
        jump action_nightbar_drink_end
    elif char1.id == yvette.id and char1.nightwear == 1:
        call action_nightbar_drink_yvette_dress1 (char1, i_show_intro) from _call_action_nightbar_drink_yvette_dress1
        jump action_nightbar_drink_end
    elif char1.id == yvette.id and char1.nightwear == 2:
        call action_nightbar_drink_yvette_dress2 (char1, i_show_intro) from _call_action_nightbar_drink_yvette_dress2
        jump action_nightbar_drink_end

    if i_show_intro == True:
        pl "Great, let's head to the empty table over there."
        char1.talk "Sure, lead the way."

    $ start_scene()
    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
    if l_bartender.id == yumiko.id:
        show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
    with fade
    pause 1.0
    "After you've made yourselves comfortable at the table..."

    char1.talk "Why don't you tell me something about yourself?"
    pl "Sure, [char1.fname]."
    $ l_topic = "yourself"
    $ chat_content = g_chat.get_topic(l_topic, char1)
    pl "[chat_content.init]"
    $ l_answer = chat_content.get_answer(l_inclination)
    char1.talk "[l_answer]"
    $ player.change_lust(chat_content.get_lust_change(l_inclination))

    pl "Let me get you something to drink, before you tell me a story about yourself. *smiles*"
    pl "What would you like to have?"
    char1.talk "Nothing too big, I'm not that thirsty. Maybe a whiskey."
    "Interesting choice of drink for a girl. Good opportunity to get two of the same."
    pl "Great, I'll tell the bartender. I'll be back in no time."
    "You walk to the bar to get the drinks."
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 1.0
    if l_bartender.introduced == False:
        l_bartender.talk "Hello [l_bartender.playername]. What can I get you?"
        $ l_bartender.introduced = True
        if l_bartender.id == yumiko.id:
            l_bartender.talk "I'm [l_bartender.fname] by the way."
            l_bartender.talk "I work at the bar each Wednesday, Friday and Sunday."
        elif True:
            l_bartender.talk "I'm [l_bartender.fname] by the way."
            if gameday >= 12:
                l_bartender.talk "I work at the bar each night except Wednesdays, Fridays and Sundays."
            elif True:
                l_bartender.talk "I work at the bar each night."
        pl "Nice to meet you sexy [l_bartender.fname]. Please call me [player.fname]."
        $ l_bartender.playername = player.fname
        l_bartender.talk "Thank you for the compliment [l_bartender.playername]. *smiles*"
        if l_bartender.id == yumiko.id:
            "Wow, she's super hot.\nA really cute asian girl with a pretty face and an amazing body."
        elif True:
            "Wow, she's really hot.\nAnd very young, probably not much older than 18 years."
    elif True:
        l_bartender.talk "Hi [l_bartender.playername]. What can I get you?"
        $ l_bartender.playername = player.fname
    pause 0.4
    pl "I'll take two whiskies. One for me and one for [char1.fname]."
    l_bartender.talk "They'll be ready in a minute."
    l_bartender.talk "Do you want to take them with you or should I bring them to your table?"
    pl "I'll wait and take them with me."
    "More time to check her out without angering [char1.fname]."
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink2.webp") with dissolve:
        zoom 0.5
    pause 1.0
    if l_bartender.id == yumiko.id:
        "You watch her pouring the drinks,\nadmiring her voluptuous hips and legs during that time."
    elif True:
        "You watch her pouring the drinks,\nadmiring her sexy back and strong legs during that time."
    pause 1.0
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp") with dissolve:
        zoom 0.5
    pause 1.0
    jobs.bartender.talk "Here are your drinks."
    "You stare at her amazing cleavage for a moment..."
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp"):
        zoom 0.5
        ease 0.6 zoom 0.85 xpos -500 ypos -150
    pause 1.0
    "It almost looks like she is leaning forward a little more than necessary..."
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp"):
        zoom 0.85 xpos -500 ypos -150
        linear 0.4 zoom 0.5 xpos 0 ypos 0
    pause 1.0
    "You better take the drinks before it gets awkward."
    show expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
        zoom 0.5
    pause 0.6
    pl "Thank you [l_bartender.fname]."
    l_bartender.talk "Nothing to thank me for."
    l_bartender.talk "See you later [l_bartender.playername]."
    pause 0.3
    pl "Bye."

    if player.has_item("pink pill") == True or player.has_item("green pill") == True:
        if char1.get_action_allowed("pink pill") == False or char1.get_action_allowed("pink pill2x") == False or char1.get_action_allowed("green pill") == False or char1.get_action_allowed("purple tablet") == False:
            "You already spiked [char1.fname]'s drink today. You better wait until tomorrow before doing it again."
        elif True:
            menu:
                "Spike [char1.fname]'s drink with one {b}pink pill{/b} to lower her inhibitions" if player.has_item("pink pill"):
                    $ player.rem_item("pink pill")
                    $ pink_pill_used = True

                "Spike [char1.fname]'s drink with a double dose {b}pink pills{/b} to lower her inhibitions" if player.get_item_quantity("pink pill") >= 2:
                    $ player.rem_item("pink pill", 2)
                    $ pink_pill2x_used = True

                "Spike [char1.fname]'s drink with one {b}green pill{/b} to increase her lust" if player.has_item("green pill"):
                    $ player.rem_item("green pill")
                    $ green_pill_used = True

                "Spike [char1.fname]'s drink with one {b}purple tablet{/b} to lower her lust" if player.has_item("purple tablet"):
                    $ player.rem_item("purple tablet")
                    $ purple_tablet_used = True
                "Don't spike [char1.fname]'s drink" if True:

                    pass

    "You walk back to your table loaded with the two drinks."
    if l_bartender.id == yumiko.id:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
        show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
        with fade
    elif True:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
        with fade
    "You place the drinks on the table and sit down."
    show expression ("locations/loc_nightbar_drink1_whiskey.png") with dissolve
    pause 1.0
    pl "Here we go [char1.fname]. Your whiskey as ordered."
    char1.talk "Thank you [char1.playername]."
    $ char1.change_affection(10)
    pause 0.6
    if renpy.loadable("scenes/" + char1.fname + "/" + char1.fname + "_nightbar_drink1_sip_night" + unicode(char1.nightwear) + ".jpg"):
        show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_sip_night[char1.nightwear].jpg") with dissolve
        hide expression ("locations/loc_nightbar_drink1_whiskey.png")
        if l_bartender.id == yumiko.id:
            hide expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
        pause 1.0
    "You each take a sip from your drink..."
    $ player.add_effect("drunk")
    if pink_pill_used == True:
        $ char1.add_action_cooldown("pink pill", 48, "")
        "It's difficult to tell, but you think she's suddenly got a horny gleam in her eye."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif pink_pill2x_used == True:
        $ char1.add_action_cooldown("pink pill2x", 48, "")
        "She definitely looks more aroused."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif green_pill_used == True:
        $ char1.add_action_cooldown("green pill", 48, "")
        $ char1.change_lust(50)
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif purple_tablet_used == True:
        $ char1.add_action_cooldown("purple tablet", 48, "")
        $ char1.change_lust(-25)
        "You are not sure, but it seems to have a more controlled look on her face..."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif True:
        char1.talk "Oh wow, that's pretty good. *smiles*"

    if l_bartender.id == yumiko.id:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
        show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
        show expression ("locations/loc_nightbar_drink1_whiskey.png")
        with dissolve
    elif True:
        scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
        show expression ("locations/loc_nightbar_drink1_whiskey.png")
        with dissolve

    $ chat_content = g_chat.get_topic(char1.get_topic("herself"), char1)
    pl "[chat_content.init]"
    $ l_answer = chat_content.get_answer(l_inclination)
    char1.talk "[l_answer]"
    $ player.change_lust(chat_content.get_lust_change(l_inclination))
    pause 1.0
    "After chatting with her for some time..."
    if char1.id == yvette.id and renpy.random.randint(1,100) <= 50 and player.get_quest_state("Lingerie_presents1_Yvette", char1) == -1 and char1.check_affection(3,0,False) == True:
        char1.talk "Do you like what I'm wearing, [char1.playername]?"
        pl "Yeah, sure - it's lovely."
        pl "Why do you ask?"
        pause 0.4
        char1.talk "I was just thinking about an underwear set I have seen..."
        char1.talk "Too bad I can't get it now. I'm sure you'd like it. *smiles*"
        pause 0.4
        pl "What is it?"
        char1.talk "Oh... I don't want to spoil the surprise, just in case I can still get it somehow. *smiles*"
        pl "Good point. *grinning*"
        $ player.add_quest("Lingerie_presents1_Yvette", char1, char1)

    if char1.check_tease_sexual(2, 0, False) == False:
        char1.talk "It was a really nice evening. Thank you [char1.playername]."
        pl "The pleasure was all mine."
        char1.talk "We absolutely have to do that again, but I'm a little tired now."
        pl "Anytime. Have a good night [char1.fname]."
        char1.talk "You too [char1.playername]."
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        $ char1.locations[actions_left-2] = char1.fname + "_room"
        $ char1.locations[actions_left-3] = char1.fname + "_room"
        jump action_nightbar_drink_end

    scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink2_night[char1.nightwear].jpg") with dissolve
    pause 1.0
    "[char1.fname] puts her hand on your leg affectionately and looks you deep in the eye."
    char1.talk "Have I told you that I really like you [char1.playername]?"
    "Oh wow, this is really hot. You wonder where this is going..."
    $ char1.add_pl_interaction("tease_talk")
    $ char1.add_pl_interaction("tease_touch")
    $ player.change_lust(char1.sexiness+2)
    menu:
        "Compliment her" if True:
            if player.check_charm(3) == False:
                pl "No you haven't. I have to say I feel the same for you."
                char1.talk "That's nice of you to say."
                $ char1.change_affection(5)
                "You chat for another 30 minutes with her hand on your thighs...\nwhich really turns you on."
                $ player.change_lust(char1.sexiness + 4)
                call actions_used (1) from _call_actions_used
                pause 1.0
                char1.talk "It was an amazing evening. Thank you [char1.playername]."
                pl "The pleasure was all mine."
                char1.talk "We absolutely have to do that again, but I'm a little tired now."
                pl "Anytime. Have a good night [char1.fname]."
                char1.talk "You too [char1.playername]."
                $ char1.locations[actions_left-1] = char1.fname + "_room"
                $ char1.locations[actions_left-2] = char1.fname + "_room"
                $ char1.locations[actions_left-3] = char1.fname + "_room"
                jump action_nightbar_drink_end

            pl "You know [char1.fname], I fell for you the moment I first saw you on the island."
            if char1.id == eva.id:
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
                pause 1.0
            char1.talk "Ohh, really. {b}Wow.{/b} With all these amazing girls around here..."
            pl "They're nothing like you..."
            call change_char_max_affection (char1, 5) from _call_change_char_max_affection
            $ char1.change_affection(5)
            call change_char_max_love (char1, 5) from _call_change_char_max_love
            $ char1.change_love(5)
            char1.talk "You really know how to flatter a lady. *smiles*"
            if char1.id == renee.id or (char1.id == faye.id and char1.nightwear == 2):
                $ l_lust_check = char1.check_lust(3, False)
            if char1.id == natasha.id and char1.nightwear == 2:
                show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "With her hand on your thighs, you can't help noticing that her bra is slowly losing the battle against her incredible knocker..."
                "...you just cannot help it but stare at her immense cleavage for a moment!"
                show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink4_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "The moment lingers into more than a full second by now!"
                char1.talk "Hey [char1.playername]!"
                char1.talk "Having breasts like mine I forgive you... *smiles*"
                pl "Uhmm sorry [char1.fname], but your ni..."
                char1.talk "If you want to see them a little better, why don't you just say so?"
                show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink5_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                pl "{b}Wow! Oh my God!{/b} They are so round and firm!"
                pl "Oops! Did I really just say that?"
                char1.talk "Thank you! I'll take that as a compliment."
                pl "Uhmm about your bra top..."
                char1.talk "Yes?"
                show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink6_night[char1.nightwear].jpg") with dissolve
                pause 0.7
                pl "It looks like your bra has shrunk a bit or something..."
                char1.talk "It's not the bra... *smirks*"
                $ player.change_lust(10)
                scene onlayer master
                show expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
                pause 0.7
                "To change the subject you ask her."
                pl "Uhmmm..."

            elif char1.id == faye.id and char1.nightwear == 2 and l_lust_check == True:
                $ char1.add_pl_interaction("tease_talk")
                $ char1.add_pl_interaction("tease_boobs")
                $ char1.add_pl_interaction("tease_touch")
                $ char1.add_pl_interaction("tease_pussy")
                $ char1.add_scene_seen("Nightbar_ladies_room")
                "With her hand on your thighs, your eyes wander towards the valley between her incredible knockers..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Damn! They're so round and firm but soft looking at the same time!"
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink4_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Oh my God! She must have noticed you staring!"
                "You quickly look up at her face..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink5_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                char1.talk "Do you like the biggest breasts the island has to offer?"
                pause 0.3
                pl "Ummm... What?"
                char1.talk "I'm not mad or anything."
                char1.talk "I guess it's impossible not to stare at my breasts... *giggles*"
                pause 0.4
                pl "*blushing* Ummm... Yes, they are incredible... amazing..."
                char1.talk "Thank you. *smiles*"
                pause 0.3
                "Trying to steer the conversation away from her tits..."
                pl "Er... would you like to have another drink?"
                pause 0.4
                char1.talk "Maybe... But I need to go to the ladies room first."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink6_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                char1.talk "I won't be long."
                pause 0.3
                pl "I'm not going anywhere. *smiling*"
                "[char1.fname] vanishes into the ladies room."
                scene expression ("locations/loc_nightbar_main.webp") with fade:
                    zoom 0.5
                pause 1.0
                "After a short while, your phone vibrates."
                "Since you're still waiting for [char1.fname], you take it out to check."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink7_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Strange... It's a message from [char1.fname]..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink8_night[char1.nightwear].jpg")
                show expression ("phone/phone_[char1.fname][char1.phone_image]_hover.png"):
                    xpos 600 ypos 100 zoom 0.70
                with dissolve
                pause 0.2
                "...okay, let's read it."
                pause 1.0
                pl "Damn! wow!"
                pause 0.3
                "A little bit nervous, you click on the icon to display the attached image..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink9_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Did she just go topless in the ladies room???"
                $ player.change_lust(char1.sexiness + 4)
                "Before you have time to think about the implications, your phone vibrates again."
                "Another message..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink10_night[char1.nightwear].jpg")
                show expression ("phone/phone_[char1.fname][char1.phone_image]_hover.png"):
                    xpos 600 ypos 100 zoom 0.70
                with dissolve
                pause 0.2
                "...again from [char1.fname]. Your eyes quickly fly over its content."
                pause 0.7
                "Hmmm... What do you wear under a thong???"
                pause 0.3
                "You click on the attached image to display it."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink11_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                pl "*Mmmmppfff* Shit!"
                "It's a bit dark down there, but that's definitely [char1.fname]'s exposed pussy!"
                "And a huge amount of underboobs..."
                $ player.change_lust(char1.sexiness + 6)
                "Before someone else sees it, you quickly turn off your phone..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink7_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "...and put it back in your pocket."
                scene expression ("locations/loc_nightbar_main.webp") with fade:
                    zoom 0.5
                pause 1.0
                "While you're still thinking about the pictures she just send you, [char1.fname] is already coming back from the ladies room."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink6_night[char1.nightwear].jpg") with fade
                pause 1.0
                char1.talk "Hi! I told you I'd be quick."
                char1.talk "Did anything interesting happen while I was gone? *smiles*"
                "You decide to play along..."
                pause 0.3
                pl "Ummm... Just the usual you know..."
                "Before answering, she sits down in her chair thrusting out her huge tits once again..."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink4_night[char1.nightwear].jpg") with fade
                pause 1.0
                char1.talk "So... Just the usual..."
                "Then she leans forward and puts her hand on your thigh."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink2_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Squeezing for a moment... Before she leans forward even further."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink12_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                "Grabbing your belt, pulling down your trousers a bit and stroking your dick with her thumb."
                char1.talk "So... Just the usual {b}M cup tits{/b} all naked in the ladies room... *smirks*"
                $ player.change_lust(char1.sexiness + 4)
                $ player.add_effect("erection")
                "Still slightly stroking your dick..."
                char1.talk "Yes! That's what I was looking for! *smirks*"
                char1.talk "Let's go upstairs where we have some more privacy."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink5_night[char1.nightwear].jpg") with dissolve
                pause 1.0
                char1.talk "Well if you want to I mean... *smiles*"
                pause 0.3
                pl "Ummm... Wow! I... Yes!"
                char1.talk "I'll move my body around that hard metal pole up there and strip for you until your pole is every bit as hard."
                pause 0.3
                "With your dick almost ready to escape from your pants..."
                pl "Let's go!"
                char1.talk "Do you know where the blue room is?"
                pause 0.3
                pl "Hmmm... I'm not sure..."
                char1.talk "Okay, follow me. I'll lead the way."
                call nightbar_blue_room_faye (char1) from _call_nightbar_blue_room_faye
                jump action_nightbar_drink_end

            elif char1.id == jessica.id and char1.nightwear == 2:
                call nightbar_drink_jessica (char1) from _call_nightbar_drink_jessica
                if _return == "masturbate":
                    $ l_masturbate = True
                jump action_nightbar_drink_end
            elif char1.id == renee.id and l_lust_check:
                call nightbar_drink_renee_footjob (char1) from _call_nightbar_drink_renee_footjob
                return "goto_player_room"
            elif True:
                "You chat for another 30 minutes with her hand on your thighs...\nwhich really turns you on."
                $ player.change_lust(char1.sexiness + 4)
                call actions_used (1) from _call_actions_used_1
                pause 1.0

            pl "Would you like another drink [char1.fname]?"
            

            char1.talk "I think I've had enough. *smiles*"
            char1.talk "The evening was incredible. Thank you so much [char1.playername]."
            pl "The pleasure was all mine."
            char1.talk "We absolutely have to do that again, but I'm a little tired now."
            pl "Anytime. Have a good night [char1.fname]."
            
            "Before she leaves, [char1.fname] pulls you close for a kiss."
            scene expression ("locations/loc_nightbar_main.webp") with dissolve:
                zoom 0.5
            call action_kiss_mouth (char1, location, True, 0) from _call_action_kiss_mouth_1
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg") with dissolve
            if l_bartender.id == yumiko.id:
                show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
            "Wow, that was intense..."
            char1.talk "You have a good night too [char1.playername]."
            $ char1.locations[actions_left-1] = char1.fname + "_room"
            $ char1.locations[actions_left-2] = char1.fname + "_room"
            $ char1.locations[actions_left-3] = char1.fname + "_room"
            "[char1.fname] leaves the nightbar."
            jump action_nightbar_drink_end
        "Just enjoy the moment and don't say anything" if True:

            pause 1.0
            scene onlayer master
            if char1.id == natasha.id or char1.id == lacey.id or char1.id == renee.id or char1.id == eva.id:
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
            elif True:
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
                if l_bartender.id == yumiko.id:
                    show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
                with dissolve
            pause 1.0
            char1.talk "You're not going to say something?"
            pl "Uhmmm..."
            $ char1.change_anger(10)
            $ char1.change_affection(-10)
            char1.talk "It was a nice evening so far, but you kinda spoiled it."
            pause 0.4
            char1.talk "Also I'm a little tired now."
            pl "Ohh, so soon?"
            char1.talk "Yes sorry... Have a good night [char1.playername]."
            pl "You too [char1.fname]!"
            "It seems she is a little angry with you. Maybe next time you get a compliment, you better return it!"
            $ char1.locations[actions_left-1] = char1.fname + "_room"
            $ char1.locations[actions_left-2] = char1.fname + "_room"
            $ char1.locations[actions_left-3] = char1.fname + "_room"
            jump action_nightbar_drink_end

        "Talk with her about the photo session" if player.get_quest_state("Eva_photo_studio", char1) >= 0 and player.has_appointment(25,char1) == False and char1.get_action_allowed("Eva_photo_studio") == True:
            $ char1.add_action_cooldown("Eva_photo_studio", 48, "")
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
            pause 0.7
            if player.get_quest_state("Eva_photo_studio", char1) == 0:
                pl "There's something I'd like to talk with you about."
                char1.talk "Okay, that sounds mysterious. *smiles*"
                pause 0.5
                pl "Not really. Joy told me that you'd like to do a photo session at the new studio."
                char1.talk "Oh yes, the photo studio!"
                pause 0.4
                pl "So would you like to do a photo session at the studio with me as your photographer?"

            elif player.get_quest_state("Eva_photo_studio", char1) == 1:
                pl "About that photo shoot at the new studio."
                char1.talk "So you want to know if I'm ready to go with you?"
                pl "Yes. *smiling*"

            elif player.get_quest_state("Eva_photo_studio", char1) == 2:
                pl "Ummm... About that photo shoot..."
                pl "I'm so sorry I missed our appointment last time."
                pl "Would you give me another chance?"
            elif True:

                pl "I loved the photo shoot we did some time ago."
                pl "Would you like to do it again?"

            if char1.check_affection(2,0,False) == False:
                char1.talk "Ummm... I don't really know. I mean I'd love to do that photo session..."
                char1.talk "But I thought Jennifer..."
                pl "Oh..."
                pause 0.5
                char1.talk "You know what, I think when we know each other a little better, it would be fun."
                char1.talk "I want to try the most kinky lingerie I can find. *smirks*"
                pl "*gulp* Okay."
                if player.get_quest_state("Eva_photo_studio", char1) < 100:
                    $ player.set_quest_state("Eva_photo_studio", char1, 1, True)
                pause 0.5
                char1.talk "Right now, I'm a little tired."
                char1.talk "Yes sorry... I really need to get some sleep. Have a good night, [char1.playername]."
                char1.talk "You have a good night too [char1.playername]."
                "[char1.fname] leaves the nightbar."
                $ char1.locations[actions_left-1] = char1.fname + "_room"
                $ char1.locations[actions_left-2] = char1.fname + "_room"
                $ char1.locations[actions_left-3] = char1.fname + "_room"
                jump action_nightbar_drink_end

            char1.talk "What do you think?"
            char1.talk "I'd love to! We're going to have so much fun!"
            pl "I have no doubt that I'm going to enjoy it. *smiling*"
            pl "How about tomorrow evening after dinner?"
            char1.talk "I don't know where the photo studio is. Can you pick me up at me room?"
            pl "Sure, what time do you have in mind?"
            char1.talk "How about 10 pm?"
            pl "Yes, that works fine."
            $ player.add_appointment(25, char1, "Eva_room", 18, True)
            if player.get_quest_state("Eva_photo_studio", char1) < 100:
                $ player.set_quest_state("Eva_photo_studio", char1, 2, True)

            char1.talk "Thank you for the nice evening, [char1.playername]."
            pl "The pleasure was all mine."
            char1.talk "We absolutely have to do that again, but I'm a little tired now."
            pl "Anytime. Have a good night [char1.fname]."
            "Before she leaves, [char1.fname] pulls you close for a hug."
            scene expression ("locations/loc_nightbar_main.webp") with dissolve:
                zoom 0.5
            call action_hug (char1, location, True, 0) from _call_action_hug_6
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
            if l_bartender.id == yumiko.id:
                show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
            with dissolve
            "Wow, that was nice..."
            char1.talk "You have a good night too [char1.playername]."
            $ char1.locations[actions_left-1] = char1.fname + "_room"
            $ char1.locations[actions_left-2] = char1.fname + "_room"
            $ char1.locations[actions_left-3] = char1.fname + "_room"
            "[char1.fname] leaves the nightbar."
            jump action_nightbar_drink_end

    label action_nightbar_drink_ladies_room:
        char1.talk "Hmmm, I could use something hard and strong now."
        "She squeezes your thigh with her hand while saying that..."
        if char1.id == natasha.id:
            char1.talk "If you'll excuse me, I need to fix my bra. *giggles*"
            char1.talk "I'll be quick!"
            pl "Sure, I'm not going anywhere, take your time."
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink7_night[char1.nightwear].jpg") with dissolve
        elif True:
            char1.talk "If you'll excuse me, I need to go to the ladies room for a moment."
            pl "Sure, I'm not going anywhere, take your time."
            scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink3_night[char1.nightwear].jpg") with dissolve
        pause 1.0
        "Having taken some steps, [char1.fname] looks over her shoulder and gives you one of those looks that can melt icebergs...."
        pause 1.0
        "After that she vanishes into the ladies rooms."
        scene expression ("locations/loc_nightbar_main.webp") with dissolve:
            zoom 0.5
        pause 1.0
        "Five minutes can be a long time when you are waiting for a hot girl like [char1.fname]... She isn't back yet."
        pause 1.0
        "After almost 10 minutes [char1.fname] still isn't back...\nWhat do you want to do?"
        menu:
            "Wait a bit longer" if True:
                pause 1.0
                "After about 15 minutes, [char1.fname] is finally back."
                scene expression ("scenes/[char1.fname]/[char1.fname]_nightbar_drink1_night[char1.nightwear].jpg")
                if l_bartender.id == yumiko.id:
                    show expression ("scenes/Yumiko/Yumiko_nightbar_overlay1.png")
                with dissolve
                pause 1.0
                pl "Here you are [char1.fname]. Is everything okay?"
                char1.talk "I don't know. I'm not feeling that well. Must be the alcohol..."
                $ char1.change_love(-10)
                $ char1.change_lust(-30)
                $ char1.change_anger(10)
                char1.talk "I think I've had enough for today, I'm really tired now."
                pl "Okay, sorry for that [char1.fname]. Have a good night."
                "Hmmm you wonder what made her angry with you."
                char1.talk "You too, [char1.playername]."
                scene expression "locations/loc_nightbar_main.webp" with fade:
                    zoom 0.5
                pause 0.5
                $ char1.locations[actions_left-1] = char1.fname + "_room"
                $ char1.locations[actions_left-2] = char1.fname + "_room"
                $ char1.locations[actions_left-3] = char1.fname + "_room"
                "[char1.fname] has left the nightbar."
                jump action_nightbar_drink_end


            "Check on her in the ladies room" if char1.id == natasha.id:
                call nightbar_ladies_room_natasha (char1) from _call_nightbar_ladies_room_natasha

    label action_nightbar_drink_end:
    call actions_used (1) from _call_actions_used_35
    if player.get_quest_state("Intro_plane_girl", char1) == 6:
        $ player.inc_quest_state("Intro_plane_girl", char1, True)
    if char1.id <> sara.id and char1.id <> lacey.id and char1.id <> ivy.id:
        $ char1.add_scene_seen("Nightbar_drink")
    $ char1.add_action_cooldown("nightbar_drink", 35, "I already had a drink with you today. Ask me again tomorrow.")
    if l_masturbate == True:
        $ location = "player_room"
        "After that evening with [char1.fname], all you can think of now is getting some relief."
        if char1.id <> ivy.id:
            "You head back to your room to help yourself."
        call pl_action_masturbate ("player_room", 0, char1, i_girl_image=l_masturbate_to) from _call_pl_action_masturbate_6
        $ menu_active = False
        $ selected_char = no_char
        $ stop_scene()
        return "goto_player_room"
    elif True:
        $ menu_active = False
        $ selected_char = no_char
        call create_list_of_chars_display () from _call_create_list_of_chars_display_6
        $ stop_scene()
        return "nothing"





label action_nightbar_get_drinks(i_use_overlay=True, i_use_new_logic=False):
    $ pink_pill_used = False
    $ pink_pill2x_used = False
    $ green_pill_used = False
    $ purple_tablet_used = False
    $ l_call = False
    $ l_use_intermediate_logic = False
    $ l_random = renpy.random.randint(1,3)
    if l_random == 1:
        pl "I'll fetch our drinks from the bar."
    elif l_random == 2:
        pl "I'll get us the drinks from the bar."
    elif True:
        pl "I can head to the bar and pick up the drinks."
        char1.talk "That'd be nice."
    pause 0.4
    char1.talk "Thank you. *smiles*"
    pause 0.4
    pl "I'll be right back."
    pause 0.4
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 1.0
    if l_bartender.introduced == False:
        l_bartender.talk "Hello [l_bartender.playername]. What can I get you?"
        $ l_bartender.introduced = True
        if l_bartender.id == yumiko.id:
            l_bartender.talk "I'm [l_bartender.fname] by the way."
            l_bartender.talk "I work at the bar each Wednesday, Friday and Sunday."
        elif True:
            l_bartender.talk "I'm [l_bartender.fname] by the way."
            if gameday >= 12:
                l_bartender.talk "I work at the bar each night except Wednesdays, Fridays and Sundays."
            elif True:
                l_bartender.talk "I work at the bar each night."
        pl "Nice to meet you sexy [l_bartender.fname]. Please call me [player.fname]."
        $ l_bartender.playername = player.fname
        l_bartender.talk "Thank you for the compliment [l_bartender.playername]. *smiles*"
        if l_bartender.id == yumiko.id:
            "Wow, she's super hot.\nA really cute Asian girl with a pretty face and an amazing body."
        elif True:
            "Wow, she's really hot.\nAnd very young, probably not much older than 18 years."
    elif True:
        $ l_random = renpy.random.randint(1,3)
        if l_random == 1:
            l_bartender.talk "Hi [l_bartender.playername]. What can I get you?"
            pl "Hello [l_bartender.fname]."
        elif l_random == 2:
            l_bartender.talk "Hey! Looks like someone is thirsty. *smiles*"
            l_bartender.talk "What would you like to have?"
            pl "Hi [l_bartender.fname]."
        elif True:
            pl "Hey [l_bartender.fname]."
            l_bartender.talk "Hello [l_bartender.playername]."
            l_bartender.talk "I guess you want to order some drinks?"
            pl "You guessed right."
        $ l_bartender.playername = player.fname
        $ l_random = renpy.random.randint(1,2)
        if l_random == 1:
            pause 0.4
            pl "You look especially gorgeous tonight. *smiling*"
            char1.talk "Thank you."
            $ l_bartender.change_affection(5)
            if l_bartender.fname == jennifer.fname:
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink7.webp") with dissolve:
                    zoom 0.5
            elif True:
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink5.webp") with dissolve:
                    zoom 0.5
                pause 0.7
            l_bartender.talk "You shouldn't let [char1.fname] hear this. *whispers*"
            pl "You're right. *whispering*"
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
                zoom 0.5
            pause 0.7
            l_bartender.talk "What can I get you?"

    pl "I'd like two whiskeys. One for me and one for my lovely companion, [char1.fname]."
    l_bartender.talk "They'll be ready in a minute."
    l_bartender.talk "Do you want to take them with you or should I bring them to your table?"
    pl "I'll take them with me, no problem."
    l_bartender.talk "Sure. *smiles*"
    $ l_random = renpy.random.randint(1,100)
    if l_random <= 25:
        "Waiting for the drinks will give you more time to check her out without angering [char1.fname]."
        scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink2.webp") with dissolve:
            zoom 0.5
        pause 0.7
        if l_bartender.id == yumiko.id:
            "You watch her pouring the drinks,\nadmiring her voluptuous hips and legs during that time."
        elif True:
            "You watch her pouring the drinks,\nadmiring her sexy back and strong legs during that time."
        scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink2.webp") with dissolve:
            subpixel True zoom 0.8 align (0.5,0.8)
        pause 0.7
        "Yes, really lovely!"
        scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp") with dissolve:
            zoom 0.5
        pause 0.7
    elif True:
        scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink2.webp") with dissolve:
            zoom 0.5
        pause 0.7
        "[l_bartender.fname] makes good on her promise and is back with the filled glasses in less than a minute..."
        pause 0.5
        scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp") with dissolve:
            zoom 0.5
        pause 0.7

    jobs.bartender.talk "Here are your drinks."
    play sound "sounds/ice_cube_glass2.mp3"
    "That's a nice view!"
    menu:
        "Stare at her cleavage" if True:
            "You stare at her amazing cleavage for a moment..."
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp"):
                subpixel True zoom 0.5 align (0.5,0.5)
                ease 1.6 zoom 0.85
            $ renpy.pause(2.0,hard=True)
            "It almost looks like she leans forward a little more than necessary..."
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink3.webp"):
                subpixel True zoom 0.85 align (0.5,0.5)
                ease 1.4 zoom 0.5
            $ renpy.pause(1.6,hard=True)
            $ player.change_lust(l_bartender.sexiness-2, i_check_erection=False)
            pause 0.4
            "You better take the drinks before it gets awkward."
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
                zoom 0.5
            pause 0.6
            pl "Many thanks [l_bartender.fname]."
            if l_bartender.fname == jennifer.fname and l_bartender.check_tease_sexual(3,0,False) == True:
                l_bartender.talk "It was my pleasure. *smirks*"
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink6.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                l_bartender.talk "Just come back any time you want more. *grins*"
                pl "Thanks. I think these will last for some time."
                l_bartender.talk "I wasn't talking about the drinks..."
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink9.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                $ player.change_lust(l_bartender.sexiness-2, i_check_erection=False)
                pl "*gulp*"
                pause 0.4
                l_bartender.talk "Did you really think I wouldn't notice you staring at my boobs? *smirks*"
                pause 0.4
                $ l_call = True
                char1.talk "{b}[char1.playername]? Are you coming?{/b}"
                pause 0.3
                pl "I should better go back."
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                l_bartender.talk "Of course, enjoy the drinks. *winks*"
                l_bartender.talk "And give [char1.fname] my regards."
                pl "Thanks and will do."
                pl "See you later, [l_bartender.fname]."
                l_bartender.talk "Bye [l_bartender.playername]."
            elif True:

                l_bartender.talk "Just doing my job."
                l_bartender.talk "Enjoy the drinks."
                pl "Thanks. See you later, [l_bartender.fname]."
                l_bartender.talk "Bye [l_bartender.playername]."
        "Just take the drinks" if True:

            pl "Thank you [l_bartender.fname]."
            l_bartender.talk "Nothing to thank me for."
            l_bartender.talk "See you later, [l_bartender.playername]."
            pause 0.3
            pl "Bye."

    if player.has_item("pink pill") == True or player.has_item("green pill") == True or player.has_item("purple tablet") == True:
        if char1.get_action_allowed("pink pill") == False or char1.get_action_allowed("pink pill2x") == False or char1.get_action_allowed("green pill") == False or char1.get_action_allowed("purple tablet") == False:
            "You already spiked [char1.fname]'s drink today. You better wait until tomorrow before doing it again."
        elif True:
            menu:
                "Spike [char1.fname]'s drink with one {b}pink pill{/b} to lower her inhibitions" if player.has_item("pink pill"):
                    $ player.rem_item("pink pill")
                    $ pink_pill_used = True

                "Spike [char1.fname]'s drink with a double dose {b}pink pills{/b} to lower her inhibitions" if player.get_item_quantity("pink pill") >= 2:
                    $ player.rem_item("pink pill", 2)
                    $ pink_pill2x_used = True

                "Spike [char1.fname]'s drink with one {b}green pill{/b} to increase her lust" if player.has_item("green pill"):
                    $ player.rem_item("green pill")
                    $ green_pill_used = True

                "Spike [char1.fname]'s drink with one {b}purple tablet{/b} to lower her lust" if player.has_item("purple tablet"):
                    $ player.rem_item("purple tablet")
                    $ purple_tablet_used = True
                "Don't spike [char1.fname]'s drink" if True:

                    pass

    "You walk back to your table loaded with the two drinks."
    if i_use_new_logic == True:
        if renpy.loadable("scenes/" + char1.fname + "/nightbar/night" + unicode(char1.nightwear) + "/" + char1.fname + "_nightbar_drink2.webp"):
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink2.webp"):
                zoom 0.5
            with fade
        elif True:
            $ l_use_intermediate_logic = True
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink1_[l_bartender.fname].webp"):
                zoom 0.5
            with fade
    elif True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink1_night[char1.nightwear]_[l_bartender.fname].webp"):
            zoom 0.5
        with fade
    pause 0.7
    if l_call == False:
        char1.talk "That was pretty fast."
        pl "Yes, [l_bartender.fname] really knows her way around the bar. *smiling*"
    elif True:
        char1.talk "And I thought you prefer the bartender's company..."
        pl "Oh... I was just saying {i}Hi{/i} and getting the drinks."
        pl "And by the way, [l_bartender.fname] sends regards. *smiling*"
        char1.talk "Thanks."
    pause 0.4
    pl "Here's your drink."
    play sound "sounds/ice_cube_glass2.mp3"
    if l_use_intermediate_logic == True:
        scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink2_[l_bartender.fname].webp") with dissolve:
            zoom 0.5
    elif i_use_new_logic == True:
        scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink3.webp") with dissolve:
            zoom 0.5
    elif i_use_overlay == True:
        show expression ("locations/loc_nightbar_drink1_whiskey.webp") with dissolve:
            zoom 0.5
    elif True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink2_night[char1.nightwear]_[l_bartender.fname].webp") with dissolve:
            zoom 0.5
    pause 0.8
    char1.talk "Thank you, [char1.playername]."
    $ char1.change_affection(5)
    pause 0.6
    if l_use_intermediate_logic == True:
        "After having placed the two drinks on the table, you sit down."
        char1.talk "Cheers!"
        pl "Cheers!"
        scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink3.webp") with dissolve:
            zoom 0.5
        pause 0.4
        "You both take a sip from your drink..."
    elif i_use_new_logic == True:
        "After having placed the two drinks on the table, you sit down..."
        if renpy.loadable("scenes/" + char1.fname + "/nightbar/night" + unicode(char1.nightwear) + "/" + char1.fname + "_nightbar_drink4_" + l_bartender.fname + ".webp"):
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink4_[l_bartender.fname].webp") with dissolve:
                zoom 0.5
        elif True:
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink4.webp") with dissolve:
                zoom 0.5
        pause 0.6
        "...and take a sip from your drink."
    elif True:
        "You both take a sip from your drink..."
    play sound "sounds/ice_cube_glass2.mp3"
    if l_use_intermediate_logic == True:
        scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink4.webp") with dissolve:
            zoom 0.5
    elif i_use_new_logic == True:
        if renpy.loadable("scenes/" + char1.fname + "/nightbar/night" + unicode(char1.nightwear) + "/" + char1.fname + "_nightbar_drink5_" + l_bartender.fname + ".webp"):
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink5_[l_bartender.fname].webp") with dissolve:
                zoom 0.5
        elif True:
            scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_drink5.webp") with dissolve:
                zoom 0.5
    elif i_use_overlay == True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink2_night[char1.nightwear]_[l_bartender.fname].webp") with dissolve:
            zoom 0.5
    elif True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink3_night[char1.nightwear]_[l_bartender.fname].webp") with dissolve:
            zoom 0.5
    pause 0.7
    $ player.add_effect("drunk")
    if pink_pill_used == True:
        $ char1.add_action_cooldown("pink pill", 48, "")
        "It's difficult to tell, but you think she's suddenly got a horny gleam in her eye."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif pink_pill2x_used == True:
        $ char1.add_action_cooldown("pink pill2x", 48, "")
        "She definitely looks more aroused."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif green_pill_used == True:
        $ char1.add_action_cooldown("green pill", 48, "")
        $ char1.change_lust(50)
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif purple_tablet_used == True:
        $ char1.add_action_cooldown("purple tablet", 48, "")
        $ char1.change_lust(-25)
        "You are not sure, but it seems to have a more controlled look on her face..."
        char1.talk "Oh wow, that stuff is really going straight to my head... *smiles*"
    elif True:
        char1.talk "Oh wow, that's pretty good. *smiles*"

    if i_use_new_logic == True:
        pass
    elif i_use_overlay == True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink1_night[char1.nightwear]_[l_bartender.fname].webp"):
            zoom 0.5
        show expression ("locations/loc_nightbar_drink1_whiskey.webp"):
            zoom 0.5
        with dissolve
    elif True:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_drink2_night[char1.nightwear]_[l_bartender.fname].webp") with dissolve:
            zoom 0.5
    pause 0.8
    return "nothing"





label nightbar_security_chat(char1):
    $ location_detail = ""
    $ player.smart_watch_character = char1
    $ menu_active = True
    $ l_left_menu_hidden = g_left_menu_hidden
    $ g_left_menu_hidden = True
    $ player.add_action_cooldown("nightbar_security_chat", 24)
    $ start_scene()

    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat1.webp") with fade:
        zoom 0.223
    pause 0.7
    "You look to your right where the security guard is standing watch."
    if char1.id == mercedes.id:
        "Red hair... {w}So it's Mercedes on duty today."
    "She does look relaxed and friendly enough."
    "So you decide to stand up and walk towards her..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat1.webp"):
        subpixel True zoom 0.223
        ease 4.0 zoom 0.85 xpos -2000 ypos -550
    $ renpy.pause (4.3, hard=True)
    pl "Hey [char1.fname]!"
    char1.talk "Hello [char1.playername]."
    char1.talk "How are you doing? {w}I hope everything is all right."
    pause 0.5
    pl "Thanks for asking, I'm fine."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
        zoom 0.5
    pause 0.6
    char1.talk "Do you have any security related issues to discuss?"
    pl "Oh... {w}No, I just came by to say {b}Hi{/b}."
    char1.talk "That's nice."
    if len(list_of_chars_display_3) >= 3:
        $ char1.change_affection(3)
        char1.talk "Although it's pretty placid here, the bar is really packed right now."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
            zoom 0.8 xpos -500
        pause 0.6
        char1.talk "It's not a good time to chat."
        char1.talk "It's my job to pay attention and make sure everyone is save and everything stays calm."
        pause 0.4
        pl "Sure, I understand."
        pl "Maybe we can talk some other time."
        char1.talk "That'd be great. {w}I'd love to chat with you when the bar is not so busy."
        pause 0.5
        pl "See you later [char1.fname]."
        char1.talk "Bye [char1.playername]!"
        scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
            zoom 0.667
        pause 0.5
        "You head back to the bar."
        jump nightbar_security_talk_end

    $ char1.add_scene_seen("Nightbar_security_chat")
    $ char1.change_affection(5)
    char1.talk "Since the bar isn't that busy tonight, we can chat and I can still do my job. *smiles*"
    char1.talk "Anything in particular you'd like to talk about?"
    $ l_option1 = True
    $ l_option2 = True
    $ l_option3 = True
    $ l_option4 = True
    $ l_option5 = True
    $ l_option6 = True
    $ l_talked = 0
    label nightbar_security_chat_menu:
    if l_talked >= 2:
        $ char2 = no_char
        if eva in list_of_chars_display_3:
            $ char2 = eva
        elif faye in list_of_chars_display_3:
            $ char2 = faye
        elif desire in list_of_chars_display_3:
            $ char2 = desire

        if char2.id == no_char.id:
            char1.talk "I think it's time I check the bar again to make sure there are no incidents."
            pause 0.4
            pl "Sure, I don't want to keep you from doing your work."
            char1.talk "It was a nice distraction. I really enjoyed talking to you."
            pl "Me too. {w}See you later [char1.fname]."
            char1.talk "Bye [char1.playername]!"
            scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
                zoom 0.667
            pause 0.5
            "You walk back to the bar."
            jump nightbar_security_talk_end
        elif True:
            char2.talk "{b}Hey [char1.fname]!{/b}"
            "Oh... That sounds like trouble..."
            char2.talk "Stop intimidating our poor [char2.playername] with your push-up bra enhanced chest."
            char2.talk "Let him come back to the bar, I'm bored!"
            menu:
                "Ignore the rude comment and keep talking with [char1.fname]" if True:
                    pl "Don't listen to her [char1.fname]."
                    pl "You're not intimidating me. {w}I really enjoy talking to you."
                "Defend [char1.fname]" if True:

                    pl "Hey [char2.fname]! That was really rude you know."
                    pl "Why did you insult [char1.fname]?"
                    $ char2.change_anger(6)
                    char2.talk "Just forget I said anything, okay."
                "Head back to the bar" if True:

                    pl "I better get back to the others."
                    pl "Sorry [char1.fname]."
                    $ char1.change_affection(-6)
                    char1.talk "Okay, if you have to..."
                    pl "See you later [char1.fname]."
                    char1.talk "Bye."
                    "You head back to the bar."
                    scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
                        zoom 0.667
                    pause 0.5
                    jump nightbar_security_talk_end

            call actions_used (1) from _call_actions_used_184
            $ char1.add_pl_interaction("tease_boobs")
            $ char1.add_pl_interaction("tease_talk")
            char1.talk "Thank you [char1.playername]."
            char1.talk "And I'm not wearing a push-up bra..."
            pause 0.5
            char2.talk "Yeah sure [char1.fname]."
            char2.talk "They're just that big all on their own... {w}You only have {b}G cups{/b}... {w}So keep on dreaming."
            pause 0.5
            pl "Just ignore her [char1.fname]. Don't let her get to you."
            char1.talk "*whispers* She seems to forget that breast size is not just about the letter..."
            char1.talk "*whispers* {b}[char1.bra_size]{/b} means my breasts are the same size as 36 H, 34 I or 32 J."
            $ char1.bra_size_known = True
            char1.talk "In fact I'm not even wearing a bra..."
            if char1.check_affection(2, 0, False) == False:
                char1.talk "I don't know why I'm telling you this..."
                char1.talk "...it's about time I take a look around and make sure everything is quiet."
                char1.talk "See you later [char1.playername]."
                pl "Bye [char1.fname]."
                scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
                    zoom 0.667
                pause 0.5
                "You head back to the bar..."
                jump nightbar_security_talk_end

            char1.talk "Let me prove it..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat9.webp") with dissolve:
                zoom 0.5
            pause 0.7
            pl "Ummm... {w}You don't have to..."
            char1.talk "Hey, I'm not getting naked!"
            pause 0.5
            pl "Oh! {w}Okay..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat9.webp"):
                zoom 0.5
                ease 1.2 zoom 0.7 xpos -400 ypos -30
            pause 1.4
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat10.webp") with dissolve:
                zoom 0.7 xpos -400 ypos -30
            pause 1.2
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat11.webp") with dissolve:
                zoom 0.7 xpos -400 ypos -30
            pause 1.2
            char1.talk "No bra! You see?"
            pause 0.5
            pl "*gulp* Yes."
            $ player.change_lust(char1.sexiness + 2)
            char1.talk "So no cheating! {w}That's just how they are!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat12.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "*whispering* Normally I'm not like this, but I'm really enjoying having all of your attention right now..."
            char1.talk "*giggles* Even if most of it is focused on my chest!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat12.webp") with dissolve:
                zoom 0.8 xpos -600 ypos -150
            pause 0.7
            $ player.change_lust(char1.sexiness)
            pl "Sorry..."
            char1.talk "Don't be... {w}As I said, I really enjoy it."
            char1.talk "And the way [char2.fname] is glaring at us... *winks*"
            char1.talk "You know, what I really don't get is..."
            char1.talk "...why everyone on this island is so obsessed with my chest..."
            char1.talk "Sure it's impressive..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat13.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "...especially when I take a deep breath. *smirks*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat13.webp") with dissolve:
                zoom 0.8 xpos -500 ypos -90
            pause 0.7
            "You stare wide eyed at her pushed out chest..."
            "...just the right size for an incredible titfuck!"
            $ player.change_lust(char1.sexiness + 1)
            "Noticing your wide eyed look..."
            char1.talk "Sorry! *laughs*"
            char1.talk "What I was trying to say is that especially by island standards, my chest isn't that special."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat14.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "But really, who has a {b}[char1.hips_size]{/b} butt?"
            $ char1.hips_size_known = True
            "To prove her point she pushes out her tight round butt even further..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat15.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Back in my home town, most guys were leering at my behind..."
            char1.talk "...and not my boobs!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat15.webp"):
                zoom 0.5
                ease 1.5 zoom 1.0 xpos -800 ypos -400
            pause 1.7
            pl "I can surely understand why!"
            char1.talk "*laughs*"
            char1.talk "Okay, enough talk about my butt..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat16.webp") with dissolve:
                zoom 0.5
            pause 0.7
            pl "Hey, I didn't start it!"
            char1.talk "Yeah, okay. *smiles*"
            char1.talk "Can I leave you alone?"
            char1.talk "I need to check the bar to make sure everything is in order."
            pause 0.5
            pl "*laughs* Sure, go ahead. I'll have a drink in the meantime."
            char1.talk "See you later [char1.playername]."
            $ char1.add_scene_seen("Nightbar_security_rude")
            pl "Bye [char1.fname]. That was a really nice distraction. *smiling*"
            scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
                zoom 0.667
            pause 0.5
            "You head back to the bar..."
            jump nightbar_security_talk_end
    menu:
        "Compliment her" if l_option1:
            $ l_option1 = False
            $ l_talked +=1
            pl "You look really great in that green dress."
            char1.talk "Thank you!"
            call change_char_max_affection (char1, 3) from _call_change_char_max_affection_121
            $ char1.change_affection(6)
            char1.talk "It's kind of my security uniform for the evenings."
            $ char1.change_lust(5)
            char1.talk "Modest enough, but still fitting for an evening at a nice bar."
            pause 0.5
            menu:
                "Flirt with her" if True:
                    pl "Oh wow! {w}If this is one of your {i}modest{/i} dresses..."
                    pl "I'd really love to see one of your bold ones. *smiles*"
                    pause 0.4
                    pl "In any case, you look super hot!"
                    if char1.check_tease_sexual(2) == True:
                        $ char1.add_pl_interaction("tease_talk")
                        $ char1.add_pl_interaction("tease_body")
                        char1.talk "Thanks again. {w}I've really tried not to display too much cleavage."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat4.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                        char1.talk "*giggles* But they're just too big to hide."
                        char1.talk "I bet you'd love to see me in a more revealing dress... *smirks*"
                        char1.talk "Why don't you pay me a visit in the evening before I'm working at the bar?"
                        $ player.add_quest("Mercedes_visit_evening", mercedes, mercedes)
                        pl "I'd love that!"
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat6.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                        char1.talk "It's really not so easy to find something that fits with a chest and hips like mine."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                        char1.talk "When it fits around the bust and butt, most of the time it looks like a potato sack and is far to loose around the waist."
                        "You take a closer look at her alluring curves..."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp"):
                            zoom 0.5
                            ease 1.5 zoom 1.0 xpos -750 ypos -720
                        pause 1.8
                        "Yes, her ass is simply amazing!"
                        $ player.change_lust(char1.sexiness)
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp"):
                            zoom 1.0 xpos -750 ypos -720
                            ease 1.5 zoom 1.0 xpos -750 ypos -350
                        pause 1.8
                        "The view of her massive side boobs isn't half bad either."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp"):
                            subpixel True zoom 1.0 xpos -750 ypos -350
                            ease 1.5 zoom 1.25 xpos -1100 ypos -50
                        pause 1.8
                        char1.talk "Do you like what you see? *smiles*"
                        pl "What's not to like! {w}You look amazing [char1.fname]."
                        char1.talk "Thanks! {w}I know. *winks*"
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat6.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                    elif True:
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                        char1.talk "Hey! I'm working here!"
                        char1.talk "I'm not wearing the dress for your amusement [char1.playername]."
                        pl "Yes sure, sorry."
                        pl "I meant it as a compliment."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
                            zoom 0.5
                        pause 0.6
                        char1.talk "Okay, I'm not mad at you."
                "Give an encouraging, friendly answer" if True:

                    pl "Yes, it's lovely. The color really complements your hair and skin tone."
                    char1.talk "You think? *smiles*"
                    pause 0.5
                    pl "Yes, absolutely."

            jump nightbar_security_chat_menu

        "Ask about her super strength" if l_option2:
            $ l_option2 = False
            $ l_talked +=1
            pl "On the day of your arrival on the island, I was really impressed about what you did with your biceps."
            pause 0.4
            pl "I mean, it came more or less out of nowhere."
            pl "I'm really curious how you did it."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp") with dissolve:
                zoom 0.5
            pause 0.6
            $ char1.change_anger(8)
            char1.talk "I already told you that I'm not supposed to talk about it. *angry*"
            char1.talk "Was it so hard to understand last time?"
            pause 0.6
            if player.check_charm(3) == False:
                pl "Ummm... {w}No... Sorry for asking again."
                "What nice cleavage!"
                menu:
                    "Take a peek at her tits" if True:
                        "Despite her anger, her tits still look incredible..."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp"):
                            zoom 0.5
                            ease 1.0 zoom 1.0 xpos -750 ypos -500
                        pause 1.6
                        if player.check_sneaking(4) == False:
                            char1.talk "Honestly? {w}>You're staring at my tits while I scold you!"
                            $ char1.change_anger(8)
                            pl "Ummm..."
                        elif True:
                            "Before she notices, you quickly look back at her face."
                            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp"):
                                zoom 1.0 xpos -750 ypos -500
                                ease 1.0 ypos -80
                            pause 1.2
                    "Don't risk it" if True:

                        "You continue to concentrate on her face..."

                char1.talk "Let's forget about it. But please don't ask again."
                pause 0.5
                pl "Okay."
            elif True:
                pl "I was just wondering why you showed me if it's supposed to be a secret..."
                pause 0.4
                "Damn! What nice cleavage!"
                menu:
                    "Take a peek at her tits" if True:
                        "Despite her anger, her tits still look incredible..."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp"):
                            zoom 0.5
                            ease 1.0 zoom 1.0 xpos -750 ypos -500
                        pause 1.6
                        if player.check_sneaking(4) == False:
                            char1.talk "Honestly? {w}>You're staring at my tits while I scold you!"
                            $ char1.change_anger(8)
                            pl "Ummm..."
                            jump nightbar_security_chat_super_strength_end

                        "Before she notices, you quickly look back at her face."
                        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp"):
                            zoom 1.0 xpos -750 ypos -500
                            ease 1.0 ypos -80
                        pause 1.2
                    "Don't risk it" if True:

                        "You continue to concentrate on her face..."

                char1.talk "You're right, I probably shouldn't have shown you in the first place."
                scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
                    zoom 0.5
                $ char1.change_anger(-4)
                char1.talk "Sorry for snapping at you."
                pl "No need to be sorry, I shouldn't have asked again."

            label nightbar_security_chat_super_strength_end:
            pause 0.6
            char1.talk "Anything else you'd like to talk about?"
            jump nightbar_security_chat_menu

        "Ask [char1.fname] to talk about herself" if l_option3 and player.get_quest_state("Mercedes_background", mercedes) == 0:
            $ l_option3 = False
            $ l_talked +=1
            pl "I'd like to know how your life was before you came to the island."
            pl "What about your childhood and your parents? {w}Where did you live?"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat5.webp") with dissolve:
                zoom 0.5
            pause 0.6
            char1.talk "I grew up in Atlanta. My mother is a teacher and my father..."
            char1.talk "...well let's say me and my mother are happy we don't see him that often any more."
            pause 0.5
            pl "I'm sorry about your father."
            char1.talk "Don't be. He's not worth it."
            "She really seems to hate her old man..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat7.webp") with dissolve:
                zoom 0.5
            pause 0.6
            pl "What kinds of sports did you like as a child?"
            char1.talk "Oh... I wasn't much into sports at that time."
            char1.talk "I really wasn't a healthy child."
            pause 0.6
            char1.talk "Unfortunately it grew worse over time..."
            char1.talk "Some advanced form of muscle degeneration."
            pl "Damn! I'm so sorry."
            pause 0.5
            pl "But you're okay now?"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat5.webp") with dissolve:
                zoom 0.7 xpos -400
            pause 0.6
            char1.talk "What do you think?"
            pl "Ummm... {w}You look quite healthy... {w}Not ill at all."
            pause 0.5
            char1.talk "By my 18th birthday, I needed a wheelchair to go any distance at all."
            pl "What happened? {w}I mean how did you get better?"
            pause 0.4
            char1.talk "Well, Joy happened!"
            char1.talk "She helped me to get back on my feet. In the most literal sense of the word."
            pause 0.6
            pl "That's great. I'm happy that you're no longer ill."
            char1.talk "I appreciate that [char1.playername]."
            char1.talk "It didn't come without a price though."
            pl "I'm not sure I understand..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat7.webp") with dissolve:
                zoom 0.7 xpos -400
            pause 0.6
            char1.talk "I'm sorry, but I've already told you too much."
            char1.talk "We're not supposed to talk about it."
            pl "{i}We{/i}?"
            char1.talk "Miriam and I."
            char1.talk "You have to ask Joy if you want to know more."
            char1.talk "Not sure she'll tell you though."
            pl "Okay, thank you [char1.fname]."
            $ player.set_quest_state("Mercedes_background", mercedes, 100, True)
            pause 0.5
            char1.talk "Anything else I can do for you?"
            jump nightbar_security_chat_menu

        "Ask her to play poker with you" if l_option6 and  player.get_quest_state("Mercedes_background", char1) == 100 and player.get_quest_state("Mercedes_visit_evening", char1) == 100:
            $ l_option6 = False
            $ l_talked +=1
            if char1.get_appointment_seen("Poker"):
                pl "I really loved it the last time we played poker. *smiling*"
                pl "Would you like to play again?"
                if char1.get_action_allowed("poker_play") == False:
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat13.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    $ l_text = char1.get_action_not_allowed_text("poker_play")
                    char1.talk "[l_text]"
                    pause 0.4
                    pl "Okay."
                elif char1.check_tease_sexual(3, 0, False) == False:
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat13.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    char1.talk "Sorry, but I'm not really in the mood right now."
                    char1.talk "Maybe ask me another time."
                    pause 0.4
                    pl "Okay, sure."
                elif True:
                    char1.talk "So you want to get another good look at these... *smirks*"
                    $ char1.add_pl_interaction("tease_boobs")
                    $ char1.add_pl_interaction("tease_talk")
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat11.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    char1.talk "Sure, it was fun! 2 am at you room, like last time?"
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat12.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    pl "That works great, I'll be waiting for you. *smiles*"
                    $ player.add_appointment(27, char1, "player_room", 10)
                    char1.talk "I'll try to leave a little early again. *smiles*"
                    pause 0.5
                    char1.talk "Anything else on your mind?"
            elif True:
                pl "Ummm... [char1.fname]. Since that visit to your room, when you were working out..."
                pl "I can't get you out of my head."
                pause 0.4
                pl "Would you maybe like to play poker with me?"
                char1.talk "Poker?"
                char1.talk "You mean strip poker? You want to see me naked?"
                pl "Er... And if I did?"
                if char1.check_tease_sexual(3) == False:
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat3.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    char1.talk "Really? You're asking me to strip for you and show you my naked breasts and butt?"
                    pause 0.5
                    pl "I take it that was a no?"
                    char1.talk "You bet your ass that it was a no!"
                    pause 0.4
                    pl "Ummm... Okay. Sorry for asking."
                    char1.talk "Don't ask a girl something like that until you know her a lot better!"
                    scene expression ("scenes/Mercedes/nightbar/Mercedes_nightbar_security_chat5.webp") with dissolve:
                        zoom 0.5
                    pause 0.6
                    char1.talk "Now is there anything else I can do for you, that doesn't involve getting naked?"
                    jump nightbar_security_chat_menu

                char1.talk "*chuckles*"
                scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat12.webp") with dissolve:
                    zoom 0.7 xpos -400
                pause 0.6
                char1.talk "Do you have a nice and quiet place where we could play without being disturbed?"
                if player.room2 == True:
                    pl "I think I do. *grins*"
                    pl "My new room fits the description nicely. *smiling*"
                    char1.talk "Great."
                    pause 0.5
                    pl "Ummm... Tonight, after the bar closes?"
                    char1.talk "So you can't wait to see me naked... *chuckles*"
                    char1.talk "Okay, sure. I try to leave a little earlier today. How about 2 am at you room?"
                    pause 0.4
                    pl "That works great, I'll be waiting for you. *smiles*"
                    $ player.add_appointment(27, char1, "player_room", 10)
                    char1.talk "It's going to be fun! *grins*"
                    pause 0.5
                    char1.talk "Anything else on your mind?"
                elif True:
                    pl "I don't know. My current room doesn't really qualify... *musing*"
                    pl "...and I can't think of another place that would work."
                    pause 0.4
                    char1.talk "That's too bad..."
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat16.webp") with dissolve:
                        zoom 0.7 xpos -400
                    pause 0.6
                    char1.talk "So I guess you'll have to find a nice place first, before you'll see those without the dress. *smirks*"
                    $ char1.add_pl_interaction("tease_boobs")
                    $ char1.add_pl_interaction("tease_talk")
                    pause 0.5
                    char1.talk "Anything else I can do for you?"

            scene expression ("scenes/Mercedes/nightbar/Mercedes_nightbar_security_chat5.webp") with dissolve:
                zoom 0.5
            pause 0.6
            jump nightbar_security_chat_menu

        "Ask about her security job" if l_option4:
            $ l_option4 = False
            $ l_talked +=1
            pl "I'm really curious how a beautiful girl like you wound up in the security business."
            pause 0.5
            char1.talk "To be honest, working security just anywhere probably wouldn't have gone that well."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
                zoom 0.7 xpos -350
            pause 0.6
            char1.talk "I mean I tried it a few times after my professional training."
            pause 0.5
            char1.talk "And since Joy organized and even monitored the training, you can believe me when I say it was top notch."
            char1.talk "Joy doesn't do anything halfway, or even just okay."
            char1.talk "My point is... {w}Working security as a woman is always harder. You have to listen to a lot of shit."
            char1.talk "From drunk guys to jealous girlfriends..."
            pause 0.5
            pl "I'm pretty sure you can handle the drunk guys. *chuckles*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat4.webp") with dissolve:
                zoom 0.6 xpos -200
            pause 0.6
            char1.talk "You bet I can!"
            pause 0.5
            char1.talk "Still, it's not a lot of fun having to listen to statements like {i}nice ass{/i} or {i}wow, huge tits{/i} all the time."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp") with dissolve:
                zoom 0.5
            pause 0.6
            "Yeah well, her tits are really incredible..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp"):
                subpixel True zoom 0.5
                ease 1.8 zoom 1.2 xpos -1100 ypos -400
            pause 2.0
            "...but why say it to her face when you can enjoy it quietly... *chuckling inwardly*"
            $ player.change_lust(char1.sexiness)
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat2.webp"):
                zoom 1.2 xpos -1100 ypos -400
                ease 1.0 ypos 0
            pause 1.4
            char1.talk "The main problem is that you're supposed to be the calming presence and you need to keep it all quiet and peaceful."
            char1.talk "So you have to be careful with your remarks. {w}And some of these assholes know it and use it against you."
            pause 0.5
            pl "I had no idea... {w}Sounds pretty bad."
            char1.talk "Don't worry, it's not like that all the time."
            char1.talk "Sometimes a nice guy comes over and just wants to talk for a bit. *winks*"
            char1.talk "If he's also cute, I don't really mind him enjoying the scenery every now and then. *winks*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp") with dissolve:
                zoom 0.5
            pause 0.6
            char1.talk "I might even encourage him. *smirks*"
            pl "Ohh... *wide eyed look*"
            "Shit, she caught you staring at her tits!"
            "Fortunately, she seemed to enjoy it."
            char1.talk "*laughs* You can look if you want!"
            $ char1.add_pl_interaction("tease_body")
            $ char1.add_pl_interaction("tease_talk")
            menu:
                "Look at her face" if True:
                    "Despite her encouraging behavior, you decide to look at her face."
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp") with dissolve:
                        zoom 1.0 xpos -800
                    pause 0.6
                    char1.talk "You're really cute you know! *laughs*"
                    pl "Just enjoying the best part of you *smiles*"
                    char1.talk "You're a liar you know! *smiles*"
                    char1.talk "But a charming one... *smiles some more*"
                    $ char1.change_affection(8)
                "Look at her side boobs" if True:

                    "You can't resist taking a closer look at her incredible tits."
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp") with dissolve:
                        subpixel True zoom 1.25 xpos -1100 ypos -450
                    pause 0.6
                    $ player.change_lust(char1.sexiness)
                    char1.talk "Yes, I figured you for a tit man. *smirks*"
                    pl "Oh... Is that a bad thing?"
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp"):
                        subpixel True zoom 1.25 xpos -1100 ypos -450
                        ease 1.2 zoom 1.25 xpos -1100 ypos 0
                    pause 1.6
                    char1.talk "Not at all... *laughs*"
                    char1.talk "I think I can satisfy every need in that department."
                    $ char1.change_lust(8)
                "Look at her butt" if True:

                    "You can't resist taking a closer look at her amazing butt."
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp") with dissolve:
                        subpixel True zoom 1.25 xpos -1200 ypos -1080
                    pause 0.6
                    $ player.change_lust(char1.sexiness)
                    char1.talk "I didn't really figure you for an ass man! *smirks*"
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat8.webp"):
                        subpixel True zoom 1.25 xpos -1200 ypos -1080
                        ease 1.6 zoom 1.25 xpos -1100 ypos 0
                    pause 0.6
                    pl "I enjoy all kinds of curves."
                    pl "I hope that's okay with you."
                    char1.talk "Well, since I have {i}all kinds of curves{/i} in the right places..."
                    char1.talk "...I guess I can accept that. {w}For now! *winks*"
                    $ char1.change_lust(5)
                    $ char1.change_affection(5)

            pause 0.5
            char1.talk "Okay... I think you've seen enough... *smiles*"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat5.webp") with dissolve:
                zoom 0.7 xpos -300
            pause 0.6
            char1.talk "Anything else you'd like to talk about?"
            jump nightbar_security_chat_menu

        "Talk about the island" if l_option5:
            $ l_option5 = False
            $ l_talked +=1
            pl "What do you think about the island? Do you like it here?"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat5.webp") with dissolve:
                zoom 0.5
            pause 0.6
            char1.talk "I think it's a nice place."
            char1.talk "The pool is really great. I just love that area."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_security_chat7.webp") with dissolve:
                zoom 0.5
            pause 0.6
            char1.talk "I haven't had a lot of opportunity to go to the beach, since Miriam's taking care of safety there."
            pause 0.4
            char1.talk "The evenings are not too bad either."
            char1.talk "Especially when I have nice company as I do right now. *smiles*"
            pause 0.5
            pl "I bet a beautiful girl such as yourself fits right in with all the other incredible girls here."
            scene expression ("scenes/Mercedes/nightbar/Mercedes_nightbar_security_chat5.webp") with dissolve:
                zoom 0.5
            pause 0.6
            char1.talk "Thank you [char1.playername], you're sweet."
            call change_char_max_affection (char1, 3) from _call_change_char_max_affection_122
            $ char1.change_affection(6)
            pause 0.5
            char1.talk "Most of them are great..."
            char1.talk "Well, some of them think they are the stars and I'm just here for security."
            pause 0.5
            pl "That's really mean."
            char1.talk "It's not that bad. {w}Let's just talk about something else."
            pl "Sure."
            jump nightbar_security_chat_menu

        "Tell her you have to go" if not l_option1 or not l_option2 or not l_option3 or not l_option4 or not l_option5:
            pl "It was really nice talking to you [char1.fname]."
            pause 0.5
            pl "I think it's a good time to get a drink now. {w}Do you want anything?"
            char1.talk "I'm good, thanks."
            pause 0.5
            pl "Okay, see you later."
            char1.talk "Bye [char1.playername]!"
            scene expression ("locations/loc_nightbar_bar_[jobs.bartender.fname].webp") with dissolve:
                zoom 0.667
            pause 0.5
            "You walk back to the bar."

    label nightbar_security_talk_end:
    call actions_used (1) from _call_actions_used_185
    $ g_left_menu_hidden = l_left_menu_hidden
    $ menu_active = False
    $ stop_scene()
    return "nothing"





label action_nightbar_arm_wrestling(char1):
    $ menu_active = True
    call main_game_background (location, location_detail, _return) from _call_main_game_background_112
    show screen main_game(location)
    pl "Ummm... [char1.fname]... {w}Would you like to arm wrestle against me?"

    if char1.get_action_allowed("Arm_wrestling") == False:
        $ l_text = char1.get_action_not_allowed_text("Arm_wrestling")
        char1.talk "[l_text]"
        pl "Okay, I'll ask again later."
        jump action_nightbar_arm_wrestling_end

    if char1.get_action_allowed("anger_block") == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_30
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("Arm_wrestling", 4, "You just asked me the exact same thing not long ago and I already said no!")
        jump action_nightbar_arm_wrestling_end

    $ char1.add_action_cooldown("Arm_wrestling", 48, "Come on, we just did it not long ago, give me a break!")
    $ l_bartender = jobs.bartender
    char1.talk "Are you sure about that?"
    pl "Yep, I think I can beat you today. *smiles*"
    char1.talk "In that case, let me change my clothes. I'll be back in no time. *grins*"
    pl "I can't wait."
    $ char1.locations[actions_left-1] = char1.fname + "_room"
    "After [char1.fname] has left, you talk with [l_bartender.fname] at the bar."
    $ start_scene()
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp"):
        zoom 0.5
    with fade
    pause 0.7
    l_bartender.talk "Hey [l_bartender.playername], how are you doing?"
    pl "I'm on an island full of beautiful girls. *grinning*"
    pl "I'm doing great."
    l_bartender.talk "I see... *giggles*"
    l_bartender.talk "Do you like a drink?"
    menu:
        "Agree" if True:
            pl "Sure, why not. A whiskey would be nice."
            l_bartender.talk "Won't take long."
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink2.webp") with dissolve:
                zoom 0.5
            pause 0.5
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink4.webp") with dissolve:
                zoom 0.5
            pause 0.7
            l_bartender.talk "Here you go."
            pl "Thank you."
            "You take the glass and drown it."
            $ player.add_effect("drunk")
            scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
                zoom 0.5
            pause 0.7
            l_bartender.talk "Are you a little nervous?"
            pl "How did you know?"
            l_bartender.talk "Just judging from the way you drowned your whiskey. *grins*"
            pl "Oh... Am I that obvious? *smiling*"
            if player.get_effect_state("yellow tablet") > 0:
                l_bartender.talk "To prevent cheating, I've added a counter substance to your drink."
                l_bartender.talk "It's harmless, but it remove the strength gain from the yellow tablet."
                pl "Oh..."
                "Damn! That didn't work!"
        "Decline" if True:

            pl "I don't know, I think I better stay sober for the arm wrestling with [char1.fname]."
            l_bartender.talk "That's probably a good call. *smiles*"
            if player.get_effect_state("yellow tablet") > 0:
                l_bartender.talk "But to prevent cheating, please drink this. It's non alcoholic, but will remove the strength gain from the yellow tablet."
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink4.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                "Damn! That didn't work!"
                pl "Ummm... Do I have to?"
                l_bartender.talk "Yes, or I'll have to tell [char1.fname]..."
                pl "Okay."
                pl "You take the glass and drown the brown liquid."
                scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
                    zoom 0.5
                pause 0.7
                $ player.rem_effect("yellow tablet")
                l_bartender.talk "Thank you."

    l_bartender.talk "My day was pretty much uneventful..."
    l_bartender.talk "...but I hope we get to see quite a spectacle soon. *grinning*"
    pause 0.6
    "You talk some more with the bartender to pass the time..."
    pause 1.0
    call actions_used (1) from _call_actions_used_249
    l_bartender.talk "Oh... [char1.fname] is back already. That was fast."
    "You turn your head in the direction [l_bartender.fname] is looking."
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling1.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "There she is... Wearing her push up bra and the too tight top "
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling2.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "Even from afar she looks incredible."
    pl "{b}Shit{/b}! I mean wow!"
    char1.talk "Hey [char1.playername], are you waiting for someone?"
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling3.webp") with dissolve:
        zoom 0.5
    $ renpy.pause(0.6,hard=True)
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling4.webp") with dissolve:
        zoom 0.5
    $ renpy.pause(0.6,hard=True)
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling5.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Just in case it was me... {w}Here I am! *grins*"
    pl "*gulp* Hello [char1.fname]."
    char1.talk "I changed as fast as I could..."
    char1.talk "...but squeezing my huge breasts into the bra wasn't easy. *smirks*"
    pl "I can only imagine..."
    char1.talk "You better don't right now. *smiles*"
    char1.talk "Would you like another look at my flexed biceps before we start?"
    menu:
        "Sure, always" if True:
            pl "Sure, I'd love to. *smiles"
            char1.talk "Fine, so her you go!"
            scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling6.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "You still think you can beat me and these biceps? *winks*"
            scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling7.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Or stay focused long enough... *grins*"
            pl "Er... I think that's enough, [char1.fname]."
            pl "Thank you."
            char1.talk "*chuckles* Are you getting hard already?"
            scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling8.webp") with dissolve:
                zoom 0.5
            pause 0.7
            pl "No, I'm not...!"
            char1.talk "You're so easy to tease, [char1.playername]. *smiles*"
        "Maybe next time" if True:

            pl "Ummm... {w}Maybe next time. I can't wait to start."
            scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling8.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Okay, me too. *smiles*"

    char1.talk "Are you ready to get beaten by a girl again? *smiles*"
    pl "That remains to be seen... *grinning*"
    pl "But yes, I'm ready!"
    char1.talk "We can use the counter at the bar. It has a good height."
    pl "Yes, worked great last time."
    char1.talk "I'll use the bartender side. It's my lucky side. *smiles*"
    pl "Fine with me."
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling9.webp") with fade:
        zoom 0.5
    pause 0.7
    char1.talk "I can't wait... *smiles*"
    pl "Me either. *smiling back*"
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling10.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "You got anything to say before I smash your hand down on the counter? *chuckles*"
    pl "Ha ha don't be so sure you're going to win!"
    char1.talk "[l_bartender.fname], can you be our referee?"
    l_bartender.talk "Sure thing."
    l_bartender.talk "Best of three or just one match?"
    pl "Best of three like last time, [char1.fname]?"
    char1.talk "Yes, so I can play with you a little longer... *chuckles*"
    pause 0.5
    pl "Okay, best of three it is!"
    l_bartender.talk "Arms on the counter, clasp hands."
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling11.webp") with dissolve:
        zoom 0.5
    pause 0.7
    l_bartender.talk "Are you both ready?"
    pl "Yes!"
    char1.talk "Me too."
    if player.get_strength() <= 5:
        "From how she holds your hand, you can already feel her incredible strength."
        "This probably was a bad idea, competing against her with your current strength."
        "It feels a little like she could crush your hand if she wanted to..."
    elif player.get_strength() == 6:
        "From the way she's squeezing your hand and judging from her unmoving arm, she's even stronger than you thought."
        "Well, you're pretty strong yourself..."
    elif player.get_strength() == 7:
        "The way she's holding your hand, you can feel that she's definitely strong for a girl."
        "But you think you might be just a little stronger than her."
    elif True:
        "Judging from how it feels when you clasp hands, she's either holding back, or you're stronger than her."

    l_bartender.talk "I will count down from 3. You start at my go."
    l_bartender.talk "Three..."
    l_bartender.talk "Two..."
    l_bartender.talk "One..."
    l_bartender.talk "Go!"
    scene expression ("events/[char1.fname]/nightbar/[char1.fname]_event_arm_wrestling12.webp") with dissolve:
        zoom 0.5
    pause 0.7

    if player.get_strength() <= 5:
        call amy_bar_arm_wrestling_low_strength_event (char1) from _call_amy_bar_arm_wrestling_low_strength_event_1
    if player.get_strength() == 6:
        call amy_bar_arm_wrestling_med_strength_event (char1) from _call_amy_bar_arm_wrestling_med_strength_event_1
    elif True:
        call amy_bar_arm_wrestling_high_strength_event (char1) from _call_amy_bar_arm_wrestling_high_strength_event_1

    label action_nightbar_arm_wrestling_end:
    $ stop_scene()
    $ menu_active = False
    return "nothing"





label action_nightbar_dance(char1, i_auto_succeed=False, i_show_intro=True):
    $ l_masturbate = False
    $ l_masturbate_to = 0
    $ l_bartender = jobs.bartender
    $ l_auto_succeed = i_auto_succeed

    pl "Hey [char1.fname]. Would you like to dance with me?"

    if char1.get_action_allowed("nightbar_dance") == False and l_auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("nightbar_dance")
        char1.talk "[l_text]"
        return "do_return"

    if char1.get_action_allowed("anger_block") == False and l_auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_87
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ location_detail = ""
        $ char1.add_action_cooldown("nightbar_dance", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "do_return"

    if l_auto_succeed == False and char1.check_affection(2) == False:
        char1.talk "Sorry [char1.playername], but I'm not in the mood right now. Maybe another time."
        pl "That's a pity. I'm sure it would have been nice."
        return "do_return"

    call action_closeup (char1, location, False, False) from _call_action_closeup_93
    char1.talk "Of course I do. I love to dance."
    char1.talk "Let's head over to the dance floor. *smiles*"
    $ l_walk_image = char1.get_walk_image(location)
    $ l_walk_image_zoom = char1.get_walk_image_zoom(l_walk_image)
    $ l_xpos = renpy.random.randint(250,450)
    $ l_flip = renpy.random.randint(0,1)
    scene expression ("locations/loc_nightbar_dance_from_bar.webp"):
        zoom 0.5
    hide screen closeup
    $ location_detail = ""
    $ start_scene()
    $ menu_active = True
    if l_flip == 0:
        show expression im.MatrixColor(l_walk_image, im.matrix.brightness(0)):
            xpos l_xpos zoom l_walk_image_zoom
    elif True:
        show expression im.Flip(l_walk_image, True):
            xpos l_xpos zoom l_walk_image_zoom


    with fade
    pause 1.0
    char1.talk "Are you coming?"
    char1.talk "You don't want to keep a pretty girl waiting, do you?"
    pause 0.4
    pl "Never! I'm right behind you!"
    pause 0.3
    "Damn! She's so sexy when she looks at you like that."
    $ player.change_lust(char1.sexiness / 2)
    "You can't wait to see her dance."
    scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_dance1.webp") with fade:
        zoom 0.5
    pause 0.5
    char1.talk "{b}[l_bartender.fname], could we have some dance music?{/b}"
    l_bartender.talk "{b}Sure my dear. Just a second.{/b}"
    play music "music/nightbar8.mp3" loop fadeout 0.3
    pause 1.2
    l_bartender.talk "{b}Is this better?{/b}"
    char1.talk "What do you think, [char1.playername]."
    pause 0.4
    "You listen to the music for some seconds..."
    pause 1.2
    pl "Yeah, sounds good."
    char1.talk "{b}Works great, thank you!{/b}"
    image yvette_night2_dance1 = Movie(play="scenes/Yvette/nightbar/night2/anim/Yvette_nightbar_dance_v1.webm", side_mask=True)
    scene expression ("locations/loc_nightbar_dance_pan.webp") at move_pana4()
    show yvette_night2_dance1 at move_video3()
    with dissolve
    pause 4.0
    char1.talk "It's a nice slow song. *smiles*"
    char1.talk "If I dance any faster, my breasts will probably bounce out of the top. *giggles*"
    pl "Er... Yeah..."
    "Her dance is distracting enough as it is already."
    $ player.change_lust(char1.sexiness)
    pause 0.4
    char1.talk "C'mon, this is so much fun! You should smile and enjoy it!"
    pl "Believe me, I really do!"
    pause 0.7
    char1.talk "I hope my bouncing around isn't too distracting."
    pl "I enjoy that too. *grinning*"
    char1.talk "Haha. *laughs* \nWhy am I not surprised? *grins*"
    pause 0.7
    char1.talk "Want me to shake my breasts for you?"
    pl "Sure. *grins*"
    char1.talk "Just let me catch my breath for a second."
    scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_dance8.webp") with fade:
        zoom 0.5
    pause 0.6
    pl "I can see that you really enjoy dancing."
    char1.talk "As I said, I love it!"
    pause 0.4
    play music "music/nightbar5.mp3" loop fadeout 0.3
    pause 0.4
    char1.talk "Already recovered. I'm up for some naughty dancing. *smiles*"
    scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_dance7.webp") with dissolve:
        zoom 0.5
    pause 0.6
    char1.talk "Ready?"
    pl "Yep."
    image yvette_night2_dance3 = Movie(play="scenes/Yvette/nightbar/night2/anim/Yvette_nightbar_dance_v3.webm", side_mask=True)
    scene expression ("locations/loc_nightbar_dance_pan.webp") at move_pana4()
    show yvette_night2_dance3 at move_video4()
    with dissolve
    pause 4.0
    $ player.change_lust(char1.sexiness+2)
    pl "Wow!"
    pl "I wonder how do you manage to keep them inside the top."
    pause 0.4
    char1.talk "*laughs* Training I guess."
    char1.talk "I have a good feeling for how fast I can move without them bouncing out."
    pause 0.4
    char1.talk "Sideways is a lot easier than up and down. *winks*"
    pause 3.0
    char1.talk "I think that's enough. My poor bosom is already getting dizzy. *chuckles*"
    scene expression ("scenes/[char1.fname]/nightbar/night[char1.nightwear]/[char1.fname]_nightbar_dance4.webp") with dissolve:
        zoom 0.5
    pause 0.6
    char1.talk "One more dance before we head back to the bar?"
    pl "Sure. I could watch you dance all evening. *smiling*"
    pause 0.4
    play music "music/nightbar6.mp3" loop fadeout 0.3
    pause 0.4
    char1.talk "Thank you. *smiles*"
    image yvette_night2_dance2 = Movie(play="scenes/Yvette/nightbar/night2/anim/Yvette_nightbar_dance_v2.webm", side_mask=True)
    scene expression ("locations/loc_nightbar_dance_pan.webp") at move_pana4()
    show yvette_night2_dance2 at move_video3()
    with dissolve
    pause 4.0
    "bla"


    $ char1.add_scene_seen("Nightbar_dance")
    label action_nightbar_dance_end:
    $ stop_scene()
    $ menu_active = False
    return "nothing"




label action_nightbar_dance_yvette(char1):

    label action_nightbar_dance_yvette_end:
    return "nothing"





label nightbar_denim_photo_shooting_intro(char1):
    pl "Hey [char1.fname]! How are you doing?"
    char1.talk "I'm good, thanks for asking. *smiles*"
    pause 0.6
    char1.talk "Can I talk with you for a minute?"
    menu:
        "Yes" if True:
            pl "Sure, anytime. What's up?"
        "You'd rather talk about..." if True:

            pl "Ummm... Maybe another time, I'd rather..."
            char1.talk "Oh really? *a little sad*"
            $ char1.change_affection(-8)
            jump nightbar_denim_photo_shooting_intro_end

    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink6.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I could use your help with something..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink6.webp"):
        zoom 0.5
        ease 1.5 zoom 1.0 xpos -600 ypos -100
    $ renpy.pause(2.0,hard=True)
    pl "*gulp*"
    "The way she's looking at you and presenting her tits, it's going to be really hard to say no."
    pause 0.6
    pl "I'm listening. *smiling*"
    char1.talk "Thanks. *smiles*"
    pause 0.5
    char1.talk "Ummm... Would you like to have a drink while we talk?"
    pause 0.4
    pl "Thanks for asking, I'm good."
    char1.talk "Okay."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink5.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Why don't you have a seat, it's going to take some time to explain."
    pause 0.4
    pl "Sure."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink7.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "After you've made yourself comfortable on the bar stool, [char1.fname] starts talking."
    pause 0.6
    char1.talk "You know, I have this friend who's a photographer."
    pause 0.4
    char1.talk "He's a really nice guy and he helped me a lot with my swimwear and clothes collections."
    char1.talk "I mean he knows so many models and he takes really great pictures."
    pause 0.4
    char1.talk "Since I'm not rich or anything, he did most of the pictures for free."
    pause 0.6
    pl "That's quite nice of him."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "As I said, he really is a nice guy."
    "You start to wonder what this is about..."
    pause 0.4
    char1.talk "He called me yesterday."
    char1.talk "He's shooting for a sexy calendar right now and his two main models left the agency and switched to another one."
    pause 0.4
    char1.talk "He was really devastated, because it's for one of his best clients."
    pause 0.4
    pl "Can't he get some other models? {w}I mean you said he knows quite a lot of them."
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink7.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Normally it wouldn't be a problem, but it's almost impossible to find suitable replacements for this project."
    pause 0.5
    pl "Okay... {w}What's so special about the calendar?"
    pause 0.6
    char1.talk "It's about really busty blondes wearing denim and tight tops."
    pl "Oh... {w}That sounds like fun. *grinning*"
    pause 0.6
    char1.talk "He told me that of the two girls who quit, one was an {b}H cup{/b} and the other one a large {b}G cup{/b}. And both are slim and athletic."
    char1.talk "A combination that's pretty hard to find."
    pause 0.5
    pl "So why did he call you?"
    char1.talk "Some time ago, I spoke with him about my job on an island full of busty girls."
    char1.talk "I offered to take some pictures..."
    pause 0.4
    char1.talk "He said that I'm a really great photographer but it would be better if a guy could take the pictures."
    char1.talk "He probably thought I didn't know where to point the camera. *chuckles*"
    pause 0.4
    pl "But you take really great pictures!"
    char1.talk "Thanks. *smiles*"
    char1.talk "But I agree with him, it's a job better done by a guy."
    char1.talk "I showed him some of the pictures you took with Eva and Brenda at the studio."
    pause 0.4
    char1.talk "Damn! I asked them if it was okay to show him the pictures, but I totally forgot to ask you."
    char1.talk "I'm really sorry."
    pause 0.5
    pl "Don't worry about it."
    pl "So what did he say?"
    pause 0.5
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "He likes them and says that you're really talented."
    pl "I am? That's cool. *smiling*"
    pause 0.4
    char1.talk "He asked if you could help him out and take some pictures for the calendar."
    char1.talk "Normally I wouldn't ask you something like that..."
    char1.talk "But he's been so nice to me and I'd love to be able to help him out."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink6.webp") with dissolve:
        zoom 0.7 xpos -350 ypos -70
    pause 0.5
    char1.talk "Please, will you help me? {w}And him? *smiles*"
    pl "Ummm... Pictures of you?"
    char1.talk "*chuckles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink9.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "You mean because of the impressive cleavage on display?"
    char1.talk "A lot is related to the dress. *smirks*"
    pause 0.5
    char1.talk "Not pictures of me. I'm too small for what his client is looking for."
    pl "Ummm... You're not small!"
    char1.talk "*chuckles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink7.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I didn't say that I'm small. Just not quite big enough for the calendar."
    pause 0.4
    pl "Are you two... {w}I mean is he your boyfriend?"
    char1.talk "*chuckles* You mean Nathan? The photographer?"
    pause 0.4
    pl "Ummm... Yeah... *defensively*"
    pause 0.4
    char1.talk "We're just friends. He's more than twice my age and more like a father."
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink6.webp") with dissolve:
        zoom 0.7 xpos -350 ypos -70
    pause 0.5
    char1.talk "Are you... {w}Jealous? *smiles*"
    $ player.change_lust(char1.sexiness+4)
    pl "Er... No! I'm just curious!"
    pause 0.5
    char1.talk "Okay, Mr. {i}just curious{/i}. {w}Could you ask some of the girls to pose for the calendar?"
    pause 0.4
    char1.talk "Please? *smiles*"
    char1.talk "You can use the studio."
    pause 0.4
    pl "You don't have to look at me like that. I wasn't going to say no."
    pl "I mean if they're okay with me taking pictures."
    pause 0.5
    char1.talk "Thank you, [char1.playername], you're the best. *smiles*"
    call change_char_max_love (char1, 4) from _call_change_char_max_love_33
    $ char1.change_love(8)
    pl "I haven't done anything yet."
    pause 0.4
    char1.talk "I hope you don't mind me looking at you like this. *smirks*"
    $ char1.add_pl_interaction("tease_talk")
    $ char1.add_pl_interaction("tease_boobs")
    pl "*chuckles*"
    pl "As long as you don't mind me getting hard, we're good *grins*"
    pause 0.4
    char1.talk "Haha, okay. I guess I had that one coming. *giggles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink7.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Thank you for helping. It really means a lot to me."
    char1.talk "Shall we talk about suitable girls for the calendar?"
    pl "Sure."
    char1.talk "What do you think, who do you want to ask?"
    pause 0.4
    "You reflect for a moment, before you answer."
    $ l_option1 = True
    $ l_option2 = True
    $ l_option3 = True
    $ l_option4 = True
    $ l_option5 = True
    $ l_option6 = True
    label nightbar_denim_photo_shooting_intro_menu:
    menu:
        "Renée" if l_option1:
            $ l_option1 = False
            pl "What do you think about Renée?"
            char1.talk "She's certainly slim and athletic, but I don't think her breasts are big enough."
            char1.talk "I mean I'm bigger than her and still too small."
            pause 0.5
            pl "Yes, you're probably right. *musing*"
            char1.talk "Any other ideas?"
            jump nightbar_denim_photo_shooting_intro_menu

        "Faye" if l_option2:
            $ l_option2 = False
            pl "How about Faye?"
            char1.talk "*laughs* I'm pretty sure Nathan's client would love that."
            char1.talk "But I don't think you'll ever be able to make her wear a blonde wig. *grins*"
            pause 0.4
            pl "Ummm... Yeah, probably not."
            pl "But it might be fun to ask."
            pause 0.4
            char1.talk "You better don't. I mean not if you want her to continue talking with you."
            char1.talk "Anyone else on your mind?"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink8.webp") with dissolve:
                zoom 0.5
            pause 0.7
            jump nightbar_denim_photo_shooting_intro_menu

        "Natasha" if l_option3:
            $ l_option3 = False
            pl "Would Natasha work?"
            char1.talk "She certainly has an impressive chest. *smiles*"
            char1.talk "And she's kind of athletic too."
            pause 0.4
            char1.talk "But can you really imagine her with blonde hair?"
            pause 0.4
            pl "You're right, probably not. *chuckles*"
            "Thinking about Natasha's dark skin and her having blonde hair makes you smile about yourself."
            pl "Yeah, definitely not a good idea."
            jump nightbar_denim_photo_shooting_intro_menu

        "Aly" if l_option4:
            $ l_option4 = False
            pl "How about Aly?"
            pl "I mean she's blonde and she certainly has the breasts. *grinning*"
            pause 0.5
            char1.talk "Could work, but I'm not quite sure. *musing*"
            char1.talk "She's not what I'd call slim or athletic."
            char1.talk "I mean she has a great figure, but is more on the voluptuous side."
            pause 0.4
            pl "Yes, there's that..."
            pl "So someone else... Let me think about it."
            jump nightbar_denim_photo_shooting_intro_menu

        "Alice" if (not l_option1 or not l_option2) and l_option5:
            $ l_option5 = False
            pl "What about Alice?"
            char1.talk "Yes, I think Alice is a perfect match."
            char1.talk "Her breasts are even bigger than G or H cups. She's slim and athletic and has blonde hair."
            pause 0.4
            char1.talk "I'm sure Nathan's client would love her pictures."
            pause 0.5
            pl "Okay. now I only have to persuade her to do it. *smiles*"
            pause 0.4
            char1.talk "I'm sure you'll manage somehow. *smiles*"
            char1.talk "One girl picked, one to go."
            pause 0.4
            pl "Yes... *musing* {w}Who else could work?"
            jump nightbar_denim_photo_shooting_intro_menu

        "Jessica" if (not l_option3 or not l_option4) and not l_option5 and l_option6:
            $ l_option6 = False
            pl "I could ask Jessica to do it."
            char1.talk "Oh yes! Definitely!"
            char1.talk "No idea why I haven't thought about her right away."
            char1.talk "Nathan would love her."
            pause 0.5
            pl "Ummm... Yeah... {w}She's probably going to tease me to death when I'm alone with her in the studio..."
            pause 0.4
            char1.talk "*chuckles Are you afraid of her?"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink9.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Or of bossy women in general?"
            pl "I'm not afraid of her. It's just that you never really know what she's up to."
            pl "One minute she behaves like she wants to rip off your clothes and the next she just leaves."
            pause 0.4
            char1.talk "Sounds like you're going to enjoy doing a photo shoot with her. *grins*"
            pl "First I have to persuade her to do it."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink7.webp") with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "I'm pretty sure she's going to say yes."

    pl "Which of the two should I ask first?"
    char1.talk "I think it's probably better if you start with Alice."
    char1.talk "Since it's about big breasts, we should start with the {i}smaller{/i} ones. *chuckles*"
    pl "Yeah, okay. Not that you could call Alice's breasts {i}small{/i}."
    char1.talk "No, not really. *grins*"
    $ player.add_quest("Denim_photo_shootings", char1, char1)
    char1.talk "Once you've taken the photos with Alice, bring me the memory card with the photos I will send them to Nathan."
    pause 0.3
    pl "Sure thing."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_get_drink6.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Thanks again for helping me with this."
    pl "Don't mention it, I still haven't done anything yet."
    pl "I hope the girls agree."
    char1.talk "I'm sure of that. I mean with a charming guy like you. *grins*"
    pause 0.4
    pl "Haha, very funny. *grinning back*"
    char1.talk "I really mean it. *smiles*"
    pause 0.5
    char1.talk "Since that's settled, is there anything I can do for you?"
    scene expression ("scenes/[l_bartender.fname]/nightbar/[l_bartender.fname]_nightbar_get_drink1.webp") with dissolve:
        zoom 0.5
    pause 0.6
    label nightbar_denim_photo_shooting_intro_end:
    return "nothing"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
