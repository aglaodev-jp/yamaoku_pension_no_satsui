label CH_06_To_the_lobby:
    window hide


    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    play ambient_se "audio/se/雨の音_2.mp3" 
    pause 1.8

    scene bg_to_the_lobby_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    # ==== フラグ分岐 ====================================================
    # 詳細は CH_00_flag.rpy

    if flag_lobby_direct: # 直接ロビーにいった場合
        narrator_arrow "僕たちは、吹き抜けの階段からロビーへと降りた。\n"
        extend "ここからだと、二階から見下ろしていたときより天井の高さがよくわかる。\n"
    else:    # 部屋に立ち寄った場合
        narrator_arrow "僕たちは部屋を出ると、先ほどの吹き抜けからロビーへ向かった\n"
        extend "階段を降りると、二階から見下ろしていたときより天井の高さがよくわかる。\n"
        
    # ====================================================================
    
    extend "そこまで広いロビーではないが、{w=0.3}吹き抜けの天井の高さもあって開放感があった。\n"
    extend "木の温もりが広がる落ち着いた空間。\n"
    extend "山奥のペンションらしく、{w=0.3}りっぱな石造りの暖炉が据えられている。\n"
    $ ctc_mode = "page"
    extend "……と、{w=0.3}思ったのだが。\n"

    scene bg_to_the_lobby_02 at fullscreen_bg
    with fade

    narrator_arrow "近づいてよく見ると、この暖炉――\n"
    extend "本物じゃない。{w=0.3}イミテーションだ。\n"
    extend "奥は黒く、モニターのような構造になっている。\n"
    $ ctc_mode = "page"
    extend "冬になると、暖炉の火の映像でも流すのだろうか。\n"

    show bg movie_loop_5 at fullscreen_bg 
    with fade
    narrator_arrow "ロビーの壁にも、モニターが一枚掛かっている。\n"
    extend "一瞬テレビかと思ったが、画面には文字やアイコンが並んでいる。\n"
    extend "これって確か……。\n"
    extend "「……デジタルサイネージってやつかな」\n"
    extend "「広告とか出すやつ？」\n"
    extend "「たぶん」\n"
    extend "ちょうど画面には、周辺の天気予報が表示されていた。\n"
    extend "こんなに雨が降っているのに、明日は晴れの予報だ。\n"
    $ ctc_mode = "page"
    extend "明日であれば、すこし外の撮影ができるかもしれない。\n"
    scene black
    with fade
    scene bg_to_the_lobby_03 at fullscreen_bg
    with fade

    narrator_arrow "丸いテーブルがいくつも並び、椅子がきちんと整えられている。\n"
    extend "使わない椅子やテーブルが壁際にいくつか避けて置かれている。\n"
    $ ctc_mode = "page"
    extend "シーズン中は、きっとここも人でいっぱいになるのだろう。\n"

    scene bg_to_the_lobby_04 at fullscreen_bg
    with fade

    narrator_arrow "壁一面の大きなガラス窓の向こうは、ウッドデッキがある。\n"
    extend "丸いテーブルと椅子がいくつか並んでいるが、どれも雨に濡れている。\n"
    extend "本来なら外でコーヒーでも飲めそうな場所だが、今はちょっと無理そうだ。\n"
    $ ctc_mode = "page"
    extend "その先は、さっきまで僕等がいた雨の森林が広がっていた。\n"

    scene black
    with fade
    narrator_arrow "とてもおしゃれで落ち着いたロビー。\n"
    extend "――なのに。\n"
    extend "人の気配は、{w=0.3}どこにもない。\n"
    extend "外ではまだ雨が降り続いている。\n"
    $ ctc_mode = "page"
    extend "ロビーに微かに響く雨音と、{w=0.3}その音に混ざる館内BGMのループが物悲しい。\n"

    scene bg_to_the_lobby_01 at fullscreen_bg
    with fade
    pause 0.4
    show sil_bg_to_the_lobby_01 at sil_center, sil_fadein
    narrator_arrow "「……ねえ」\n"
    extend "[heroine['first']]が小声で言う。\n"
    extend "「薄々感じていたんだけど…{w=0.3}今日の宿泊客、{w=0.3}私たちだけ？」\n"
    extend "僕は苦笑する。\n"
    extend "「オフシーズンだし、あり得なくはないね。"
    $ ctc_mode = "page"
    extend "まあ、誰もいないほうが撮影しやすいし、好都合じゃないか？」\n"

    show sil_bg_to_the_lobby_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_to_the_lobby_01
    pause 0.4

    scene bg_to_the_lobby_05 at fullscreen_bg
    with fade
    pause 0.4
    show sil_bg_to_the_lobby_02 at sil_center, sil_fadein

    narrator_arrow "僕は中央の丸テーブルの椅子に座った。\n"
    extend "「さて、どう撮るか決めないと」\n"
    extend "[heroine['first']]も向かいに腰掛け、頬杖をつく。\n"
    extend "「どんなシーンから撮る？」\n"
    $ ctc_mode = "page"
    extend "このペンションは、絵になる場所が多そうだ。\n"

    $ choice_comment = "「どうするか……」"

    menu:
        "１　ペンションを探検しながら撮影しよう":
            $ choice_comment = ""
            jump CH_07a_Start_filming

        "２　ここは木下さんに相談だ":
            $ choice_comment = ""
            jump CH_07b_Start_filming

        "３　……今日はもう休まない？":
            $ choice_comment = ""
            jump CH_07c_Start_filming