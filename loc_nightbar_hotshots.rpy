init python:
    from copy import deepcopy



    class cl_hotshots_games():
        def __init__(self, i_id, i_name, i_base_spiciness):
            self.id = i_id
            self.name = i_name
            self.base_spiciness = i_base_spiciness
            return





    class cl_hotshots():
        def __init__(self, i_char):
            self.heat = 0
            self.player_drunk = 0
            self.player_undress = 1
            self.player_max_undress = 4
            self.opponent_drunk = 0
            self.opponent_undress = 1
            self.opponent_max_undress = 4
            self.opponent = i_char
            self.who_plays = ""
            self.current_game = cl_hotshots_games(0, "", 0)
            self.game_list = []
            self.game_list.append(cl_hotshots_games(1, "Auto-win", 0))
            self.game_list.append(cl_hotshots_games(2, "Auto-loose", 0))
            self.game_list.append(cl_hotshots_games(3, "Personal Question", 0))
            self.game_list.append(cl_hotshots_games(4, "Soft Question", 5))
            self.game_list.append(cl_hotshots_games(5, "Hard Question", 10))
            self.game_list.append(cl_hotshots_games(6, "Hangman", 3))
            self.game_list.append(cl_hotshots_games(7, "Quarters", 3))
            self.questions = deepcopy(gl_hs_questions)
            self.questions_player = deepcopy(gl_hs_questions_player)
            
            
            
            self.strip_encourage = [ ["Strip! Strip! Strip!", "Nice! Let's see a bit more of our beautiful lady!", "Time to undress sweetie! *laughs*", "It feels pretty hot in here... Maybe that jacket is not necessary *winks*"],\
                                     ["Aaaaaand... stripping action! *laughs*", "The crowd demands to see more flesh darling! *laughs*", "Can't wait to see you stripping some more *giggles*", "Hey people! Pay attention, lingerie show is about to begin!"],\
                                     ["Woohooo! Boobies out! *cheering*", "Boobieeeeeeessss!! *laughs*", "Woohoo! Let's see those {b}little{/b} puppies of yours!", "Bra off in 3... 2... 1... Hooray!"] ]
            
            
            self.strip_encourage_player = [ ["Strip! Strip! Strip!", "Nice! Let's see a bit more of our nice guy!", "Time to undress honey! *giggles*", "It's pretty hot in here... Why don't you get rid of the tie and the shirt!"],\
                                            ["Aaaaaand... stripping action! *snickers*", "The ladies want to see some more flesh darling!", "Can't wait to see you without your T-shirt! *giggles*", "Girls, let's see his cute upper body!"],\
                                            ["Woohooo! Get rid of the trousers! *cheering*", "Let us see those trunks of yours!", "Are you hard already? *giggles* {w}Let's see...", "Trouser off in 1,2,3... Yeah!"] ]
            
            
            self.drinking_comments = [ ["What is that stuff??? {w}It burns like hell!", "What the hell is that!? {w}My throat is burning now!", "Cough! cough! cough! {w}Damn... That's strong indeed!", "Damn Yumiko! {w}This stuff tastes like poison!"],\
                                       ["It doesn't taste too bad after all... {w}I think I could get used to it. *giggles*", "Mmmhh, it's not that hard anymore... {w}I must be getting used to it *blinks*", "I think I'm starting to appreciate it's flavor {w}It's not that bad any more *giggles*", "Interesting... {w}Suddenly it's not as bad as before *blinks*"],\
                                       ["Damn! {w}This shit is fucking good now! *laughs*", "Hell yes! {w}I love this brew! *laughs out loud*", "Ummmhnnn... Blessed liquor... {w}Another round here Yumiko *laughs*", "This tastes amazing suddenly! {w}I really wonder why? *giggles*"] ]
            
            
            self.asking_about_boobs = [ ["Interesting secret word don't you think?{w}\nDo my {b}&s_word{/b} look good tonight? *smiles*", "Speaking about that...{w}\nWhat do you think about my {b}&s_word{/b}? *smirks*", "Nice word choice indeed{w}\nI wonder what a certain handsome lottery winner thinks about my {b}&s_word{/b}. *blinks*"],\
                                        ["Mmmmhhh...{w} {b}&s_word{/b}...{w}\nDo you like mine? *flirting*", "Come on, don't be shy! Take a closer look at my {b}&s_word{/b}{w}\nDo you like what you see? *giggles*", "{b}&s_word{/b} are good. I like {b}&s_word{/b} *laughs*{w}\nDo you like them too?"],\
                                        ["Ha haha! {b}&s_word{/b}!{w}\nWhat about mine? *laughs*", "{b}&s_word{/b}, {b}&s_word{/b}, {b}&s_word{/b}... I loooove my {b}&s_word{/b}{w}\nDo you love them too? *laughs*", "Let's talk about my {b}&s_word{/b} for once! *laughing out loud*{w}\nYou like them too. Don't you, you naughty boy? *more laughs*"] ]
            
            
            self.answer_about_boobs = [ ["I love them!", "Absolutely! They're fantastic in size and shape!", "Sure my lady. They're hot and beautiful!", "Of course I adore them... what man wouldn't? *smiles*"],\
                                        ["Sure girl! They're awesome you know!", "I totally love them... {w} And you're a naughty girl!", "Testing me huh? {w}Okay, any man would give his right arm for them!", "You're such a tease girl! {w}But they're indeed irresistible!"],\
                                        ["Damn you're such a tease! {w}I loooove them!", "They rock you know! {w}I could {i}admire{/i} them all night long!", "You're driving me crazy! {w}They're aaaawesome! *laughs*", "I don't know if I can resist to touch them if you come even a little bit closer!"] ]
            return
        
        def get_random_text(self, i_field, i_primary_index=None):
            l_list = getattr(self, i_field)
            if i_primary_index == None:
                return random.choice(l_list)
            else:
                return random.choice(l_list[i_primary_index])
        
        def get_question(self, i_category):
            question_category_list = []
            
            for l_question in self.questions:
                if l_question.type == i_category:
                    question_category_list.append(l_question)
            
            if len(question_category_list) == 0:
                self.questions = deepcopy(gl_hs_questions)
                for l_question in self.questions:
                    if l_question.type == i_category:
                        question_category_list.append(l_question)
            
            lo_question = renpy.random.choice(question_category_list)
            self.questions.remove(lo_question)
            return lo_question
        
        def get_question_player(self, i_category):
            question_category_list = []
            for l_question in self.questions_player:
                if l_question.type == i_category:
                    question_category_list.append(l_question)
            if len(question_category_list) == 0:
                self.questions_player = deepcopy(gl_hs_questions_player)
                for l_question in self.questions_player:
                    if l_question.type == i_category:
                        question_category_list.append(l_question)
            lo_question = renpy.random.choice(question_category_list)
            self.questions_player.remove(lo_question)
            return lo_question
        
        def get_drinking_comment(self):
            return renpy.random.choice(self.drinking_comments)
        
        def select_subgame(self):
            self.current_game = random.choice(self.game_list)
            return
        
        def switch_who_plays(self):
            if self.who_plays == "P":
                self.who_plays = "G"
            else:
                self.who_plays = "P"
            return
        
        def check_girl_undress_inclination(self):
            if self.opponent_undress == 1 and self.opponent.relationship_type > 1:
                return True
            elif self.opponent_drunk >= (self.opponent_undress * 22) - int(self.opponent.lust / 20) - (self.opponent.relationship_type * 4):
                return True
            else:
                return False





    class cl_hangman():
        def __init__(self):
            self.remaining_attempts = 7
            self.available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.current_guesses = []
            self.breasts_words = ["BREASTS", "MELONS", "BOOBS", "TITS", "KNOCKERS", "FUNBAGS", "JUGGS", "MAMMARIES", "TITTIES", "HOOTERS", "BOOBIES", "GAZONGAS", "MOUNDS", "HONKERS", "TATAS", "BAZOOKAS", "GLOBES"]
            self.positions_words = ["DOGGYSTYLE", "MISSIONARY", "COWGIRL", "RIDING", "SPOONING", "WHEELBARROW", "BLOWJOB", "HANDJOB", "TITJOB", "TITFUCK", "BOOBJOB", "CUNNILINGUS", "FACESITTING"]
            self.other_words = [\
                "NIPPLES", "AREOLAS", "CLEAVAGE", "CHEST", "RACK", "ASS", "BUM", "BUTT", "BUTTOCKS", "TUSH", "ARSE", "TUSHIE", "LIPS", "BOSOM", "TONGUE",\
                "PUSSY", "VAGINA", "CLITORIS", "LABIA", "CUNT", "DICK", "COCK", "PENIS", "BULGE", "CROTCH", "PACKAGE", "HUNG", "ERECTION",\
                "PASSION", "PASSIONATE", "KISS", "KISSES", "KISSING", "CARESSES", "CARESSING", "GROPE", "GROPING", "FLASH", "FLASHING", "TEASE", "TEASING",\
                "LINGERIE", "PANTIES", "TANGA", "THONG", "STOCKINGS", "CORSET", "PUSHUPS", "BUSTIER", "BODYSUIT", "STILETTOS", "HEELS", "MINISKIRT", "TOPLESS", "NUDE", "NUDIST", "NUDISM",\
                "SEXY", "LUST", "NAUGHTY", "SENSUAL", "HORNY", "HOT", "LEWDNESS", "AROUSAL", "LUXURIA", "DESIRE", "SEXUAL", "WILD", "FELINE", "SEXINESS", "NYMPHO",\
                "MASTURBATE", "MASTURBATION", "ONANISM", "DILDO", "VIBRATOR", "HITACHI", "FINGERING", "BANANA", "CARROT", "CUCUMBER", "ZUCCHINI", "TENGA",\
                "CUM", "CUMMING", "LOAD", "ORGASM", "ECSTASY", "MULTIORGASMIC", "SQUIRTER", "SQUIRTING", "EJACULATION",\
                "BISEXUAL", "BISEXUALITY", "CYBERSEX", "SEXTING", "AMBISEXUAL", "SEXUALIZE", "PANSEXUAL", "HYPERSEXUAL", "INTERSEXUAL",\
                "SEX", "FUCK", "FUCKING", "SCREW", "COPULATE", "FORNICATE", "COITUS", "BANG",\
                "THREESOME", "FOURSOME", "ORGY", "ANAL", "VAGINAL", "ORAL", "GLORYHOLE", "LESBIAN", "HARDCORE", "POLEDANCE", "LAPDANCE", "TITFIGHT", "HUMPING", "SCISSORS", "HOTSHOTS"]
            self.all_words = []
            self.all_words.extend(self.breasts_words)
            self.all_words.extend(self.positions_words)
            self.all_words.extend(self.other_words)
            return
        
        def get_known_percentage(self, s_word):
            i_counter = 0
            for i_letter in s_word:
                if i_letter in self.current_guesses:
                    i_counter += 1
            return int( (i_counter * 100) / len(s_word) )





label nightbar_play_hotshots(char1):
    show screen main_game(location)
    pl "[char1.fname], would you like to play {b}HotShots{/b} with me?"

    if char1.get_action_allowed("nightbar_play_hotshots") == False:
        $ l_text = char1.get_action_not_allowed_text("nightbar_play_hotshots")
        char1.talk "[l_text]"
        return "do_return"

    if char1.get_action_allowed("anger_block") == False:
        call action_closeup (char1, location, False, False) from _call_action_closeup_31
        $ l_text = char1.get_action_not_allowed_text("anger_block")
        char1.talk "[l_text]"
        $ char1.change_anger(3)
        pl "Ummm... Yeah, sorry."
        hide screen closeup
        $ g_intimate_char = no_char
        $ location_detail = ""
        $ char1.add_action_cooldown("nightbar_play_hotshots", 4, "You just asked me the exact same thing not long ago and I already said no!")
        return "do_return"

    if char1.check_affection(2) == False:
        char1.talk "Sorry [char1.playername], but I'm not in the mood right now. Maybe another time."
        pl "That's a pity, but I understand."
        return "do_return"

    if char1.id == eva.id or char1.id == desire.id:
        $ l_zoom = 0.5
    elif True:
        $ l_zoom = 0.667

    if char1.id == aly.id:
        if player.get_quest_state("Aly_nightwear", char1) == -1:
            char1.talk "I'd love to play with you, but I don't think I have anything suitable to wear."
            pl "Ohh..."
            pause 0.3
            pl "Can I do something to help?"
            char1.talk "I don't know."
            char1.talk "If you could find me something suitable and somehow get it to the island..."
            pause 0.3
            pl "What kind of outfit do you have in mind?"
            char1.talk "Ummm... I'm not sure. Maybe something in green or black?"
            char1.talk "But it can't be just a one piece dress..."
            char1.talk "Since I've seen how {b}HotShots{/b} works, it has to have several parts."
            pl "Hmmmm... Okay."
            char1.talk "Maybe you could talk to Jennifer. She always has the best ideas concerning clothes and fashion."
            pause 0.4
            pl "I'll see what I can do."
            $ player.add_quest("Aly_nightwear", char1, char1)
            char1.talk "Thank you [char1.playername]!"
            return "do_return"
        elif player.get_quest_state("Aly_nightwear", char1) == 20:
            char1.talk "I still don't have anything suitable to wear..."
            call action_give_present (char1, location, "Aly_nightwear") from _call_action_give_present_3
            show screen main_game(location)
            call change_char_max_affection (char1, 5) from _call_change_char_max_affection_115
            $ char1.change_affection(10)
            $ char1.change_favor(20)
            $ player.set_quest_state("Aly_nightwear", char1, 100, True)
            jump nightbar_play_hotshots_change_clothes
        elif player.get_quest_state("Aly_nightwear", char1) < 100:
            char1.talk "I think we've talked about it. I need another outfit first."
            pl "You're right, sorry for asking again."
            return "do_return"

    $ menu_active = True
    $ player.smart_watch_character = char1
    char1.talk "Oh, yeah, that game. I'm sure it's going to be fun..."
    pause 0.4
    label nightbar_play_hotshots_change_clothes:
    if char1.id == aly.id and char1.nightwear == 3:
        $ g_hotshots = cl_hotshots(char1)
        $ yumiko.add_scene_seen("Hotshots_host")
        $ char1.add_scene_seen("Hotshots")
        $ char1.add_pl_interaction("others")
        $ start_scene()
        jump nightbar_play_hotshots_after_change_clothes
    $ char1.change_lust(100)
    $ char1.change_affection(100)
    $ char1.change_love(100)

    char1.talk "Let me go to my room and change clothes."
    char1.talk "I don't want to ruin this outfit by spilling a drink or something... *giggles*"
    pause 0.4
    pl "Great, I'll wait for you at the bar."
    char1.talk "Sure, I won't take long."
    $ start_scene()
    scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp" with fade:
        zoom 0.5
    $ g_hotshots = cl_hotshots(char1)
    $ yumiko.add_scene_seen("Hotshots_host")
    $ char1.add_scene_seen("Hotshots")
    $ char1.add_pl_interaction("others")
    "You chat with Yumiko for some time before [char1.fname] comes back."
    "Which is almost 30 minutes later..."
    call actions_used (1) from _call_actions_used_53

    play music ["music/nightbar1.mp3", "music/nightbar3.mp3", "music/nightbar2.mp3", "music/nightbar5.mp3", "music/nightbar4.mp3"] loop fadeout 0.7 fadein 0.7
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
        zoom l_zoom
    with fade
    pause 0.8
    if char1.id == aly.id:
        char1.talk "Now you see how the outfit looks when I wear it!"
        pause 0.4
        char1.talk "I hope it looks as good as you imagined."
        pause 0.5
        pl "Oh Wow! Yes it looks really spectacular!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with dissolve:
            zoom 0.5
        char1.talk "You need to take a look at the boots! I love them!"
        pause 0.3
        pl "Ummm... Yeah, the boots..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            subpixel True
            zoom 0.5
            ease 1.7 zoom 0.9 xpos -650 ypos -60
        pause 2.3
        pl "*gulp* {w}Yes, your boobs are incredible!"
        pause 0.3
        char1.talk "Er... What?"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            zoom 0.9 xpos -650 ypos -60
            ease 1.5 zoom 0.5 xpos 0 ypos 0
        pause 2.0
        pl "I really love the boots. *smiling*"
        pause 0.3
        char1.talk "Oh, thank you! I thought you said something else..."
        pause 0.4
        pl "Ummm... No, no, why? It's really an incredible pair. *smiling*"
        pause 0.3
        char1.talk "*laughs* Very funny... I knew I heard you say boobs!"
        pause 0.3
        pl "Er... Maybe... *smiling*"

    elif char1.id == amy.id:
        char1.talk "I hope it was worth the wait [char1.playername]. *smirks*"
        pause 0.3
        pl "Wow [char1.fname], OMG! {w}What an outfit!"
        char1.talk "I checked my butt in the mirror and I think it looks fantastic in these tight shorts."
        char1.talk "Don't you agree?"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 0.667
            ease 1.4 zoom 1.0 xpos -550 ypos -360
        pause 2.0
        pl "*gulp* Yes, definitely!"
        char1.talk "And the push-up bra really makes my babies look huge... *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 1.0 xpos -550 ypos -360
            linear 1.0 zoom 1.0 xpos -550 ypos 0
        pause 1.4
        pl "Ummm... Yeah I guess..."
        char1.talk "I think it's gonna make it that much easier for me to win when you're distracted like this... *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 1.0 xpos -550 ypos 0
            ease 1.0 zoom 0.667 xpos 0
        pause 1.3

    elif char1.id == brenda.id:
        char1.talk "I hope I didn't make you wait for too long [char1.playername]."
        pause 0.4
        pl "No, not at all. *smiling*"
        pl "Oh wow! The skirt looks great on you [char1.fname]."
        pause 0.3
        char1.talk "Only the skirt? *smiles back*"
        pause 0.4
        pl "No, no... Everything on you looks incredible... *lamely*"
        "She just smiles back..."
        "You can't help taking a closer look at her incredible ass..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 0.667
            ease 1.5 zoom 1.0 xpos -500 ypos -360
        pause 2.0
        "...before you imagine how her round butt must look without the skirt."
        "She's probably wearing red panties..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_butt.webp") with dissolve15:
            zoom 1.0 xpos -500 ypos -360
        pause 2.0
        "You stare at her ass for another moment, before looking back at her face."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp") with dissolve3:
            zoom 1.0 xpos -500 ypos -360
        pause 0.5
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 1.0 xpos -500 ypos -360
            ease 1.2 zoom 1.0 xpos -500 ypos 0
        pause 1.7

    elif char1.id == desire.id:
        char1.talk "Hey [char1.playername], I hope Yumiko kept you company while you had to wait for me. *smiles*"
        pl "Oh... Yes, she did."
        "Holy shit, look at that top!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 0.5
            ease 1.5 zoom 1.0 xpos -800 ypos -80
        $ renpy.pause(2.0, hard=True)
        $ player.change_lust(char1.sexiness-2)
        "Noticing you staring at her chest..."
        char1.talk "I got that top before my implants..."
        if char1.breast_type_known == False:
            "Interesting... Now you know she got implants."
            $ char1.breast_type_known = True
        char1.talk "It might be just a little too small now. *winks*"
        char1.talk "I mean, it wasn't always showing underboobs..."
        pause 0.6
        if player.get_quest_state("Desire_at_university", char1) == -1:
            pl "Oh... {w}You must be quite fond of it to have kept it for so long."
            char1.talk "Yes I am. It reminds me of my time at the university."
            char1.talk "Where I had that thing with the young professor going..."
            pause 0.5
            char1.talk "I mean, I was already good looking without the implants. *winks*"
            pause 0.5
            pl "I don't doubt that for a second. *smiles*"
            char1.talk "I might even have some pictures on my phone from that time..."
            pl "Are you going to tell me about your time at university and that thing between you and your professor?"
            pause 0.5
            char1.talk "Maybe later. But if you like, I'll check my phone and send you a picture."
            pl "I'd love that."
            char1.talk "Okay. *smiles*"
            $ char1.add_queued_sexting(500,529,30)
            $ player.add_quest("Desire_at_university", char1, char1)
            pause 0.6
            char1.talk "Another reason I'm still wearing it, is that I think it looks super hot on me. *grins*"
        elif True:
            char1.talk "I'm still wearing it, because I think that it looks super hot on me. *grins*"
        char1.talk "And it's really tight, so it doesn't even ride up when I stretch. *smiles*"
        char1.talk "Just look!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with fade:
            zoom 0.5
        pause 0.8
        pl "{b}Wow{/b}!"
        pause 0.2
        char1.talk "*smiles*"
        pause 0.3
        char1.talk "I guess that means you like the outfit I've selected for the game?"
        pause 0.5
        pl "*gulp* Yes, I love it!"
        pl "You look mind blowing wearing it!"
        pause 0.5
        $ char1.change_affection(5)
        char1.talk "Thank you. *smiles*"
        char1.talk "Playing {b}Hotshots{/b} is really great to see how well you know me by now. *smiles*"
        "She takes a step towards you, giving you a seductive look..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with fade:
            zoom 0.667 xpos -700
        pause 0.8
        char1.talk "If you want to see my naked boobs, you'll have to win a bunch of rounds. *smirks*"
        char1.talk "I'm pretty sure you'd like that. *grins*"
        "You let your eyes wander down to her impressive cleavage..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp"):
            zoom 0.667 xpos -700
            ease 2.0 xpos -750 ypos -720
        $ renpy.pause(2.4,hard=True)
        "Oh yeah! Your dick would really love it between those mounds!"
        $ player.change_lust(char1.sexiness)
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with dissolve10:
            zoom 0.334
        pause 0.7
        pl "I bet you know the answer to that question already. *grinning*"
        char1.talk "Yes I do. *smiles*"

    elif char1.id == eva.id:
        "You watch [char1.fname] walking down the stairs into the bar,\nwhen she hesitates on the last step and takes a short moment to smile at you."
        pl "{b}OMG! Wow!{/b}"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with fade:
            zoom 0.5
        pause 0.8
        char1.talk "Hello [char1.playername]!"
        pl "Hey [char1.fname]."
        char1.talk "I hope you like the outfit I selected for the game."
        pause 0.5
        pl "Yes, absolutely! It's super hot!"
        "You take the chance to get a good look at her gravity-defying knockers."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            subpixel True zoom 0.5
            ease 1.7 zoom 1.0 xpos -900 ypos -120
        $ renpy.pause(2.2,hard=True)
        $ player.change_lust(char1.sexiness)
        char1.talk "Don't get hard before the game starts. *smirks*"
        pause 0.5
        pl "Ummm... Yeah... *sheepishly*"
        char1.talk "Time to sit down... *chuckles*"
        "She turns around and..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with fade:
            zoom 0.5
        pause 0.8
        "...shows off her perfectly round ass."
        $ player.change_lust(char1.sexiness-2)
        pause 0.4
        "Yeah! What a spectacular view!"
        pause 0.6
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp") with fade:
            zoom 0.5
        pause 0.8
        char1.talk "Like what you see?"
        pause 0.4
        pl "Oh... Sure. I couldn't find anything to complain about even if I wanted to. *grinning*"
        pause 0.4
        char1.talk "Play well and you're going to see a lot more. *smiles*"
        pl "Trust me, I'll try my best. *smiling back*"

    elif char1.id == faye.id:
        "You stare at [char1.fname] walking down the stairs into the bar."
        pl "{b}Wow!{/b}"
        "[char1.fname] just smiles..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with fade:
            zoom 0.667
        pause 0.8
        char1.talk "Hey [char1.playername]!"
        pl "Hello [char1.fname]."
        pause 0.4
        char1.talk "I hope the wait wasn't too long."
        pl "Er... No, it's fine."
        char1.talk "Do you like my outfit, especially the semi-transparent top? *smiles*"
        pl "Yeah, definitely!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            subpixel True zoom 0.667
            ease 2.0 zoom 1.33 xpos -1050 ypos -50
        $ renpy.pause(2.4,hard=True)
        "You stare in awe at her huge tits that are clearly visible under the net top."
        $ player.change_lust(char1.sexiness)
        char1.talk "So I guess I made the right choice with this outfit."
        pause 0.5
        char1.talk "Since some of the girls were comparing my breasts to volleyballs... *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with dissolve:
            zoom 0.667
        pause 0.8
        char1.talk "I'm not really sure that's a fair comparison."
        char1.talk "Yumiko, can you hand me the volleyball please."
        yumiko.talk "So it was you who put it under the counter..."
        char1.talk "Yes, guilty as charged. *smiles*"
        yumiko.talk "Not really sure what you want with it, but here it is."
        char1.talk "Thank you."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp") with fade:
            zoom 0.667
        pause 0.8
        char1.talk "What do you think [char1.playername]?"
        char1.talk "Was it fair to compare my breasts to volleyballs?"
        "You stare at her enormous tits, easily dwarfing the volleyball..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp"):
            subpixel True zoom 0.667
            ease 2.0 zoom 1.33 xpos -950 ypos -150
        $ renpy.pause(2.4,hard=True)
        pl "Ummm... No, I don't think so..."
        pl "The volleyball looks kind of small and insignificant beside your chest."
        char1.talk "*giggles* Just what I thought."
        char1.talk "So I guess that means you're sufficiently motivated to win this game. *smirks*"
        pl "Definitely! *smiling*"
        char1.talk "Yumiko, can you please take the ball and put it under the counter again."
        yumiko.talk "Sure."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with fade:
            zoom 0.667
        pause 0.8
        char1.talk "Thank you."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with dissolve:
            subpixel True zoom 1.1 xpos -832 ypos -50
        pause 0.6

    elif char1.id == heather.id:
        char1.talk "Hi [char1.playername]! I'm sorry that I've made you wait."
        char1.talk "It wasn't easy to find something layered in my wardrobe to be able to properly {i}undress{/i}. *smiles*"
        pause 0.5
        pl "No problem at all."
        pause 0.4
        char1.talk "Do you like my outfit?"
        pause 0.4
        pl "Oh yes, I mean the dress is incredible."
        "You wonder how she managed to put it on. It must be some super stretchy material..."
        char1.talk "Would you like to see the back?"
        pl "Of course!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with dissolve:
            zoom 0.5
        pause 0.8
        "In contrast to her small waist, her booty looks really impressive."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            zoom 0.5
            ease 2.0 zoom 1.0 xpos -900 ypos -720
        pause 2.8
        pl "Your boot... {w}er... I mean {i}boots{/i} are really nice too."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            zoom 1.0 xpos -900 ypos -720
            ease 3.0 zoom 1.0 xpos -900 ypos -150
        pause 3.8
        "Damn those tits! Despite being squeezed into the dress, they're impossible to miss..."
        "...even from behind."
        pl "Ummm... I'm looking forward to get to know you a little better playing the game."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with dissolve:
            zoom 0.5
        pause 0.8
        char1.talk "That's sweet of you to say, but I'm pretty sure you're even more looking forward to seeing my huge {b}J cups{/b} exposed! *smiles*"
        pause 0.5
        call show_image_sequence ("scenes/Heather/nightbar/anim/Heather_nightbar_hs0_bg.webp", "scenes/Heather/nightbar/anim/Heather_nightbar_hs0_[number].webp", 1, 19, 0.12, 0.667, 0.667) from _call_show_image_sequence_1
        pause 0.4
        pl "Ummm... Wow!"
        "You stare at her jiggling tits for a moment..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp"):
            zoom 0.5
            ease 2.0 zoom 1.0 xpos -1000 ypos -600
        pause 2.6
        "...before looking back at her face to answer."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp"):
            zoom 1.0 xpos -1000 ypos -600
            ease 2.0 zoom 1.0 xpos -1000 ypos 0
        pause 2.6
        pl "Yeah, I wouldn't mind that either!"
        char1.talk "If you're good at the game you might even get an eyeful. *smirks*"
        pl "We'll find out soon enough. *smiling*"

    elif char1.id == jessica.id:
        char1.talk "Hello [char1.playername]!"
        char1.talk "I guess we're lucky that I just turned 18 yesterday, or we couldn't play this drinking game."
        char1.talk "I just came back from school and didn't have time to change."
        char1.talk "I hope you don't mind too much."
        pause 0.5
        pl "{b}Oh wow!{/b} {w}I mean you look great and I don't mind at all."
        if alice.get_appointment_seen("Reward_sg") == True:
            pl "Ummm... Somehow your outfit looks familiar."
            char1.talk "You noticed!"
            char1.talk "That's because Alice and I attended the same school."
            char1.talk "So she has the same school uniform."
            char1.talk "Yes, and her tits are almost as big as mine. *smirks*"
            pl "Er... *gulp*"
        pause 0.4
        char1.talk "We have to wear the school uniform on campus you know."
        char1.talk "Although it's quite distracting for some of the teachers... *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            subpixel True zoom 0.667
            ease 2.0 zoom 1.1 xpos -600 ypos -20
        pause 2.4
        pl "I can see why it might be! *chuckles*"
        char1.talk "They probably didn't have {b}me{/b} on their minds when they designed it. *giggles some more*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "Oh! The knot is almost loose again!"
        char1.talk "No matter how often I fix it... {w}Doesn't take long to almost come undone again."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with dissolve:
            zoom 0.5
        pause 0.7
        char1.talk "Yeah well, they probably consider C cups huge... *smirks*"
        char1.talk "Let me just pull it tight."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp"):
            subpixel True zoom 0.5
            ease 1.8 zoom 0.75 xpos -500
        pause 2.0
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_3.webp") with dissolve10:
            subpixel True zoom 0.75 xpos -500
        pause 1.2
        char1.talk "Yes, that's much better."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_4.webp") with dissolve10:
            subpixel True zoom 0.75 xpos -500
        pause 1.2
        char1.talk "Now it gives a nice push-up effect, don't you agree?"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_4.webp"):
            subpixel True zoom 0.75 xpos -500
            ease 1.6 zoom 1.0 xpos -900 ypos -150
        pause 2.0
        pl "Ummm... Yes, I guess."
        $ player.change_lust(char1.sexiness)
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_4.webp"):
            subpixel True zoom 1.0 xpos -900 ypos -150
            ease 5.5 zoom 1.25 xpos -1300 ypos -400
        pause 1.5
        char1.talk "My biology teacher Mr. Norton looked at my top several times today... *musing*"
        char1.talk "...probably the knot was loose again."
        char1.talk "Strange that he didn't say anything."
        pause 0.6
        pl "I'm sure it must have been the tie... *chuckles*"
        char1.talk "Oh? Is it loose again already?"
        pl "Not that I can see."
        char1.talk "Okay... Just asking, because you were looking at my chest..."
        char1.talk "...just like Mr. Norton."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_4.webp") with dissolve:
            zoom 0.75 xpos -400
        pause 0.6
        pl "I'm sorry!"
        char1.talk "Ummm... Why?"
        pause 0.4
        char1.talk "Can we start with the game now?"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_5.webp") with dissolve:
            zoom 0.5
        pause 0.6
        char1.talk "I can't wait to get my first drink. *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_5.webp"):
            zoom 0.5
            ease 1.8 zoom 0.667 xpos -300
        pause 2.0
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_6.webp") with dissolve10:
            zoom 0.5
        pause 1.2
        char1.talk "[char1.playername]?"
        pl "Yes?"
        char1.talk "Would you pour me a glass?"
        char1.talk "I hope you don't mind doing it while I lean on the counter..."
        pause 0.3
        char1.talk "Please?!"
        pl "Yes sure. {w}Ummm... I hope you don't mind, Yumiko?"
        yumiko.talk "Not at all, go ahead. *smiles*"
        "You walk around [char1.fname] and go behind the bar to get the drink."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_6.webp"):
            zoom 0.5
            ease 2.8 zoom 1.0 xpos -1150 ypos -400
        pause 2.4
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_7.webp") with fade:
            zoom 0.667
        pause 0.8
        "You pick a bottle from the shelf and pour a glass."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_7.webp"):
            zoom 0.667
            ease 1.3 zoom 1.0 xpos -500 ypos -100
        pause 1.4
        "When you turn around, glass in hand, [char1.fname] is chatting with one of the girls..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_8.webp") with fade:
            zoom 0.5
        pause 0.3
        "... which gives you a nice unobstructed view of her deep cleavage."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_8.webp"):
            zoom 0.5
            ease 2.1 zoom 1.0 xpos -700 ypos -720
            pause 1.5
            linear 1.0 zoom 0.75 xpos -350 ypos -200
            linear 0.9 zoom 0.5 xpos 0 ypos 0
        pause 5.7
        pl "Ummm... [char1.fname]! {w}Here is your drink."
        call show_image_sequence ("", "scenes/Jessica/nightbar/anim/Jessica_nightbar_hs0_9_[number].webp", 1, 7, 0.16, 1.0, 0.5) from _call_show_image_sequence_3
        pause 0.6
        char1.talk "Since we have the alcohol now... *grins*"
        char1.talk "Are you ready to lose to a super busty school girl? *smiles*"
        pause 0.4
        pl "We'll see about the losing part. *smiling*"

    elif char1.id == yvette.id:
        char1.talk "Hey [char1.playername]! I found this in my wardrobe. I hope you like it!"
        pause 0.3
        pl "Wow, yes! Definitely!"
        "You really don't know where to look first..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 0.667
            ease 1.0 zoom 1.0 xpos -600
        pause 1.5
        "Now wait... Something is different..."
        pl "Ummm... Your hair is red... How did you...?"
        pause 0.3
        char1.talk "You noticed it right away! *smiles*"
        pause 0.2
        char1.talk "Just wanted to try something different for tonight."
        char1.talk "It's one of those quick colors. You only need to wash your hair once and it comes out!"
        char1.talk "You like it?"
        pause 0.4
        pl "Yes, very much! It's not for everyday, but it's cute!"
        char1.talk "Thank you!"
        pause 0.4
        char1.talk "And the outfit?"
        "You let your eyes slide down to her amazing chest and abs..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp"):
            zoom 1.0 xpos -600
            ease 2.0 zoom 1.0 xpos -600 ypos -360
        pause 2.8
        "Shit! She must be wearing a padded bra or something. Her tits look gigantic in the sweater."
        $ player.change_lust(char1.sexiness - 2)
        "Trying not to be too obvious, you look at her exposed abs."
        pause 0.4
        "She mistakes your hesitation to answer..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp") with dissolve:
            zoom 0.667
        pause 0.5
        char1.talk "You think the sweater is too small?"
        pause 0.3
        char1.talk "Hmmm... Maybe *musing*"
        char1.talk "If I tried to pull it down a bit..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with dissolve:
            zoom 0.5
        pause 0.8
        "You stare wide eyed at her now exposed cleavage..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp"):
            subpixel True
            zoom 0.5
            ease 1.5 zoom 0.9 xpos -700 ypos -50
        pause 1.9
        char1.talk "*giggles* That's not much better I guess."
        pl "Ummm... It's different, but incredibly sexy too!"
        $ player.change_lust(char1.sexiness)
        pause 0.3
        char1.talk "I probably shouldn't wear padded bras with my {b}J cups{/b}..."
        char1.talk "Normally the sweater really isn't that small."
        char1.talk "But since we're playing an undressing game, I wanted to come prepared and not half naked. *giggles some more*"
        pause 0.3
        char1.talk "Well I guess that didn't really work out."
        pause 0.4
        char1.talk "But at least I got you distracted, which makes it easier for me to win. *smiles*"
        "She turns around towards the bar."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with dissolve:
            zoom 0.667
    elif True:
        char1.talk "Hey [char1.playername]! I'm back."
        pause 0.3
        pl "Wow [char1.fname], you look spectacular!"
        char1.talk "Thank you. *smiles*"

    pause 0.5
    char1.talk "Can we sit at the bar while we play?"
    pl "Sure, works fine for me."
    if char1.id == yvette.id:
        "Damn! Everything on her looks incredible!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp"):
            zoom 0.667
            ease 1.0 zoom 1.0 xpos -500 ypos -300
        pause 1.4
        "How her firm ass is squeezed into the jeans shorts, almost bursting out!"

    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
        zoom l_zoom
    pause 0.8

    if char1.id == amy.id:
        "You can't resist taking a closer look at her amazing cleavage!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp"):
            zoom 0.667
            ease 1.0 zoom 1.0 xpos -500 ypos -250
        pause 1.4
        "Holy shit!"
        $ player.change_lust(char1.sexiness)
        char1.talk "*giggles* I knew it... You're already distracted! *smiles*"
        pause 0.3
        pl "Er... Yes, maybe a little. *smiling*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with dissolve:
            zoom 0.667
        pause 0.7
    elif char1.id == renee.id:
        "You can't resist taking a closer look at her incredible legs!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1_legs.webp"):
            zoom 0.667
            ease 2.0 zoom 1.0 xpos -500 ypos -360
        pause 3.0
        char1.talk "Is there something wrong with my shoes?"
        pause 0.3
        pl "Ummm... No, not at all..."
        pause 0.4
        pl "I was just..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with dissolve:
            zoom 0.667
        char1.talk "Checking out my muscular legs? *smiles"
        pause 0.3
        pl "Err Yeah... *lamely*"
        pause 0.3
        char1.talk "I guess we're going to have a lot of fun! *giggles*"
        pause 0.5
    elif char1.id == eva.id:
        "You can't resist taking a closer look at her knockers..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp"):
            zoom 0.5
            ease 1.5 zoom 1.0 xpos -800 ypos -400
        $ renpy.pause(2.2,hard=True)
        char1.talk "You like my diamond necklace? *smirks*"
        $ player.change_lust(char1.sexiness)
        pl "*gulp*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with dissolve:
            zoom 0.5
        pause 0.7
        pl "Er.. Yeah, it's really nice."

    char1.talk "?"

    if renpy.random.randint(0,1) == 0:
        pl "If it's all the same to you, I'll start this time!"
        char1.talk "Sure, go ahead!"
        $ g_hotshots.who_plays = "P"
    elif True:
        pl "Please go ahead and start."
        char1.talk "Okay great. Thank you!"
        $ g_hotshots.who_plays = "G"

    scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp" with dissolve:
        zoom 0.5
    yumiko.talk "Hey! I love {b}HotShots{/b}! You need someone to spin the wheel?"
    yumiko.talk "Please let me do that for you. *smiles*"
    pause 0.3
    pl "Sure Yumiko! It's going to be so much fun!"
    char1.talk "Thanks sweetie! That's nice of you to offer."
    pause 0.3
    "Yumiko walks to the wheel..."


    label nightbar_play_hotshots_start_loop:
    hide screen nightbar_hotshots_stats
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_hs1.webp"):
        zoom 0.667
    with fade
    pause 0.7
    if g_hotshots.who_plays == "G":
        yumiko.talk "It's [char1.fname]'s turn!"
    elif True:
        yumiko.talk "It's [char1.playername]'s turn!"
    pause 0.3
    yumiko.talk "Let's spin the wheel!"
    $ g_hotshots.select_subgame()
    show expression (Movie(channel="vid", play= "scenes/Yumiko/nightbar/Yumiko_nightbar_hs_v1.webm")) with dissolve:
        zoom 0.667
    pause 1.7
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_hs_wheel_result" + unicode(g_hotshots.current_game.id) + ".webp") with dissolve10:
        zoom 0.667
        pause 0.8
        ease 0.8 zoom 0.85 xpos -250
    pause 1.8
    if g_cheats_enabled == False:
        $ renpy.block_rollback()
    if g_hotshots.current_game.id == 1:
        yumiko.talk "Hey! You're lucky, it's an {b}Auto-win{/b}!"
    elif g_hotshots.current_game.id == 2:
        yumiko.talk "Ooowww! I'm really sorry, but it's an {b}Auto-loss{/b}!"
    elif True:
        yumiko.talk "Yeah nice... It's {b}[g_hotshots.current_game.name]{/b}!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with fade:
        zoom l_zoom
    pause 0.8
    show screen nightbar_hotshots_stats


    call nightbar_hotshots_play_subgame (g_hotshots.current_game) from _call_nightbar_hotshots_play_subgame

    if g_hotshots.who_plays == "P" and _return == True:
        call nightbar_hotshots_player_won () from _call_nightbar_hotshots_player_won

    elif g_hotshots.who_plays == "P" and _return == False:
        call nightbar_hotshots_player_lost () from _call_nightbar_hotshots_player_lost

    elif g_hotshots.who_plays == "G" and _return == True:
        "[char1.fname] succeeded!"
        call nightbar_hotshots_player_lost () from _call_nightbar_hotshots_player_lost_1

    elif g_hotshots.who_plays == "G" and _return == False:
        "[char1.fname] failed!"
        call nightbar_hotshots_player_won () from _call_nightbar_hotshots_player_won_1

    $ l_sex = False
    if g_hotshots.heat >= 100:
        call nightbar_hotshots_heat (char1) from _call_nightbar_hotshots_heat
        jump nightbar_play_hotshots_end
    elif g_hotshots.opponent_drunk >= 100:
        jump nightbar_play_hotshots_girlpassout_end
    elif g_hotshots.player_drunk >= 100:
        jump nightbar_play_hotshots_girlpassout_end #nightbar_play_hotshots_player_end

    $ g_hotshots.switch_who_plays()
    jump nightbar_play_hotshots_start_loop


    label nightbar_play_hotshots_girlpassout_end:
        "[char1.fname] passed out.\n{b}Game over{/b}!"
        hide screen nightbar_hotshots_stats
        "...about half an hour later she wakes up again."
        call actions_used (1) from _call_actions_used_166
        char1.talk "Ummm... Wow! That was a bit too much I guess!"
        jump nightbar_play_hotshots_end

    label nightbar_play_hotshots_player_end:
        scene expression "gui/black.jpg" with fade
        pause 1.0
        "You passed out.\n{b}Game over{/b}!"
        hide screen nightbar_hotshots_stats
        "...about half an hour later you wake up again."
        call actions_used (1) from _call_actions_used_167
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
            zoom l_zoom
        pause 0.7
        "[char1.fname] has dressed in the meantime."
        pl "Ummm... Wow! That was a bit too much I guess!"
        pause 0.4
        char1.talk "*giggles* Yes, definitely!"
        pause 0.5

    label nightbar_play_hotshots_end:
    if g_hotshots.opponent_undress == g_hotshots.opponent_max_undress:
        $ char1.add_scene_seen("Hotshots_undressed")
    call actions_used (1) from _call_actions_used_109
    if g_hotshots.heat >= 100 and char1.id == aly.id:
        char1.talk "I'll have that shower now. *smiles*"
        char1.talk "Enjoy the rest of your evening [char1.playername]!"
        pl "You too [char1.fname]!"
        scene expression "locations/loc_nightbar_main.webp" with fade:
            zoom 0.5
        pause 0.5
        "[char1.fname] has left the night bar."
        "You text Yumiko the {i}all clear{/i} and thank her again."
        "A short time later, Yumiko and the girls are back..."
        $ char1.locations[actions_left-3] = char1.fname + "_room"
        $ char1.locations[actions_left-4] = char1.fname + "_room"
        $ char1.add_action_cooldown("nightbar_play_hotshots", 125, "We already played not too long ago. Please ask me again later.")
        $ player.add_action_cooldown("nightbar_play_hotshots", 30, "You already played {b}HotShots{/b} today, let's do something else!")
    elif g_hotshots.heat >= 100 and char1.id == heather.id:
        char1.talk "I'll wait for you in my room. *smiles*"
        char1.talk "See you in an hour [char1.playername]!"
        $ char1.add_action_cooldown("hotshots_reward", 4)
        $ char1.add_action_cooldown("hotshots_reward_valid", 12)
        $ player.add_quest("Heather_hotshots_reward", char1, char1)
        pl "Sure! *smiling back*"
        $ char1.locations[actions_left-3] = char1.fname + "_room"
        $ char1.locations[actions_left-4] = char1.fname + "_room"
        $ char1.locations[actions_left-5] = char1.fname + "_room"
        $ char1.locations[actions_left-6] = char1.fname + "_room"
        $ char1.locations[actions_left-7] = char1.fname + "_room"
        $ char1.locations[actions_left-8] = char1.fname + "_room"
        $ char1.add_action_cooldown("nightbar_play_hotshots", 125, "We already played not too long ago. Please ask me again later.")
        $ player.add_action_cooldown("nightbar_play_hotshots", 30, "You already played {b}HotShots{/b} today, let's do something else!")
        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp" with fade:
            zoom 0.5
        pause 0.5
        "[char1.fname] has left the night bar."
    elif True:
        if l_sex == False:
            char1.talk "I'll go back to my room and change."
            char1.talk "Enjoy the rest of your evening [char1.playername]!"
            pl "You too [char1.fname]!"
            $ char1.locations[actions_left-3] = char1.fname + "_room"
            $ char1.locations[actions_left-4] = char1.fname + "_room"
            $ char1.add_action_cooldown("nightbar_play_hotshots", 125, "We already played not too long ago. Please ask me again later.")
            $ player.add_action_cooldown("nightbar_play_hotshots", 30, "You already played {b}HotShots{/b} today, let's do something else!")
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp" with fade:
                zoom 0.5
            pause 0.5
            "[char1.fname] has left the night bar."
    $ menu_active = False
    $ selected_char = no_char
    call create_list_of_chars_display () from _call_create_list_of_chars_display_12
    $ stop_scene()
    return "nothing"





label nightbar_hotshots_play_subgame(i_subgame):
    if i_subgame.id == 1:
        return True
    elif i_subgame.id == 2:
        return False
    elif i_subgame.id == 3:
        call nightbar_hotshots_play_question ("personal") from _call_nightbar_hotshots_play_question
        return _return
    elif i_subgame.id == 4:
        call nightbar_hotshots_play_question ("soft") from _call_nightbar_hotshots_play_question_1
        return _return
    elif i_subgame.id == 5:
        call nightbar_hotshots_play_question ("hard") from _call_nightbar_hotshots_play_question_2
        return _return
    elif i_subgame.id == 6:
        call nightbar_hotshots_play_hangman () from _call_nightbar_hotshots_play_hangman
        return _return
    elif i_subgame.id == 7:
        call nightbar_hotshots_play_quarters () from _call_nightbar_hotshots_play_quarters
        return _return





label nightbar_hotshots_player_lost():
    "Now [char1.fname] can choose if you drink or undress."
    if g_hotshots.player_undress >= g_hotshots.player_max_undress:
        char1.talk "Mmmm... You're almost naked already... "
        char1.talk "Time to see you completely naked! *smirks*"
        char1.talk "It's a really tempting idea... {w}but no... {w}not yet!"
        char1.talk "For now just have a drink. It's on me! *giggles*"
        call nightbar_hotshots_player_drinks () from _call_nightbar_hotshots_player_drinks
    elif True:
        if renpy.random.randint(1,100) >= 60 and (g_hotshots.player_undress >= 2 or g_hotshots.player_drunk < 50):
            char1.talk "Hey [char1.playername], please have a drink!"
            call nightbar_hotshots_player_drinks () from _call_nightbar_hotshots_player_drinks_1
        elif True:
            if g_hotshots.player_undress > 1:
                char1.talk "I'd really love to see you strip some more!"
            elif True:
                char1.talk "I'd really love to see you strip some!"
            pl "Okay, fair is fair!"
            scene expression ("scenes/Player/nightbar/Player_nightbar_hs[g_hotshots.player_undress].webp") with fade:
                zoom 0.667
            pause 0.8
            $ l_player_undress_new = g_hotshots.player_undress + 1
            $ l_text = g_hotshots.get_random_text("strip_encourage_player", g_hotshots.player_undress - 1)
            yumiko.talk "[l_text]"
            "More cheers from the ladies..."
            scene expression ("scenes/Player/nightbar/Player_nightbar_hs[l_player_undress_new].webp") with fade:
                zoom 0.667
            pause 1.2
            $ g_hotshots.player_undress += 1
            pl "Okay, that's as far as it goes right now!"
            pause 0.5
            $ g_hotshots.heat += player.looks + g_hotshots.player_undress + int(char1.lust / 15)
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with fade:
                zoom l_zoom
            pause 0.8
            char1.talk "Really not bad at all! *smirks*"
            $ char1.change_lust(player.looks + 2)
            show expression ("scenes/Player/nightbar/Player_nightbar_hs[g_hotshots.player_undress].webp") with fade:
                zoom 0.667
            pause 0.8
            pl "I hoped you'd say that. *chuckles*"
    return





label nightbar_hotshots_player_won():
    yumiko.talk "Now you can choose if [char1.fname] should drink or undress."
    show screen nightbar_hotshots_stats
    menu:
        "Ask her to drink a shot" if True:
            hide screen nightbar_hotshots_stats
            pl "I think this one calls for a shot... *smiling*"
            pause 0.3
            label nightbar_hotshots_player_won_drink:
            pl "Cheers [char1.fname]!"
            char1.talk "Okay - let's see how that stuff tastes..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress]_drink1a.webp") with dissolve:
                zoom l_zoom
            pause 0.8
            yumiko.talk "5, 4, 3,... *cheering her on*"
            yumiko.talk "2, 1,... down it!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress]_drink1b.webp") with dissolve:
                zoom l_zoom
            pause 0.8
            $ l_drinking_comment = g_hotshots.get_random_text("drinking_comments", int(g_hotshots.opponent_drunk / 34))
            $ l_weight_adjust = int(int(char1.weight[0:3]) / 8)
            $ l_drunk_change = random.randint(28,38) - int(char1.endurance / 10) - l_weight_adjust
            if l_drunk_change < 5:
                $ g_hotshots.opponent_drunk += 5
            elif True:
                $ g_hotshots.opponent_drunk += l_drunk_change
            char1.talk "Hmmm..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress]_drink1a.webp"):
                zoom l_zoom
            show expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_drink_empty.webp"):
                zoom l_zoom
            with dissolve
            pause 0.8
            char1.talk "[l_drinking_comment]"
            pause 0.4
            yumiko.talk "Well, really..."
            if g_hotshots.opponent_drunk >= 75:
                char1.talk "Oh wow! I guess I'm pretty drunk already..."
            elif g_hotshots.opponent_drunk >= 50:
                char1.talk "I'm slowly starting to feel the effect!"
            elif g_hotshots.opponent_drunk >= 25:
                char1.talk "I feel a little light headed..."
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with dissolve:
                zoom l_zoom
            pause 0.8
            show screen nightbar_hotshots_stats
            pl "Make sure you don't drink more than you can handle... *chuckles*"
            char1.talk "Now look who's talking..."
        "Ask her to undress" if True:

            hide screen nightbar_hotshots_stats#paslēpj statistikas ekrānu
            pl "How about you strip a bit... *smiling*"
            if g_hotshots.opponent_undress >= g_hotshots.opponent_max_undress:# Pārbauda vai meitene vēl nav izģērbta
                char1.talk "I'm almost naked already darling *giggles*"
                char1.talk "Let me take a shot instead!"
                jump nightbar_hotshots_player_won_drink
            elif True:
                if char1.lust<10:
                    char1.talk "Not so fast, cowboy..."
                    if g_hotshots.opponent_undress == 1:# Pārbaude, vai spēlētājs ir novilcis tikai vienu mantu
                        char1.talk "I'm still too sober to start undressing..."
                    elif True:
                        char1.talk "I need to drink a little bit more to undress further..."
                    char1.talk "Let me take a shot instead! *blinks*"
                    $ g_hotshots.heat -= random.randint(5,15)#Samazina "g_hotshots.heat" par nejaušu skaitli no 5 līdz 15
                    if g_hotshots.heat < 0:
                        $ g_hotshots.heat = 0
                    jump nightbar_hotshots_player_won_drink# Pārlēkšana uz "nightbar_hotshots_player_won_drink" līniju
                elif True:
                    char1.talk "Since you asked nicely and it's part of the game..."
                    $ l_text = g_hotshots.get_random_text("strip_encourage", g_hotshots.opponent_undress - 1) # Izvēlēties nejaušu tekstu no resursiem
                    yumiko.talk "[l_text]"
                    "Some cheers from the other girls..."
                    char1.talk "I'm going to pay you back for this... *giggles*"
                    pause 0.3
                    pl "Ummm... I didn't say anything..."
                    char1.talk "Relax [char1.playername], I was only joking."
                    $ l_hotshots_opponent_undress = g_hotshots.opponent_undress + 1# Iestata mainīgo, kas attiecas uz apģērba noņemšanu
                    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[l_hotshots_opponent_undress].webp") with fade:
                        zoom l_zoom
                    pause 0.8
                    $ g_hotshots.opponent_undress += 1# Palielina pretinieka  noņemtā apģērba skaitu
                    $ g_hotshots.heat += char1.sexiness + g_hotshots.opponent_undress * 2 + int(player.lust/15) # Palielina "g_hotshots.heat" vērtību pamatojoties uz seksualitāti, spēlētāja noņemtā apģērba skaitu reiz 2 un spēlētāja kārība dalīts ar 15
                    $ player.change_lust(int(char1.sexiness/2) + g_hotshots.opponent_undress * 2)
                    show screen nightbar_hotshots_stats# Parāda statistikas ekrānu
                    if len(char1.hs_undress_talk) >= g_hotshots.opponent_undress - 1:
                        $ l_talk1 = char1.hs_undress_talk[g_hotshots.opponent_undress - 2][0]#Mainīgam tiek piesaistīts nejaušs teksts par apģērba noņemšanu
                        $ l_talk2 = char1.hs_undress_talk[g_hotshots.opponent_undress - 2][1]
                        $ l_talk3 = char1.hs_undress_talk[g_hotshots.opponent_undress - 2][2]
                        char1.talk "[l_talk1]"#Meitene pasaka pirmo tekstu 
                        if l_talk2 != "":#parbauda vai teksts l_talk2 nav tukša virkne
                            pl "[l_talk2]"
                        if l_talk3 != "":#parbauda vai teksts l_talk3 nav tukša virkne
                            char1.talk "[l_talk3]"
                    elif True:#Izpildās vienmēr ja līdz tam aiziet kods
                        char1.talk "Everyone happy now?"
                        pl "I guess we are! *smiling*"
                    pause 0.4
                    yumiko.talk "We can't wait for the next round... *laughs*"
    return





label nightbar_hotshots_player_drinks():
    pl "Just one... *chuckles*"
    scene expression ("scenes/Player/nightbar/Player_nightbar_hs[g_hotshots.player_undress]_drink1a.webp") with fade:
        zoom 0.667
    pause 0.8
    pl "No problem! Here you go!"
    scene expression ("scenes/Player/nightbar/Player_nightbar_hs[g_hotshots.player_undress]_drink1b.webp") with dissolve:
        zoom 0.667
    pause 0.8
    $ g_hotshots.player_drunk += random.randint(25,30) - int(player.endurance / 10)
    pl "*gulp* *gulp*"
    scene expression ("scenes/Player/nightbar/Player_nightbar_hs[g_hotshots.player_undress]_drink1a.webp"):
        zoom 0.667
    show expression ("scenes/Player/nightbar/Player_nightbar_hs0_drink_empty.webp"):
        zoom 0.667
    with dissolve
    pause 0.8
    pl "Now that wasn't so bad! *chuckles*"
    show expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with fade:
        zoom l_zoom
    pause 0.8
    char1.talk "Ha ha, if you say so! *smirks*"
    if renpy.random.randint(1,100) > 50:
        $ player.add_effect("drunk")
    return





label nightbar_hotshots_play_hangman():
    $ hs_hangman = cl_hangman()

    if g_hotshots.who_plays == "P":
        $ secret_word = random.choice(hs_hangman.all_words)
        if g_cheats_enabled == False:
            $ renpy.block_rollback()
        show screen nightbar_hotshots_play_hangman(secret_word)

        label nightbar_hotshots_play_hangman_start_loop:
        $ i_guess = renpy.input("Guess a letter (only English alphabet):").upper()
        if len(i_guess) <> 1:
            "Sorry, not a valid input. Enter only one character please."
            jump nightbar_hotshots_play_hangman_start_loop
        elif i_guess not in hs_hangman.available_letters:
            "Sorry, not a valid letter. Only english alphabet characters allowed."
            jump nightbar_hotshots_play_hangman_start_loop
        elif i_guess in hs_hangman.current_guesses:
            "You already guessed this letter. Try another one."
            jump nightbar_hotshots_play_hangman_start_loop

        $ hs_hangman.current_guesses.append(i_guess)
        if i_guess not in secret_word:
            $ hs_hangman.remaining_attempts -= 1
        if hs_hangman.remaining_attempts == 0:
            hide screen nightbar_hotshots_play_hangman
            yumiko.talk "Unfortunately you didn't manage to solve it!"
            return False

        $ counter = 0
        while counter < len(secret_word):
            if (secret_word[counter:counter+1]) not in hs_hangman.current_guesses:
                jump nightbar_hotshots_play_hangman_start_loop
            $ counter += 1
        hide screen nightbar_hotshots_play_hangman
        $ g_hotshots.heat += g_hotshots.current_game.base_spiciness
        yumiko.talk "Yes, {b}[secret_word]{/b} is correct!"
        yumiko.talk "You did it! {w}You solved the Hangman!"
        call nightbar_hotshots_hangman_comments (secret_word) from _call_nightbar_hotshots_hangman_comments
        return True

        label nightbar_hotshots_play_hangman_solve:
        $ i_solution_guess = renpy.input("Time to solve then! Try to guess the secret word:")
        hide screen nightbar_hotshots_play_hangman
        if i_solution_guess.upper() == secret_word:
            $ g_hotshots.heat += g_hotshots.current_game.base_spiciness
            yumiko.talk "Yes, {b}[secret_word]{/b} is correct!"
            yumiko.talk "You did it! {w}You solved the Hangman!"
            call nightbar_hotshots_hangman_comments (secret_word) from _call_nightbar_hotshots_hangman_comments_1
            return True
        elif True:
            yumiko.talk "Unfortunately you didn't manage to solve it!"
            return False
    elif True:

        $ secret_word_sample_list = random.sample(hs_hangman.all_words, 6)
        "Choose the secret word"
        menu:
            "[secret_word_sample_list[0]]" if True:
                $ secret_word = secret_word_sample_list[0]
            "[secret_word_sample_list[1]]" if True:
                $ secret_word = secret_word_sample_list[1]
            "[secret_word_sample_list[2]]" if True:
                $ secret_word = secret_word_sample_list[2]
            "[secret_word_sample_list[3]]" if True:
                $ secret_word = secret_word_sample_list[3]
            "[secret_word_sample_list[4]]" if True:
                $ secret_word = secret_word_sample_list[4]
            "[secret_word_sample_list[5]]" if True:
                $ secret_word = secret_word_sample_list[5]
        show screen nightbar_hotshots_play_hangman(secret_word)

        label nightbar_hotshots_girl_play_hangman_start_loop:
        if random.randint(1,100) <= 15 + (char1.poker_skill * 3):
            $ i_guess = secret_word[random.randint(0, len(secret_word) - 1)]
        elif True:
            $ i_roll = random.randint(1,100)
            if i_roll <= 40 + char1.poker_skill + 1:
                $ i_guess = random.choice(['E', 'T', 'A', 'O', 'I'])
            elif i_roll <= 70 + char1.poker_skill + 1:
                $ i_guess = random.choice(['N', 'S', 'R', 'H', 'D'])
            elif i_roll <= 82 + char1.poker_skill + 1:
                $ i_guess = random.choice(['L', 'U', 'C', 'M'])
            elif i_roll <= 90 + char1.poker_skill + 1:
                $ i_guess = random.choice(['F', 'Y', 'W', 'G'])
            elif i_roll <= 97 + char1.poker_skill + 1:
                $ i_guess = random.choice(['P', 'V', 'B', 'X'])
            elif True:
                $ i_guess = random.choice(['K', 'Q', 'J', 'Z'])
        if i_guess in hs_hangman.current_guesses:
            jump nightbar_hotshots_girl_play_hangman_start_loop
        "[char1.fname] chooses the letter {b}[i_guess]{/b}!"

        $ hs_hangman.current_guesses.append(i_guess)
        if i_guess not in secret_word:
            $ hs_hangman.remaining_attempts -= 1
            if hs_hangman.remaining_attempts == 0:
                "[char1.fname] has run out of attempts!"
                hide screen nightbar_hotshots_play_hangman
                return False
        if hs_hangman.get_known_percentage(secret_word) >= 75 - (char1.poker_skill * 5):
            "[char1.fname] tries to solve..."
            char1.talk "I think it's {b}[secret_word]{/b}!"
            yumiko.talk "Yes, that's the correct answer!"
            hide screen nightbar_hotshots_play_hangman
            call nightbar_hotshots_hangman_comments (secret_word) from _call_nightbar_hotshots_hangman_comments_2
            return True

        jump nightbar_hotshots_girl_play_hangman_start_loop





label nightbar_hotshots_hangman_comments(s_word):
    if s_word in hs_hangman.breasts_words:
        $ l_text = g_hotshots.get_random_text("asking_about_boobs", int(g_hotshots.opponent_drunk / 34))
        $ l_text = l_text.replace("&s_word", s_word)
        char1.talk "[l_text]"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp"):
            zoom l_zoom
            ease 1.0 zoom l_zoom * 1.5 xpos -500 ypos -250
        $ renpy.pause(1.4, hard=True)
        $ l_text = g_hotshots.get_random_text("answer_about_boobs", int(g_hotshots.player_drunk / 34))
        pl "[l_text]"
        $ g_hotshots.heat += 3
        yumiko.talk "Okay, you're a nice couple. Could you please stop flirting and get back to the game? *smiles*"


    return





label nightbar_hotshots_play_question(i_category):
    $ l_correct_answer = False

    if g_hotshots.who_plays == "P":
        $ lo_question = g_hotshots.get_question(i_category)
        $ lo_question.question = lo_question.question.replace("&1", char1.fname)

        yumiko.talk "[lo_question.question]"
        $ g_hotshots.heat += g_hotshots.current_game.base_spiciness
        if g_cheats_enabled == False:
            $ renpy.block_rollback()
        if i_category == "hard":
            if g_hotshots.opponent_drunk < 25:
                char1.talk "Ohhh, wow! Yumiko, what kind of question is that???"
                yumiko.talk "I think it's a pretty hot one, don't you all agree?"
                pause 0.3
                pl "[char1.fname], we really want to know!"
                "Cheers from the crowd! *clap* clap*"
                pause 0.4
                char1.talk "Yeah okay..."
                yumiko.talk "So, [yumiko.playername], what do you think?"
                yumiko.talk "[lo_question.question]"
            elif g_hotshots.opponent_drunk < 50:
                char1.talk "Yumiko! Maybe I'm a bit drunk but this is still embarrassing!"
                yumiko.talk "Rules are rules darling...\nAnd honestly, we all want to know, right? *giggles*"
                pause 0.3
                pl "I do want to know!"
                t_crowd_of_girls "Hooray for [char1.fname]! *cheers and whistles from the crowd*"
                pause 0.4
                char1.talk "Okay, okay..."
                yumiko.talk "So, [yumiko.playername], what do you think?"
                yumiko.talk "[lo_question.question]"
            elif g_hotshots.opponent_drunk < 75:
                char1.talk "Damn, look what you've done! I'm not even embarrassed anymore! *laughs*"
                yumiko.talk "You look adorable when you're drunk!"
                t_crowd_of_girls "[char1.fname]! [char1.fname]! [char1.fname]!"
                pause 0.3
                pl "This is a lot of fun!"
                char1.talk "Yeah, but I'll remember what you're doing to me. I'm still not that drunk! *trying to be serious*"
                pause 0.4
                yumiko.talk "So, [yumiko.playername], what do you think?"
                yumiko.talk "[lo_question.question]"
            elif True:
                char1.talk "Okaaaay... I'mmmmm really drunk now! *laughs*{w}\nI'll tell you what you want to know! *more laughs*"
                yumiko.talk "Ha ha! You rock [char1.fname]!"
                t_crowd_of_girls "Woohoo!! [char1.fname] is the best! *someone in the crowd*"
                yumiko.talk "What do you think [yumiko.playername], doesn't she look pretty sexy right now?"
                pause 0.3
                pl "Yes, definitely! *laughing*"
                char1.talk "Sure, have your fun everyone! I guess I'm too drunk to care! *giggles*"
                yumiko.talk "[yumiko.playername], what do you think?"
                yumiko.talk "[lo_question.question]"

        $ lt_answers = lo_question.get_answers(char1)
        if g_cheats_enabled == False:
            $ renpy.block_rollback()
        menu:
            "[lt_answers[0]]" if True:
                $ l_answer_given = lt_answers[0]
            "[lt_answers[1]]" if len(lt_answers) >= 2:
                $ l_answer_given = lt_answers[1]
            "[lt_answers[2]]" if len(lt_answers) >= 3:
                $ l_answer_given = lt_answers[2]
            "[lt_answers[3]]" if len(lt_answers) >= 4:
                $ l_answer_given = lt_answers[3]
            "[lt_answers[4]]" if len(lt_answers) >= 5:
                $ l_answer_given = lt_answers[4]

        $ renpy.block_rollback()
        if l_answer_given == char1.get_hs_answer(lo_question.id).answer:
            $ l_correct_answer = True
        pause 0.6
        yumiko.talk "Please tell us [char1.fname], is {b}[l_answer_given]{/b} the correct answer?"
        if l_correct_answer == True:
            char1.talk "Yes, {b}[l_answer_given]{/b} is the correct answer!"
            $ g_hotshots.heat += char1.get_hs_answer(lo_question.id).answer_heat_bonus
            if lo_question.id == 7 and char1.body_height_known == False:
                "Interesting - now you know [char1.fname]'s height."
                $ char1.body_height_known = True
            if lo_question.id == 8 and char1.bra_size_known == False:
                "Interesting - now you know [char1.fname]'s bra size."
                $ char1.bra_size_known = True
            if lo_question.id == 10 and char1.hips_size_known == False:
                "Interesting - now you know [char1.fname]'s hips size."
                $ char1.hips_size_known = True
            if lo_question.id == 11 and char1.waist_size_known == False:
                "Interesting - now you know [char1.fname]'s waist size."
                $ char1.waist_size_known = True
            if lo_question.id == 19 and char1.age_known == False:
                "Interesting - now you know [char1.fname]'s age."
                $ char1.age_known = True
            if char1.get_hs_answer(lo_question.id).commentary_image <> "" and eval(char1.get_hs_answer(lo_question.id).commentary_image_condition):
                scene expression (char1.get_hs_answer(lo_question.id).commentary_image) with dissolve:
                    zoom 0.667
                pause 0.4
                $ g_hotshots.heat += char1.get_hs_answer(lo_question.id).image_heat_bonus
            if char1.get_hs_answer(lo_question.id).commentary <> "" and eval(char1.get_hs_answer(lo_question.id).commentary_condition):
                $ l_commentary = char1.get_hs_answer(lo_question.id).commentary
                char1.talk "[l_commentary]"
                $ g_hotshots.heat += char1.get_hs_answer(lo_question.id).commentary_heat_bonus
        elif True:
            char1.talk "No, unfortunately {b}[l_answer_given]{/b} is not the correct answer!"
        return l_correct_answer
    elif True:

        $ lo_question = g_hotshots.get_question_player(i_category)
        $ lo_question.question = lo_question.question.replace("&1", player.fname)

        yumiko.talk "[lo_question.question]"
        $ g_hotshots.heat += int(g_hotshots.current_game.base_spiciness / 2)
        if i_category == "hard":
            pl "Yumiko! That's really a personal question!"
            yumiko.talk "Yes it is. That's why we all can't wait to hear the answer!"
            pause 0.3
            char1.talk "[char1.playername], we really want to know! *smirks*"
            "Cheers from the crowd! *clap* clap*"
            pause 0.4
            pl "Okay, okay..."
            yumiko.talk "[char1.fname], what do you think?"
            yumiko.talk "[lo_question.question]"

        $ lt_answers = lo_question.get_answers(player)
        $ l_answer_options = ""

        if len(lt_answers) > 0:
            $ l_answer_options = lt_answers[0]
        if len(lt_answers) > 1:
            $ l_answer_options = l_answer_options + "{w} or " + lt_answers[1]
        if len(lt_answers) > 2:
            $ l_answer_options = l_answer_options + "{w} or " + lt_answers[2]
        if len(lt_answers) > 3:
            $ l_answer_options = l_answer_options + "{w} or " + lt_answers[3]
        if len(lt_answers) > 4:
            $ l_answer_options = l_answer_options + "{w} or " + lt_answers[4]

        $ l_answer_options = l_answer_options + "?"
        yumiko.talk "[l_answer_options]"
        yumiko.talk "Your turn to answer, [char1.fname]!"
        if lo_question.id in char1.hs_player_answers_known:
            if random.randint(1,100) <= 80:
                $ l_answer = player.get_hs_answer(lo_question.id).answer
                $ l_correct_answer = True
                char1.talk "I rememeber the answer to that question *smiles*"
                char1.talk "It's {b}[l_answer]{/b}!"
            elif True:
                $ l_answer = renpy.random.choice(lt_answers)
                if l_answer == player.get_hs_answer(lo_question.id).answer:
                    $ l_correct_answer = True
                char1.talk "Uhmmm... you already made me this question but I can't recall exactly..."
                char1.talk "Maybe {b}[l_answer]{/b}?"
        elif True:
            $ l_counter = 0
            while l_counter < int(char1.rsm[0].affection / 34) + 1:
                $ l_answer = renpy.random.choice(lt_answers)
                if l_answer == player.get_hs_answer(lo_question.id).answer:
                    $ l_correct_answer = True
                    $ l_counter = 999
                    if lo_question.id not in char1.hs_player_answers_known:
                        $ char1.hs_player_answers_known.append(lo_question.id)
                $ l_counter += 1
            if g_cheats_enabled == False:
                $ renpy.block_rollback()
            char1.talk "I think the correct answer is {b}[l_answer]{/b}!"

        yumiko.talk "Okay [yumiko.playername], is that correct?"
        if l_correct_answer == True:
            pl "Yes, {b}[l_answer]{/b} is the correct answer."
        elif True:
            pl "I'm sorry, but {b}[l_answer]{/b} is not the right answer!"
        return l_correct_answer





label nightbar_hotshots_play_quarters():
    $ direction = 0
    $ depth = 0
    $ force = 0
    $ dir_increase = True
    $ i_return = False

    if g_hotshots.who_plays == "P":
        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_take_shot.webp" with dissolve:
            zoom 0.5
        pause 0.4
        yumiko.talk "Let's see how good you are at quarters with some distractions... *giggles*"


        call screen nightbar_hotshots_play_quarters_direction
        if g_cheats_enabled == False:
            $ renpy.block_rollback()
        $ dir_increase = True
        if direction >= 47 and direction <= 53:
            "You have the feeling that you got that one just right!"


        call screen nightbar_hotshots_play_quarters_depth
        if g_cheats_enabled == False:
            $ renpy.block_rollback()
        $ dir_increase = True


        call screen nightbar_hotshots_play_quarters_force
        if g_cheats_enabled == False:
            $ renpy.block_rollback()



        hide screen nightbar_hotshots_stats
        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_miss.webp" with fade:
            zoom 0.667
        pause 0.9
        $ l_ypos = 340 + (100 - depth - force) * 3
        if l_ypos < 500 and l_ypos > 300:
            if l_ypos > 400:
                $ l_ypos = 500
            elif True:
                $ l_ypos = 300
        if direction >= 47 and direction <= 53 and depth + force >= 130 and depth + force <= 150 and renpy.random.randint(1,100) <= 33:
            $ yumiko.add_scene_seen("Hotshots_easter_egg1")
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot1.webp" with dissolve:
                zoom 0.5
            yumiko.talk "Oh my God! *giggles*"
            yumiko.talk "How did you manage a shot like this?"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot1.webp":
                zoom 0.5
                ease 1.5 zoom 1.0 xpos -700
            pause 2.0
            pl "Ummm... Sorry!"
            pl "Honestly I have no idea how it happened!"
            pl "Must have been a lucky shot! *chuckles*"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot2.webp" with dissolve:
                zoom 0.667
            pause 0.8
            yumiko.talk "*laughs* Lucky or not... You shot it in... {w}You take it out!"
            pause 0.4
            pl "Er... Okay!"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot1.webp" with dissolve:
                subpixel True
                zoom 0.7 xpos -300
            "You move your hand towards her cleavage to pick out the quarter."
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot1.webp":
                subpixel True
                zoom 0.7 xpos -300
                ease 1.5 zoom 1.25 xpos -1100
            pause 1.7
            yumiko.talk "Hey! That's too easy!"
            yumiko.talk "You have to do it without using your hands!"
            pause 0.3
            pl "How am I supposed to get it out without using my hands?"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot2.webp" with dissolve10:
                zoom 0.8 xpos -200
            pause 0.8
            yumiko.talk "I'm told you're good with your mouth... *giggles*"
            pause 0.4
            pl "Ummm... You mean..."
            yumiko.talk "Use you tongue, your teeth, your lips, whatever works best. *smirks*"
            "{b}Tongue! Lips! Yeah!{/b} *cheers from the crowd of girls*"
            pause 0.4
            yumiko.talk "Let me help you get a better angle... *winks*"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot3.webp" with dissolve:
                zoom 0.5
            pause 0.9
            "Yes! That's the spirit! *some more cheers from the girls"
            $ g_hotshots.heat += yumiko.sexiness
            yumiko.talk "You need to get closer to pull it out! *smirks*"
            "Obediently you get your mouth closer to the quarter (and her incredible cleavage)..."
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot3.webp":
                zoom 0.5
                ease 2.0 zoom 1.0 xpos -750 ypos -720
            pause 3.0
            "You stick your tongue out as far as you can to reach the quarter..."
            if g_hotshots.player_undress == 1:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot4_1.webp" with fade:
                    zoom 0.667
            elif True:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot4_2.webp" with fade:
                    zoom 0.67
            pause 0.9
            "Wow! Her cleavage is remarkably deep! {w}It's almost impossible to reach it..."
            yumiko.talk "You really think it's gonna work this way?"
            pause 0.3
            pl "I'm leeeely dyinnng..."
            yumiko.talk "It's tickling... *laughs*"
            yumiko.talk "Let me help you, or you'll never get it out!"
            if g_hotshots.player_undress == 1:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot5_1.webp" with dissolve:
                    zoom 0.667
            elif True:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot5_2.webp" with dissolve:
                    zoom 0.667
            yumiko.talk "Now you should be close enough! *giggles*"
            "Yeah! Yeah! Get him hard! *cheers from the girls*"
            $ player.change_lust(yumiko.sexiness + 2)
            $ g_hotshots.heat += yumiko.sexiness + 10
            char1.talk "But don't suffocate him, we still need him to play with us! *giggles*"
            pause 0.3
            if g_hotshots.player_undress == 1:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot5_1.webp":
                    zoom 0.667
                    ease 1.0 zoom 1.0 xpos -400 ypos -360
            elif True:
                scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot5_2.webp":
                    zoom 0.667
                    ease 1.0 zoom 1.0 xpos -400 ypos -360
            pause 1.6
            pl "*Mmmmpfff* Hmmmm..."
            pause 0.5
            yumiko.talk "You got it?"
            pause 0.4
            pl "Yeessss!"
            yumiko.talk "Does [player.fname] rock?"
            "Yeah! [player.fname] rocks! Yeah, yeah! *applause from the girls*"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot6.webp" with fade:
                zoom 0.667
            pause 1.0
            "You finally managed to get hold of the quarter with your mouth..."
            yumiko.talk "That was fun! *laughs*"
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_trick_shot2.webp" with dissolve:
                zoom 0.667
            pause 0.7
            yumiko.talk "Everyone ready to continue with the game?"
            "Yeeeessss! *cheers from the girls*"
        elif direction < 40:
            $ l_ypos = 340 + (100 - depth - force) * 3
            if l_ypos < 330:
                $ l_ypos = 330
            show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                zoom 0.8 xpos 710 - (50 - direction) * 6 ypos l_ypos
            yumiko.talk "Oh, you failed. Your shot has drifted to the left.\nBetter luck next time!"
            $ i_return = False
        elif direction > 60:
            $ l_ypos = 340 + (100 - depth - force) * 3
            if l_ypos < 350:
                $ l_ypos = 350
            show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                zoom 0.8 xpos 710 - (50 - direction) * 6 ypos l_ypos
            yumiko.talk "Oh, you failed. Your shot has drifted to the right.\nBetter luck next time!"
        elif True:
            if depth + force < 80:
                show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                    zoom 0.8 xpos 710 + (50 - direction) * 6 ypos l_ypos
                yumiko.talk "Oh, you failed! Your shot has been too short.\nBetter luck next time!"
            elif depth + force >= 120:
                show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                    zoom 0.6 xpos 710 - (50 - direction) * 6 ypos 260 + abs(direction-51)
                yumiko.talk "Oh, you failed! Your shot was too long.\nBetter luck next time!"
            elif True:
                if direction >= 47 and direction <= 53 and depth + force >= 94 and depth + force <= 106:
                    scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_hit.webp" with dissolve:
                        zoom 0.667
                    pause 0.7
                    yumiko.talk "That was a PERFECT shot! Congratulations"
                    $ i_return = True
                elif True:
                    if random.randint(0,100) >= 25:
                        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_hit.webp" with dissolve:
                            zoom 0.667
                        pause 0.7
                        yumiko.talk "Hey, Well done! You made it!"
                        $ i_return = True
                    elif True:
                        if direction >= 50:
                            show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                                zoom 0.8 xpos 840 ypos 340 + (100 - depth - force) * 3
                        elif True:
                            show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                                zoom 0.8 xpos 600 ypos 340 + (100 - depth - force) * 3
                        yumiko.talk "Oh, you failed! But it was a good shot!.\nIt probably was just bad luck."

        $ g_hotshots.heat += g_hotshots.current_game.base_spiciness
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with dissolve:
            zoom l_zoom
        pause 0.4
        return i_return
    elif True:

        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_take_shot.webp" with dissolve:
            zoom 0.5
        pause 0.4
        yumiko.talk "Okay [char1.fname]... Show us your skills with quarters."
        yumiko.talk "gambatte kudasai ne! *smiles*"

        scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_miss.webp" with fade:
            zoom 0.667
        pause 0.5

        "[char1.fname] takes a shot..."
        pause 0.7
        if random.randint(0,100) <= char1.hs_quarters_skill - int(g_hotshots.opponent_drunk / 10):
            scene expression "scenes/Yumiko/nightbar/Yumiko_nightbar_quarters_hit.webp" with dissolve:
                zoom 0.667
            pause 0.4
            yumiko.talk "Hey, well done! You made it!"
            $ experience_roll = random.randint(0,100)
            if experience_roll > char1.hs_quarters_skill and char1.hs_quarters_skill < 60:
                $ char1.hs_quarters_skill += 1
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with dissolve:
                zoom l_zoom
            pause 0.4
            return True
        elif True:
            $ fail_direction = random.choice(["left", "right"])
            if fail_direction == "left":
                show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                    zoom 0.8 xpos 610 - random.randint (0,50) ypos random.randint(300,500)
                pause 0.4
                yumiko.talk "Oh, you failed!"
                yumiko.talk "Your shot has drifted to the left.\nBetter luck next time!"
            elif fail_direction == "right":
                show expression ("locations/loc_nightbar_quarter.webp") with dissolve:
                    zoom 0.8 xpos 810 + random.randint (0,50) ypos random.randint(300,500)
                pause 0.4
                yumiko.talk "Oh, you failed!"
                yumiko.talk "Your shot has drifted to the right.\nBetter luck next time!"
            scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_undress].webp") with dissolve:
                zoom l_zoom
            pause 0.4
            return False





screen nightbar_hotshots_stats:
    $ l_undress_girl = g_hotshots.opponent_undress - 1
    $ l_max_undress_girl = g_hotshots.opponent_max_undress - 1
    $ l_undress_player = g_hotshots.player_undress - 1
    $ l_max_undress_player = g_hotshots.player_max_undress - 1
    frame:
        xsize 200 xalign 1.0 yalign 0.0
        has vbox
        text "Girl undress: [l_undress_girl] / [l_max_undress_girl]" size 15 color "#66c1e0"
        text "Player undress: [l_undress_player] / [l_max_undress_player]" size 15 color "#66c1e0"
        text ""
        text "Heat: [g_hotshots.heat]" size 15 color "#66c1e0"
        text "Player drunkenness: [g_hotshots.player_drunk]" size 15 color "#66c1e0"
        text "Girl drunkenness: [g_hotshots.opponent_drunk]" size 15 color "#66c1e0"





screen nightbar_hotshots_play_quarters_direction:
    if dir_increase:
        timer 0.01 action If ( direction < 100, SetVariable("direction", direction + 1), ToggleVariable("dir_increase") ) repeat True
    else:
        timer 0.01 action If ( direction > 0, SetVariable("direction", direction - 1), ToggleVariable("dir_increase") ) repeat True

    text "Click on the hand to set the {b}direction{/b}!" size 18 color "#66c1e0" xalign 0.98 yalign 0.95
    imagebutton idle im.FactorScale("locations/loc_nightbar_quarter2_1.webp",0.4) xpos 680 ypos 575 xanchor 0.5 yanchor 0.0
    if direction >=45 and direction <= 55:
        imagebutton idle im.FactorScale("scenes/Player/nightbar/Player_nightbar_quarters_hand_green.webp",0.5) xpos 700 ypos 600 xanchor 0.5 yanchor 0.0 action Return(direction) at myrotate(float(direction-50)*0.35)
    else:
        imagebutton idle im.FactorScale("scenes/Player/nightbar/Player_nightbar_quarters_hand.webp",0.5) xpos 700 ypos 600 xanchor 0.5 yanchor 0.0 action Return(direction) at myrotate(float(direction-50)*0.35)

screen nightbar_hotshots_play_quarters_depth:
    if dir_increase:
        timer 0.02 action If ( depth < 100, SetVariable("depth", depth + 1), ToggleVariable("dir_increase") ) repeat True
    else:
        timer 0.02 action If ( depth > 0, SetVariable("depth", depth - 1), ToggleVariable("dir_increase") ) repeat True

    text "Click on the hand to set the {b}depth{b}!" size 18 color "#66c1e0" xalign 0.98 yalign 0.95
    imagebutton idle im.FactorScale("locations/loc_nightbar_quarter2_1.webp",0.4) xpos 680 ypos 580 xanchor 0.5 yanchor 0.0
    $ l_image_select = int((depth + 5.1 ) / 10)
    if l_image_select == 0:
        $ l_image_select = 1
    imagebutton idle im.FactorScale("scenes/Player/nightbar/Player_nightbar_quarters_hand" + unicode(l_image_select) + ".webp",0.5) xpos 700 ypos 600 + l_image_select*5 xanchor 0.5 yanchor 0.0 action Return(depth)

screen nightbar_hotshots_play_quarters_force:
    if dir_increase:
        timer 0.01 action If ( force < 100, SetVariable("force", force + 1), ToggleVariable("dir_increase") ) repeat True
    else:
        timer 0.01 action If ( force > 0, SetVariable("force", force - 1), ToggleVariable("dir_increase") ) repeat True

    text "Click on the hand to set the {b}force{b}!" size 18 color "#66c1e0" xalign 0.98 yalign 0.95
    imagebutton idle im.FactorScale("locations/loc_nightbar_quarter2_1.webp",0.4) xpos 680 ypos 580 xanchor 0.5 yanchor 0.0
    $ l_image_select = int((force + 5.1 ) / 10)
    if l_image_select == 0:
        $ l_image_select = 1
    imagebutton idle im.FactorScale("scenes/Player/nightbar/Player_nightbar_quarters_hand" + unicode(l_image_select) + ".webp",0.5) xpos 700 ypos 600 + l_image_select*5 xanchor 0.5 yanchor 0.0 action Return(force)





screen nightbar_hotshots_play_hangman(secret_word):
    $ l_xalign = 0.226
    $ l_yalign = 0.0
    if persistent.use_new_ui == True:
        $ l_xalign = 0.05
        $ l_yalign = 0.15
    frame:
        xsize 400 xalign l_xalign yalign l_yalign
        has vbox
        hbox:
            xfill True
            text "{u}Guess the secret word{/u}" xalign 0.5 size 18 color "#66c1e0"
        text ""
        hbox:
            xalign 0.5 yalign 0.5
            for i_letter in secret_word:
                if i_letter in hs_hangman.current_guesses:
                    text i_letter.upper()
                else:
                    text "_"
                text "  "
        text ""
        hbox:
            xfill True yalign 1.0
            text "Remaining Attempts: [hs_hangman.remaining_attempts]" xalign 0.0 size 15 color "#66c1e0"
            if g_hotshots.who_plays == "P":
                textbutton "Solve!" action Jump("nightbar_hotshots_play_hangman_solve") xalign 1.0





label nightbar_hotshots_heat(char1):
    char1.talk "Is it just me, or is it {b}really{/b} hot in here???"
    hide screen nightbar_hotshots_stats
    pl "Ummm... *sweating a little looking at her*"
    if g_hotshots.opponent_undress <> g_hotshots.opponent_max_undress:
        char1.talk "Mmmmm... I need to get rid of some more clothes..."
        $ l_x_size,l_y_size = renpy.image_size("scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs" + unicode(g_hotshots.opponent_max_undress) + ".webp")
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_max_undress].webp") with fade:
            zoom float(1280.0/l_x_size)
        pause 0.8
        $ g_hotshots.opponent_undress = g_hotshots.opponent_max_undress
        char1.talk "Mmmmm... It's not much better..."
        char1.talk "I still feel so hot!"

    if char1.id <> renee.id and char1.id <> heather.id and char1.id <> jessica.id:
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with fade:
            zoom 0.5
        pause 0.8

    if char1.id == aly.id:
        call nightbar_hotshots_heat_aly (char1) from _call_nightbar_hotshots_heat_aly
    elif char1.id == amy.id:
        call nightbar_hotshots_heat_amy (char1) from _call_nightbar_hotshots_heat_amy
    elif char1.id == brenda.id:
        call nightbar_hotshots_heat_brenda (char1) from _call_nightbar_hotshots_heat_brenda
    elif char1.id == desire.id:
        call nightbar_hotshots_heat_desire (char1) from _call_nightbar_hotshots_heat_desire
    elif char1.id == eva.id:
        call nightbar_hotshots_heat_eva (char1) from _call_nightbar_hotshots_heat_eva
    elif char1.id == faye.id:
        call nightbar_hotshots_heat_faye (char1) from _call_nightbar_hotshots_heat_faye
    elif char1.id == heather.id:
        call nightbar_hotshots_heat_heather (char1) from _call_nightbar_hotshots_heat_heather
    elif char1.id == jessica.id:
        call nightbar_hotshots_heat_jessica (char1) from _call_nightbar_hotshots_heat_jessica
    elif char1.id == renee.id:
        call nightbar_hotshots_heat_renee (char1) from _call_nightbar_hotshots_heat_renee
    elif char1.id == yvette.id:
        call nightbar_hotshots_heat_yvette (char1) from _call_nightbar_hotshots_heat_yvette
    call actions_used (1) from _call_actions_used_110
    return _return





label nightbar_hotshots_heat_aly(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Mmmm...I feel like I'm on fire!"
    "She walks towards you, her [l_breast_size_text] swinging left and right while she does."
    pause 0.3
    char1.talk "Do you like my huge knockers? *moans*"
    pause 0.3
    pl "Yes! Wow!"
    "You let your eyes roam over her cute face and voluptuous body."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True
        zoom 0.5
        ease 2.0 zoom 1.2 xpos -1000 ypos -550
    pause 2.5
    "Oh my God! What a pair of juicy tits!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True
        zoom 1.2 xpos -1000 ypos -550
        ease 1.2 zoom 1.2 xpos -1000 ypos 0
    pause 1.6
    "Combined with such an innocent looking face..."
    $ player.change_lust(char1.sexiness+4)
    pause 0.4
    char1.talk "Would you like me to squeeze them for you?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True
        zoom 1.2 xpos -1000 ypos 0
        ease 1.2 zoom 0.7 xpos -300
    pause 1.6
    char1.talk "From the way you're staring at them, I guess that means yes! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        subpixel True
        zoom 0.65 xpos -250
    pause 1.0
    "You wonder what has gotten into the shy [char1.fname]..."
    "... not that it's a bad thing to have her all horny and seductive!"
    pause 0.4
    pl "You're incredible [char1.fname]!"
    pause 0.4
    char1.talk "Thank you [char1.playername]!"
    pause 0.5
    char1.talk "Would you like to get your hands on some of my incredibleness?"
    char1.talk "And squeeze them yourself?"
    "You've always dreamed of getting your hands on her knockers and giving them a good squeeze!"
    $ player.change_lust(char1.sexiness+6)
    pause 0.5
    pl "*gulp* I'd love to!"
    char1.talk "What are you waiting for?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp"):
        subpixel True
        zoom 0.65 xpos -250
        ease 1.4 zoom 0.9 xpos -700 ypos -400
    pause 2.0
    "You lay your hands on her incredible tits..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3a.webp") with dissolve:
        zoom 0.667
    pause 1.2
    char1.talk "And now squeeze them for me! *moans*"
    show aly_heat_animate1 with dissolve3:
        zoom 0.667
        "scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3b.webp"
        pause 0.4
        "scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3c.webp"
        pause 0.8
        "scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3b.webp"
        pause 0.4
        "scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3a.webp"
        pause 0.6
        repeat
    pause 4.0
    "Damn! How you wanted to get your hands on those balloons..."
    "... they're so huge and soft!"
    pause 1.0
    char1.talk "Mmmm... Yes... I really like that! *moans*"
    pause 1.0
    "You could do that all day, so if she enjoys it... *smiling inwardly*"
    pause 2.0
    char1.talk "Ahhh... Mmmmm... Yes!"
    "Wow! Is she really getting off just from the tit squeeze???"
    "You take a moment to look up at her face."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 0.667
    pause 0.6
    char1.talk "Mmmmm... Don't stop! *moans*"
    char1.talk "Ahhh.... OMG!"
    "When you look back down at her tits..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with dissolve:
        zoom 0.667
    pause 1.2
    "She's fingering herself!"
    "Wow! That certainly explains the moaning!"
    char1.talk "I want to fuck you with my huge tits while I pleasure myself! *moans*"
    pause 0.3
    t_crowd_of_girls "Yeah! {b}{w}[char1.fname]! {w}[char1.fname]! {w}[char1.fname]! {/b}"
    "She was completely oblivious of her surroundings..."
    "... that changed when the girls started cheering."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with dissolve:
        zoom 0.667
    pause 0.8
    char1.talk "Oh my God! they're all watching..."
    pause 0.3
    char1.talk "I can't do this while they're all staring at us!"
    pause 0.3
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 0.7
    yumiko.talk "Girls! You've heard her!"
    yumiko.talk "I guess the bar closes early today. Everyone except our two lovebirds get out!"
    pause 0.4
    t_crowd_of_girls "Boo! No! {w}Just when it started to get really interesting..."
    yumiko.talk "Okay, let's go girls!"
    yumiko.talk "[yumiko.playername], send me a text when you're done."
    pause 0.3
    pl "Ummm... Yeah, sure! And thank you Yumiko."
    yumiko.talk "No problem."
    "I doesn't take Yumiko long, to lead all the girls out..."
    scene expression ("locations/loc_nightbar_main.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "You begin to undress as soon as the bar is empty except for yourself and [char1.fname]..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with fade:
        zoom 0.667
    pause 0.5
    char1.talk "I'm sorry... But I don't know if I can continue this now..."
    pl "Ummm... really?"
    char1.talk "I don't know... That kind of killed the mood for me. *looking a bit sad*"
    pause 0.4
    pl "Please don't do this to me [char1.fname]... *pleading*"
    pause 0.4
    char1.talk "Okay, I guess it really wouldn't be fair."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp") with dissolve:
        zoom 0.667
    pause 0.7
    char1.talk "Can you play with my nipples for a bit to get me in the mood again?"
    pause 0.4
    char1.talk "They're really sensitive and I should get horny again in no time!"
    pl "Yeah! Sure! *grinning*"
    "She walks towards you, turns around and leans back against you..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with fade:
        zoom 0.667
    pause 1.2
    "...while you caress and play with her nipples."
    char1.talk "Mmmmm... *moans*"
    pause 0.4
    char1.talk "Can you feel them getting hard!"
    $ char1.change_lust(10)
    pl "Yes, definitely!"
    "Playing with her nipples and her moaning and dirty talk really turns you on."
    $ player.change_lust(char1.sexiness + 2)
    pause 0.4
    char1.talk "Oh yes! You're doing great! Don't stop! Aaaaahhh... Mmm..."
    "It doesn't take her long to move her hand..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") with dissolve:
        zoom 0.667
    pause 0.7
    "... right back between her legs."
    $ char1.change_lust(15)
    char1.talk "Mmmmm... {b}Yes{/b}! {w}OMG!"
    $ player.change_lust(char1.sexiness + 4)
    $ player.add_effect("erection")
    "With her ass rubbing against your dick, it doesn't take long to get you rock hard."
    pause 0.6
    char1.talk "Mmmm... *moans* It feels like you're ready too!"
    pause 0.4
    char1.talk "Let me turn around..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with fade:
        zoom 0.667
    pause 0.7
    "With her hand still inside her pants, you grab her tits again."
    pl "Come a little closer [char1.fname]!"
    pause 0.4
    char1.talk "I'm even getting on my knees for you!"
    pause 0.3
    char1.talk "I want you to stick that hard rod of yours between my tits..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat11.webp") with dissolve:
        zoom 0.7 xpos -50 ypos -5
    pause 0.7
    char1.talk "... abuse and squeeze them any way you want..."
    char1.talk "... while I pleasure myself, rubbing my fingers against my wet pussy!"
    "Wow! her cleavage is deep enough to swallow your whole dick!"
    pause 0.4
    char1.talk "Now fuck my huge tits!"
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat_v1.webm")):
        subpixel True
        zoom 0.7 xpos -50 ypos -5
    pause 4.0
    char1.talk "Mmmm... Yes... Cum for me [char1.playername]! *moans*"
    pause 0.6
    char1.talk "Cover my huge tits in your cum!"
    pause 1.5
    char1.talk "And now tell me how much you love fucking my huge tits!"
    pause 0.4
    pl "Oh my God [char1.fname]! {b}I love fucking your incredible tits!{/b}"
    pause 0.8
    char1.talk "Show me that you mean it!"
    pause 0.4
    char1.talk "Abuse them and fuck them harder! Cover me in your cum! Mmmm... *moans*"
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat_v2.webm")):
        subpixel True
        zoom 0.7 xpos -50 ypos -5
    pause 1.8
    "You ram your dick even faster into her vast cleavage..."
    pause 2.0
    char1.talk "I'm going to make you cum hard!"
    pause 0.5
    pl "Yes! OMG! I'm almost there... *moans*"
    pause 0.5
    char1.talk "Come for me! {w}Cum all over my huge tits!"
    pause 0.5
    char1.talk "Then I'm going to squeeze every last drop from your dick, while I finish myself off! *moans*"
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat_v2.webm")):
        subpixel True
        zoom 0.7 xpos -50 ypos -5
        ease 0.15 zoom 0.7 xpos -46 ypos -3
        ease 0.15 zoom 0.7 xpos -50 ypos -5
        repeat
    pause 2.0
    pl "I'm cummmmminnnnggg!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat12.webp") with fade5:
        zoom 0.75 xpos -100 ypos -50
    pause 0.8
    pl "{b}OMG{/b}! This is incredible!"
    $ player.change_lust(-40)
    $ player.change_endurance(-35)
    char1.talk "Mmmmm... *moans* Ahhh..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat12.webp"):
        subpixel True
        zoom 0.75 xpos -100 ypos -50
        ease 0.2 xpos -98 ypos -45
        ease 0.2 xpos -100 ypos -50
        repeat
    pause 0.8
    char1.talk "Oh Yes! Mmmmmmmm..."
    $ char1.change_lust(-40)
    $ char1.change_endurance(-30)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat12.webp") with dissolve:
        zoom 0.667
    pause 0.5
    char1.talk "Yeah! That was good!"
    pause 0.4
    "Looking at the mess you've made on her tits..."
    char1.talk "Hmmm... I think I need to clean this up."
    "She gets down on her knees and..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat13.webp") with dissolve:
        zoom 0.667
    pause 0.8
    "...starts sucking and licking your cock dry!"
    pause 0.4
    pl "Oh my God [char1.fname]!"
    pause 0.4
    pl "It's so intense..."
    show expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat14.webp") with dissolve:
        zoom 0.667 alpha 0.5
    pause 0.8
    char1.talk "Mmmmmpfff..."
    $ player.change_lust(char1.sexiness + 6)
    pl "Mmmm.... Please stop!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat14.webp") with dissolve:
        zoom 0.667
    pause 0.8
    "Finally after she's licked and sucked every last drop of cum from your dick, she lets go."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat15.webp") with dissolve:
        zoom 0.667
    pause 0.8
    $ char1.add_pl_interaction("titfuck")
    $ char1.add_pl_interaction("blowjob")
    char1.talk "Look, it's all cleaned up now."
    char1.talk "Well, I guess that doesn't hold true for my breasts... *giggles*"
    pause 0.4
    pl "Damn [char1.fname]! This was so intense!"
    char1.talk "I had my fun too."
    char1.talk "I don't know why, but making a guy climax between my tits while I pleasure myself is such a turn on for me!"
    pause 0.4
    pl "Ummm... We can repeat it anytime you want! *chuckling*"
    char1.talk "*giggles* I bet you'd love that..."
    "She takes a handkerchief and tentatively cleans up her tits, before standing up."
    show expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with dissolve:
        subpixel True zoom 0.85 xpos -500
    pause 0.8
    char1.talk "I still need a shower now..."
    pl "I guess you do. *smiling*"
    "You both get dressed..."
    show expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp") with fade:
        zoom 0.667
    pause 0.7
    return _return





label nightbar_hotshots_heat_amy(char1):
    $ l_scene_value = renpy.random.randint(1,2)
    "Completely oblivious of the other girls, [char1.fname] stretches lasciviously..."
    $ l_breast_size_text = char1.get_breast_size_text()
    "...showcasing her [l_breast_size_text]!"
    char1.talk "Mmmm... I feel incredibly hot! *moans*"
    pause 0.3
    char1.talk "Do you like what you see [char1.playername]?"
    pause 0.4
    pl "*gulp* Yes!"
    "You let your eyes slide over her incredible body,\nstarting with her legs and abs..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -850 ypos -720
    pause 2.5
    "Wow! She's incredible!"
    $ player.change_lust(char1.sexiness)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 1.0 xpos -850 ypos -720
        linear 5.0 zoom 1.0 xpos -850 ypos -150
    pause 5.5
    "As your eyes reach her face, you lean back a little."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 1.0 xpos -850 ypos -150
        ease 1.0 zoom 0.8 xpos -500 ypos -50
    pause 1.5

    if l_scene_value == 1:
        $ char1.add_scene_seen("Hotshots_heat1")
        char1.talk "Do you want me to come closer?"
        pl "Oh yes!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
            zoom 0.5
        pause 0.8
        char1.talk "I want you to squeeze and caress my big tits and nipples!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve10:
            zoom 1.0 xpos -850 ypos 0
        pause 1.2
        char1.talk "Can you do that for me?"
        "You look down at her huge melons..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp"):
            zoom 1.0 xpos -850 ypos 0
            linear 1.2 zoom 1.0 xpos -850 ypos -600
        pause 1.7
        "... and only manage a nod!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve10:
            zoom 0.8 xpos -550 ypos 0
        pause 1.2
        char1.talk "Is that a yes?"
        pause 0.4
        pl "Ummm... Yes! I'm sure I can manage... *smirks*"
        char1.talk "Mmmmm... Gooood! I really need it!"
        "She turns around and leans back against you..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1a.webp") with fade:
            zoom 0.5
        pause 1.0
        "...rubbing her firm ass on your dick, while you squeeze her massive tits!"
        char1.talk "Mmmm... Yes! Squeeze them really hard!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1a.webp"):
            zoom 0.5
            subpixel True
            ease 1.4 zoom 0.9 xpos -750 ypos -70
        pause 2.0
        $ char1.change_lust(10)
        pl "I don't want to hurt you."
        pause 0.3
        char1.talk "Don't worry, you won't!"
        "Still oblivious about all the other girls watching the both of you, she whispers into your ear..."
        pause 0.3
        char1.talk "Did you know that my nipples are so sensitive, I can orgasm just from playing with them..."
        pl "Ummm... No, no I didn't!"
        $ player.change_lust(char1.sexiness)
        char1.talk "Mmmm... Play with them and caress them until you make me cum! *moans*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1b.webp") with dissolve:
            zoom 0.9 xpos -750 ypos -70
        pause 0.8
        pl "Emmm... Like this?"
        pause 0.3
        char1.talk "Hmmm... Yes! You're doing great! *moans*"
        $ char1.change_lust(20)
        char1.talk "Don't stop!"
        $ player.change_lust(char1.sexiness + 5)
        char1.talk "And now squeeze them real hard again!"
        "You comply and take both of her enormous juggs in your hands..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1a.webp") with dissolve:
            zoom 0.9 xpos -750 ypos -70
        pause 0.8
        char1.talk "Aaaa... Mmmm... Yes!"
        $ char1.change_lust(10)
        char1.talk "Now caress my nipples until I cum! You can even pinch and pull them!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1b.webp") with dissolve:
            zoom 0.9 xpos -750 ypos -70
        pause 0.8
        char1.talk "Mmmm... *moans*"
        pause 0.8
        char1.talk "Yes, I'm almost there now..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1b.webp"):
            zoom 0.9 xpos -750 ypos -70
            ease 1.5 zoom 0.6 xpos -200 ypos -50
        pause 1.8
        $ player.change_lust(char1.sexiness)
        $ player.add_effect("erection")
        "Right at that moment, she rubs her ass against your erect dick!"
        char1.talk "Ohhh... Wow! Don't stop OMG! *moans*"
        pause 0.4
        char1.talk "Yes! Oh Yes!"
        show expression im.Alpha("scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat1b_cum.webp", 0.8) with dissolve:
            zoom 0.6 xpos -200 ypos -50
        pause 1.0
        $ char1.change_lust(-50)
        $ char1.change_endurance(-30)
        char1.talk "Oh wow! Just what I needed!"
        char1.talk "You were great [char1.playername]. Thank you!"
        "She really orgasmed from your nipple play..."
        "...probably your hard dick pressed against her ass helped too!"
        t_crowd_of_girls "*cheers from the girls* {b}[char1.fname], [char1.fname], [char1.fname]{/b}!"
        t_crowd_of_girls "{b}[player.fname], [player.fname], [player.fname]{/b}! *more cheers from the girls*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_max_undress].webp") with fade:
            zoom 0.667
        pause 1.0
        char1.talk "Wow! I really need to catch my breath for a moment... *giggles*"
        scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
            zoom 0.5
        pause 0.5
        yumiko.talk "Now that was an incredible ending for our HotShots game!"
        pl "Ummm... Yeah... *lamely*"
        "Still hard, you can't completely agree..."
        yumiko.talk "I suggest you both get dressed now. *smirks*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
            zoom 0.667
        pause 0.8
        char1.talk "I feel much better, no longer so hot!"
        pause 0.3
        pl "Ummm... You're welcome..."
        char1.talk "Not that I'm not always super hot... *winks*"
        pl "Yeah, definitely!"
    elif l_scene_value == 2:
        $ char1.add_scene_seen("Hotshots_heat2")
        char1.talk "Would you like to kiss me [char1.playername]?"
        pause 0.3
        pl "I'd love to!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
            zoom 0.5
        pause 0.8
        char1.talk "Tell me how much you want my wet tongue inside you mouth!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve10:
            zoom 1.0 xpos -850 ypos -600
        pause 1.2
        "Staring at her huge tits, it takes you a moment to register that [char1.fname] is talking to you."
        pause 0.3
        pl "Ummm... What?"
        char1.talk "Are we a little distracted by some hot girl's naked tits? *giggles*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve10:
            zoom 0.8 xpos -550 ypos 0
        pl "Sorry, I guess I was. *sheepishly*"
        pl "What is it you asked?"
        char1.talk "Never mind, let me show you!"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat2a.webp") with fade:
            zoom 0.5
        pause 0.8
        "She wraps her right leg around you and brings her mouth close to yours."
        char1.talk "Do you like how my breasts are squished against your chest? *whispers*"
        pause 0.4
        pl "Oh yes!"
        char1.talk "When you were focused on my chest, I asked how much you want my wet tongue inside your mouth. *purrs*"
        char1.talk "I'm so hot and horny... *whispers*"
        $ player.change_lust(char1.sexiness + 4)
        "Without waiting for an answer..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat2b.webp") with fade:
            zoom 0.5
        pause 0.8
        char1.talk "Mmmm... *slurp* *kissing sounds*"
        $ char1.change_lust(10)
        pl "Mmmmm... *moans*"
        $ player.change_lust(char1.sexiness + 6)
        char1.talk "I can feel that you like it too. *moans*"
        char1.talk "Or is that a gun in your pants? *whispering*"
        pl "Too bad we're not alone right now! *whispering*"
        pause 0.4
        char1.talk "I don't really care... *moans*"
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat2c.webp") with dissolve:
            zoom 0.5
        pause 1.0
        "Wrapping her other leg around you and rubbing her crotch against your dick..."
        pl "Mmmmm... Wow!"
        $ player.change_lust(char1.sexiness + 8)
        $ player.add_effect("erection")
        char1.talk "*slurp* *kissing sounds*"
        char1.talk "I bet I can make you cum just by kissing and rubbing my body against you!"
        pause 0.3
        pl "I won't bet against you! *chuckles*"
        pause 1.0
        char1.talk "Mmmmm.... Aaaa... *more kissing sounds*"
        pause 0.4
        t_crowd_of_girls "{b}Make him cum{/b}! {w}{b}Make him cum{/b}! *cheers from the other girls*"
        yumiko.talk "Oh wow! I think it's time for you two to get a room!"
        "You were so engrossed in the kiss and embrace, that you had forgotten about the other girls..."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat2a.webp") with fade:
            zoom 0.5
        pl "Ummm... What?"
        t_crowd_of_girls "{b}Make him cum{/b}! {w}{b}Make him cum{/b}! *more cheers from the other girls*"
        "Somehow the girls' shouts kind of killed the mood."
        char1.talk "I think we better stop."
        pause 0.4
        pl "It was incredible, but I agree."
        char1.talk "I was starting to get really horny!"
        char1.talk "But somehow that just killed the mood."
        "[char1.fname] climbs down from your lap and walks back to her stool."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_max_undress].webp") with fade:
            zoom 0.667
        pause 0.8
        char1.talk "I guess we should put some clothes back on... *smiles*"
        pl "Yes, probably a good idea."
        t_crowd_of_girls "{b}Boohhh{/b}! {b}Boohh{/b}! That's not the spirit!"
        scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
            zoom 0.5
        pause 0.5
        yumiko.talk "Hey girls! Give them some space!"
        yumiko.talk "I think that was a hot ending to our game none the less."
        scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
            zoom 0.667
        pause 0.7
        yumiko.talk "And since both players are dressed now, enjoy your evening everyone!"
    return _return





label nightbar_hotshots_heat_brenda(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Mmmm... It's really hot in here, don't you think [char1.playername]?"
    "She walks towards you, showcasing her [l_breast_size_text]."
    pause 0.3
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Before I came to the island I was the star with my [l_breast_size_text] anywhere I went..."
    pause 0.4
    pl "Ummm... I'm quite sure of that [char1.fname]!"
    $ player.change_lust(char1.sexiness)
    pl "They're really nice!"
    pause 0.4
    char1.talk "Ha ha! Yeah nice... *a little sad*"
    char1.talk "From your reaction, I guess it's a good thing that I have an amazing butt, even by island standards!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "I really liked the way you were staring at it when I walked in..."
    pause 0.4
    pl "Ummm... I didn't..."
    char1.talk "Yes you did! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "It looks a lot better without the skirt hiding my perfectly round cheeks!"
    pause 0.4
    pl "Wow [char1.fname]! It's perfect!"
    "And the panties she's wearing are even better than you had imagined."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -900 ypos -650
    pause 2.7
    char1.talk "I'm still so hot!"
    char1.talk "I really need to get rid of the skirt!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve10:
        zoom 0.5
    pause 1.3
    char1.talk "Isn't it an amazing sight?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -700 ypos -600
    pause 2.7
    pl "Yes! Definitely!"
    $ player.change_lust(char1.sexiness+3)
    char1.talk "Mmmmm... I want you to touch me! *moans"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with fade:
        zoom 0.667
    pause 0.8
    char1.talk "Squeeze my breasts [char1.playername]!"
    "She walks towards you, turns around and leans back against you..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1.webp") with fade:
        zoom 0.667
    pause 0.8
    "Holding her tits in your hands, they're more than a handful!"
    pl "Your breasts are really soft [char1.fname]."
    pause 0.3
    char1.talk "Yes I know. *whispering*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1.webp"):
        zoom 0.667
        ease 0.8 zoom 0.75 xpos -100 ypos -50
    pause 1.2
    char1.talk "But my ass is a lot less soft... *moans*"
    pause 0.4
    "She starts grinding her ass against your crotch!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat1.webp"):
        subpixel True
        zoom 0.75 xpos -100 ypos -50
        ease 0.35 xpos -106 ypos -50
        ease 0.2 xpos -106 ypos -52
        ease 0.35 xpos -100 ypos -52
        ease 0.2 xpos -100 ypos -50
        repeat
    pause 3.5
    char1.talk "Mmmm... Cum for me [char1.playername]... *whispers into your ear*"
    $ player.change_lust(char1.sexiness + 8)
    pl "Ohh... Mmmm... Wow!"
    pause 0.3
    "She doesn't stop rubbing her ass against your dick!"
    $ player.add_effect("erection")
    char1.talk "Mmmmmm... Yes! That's what I was waiting for... *moans*"
    "With her perfect round ass rubbing against your dick, it was only a question of time until you got hard!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat2.webp") with fade:
        zoom 0.75 xpos -150 ypos -90
    pause 0.8
    "Looking down, you can see your dick sitting comfortably between her incredible butt cheeks..."
    $ player.change_lust(char1.sexiness + 6)
    yumiko.talk "{b}Hey you two{/b}!"
    pause 0.4
    char1.talk "Ummm... What is it? *moans*"
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 0.5
    pl "Yeah?"
    t_crowd_of_girls "Make him {b}cum{/b}! {w}Make him {b}cum{/b}!"
    pause 0.4
    yumiko.talk "As much as it was really exhilarating to watch..."
    yumiko.talk "I won't have more cum sprayed around my bar!"
    pause 0.4
    t_crowd_of_girls "{b}Boooohhh...{/b} {w}{b}Boooohhh...{/b}"
    pause 0.3
    yumiko.talk "Come on girls, we all had our fun!"
    yumiko.talk "And now let them get dressed."
    pause 0.4
    char1.talk "Yes, okay... *quietly*"
    "[char1.fname] extracts herself from your embrace and dresses."
    pause 0.6
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
        zoom 0.667
    pause 0.7
    "You also grab your pants and shirt and put them back on."
    pause 0.6
    yumiko.talk "Thank you for playing [char1.fname] and [player.fname]."
    yumiko.talk "Don't be angry I stopped you!"
    pause 0.3
    yumiko.talk "You can always continue in one of your rooms... *smiles*"
    pause 0.5
    yumiko.talk "Since our two players are dressed now, enjoy your evening everyone!"
    t_crowd_of_girls "You too Yumiko! *chorus from the girls*"
    return _return





label nightbar_hotshots_heat_eva(char1):
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Yes, it's definitely far too hot in here!"
    "She smiles at you, parading her [l_breast_size_text]."
    pl "Ummm... Yeah..."
    char1.talk "I don't know why I'm so horny all of a sudden! *moans*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        zoom 0.334
    pause 0.8
    $ char1.change_lust(15)
    char1.talk "I could really use some help, [char1.playername]!"
    char1.talk "Mmmm.... *moans*"
    pause 0.5
    pl "{b}Holy shit{/b}!"
    $ player.change_lust(char1.sexiness+2)
    $ char1.add_pl_interaction("tease_boobs")
    $ char1.add_pl_interaction("tease_pussy")
    $ char1.add_pl_interaction("tease_masturbate")
    char1.talk "Pull out your dick, [char1.playername]!"
    char1.talk "I want to see how hard you are for me!"
    yumiko.talk "Oh... {w}{b}Girls! We better let them have some private time...{/b}"
    t_crowd_of_girls "Ummm... No! {w}We want to see his dick too! *giggles*"
    yumiko.talk "Out with you! Let's go!"
    pause 0.5
    t_crowd_of_girls "*murmurs* Do we really have to?"
    yumiko.talk "Yes!"
    "Yumiko shoves the other girls out of the bar..."
    pause 0.5
    char1.talk "I'm so wet! *moans*"
    $ char1.change_lust(10)
    "[char1.fname] removes her pants and takes a step towards you..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.334
    pause 0.8
    char1.talk "You're still wearing your pants!"
    char1.talk "Mmmm... Ahhh... *moans*"
    char1.talk "If I don't get your dick immediately, I'm going to have to help myself... Mmmm.... *moans*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.334
        ease 2.2 zoom 0.75 xpos -1200 ypos -300
    $ renpy.pause(2.8,hard=True)
    "Just look at her mountainous knockers."
    "The way they're proudly standing out on her small frame."
    $ player.change_lust(char1.sexiness+2)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.75 xpos -1200 ypos -300
        ease 2.1 zoom 0.75 xpos -1100 ypos -900
    $ renpy.pause(2.5,hard=True)
    "And how she's fingering her pussy..."
    "That's so fucking hot!"
    $ player.change_lust(char1.sexiness+2)
    char1.talk "Stop staring at me and get your dick out, or I'll cum without you!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve10:
        zoom 0.6 xpos -800 ypos -30
    pause 0.6
    pl "{b}Wait{/b}! I'll be quick!"
    char1.talk "You better be! Mmmm... *moans*"
    $ char1.change_lust(15)
    "You undress as quickly as possible, not taking your eyes off her."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.6 xpos -800 ypos -30
        ease 4.0 zoom 0.334 xpos 0 ypos 0
    $ renpy.pause(4.4,hard=True)
    pl "I'm done!"
    char1.talk "It was about time!"
    pause 0.4
    "She walks towards you, turns around and rubs her ass against your dick..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Do you think I'm hot, [char1.playername]? *whispering in your ear*"
    pause 0.4
    pl "Oh yes, you're super hot, [char1.fname]."
    pause 0.5
    char1.talk "Now be a good boy and squeeze my tits."
    char1.talk "I know you want to! *smirks*"
    pause 0.4
    "While you grab her huge knockers, she takes your dick and squeezes it between her legs..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5a.webp") with dissolve:
        zoom 0.3334
    pause 0.8
    "...rubbing it against her wet pussy."
    char1.talk "Mmmm... Yes! That's much better! *moans*"
    scene eva_rubbing_animate:
        zoom 0.3334
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5a.webp"
        pause 0.3
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5b.webp"
        pause 0.15
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5c.webp"
        pause 0.15
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5d.webp"
        pause 0.3
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5c.webp"
        pause 0.15
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat5b.webp"
        pause 0.15
        repeat
    $ renpy.pause(2.5,hard=True)
    call actions_used (1) from _call_actions_used_306
    char1.talk "Does this turn you on, [char1.playername]?"
    pl "Oh Yes... *moans*"
    $ player.change_lust(char1.sexiness)
    pause 0.5
    char1.talk "Don't you dare cum already!"
    pause 0.6
    char1.talk "I need you inside me!"
    pause 0.4
    pl "Aahhh.. Mmmm... I can't wait."
    "She moves away from you and leans against the counter, pushing out her ass!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Fuck me, [char1.playername]!"
    char1.talk "I want your huge dick inside my tight pussy!"
    "You ram your hard-on into her wet and really tight pussy!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with fade:
        zoom 0.5
    pause 0.8
    pl "Is it big enough for you? *smirks*"
    char1.talk "{b}Yes! OMG!{/b}"
    char1.talk "Punish me with your huge dick!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp") with fade:
        zoom 0.3333334
    pause 0.8
    $ renpy.start_predict("*Eva_nightbar_hs_fuck_cam1*")
    char1.talk "Make me cum really hard! *moans*"
    $ char1.add_pl_interaction("sex")
    $ lo_cam0 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_hs_fuck_cam1_", {"face_x":1150, "face_y":760, "breasts_x":1630, "breasts_y":1260, "pussy_x":2740, "pussy_y":1280})
    $ ll_cameras = []
    $ ll_cameras.append(lo_cam0)
    $ ll_sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,1]
    $ l_cum_control = {"cum_x":1900, "cum_y":1270, "cum_fps":50, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":char1.talk, "what":"Yes! I'm almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"Just a little longer...", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"You're so huge and hard!", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Oh my God! I'm cummmminnnggg!", "pause":1.2})
    $ ll_cum_talk.append({"who":pl, "what":"Cummmiinnnggg too!", "pause":1.0})
    $ ll_speed_talk = [{"fast":"Give me that dick!", "faster":"*moans* Make me cum! You're so good!", "slow":"*moans* Oh Yes! *moans", "slower":"Please don't slow down!"}]
    call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 1.0) from _call_interactive_sex_28
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with dissolve:
        zoom 0.46666666 xpos -247 ypos -233
    pause 0.8
    "You spray your load into her eagerly waiting pussy!"
    $ renpy.stop_predict("*Eva_nightbar_hs_fuck_cam1*")
    $ player.change_lust(-60)
    $ player.change_endurance(-60)
    char1.talk "Wow! That was the best sex I've had in a long time!"
    $ char1.change_lust(-60)
    $ char1.change_endurance(-40)
    pl "You're so tight [char1.fname]."
    char1.talk "Maybe it's because you're so big, [char1.playername]. *smirks*"
    call change_char_max_love (char1, 5) from _call_change_char_max_love_31
    $ char1.change_love(10)
    call actions_used (1) from _call_actions_used_307
    "You pull your dick out while [char1.fname] stands up."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "That was awesome! *smiles"
    pl "Yes it was. *grinning*"
    pause 0.5
    char1.talk "You're a sex machine. *winks*"
    char1.talk "That's one of the drawbacks when you look like I do. Most guys are so excited they cum far too soon for me to have fun."
    pause 0.3
    pl "I wonder why that is... *smirks*"
    char1.talk "With you it was just {b}wow{/b}!"
    pl "Thanks."
    pause 0.5
    char1.talk "I really like playing games with you. *smirks*"
    pl "Likewise. *grinning*"
    char1.talk "I'm going to sleep like a baby tonight. *smiles*"
    pl "Me too."
    "She collects her clothes and gets dressed."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with fade:
        zoom 0.5
    pause 0.8
    "You follow her example and pick up your clothes as well."
    pause 0.6
    char1.talk "I'll tell the girls we're done."
    pause 0.5
    pl "Okay. *grinning*"
    $ char1.add_scene_seen("Hotshots_heat1")
    return _return





label nightbar_hotshots_heat_desire(char1):
    $ char1.add_pl_interaction("tease_talk")
    $ char1.add_pl_interaction("tease_body")
    $ char1.add_pl_interaction("tease_boobs")
    $ char1.add_pl_interaction("tease_ass")
    $ char1.add_pl_interaction("tease_pussy")
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Holy Shit! It must have been the drinks..."
    $ char1.change_lust(10)
    char1.talk "My nipples feel like they're on fire!"
    pause 0.5
    char1.talk "Do you like my [l_breast_size_text]? *moans*"
    pause 0.3
    pl "Oh Wow! I mean Yes!"
    $ l_breast_size_text = char1.get_breast_size_text()
    "You stare in awe at her [l_breast_size_text]..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True zoom 0.5
        ease 2.0 zoom 1.2 xpos -1000 ypos -550
    $ renpy.pause(2.5,hard=True)
    "Oh my God! What a pair of breasts! And her erect nipples are so hot!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True zoom 1.2 xpos -1000 ypos -550
        ease 1.9 zoom 1.2 xpos -1100 ypos -70
    $ renpy.pause(2.4,hard=True)
    "Looking into her beautiful face, her seductive smile is driving you wild!"
    $ player.change_lust(char1.sexiness+4)
    char1.talk "I want to do some pole dancing... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Come on, let's head over to the pole."
    pl "Okay. *grinning*"
    "Not hesitating even for a moment, you take her hand..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "...still staring at her well-rounded knockers."
    char1.talk "[jobs.bartender.fname], could you please switch the pole dance lights to red?"
    pause 0.4
    t_crowd_of_girls "{b}Yeah!{/b} {b}{w}Yeah!{/b} {b}{w}Red is nice!{/b}"
    jobs.bartender.talk "Okay, I'm on it."
    pause 0.4
    "You have barely reached the pole dance area, when [char1.fname] let's go of your hand and turns around..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with fade:
        zoom 0.5
    pause 0.7
    char1.talk "The thong would only be in the way..."
    char1.talk "Oh...\n{w}You don't mind if I pull it down? Do you, [char1.playername]?"
    pause 0.4
    pl "Ummm... N.. No, not at all."
    "You get a perfect view on her shapely butt and huge round side boobs!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp"):
        zoom 0.5
        ease 1.6 zoom 0.8 xpos -450 ypos -240
    $ renpy.pause(2.1,hard=True)
    "{b}Oh dear God{/b}! Her tits look fabulous from behind!"
    $ player.change_lust(char1.sexiness+2)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with dissolve:
        zoom 0.8 xpos -450 ypos -280
    pause 0.7
    char1.talk "Okay, that was the thong!"
    char1.talk "And now the stockings..."
    pause 0.5
    char1.talk "I think we won't need them either."
    pause 0.4
    "[char1.fname] slowly leans forward to peel off her stockings..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with dissolve:
        zoom 0.5334 xpos -450 ypos -330
    pause 0.7
    "...giving you a perfect view of her exposed, juicy pussy."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp"):
        zoom 0.5334 xpos -450 ypos -330
        ease 1.8 zoom 1.0 xpos -1400 ypos -1100
    $ renpy.pause(2.2,hard=True)
    $ player.change_lust(char1.sexiness+4)
    $ player.add_effect("erection")
    pl "{b}Wow{/b}! *gulp*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with dissolve:
        zoom 1.0 xpos -1400 ypos -1100
    pause 0.7
    char1.talk "Did you say something? *smirks*"
    pause 0.4
    pl "Ummm..."
    pause 0.4
    char1.talk "Mmmm... I'm so horny! *moans*"
    "She grabs the pole, before sliding down onto her knees..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp") at zoom_c(i_zoom=0.3334) with fade
    pause 0.7
    char1.talk "I'm so ready for that pole dance. *smirks*"
    pause 0.4
    char1.talk "Why aren't you naked yet?"
    "Did she just ask you to strip?"
    pl "Er... What?"
    char1.talk "What kind of pole dance do you think I have in mind?"
    char1.talk "I want {b}your{/b} hard pole right between my legs! *moans*"
    pl "Oh..."
    "It seems that it's your lucky night."
    pause 0.4
    char1.talk "What are you waiting for?"
    "As you begin to undress..."
    jobs.bartender.talk "Oh oh... {w}Girls, we better give them some space..."
    t_crowd_of_girls "{b}No! It's just getting interesting!{/b}"
    jobs.bartender.talk "Let's go! Out with you, girls!"
    pause 0.5
    t_crowd_of_girls "Mhhh... Okay..."
    "Just when [jobs.bartender.fname] has shoved the last girl out of the bar, you're done undressing."
    pause 0.4
    char1.talk "I want you to get on your back. I really want to ride that pole!"
    "This is probably not a good time to argue, so you do as you're told."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp"):
        zoom 0.3334
        ease 2.7 zoom 0.8 xpos -1000 ypos -100
        pause 0.6
        ease 2.7 zoom 0.8 xpos -1000 ypos -700
    $ renpy.pause(6.3,hard=True)
    char1.talk "Now that's what I call a hard pole!"
    $ char1.add_phone_background("Desire3")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") at zoom_c(i_zoom=0.5) with fade
    pause 0.7
    $ renpy.start_predict("*Desire_hotshots_sex_cam*")
    char1.talk "I'm going to make you cum hard! *moans*"
    $ char1.add_pl_interaction("sex")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") at zoom_c(i_zoom=0.5) with dissolve
    pause 0.7
    char1.talk "Mmmm... Ahh... You're so huge! *moans*"
    $ ll_cameras = []
    $ ll_cameras.append(cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_hotshots_sex_cam1_", {"face_x":1905, "face_y":538, "breasts_x":1906, "breasts_y":1254, "pussy_x":1910, "pussy_y":2055}))
    $ ll_cameras.append(cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_hotshots_sex_cam2_", {"face_x":1850, "face_y":475, "breasts_x":1900, "breasts_y":950, "pussy_x":1970, "pussy_y":1380}))
    $ ll_sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,18,18,1]
    $ ll_cum_sequence = [1,2,3,4,5,6,7,7,8,8,12,12,13,14,15,16,17,17,18,18,1]
    $ l_cum_control = {"cum_x":1900, "cum_y":1800, "cum_fps":40, "cum_zoom":0.5, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":pl, "what":"{b}OMG{/b}! I'm almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Mmmm... I'm close too... *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Can you hold it just a little longer? *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":pl, "what":"Yes, I'm trying! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"I really can't hold it back any longer! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"It's okay, I'm cumming too! *moans", "pause":1.2})
    $ ll_speed_talk = [{"fast":"Fuck! This is so good!", "faster":"*moans* Yes, OMG! You're incredible!", "slow":"Your bouncing tits are driving me crazy!", "slower":"Please don't slow down!"}]
    play sound2 "sounds/female_sex1.mp3" fadein 0.5
    call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_cum_sequence, ll_cum_talk, ll_speed_talk, 0.8, i_char=player) from _call_interactive_sex_29
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") with dissolve:
        zoom 0.5
    pause 0.7
    $ renpy.stop_predict("*Desire_hotshots_sex_cam*")
    call actions_used (1) from _call_actions_used_308
    stop sound2 fadeout 0.5
    pl "{b}OMG Yes!{/b}"
    char1.talk "I'm cumming!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat11.webp") with dissolve:
        zoom 0.5
    pause 0.7
    $ char1.change_lust(-50)
    $ char1.change_endurance(-40)
    $ player.change_lust(-50)
    $ player.change_endurance(-30)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat12.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Holy shit! That was incredible!"
    pl "Yes it was. *grinning*"
    pl "You're so hot, [char1.fname]!"
    pause 0.4
    pl "The way your big breasts were bouncing up and down..."
    char1.talk "You mean those fucking huge knockers? *smiles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat13.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Yes. Okay... *grinning* They're fucking huge, not just big. *chuckles*"
    char1.talk "Would you like to see them bounce some more? *smirks*"
    pause 0.4
    pl "Ohh... I'm completely spent, I don't think I'm up for another round."
    pause 0.4
    char1.talk "Me too. I'm just teasing you. *smiles*"
    char1.talk "We better let the others know that we're done. I'm, sure they want to use the bar too."
    pause 0.4
    pl "You're right."
    "You both dress and walk back to the bar."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_2.webp") with fade:
        zoom 0.334
    char1.talk "I'm going to sleep really great tonight! *smiles*"
    pl "Me too. *grinning*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "I'll let the girls know we're done."
    pause 0.5
    pl "Okay. *smiles*"
    $ char1.add_scene_seen("Hotshots_heat1")
    return _return





label nightbar_hotshots_heat_faye(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Mmmm... OMG! {w}I feel so horny!"
    "Pushing out her [l_breast_size_text], she looks at you like she wants to devour you..."
    pause 0.3
    char1.talk "Can you do something about it [char1.playername]?"
    char1.talk "...or do I have to pleasure myself."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Don't you want to touch my huge knockers, caress my nipples?"
    char1.talk "They're so sensitive right now..."
    pl "Wow!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Or maybe you want to feel the wetness between my thighs..."
    pause 0.5
    char1.talk "Why do you still have your pants on [char1.playername]?"
    pl "Ummm...."
    pause 0.5
    yumiko.talk "Girls! I think it's best we give them some space... *chuckles*"
    t_crowd_of_girls "Noooo... {w}It's just getting interesting..."
    yumiko.talk "Clear the bar, out with all of you!"
    yumiko.talk "I'm not talking about you [char1.fname], but you probably weren't listening anyway."
    "Yumiko and the other girls leave the bar."
    pause 0.5
    "You start to undress..."
    char1.talk "Mmmm... Ahhh... *moans*"
    $ player.change_lust(char1.sexiness + 2)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 0.5
    pause 0.8
    $ char1.change_lust(10)
    char1.talk "Hurry up [char1.playername], or I'm cumming without you."
    char1.talk "I can't hold myself back much longer... *moans some more*"
    pl "I'm done!"
    char1.talk "I can see that. *smirks*"
    "She turns around right in front of your bar stool..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with fade:
        zoom 0.5
    pause 0.8
    "You can't wait to get your hands on her incredible knockers."
    $ player.change_lust(char1.sexiness + 4)
    $ player.add_effect("erection")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -800
    $ renpy.pause(2.3,hard=True)
    char1.talk "I hope you're rock hard by now!"
    char1.talk "Do you have enough space for me on your bar stool?"
    char1.talk "I'd like to squeeze in between your legs."
    pause 0.3
    pl "For you, I can make space..."
    "You spread your legs apart to make more space for her incredible ass."
    char1.talk "I want you to put your hand inside my panties and work on my wet pussy..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Yes! OMG! {w}That feels so good!"
    "Looking over her shoulder, you take in the view of her fantastic tits, while caressing her nipple..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with fade:
        zoom 0.5
    pause 0.8
    $ player.change_lust(char1.sexiness + 4)
    pl "I love your huge tits [char1.fname]! They're incredible."
    char1.talk "Thank you!"
    char1.talk "As long as you keep one hand inside my panties, you can do whatever you want with your other hand."
    "By now, you're really horny yourself."
    "You rub your hard cock against her firm ass..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "*moans* Your dick feels really good rubbing against my butt..."
    char1.talk "Mmmm... Don't forget my pussy... {w}Can you put another finger..."
    "You put three fingers inside her wet cunt."
    char1.talk "Ahhh... OMG, yes!"
    "She starts grinding her butt rhythmically against your hard dick..."
    $ char1.add_pl_interaction("sex")
    $ ll_cameras = []
    $ ll_cameras.append(cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_hs_cam1_", {"face_x":0, "face_y":0, "breasts_x":600, "breasts_y":600, "pussy_x":1470, "pussy_y":920}))
    $ ll_cameras.append(cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_hs_cam2_", {"face_x":0, "face_y":0, "breasts_x":1370, "breasts_y":640, "pussy_x":0, "pussy_y":0}))
    $ ll_sequence = [1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1]
    $ l_cum_control = {"cum_x":1000, "cum_y":750, "cum_fps":50, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":char1.talk, "what":"{b}Yes!{/b} Insert another finger! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Mmmm... I'm really close now... *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":pl, "what":"Just a little longer...", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Look at my fucking huge tits!", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"And now cum for me!", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"I'm ready to blow...", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Yes! I'm cummmminnnggg!", "pause":1.2})
    $ ll_cum_talk.append({"who":pl, "what":"Cummmiinnnggg too!", "pause":1.0})
    $ ll_speed_talk = [{"fast":"Oh my God! Yes! I'm so horny!", "faster":"*moans* Yes! Finger me!", "slow":"You're so hard! *moans*", "slower":"Please don't slow down!"}]
    call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 1.5) from _call_interactive_sex_17
    $ char1.change_lust(-40)
    $ char1.change_endurance(-40)
    call actions_used (1) from _call_actions_used_250
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with dissolve:
        zoom 0.5
    pause 0.8
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") with dissolve:
        zoom 0.5
    pause 0.8
    $ player.change_lust(-40)
    $ player.change_endurance(-40)
    char1.talk "That was great!"
    pause 0.6
    pl "Yes, absolutely!"
    pause 0.5
    char1.talk "Let me clean your dick up for you!"
    "She turns around and gets on her knees..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat11.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Mmmmpfff... *slurp* *slurp*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat12.webp") with dissolve:
        zoom 0.5
    pause 0.8
    pl "Mmmm... OMG!"
    $ player.change_lust(10)
    "The way she's sucking on your dick already makes you a little hard again."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat13.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "All cleaned up now. *smirks*"
    char1.talk "And it seems our friend can't get enough of me... *winks*"
    "You can't resist looking from her face to her huge mounds..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat14.webp") with dissolve:
        zoom 0.5
    pause 0.8
    pl "Oh my God [char1.fname], they're huge!"
    pause 0.4
    char1.talk "You have no idea [char1.playername]..."
    char1.talk "Your dick is about 8 inches?"
    pl "Yeah, about that I guess."
    char1.talk "Do you want to see me make it vanish inside my 12 inch cleavage?"
    char1.talk "That's about how deep it is when I squeeze my mounds just a little..."
    pl "*gulp* Okay."
    char1.talk "Let me show you!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat15.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "You feel a slight pressure all around your hardening dick."
    char1.talk "Can we continue at GREEN ROOM?"
    menu:
        "Yes, I wouldn't mind " if True:
            jump nightbar_blue_room_faye2
        "No, sorry but I have to go" if True:
           char1.talk "it's a pity"
    $ player.change_lust(char1.sexiness * 2)
    pl "Wow!"
    char1.talk "I guess you could say that. *smirks*"
    char1.talk "And now before I need to clean up my tits as well, let me give you some room *giggles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with fade:
        zoom 0.8 xpos -600
    pause 0.8
    char1.talk "I really enjoyed the game."
    char1.talk "Especially the ending. *smiles*"
    pl "Trust me, I enjoyed it more. *smiling back*"
    pause 0.6
    char1.talk "Maybe..."
    "[char1.fname] picks up her clothes and gets dressed."
    "You follow her example and dress too."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_1.webp") with fade:
        zoom 1.25 xpos -1000
    pause 0.8
    char1.talk "I'll let the girls know we're done."
    pause 0.5
    pl "Sure, thanks."
    return _return

label nightbar_blue_room_faye2:
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom1.webp") with fade:
        zoom 0.3334
    pause 1.0
    char1.talk "What are you waiting for?"
    char1.talk "Come on!"
    "You practically jump out of your chair to follow her."
    pause 0.3
    pl "Coming!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom1.webp"):
        subpixel True zoom 0.3334 align (0.5,0.95)
        ease 2.3 zoom 0.6
    $ renpy.pause(2.6,hard=True)
    char1.talk "Hey [char1.playername]! Stop staring at my legs and ass! *giggles*"
    pl "As the lady commands. *grinning*"
    "You let you eyes slide up..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom1.webp"):
        subpixel True zoom 0.6 align (0.5,0.95)
        ease 2.3 zoom 0.7 align (0.5,0.0)
    $ renpy.pause(2.6,hard=True)
    "Until they rest on her beautiful face and magnificent tits."
    pause 0.4
    char1.talk "It's the first room to the left at the top of the stairs..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom2.webp") with fade:
        zoom 0.5
    pause 1.0
    char1.talk "Here we are!"
    pause 0.3
    "You look around the room for a moment."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom3.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Do you like it here?"
    pause 0.3
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom2.webp") with dissolve:
        zoom 0.7 align (0.7,0.1)
    pause 0.7
    pl "You're here, so yes, I love it."
    char1.talk "Thanks, but I meant the room..."
    char1.talk "Do you like the room?"
    pause 0.3
    pl "Yes. It looks cozy and kind of sexy too. *smiling*"
    pause 0.3
    char1.talk "Have a seat on the round sofa and I'll start working on that pole... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom3.webp") with dissolve:
        zoom 0.5
    "Turning towards the sofa, you already imagine how [char1.fname]'s gonna look pole dancing and stripping..."
    $ player.change_lust(char1.sexiness)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom3.webp"):
        subpixel True zoom 0.5 align (0.8,0.7)
        ease 2.0 zoom 1.0
    $ renpy.pause(2.4,hard=True)
    "...before you sit down."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom4.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I promise you won't forget this night! *smiles*"
    pause 0.3
    char1.talk "For what I've in mind, I won't be needing the skirt..."
    char1.talk "Everyone is always looking at my huge chest, but I'm really proud of my butt, too!"
    pause 0.3
    char1.talk "I really like how it looks in a small thong."
    "She's right! It's definitely a nice ass!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom4.webp"):
        subpixel True zoom 0.5 align (0.6,0.7)
        ease 1.5 zoom 1.0
    $ renpy.pause(1.8,hard=True)
    pl "Your butt is incredible, [char1.fname]!"
    char1.talk "Thank you. *smiles*"
    #call change_char_max_affection (char1, 4) from _call_change_char_max_affection_94
    $ char1.change_affection(8)
    char1.talk "It looks even better when I push it out!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom5.webp") with dissolve:
        zoom 0.6667 align (0.6,0.7)
    pause 0.7
    pl "Yeah wow! Definitely!"
    $ player.change_lust(char1.sexiness)
    char1.talk "Some call 36-24-36 an hour glass figure..."
    char1.talk "What about 44-22-40?"
    $ faye.waist_size_known = True
    $ faye.hips_size_known = True
    pause 0.3
    pl "Oh wow!"
    "You look at her shapely ass for a moment, before your eyes wander up..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom5.webp"):
        subpixel True zoom 0.6667 align (0.6,0.7)
        ease 2.1 zoom 0.55 align (0.6,0.1)
    $ renpy.pause(2.3,hard=True)
    "Noticing you gazing at her chest..."
    char1.talk "*giggles* I know, no matter how good my ass might look."
    char1.talk "It can't compete with these! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Yeah! *grinning*"
    $ player.change_lust(char1.sexiness + 4)
    $ player.add_effect("erection")
    "You feel you pants getting tighter as your dick tries to break free..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6.webp"):
        subpixel True zoom 0.5 align (0.6,0.1)
        ease 1.7 zoom 0.9
    $ renpy.pause(1.9,hard=True)
    "... while you stare in awe at her gigantic tits!"
    char1.talk "Before I start..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "...could you do something for me [char1.playername]?"
    pause 0.3
    pl "Sure, anything."
    pause 0.3
    char1.talk "Great, I want to see your hard dick while I dance for you."
    char1.talk "Could you please undress."
    pause 0.3
    "Well considering she's almost naked herself, you can't find a good reason to say no."
    pl "Ummm... Sure, if that's what you want me to do."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6.webp") with dissolve:
        subpixel True zoom 0.85 align (0.6,0.1)
    pause 0.7
    char1.talk "Yes, please!"
    "Not taking your eyes off her, you undress and lean back on the sofa."
    "It's a good thing, that this room is well heated..."
    pause 0.3
    "...or maybe it's [char1.fname]'s presence."
    pause 0.3
    "In any case you're not feeling the slightest bit cold."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6mc.webp") with dissolve:
        zoom 0.5
    pause 0.5
    pl "I'm done."
    char1.talk "Yes, I can see that. *smiles*"
    pause 0.3
    char1.talk "It'll be so much more fun watching you trying not to grab your dick... *smirks*"
    pause 0.3
    pl "Ummm... What?"
    "She's such a tease..."
    pause 0.4
    pl "Damn you [char1.fname]!"
    "You're pretty determined not to give her the satisfaction of seeing you grab your dick while she dances for you..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom7.webp") with dissolve:
        zoom 0.3334
    pause 0.7
    char1.talk "*giggles* Let's get started!"
    pause 0.3
    "This is gonna be hard. You're already super horny!"
    "You let your eyes roam over her amazing body. Starting with her shapely legs..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom7.webp"):
        subpixel True zoom 0.3334 align (0.5,1.0)
        ease 1.7 zoom 0.6667
    $ renpy.pause(1.9,hard=True)
    "...not lingering for long, you look up at her knowing smile."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom7.webp"):
        subpixel True zoom 0.6667 align (0.5,1.0)
        ease 2.7 align (0.5,0.0)
    $ renpy.pause(3.0,hard=True)
    "Her amazing tits in full view as well."
    char1.talk "You haven't seen any of the good moves yet..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "{b}Oh my God, [char1.fname]{/b}! Your tits are epic!"
    $ char1.add_phone_background("Faye5")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom12.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "Seeing the fascinated and horny look on your face..."
    pause 0.3
    char1.talk "Ohh... I think I might have overdone it a bit... *smiles*"
    char1.talk "I don't want to risk having you cum just from watching me. *muses*"
    char1.talk "The show's far from over and I want you to be able to pleasure me with your hard dick..."
    "She slowly starts walking towards you..."
    show expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v1.webm")):
        zoom 0.5
    $ renpy.pause(2.9,hard=True)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom13.webp") with Dissolve(0.3):
        zoom 0.5
    pause 0.4
    pl "You think that's gonna improve things?"
    pause 0.3
    char1.talk "My huge bouncing tits probably won't... *smiles*"
    char1.talk "...but I have something for you that will!"
    pl "Ummm... Okay?"
    char1.talk "Here is a half dose of the blue pill."
    char1.talk "Having it inside your system will give you incredible stamina..."
    pause 0.3
    pl "A half dose?"
    char1.talk "Well you know about the other effect... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom13.webp") with dissolve:
        zoom 0.6 align (0.5,0.1)
    pause 0.4
    char1.talk "Your dick gets huge and I mean fucking horse dick huge."
    pause 0.3
    char1.talk "This can be fun sometimes as I like them really huge!"
    char1.talk "But today I want you to fuck me with all you've got, without having to hold back."
    char1.talk "Somewhat bigger is fine, but I don't want to be split in half. *giggles*"
    char1.talk "So please take it."
    pl "Okay."
    "You take the blue pill from her and swallow it."
    "It doesn't take long before you feel the effect."
    "Now there is no longer the risk of cumming too soon..."
    pl "I can already feel the effect!"
    pause 0.3
    pl "Now you can tease all you want... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6mc.webp") with fade:
        zoom 0.5
    pause 0.5
    char1.talk "I can see that it's working! *smiles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom6mc2.webp") with dissolve10:
        zoom 0.5
    pause 0.7
    pl "Wow!"
    char1.talk "That's a really nice size now... *giggles*"
    pause 0.3
    char1.talk "So... Where was I?"
    "[char1.fname] walks back to the pole."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom12.webp") with fade:
        zoom 0.667
    pause 0.7
    char1.talk "Yeah! Fucking huge tits! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom8.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "{b}Yes{/b}!"
    "Since you're able to enjoy her amazing knockers even more now..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom8.webp"):
        zoom 0.5 align (0.6,0.3)
        ease 1.7 zoom 1.0
    $ renpy.pause(1.9,hard=True)
    char1.talk "If you come any closer, you'll impale me with that pole of yours! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom9.webp") with dissolve:
        zoom 1.0 align (0.5,0.2)
    pause 0.7
    char1.talk "It's not your turn yet big boy."
    char1.talk "Get back on the sofa. I'll be with you soon enough!"
    "Not taking your eyes off her, you slowly move back..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom9.webp"):
        subpixel True zoom 1.0 align (0.5,0.2)
        ease 2.6 zoom 0.5
    $ renpy.pause(2.9,hard=True)
    pl "This isn't fair..."
    char1.talk "Stop complaining. *giggles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom10.webp") with dissolve:
        zoom 0.6 align (0.6,0.1)
    pause 0.7
    char1.talk "Hmmmm... *moans*"
    pause 0.3
    char1.talk "I bet you'd love to change places with this pole... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom10.webp"):
        subpixel True zoom 0.6 align (0.6,0.1)
        ease 1.6 zoom 1.0
    $ renpy.pause(1.9,hard=True)
    pl "You bet! *smiling*"
    "Mind-blowing how the huge dance pole is almost completely engulfed by her knockers!"
    char1.talk "You could probably enjoy this all night now..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom11.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "...but I'm so wet and horny. I need you inside me."
    pl "I can't wait to pay you back! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom12.webp") with dissolve:
        zoom 0.5
    pause 0.4
    char1.talk "I'm sure of that!"
    "She slowly starts walking towards you again with her sexy swaying huge globes..."
    show expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v1.webm")):
        zoom 0.5
    $ renpy.pause(2.9,hard=True)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom13.webp") with Dissolve(0.3):
        zoom 0.5
    pause 0.4
    char1.talk "Time to get rid of this tiny red string."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom14.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "If you can't control yourself and need to stroke your huge dick..."
    char1.talk "Now would be a good time. *smirks*"
    "You're pretty determined not to give her the satisfaction..."
    pause 0.3
    pl "Not that you don't have a really nice ass..."
    pl "... but I think I can wait for the grand prize."
    pause 0.3
    char1.talk "If you say so..."
    "She turns around and climbs on the sofa."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom15.webp") with fade:
        zoom 0.5
    pause 1.0
    char1.talk "Mmmm... You're right... *moans*"
    char1.talk "It just wouldn't do to touch yourself..."
    char1.talk "Mmmmm... Aaaa... *moans some more*"
    char1.talk "A real guy doesn't need to do that in front of a naked girl!"
    pause 0.3
    char1.talk "Not even when she's got the biggest tits he's ever seen..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom15.webp"):
        subpixel True zoom 0.5 align (0.65,0.15)
        ease 1.4 zoom 0.85
    $ renpy.pause(1.7,hard=True)
    $ player.change_lust(char1.sexiness * 2)
    "Blue pill or not, if you don't get your dick inside her soon, you're gonna grab it yourself..."
    "But not just yet!"
    pause 0.4
    char1.talk "I know you'd like to put it between my huge mounds and fuck them real good..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom16.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Wow! Oh my God!"
    char1.talk "Maybe next time I'll let you play with my tits... *smiles*"
    pause 0.3
    char1.talk "Wrap them around your swollen manhood..."
    pause 0.3
    char1.talk "Until you cum all over them..."
    pause 0.4
    "Despite the incredible view you still manage not to grab your dick..."
    char1.talk "I'm so horny! Please fuck me!"
    pause 0.3
    "Well, you can play her game too..."
    pl "I really like the view and I'm not that horny yet... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom16.webp"):
        subpixel True zoom 0.5 align (0.65,0.3)
        ease 1.5 zoom 0.8
    $ renpy.pause(1.8,hard=True)
    "The way she's smiling at you, she knows you're lying!"
    char1.talk "{i}Really{/i}..."
    char1.talk "We can't have that!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom17.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "The prove her point, [char1.fname] starts to massage your dick with her foot."
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v2.webm")) at zoom_c(0.5)
    $ renpy.pause(3.0,hard=True)
    $ player.change_lust(char1.sexiness)
    pl "You're a naughty girl [char1.fname]."
    char1.talk "I know! *smirks*"
    char1.talk "What are you gonna do about it?"
    "Instead of an answer, you grab her leg, turn her around and slide your rock-hard cock inside her wet pussy."
    $ renpy.start_predict("*Faye_blue_room_sex_cam*")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom18.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Mmmm... {b}Yes{/b}! I've been a bad girl! *moans*"
    pause 0.4
    pl "It's time to pay you back, {i}Honey{/i}!"
    $ ll_cameras = []
    $ lo_cam0 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_blue_room_sex_cam1_", {"face_x":1900, "face_y":900, "breasts_x":1700, "breasts_y":680, "pussy_x":1040, "pussy_y":460})
    $ lo_cam1 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_blue_room_sex_cam2_", {"face_x":1330, "face_y":370, "breasts_x":1340, "breasts_y":680, "pussy_x":0, "pussy_y":0})
    $ ll_cameras.append(lo_cam0)
    $ ll_cameras.append(lo_cam1)
    $ ll_sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    $ l_cum_control = {"cum_x":1575, "cum_y":765, "cum_fps":35, "cum_zoom":0.5, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":char1.talk, "what":"{b}Yes!{/b}I'm almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"Take your time, that pill you gave me is amazing!", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Damn! You're killing me! *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"I'm cummmminnnggg!", "pause":1.2})
    $ ll_speed_talk = [{"fast":"Yes! Faster!", "faster":"*moans* Make me cum hard!", "slow":"You're so big and hard! *moans*", "slower":"Please don't slow down!"}]
    #call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 0.85) from _call_interactive_sex_87
    $ char1.add_pl_interaction("sex")
    char1.talk "Mmmm... Yes!"
    $ char1.change_lust(-50)
    $ char1.change_endurance(-50)
    char1.talk "Oh wow!"
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom18.webp") with dissolve:
        zoom 0.5
    pause 0.7
    $ renpy.stop_predict("*Faye_blue_room_sex_cam*")
    char1.talk "What are you doing?"
    char1.talk "You haven't cum yet!"
    pl "I'm far from finished and I don't want to hurt you."
    char1.talk "If you don't continue fucking me like you mean it, I'm going to hurt you. *smirks*"
    pause 0.4
    pl "Oh... Okay. *grinning*"
    show expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v3.webm")) at move_video5()
    $ renpy.pause(1.5,hard=True)
    pl "Mmmm... You're so tight! *moans*"
    $ renpy.pause(2.0,hard=True)
    char1.talk "You're so big and hard... Just how I love it. *moans some more*"
    $ char1.change_lust(10)
    $ renpy.pause(2.0,hard=True)
    "She feels so tight and some of that is probably related to the immense size of your dick!"
    pl "Aaahhh... Mmmmm..."
    $ renpy.pause(2.0,hard=True)
    $ char1.change_lust(15)
    char1.talk "Yes baby! You're making me cum again!"
    pause 0.7
    char1.talk "Look at my huge knockers!"
    pause 1.0
    show expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v4.webm")) at zoom_c(0.5, i_speed=3.0, i_factor=1.3, i_align_y=0.3) with dissolve
    hide expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v3.webm"))
    #call actions_used (1) from _call_actions_used_645
    $ renpy.pause(2.0,hard=True)
    "The way her huge knockers are bouncing is driving you crazy with lust!"
    pause 1.0
    char1.talk "Harder [char1.playername]!"
    pause 0.5
    pl "Mmmm.... *moans* Can you take it?"
    pause 1.0
    char1.talk "Stop talking and FUCK ME HARDER! *moans*"
    $ char1.change_lust(15)
    show expression (Movie(channel="vid", play="scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_blueroom_v3.webm")) at move_video5() with dissolve
    $ renpy.pause(1.5,hard=True)
    "You ram your dick into her tight pussy, making her moan even more..."
    pause 2.0
    char1.talk "Oh my God! Mmmmm... It's so intense... *moans*"
    pause 1.5
    pl "I'm almost there!"
    pause 0.7
    char1.talk "YES! Ahhh... *screams*"
    char1.talk "Me too!"
    $ char1.change_endurance(-20)
    $ char1.change_lust(-40)
    pause 1.0
    "With the effects of the blue pill starting to fade, you can't keep it up any longer..."
    pl "Cummminnng too..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom18.webp") with dissolve:
        zoom 0.5
    pause 0.7
    "You shoot your cum into her tight pussy!"
    $ player.change_endurance(-40)
    $ player.change_lust(-50)
    pause 0.5
    char1.talk "Wow! That was incredible!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom19.webp") with dissolve:
        zoom 0.5
    pause 0.5
    char1.talk "I want your hot cum on my body!"
    "Even after your intense orgasm, the effect of the blue pill makes you pump out more cum..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom20.webp") with dissolve:
        zoom 0.5
    pause 0.5
    pl "It was amazing [char1.fname]. You're so tight!"
    pause 0.5
    char1.talk "*giggles* I'm not that tight! Your dick was just so fucking huge!"
    pause 0.5
    char1.talk "Now I really need a shower... *smirks*"
    pl "Yeah, sorry about that."
    char1.talk "Nothing to be sorry about. I love taking showers..."
    char1.talk "...and I love your cum all over my body!"
    pause 0.3
    char1.talk "But I'm not leaving without a proper kiss!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom21.webp") with fade:
        zoom 0.5
    pause 0.7
    play sound "sounds/kiss3.mp3"
    char1.talk "Mmmm... *kissing sounds*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom21.webp"):
        zoom 0.5 align (0.6,0.0)
        ease 1.5 zoom 0.8
    $ renpy.pause(1.8,hard=True)
    "You french kiss for a while which gets you turned on all over again..."
    $ player.change_lust(char1.sexiness + 2)
    pause 0.5
    "Until she breaks it off."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_blueroom13.webp") with fade:
        zoom 0.5
    pause 0.5
    char1.talk "Have a good night my stallion."
    pl "You too [char1.fname]."
    $ char1.add_scene_seen("Nightbar_blue_room")
    $ char1.locations[actions_left-1] = char1.fname + "_room"
    $ char1.locations[actions_left-2] = char1.fname + "_room"
    $ char1.locations[actions_left-3] = char1.fname + "_room"
    $ char1.locations[actions_left-4] = char1.fname + "_room"
    "[char1.fname] dresses and leaves the blue room. You head down the stairs too."
    scene expression "locations/loc_nightbar_stairs_down.webp" with fade:
        zoom 0.667
    pause 0.7
    return "nothing"



label nightbar_hotshots_heat_heather(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    "She slides down from the bar stool..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "I feel like I'm on fire!"
    "Despite her [l_breast_size_text] in full view, you take a look at her legs covered in those boots..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve10:
        zoom 0.5
    pause 1.2
    "...her boots really seem to scream {b}fuck me{/b}!"
    $ player.change_lust(char1.sexiness)
    char1.talk "Really? {w}You're looking at my legs right now?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with dissolve10:
        zoom 0.5
    pause 1.3
    char1.talk "I'm getting hornier every second!"
    char1.talk "I feel my nipples growing already..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -800 ypos -500
    pause 2.8
    "Compared to her small areolas, her nipples are indeed quite huge."
    char1.talk "What do you think?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 1.0 xpos -800 ypos -500
        ease 3.0 zoom 0.5 xpos 0 ypos 0
    pause 1.2
    char1.talk "Aren't my huge babies more interesting than my legs? *smirks*"
    pause 0.5
    pl "Ummm... Wow!"
    "She walks towards you, her [l_breast_size_text] swinging left and right while she does."
    call show_image_sequence ("scenes/Heather/nightbar/anim/Heather_nightbar_hs0_heat_bg.webp", "scenes/Heather/nightbar/anim/Heather_nightbar_hs0_heat[number].webp", 1, 10, 0.2, 0.5, 0.5) from _call_show_image_sequence_2
    $ player.change_lust(char1.sexiness + 4)
    pl "Damn [char1.fname], you're killing me!"
    t_crowd_of_girls "*cheers from the girls* {b}[char1.fname], [char1.fname], [char1.fname]{/b}!"
    t_crowd_of_girls "{b}[player.fname], [player.fname], [player.fname]{/b}! *more cheers from the girls*"
    scene expression "scenes/[char1.fname]/nightbar/anim/[char1.fname]_nightbar_hs0_heat_bg.webp":
        zoom 0.5
    show expression ("scenes/[char1.fname]/nightbar/anim/[char1.fname]_nightbar_hs0_heat10.webp"):
        zoom 0.5
        ease 1.5 zoom 0.7 xpos -350 ypos -50
    pause 2.0
    char1.talk "I know you and the girls would really like to see some action now..."
    char1.talk "But I'm not that kind of girl."
    char1.talk "I mean I can be all kinds of naughty in public..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 0.5
    pause 0.9
    char1.talk "...but some things are better done in private. *smirks*"
    char1.talk "Why don't you come to my room a bit later tonight. Maybe in about an hour?"
    char1.talk "I'll have a nice surprise waiting for you!"
    $ char1.rem_action_cooldown("visit_girls_room")
    pause 0.5
    pl "Ummm... Okay... *a little sad*"
    t_crowd_of_girls "{b}Boohhh{/b}! {b}Boohh{/b}! That's not the spirit!"
    yumiko.talk "Come on girls! Be nice and respect her decision."
    t_crowd_of_girls "*some muttering* Hmmm... Okay..."
    "[char1.fname] picks up her clothes and gets dressed."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
        zoom 0.667
    pause 0.7
    "Not wanting to be the only one sitting at the bar half naked, you dress as well."
    pause 0.6
    yumiko.talk "Since both of you are dressed now, I declare the game ended!"
    yumiko.talk "Enjoy your evening everyone!"
    t_crowd_of_girls "You too Yumiko! *chorus from the girls*"
    pause 0.6
    yumiko.talk "And let me know how your evening ended [player.fname]... *winks*"
    return _return





label nightbar_hotshots_heat_jessica(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    "She stands up from the bar stool..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with fade:
        zoom 0.5
    pause 0.8
    "... and stretches lasciviously."
    "Making her [l_breast_size_text] balloon out!"
    pause 0.5
    char1.talk "Have you ever met a school girl with a body like mine?"
    char1.talk "With tits almost the size of volleyballs and yet so soft?"
    $ char1.add_pl_interaction("tease_talk")
    $ char1.add_pl_interaction("tease_boobs")
    pl "*gulp*"
    pl "Ummm... I don't think so..."
    $ player.change_lust(char1.sexiness + 4)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        zoom 0.5
        ease 1.8 zoom 1.0 xpos -800 ypos -400
    pause 2.2
    char1.talk "The way you're staring at them like you want to do all kinds of naughty things with them makes me really wet!"
    char1.talk "Oh... {w}I guess a good girl shouldn't say that..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        zoom 0.5
    pause 0.8
    $ char1.change_lust(8)
    t_crowd_of_girls "{b}Jessi! {w}Jessi! {w}Jessi!{/b}"
    pause 0.4
    char1.talk "Do you think I'm a good girl Mr. [player.lname]?"
    pause 0.5
    char1.talk "I guess good girls don't have sex in a bar... *musing*"
    "You slowly let your eyes roam over her fantastic body..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp"):
        subpixel True zoom 0.5
        ease 1.4 zoom 1.0 xpos -800 ypos -720
        pause 0.5
        ease 4.0 zoom 1.0 xpos -900 ypos 0
    $ renpy.pause(6.0, hard=True)
    char1.talk "So... {w}Do you think I'm a good girl?"
    $ player.change_lust(char1.sexiness + 2)
    menu:
        "Yes, you think she's a good girl most of the time" if True:
            pl "I think you're a good girl most of the time..."
            pause 0.4
            pl "Just not today it seems. *grinning*"
            char1.talk "Mmmm... *moans* I guess you don't know me well enough Mr. [player.lname]..."
        "No, she's not a good girl" if True:

            pl "Oh no! You're definitely not a good girl [char1.fname]."
            char1.talk "You're right..."
            char1.talk "A good girl shouldn't masturbate in front of a guy..."
            $ char1.change_lust(8)
            char1.talk "Not even when the guy is as cute as you are. *moans*"

    pause 0.5
    char1.talk "Damn! This thong is so in the way of more fun!"
    "She turns around and..."
    $ char1.add_pl_interaction("tease_ass")
    $ char1.add_pl_interaction("tease_pussy")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3a.webp") with fade:
        zoom 0.5
    pause 0.8
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3b.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "...pulls her thong down over her incredible ass..."
    "...exposing her wet pussy!"
    pause 0.5
    "Holy shit! This girl is driving you crazy with lust!"
    $ player.change_lust(char1.sexiness + 4)
    char1.talk "Just look how tight my sweet pussy is!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3c.webp") with dissolve3:
        zoom 0.5
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3d.webp") with dissolve3:
        zoom 0.5
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3e.webp") with dissolve3:
        zoom 0.5
    pause 0.7
    "Leaning forward until her hands are on the bar stool, you have an incredible view of her tight wet pussy!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3e.webp") with dissolve:
        zoom 1.0 xpos -800 ypos -600
    pause 0.8
    $ player.change_lust(char1.sexiness + 4)
    pl "*gulp*"
    char1.talk "I'm definitely not a good girl! *smirks*"
    $ char1.change_lust(8)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "But I guess even a bad girl can't walk around naked in a bar forever. *smiles*"
    pl "Ohhh...!?"
    char1.talk "Don't look at me like that!"
    char1.talk "It'll be fun too!"
    "She picks up her top from the floor..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5a.webp") with fade:
        zoom 0.5
    pause 0.8
    "...and pulls it tight."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5b.webp") with dissolve3:
        zoom 0.5
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5c.webp") with dissolve3:
        zoom 0.5
    pause 0.7
    char1.talk "So what do you think Mr. [player.lname]?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "My math teacher told me my huge tits look even bigger squeezed inside a tight top!"
    pause 0.4
    char1.talk "Do you think they look bigger?"
    pl "*gulp* Ummm... {w}Yeah, maybe..."
    $ player.change_lust(char1.sexiness + 4)
    $ player.add_effect("erection")
    "Your massive boner threatens to destroy your pants..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Yes, I think so too!"
    char1.talk "When I put a dildo between them, it always looks so small."
    "Looking down at the bulge in your pants..."
    char1.talk "Oh! Did I cause that? *smirks*"
    char1.talk "Wow! It looks really big..."
    char1.talk "I wonder how it would compare to my dildo... *musing*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8a.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Silly me! *giggles*"
    char1.talk "I still haven't put my skirt back on..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8b.webp") with dissolve3:
        zoom 0.5
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8c.webp") with dissolve3:
        zoom 0.5
    pause 0.7
    char1.talk "That's much better!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Oh... {w}I'm not so sure I agree!"
    t_crowd_of_girls "{b}[player.fname]! {w}[player.fname]! {w}[player.fname]!{/b}"
    pause 0.4
    t_crowd_of_girls "{b}Jessi! {w}Jessi! {w}Jessi!{/b}"
    if char1.get_scene_seen_times("Hotshots_heat1") > 1:
        if char1.check_love(4, 0, False) == True and char1.check_lust(4, False) == True:
            char1.talk "Would you like to go upstairs with me?"
            pl "Oh wow, yes!"
            char1.talk "{b}Bye girls!{/b} The green room is occupied for the next few hours... *smirks*"
            yumiko.talk "Have fun you two!"
            t_crowd_of_girls "{b}Yeah!{/b} Have lots of fun! {w}And don't damage the sofa... *laughter*"
            #call nightbar_green_room_jessica (char1) from _call_nightbar_green_room_jessica
            
    elif True:
        char1.talk "Next time you win, I'll have a surprise waiting for you!"
        pl "Now you've made me really curious!"
    if char1.id == jessica.id:
        jump nightbar_green_room_jessica2
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
        zoom 0.667
    pause 0.7
      
    "Not wanting to be the only one sitting at the bar half naked, you dress as well."
    pause 0.6
    yumiko.talk "Since both of you are dressed now, I declare the game ended!"
    yumiko.talk "Everyone, enjoy your evening!"
    t_crowd_of_girls "You too Yumiko! *chorus from the girls*"
    label nightbar_hotshots_heat_jessica_end:
    return _return
    
label nightbar_green_room_jessica2:
    $ l_sex = True
    $ char1.add_pl_interaction("sex")
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room1.webp") with fade:
        zoom 0.334
    pause 0.7
    char1.talk "Are you coming?"
    "Still a bit stunned, you get up and follow her to the stairs."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room1.webp"):
        subpixel True zoom 0.334
        ease 4.2 zoom 0.8 xpos -900 ypos -200
    $ renpy.pause(4.5, hard=True)
    pl "I'm right behind you!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room2.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "I hope you're a lot more than that real soon!"
    "You stare at her incredible ass and exposed pussy for a moment..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room2.webp") with dissolve:
        subpixel True zoom 1.25 xpos -950 ypos -800
    pause 0.7
    $ player.change_lust(char1.sexiness + 4)
    char1.talk "Does looking at my firm ass and pussy turn you on?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room2.webp"):
        subpixel True zoom 1.25 xpos -950 ypos -800
        ease 2.0 ypos 0
    pause 2.3
    pl "Yes, definitely! *grinning sheepishly*"
    char1.talk "I can't wait to feel you inside me! *moans*"
    char1.talk "Let's keep going!"
    "You enter the green room right behind her."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room3.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "How about we take the large round bed?"
    pl "Sure, there's a lot more space than on the sofa."
    char1.talk "My thoughts exactly. *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room4.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "You look really beautiful [char1.fname]!"
    char1.talk "Thank you!"
    char1.talk "Just wait until I'm naked!"
    pause 0.4
    char1.talk "I promise you won't forget your night with the busty schoolgirl. *smirks*"
    char1.talk "I want to watch you undressing! {w}Always makes me horny!"
    pause 0.4
    "You undress in front of her..."
    pause 0.7
    "She takes an appreciative look at you."
    char1.talk "That's how I love it!"
    $ char1.change_lust(15)
    char1.talk "Now it's my turn!"
    "You watch how she removes her top and skirt, followed by the white stockings..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room5.webp") with fade:
        zoom 0.334
    pause 0.7
    pl "{b}Wow{/b}! {w}You're so hot [char1.fname]!"
    char1.talk "Come here and show me how hot you think I am!"
    "You walk to the bed..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room5.webp"):
        zoom 0.334
        ease 2.5 zoom 0.8 xpos -1100 ypos -500
    pause 2.7
    "...and climb on it between her legs..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room6.webp") with dissolve:
        zoom 0.5
    pause 0.8
    pl "You look delicious! {w}I want to taste you [char1.fname]!"
    pause 0.4
    char1.talk "I'm not holding you back!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room7.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "She spreads her legs and starts playing with one of her nipples!"
    pause 0.4
    "You watch her for a moment, before you dive between here legs and start licking her pussy..."
    $ ll_cameras = []
    $ lo_cam1 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_green_room_v1_cam1_", {"face_x":0, "face_y":0, "breasts_x":490, "breasts_y":200, "pussy_x":1480, "pussy_y":760})
    $ ll_cameras.append(lo_cam1)
    $ lo_cam2 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_green_room_v1_cam2_", {"face_x":0, "face_y":0, "breasts_x":960, "breasts_y":600, "pussy_x":1400, "pussy_y":510})
    $ ll_cameras.append(lo_cam2)
    $ ll_sequence = [1,2,3,4,5,6,6,5,4,3,2,1,2,3,4,5,6,6,5,4,3,2,1,1,2,3,4,4,3,2,1]
    $ l_cum_control = {"cum_x":1480, "cum_y":760, "cum_fps":35, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":char1.talk, "what":"You should really stop now... *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Mmmm... Yes! *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"I want you to fuck me now! *moans*", "pause":0.2})
    $ ll_speed_talk = [{"fast":"Oh my God Yes! You're incredible!", "faster":"*moans* If you don't slow down I'll cum!", "slow":"Just a little break... *moans*", "slower":"Please don't slow down! Lick me harder!"}]
    #call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 2.0, "Stop licking") from _call_interactive_sex_6
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room7.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "You were incredible, I almost came! *moans*"
    char1.talk "Please take me from behind..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room10.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "...I need to feel your hard cock inside my tight pussy!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room10.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -800 ypos -300
    pause 2.3
    pl "I can't wait!"
    "You push your hard cock inside her eagerly waiting pussy!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room11.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Oh my God! yes!"
    $ ll_cameras = []
    $ lo_cam1 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_green_room_v2_cam2_", {"face_x":0, "face_y":0, "breasts_x":0, "breasts_y":0, "pussy_x":1200, "pussy_y":950})
    $ ll_cameras.append(lo_cam1)
    $ lo_cam2 = cl_camera("images/scenes/" + char1.fname + "/nightbar/anim/" + char1.fname + "_nightbar_green_room_v2_cam1_", {"face_x":720, "face_y":580, "breasts_x":1160, "breasts_y":870, "pussy_x":1840, "pussy_y":570})
    $ ll_cameras.append(lo_cam2)
    $ ll_sequence_full = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    $ ll_sequence_to_in = [1,2,3,4,5]
    $ ll_sequence_to_full = [5,4,3,2,1]
    $ ll_sequence_in = [6,6,7,7,8,8,9,9,10,10,10,9,9,9,8,8,7,7,6,6]
    $ ll_sequence = ll_sequence_to_full + ll_sequence_full + ll_sequence_full + ll_sequence_to_in + ll_sequence_in + ll_sequence_in + ll_sequence_to_full + ll_sequence_full + ll_sequence_full + ll_sequence_to_in + ll_sequence_in
    $ l_cum_control = {"cum_x":1200, "cum_y":950, "cum_fps":35, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":char1.talk, "what":"Yes! Almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"Me too! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"Just a little longer...", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Mmmm... Okay! *moans*", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Yes! I'm cummmminnnggg!", "pause":1.2})
    $ ll_cum_talk.append({"who":pl, "what":"Cummmiinnnggg too!", "pause":1.0})
    $ ll_speed_talk = [{"fast":"Yes! Faster!", "faster":"*moans* Yes! Make me cum very hard!", "slow":"Oh my God! You're so huge! *moans*", "slower":"Please don't slow down!"}]
    #call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, ll_speed_talk, 0.8, "Cum!") from _call_interactive_sex_7
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room12.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "You unload your cum into her tight pussy!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room13.webp") with dissolve:
        zoom 0.5
    pause 0.8
    $ player.change_lust(50)
    $ player.change_endurance(50)
    $ char1.change_lust(50)
    $ char1.change_endurance(50)
    "Before you pull out."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room14.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Fuck! {w}That was amazing [char1.playername]!"
    pl "Yes, absolutely!"
    char1.talk "I didn't know that being a school girl would be so much fun! *smiles*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room15.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Thank you for this exciting evening [char1.playername]. *smiles"
    pause 0.5
    pl "Nothing to thank me for. I'm pretty sure I enjoyed it at least as much as you! *smiling back*"
    char1.talk "It's a bit cold here without the exercise... *smirks*"
    pause 0.5
    char1.talk "Can you hand me the top and skirt please."
    pause 0.6
    pl "Sure, here you go."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_green_room16.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Thanks."
    "You get dressed as well."
    char1.talk "Shall we go back down?"
    pl "Yes, Okay."
    scene expression ("locations/loc_nightbar_stairs_down.webp") with fade:
        zoom 0.667
    pause 0.7
    pl "See you later [char1.fname]."
    char1.talk "Absolutely! {w}And oh... {w}After you [char1.playername]. *giggles*"
    char1.talk "I want to have a look at your tight butt! *smirks*"
    pl "Haha! *laughs*"
    "You head down the stairs back to the night bar."
    pause 0.5
    "Still thinking about the incredible sex you've just had with [char1.fname]."
    $ char1.add_scene_seen("Nightbar_green_room")
    $ char1.add_phone_background("Jessica4")
    return "nothing"

label nightbar_hotshots_heat_renee(char1):
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "I feel like my body is on heat all of a sudden. *moans*"
    "She squeezes her [l_breast_size_text]."
    pause 0.3
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Somehow my tits feel just a little fuller."
    pause 0.4
    $ player.change_lust(char1.sexiness)
    pl "Ummm... I really don't know..."
    pause 0.5
    yumiko.talk "Hey [char1.fname], why don't you show us some pole dance moves?"
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 0.5
    yumiko.talk "I've heard you're really good at it!"
    pause 0.4
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.opponent_max_undress].webp") with fade:
        zoom 0.667
    pause 0.8
    char1.talk "Er... I'm not sure.. I mean, I'm not wearing p..."
    t_crowd_of_girls "{b}Poledance!{/b} {w}{b}Poledance!{/b} {w}{b}Poledance!{/b}"
    pause 0.4
    t_crowd_of_girls "{b}Turn him on!{/b} {w}{b}Make him sweat!{/b}"
    pause 0.3
    char1.talk "Okay! Okay! I'll do it!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "If you want me to [char1.playername]!"
    pause 0.4
    pl "Oh Wow! Sure I want to see you pole dance!"
    pause 0.3
    char1.talk "Okay then! {w}Yumiko, can you please change the lights from blue to red."
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with fade:
        zoom 0.5
    pause 0.5
    yumiko.talk "Sure [char1.fname], here you go!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with fade:
        zoom 0.5
    pause 0.8
    char1.talk "Having really huge tits is great when pole dancing..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Although mine aren't super huge, they're big enough! *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -800
    pause 2.8
    "For any woman of her athletic build, in fact her tits are quite huge!"
    pause 0.3
    char1.talk "Flexibility and being athletic is even more important!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 1.0 xpos -800
        ease 3.0 zoom 1.0 xpos -800 ypos -650
    pause 3.5
    "And her legs are even better!"
    pause 0.4
    char1.talk "Now if you stop staring at my legs and give me some room, I can let the show begin... *smirks*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 1.0 xpos -800 ypos -650
        ease 1.5 zoom 0.5 xpos 0 ypos 0
    pause 2.0
    char1.talk "You'll see, I have plenty of flexibility!"
    "She grabs the pole with both hands, holds on tight..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 0.5
    "...and spreads her legs!"
    "Shit! She's not wearing anything below her skirt!"
    $ player.change_lust(char1.sexiness + 6)
    t_crowd_of_girls "{b}Cherry!{/b} {w}{b}Cherry!{/b} {w}{b}Pussy!{/b} {w}{b}Pussy!{/b}"
    pause 0.3
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp"):
        zoom 0.5
        ease 3.0 zoom 1.0 xpos -750 ypos -400
    pause 1.5
    yumiko.talk "{b}Hey girls{/b}! {w}Behave! *giggles*"
    pause 1.0
    pl "*gulp* {b}Oh Wow{/b}!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp"):
        zoom 1.0 xpos -750 ypos -400
        ease 2.0 zoom 1.0 xpos -750 ypos -40
    pause 2.8
    char1.talk "Anyone else feeling {b}HOT{/b} now too? *smiles*"
    pause 0.7
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp"):
        zoom 1.0 xpos -750 ypos -40
        ease 1.5 zoom 0.5 xpos 0 ypos 0
    pause 2.0
    t_crowd_of_girls "{b}[player.fname]!{/b} {w}{b}[player.fname]!{/b} {w}*laughs from the girls*"
    pause 0.4
    yumiko.talk "Our dear [player.fname] looks quite taken... *giggles*"
    pause 0.3
    yumiko.talk "{b}Hey [char1.fname]{/b}! We want to see more!"
    pause 0.4
    yumiko.talk "{b}Girls{/b}! {w}Let her know how much we want it!"
    t_crowd_of_girls "{b}[char1.fname]!{/b} {w}{b}[char1.fname]!{/b} {w}{b}[char1.fname]!{/b}"
    pause 0.3
    t_crowd_of_girls "{b}We want more!{/b} {w}{b}We want more!{/b}"
    pause 0.4
    char1.talk "The next one's for [char1.playername]! *smiles"
    pause 0.4
    char1.talk "So you can stare at my face, tits, pussy and legs at the same time!"
    pl "Er... What?"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with dissolve:
        zoom 0.5
    pause 0.9
    "She lifts her leg in the air and spreads herself wide!"
    "Damn! Sex with her must be incredible!"
    $ player.change_lust(char1.sexiness + 7)
    char1.talk "Don't be shy! Come closer! *smirks*"
    pause 0.3
    pl "If you insist... *sheepishly*"
    "You slowly walk closer to her..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp"):
        subpixel True
        zoom 0.5
        linear 3.0 zoom 1.1 xpos -900 ypos -70
    pause 3.6
    char1.talk "Are you enjoying the view [char1.playername]?"
    char1.talk "Thinking some dirty thoughts? *smirks*"
    pause 0.4
    pl "Ummm..."
    t_crowd_of_girls "{b}[player.fname]!{/b} {w}{b}[player.fname]!{/b} {w}*laughs from the girls*"
    char1.talk "Now if you step back a bit, I'm ready for the final pose!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp"):
        subpixel True
        zoom 1.1 xpos -900 ypos -70
        linear 2.0 zoom 0.5 xpos 0 ypos 0
    pause 0.7
    "As the girls cheer you on, you take a few steps backward..."
    t_crowd_of_girls "{b}[char1.fname]!{/b} {w}{b}[char1.fname]!{/b} {w}{b}[char1.fname]!{/b}"
    "She expertly grabs her skirt, opens it and throws it to the side,"
    "before getting down on her knees."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with dissolve:
        zoom 0.5
    pause 1.0
    pl "Wow! That's {b}super hot{/b}!"
    $ player.change_lust(char1.sexiness + 8)
    pause 0.4
    t_crowd_of_girls "{b}Super hot!{/b} {w}{b}Super hot!{/b}"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp"):
        zoom 0.5
        ease 1.5 zoom 1.0 xpos -750 ypos -550
    pause 2.0
    pl "[char1.fname], [char1.fname], [char1.fname]!"
    pause 0.4
    char1.talk "Yumiko, lights off please!"
    pause 0.8
    yumiko.talk "Here you go!"
    show expression "gui/black.jpg":
        alpha 0.0
        linear 1.0 alpha 0.95
    pause 1.5
    t_crowd_of_girls "Ohhh yeah! That was great [char1.fname]!"
    pause 0.8
    "After a moment, Yumiko turns the lights back on."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp") with fade:
        zoom 0.5
    pause 1.0
    char1.talk "Did you like the pole dance?"
    pause 0.4
    pl "Oh Yes! You were incredible [char1.fname]!"
    char1.talk "Thank you! *smiles*"
    call change_char_max_affection (char1, 4) from _call_change_char_max_affection_101
    $ char1.change_affection(8)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp"):
        zoom 0.5
        ease 1.5 zoom 0.8 xpos -600 ypos -50
    pause 2.0
    char1.talk "I'm still kind of {i}hot{/i}, you know... *whispering*"
    "She grabs you head and pulls you close for a deep kiss..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat8.webp") with dissolve:
        zoom 0.5
    pause 1.5
    char1.talk "Mmmmmm... *moans*"
    pause 0.3
    pl "*kissing sounds*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat8.webp"):
        zoom 0.5
        linear 1.2 zoom 0.8 xpos -500
    pause 1.7
    char1.talk "*whispering* Next time, maybe I'll dance on {b}your{/b} pole."
    $ player.change_lust(char1.sexiness + 6)
    pl "Is that a promise?"
    pause 0.3
    char1.talk "We'll see..."
    pause 0.6
    yumiko.talk "Okay girls, that concludes our HotShots game this evening!"
    pause 0.4
    char1.talk "Hmmm... Okay..."
    "[char1.fname] extracts herself from your embrace and gets dressed..."
    pause 0.6
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs1.webp") with fade:
        zoom 0.667
    pause 0.7
    "...while you get dressed too."
    pause 0.5
    yumiko.talk "Since our two players are dressed now, enjoy your evening everyone!"
    t_crowd_of_girls "You too Yumiko! *chorus from the girls*"
    $ char1.add_scene_seen("Hotshots_heat1")
    return _return





label nightbar_hotshots_heat_yvette(char1):
    $ char1.add_scene_seen("Hotshots_heat1")
    $ l_breast_size_text = char1.get_breast_size_text()
    char1.talk "Oh wow! *moans* It feels like I'm on fire!"
    $ char1.change_lust(15)
    "She slowly walks towards you, making you all the more aware of her [l_breast_size_text]."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True
        zoom 0.5
        ease 2.0 zoom 1.2 xpos -1000 ypos -550
    pause 2.8
    "It doesn't take her long to notice you staring at her voluptuous knockers..."
    char1.talk "Do you like my breasts? *smiles*"
    pause 0.3
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat1.webp"):
        subpixel True
        zoom 1.2 xpos -1000 ypos -550
        ease 1.8 zoom 1.2 xpos -1000 ypos 0
    pause 2.5
    pl "Yes! OMG! I love them!"
    $ player.change_lust(char1.sexiness + 2)
    char1.talk "Mmmm... I thought so. *smiles*"
    pause 0.6
    char1.talk "Let's see if you also like my butt..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat2.webp") with dissolve:
        zoom 0.5
    pause 0.8
    char1.talk "Round and juicy enough?"
    pause 0.5
    pl "It's lovely!"
    char1.talk "Even with my chest exposed, I still feel so hot!"
    char1.talk "Let's see if this helps..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp") with dissolve:
        zoom 0.5
    pause 0.8
    if g_hotshots.player_undress < 3:
        char1.talk "I think it's only fair that you expose your muscular upper body as well now!"
        pl "Sure, for whatever reason I feel it's really hot in here... *smiles*"
        if g_hotshots.player_undress == 1:
            "You remove your shirt and T-shirt, while she slides her shorts further down."
        elif True:
            "You remove your T-shirt, while she slides her shorts further down."
        $ g_hotshots.player_undress = 3
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat3.webp"):
        zoom 0.5
        ease 2.0 zoom 1.0 xpos -600 ypos -200
    pause 2.8
    pl "*gulp* Oh wow [char1.fname]!"
    char1.talk "Hmmm... It's still not much cooler..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 1.0 xpos -600 ypos -200
    pause 0.8
    "After she has pulled down her shorts, you get a good look at her amazing ass, covered only by a tiny string now."
    $ player.change_lust(char1.sexiness + 3)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat4.webp") with dissolve:
        zoom 1.0 xpos -600 ypos -200
        ease 2.0 zoom 0.5 xpos 0 ypos 0
    pause 2.5
    char1.talk "Do you think you can see my breasts from behind?"
    pause 0.3
    pl "Ummm... I don't kn..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat5.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "How about now? *giggles*"
    pl "Oh my God!"
    t_crowd_of_girls "{b}Yeah!{/b} {b}{w}Yeah!{/b} {b}{w}Wow [char1.fname]!{/b} {b}{w}Great knockers!{/b}"
    "You stare in awe at her voluptuous form.\n{w}What an incredible combination of soft and round paired with a tiny waist."
    $ player.change_lust(char1.sexiness + 4)
    char1.talk "I want to touch you [char1.playername]. *moans*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat6.webp") with dissolve:
        zoom 0.8 xpos -450 ypos -432
    pause 0.7
    pl "*gulp*"
    "She slowly turns around..."
    show expression (Movie(channel="vid", play= "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs0_heat_v1.webm")):
        zoom 0.8 xpos -450 ypos -432
        ease 2.5 ypos 0
    pause 2.6
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat7.webp"):
        subpixel True zoom 0.8 xpos -450
        pause 0.4
        ease 1.4 zoom 1.2 xpos -1050
    pause 1.2
    char1.talk "Let me make you sweat, too!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp") with dissolve:
        subpixel True zoom 1.2 xpos -1150
    pause 0.8
    "Mesmerized by her beautiful eyes, it takes you a moment to notice how she's squeezing her enormous tits..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat8.webp"):
        subpixel True zoom 1.2 xpos -1150
        ease 2.0 zoom 0.7 xpos -300
    pause 2.8
    "...which makes them balloon out to marvelous proportions."
    $ player.change_lust(char1.sexiness + 3)
    pl "You're so beautiful [char1.fname]!"
    char1.talk "Thank you."
    call change_char_max_affection (char1, 3) from _call_change_char_max_affection_116
    $ char1.change_affection(6)
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with dissolve:
        subpixel True zoom 0.6 xpos -200
    char1.talk "Can I kiss you [char1.playername]? *moans*"
    pause 0.4
    pl "I'd love that."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat10.webp") with fade:
        zoom 0.667
    pause 0.8
    "You get a quick look at her sensual mouth, before she's on your lap..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat11.webp") with dissolve:
        zoom 0.5
    pause 0.8
    "...pushing her wet tongue into your mouth."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat11.webp"):
        zoom 0.5
        ease 4.0 zoom 1.0 xpos -800 ypos -100
        pause 0.7
        ease 4.0 zoom 0.5 xpos 0 ypos 0
    pause 2.0
    char1.talk "Mmmm.... Mmmmmmm... *slurp*"
    pause 2.0
    char1.talk "*moans* Mmm... Aaaa..."
    $ char1.change_lust(20)
    $ player.change_lust(char1.sexiness)
    $ player.add_effect("erection")
    char1.talk "Mmmm... Mmmmmmm... *slurp*"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat12.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "What I feel pressed against my stomach..."
    char1.talk "...is that all you? *smirks"
    pause 0.4
    pl "Sorry [char1.fname]! {w}It's just... {w}I mean you're so incredibly hot!"
    char1.talk "Hush... It's really turning me on."
    $ char1.change_lust(15)
    char1.talk "Do you like my huge breasts?"
    pause 0.4
    pl "What kind of question is that? {w}I love them!"
    pl "They're incredible."
    pause 0.4
    char1.talk "Just wanted to make sure you're going to enjoy this..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat13.webp") with dissolve:
        zoom 0.5
    pause 0.7
    pl "Mmmm... Mmmmhhhh..."
    "With your head buried between her tits, it didn't take the tip of your dick long to stick from your pants..."
    "...rubbing against her tight stomach."
    char1.talk "{b}Ohhh!{/b} *whispering* You're wet with precum already..."
    pause 0.5
    pl "Mmmmmmm.... Ahhh...."
    char1.talk "Too bad we can't fuck right now with all the other girls watching..."
    pause 0.5
    char1.talk "Would you like to cum against my stomach?"
    char1.talk "Just grab my ass tighter if you'd like to do that."
    "The prospect of cumming with your head buried deeply between her mounds almost drives you over the edge."
    "Not really able to speak, you grab her ass to signal your consent."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat14a.webp") with dissolve:
        zoom 0.5
    pause 0.7
    char1.talk "Let me move a bit further down..."
    scene nightbar_hot_yvette1:
        zoom 0.5
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs" + unicode(g_hotshots.player_undress) + "_heat14b.webp"
        pause 0.5
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs" + unicode(g_hotshots.player_undress) + "_heat14c.webp"
        pause 0.5
        "scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs" + unicode(g_hotshots.player_undress) + "_heat14d.webp"
        pause 0.5
    pause 2.1
    char1.talk "Yes, that's much better... *moans*"
    $ cam1 = cl_camera("images/scenes/" + char1.fname + "/nightbar/" + char1.fname + "_nightbar_hs" + unicode(g_hotshots.player_undress) + "_heat_rub", {"face_x":0, "face_y":0, "breasts_x":1430, "breasts_y":670, "pussy_x":1470, "pussy_y":1270})
    $ ll_cameras = []
    $ ll_cameras.append(cam1)
    $ ll_sequence = [1,2,3,4,5,6,6,5,4,3,2,1]
    $ l_cum_control = {"cum_x":1430, "cum_y":900, "cum_fps":35, "cum_zoom":0.7, "cum_cam_id":0}
    $ ll_cum_talk = []
    $ ll_cum_talk.append({"who":pl, "what":"Mmmm... I'm almost there! *moans*", "pause":1.0})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Take your time and enjoy it!", "pause":1.7})
    $ ll_cum_talk.append({"who":pl, "what":"Oh my God! Yes!", "pause":1.0})
    $ ll_cum_talk.append({"who":pl, "what":"Ahhhh.... I'm cummmminnggg...", "pause":1.2})
    $ ll_cum_talk.append({"who":char1.talk, "what":"Mmmm... Yes! *moans*", "pause":0.2})
    call interactive_sex (char1, ll_cameras, ll_sequence, l_cum_control, ll_sequence, ll_cum_talk, [], 2.5) from _call_interactive_sex_2
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat_rub6.webp") with fade:
        zoom 0.8 xpos -450 ypos -200
    pause 0.8
    $ player.change_lust(-40)
    $ player.change_endurance(-30)
    char1.talk "{b}Wow{/b}! That was quite the load [char1.playername]!"
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs[g_hotshots.player_undress]_heat12.webp") with dissolve:
        zoom 0.7 xpos -300 ypos -100
    pause 0.7
    char1.talk "I didn't think I would, {w}but the way the tip of your dick was brushing against my pussy... *whispering*"
    char1.talk "I came too. *whispering*"
    $ char1.change_lust(-40)
    $ char1.change_endurance(-40)
    char1.talk "Did you enjoy it? {w}I mean I certainly did! *giggles*"
    pause 0.3
    pl "Yes, very much."
    pl "I think I'd have exploded from sheer lust if we hadn't done this."
    pause 0.4
    char1.talk "Now we don't have to go to our rooms to masturbate... *smirks*"
    pl "Ohh... We could have gone together to avoid that... *chuckles*"
    "[char1.fname] climbs from your lap..."
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0_heat9.webp") with fade:
        zoom 1.0 xpos -800
    pause 0.7
    char1.talk "Maybe next time... {w}And now I need a shower!"
    pause 0.6
    yumiko.talk "Okay girls, that was our HotShots game for tonight!"
    scene expression ("scenes/Yumiko/nightbar/Yumiko_nightbar_get_drink1.webp") with dissolve:
        zoom 0.5
    yumiko.talk "I hope everyone enjoyed it!"
    char1.talk "Ummm... Yumiko... {w}Could I have a towel?"
    pause 0.4
    yumiko.talk "Sure sweety, you can take this one!"
    "[char1.fname] cleans herself up and gets dressed..."
    pause 0.6
    scene expression ("scenes/[char1.fname]/nightbar/[char1.fname]_nightbar_hs0.webp") with fade:
        zoom 0.667
    pause 0.7
    "...while you get dressed too."
    pause 0.5
    yumiko.talk "Since our two lovebirds are dressed now, enjoy your evening everyone!"
    t_crowd_of_girls "You too Yumiko! *chorus from the girls*"
    return _return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
