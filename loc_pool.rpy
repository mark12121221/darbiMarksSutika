


screen pool_actions:
    if selected_char.id <> 999 and location == "pool":
        text "Pool [selected_char.fname]" size 15 color "#66c1e0" xpos 1093 ypos 425
        $ xpos_new = 1093
        if menu_active == True:
            if selected_char.get_action_icon_available("pool_sunbed"):
                imagebutton auto "gui/action_pool_sunbed_%s.png" xpos xpos_new ypos 445 focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("pool_swim"):
                imagebutton auto "gui/action_pool_swim_%s.png" xpos xpos_new ypos 445 focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("pool_play"):
                imagebutton auto "gui/action_pool_play_%s.png" xpos xpos_new ypos 445 focus_mask True
        else:
            if selected_char.get_action_icon_available("pool_sunbed"):
                imagebutton auto "gui/action_pool_sunbed_%s.png" action Return("do_pool_sunbed") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to take the sunbed beside her.") focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("pool_swim"):
                imagebutton auto "gui/action_pool_swim_%s.png" action Return("do_pool_swim") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to go swimming with you.") focus_mask True
                $ xpos_new += 45
            if selected_char.get_action_icon_available("pool_play"):
                imagebutton auto "gui/action_pool_play_%s.png" action Return("do_pool_play") xpos xpos_new ypos 445 hovered tt.Action ("Ask [selected_char.fname] to play in the pool with you.") focus_mask True





screen pool_pl_actions:
    if selected_char.id == 999 and location == "pool":
        text "Player pool actions" size 15 color "#66c1e0" xpos 1093 ypos 310
        if menu_active == True:
            imagebutton idle "gui/action_pool_sunbed_idle.png" xpos 1093 ypos 330
            if actions_left > 44 or actions_left < 25:
                text "X" size 30 color "#cc0000" xpos 1103 ypos 333
            imagebutton idle "gui/action_pool_swim_idle.png" xpos 1138 ypos 330
            if mercedes.locations[actions_left-1] == "pool":
                imagebutton idle "gui/action_talk_lifeguard_idle.png" xpos 1183 ypos 330
        else:
            if actions_left > 44 or actions_left < 25:
                imagebutton auto "gui/action_pool_sunbed_%s.png" action NullAction() xpos 1093 ypos 330 hovered tt.Action ("It is not warm enough and there is not much sun. It wouldn't be relaxing!") focus_mask True
                text "X" size 30 color "#cc0000" xpos 1103 ypos 333
            else:
                imagebutton auto "gui/action_pool_sunbed_%s.png" action Return("do_pl_relax") xpos 1093 ypos 330 hovered tt.Action ("Relax a bit at the pool, enjoy the sun.") focus_mask True
            if player.trained_today == False and player.get_effect_state("hungry") <= 1 and player.get_effect_state("injured") <= 1:
                imagebutton auto "gui/action_pool_swim_%s.png" action Return("do_pl_endurance") xpos 1138 ypos 330 hovered tt.Action ("Swim to increase your endurance.") focus_mask True
            else:
                if player.get_effect_state("hungry") >= 2:
                    $ display_text = "You are too hungry for training. Eat something first."
                elif player.get_effect_state("injured") >= 2:
                    $ display_text = "You are too injured to swim. Get better first!"
                else:
                    $ display_text = "You already trained today."
                imagebutton auto "gui/action_pool_swim_%s.png" action NullAction() xpos 1138 ypos 330 hovered tt.Action (display_text) focus_mask True
                text "X" size 30 color "#cc0000" xpos 1148 ypos 333
            if mercedes.locations[actions_left-1] == "pool":
                if mercedes.get_action_allowed("pool_lifeguard_chat") == True:
                    if len(mercedes.get_scenes_not_seen("pool_chat")) == 0:
                        imagebutton auto "gui/action_talk_lifeguard_%s.png" action Return("do_pl_talk_pool_lifeguard_mercedes") tooltip ("03_Talk with Mercedes, the lifeguard at the pool") focus_mask True
                        add "gui/action_frame_green.png" alpha 0.7 xpos -43
                        null width -46
                    else:
                        imagebutton auto "gui/action_talk_lifeguard_%s.png" action Return("do_pl_talk_pool_lifeguard_mercedes") tooltip ("03_Talk with Mercedes, the lifeguard at the pool") hovered [SetVariable("g_achievements_hover", selected_char.get_scenes_not_seen("pool_chat")), Show("show_achievements")] unhovered Hide("show_achievements") focus_mask True
                else:
                    imagebutton auto "gui/action_talk_lifeguard_%s.png" action NullAction() tooltip ("03_You've talked with the lifeguard not long ago. Give her a break.") hovered [SetVariable("g_achievements_hover", []), Show("show_achievements")] focus_mask True
                    text "X" size 30 color "#cc0000" xpos 1193 ypos 333





screen pool_lifeguard:
    if mercedes.locations[actions_left-1] == "pool" and location == "pool":
        $ ll_tint = get_daytime_outdoor_tint(daytime)
        if menu_active == True:
            add im.MatrixColor("characters/Mercedes/Mercedes_pool_lifeguard.webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) zoom 0.5
        else:
            add im.MatrixColor("characters/Mercedes/Mercedes_pool_lifeguard.webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) zoom 0.5
            if mercedes.get_action_allowed("pool_lifeguard_chat") == True:
                if persistent.ui_show_open_achievements <> True or len(mercedes.get_scenes_not_seen("pool_chat")) == 0:
                    imagebutton hover im.Alpha(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5),0.01) idle im.Alpha(im.Grayscale(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5)),0.2) action Return("do_pl_talk_pool_lifeguard_mercedes") tooltip ("03_Talk with Mercedes, the lifeguard at the pool" + mercedes.get_scenes_not_seen_text("pool_chat")) hovered SetVariable("player.smart_watch_character", mercedes) unhovered SetVariable("player.smart_watch_character", no_char) focus_mask True
                else:
                    imagebutton hover im.Alpha(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5),0.01) idle im.Alpha(im.Grayscale(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5)),0.2) action Return("do_pl_talk_pool_lifeguard_mercedes") tooltip ("03_Talk with Mercedes, the lifeguard at the pool") hovered [SetVariable("player.smart_watch_character", mercedes), SetVariable("g_achievements_hover", mercedes.get_scenes_not_seen("pool_chat")), Show("show_achievements")] unhovered [SetVariable("player.smart_watch_character", no_char), Hide("show_achievements")] focus_mask True
            else:
                imagebutton hover im.Alpha(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5),0.01) idle im.Alpha(im.Grayscale(im.FactorScale("characters/Mercedes/Mercedes_pool_lifeguard.webp", 0.5)),0.2) action NullAction() hovered SetVariable("player.smart_watch_character", mercedes) tooltip ("03_You've talked with the lifeguard not long ago") focus_mask True unhovered SetVariable("player.smart_watch_character", no_char)




label action_pool_sunbed(char1, i_auto_succeed=False, i_intro=True):
    show screen main_game(location)
    $ menu_active = True
    $ option0 = True
    $ option1 = True
    $ option2 = True
    $ option3 = True
    $ option4 = True
    $ option5 = True

    if char1.get_action_allowed("pool_sunbed") == False and i_auto_succeed == False and i_intro == True:
        $ l_text = char1.get_action_not_allowed_text("pool_sunbed")
        char1.talk "[l_text]"
        pl "Sure, see you later!"
        jump action_pool_sunbed_end

    if char1.get_action_allowed("anger_block") == False and i_auto_succeed == False and i_intro == True:
        call action_closeup (char1, location, False, False) from _call_action_closeup_24
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("pool_sunbed", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    $ start_scene()
    if char1.id == brenda.id:
        call action_pool_sunbed_brenda (char1) from _call_action_pool_sunbed_brenda
        jump action_pool_sunbed_end
    elif char1.id == desire.id:
        call action_pool_sunbed_desire (char1) from _call_action_pool_sunbed_desire
        jump action_pool_sunbed_end
    elif char1.id == faye.id:
        call action_pool_sunbed_faye (char1) from _call_action_pool_sunbed_faye
        jump action_pool_sunbed_end
    elif char1.id == ivy.id:
        call action_pool_sunbed_ivy (char1) from _call_action_pool_sunbed_ivy
        jump action_pool_sunbed_end
    elif char1.id == yvette.id:
        call action_pool_sunbed_yvette (char1, i_intro=i_intro) from _call_action_pool_sunbed_yvette
        jump action_pool_sunbed_end

    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg")
    with fade
    if i_intro == True:
        pl "Hi [char1.fname]! Is it okay if I take the sun lounger beside you?"
        char1.talk "Sure [char1.playername], I'd love to have some company."
    $ char1.add_scene_seen("Pool_sunbed")

    $ char1.add_action_cooldown("pool_sunbed", actions_left, "We did that not long ago. Maybe we can do it again tomorrow?")
    label action_pool_sunbed_menu:
    if char1.id == brenda.id:
        call action_pool_sunbed_brenda_menu () from _call_action_pool_sunbed_brenda_menu
        jump action_pool_sunbed_end
    elif char1.id == desire.id:
        call action_pool_sunbed_desire_menu () from _call_action_pool_sunbed_desire_menu
        jump action_pool_sunbed_end
    elif char1.id == ivy.id:
        call action_pool_sunbed_ivy_menu () from _call_action_pool_sunbed_ivy_menu
        jump action_pool_sunbed_end
    elif char1.id == yvette.id:
        call action_pool_sunbed_yvette_menu () from _call_action_pool_sunbed_yvette_menu
        jump action_pool_sunbed_end
    menu:
        "Play game with [char1.fname]" if char1.id == alice.id and option0:#Parādās tikai tādā gadijumā, ja izvēlētā meitene ir Alise un līdz šim šodien netika spēlēta spēle
            $numbers= True
            $option0 = False
            $answer1=0
            $answer2=0
            $attempts_pool_alice = 0
            $correct_answers_pool_alice = 0
            pl "Guess, what number I made up?"
            $ num_input2 = renpy.input("Enter a number from 1 to 10", length=3)# Spēlētājs ievada skaitli no 1 līdz 10 
            while not num_input2.isdigit() and num_input2<1 or num_input2>10 :#Tiek pārbaudīts vai ir derīgs ievadītais simbols
                "Please enter a number from 1 to 10"
                $ num_input2 = renpy.input("Enter a number from 1 to 10", length=3)
            $num_input2 = int(num_input2)
            while attempts_pool_alice < 3 and correct_answers_pool_alice < 1:#Spēle beidzas, kad meitene iztērē 3 iespējas vai uzmina skaitli
                $new_rand = renpy.random.randint(1, 10)#Meitene min skaitļus ar nejaušo skaitļu no 1 līdz 10 palīdzību
                while numbers==True:#Tiek pārbaudīts, lai meitene neatkārto skaitļus
                    $new_rand = renpy.random.randint(1, 10)
                    if new_rand != answer1 and new_rand != answer2:
                        $numbers = False
                $numbers=True
                char1.talk"Hmmm, your number is [new_rand]?"# Meitene saka savu atbildes variantu
                if  num_input2 == new_rand:# ja tiek uzminēts skaitlis tiek 
                    $correct_answers_pool_alice +=1
                    $attempts_pool_alice +=1
                else:#ja skaitlis netiek uznimēts, tad tas tiek padots mainīgajos nakamajai salīdzināšanai
                    if attempts_pool_alice==0:
                        $answer1= new_rand
                    elif attempts_pool_alice==1:
                        $answer2= new_rand
                    $attempts_pool_alice +=1
                    pl"You are wrong! "
                    char1.talk"Your [attempts_pool_alice]/3 attempts."
            if correct_answers_pool_alice == 1:#Meitene ir uzminējusi skaitli un viņu apsveic ar uzvaru
                "Congratulations, you guessed it"
            else:#Meitene ir neuzminējusi skaitli un spēlētājam parādās izvēlne ar sižeta turpinājumiem 
                char1.talk "Сhoose what you want to do?"
                menu:
                    "Сontinue in the pool":
                        $char1.swimwear = 0#Meitene nomaina apģērbu, lai viss būtu pēc sižeta
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_jump_in1_swim[char1.swimwear].jpg") with dissolve#tiek parādīts skats, kurš atrodas pa šo ceļu
                        menu:
                            "Reproach her for splashing":
                                $ char1.change_anger(5)#Tiek mainītas vērtības meiteņu rakstura īpašībām atticīgi vērtībām iekavās
                                $ char1.change_lust(-25)
                                $ char1.change_love(-10)
                                char1.talk"Why are you being so rude?"
                                menu:
                                    "I'm not in the mood":
                                        char1.talk"I'm sorry if I offended you."
                                    "It's okay, it was a joke.":
                                        char1.talk"Okay, but don't joke so I can be offended."
                                        $ char1.change_anger(-3)
                                        $ char1.change_lust(15)
                                        $ char1.change_love(5)
                            "Wow, you jumped beautifully.":
                                $ char1.change_anger(-10)
                                $ char1.change_lust(20)
                                $ char1.change_love(10)
                                char1.talk"Thank you for inviting me to swim, I just didn't want to go alone."
                                menu:
                                    "I'm always in favor of swimming with a beautiful girl like you":
                                        char1.talk"Thank you for the compliment."
                                    "I propose to every girl, you are not special":
                                        char1.talk"Everything is clear with you"
                                        $ char1.change_lust(-10)
                                        $ char1.change_love(-5)
                        scene expression("scenes/[char1.fname]/[char1.fname]_pool_play_swim[char1.swimwear].jpg") with dissolve:#dissolve uztaisa gludu pāreju no viena skata uz otru
                            pause 1.0#Tiek uztaisīta pauze pirms turpina darboties kods
                        char1.talk"Do you like my swimsuit?"
                        menu:
                            "Yes, sure":
                                char1.talk"You won't believe it, but I'm very pleased"
                                $ char1.change_lust(15)
                                $ char1.change_love(7)
                            "it's ugly please change your clothes":
                                char1.talk"Ok, wait a few seconds"
                                $char1.swimwear=1#Meitene parģerbjas uzvelk citu peldkostīmu
                                pause 1.5
                                char1.talk"Is this swimsuit better?"
                                pl"Yes, you look great in it"
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play1_swim[char1.swimwear].jpg") with dissolve:
                            pause 0.5
                        menu:
                            "Throw her into the water":
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play2_swim[char1.swimwear].jpg") with dissolve:
                                    pause 0.6
                                pl"HAHAHAHAHA"
                            "Put her in the water":
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play3_swim[char1.swimwear].jpg") with dissolve 
                                char1.talk"Why did you do this, put me back?"
                                if char1.lust > 70 and int(char1.rsm[0].love)>55:#Tiek pārbaudītas mīletības un karības vērtības
                                    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play9_swim[char1.swimwear].jpg") with dissolve
                                    pl"You are beautiful"
                        pl"We can go back to the sunbed."
                        char1.talk"Of course"
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_exit1_swim[char1.swimwear].jpg") with dissolve:
                            pause 1.0
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg")
                    "Continue in the pool with a surprise":
                        $char1.swimwear = 2#Meitene parģerbjas uzvelk citu peldkostīmu
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_jump_in1_swim[char1.swimwear].jpg") with dissolve
                        char1.talk"I changed my clothes to surprise you."
                        menu:
                            "Why did you jump so hard?":
                                char1.talk"I'm sorry, I didn't mean to spray you."
                                pause 1.5
                                $ player.change_anger(5)
                                $ player.change_lust(-25)
                                $ player.change_love(-10)
                                char1.talk"What can I do to make you forgive me?"
                                menu:
                                    "It's better not to do anything.":
                                        $ char1.change_lust(-15)
                                        $ char1.change_love(-7)
                                    "It's okay, it was a joke.":
                                        char1.talk"Okay, but don't joke so I can be offended."
                                        $ char1.change_anger(-3)
                                        $ char1.change_lust(15)
                                        $ char1.change_love(5)
                            "Wow, you jumped beautifully.":
                                $ char1.change_anger(-10)
                                $ char1.change_lust(20)
                                $ char1.change_love(10)
                                char1.talk"Thank you for inviting me to swim, I just didn't want to go alone."
                                menu:
                                    "I'm always in favor of swimming with a beautiful girl like you":
                                        char1.talk"Thank you for the compliment."
                                    "I propose to every girl, you are not special":
                                        char1.talk"Everything is clear with you"
                                        $ char1.change_lust(-15)
                                        $ char1.change_love(-10)
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play_swim[char1.swimwear].jpg") with dissolve:
                            pause 1.0
                        char1.talk"Do you like my swimsuit?"
                        menu:
                            "Yes, sure":
                                char1.talk"Was that sarcasm?"
                                pl"No"
                                $ char1.change_lust(15)
                                $ char1.change_love(7)
                            "You look great in this swimsuit.":
                                char1.talk"That's so sweet of you."
                                pause 1.5
                                pl"Can I take you for a ride?"
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play1_swim[char1.swimwear].jpg") with dissolve
                        char1.talk"Yeah"
                        char1.talk"Although it's better not to, I don't feel confident."
                        pl"Everything will be fine, don't worry."
                        char1.talk"I'm afraid of falling into the water"
                        menu:
                            "Throw her into the water":
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play2_swim[char1.swimwear].jpg") with dissolve:
                                    pause 0.5
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play3_swim[char1.swimwear].jpg") with dissolve
                                char1.talk"What happened?"
                                pl"Wow, everything is very good, I like this surprise"
                            "Throw her into the water a little later":
                                pl"You said something about a surprise"
                                char1.talk"Oh, yes, I completely forgot, throw me into the water"
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play2_swim[char1.swimwear].jpg") with dissolve:
                                    pause 0.5
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play3_swim[char1.swimwear].jpg") with dissolve
                                pl"Wow, everything is very good, I like this surprise"
                        
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play9_swim[char1.swimwear].jpg") with dissolve
                        pl"We can go back to the sunbed."
                        char1.talk"Of course"
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_exit1_swim[char1.swimwear].jpg") with dissolve
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg")
                    "Continue here":
                        $char1.swimwear = 2#Meitene parģerbjas uzvelk citu peldkostīmu
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose2_swim[char1.swimwear].jpg") with dissolve
                        char1.talk"I changed my swimsuit so we could continue"
                        menu:
                            "Wow, how sexy you look":
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose3_swim[char1.swimwear].jpg") with dissolve:
                                    pause 1.0
                                $ char1.change_lust(15)
                                $ char1.change_love(15)
                                pl"Wow!!!"
                            "Are you in the mood?" if char1.check_affection(2) == True:#parbauda vai ir sasniegts otrais mīlestības limenis
                                char1.talk"Yes, of course"
                                $ char1.change_lust(10)
                                $ char1.change_love(10)
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose4_swim[char1.swimwear].jpg") with dissolve
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg")
                    "Continue here with surprise":
                        $answer = renpy.random.randint(1, 10)
                        $char1.swimwear = 1#Meitene parģerbjas uzvelk citu peldkostīmu
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose2_swim[char1.swimwear].jpg") with dissolve
                        char1.talk"I changed my clothes to surprise you."
                        
                        if int(char1.rsm[0].affection>80):#Tiek pārbaudīta simpātijas vērtībaun ja tā ir lielāka par 80, tad  
                            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose3_swim[char1.swimwear].jpg") with dissolve
                        char1.talk"Do you want a surprise?"
                        menu:
                            "Yes, of course":
                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose4_swim[char1.swimwear].jpg") with dissolve
                                Char1.talk"You are ready?"
                                if answer>3:
                                    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose5_swim[char1.swimwear].jpg") with dissolve
                                menu:
                                    "Wow, I like your surprise":
                                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg") with dissolve:
                                            pause 1.5 
                                        char1.talk"Can I kiss you?"
                                        $answer = renpy.random.randint(1, 10)
                                        menu:
                                            "Yes, let's do":
                                                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose10_swim[char1.swimwear].jpg") with dissolve
                                                pl"I will never forget this moment"
                                            "Let's do it next time" if answer>5 and player.lust<95:
                                                char1.talk"So sad to hear"
                                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose10_swim[char1.swimwear].jpg") with dissolve
                                    "Please get dressed, I didn't expect such surprises to await me":
                                        char1.talk"Sorry, I thought you'd like me"
                                
                            "No, i'm not in the mood today" if player.lust<70:#izvēles variants parādās tikai tad, ja spēlētāja kārība ir zem 70
                                char1.talk"Ok, then another time"
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg") with dissolve
        "Chat with [char1.fname]" if option1:
            $ option1 = False
            pl "How was your day so far?"
            char1.talk "Nothing spectacular, just hanging out and relaxing,\nlike most days on the island."
            char1.talk "How was yours?"
            menu:
                "Tell her it was ok" if True:
                    pl "Thanks for asking pretty much the same as yours.\nVery relaxing. I like it here."
                    char1.talk "So maybe it gets a little more interesting for the both of us now. *smiles*"
                    $ char1.change_affection(4)
                "Try to be charming" if True:

                    if player.check_charm(2) == True:
                        pl "Until now it was ok. But it looks like it's gonna be great now. *smiles*"
                        char1.talk "You are quite the charmer [char1.playername]. I like that. *smiles back*"
                        call change_char_max_affection (char1, 5) from _call_change_char_max_affection_8
                        $ char1.change_affection(8)
                        pl "I meant every word of it."
                    elif True:
                        pl "I like it here, there are so many cute girls on the island."
                        $ char1.change_affection(-8)
                        char1.talk "So you would rather be with someone else right now?"
                        pl "Uhmm no, that's not what I meant..."
                        char1.talk "*sulks*"
                        "Damn that didn't come out right..."

        "Ask her if she needs some sun lotion applied to her back" if option2 and char1.get_action_icon_available("pool_sunlotion"):
            $ option2 = False
            pl "[char1.fname], would you like me to apply some sun lotion to your back?"
            if char1.get_action_icon_available("pool_sunlotion_right_swimsuit") == False:
                char1.talk "With another outfit maybe. I don't want to have the lotion smeared all over my swimsuit."
                jump action_pool_sunbed_menu

            if char1.get_action_allowed("sunlotion") == False:
                char1.talk "Thanks for asking, but it's not necessary right now. It's still fresh enough."
            elif True:
                if player.check_charm(2) == True or char1.check_affection(2) == True:
                    char1.talk "Thanks for asking [char1.playername]. I'm burning up, so yes please."
                    call action_pool_sunbed_lotion (char1, False) from _call_action_pool_sunbed_lotion_1
                    if _return == False:
                        $ start_scene()
                        jump action_pool_sunbed_end
                    elif True:
                        $ start_scene()
                        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_swim[char1.swimwear].jpg")
                        with fade
                        pause 0.4
                elif True:
                    char1.talk "Don't worry [char1.playername], I already did that."

        "Ask her to pose for you" if option3 and char1.get_action_icon_available("pool_sunbed_pose", True):
            $ option3 = False
            pl "Would you strike some poses for me?"
            pl "I'd really love to see that!"
            if char1.get_action_icon_available("pool_sunbed_pose") == False:
                char1.talk "*smiles* Maybe, but not in my current outfit."
                jump action_pool_sunbed_menu
            if char1.check_affection(2, 0, False) == True and char1.check_love(1, 0, False) == True:
                if char1.id <> heather.id:
                    char1.talk "Sure, I'd be happy to do that for you."
                call action_pool_sunbed_pose (char1) from _call_action_pool_sunbed_pose
                if _return == "jump_menu":
                    jump action_pool_sunbed_menu
                elif _return == "goto_player_room":
                    $ location_detail = ""
                    $ menu_active = False
                    $ location = "player_room"
                    $ stop_scene()
                    if not option1 or not option2 or not option3 or not option4:
                        $ actions_used += 1
                        $ char1.add_pl_interaction("others")
                    return "goto_player_room"
                jump action_pool_sunbed_end

            call check_favor (char1, 20) from _call_check_favor
            if _return == True:
                char1.talk "Great, so here we go."
                call action_pool_sunbed_pose (char1) from _call_action_pool_sunbed_pose_2
                if _return == "jump_menu":
                    jump action_pool_sunbed_menu
                elif _return == "goto_player_room":
                    $ location_detail = ""
                    $ menu_active = False
                    $ location = "player_room"
                    $ stop_scene()
                    if not option1 or not option2 or not option3 or not option4:
                        $ actions_used += 1
                        $ char1.add_pl_interaction("others")
                    return "goto_player_room"
                jump action_pool_sunbed_end
            elif True:
                if char1.rsm[0].favor >= 20:
                    char1.talk "It's your loss. *smirks*"
                elif True:
                    char1.talk "I don't know, maybe later when we know each other a little better."

        "Tell her that she looks sexy on the sunbed" if option4:
            $ option4 = False
            pl "[char1.fname], you look striking and very sexy on that sunbed."
            if player.check_charm(2) == True or char1.check_tease_sexual(1, 0, False) == True:
                char1.talk "*smiles* You are sweet [char1.playername]. Thank you."
                call change_char_max_affection (char1, 5) from _call_change_char_max_affection_9
                $ char1.change_affection(5)
            elif True:
                char1.talk "*frowns* I hope for your sake that you can do better than that [char1.playername]."
                $ char1.change_affection(-5)

        "Talk to [char1.fname] about her teenager photos" if option5 and char1.id == aly.id and player.get_quest_state("Aly_breast_development",char1) >= 1 and player.get_quest_state("Aly_breast_development",char1) < 100:
            $ option5 = False
            if player.get_quest_state("Aly_breast_development",char1) == 1:
                pl "Ummm... [char1.fname]..."
                char1.talk "What's up [char1.playername]?"
                pl "You sent me this nice picture wearing your winter clothes after your 16th birthday."
                pl "I really like it."
                pl "Do you happen to have another one you'd be willing to share, maybe one from spring time?"
                if char1.check_affection(2, 0, False) == False or char1.check_love(1, 0, False) == False:
                    char1.talk "Sorry, but I'm not comfortable doing that right now."
                    char1.talk "Maybe when we know each other a little better, okay?"
                    pl "Sure [char1.fname], whenever you're ready."
                    jump action_pool_sunbed_menu
                if char1.get_action_allowed("Aly_breast_development") == False:
                    char1.talk "I've send you the first one not long ago. Maybe ask me later, okay?"
                    pl "Sure."
                    jump action_pool_sunbed_menu
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose5_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                char1.talk "Soooo... You want to have another one..."
                char1.talk "Since you're really cute and I like you, I will check if I can find something nice on my phone. *smiles*"
                pl "Thank you very much."
                char1.talk "It's my pleasure and I'm pretty sure it's gonna be yours too. *smirks*"
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose5_swim[char1.swimwear].jpg") with dissolve
                $ aly.add_queued_sexting(501,502,6)
                $ player.inc_quest_state("Aly_breast_development",aly)
                $ char1.add_action_cooldown("Aly_breast_development", 30)
                char1.talk "Anything else you want to do?"
                jump action_pool_sunbed_menu

            elif player.get_quest_state("Aly_breast_development",char1) == 2:
                pl "Ummm... [char1.fname], I really adored the spring image you shared with me."
                pl "The jean shorts you're wearing look incredible on you."
                pl "I'm loving your story about your breast development. Could I see a bikini picture from that time."
                if char1.get_action_allowed("Aly_breast_development") == False:
                    char1.talk "I've send you the spring picture not long ago. Ask me later, okay?"
                    pl "Will do."
                    jump action_pool_sunbed_menu
                char1.talk "Okay [char1.playername]."
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                char1.talk "If you do something for me too."
                pl "Sure [char1.fname], what is it?"
                char1.talk "I love black roses, but unfortunately they're very hard to come by."
                char1.talk "Especially here on the island."
                char1.talk "If you find one for me, I will send you the bikini picture you asked for. *smiles*"
                pl "Ohhh... Okay. I will try to get one."
                "Hmmmm... You have no idea where to get one of those black roses."
                "You should ask Jennifer. She seems to know a lot about how to get {i}stuff{/i}... Maybe she has an idea."
                $ player.inc_quest_state("Aly_breast_development",aly)
                $ char1.add_action_cooldown("Aly_breast_development", 30)
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                char1.talk "Anything else you want to talk about?"
                jump action_pool_sunbed_menu

            elif player.get_quest_state("Aly_breast_development",char1) == 12:
                pl "I hope you don't mind me saying that the bikini pool pic was super hot."
                pl "Since you were only 16 when it was taken."
                char1.talk "Don't worry about it. I know I look damn hot in that one. *smiles*"
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose8_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                char1.talk "Even though my breasts were still relatively small compared to my current size."
                char1.talk "They were already quite impressive. *smirks*"
                pl "Yeah, absolutely. *smiling sheepishly*"
                pl "I wanted to ask you if you'd be willing to send me one from your 18th birthday, or shortly after?"
                if char1.check_love(3, 0 , False) == False:
                    char1.talk "Sorry, but I'm not comfortable doing that right now."
                    char1.talk "I only want to share private images like that with someone really special to me."
                    char1.talk "Not that I don't like you [char1.playername]."
                    char1.talk "But we're not quite there yet."
                    pl "Sure [char1.fname], I understand. I hope you change your mind one day."
                    char1.talk "That's up to you too. *smiles*"
                    jump action_pool_sunbed_menu

                if char1.get_action_allowed("Aly_breast_development") == False:
                    char1.talk "I sent you the last picture not long ago. Maybe ask me later, okay?"
                    pl "Yes."
                    jump action_pool_sunbed_menu

                char1.talk "I bet you're hoping for something really hot..."
                char1.talk "...since you're asking for a picture after my 18th birthday."
                pl "Not at all [char1.fname]. Anything you're comfortable sharing."
                pause 0.4
                pl "Although I'd love to see you in lingerie."
                pl "I'm just curious to see how gorgeous [char1.fname] looked when she was 18. *smiling*"
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose3_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                char1.talk "Yeah I bet and me having incredible {b}H cup{/b} breasts probably doesn't hurt either. *winks*"
                pl "Ummm... I guess not."
                char1.talk "I'm pretty sure I can find something to your liking. *smiles*"
                pl "Thank you!"
                $ aly.add_queued_sexting(503,504,8)
                $ player.inc_quest_state("Aly_breast_development",aly)
                $ char1.add_action_cooldown("Aly_breast_development", 30)
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose3_swim[char1.swimwear].jpg")
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose8_swim[char1.swimwear].jpg")
                with dissolve
                pause 0.8
                char1.talk "Anything else you want to talk about?"
                jump action_pool_sunbed_menu

            elif player.get_quest_state("Aly_breast_development",char1) == 13:
                pl "Oh my God [char1.fname]! The picture wearing the light blue lingerie was incredible!"
                char1.talk "I thought you might like it. *smiles*"
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg") with dissolve
                pause 0.7
                pl "Definitely!"
                pl "Thanks again for letting me see it."
                char1.talk "You're welcome [char1.playername]."
                char1.talk "I have another one wearing the same lingerie."
                pause 0.4
                char1.talk "Well, maybe not really completely wearing it any more... *giggles*"
                if char1.get_action_allowed("Aly_breast_development") == False:
                    char1.talk "Since it was long ago that I've send you the first lingerie pic..."
                    char1.talk "Let's talk about what I'd like to have in exchange for sending it to you later, okay?"
                    pl "Sure [char1.fname]."
                    "You wonder about the picture and also about what she wants you to do for it."
                    char1.talk "Anything else you want to talk about?"
                    jump action_pool_sunbed_menu

                pl "*Hmpf* What?"
                char1.talk "Yeah well you know, this lingerie isn't made to stay on forever..."
                pl "Yeah, I guess..."
                pause 0.4
                pl "Ummm... [char1.fname]?"
                pause 0.2
                pl "What would you have me do to send me that picture?"
                char1.talk "Let me think about it for a moment..."
                $ l_cur_gold = char1.get_number_of_trophies(1, "W")
                $ l_all_gold = char1.get_number_of_trophies(1, "T")
                pause 0.5
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg")
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose8_swim[char1.swimwear].jpg")
                with dissolve
                pause 0.8
                char1.talk "Well you know..."
                pause 0.3
                char1.talk "I really like those trophies."
                if l_cur_gold < 2:
                    char1.talk "If you help me get at least three of the current gold trophies..."
                    char1.talk "...the picture is all yours!"
                    pause 0.5
                    char1.talk "Do we have a deal?"
                    pl "Yes! I will see what I can do. But I might need your help with one or two of them."
                    char1.talk "Just get me in the right mood and I'm sure it will all work out!"
                    $ player.set_quest_state("Aly_breast_development", aly, 14)
                elif True:
                    if l_all_gold == 0:
                        char1.talk "If you help me get at least two of the all time gold trophies..."
                        char1.talk "...the picture is all yours!"
                        pause 0.5
                        char1.talk "Do we have a deal?"
                        pl "Yes! I will see what I can do. But I might need your help with those."
                        char1.talk "Just get me in the right mood and I'm sure it will all work out!"
                        $ player.set_quest_state("Aly_breast_development", aly, 15)
                    elif True:
                        char1.talk "If you help me get at least three of the all time gold trophies..."
                        char1.talk "...the picture is all yours!"
                        pause 0.5
                        char1.talk "Do we have a deal?"
                        pl "Yes! I will see what I can do. But I might need your help with one or two of them."
                        char1.talk "Just get me in the right mood and I'm sure it will all work out!"
                        $ player.set_quest_state("Aly_breast_development", aly, 16)
                "Oh wow! This shouldn't be too hard..."
                "...but it might take some time *musing*"
                char1.talk "Just let me know when you think the trophies are all there. *smiles*"
                pl "Okay, will do."
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose8_swim[char1.swimwear].jpg")
                with dissolve
                pause 0.8
                char1.talk "Anything else you want to talk about?"
                jump action_pool_sunbed_menu

            elif player.get_quest_state("Aly_breast_development",char1) == 14 or player.get_quest_state("Aly_breast_development",char1) == 15 or player.get_quest_state("Aly_breast_development",char1) == 16:
                pl "You should have all the required trophies now."
                if char1.get_action_allowed("Aly_breast_development") == False:
                    char1.talk "I've just checked not long ago and I didn't have them yet."
                    char1.talk "Please ask me again a little later, okay."
                    pl "Ummm... Yeah sure."
                    char1.talk "Anything else you want to talk about?"
                    jump action_pool_sunbed_menu
                char1.talk "Let me check my phone for a moment..."
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg") with dissolve
                pause 1.2
                if player.get_quest_state("Aly_breast_development",char1) == 14:
                    $ l_req_level = 3
                    $ l_has_level = char1.get_number_of_trophies(1, "W")
                    if l_has_level < l_req_level:
                        char1.talk "I asked you to get me at least [l_req_level] current/weekly gold trophies."
                elif player.get_quest_state("Aly_breast_development",char1) == 15:
                    $ l_req_level = 2
                    $ l_has_level = char1.get_number_of_trophies(1, "T")
                    if l_has_level < l_req_level:
                        char1.talk "I asked you to get me at least [l_req_level] all time gold trophies."
                elif player.get_quest_state("Aly_breast_development",char1) == 16:
                    $ l_req_level = 3
                    $ l_has_level = char1.get_number_of_trophies(1, "T")
                    if l_has_level < l_req_level:
                        char1.talk "I asked you to get me at least [l_req_level] all time gold trophies."
                if l_has_level < l_req_level:
                    char1.talk "You've only helped me get [l_has_level] so far."
                    pl "Oh... Sorry."
                    char1.talk "No need to be sorry, but I won't send you the picture yet."
                    hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg")
                    with dissolve
                    pause 0.8
                    char1.talk "Anything else you want to talk about?"
                    jump action_pool_sunbed_menu
                char1.talk "Wow [char1.playername]!"
                char1.talk "Thank you. You really did it!"
                char1.talk "I just love those trophies."
                pause 0.5
                char1.talk "I'll send you the picture as soon as I have some private time."
                $ aly.add_queued_sexting(504,505,2)
                $ player.set_quest_state("Aly_breast_development", aly, 100)
                pl "Thank you!"
                char1.talk "Oh... You might want to check it when you're alone in your room... *giggles*"
                char1.talk "Just in case..."
                pl "Ummm... Okay..."
                hide expression ("scenes/[char1.fname]/[char1.fname]_pool_sunbed_pose6_swim[char1.swimwear].jpg")
                with dissolve
                pause 0.8
                char1.talk "Anything else you want to talk about?"
                jump action_pool_sunbed_menu
            elif True:

                char1.talk "I've already told you what you need to do."
                "Check the quest app to see the next step you need to do in order to make progress in getting another photo from her."
                jump action_pool_sunbed_menu
        "Tell her you have to leave now" if True:

            pl "I am very sorry [char1.fname], but I have to leave now."
            char1.talk "No problem, I'll work on my tan for a bit. See you later, [char1.playername]. *smiles*"
            jump action_pool_sunbed_end

    jump action_pool_sunbed_menu

    label action_pool_sunbed_end:
    if not option1 or not option2 or not option3 or not option4:
        $ actions_used += 1
        $ char1.add_pl_interaction("others")
    $ menu_active = False
    $ stop_scene()
    return "do_return"





label action_pool_sunbed_pose(char1):
    $ menu_active = True
    $ l_left_menu_hidden = g_left_menu_hidden
    $ g_left_menu_hidden = True
    $ start_scene()

    if char1.id==faye.id:
        call action_pool_sunbed_pose_faye (char1) from _call_action_pool_sunbed_pose_faye
    elif char1.id==amy.id:
        call action_pool_sunbed_pose_amy (char1) from _call_action_pool_sunbed_pose_amy
    elif char1.id==yvette.id and char1.swimwear == 1:
        call action_pool_sunbed_pose_yvette (char1) from _call_action_pool_sunbed_pose_yvette
    elif char1.id==yvette.id and char1.swimwear == 2:
        call action_pool_sunbed_pose2_yvette (char1) from _call_action_pool_sunbed_pose2_yvette
    elif char1.id==alice.id:
        call action_pool_sunbed_pose_alice (char1) from _call_action_pool_sunbed_pose_alice
    elif char1.id==jessica.id:
        call action_pool_sunbed_pose_jessica (char1) from _call_action_pool_sunbed_pose_jessica
    elif char1.id==ivy.id:
        call action_pool_sunbed_pose_ivy (char1) from _call_action_pool_sunbed_pose_ivy
    elif char1.id==aly.id:
        call action_pool_sunbed_pose_aly (char1) from _call_action_pool_sunbed_pose_aly
    elif char1.id==heather.id:
        call action_pool_sunbed_pose_heather (char1) from _call_action_pool_sunbed_pose_heather
    elif char1.id==desire.id:
        call action_pool_sunbed_pose_desire (char1) from _call_action_pool_sunbed_pose_desire
    elif char1.id==brenda.id:
        call action_pool_sunbed_pose_brenda (char1) from _call_action_pool_sunbed_pose_brenda

    if _return <> "jump_menu":
        $ special_id = ""
        $ menu_active = False
        scene onlayer master
        $ g_left_menu_hidden = l_left_menu_hidden
        $ stop_scene()
    return _return





label action_pool_sunbed_lotion(char1, i_intro=False, i_check=True):
    $ ll_tint = get_daytime_outdoor_tint(daytime)
    $ l_good_terms = True
    $ menu_active = True
    $ l_left_menu_hidden = g_left_menu_hidden
    $ g_left_menu_hidden = True
    call create_list_of_chars_display () from _call_create_list_of_chars_display_2
    $ l_breast_size_text = char1.get_breast_size_text()
    $ start_scene()

    if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_sunlotion0_swim" + unicode(char1.swimwear) + ".webp"):
        scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_sunlotion0_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
            zoom 0.5
    elif True:
        scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion0_swim[char1.swimwear].jpg")
    with dissolve

    if i_intro == True:
        char1.talk "Oh hi [char1.playername]. I'm so glad to see you. Could you lotion my back, I'm burning up."
        pause 1.0
        "Oh shit, look at her [l_breast_size_text] and those shapely legs."
        menu:
            "Agree to lotion her back." if True:
                pl "Sure [char1.fname], no trouble at all."
            "Politely tell her that now is not a good time." if True:

                pl "Sorry [char1.fname], but I don't have much time right now. Maybe later?"
                if char1.check_affection(3, 0, False) == True or renpy.random.randint(1,10) <= 5:
                    char1.talk "Sure, no problem. See you later!"
                elif True:
                    char1.talk "You're really gonna let me get sunburn..."
                    pause 0.5
                    char1.talk "Pfff..."
                    $ char1.change_affection(-6)
                    pl "Sorry, but I've got to go..."
                $ action_initiative = ""
                $ initiative_char = no_char
                $ menu_active = False
                $ stop_scene()
                $ g_left_menu_hidden = l_left_menu_hidden
                return True

    if char1.id == jessica.id:
        call action_pool_sunbed_lotion_jessica (char1) from _call_action_pool_sunbed_lotion_jessica
        jump action_pool_sunbed_lotion_end
    elif char1.id == faye.id:
        call action_pool_sunbed_lotion_faye (char1) from _call_action_pool_sunbed_lotion_faye
        jump action_pool_sunbed_lotion_end

    if i_intro == False and i_check == True:
        char1.talk "Let me turn around..."
        pause 0.4
        "Oh shit, look at her [l_breast_size_text] and those shapely legs."
        pl "Sure [char1.fname], no trouble at all. Let me move your hair out of the way."
    elif i_intro == False and i_check == False:
        pl "Let me move your hair out of the way."

    $ char1.add_scene_seen("Pool_lotion")
    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion1_swim[char1.swimwear].jpg") with dissolve
    pause 1.0
    "You begin to rub the lotion into her back..."
    pause 0.4
    char1.talk "Thank you for saving my back. Already feels much cooler."
    pl "Anytime!"
    pause 0.5
    pl "Okay, almost done..."
    pause 0.4
    if char1.id == yvette.id and char1.swimwear == 2:
        menu:
            "Ask her to take off her bikini top to better lotion her back" if True:
                jump action_pool_sunbed_lotion_no_bra
            "Rub the lotion into her butt" if True:

                jump action_pool_sunbed_lotion_butt

    label action_pool_sunbed_lotion_no_bra:
    pl "I could distribute it more evenly if you open your bra for a moment."
    if i_check == True and char1.check_affection(2,0,False) == False:
        char1.talk "That's not necessary right now, but thanks for asking."
        pl "Ok sure. Enjoy your sunbath."
        char1.talk "I will. *smiles*"
        jump action_pool_sunbed_lotion_end

    $ char1.add_action_cooldown("sunlotion", 8, "That's not necessary right now, but thanks for asking.")
    pause 0.6
    char1.talk "Right, I better take it off. I don't want to have sun lotion smeared all over it."
    show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion2_swim[char1.swimwear].jpg") with fade
    pause 1.0
    "Wow, look at those squeezed titties. You really want to touch them."
    $ player.change_lust(char1.sexiness)
    menu:
        "Use the lotion on her back." if True:
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion4_swim[char1.swimwear].jpg") with dissolve
            pause 1.0
            "You rub the lotion on her exposed back."
            pl "Now all should be well taken care off."
            char1.talk "Thank you very much, you're the best."
            $ char1.change_anger(-5)
            $ char1.change_favor(8)
            pl "No problem, enjoy your sunbath."
            jump action_pool_sunbed_lotion_end
        "Rub the lotion on her exposed side boobs." if True:

            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion4_swim[char1.swimwear].jpg") with dissolve
            pause 0.3
            "You start with her back and continue rubbing the lotion into her breasts..."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion3_swim[char1.swimwear].jpg") with dissolve
            pause 0.4
            "Giving her tits a good squeeze in the process."
            char1.talk "Hey, [char1.playername] what do you think you are doing???"
            if player.check_charm(3) == True:
                pl "Was I too rough? I apologize."
                pause 0.3
                pl "Just wanted to make sure you don't get sunburn."
                "She slowly pushes her head and chest up from the lounger,\nlooking you straight in the eye."
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion5_swim[char1.swimwear].jpg") with dissolve
                pause 1.0
                char1.talk "*smirks* If this was a trick to get a rise out of me, it worked."
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion6_swim[char1.swimwear].jpg") with dissolve
                pause 1.0
                "Wow, she really has a nice pair of tits."
                pause 0.5
                char1.talk "Okay, you had your fun. Let's just relax a bit."
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion6_swim[char1.swimwear].jpg"):
                    zoom 1.0
                    subpixel True
                    linear 1.0 zoom 2.0 xpos -500 ypos -300
                pause 1.5
                "You can't help but take a closer look at her exposed tits."
                $ player.change_lust(10)
                pl "Sure [char1.fname]. If you need another dose of sun lotion, let me know."
                char1.talk "Don't push it [char1.playername]!"
                jump action_pool_sunbed_lotion_end
            elif True:

                pl "Uhmmm... making sure everything is well rubbed..."
                char1.talk "Stop that {b}right now!{/b}"
                "She slowly pushes her head and chest up from the lounger,\nlooking you straight in the eye."
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion6_swim[char1.swimwear].jpg") with dissolve
                pause 1.0
                char1.talk "You had your fun, now leave me alone."
                "I guess the sight of her exposed tits is almost worth her anger."
                $ char1.change_anger(20)
                $ char1.change_affection(-10)
                "You decide you'd better leave her alone for the moment."
                $ l_good_terms = False
                jump action_pool_sunbed_lotion_end


    label action_pool_sunbed_lotion_butt:
    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion11_swim[char1.swimwear].jpg") with dissolve
    "You start rubbing the remainder of the lotion into her butt."
    pl "Almost done [char1.fname]. Just a little left."
    char1.talk "Great, thanks for taking care of all my exposed parts. *giggles*"
    scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion12_swim[char1.swimwear].jpg") with dissolve
    "You can't help yourself but stare at her perfect butt for a moment."
    pause 1.0
    "Before you..."
    menu:
        "...answer that all has been rubbed in now." if True:
            pl "Now you are good to enjoy the sun for another hour or two."
            pl "If you need another dose of sun lotion, let me know."
            char1.talk "Thanks [char1.playername], I will take you up on that."
        "...move your hand further down and lotion her inner thighs." if True:

            "You slowly move your hand from her butt towards her inner thighs and start rubbing some more lotion."
            show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion7_swim[char1.swimwear].jpg"):
                alpha 0.0
                linear 1.0 alpha 1.0
            pause 1.5
            if char1.check_tease_sexual(3) == True:
                char1.talk "*moans* Hmmmm... What are you doing... *uhmmm* *mhhhhh*"
                "This really is turning her on..."
                "When you move your fingers towards her pussy,\nshe is already moving rhythmically and pressing her pussy into the lounger and your hand..."
                scene onlayer master
                show pool_sunlotion_animate1:
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8a_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.4
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.4
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8c_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.4
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.4
                    repeat
                pause 2.0
                char1.talk "*hmmmmm* Don't stop... This feels great.. *hmmmmm*"
                pause 2.0
                char1.talk "*hmmmm* *hmmmmmmmm* Harder, harder..."
                "You push two fingers inside her wet pussy and massage her clit..."
                scene onlayer master
                show pool_sunlotion_animate2:
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8a_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.25
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.25
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8c_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.25
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.25
                    repeat
                pause 2.0
                char1.talk "{b}Yes, yes{/b} almost there, harder... *hmmmmm*"
                "She rams her pussy into your hand and the lounger...\nYou wonder how long she can last like that..."
                scene onlayer master
                show pool_sunlotion_animate2:
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8a_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.15
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.15
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8c_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.15
                    "scenes/" + char1.fname + "/" + char1.fname + "_pool_sunlotion8b_swim" + unicode(char1.swimwear) + ".jpg"
                    pause 0.15
                    repeat
                pause 2.0
                char1.talk "Yes, OMG I am cummmmminnnnnggg..."
                $ char1.change_lust(-50)
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion7_swim[char1.swimwear].jpg"):
                    alpha 0.0
                    linear 1.0 alpha 1.0
                "You slowly stop massaging her pussy and take out your hand."
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion9_swim[char1.swimwear].jpg") with fade
                pause 1.0
                char1.talk "Wow, that was the best sun lotioning I have ever had *grins*"
                $ char1.change_favor(20)
                pl "If you need another one let me know... *grins*"
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion9_swim[char1.swimwear].jpg"):
                    zoom 1.0
                    linear 1.0 zoom 1.75 xpos -400 ypos -540
                pause 2.0
                "Oh my God she really needed it from the looks of it."
                "She notices your gaze wandering down between her legs."
                char1.talk "*giggles* Sorry, I am quite the gusher... *giggles some more.*"
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion9_swim[char1.swimwear].jpg"):
                    zoom 1.75 xpos -400 ypos -540
                    linear 0.6 zoom 1.5 xpos -300 ypos 0
                pause 1.0
                show expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion10_swim[char1.swimwear].jpg") with dissolve:
                    zoom 1.5 alpha 0.0 xpos -300 ypos 0
                    linear 0.7 alpha 1.0
                pause 1.2
                char1.talk "*smirks* Maybe next time we should go someplace a little more private."
                "Wow, what a babe. Did she just...?"
                $ player.change_lust(30)
                pl "Uhhmmmmm okay sure."
                char1.talk "You are cute when you are blushing. *giggles*"
                char1.talk "And now I need to clean myself up."
                pause 0.5
                char1.talk "See you later [char1.playername]!"
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_sunlotion10_swim[char1.swimwear].jpg"):
                    zoom 1.5 xpos -300 ypos 0
                    subpixel True
                    ease 0.6 zoom 1.0 xpos 0 ypos 0
                pause 1.0
                pl "Sure, see you later [char1.fname]."
                $ char1.add_scene_seen("Pool_lotion_extras")
                $ char1.locations[actions_left-2] = char1.fname + "_room"
                $ char1.locations[actions_left-3] = char1.fname + "_room"
                $ l_good_terms = False
            elif True:
                char1.talk "*Angry*{b}Hey [char1.playername]{/b} what do you think you are doing. Stop that right now."

    label action_pool_sunbed_lotion_end:
    $ menu_active = False
    $ location_old = location
    scene onlayer master
    $ char1.add_pl_interaction("others")
    call advance_time (1) from _call_advance_time_14
    call create_list_of_chars_display () from _call_create_list_of_chars_display_4
    $ action_initiative = ""
    $ initiative_char = no_char
    $ stop_scene()
    $ g_left_menu_hidden = l_left_menu_hidden
    if l_good_terms == True:
        return True
    elif True:
        return False





label action_pool_swim(char1, i_intro=True, i_auto_succeed=False):
    $ ll_tint = get_daytime_outdoor_tint(daytime, 0.8)
    if i_intro == True:
        show screen main_game(location)

    if not renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_" + location + "_" + "swim1_swim" + unicode(char1.swimwear) + ".webp"):
        "Sorry, but this action is not yet supported for [char1.fname]."
        return "nothing"

    if char1.get_action_allowed("pool_swim") == False and i_auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("pool_swim")
        char1.talk "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and i_auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_25
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("pool_swim", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    if i_intro == True:
        pl "[char1.fname], would you like to swim with me in the pool?"
        if char1.check_affection(1, 0, False) == False:
            char1.talk "I'm sorry [char1.playername], but not right now. Maybe later when we know each other a little better."
            $ char1.add_action_cooldown("pool_swim", actions_left, "You already asked me today. Maybe ask me again tomorrow, okay?")
            return "nothing"
        elif True:
            char1.talk "Sure [char1.playername], I'd love to."
            char1.talk "I'm in first... *giggles*"
            $ start_scene()
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit1_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                zoom 0.5
            with fade
            pause 0.7
            "[char1.fname] climbs down the ladder and starts floating in the water..."
    elif True:
        if char1.id == yvette.id:
            $ start_scene()
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit1_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                zoom 0.5
            with fade
            pause 0.7
        "[char1.fname] climbs down the ladder and floats in the water..."

    $ location_detail = "swim"
    $ start_scene()
    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim0_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
        zoom 0.5
    with fade
    pause 0.6
    $ char1.add_scene_seen("Pool_swim")
    $ menu_active = True
    $ option1 = True
    $ option2 = True
    $ option3 = True
    $ option4 = False
    $ l_boner = False
    $ l_let_win = False
    $ l_look_chest = False
    pause 0.5

    char1.talk "Come on in!"
    char1.talk "What are you waiting for?"
    char1.talk "The water's great!"
    "You climb in after her."
    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim0_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
        zoom 0.5 align (0.5,0.7)
        subpixel True
        ease 2.3 zoom 0.8
    $ renpy.pause(2.5,hard=True)
    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim1_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
        zoom 0.5
    pause 0.4
    char1.talk "The pool's great! I love it."
    pause 0.4
    pl "Yeah, I can see that."
    pause 0.4
    pl "And the view is amazing. *grinning*"
    "She just smiles at you and starts swimming in place..."
    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim2_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
        zoom 0.5
    pause 0.4
    "What do you want to do?"
    label action_pool_swim_menu:
    menu:
        "Swim with her" if option1:
            $ option1 = False
            pl "Would you like to swim some laps?"
            char1.talk "Sure!"
            char1.talk "Try to catch me... *giggles*"
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim3_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom 0.5
            pause 0.7
            $ l_breast_size_text = char1.get_breast_size_text()
            "You admire her [l_breast_size_text] for a moment..."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim3_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                subpixel True zoom 0.5 align (0.5,0.3)
                ease 1.5 zoom 0.8
            $ renpy.pause(1.7,hard=True)
            char1.talk "Whoever reaches the other side of the pool first wins!"
            "Then she goes freestyle!"
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim4_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                subpixel True zoom 0.5 align (0.9,0.4)
                pause 1.2
                ease 1.9 zoom 0.75
            $ renpy.pause(3.2,hard=True)
            "She's faster than you'd have thought..."
            menu:
                "Follow her but let her win" if True:
                    $ l_let_win = True
                    "You follow her, but make sure to stay a little behind to let her win."
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim5_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom 0.5
                    pause 0.7
                    "[char1.fname] reaches the end of the pool just a short moment before you."
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim12_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                    pause 0.7
                    char1.talk "I won! *smiling and still trying to catch her breath*"
                    pause 0.3
                    pl "You're really fast. *smiling*"
                    char1.talk "*giggles* I know you let me win."
                    pause 0.3
                    char1.talk "That's so sweet of you!"
                    call change_char_max_love (char1, 4) from _call_change_char_max_love_24
                    $ char1.change_love(8)
                    if char1.check_affection(3, 0, False) == True and char1.check_love(2, 0, False) == True:
                        "She gets closer and jumps into your arms..."
                        scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim13_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                        pause 0.7
                        char1.talk "Thank you! *kiss*"
                        pause 0.3
                        pl "Oh wow!"
                        char1.talk "Since you were so nice, you deserved a little reward."
                        pl "*smiling*"
                        $ char1.add_pl_interaction("hug/kiss")
                        scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim15_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                        pause 0.7
                        $ char1.add_scene_seen("Pool_swim_let_win")

                    char1.talk "I know that I am not the best swimmer. *looking a little sad*"
                    pause 0.3
                    char1.talk "Some of my assets are slowing me down..."
                    $ char1.add_pl_interaction("tease_talk")
                    char1.talk "Too much resistance in the water... *giggles*"
                    pause 0.4
                    char1.talk "So it's really cool that you let me win!"
                    pause 0.8
                    pl "It would have been very close anyway. *smiling*"
                    "You talk for a while longer..."
                    pause 1.5
                    char1.talk "*shivers* I am getting a bit cold."
                    pause 0.3
                    char1.talk "Is it okay with you if I get out and warm up?"
                    pl "Of course [char1.fname]."
                    char1.talk "Okay, see you later [char1.playername]."
                    pl "Sure."
                    $ player.rem_effect("erection")
                    jump action_pool_swim_end
                "Try to to win, swim as fast as you can" if True:

                    $ l_player_skill = player.get_strength() * 15 + player.get_endurance() - 10
                    $ l_girl_skill = char1.strength * 15 + char1.endurance
                    if l_player_skill <= l_girl_skill:
                        "You try to catch up and overtake her, but she's a good swimmer and the head start was too much..."
                        jump action_pool_swim_lose

                    "You swim as fast as you an and overtake [char1.fname]..."
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim11_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom 0.5
                    pause 0.7
                    "... reaching the end of the pool just before her."
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim12_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                    pause 0.7
                    char1.talk "Wow! You're really fast. *smiling and still trying to catch her breath*"
                    char1.talk "Even with my head start... *a little sad*"
                    $ char1.change_affection(-5)
                    pl "Don't be sad, it was very close."
                    pl "You did great!"
                    char1.talk "Oh!? I did?"
                    pause 0.3
                    pl "Yes, certainly."
                    $ char1.change_affection(5)
                    char1.talk "Thank you!"
                    pause 0.3
                    char1.talk "Some of my assets are slowing me down..."
                    $ char1.add_pl_interaction("tease_talk")
                    char1.talk "Too much resistance in the water... *giggles*"
                    pause 0.4
                    "You talk for a while longer..."
                    pause 1.5
                    char1.talk "*shivers* I am getting a bit cold."
                    pause 0.3
                    char1.talk "Is it okay with you if I get out and warm up?"
                    pl "Of course [char1.fname]."
                    char1.talk "Okay, see you later [char1.playername]."
                    pl "Sure."
                    $ player.rem_effect("erection")
                    jump action_pool_swim_end

            label action_pool_swim_lose:
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim5_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom 0.5
            pause 0.7
            "[char1.fname] reaches the end of the pool just a short moment before you can catch up."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim12_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            char1.talk "I won! *smiling and still trying to catch her breath*"
            pause 0.3
            char1.talk "You don't look like you let me win though."
            char1.talk "I guess I had a good head start... *giggles*"
            pause 0.2
            char1.talk "I'm not that fast in the water."
            char1.talk "My assets are always slowing me down. *smirks*"
            $ char1.add_pl_interaction("tease_talk")
            pl "I really tried to overtake you. *smiling*"
            "You talk for a while longer..."
            pause 1.5
            char1.talk "*shivers* I am getting a bit cold."
            pause 0.3
            char1.talk "Is it okay with you if I get out and warm up?"
            pl "Of course [char1.fname]."
            char1.talk "Okay, see you later [char1.playername]."
            pl "Sure."
            $ player.rem_effect("erection")
            jump action_pool_swim_end

        "Try to submerge her" if option2:
            $ option2 = False
            if char1.id == yvette.id:
                "Since she cannot stand in the pool, but you can, it's easy to push her under with just one arm."
                scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim6_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                pause 0.7
                "Poor [char1.fname] struggles a bit at first, but doesn't stand a chance."
                pause 0.4
                "Since you just wanted to have some fun and don't want to hurt her, you let go after a few seconds..."
                scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim7_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                pause 0.7
                char1.talk "*pffff* Hey [char1.playername]!"
                pause 0.3
                if char1.check_affection(2, 0, False) == True and char1.check_love(1, 0, False) == True:
                    char1.talk "*giggles* Now I'm all wet..."
                    char1.talk "Not that I wasn't before... *giggles some more*"
                    pl "I'm glad you're not mad at me. *smiles*"
                    char1.talk "Why should I be? It was fun!"
                    $ option4 = True
                elif True:
                    $ char1.change_anger(8)
                    char1.talk "Do you think just because I'm not that tall, you can pull me under?"
                    pl "Ummm... No, it was just fun..."
                    pause 0.4
                    char1.talk "I don't think it was that funny."
                    pl "I'm sorry."
                    $ char1.change_anger(-4)
                    "Your being sorry seems to have mollified her a bit."

        "Dive for a moment and look at her chest" if option3:
            $ option3 = False
            $ l_look_chest = True
            "You put your head under water for a moment, to {i}wet your hair{/i}..."
            $ l_breast_size_text = char1.get_breast_size_text()
            "...getting a good look at her [l_breast_size_text]."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim14_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom 0.5
            pause 0.7
            "{b}Damn{/b}! Look at those globes!"
            "Just a {i}little{/i} closer..."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim14_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                subpixel True zoom 0.5 align (0.75,0.6)
                ease 2.2 zoom 1.0
            $ renpy.pause(2.4,hard=True)
            $ player.change_lust(char1.sexiness + 4)
            char1.talk "Don't you want to come up? *muffled by the water*"
            char1.talk "Or do you want to {i}swim{/i} with your head under water for longer? *muffled by the water*"
            "You slowly resurface..."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim14_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                subpixel True zoom 1.0 align (0.75,0.6)
                ease 2.1 zoom 1.0 align (0.75,0.0)
            $ renpy.pause(2.2,hard=True)
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim2_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.8, i_align_x=0.7,i_align_y=0.1) with dissolve
            pause 0.7
            "She looks at you with a knowing smile..."
            char1.talk "Did you find any interesting underwater creatures? *grins*"
            pause 0.3
            pl "Ummm... I was just wetting my hair... *lamely*"
            pause 0.6
            char1.talk "Okay, sure. *smirks*"

        "Submerge her again" if option4:
            $ option4 = False
            "Well... No risk no fun, you push her under another time..."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim6_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom 0.5
            pause 0.7
            "Holding her just a little longer this time, before letting go."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim7_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            if char1.check_lust(3) == False:
                char1.talk "Okay that's it for now!"
                char1.talk "Why are you mean to me? I didn't do anything wrong, did I?"
                pause 0.4
                pl "Ummm.... Sorry!"
                char1.talk "I think I'm going out now... *sulking*"
                $ char1.change_affection(-5)
                jump action_pool_swim_end

            $ char1.add_scene_seen("Pool_swim_submerge")
            char1.talk "*pffff* {b}[char1.playername]{/b}!"
            pause 0.3
            char1.talk "I told you not to submerge me again!"
            pause 0.6
            char1.talk "Since I'm not strong enough to pull you under...*smiles*"
            "She grabs your neck with both her arms and pulls you close..."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim8_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            "... burying your head between her massive breasts."
            pause 0.4
            char1.talk "Are you getting enough air? *giggles*"
            pause 0.5
            pl "*mmmmhhhhpfff*"
            "After your muffled sounds, she lets go of your head."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim9_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom 0.5
            pause 0.7
            char1.talk "Are you okay [char1.playername]? *concerned*"
            pl "Yeah! *grinning*"
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim10_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            char1.talk "You could have shaken me off any time..."
            pause 0.3
            char1.talk "...and you drowned me twice."
            "She grabs your neck again, holding you even tighter this time."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim8_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            "...whispering in your ear."
            char1.talk "This time, I'm going to keep you there until you have to stay with me in the water for at least half an hour... *chuckles*"
            "Your face pressed against her huge soft pillows, you can already feel your dick reacting!"
            $ player.change_lust(char1.sexiness+2)
            $ player.add_effect("erection")
            "And she can feel it too!"
            pause 0.4
            char1.talk "Got you! *chuckles some more*"
            pause 0.4
            char1.talk "Now you know that every action has consequences! *smiles*"
            "She lets go of your neck and head."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim7_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            char1.talk "Even when you enjoy the consequences. *smiles some more*"
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim10_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            "You already miss the place between her tits..."
            "...getting a boner and having to stay in the water until it wears off is a small price to pay."
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim2_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
            pause 0.7
            if char1.id == yvette.id and l_look_chest == True and char1.check_love(3,0,False) == True:
                if char1.swimwear <> 2:
                    char1.talk "Too bad I'm not wearing my skimpy bikini right now..."
                    pl "Why do you say that?"
                    char1.talk "It' a secret. *grins*"
                    pause 0.4
                    pl "Okay..."
                    pause 0.4
                    jump action_pool_swim_not_topless

                if len(list_of_chars_display_3) > 1:
                    char1.talk "Too bad we're not alone at the pool right now..."
                    pl "What do you have in mind?"
                    char1.talk "Not much fun telling you. You'll see when we're alone. *smiles*"
                    pause 0.4
                    pl "Okay..."
                    pause 0.4
                    jump action_pool_swim_not_topless

                if mercedes.active == True:
                    mercedes.talk "Hey guys!"
                    scene expression im.MatrixColor("scenes/mercedes/pool/Mercedes_pool_lifeguard_leave1.webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with fade
                    pause 0.7
                    char1.talk "Hi [mercedes.fname]!"
                    pl "Hello, how are you doing?"
                    pause 0.4
                    "Damn! What a body!"
                    $ char1.change_lust(mercedes.sexiness)
                    pause 0.4
                    mercedes.talk "I'm good. *smiles*"
                    pause 0.4
                    mercedes.talk "Joy wants to see me in her office, so I have to leave the pool unattended for a while."
                    mercedes.talk "So please don't drown while I'm away."
                    pause 0.4
                    char1.talk "No worries, we're good."
                    pl "Yes. Don't worry about us."
                    pause 0.4
                    mercedes.talk "Hearing you both say that, I'm asking myself if I should worry now... *muses*"
                    pause 0.4
                    mercedes.talk "I don't know how long it will take."
                    pl "Okay."
                    char1.talk "Yeah, no problem."
                    pause 0.4
                    mercedes.talk "See you later."
                    char1.talk "Bye!"
                    scene expression im.MatrixColor("scenes/mercedes/pool/Mercedes_pool_lifeguard_leave2.webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom 0.5
                    pause 0.7
                    pl "Send greetings to Joy. *smiling*"
                    mercedes.talk "Will do."
                    scene expression im.MatrixColor("scenes/mercedes/pool/Mercedes_pool_lifeguard_leave3.webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom 0.5
                    pause 0.7
                    char1.talk "I take it that the way [mercedes.fname] was leaning down didn't help with your boner. *grins*"
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_swim2_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(0.5) with dissolve
                    pause 0.7
                    pl "Ummm..."

                char1.talk "Let's skip the swimming for today. Since we're alone at the pool, I have a better idea."
                pause 0.4
                "She swims to the ladder and climbs out..."
                $ l_exit = char1.get_pool_exit_image_id()
                $ l_exit_zoom = char1.get_pool_exit_image_zoom(l_exit)
                scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(l_exit_zoom) with fade
                pause 0.7
                pl "Are you leaving already?"
                pause 0.4
                char1.talk "No, I'm not leaving."
                call action_pool_pose_topless_yvette (char1) from _call_action_pool_pose_topless_yvette
                $ char1.add_pl_interaction("others")
                $ char1.add_action_cooldown("pool_swim", actions_left, "We already swam in the pool today. Ask me again tomorrow, okay?")
                jump action_pool_swim_end2

            label action_pool_swim_not_topless:
            char1.talk "Okay, what now? *giggles*"
            $ l_boner = True
            call actions_used (1) from _call_actions_used_99

        "Tell her you've had enough" if l_boner == False:
            pl "It was really fun with you in the water [char1.fname]."
            pause 0.3
            pl "But I better get out now."
            pause 0.3
            char1.talk "Ohh... Okay. *looking a bit sad*"
            jump action_pool_swim_end

    jump action_pool_swim_menu

    label action_pool_swim_end:
    if not option1 or not option2 or not option3:
        $ l_exit = char1.get_pool_exit_image_id()
        $ l_exit_zoom = char1.get_pool_exit_image_zoom(l_exit)
        if l_exit > 0:
            if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp"):
                scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(l_exit_zoom)
                with fade
            elif True:
                scene expression im.MatrixColor("scenes/" + char1.fname + "/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".jpg", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(l_exit_zoom)
                with fade
            pause 1.0
            if l_exit == 1:
                "You watch her climb out of the pool..."
                "...using the opportunity to get a good look at her nice butt."
                pause 0.5
                "Before she wraps herself up in the towel."
            elif l_exit == 2:
                "She pushes herself up on the edge of the pool not using the ladder..."
                "{b}Wow{/b}! She's really strong!"
                pause 0.5
                "You use the opportunity to get a good look at her incredibly tight and sexy butt!"
                if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp"):
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom l_exit_zoom * 1.6 xpos -450 ypos -320
                pause 0.6
                "Before she wraps herself up in the towel."

        call actions_used (1) from _call_actions_used_100
        $ char1.add_pl_interaction("others")
        $ char1.add_action_cooldown("pool_swim", actions_left, "We already swam in the pool today. Ask me again tomorrow, okay?")

    label action_pool_swim_end2:
    $ location_detail = ""
    $ menu_active = False
    $ stop_scene()
    return "do_return"





label action_pool_play(char1, i_intro=True, i_auto_succeed=False):
    $ ll_tint = get_daytime_outdoor_tint(daytime)
    $ l_no_exit = False
    if i_intro == True:
        show screen main_game(location)

    if char1.get_action_allowed("pool_play") == False and i_auto_succeed == False:
        $ l_text = char1.get_action_not_allowed_text("pool_play")
        char1.talk "[l_text]"
        return "nothing"

    if char1.get_action_allowed("anger_block") == False and i_auto_succeed == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_26
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("pool_play", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "nothing"

    if i_intro == True:
        pl "[char1.fname], would you like to play in the pool?"
        if char1.check_affection(1, 0, False) == False:
            char1.talk "I'm sorry [char1.playername], but not right now. Maybe later when we know each other a little better."
            $ char1.add_action_cooldown("pool_play", actions_left, "You just asked me not long ago. Maybe tomorrow?")
            return "nothing"
        elif True:
            char1.talk "Sure [char1.playername], I'd love to."
            char1.talk "I'm in first... *giggles*"
            pause 0.4
            if char1.id == desire.id or char1.id == lacey.id or char1.id == renee.id:
                "[char1.fname] grabs the air mattress, throws it into the pool..."
            elif True:
                "[char1.fname] grabs her swim ring, throws it into the pool..."
            "...and jumps in right after."
    elif True:
        if char1.id == desire.id or char1.id == lacey.id or char1.id == renee.id:
            "[char1.fname] grabs the air mattress, throws it into the pool..."
        elif True:
            "[char1.fname] grabs her swim ring, throws it into the pool..."
        "...and jumps in right after."

    $ l_jump_in = char1.get_pool_jump_in_image_id()
    $ location_detail = "play"
    $ start_scene()
    if l_jump_in > 0:
        if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_jump_in" + unicode(l_jump_in) + "_swim" + unicode(char1.swimwear) + ".webp"):
            scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_jump_in" + unicode(l_jump_in) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                zoom char1.get_pool_jump_in_image_zoom(l_jump_in)
            with fade
        elif True:
            show expression ("scenes/[char1.fname]/[char1.fname]_pool_jump_in[l_jump_in]_swim[char1.swimwear].jpg") with fade
        if l_jump_in == 1:
            char1.talk "Ahhhhhhh!!!"
            pause 1.0
            $ l_breast_size_text = char1.get_breast_size_text()
            if char1.swimwear == 2:
                if l_breast_size_text.endswith("chest"):
                    "Jumping into the pool with that tiny bikini, her [l_breast_size_text] is almost begging to break free..."
                elif True:
                    "Jumping into the pool with that tiny bikini, her [l_breast_size_text] are almost begging to break free..."
                "Wouldn't that make for an incredibly sexy sight!?"
                $ player.change_lust(char1.sexiness / 2)
            elif True:
                "The water sprays high as she jumps into the pool..."
        elif l_jump_in == 2:
            pause 1.0
            $ l_breast_size_text = char1.get_breast_size_text()
            if char1.swimwear == 2:
                "Diving into the pool with that tiny bikini almost makes her [l_breast_size_text] get free of the top."
                "Her strong legs and shapely thighs make for another incredibly sexy sight."
                $ player.change_lust(char1.sexiness / 2)
            elif True:
                "The water sprays high as she jumps into the pool..."
        pause 0.7

    if char1.id == desire.id:
        call action_pool_play_desire (char1) from _call_action_pool_play_desire
        jump action_pool_play_end
    elif char1.id == lacey.id:
        call action_pool_play_lacey (char1) from _call_action_pool_play_lacey
        jump action_pool_play_end
    elif char1.id == jessica.id:
        call action_pool_play_jessica (char1) from _call_action_pool_play_jessica
        if _return == "no_exit":
            $ l_no_exit = True
        jump action_pool_play_end
    elif char1.id == renee.id:
        call action_pool_play_renee (char1) from _call_action_pool_play_renee
        jump action_pool_play_end

    $ char1.add_scene_seen("Pool_play")
    show expression ("scenes/[char1.fname]/[char1.fname]_pool_play_swim[char1.swimwear].jpg") with dissolve
    pause 0.7
    "Reemerging from the water, [char1.fname] makes herself comfortable sitting in the swim ring."
    pause 0.5
    $ l_breast_size_text = char1.get_breast_size_text()
    if char1.swimwear == 2 or char1.swimwear == 3:
        "Presenting her half-exposed [l_breast_size_text] in an alluring way."
        $ player.change_lust(char1.sexiness / 2)
    elif char1.swimwear == 1:
        "Presenting her [l_breast_size_text] in a demure way."
    elif True:
        "Too bad her [l_breast_size_text] are mostly covered by the swimsuit..."
    pause 0.7
    char1.talk "Why don't you come in and have some fun?"
    if not renpy.loadable("scenes/" + char1.fname + "/" + char1.fname + "_pool_play1_swim" + unicode(char1.swimwear) + ".jpg"):
        pl "I don't know [char1.fname], I'd just like to watch you for a bit if that's ok with you."
        char1.talk "Hmm okay sure, it's your loss. *giggles*"
        jump action_pool_play_end

    pl "Sure, I'm coming in right away."
    show expression ("scenes/[char1.fname]/[char1.fname]_pool_play1_swim[char1.swimwear].jpg") with dissolve
    pause 1.0
    "After talking for a few minutes, you can no longer resist staring at her pretty face and marvelous breasts..."
    scene onlayer master
    show expression ("scenes/[char1.fname]/[char1.fname]_pool_play1_swim[char1.swimwear].jpg"):
        zoom 1.0
        subpixel True
        linear 1.0 zoom 1.75 xpos -550 ypos -100
    pause 2.0
    "She doesn't seem to mind the attention."
    "You have the feeling she even enjoys it."
    show expression ("scenes/[char1.fname]/[char1.fname]_pool_play1_swim[char1.swimwear].jpg"):
        zoom 1.75 xpos -550 ypos -100
        subpixel True
        linear 0.6 zoom 1.0 xpos 0 ypos 0
    "Encouraged by her behavior, you decide that it's time for some action..."
    $ menu_active = True
    $ option1 = True
    $ option2 = True
    $ option3 = True
    $ option4 = True
    label action_pool_play_menu:
    menu:
        "Push her around a bit in her pool ring." if option1:
            $ option1 = False
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play9_swim[char1.swimwear].jpg") with dissolve
            pause 1.0
            "You push her around in the pool while talking to her."
            $ l_chat_content = g_chat.get_topic(char1.get_topic("herself"), char1)
            pl "[l_chat_content.init]"
            $ l_inclination = renpy.random.choice([1,1,1,0])
            $ l_answer = l_chat_content.get_answer(l_inclination)
            char1.talk "[l_answer]"
            $ player.change_lust(l_chat_content.get_lust_change(l_inclination))
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play10_swim[char1.swimwear].jpg") with dissolve
            pause 1.0
            "You push her around some more using the opportunity to get a closer look at her."
            $ l_topic = "yourself"
            $ l_chat_content = g_chat.get_topic(l_topic, char1)
            pl "[l_chat_content.init]"
            $ l_inclination = renpy.random.choice([1,1,1,0])
            $ l_answer = l_chat_content.get_answer(l_inclination)
            char1.talk "[l_answer]"
            $ player.change_lust(l_chat_content.get_lust_change(l_inclination))
            $ l_breast_size_text = char1.get_breast_size_text()
            "Yes, she really is a sexy girl. With a cute face and [l_breast_size_text]."
            $ player.change_lust(char1.sexiness)
            char1.talk "This was fun, maybe we can do that again?"
            call change_char_max_affection (char1, 4) from _call_change_char_max_affection_14
            $ char1.change_affection(7)
            pl "Sure, anytime."
            jump action_pool_play_end

        "Tip the pool ring over and throw her into the water." if option2:
            $ option2 = False
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play2_swim[char1.swimwear].jpg") with dissolve
            "You grab [char1.fname] with the tire and tip her over..."
            char1.talk "*screaming* Hey [char1.playername], what are you doing???"
            "After she reemerges from the water..."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play3_swim[char1.swimwear].jpg") with dissolve
            if (char1.swimwear <> 2 and char1.id <> yvette.id) or char1.swimwear == 1:
                jump action_pool_play_not_topless

            if char1.swimwear == 2:
                "She seems to be a bit angry with you... AND wow, she's lost her bikini top in the water..."
            elif True:
                "She seems to be a bit angry with you... AND wow, her swimsuit is no longer covering her incredible tits..."
            "You try hard not to stare at her exposed breasts, but concentrate on her face instead."
            char1.talk "Look, now I'm all wet..."
            if player.check_charm(2) == False:
                "It's just now that she notices her exposed tits."
                char1.talk "Oh my God get out of the pool and leave me alone to fix this."
                $ char1.change_anger(10)
                "You decide that it's best not to anger her further. You leave the pool."
                jump action_pool_play_end

            if char1.id == yvette.id:
                pl "Please don't be angry [char1.fname], it's just water."
                pause 0.5
                menu:
                    "Tell her that her breasts are exposed." if True:
                        pl "I'd worry more about your bare breasts! *giggles*"
                        "It's just now that she notices her exposed tits."
                        if char1.check_tease_sexual(2) == False:
                            char1.talk "Okay you had your fun, now leave me alone and let me fix this."
                            "You decide that it's best not to anger her further. You leave the pool."
                            jump action_pool_play_end

                        char1.talk "And you tell me just now, after staring for what a min..."
                        "You cannot help but smile at her."
                        "Somehow your smile has melted away her anger."
                        char1.talk "*smiles* Okay you had your fun, now let me get my breasts covered and dry myself off before I get cold."
                        pl "Sure [char1.fname]."
                        jump action_pool_play_end
                    "Enjoy the view for a moment longer and don't tell her." if True:

                        $ char1.add_scene_seen("Pool_play_extras")
                        pl "*smiles* Come on [char1.fname], admit that it was fun."
                        char1.fname "*giggles* Okay you win. It was fun."
                        call change_char_max_affection (char1, 4) from _call_change_char_max_affection_61
                        $ char1.change_affection(8)
                        char1.talk "What I really don't like is that I have to look up at you while I'm angry..."
                        char1.talk "Somehow that doesn't really work."
                        "She grabs the swim ring and climbs onto it..."
                        show expression ("scenes/[char1.fname]/[char1.fname]_pool_play5_swim[char1.swimwear].jpg") with dissolve
                        pause 1.0
                        char1.talk "This is much better! *giggles*"
                        char1.talk "For the moment you are the small one and..."
                        pause 0.4
                        char1.talk "...I'm the huge girl! *giggles some more*"
                        "She probably wasn't referring to her tits..."
                        "...but {b}Damn{/b}!"
                        show expression ("scenes/[char1.fname]/[char1.fname]_pool_play4_swim[char1.swimwear].jpg") with dissolve
                        pause 1.0
                        "You cannot resist to stare at her incredible juggs!"
                        "So huge and soft right in front of your face..."
                        $ player.change_lust(char1.sexiness + 4)
                        pl "Oh my God! [char1.fname]! Huge just doesn't cover it!"
                        char1.talk "See, it's really fun looking down on you for a change [char1.playername]. *smiles*"
                        "She still hasn't noticed that her breasts are exposed..."
                        "You finally pry your eyes loose from her amazing chest and look up at her sweet face."
                        show expression ("scenes/[char1.fname]/[char1.fname]_pool_play6_swim[char1.swimwear].jpg") with dissolve
                        pause 1.0
                        "You decide that now is a good time to finally tell her that her tits are exposed."
                        if char1.swimwear == 0:
                            pl "Ummm... [char1.fname], your swimsuit has slipped a bit..."
                        elif True:
                            pl "Ummm... [char1.fname], you've lost your bikini top..."
                        hide expression ("scenes/[char1.fname]/[char1.fname]_pool_play6_swim[char1.swimwear].jpg") with dissolve
                        pause 0.7
                        "She looks down at her chest too."
                        show expression ("scenes/[char1.fname]/[char1.fname]_pool_play6_swim[char1.swimwear].jpg") with dissolve
                        pause 1.0
                        char1.talk "{b}[char1.playername]{/b}! You are unbelievable!"
                        pause 0.3
                        char1.talk "Have I been exposed like this since you pushed me under?"
                        pause 0.2
                        pl "Er... Yes. *smiles sheepishly*"
                        char1.talk "And you are telling me just now..."
                        pause 0.4
                        char1.talk "Do you want to have another look before I wrap them up?"
                        menu:
                            "Sure [char1.fname], I'd love to..." if True:
                                char1.talk "I knew you'd say that! *giggles*"
                                pl "Am I that obvious?"
                                char1.talk "Well I know what effect my tits have on most guys, even when they are not out in the open."
                                char1.talk "Not that you are like most guys..."
                                char1.talk "But I am sure you enjoy me squeezing them into the swim ring!"
                            "Ummm... I don't know maybe not?" if True:

                                char1.talk "Now you are getting shy all of a sudden? *smirks*"
                                pl "No! I've just thought..."
                                char1.talk "That is kinda cute. *smiles*"
                                $ char1.change_affection(8)
                                char1.talk "I am sure you still do not mind me squeezing them into the swim ring, do you?"

                        char1.talk "Here we go! *smirks*"
                        show expression ("scenes/[char1.fname]/[char1.fname]_pool_play7_swim[char1.swimwear].jpg") with dissolve
                        pause 1.0
                        "You are asking yourself how a girl so incredibly hot can be so nice at the same time..."
                        pl "That's really a sight to behold [char1.fname]!"
                        pause 0.5
                        pl "And did I tell you that you have the sweetest smile."
                        char1.talk "No, you charmer, you did not. *giggles*"
                        pause 0.3
                        char1.talk "But they are still getting wrapped up now."
                        "Seeing the sad look in your eyes..."
                        char1.talk "I am sorry, but it is getting a bit cold, I am shivering already."
                        char1.talk "I need to get out and dry myself off."
                        pl "Oh okay, sure. I understand [char1.fname]."
                        "She fixes her swimwear and swims to the stairs..."
                        jump action_pool_play_end
            elif True:

                pl "Please don't be angry [char1.fname], it's just water. I'd worry more about your bikini top. *giggles*"
                "It's just now that she notices her exposed tits."
                if char1.check_tease_sexual(2) == False:
                    char1.talk "Okay you had your fun, now leave me alone and let me fix this."
                    "You decide that it's best not to anger her further. You leave the pool."
                    jump action_pool_play_end

                char1.talk "And you tell me just now, after staring for what a min..."
                "You cannot help but smile at her."
                "Somehow your smile has melted away her anger."

            if char1.id <> amy.id:
                char1.talk "*smiles* Okay you had your fun, now let me get my top back on and dry myself off before I get cold."
                pl "Sure [char1.fname]."
                jump action_pool_play_end

            char1.talk "*smiles* Okay you had your fun, now I'm gonna have mine."
            "She grabs your shoulders and presses you against the edge of the pool..."
            "First you try to resist a bit. But wow she is strong. Even stronger than she looks."
            "You are not sure you could have stopped her even if you wanted to."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play4_swim[char1.swimwear].jpg") with dissolve
            char1.talk "Now this is my kind of fun... *slurp* *slurp*"
            "She presses her huge tits into your chest and sticks her tongue into your mouth."
            char1.talk "Hmmmm *slurp*"
            "Feeling her wet tongue inside your mouth and her heavy knockers pressed against your chest, your body starts to react."
            $ player.change_lust(30)
            $ player.add_effect("horny")
            $ player.add_effect("erection")
            "Feeling your erection, [char1.fname] starts rubbing her thigh against your dick."
            char1.talk "Not having you hard by now, that would have really made me angry..."
            if len(list_of_chars_display_3) > 1:
                char1.talk "Too bad we are not alone right now..."
                char1.talk "Ok, that's enough for now. Let me get dressed."
                pl "Hmmm okay [char1.fname]."
                "You wonder what would have happened alone with her..."
                jump action_pool_play_end

            $ char1.add_scene_seen("Pool_play_extras")
            char1.talk "Have you noticed that we are alone at the pool right now? *grins*"
            "You look around the pool and you are really the only ones at the time."
            pl "Uhmmm yes, you are right."
            "She reaches down with her left hand inside your pants and pulls your rock hard cock out..."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play5_swim[char1.swimwear].jpg") with dissolve
            pause 0.8
            pl "Oh wow [char1.fname] what are you doing?"
            char1.talk "We are alone here, so just enjoy it and stop pretending you don't like it. *giggles*"
            "After working on your dick with her hand for some time,\nshe grabs it and pushes it deep inside her hungry pussy..."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play6_swim[char1.swimwear].jpg") with dissolve
            pause 1.2
            pl "Wow [char1.fname] that feels amazing. You are so tight."
            char1.talk "You have no idea [char1.playername]. I have incredible control of my well developed vaginal muscle..."
            char1.talk "I am sure I could make you cum without moving one bit. But where is the fun in that? *giggles*"
            "With her strong thighs slung around your waist, she starts riding you."
            pl "[char1.fname], don't stop. You are incredible."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play7_swim[char1.swimwear].jpg") with dissolve
            pause 1.2
            "Looking you deep into the eyes, she can see that you are almost done."
            "So she starts fingering her breast and nipple while riding you harder and harder."
            char1.talk "YES [char1.playername], that's it. Fuck me harder, harder..."
            "She slams your hard rod into her pussy harder and harder."
            pl "I cannot hold it any more, I am cummmiiiinnnggg..."
            char1.talk "Give it all to me, cummminnnggg too. YES, YES, hmmmmm..."
            $ player.change_lust(-50)
            $ player.change_endurance(-50)
            $ char1.add_pl_interaction("sex")
            "Very much exhausted you sink into her strong arms..."
            $ char1.change_lust(-50)
            $ char1.change_endurance(-50)
            "Even after the incredible pool sex, she likes to tease you some more."
            scene expression ("scenes/[char1.fname]/[char1.fname]_pool_play8_swim[char1.swimwear].jpg") with dissolve
            pause 1.5
            char1.talk "You were great [char1.playername]. So you get to enjoy these for some time."
            "Having your face pressed into her huge wet breasts normally would have made you hard instantly. But you are much too exhausted right now."
            pl "Uhmmm [char1.fname] could I get some air?"
            char1.talk "*giggles* Oops sorry, didn't want to suffocate you."
            pl "*grins* No worries, it wasn't that bad."
            char1.talk "I guess you need some time to relax as well now."
            pl "Yes, absolutely."
            char1.talk "See you later [char1.playername]."
            pl "You too [char1.fname]."
            jump action_pool_play_end

    label action_pool_play_not_topless:
        "She seems to be a bit angry with you."
        char1.talk "Look, now I'm all wet..."
        if player.check_charm(2) == True:
            pl "*smiles* Come on [char1.fname], admit that it was fun."
            char1.fname "*giggles* Okay you win. It was fun."
            call change_char_max_affection (char1, 4) from _call_change_char_max_affection_15
            $ char1.change_affection(8)
            char1.talk "Now I'd like to dry myself off before I get cold."
            pl "Okay sure [char1.fname]."
        elif True:
            pl "Uhmmm yes."
            $ char1.change_anger(10)
            char1.talk "Now I'd like to dry myself off before I get cold."
            pl "Okay sure [char1.fname]."

    label action_pool_play_end:
    if not option1 or not option2 or not option3 or not option4:
        $ l_exit = char1.get_pool_exit_image_id()
        $ l_exit_zoom = char1.get_pool_exit_image_zoom(l_exit)
        if l_exit > 0 and not l_no_exit:
            if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp"):
                scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) at zoom_c(l_exit_zoom)
                if l_exit == 2 and char1.id == amy.id and char1.swimwear == 2:
                    call show_hidden_images (char1, "pool_exit", "trophies/Trophy_masturbate_all_2.png", 0.15, 0.01, 0.32) from _call_show_hidden_images
                with fade
            elif True:
                scene expression ("scenes/[char1.fname]/[char1.fname]_pool_exit[l_exit]_swim[char1.swimwear].jpg")
                if l_exit == 2 and char1.id == amy.id and char1.swimwear == 2:
                    call show_hidden_images (char1, "pool_exit", "trophies/Trophy_masturbate_all_2.png", 0.15, 0.01, 0.32) from _call_show_hidden_images_1
                with fade
            pause 1.0
            if l_exit == 1:
                "You watch her climb out of the pool..."
                "...using the opportunity to get a good look at her nice butt."
                pause 0.5
                "Before she wraps herself up in the towel."
            elif l_exit == 2:
                "She pushes herself up on the edge of the pool not using the ladder..."
                "{b}Wow{/b}! She's really strong!"
                pause 0.5
                "You use the opportunity to get a good look at her incredibly tight and sexy butt!"
                if renpy.loadable("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp"):
                    scene expression im.MatrixColor("scenes/" + char1.fname + "/pool/" + char1.fname + "_pool_exit" + unicode(l_exit) + "_swim" + unicode(char1.swimwear) + ".webp", im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                        zoom l_exit_zoom * 1.6 xpos -450 ypos -320
                pause 0.6
                "Before she wraps herself up in the towel."

        call actions_used (1) from _call_actions_used_186
        $ char1.add_pl_interaction("others")
        $ char1.add_action_cooldown("pool_play", actions_left, "We just played in the pool. Maybe we can do it again tomorrow?")

    $ location_detail = ""
    $ stop_scene()
    $ menu_active = False
    return "do_return"





label pool_distraction():
    $ list_of_girls_at_pool = player.get_chars_at_lcoation(location, actions_left)
    $ list_of_girls_at_pool_with_distraction = []
    $ list_of_char1_distractions = []
    $ l_counter = 0
    $ l_angry = "1"
    while l_counter < len(list_of_girls_at_pool):
        if renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction1_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".jpg"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction1_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".webp"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction2_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".jpg"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction2_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".webp"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction3_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".jpg"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction3_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".webp"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction4_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".jpg"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction4_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".webp"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction5_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".jpg"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        elif renpy.loadable("events/" + list_of_girls_at_pool[l_counter].fname + "/pool/" + list_of_girls_at_pool[l_counter].fname + "_pool_distraction5_1_swim" + unicode(list_of_girls_at_pool[l_counter].swimwear) + ".webp"):
            if list_of_girls_at_pool[l_counter].get_action_allowed("pool_distraction") == True:
                $ list_of_girls_at_pool_with_distraction.append(list_of_girls_at_pool[l_counter])
        $ l_counter += 1

    if len(list_of_girls_at_pool_with_distraction) == 0:
        return "continue"
    elif True:
        $ char1 = renpy.random.choice(list_of_girls_at_pool_with_distraction)
        $ player.smart_watch_character = char1

    $ menu_active = True
    show screen main_game(location)
    $ char1.add_action_cooldown("pool_distraction", 96, "")

    $ l_counter = 1
    while l_counter <= 20:
        if renpy.loadable("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction" + unicode(l_counter) + "_1_swim" + unicode(char1.swimwear) + ".jpg"):
            $ list_of_char1_distractions.append(l_counter)
            $ l_extension = "jpg"
            $ l_zoom = 1.0
        elif renpy.loadable("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction" + unicode(l_counter) + "_1_swim" + unicode(char1.swimwear) + ".webp"):
            $ list_of_char1_distractions.append(l_counter)
            $ l_extension = "webp"
            $ l_zoom = 0.5
        $ l_counter += 1

    $ l_distraction_id = renpy.random.choice(list_of_char1_distractions)
    $ ll_tint = get_daytime_outdoor_tint(daytime)

    $ char2 = char1
    if len(list_of_girls_at_pool) > 1 and renpy.random.randint(1,10) <= 7:
        while char2 == char1:
            $ char2 = renpy.random.choice(list_of_girls_at_pool)

    $ start_scene()
    scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_1_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
        subpixel True zoom l_zoom
    with dissolve
    pause 1.0
    if l_distraction_id == 1:
        "As you try to relax, your eye is caught by [char1.fname] sitting at the pool's edge"
        $ l_breast_size_text = char1.get_breast_size_text()
        "Giving you a nice side view of her [l_breast_size_text]."
    elif l_distraction_id == 2:
        "As you try to relax, you spot [char1.fname] in the pool, pushing herself out on the edge."
        $ l_breast_size_text = char1.get_breast_size_text()
        "Giving you an incredible view of her [l_breast_size_text]. Almost pushing them into your face!"
    elif l_distraction_id == 3:
        if renpy.loadable("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction_angry3_swim"  + unicode(char1.swimwear) + "." + l_extension):
            $ l_angry = "3"
        "As you try to relax, you spot [char1.fname], sitting at the edge of the pool,\nletting her feet dangle in the water."
        "Giving you an unforgettable view of her amazing ass..."
        $ l_breast_size_text = char1.get_breast_size_text()
        "...not to mention a side view of her [l_breast_size_text]."
    elif l_distraction_id == 4:
        "As you try to relax, [char1.fname] tanning topless on a sunbed near you is catching your eye."
        $ l_breast_size_text = char1.get_breast_size_text()
        "Baring her [l_breast_size_text] for all the world to see."
        "Well maybe not for all the world, since you're the only guy on the island..."
    elif l_distraction_id == 5:
        $ l_angry = "5"
        "As you try to relax, [char1.fname] walking by your sunbed catches your eye."
        $ l_breast_size_text = char1.get_breast_size_text()
        "She really has a nice ass!"
        "And the side view of her [l_breast_size_text] isn't half bad either."

    menu:
        "Ignore her and continue relaxing" if True:
            jump pool_distraction_do_relax
        "Spy on her from behind your sunglasses" if True:

            "You watch her a bit longer, safely hidden behind your dark sunglasses."

    if l_distraction_id == 4:
        call pool_distraction_id4 (char1, char2) from _call_pool_distraction_id4
        if _return == "do_relax":
            jump pool_distraction_do_relax
        elif True:
            jump pool_distraction_common

    $ l_breast_size_text = char1.get_breast_size_text()
    if l_distraction_id == 2:
        "[char1.fname] with her [l_breast_size_text], slim waist and tight abs is a sight to behold!"
    elif True:
        "Her [l_breast_size_text] and firm butt are truly a glorious sight!"
    $ player.change_lust(char1.sexiness - 2 + char1.swimwear)
    scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_1_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
        subpixel True zoom l_zoom
        ease 1.0 zoom l_zoom * 1.5 xpos -400 ypos -50
    pause 1.5

    if l_distraction_id == 5:
        "You look at her butt as she walks by your sun lounger..."
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_2_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            subpixel True zoom l_zoom * 1.5 xpos -400 ypos -360
        pause 1.2

    if char2.id <> char1.id:
        "Still staring at [char1.fname], you don't notice that [char2.fname] caught you staring..."
        char2.talk "Ahem! *coughing slightly*"
    elif renpy.random.randint(1,10) <= 5:
        pause 1.0
        "You stare at her for a little longer, when she somehow {i}feels{/i} your eyes on her."
    elif True:
        pause 1.0
        "You watch her for a little longer without her noticing you, before you decide to finally relax a bit."
        jump pool_distraction_do_relax

    if l_distraction_id == 5:
        "You try to tear your gaze away from [char1.fname]'s incredible ass..."
    elif True:
        $ l_breast_size_text = char1.get_breast_size_text()
        "You try to tear your gaze away from [char1.fname]'s [l_breast_size_text]..."
    "...but it's already too late!"
    "You've been caught staring!"
    pause 0.5
    if char1.check_tease_sexual(2) == False:
        if l_distraction_id == 5:
            "[char1.fname] turns around, gives you an angry stare and..."
        elif l_distraction_id <> 2:
            "[char1.fname] gives you an angry stare, before she stands up and..."
        elif True:
            "[char1.fname] gives you an angry stare, gets out of the water, dries herself off and..."
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction_angry"  + unicode(l_angry) + "_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with fade:
            subpixel True zoom l_zoom
        pause 1.0
        "...bawls you out!"
        char1.talk "You know that it's rude to stare at a girl like you just did!?"
        if l_extension == "webp":
            scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction_angry"  + unicode(l_angry) + "_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                subpixel True zoom l_zoom * 2 xpos -900
        pause 0.8
        pl "Ummm...."
        "Not really interested in your answer, [char1.fname] leaves the pool area..."
        call actions_used (1) from _call_actions_used_56
        $ char1.locations[actions_left-2] = char1.fname + "_room"
        show expression ("locations/loc_pool_distraction.jpg") with dissolve
        pause 1.0
        "After that encounter, you decide to relax for some time."
        jump pool_distraction_do_relax

    if l_distraction_id == 5:
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_3_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            subpixel True zoom l_zoom
    elif True:
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_2_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            subpixel True zoom l_zoom * 1.5 xpos -400 ypos -50
    pause 1.0
    char1.talk "Oh! Hi [char1.playername]! *smiles*"
    $ char1.add_event_seen("Pool_distraction" + unicode(l_distraction_id))
    pause 0.5
    if l_distraction_id == 5:
        char1.talk "Did you just stare at my butt? *smirks*"
        char1.talk "Let me give you a better view!"
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_3_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            subpixel True zoom l_zoom * 1.5 xpos -250 ypos -250
        pause 0.7
        char1.talk "When I stick it out, it looks even better! *smirks*"
        $ player.change_lust(char1.sexiness - 2 + char1.swimwear)
    elif True:
        $ l_randint = renpy.random.randint(1,3)
        if l_randint == 1:
            char1.talk "Are you enjoying the view? *smirks*"
        elif l_randint == 2:
            $ l_breast_size_text = char1.get_breast_size_text()
            if l_distraction_id == 1:
                char1.talk "You like the side view of my [l_breast_size_text]? *smiles*"
            elif l_distraction_id == 2:
                char1.talk "Are you staring at my [l_breast_size_text]? *smiles*"
            elif True:
                char1.talk "Sooo... You like my tight butt and my [l_breast_size_text]? *smirks*"
            $ player.change_lust(char1.sexiness - 2)
        elif True:
            char1.talk "Staring is kinda rude you know..."
            $ l_breast_size_text = char1.get_breast_size_text()
            $ l_body_type_text = char1.get_body_type_text()
            if char1.breast_size >= 2:
                char1.talk "But I forgive you! Even some of the girls stare at my [l_breast_size_text] and my [l_body_type_text] body! *smiles*"
            elif True:
                char1.talk "But I forgive you! Even some of the girls start at my [l_body_type_text] body! *smiles*"
            $ player.change_lust(char1.sexiness - 2)

    if player.check_charm(4) == True:
        if l_distraction_id == 5:
            pl "You have an incredible behind [char1.fname]."
            pl "From all angles, sticking it out or not... *smiling*"
            scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction"  + unicode(l_distraction_id) + "_3_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                subpixel True zoom l_zoom * 1.5 xpos -250 ypos -250
                ease 1.5 ypos 0
            pause 1.8
            char1.talk "Thank you [char1.playername]! Happy you enjoy the view!"
        elif l_distraction_id == 1 or l_distraction_id == 3:
            pl "There's nothing more magnificent than a beautiful girl sitting at the pool's edge! *smiling*"
        elif l_distraction_id == 2:
            pl "There's nothing better than a beautiful wet girl climbing out of the pool! *smiling*"
        pause 0.3
        pl "So yeah, I'm enjoying the view very much! *smiling some more*"
        if char1.swimwear == 2:
            char1.talk "I guess it doesn't hurt that the girl in question is only wearing a tight little bikini... *smiles back*"
            if l_distraction_id == 2:
                char1.talk "Or that she's all wet!"
        elif True:
            char1.talk "You are such a charmer!"
            if l_distraction_id == 2:
                char1.talk "I'm sure you really like the wet look! *giggles*"

        char1.talk "Well, I really don't mind you looking! *smiles*"
        call change_char_max_affection (char1, 5) from _call_change_char_max_affection_72
        $ char1.change_affection(10)
        jump pool_distraction_common
    elif True:
        pl "Ummm... Sorry for staring... *lamely*"
        char1.talk "Don't worry about it! *smiling*"
        pause 1.0
        char1.talk "Unfortunately I have to leave now."
        pause 0.3
        pl "Oh... Okay!"
        char1.talk "Bye [char1.playername], see you later!"
        pl "See you [char1.fname]!"
        call actions_used (1) from _call_actions_used_57
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        show expression ("locations/loc_pool_distraction.jpg") with dissolve
        pause 1.0
        "[char1.fname] leaves the pool area..."
        "You decide to finally relax for a bit."
        jump pool_distraction_do_relax

    label pool_distraction_common:
    if char1.get_action_icon_available("pool_play") == True and char1.get_action_allowed("pool_play") == True and renpy.random.randint(1,10) <= 7:
        char1.talk "Why don't we play in the pool for a bit?"
        menu:
            "Agree to play in the pool." if True:
                pl "Sure, let's get in! It's gonna be fun!"
                char1.talk "Cool!"
                $ char1.change_affection(5)
                call action_pool_play (char1, False) from _call_action_pool_play_1
                jump pool_distraction_end
            "Tell her you'd like to relax for a bit." if True:

                pl "I'd like to just relax for a bit if that's okay with you."
                char1.talk "Ohhh... Okay! *disappointed*"
                $ char1.change_affection(-5)
                "You decide to relax for a bit now..."
                jump pool_distraction_do_relax

            "Propose to swim for a bit." if char1.get_action_icon_available("pool_swim") and char1.get_action_allowed("pool_swim"):
                pl "How about we swim for a bit instead?"
                if char1.check_affection(2) == True and char1.check_love(1) == True:
                    char1.talk "Umm yeah okay!"
                    call action_pool_swim (char1, False) from _call_action_pool_swim_1
                    jump pool_distraction_end
                elif True:
                    char1.talk "Ummm... I don't know, maybe later?"
                    pl "Okay, sure!"
                    if l_distraction_id == 4:
                        pl "I will go back to my sunbed and relax a bit."
                        pl "See you later [char1.fname]!"
                        char1.fname "Bye [char1.playername]."
                    elif True:
                        "You decide to relax for a bit now..."
                    jump pool_distraction_do_relax

    elif char1.get_action_icon_available("pool_swim") == True and char1.get_action_allowed("pool_swim") == True and renpy.random.randint(1,10) <= 6:
        char1.talk "Why don't we swim in the pool for a bit?"
        menu:
            "Agree to swim in the pool." if True:
                pl "Sure, let's get in!"
                char1.talk "Cool!"
                $ char1.change_affection(5)
                call action_pool_swim (char1, False) from _call_action_pool_swim_2
                jump pool_distraction_end
            "Tell her you'd like to relax for a bit." if True:

                pl "I'd like to just relax for a bit if that's okay with you."
                char1.talk "Ohhh... Okay! *disappointed*"
                $ char1.change_affection(-5)
                "You decide to relax for a bit now..."
                jump pool_distraction_do_relax

            "Propose to play in the pool for a bit." if char1.get_action_icon_available("pool_play") and char1.get_action_allowed("pool_play"):
                pl "How about we play in the pool instead?"
                if char1.check_affection(2) == True and char1.check_love(1) == True:
                    char1.talk "Umm yeah okay!"
                    call action_pool_play (char1, False) from _call_action_pool_play_2
                    jump pool_distraction_end
                elif True:
                    char1.talk "Ummm... I don't know, maybe later?"
                    pl "Okay, sure!"
                    if l_distraction_id == 4:
                        pl "I will go back to my sunbed and relax a bit."
                        pl "See you later [char1.fname]!"
                        char1.fname "Bye [char1.playername]."
                    elif True:
                        "You decide to relax for a bit now..."
                    jump pool_distraction_do_relax

    pause 1.0
    char1.talk "Too bad I have to leave now."
    pause 0.3
    pl "Oh... Okay!"
    char1.talk "Bye [char1.playername], see you later!"
    pl "See you [char1.fname]!"
    call actions_used (1) from _call_actions_used_58
    $ char1.locations[actions_left-1] = char1.fname + "_room"
    show expression ("locations/loc_pool_distraction.jpg") with dissolve
    pause 1.0
    "[char1.fname] leaves the pool area..."
    "You decide to finally relax for a bit."

    label pool_distraction_do_relax:
    $ stop_scene()
    $ menu_active = False
    return "do_relax"

    label pool_distraction_end:
    $ stop_scene()
    $ menu_active = False
    return "nothing"




label pool_distraction_id4(char1, char2):
    $ ll_tint = get_daytime_outdoor_tint(daytime)
    if renpy.loadable("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_1_swim" + unicode(char1.swimwear) + ".webp"):
        $ l_extension = "webp"
        $ l_zoom = 0.5
    elif True:
        $ l_extension = "jpg"
        $ l_zoom = 1.0

    $ l_breast_size_text = char1.get_breast_size_text()
    "[char1.fname] with her exposed [l_breast_size_text], slim waist and tight abs is a sight to behold!"
    $ player.change_lust(char1.sexiness - 2 + char1.swimwear)
    "Since she appears to be sleeping, it's a good opportunity to {i}casually{/i} walk by and get an even better look."
    menu:
        "Don't risk getting caught and stay on your sunbed." if True:
            "You decide the view is great sitting on your sunbed..."
            "...walking by is not worth the risk of getting caught."
            pause 1.0
            "After having stared for some time, you decide to relax a bit."
            return "do_relax"
        "Walk by her sunbed and take a closer look (you might get caught)." if True:

            "You get up and leisurely walk towards her sunbed..."
            scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_1_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])):
                zoom l_zoom
                ease 2.8 zoom l_zoom * 2 xpos -1200 ypos -150
            $ renpy.pause(3.2, hard=True)
            scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_2_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom l_zoom
            pause 0.8
            $ l_breast_size_text = char1.get_breast_size_text()
            "From up close, her [l_breast_size_text] are even more impressive!"
            "You wonder how they'd feel in your hands..."
            $ player.change_lust(char1.sexiness + 2)
            pause 1.0
            "After another look, you continue your stroll passing by her sunbed."
            scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_3_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
                zoom l_zoom
            pause 1.0
            if player.check_sneaking(3) == True:
                if char1.id <> char2.id:
                    "Still staring at [char1.fname], you don't notice that [char2.fname] caught you lingering..."
                    char2.talk "Ahem! *coughing slightly*"
                    jump pool_distraction_id4_caught
                elif renpy.random.randint(1,13) > (player.get_hacking() + 5):
                    "You stare at her for a little longer, when she stirs and opens her eyes..."
                    jump pool_distraction_id4_caught
            elif True:
                jump pool_distraction_id4_caught

            "[char1.fname] still hasn't noticed you. What do you want to do?"
            menu:
                "Make some noise to get her attention." if True:
                    pl "*coughing slightly*"
                    "Noticing the noise, [char1.fname] stirs and slowly opens her eyes..."
                    jump pool_distraction_id4_caught
                "Take another good look before walking back to your sunbed to relax." if True:

                    pause 1.0
                    "You take another good look, before you walk back to your sunbed to finally relax a bit."
                    $ player.change_lust(char1.sexiness + 2)
                    return "do_relax"

    label pool_distraction_id4_caught:
    if char1.check_tease_sexual(3) == False:
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_5_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            zoom l_zoom
        pause 0.7
        char1.talk "How long have you been standing here?"
        pl "Ummm... I'm just passing by... *lamely*"
        $ char1.change_anger(15)
        $ char1.change_affection(-8)
        char1.talk "Yeah sure! *angry*"
        char1.talk "So it's not enough to see me topless from your sunbed..."
        char1.talk "...you have to walk here and stare at my tits?"
        pause 0.6
        pl "Sorry, I haven't..."
        char1.talk "Just skip it, okay?"
        char1.talk "I'm leaving..."
        "[char1.fname] stands up, puts her bra back on and leaves the pool area."
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction_angry1_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with fade:
            zoom l_zoom
        pause 0.8
        "Oh damn! She sounded quite pissed..."
        "You better get back to your sunbed and relax a bit to cool down."
        call actions_used (1) from _call_actions_used_59
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        return "do_relax"

    scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_4_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
        zoom l_zoom
    pause 0.8
    char1.talk "Oh, hi [char1.playername]! How are you doing? *smiles*"
    pl "Hello [char1.fname]!"
    pl "I'm good! Thanks for asking."
    pl "It seems you're enjoying the sun too."
    "It's just now that she's conscious of her exposed breasts..."
    char1.talk "Ummm... Yeah... *smiles sheepishly*"
    char1.talk "Didn't want to get tan lines you know..."
    if player.check_charm(4) == False:
        pl "Ahh... okay!"
        char1.talk "I think I'll go inside a bit now, before I get sunburn..."
        char1.talk "See you later [char1.playername]."
        pl "Bye [char1.fname]!"
        "She stands up, gets her bra and leaves the pool area."
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction_angry2_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with fade:
            zoom l_zoom
        pause 1.0
        call actions_used (1) from _call_actions_used_60
        $ char1.locations[actions_left-1] = char1.fname + "_room"
        "You decide that now is the perfect time to finally relax a bit."
        return "do_relax"

    pl "I can totally understand that."
    pl "Perfect breasts as yours should always get the best possible treatment! *smiling*"
    char1.talk "Exactly... *giggles* ...and thank you!"
    pause 0.4
    char1.talk "And I suspect you don't mind looking at them while we talk either! *smiles*"
    if l_extension == "webp":
        scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_7_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
            zoom l_zoom
        char1.talk "Do you like it when I squeeze them for you?"
        $ char1.add_pl_interaction("tease_talk")
        $ char1.add_pl_interaction("tease_boobs")
        $ player.change_lust(char1.sexiness + 2)
        pl "*gulp* Yes, very much."
        char1.talk "*smiles* You're cute when you're embarrassed."
        pause 0.4
        pl "Ummm... You think? {w}Well, thanks I guess."
    elif True:
        pl "I cannot complain in any way! *still smiling*"
    call change_char_max_affection (char1, 5) from _call_change_char_max_affection_73
    $ char1.change_affection(10)
    char1.talk "It's time I put them back in, before my nipples get sunburn. *smiles*"
    "She puts her top back on and sits up."
    scene expression im.MatrixColor("events/" + char1.fname + "/pool/" + char1.fname + "_pool_distraction4_6_swim" + unicode(char1.swimwear) + "." + l_extension, im.matrix.tint(ll_tint[0], ll_tint[1], ll_tint[2])) with dissolve:
        zoom l_zoom
    pause 0.8
    $ char1.add_event_seen("Pool_distraction4")
    return "nothing"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
