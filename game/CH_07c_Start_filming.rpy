label CH_07c_Start_filming:

    window hide

    scene bg_to_the_lobby_05 at fullscreen_bg
    with fade
    pause 0.4
    show sil_c_start_filming_01 at sil_center, sil_fadein

    narrator_arrow "僕は少し考えてから言った。\n"
    extend "「――もう撮影は終わりにしよう」\n"
    extend "[heroine['first']]が一瞬、固まる。\n"
    $ ctc_mode = "page"
    extend "「ほんとにやめるの？」\n"

    $ choice_comment = "僕は言った。"

    menu:
        "１　いや、やっぱり撮ろう":
            $ choice_comment = ""
            jump CH_07c_choice_1

        "２　本当に今日はやめよう":
            $ choice_comment = ""
            jump CH_07c_choice_2

label CH_07c_choice_1:
    pause 0.4
    narrator_arrow "「……いや、やっぱり撮ろう」\n"
    extend "「でしょ？{w=0.3}じゃあ、撮影作戦会議」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]も頷く。\n"

    $ choice_comment = "じゃあ……"

    menu:
        "１　ペンションを探検しながら撮影しよう":
            $ choice_comment = ""
            jump CH_07a_Start_filming

        "２　ここは木下さんに相談だ":
            $ choice_comment = ""
            jump CH_07b_Start_filming


label CH_07c_choice_2:
    pause 0.4

    stop music fadeout 1.5

    narrator_arrow "「……やっぱりやめよう。"
    extend "今日は天候も悪いし、{w=0.3}これ以上撮影してもいい絵は取れない気がするんだよね」\n"
    extend "本当は、もう少し粘りたかったけど、この天気じゃどうにもならない。\n"
    extend "[heroine['first']]は、小さく息をついてから顔を上げた。\n"
    extend "「そうね、{w=0.3}どうせ明日もあるし、{w=0.3}やめよっか。\n"
    extend "無理しても仕方ないしね」\n"
    $ ctc_mode = "page"
    extend "少し残念そうだが、[heroine['first']]は同意してくれた。\n"

    narrator_arrow "「……ごめん。{w=0.5}せっかく来たのに、ちゃんと撮れなくて」\n"
    extend "僕がそう言うと、[heroine['first']]は軽く首を振る。\n"
    extend "「ううん。{w=0.5}今日は下見ってことでいいじゃん"
    extend "……それに、今日は移動も長かったし。"
    $ ctc_mode = "page"
    extend "[player['first']]君に無理させたくないよ、{w=0.3}なんか顔色悪いよ」\n"

    narrator_arrow "「……そうだね。{w=0.5}ありがとう。」\n"
    extend "助かった、{w=0.3}って思っている自分もいる。\n"
    extend "実はかなり疲れていたんだ。\n"
    extend "昨夜は遅くまで木下さんとロケハンの打ち合わせ。\n"
    extend "そして今朝は、兄の家まで車を借りに行くのに早起きして。\n"
    extend "そこから途中で[heroine['first']]を乗せ、{w=0.3}慣れない運転でこのペンションまでやってきたのだ。\n"
    extend "……僕は、{w=0.5}思った以上にこたえていた。\n"
    extend "「今日は、{w=0.3}早めに休もうかな」\n"
    extend "僕がそう言うと、[heroine['first']]は{w=0.3}「うんうん！」と何度もうなずく。\n"
    $ ctc_mode = "page"
    extend "階段へ向かう足取りは、{w=0.3}少しだけ軽くなっていた。\n"

    show sil_c_start_filming_01 at sil_center, sil_fadeout
    hide sil_c_start_filming_01
    scene black
    with fade
    pause 1.0

    scene bg_c_start_filming_01 at fullscreen_bg
    with fade
    pause 0.3
    show sil_c_start_filming_02 at sil_center, sil_fadein

    narrator_arrow "しばらく部屋でまったりしたあと、{w=0.3}ふと時計を見ると思っていたより時間が過ぎていた。\n"
    extend "「……そろそろ、{w=0.3}ご飯どうする？」\n"
    extend "[heroine['first']]がベッドの上で体を起こす。\n"
    extend "「そういえば、{w=0.3}何も決めてなかったな」\n"
    $ ctc_mode = "page"
    extend "スマホを確認すると、{w=0.3}木下さんからメッセージが届いていた。\n"
    pause 0.3
    show sil_c_start_filming_02 at sil_center, sil_fadeout
    pause 0.3
    hide sil_c_start_filming_02
    scene black
    with fade

    scene bg_sumaho_01 at fullscreen_bg
    with fade

    narrator_arrow "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「おつかれ～写真は十分だから心配すんな」\n"
    extend "{nw}\n"
    narrator_arrow "**木下：**{nw}\n"
    extend "「そういえばさ、今回素泊まりだよね？」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「夕飯困ると思って、山のふもとのレストラン、予約しといたよ」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「地図送っとく」\n"

    scene black
    with fade

    scene bg_c_start_filming_01 at fullscreen_bg
    with fade
    pause 0.3
    show sil_c_start_filming_02 at sil_center, sil_fadein

    narrator_arrow "「……段取りいいな」\n"
    extend "こういうところだけは本当に感心する。\n"
    extend "「ね、{w=0.3}ちょうどよかった」\n"
    extend "[heroine['first']]が肩を揺らして笑う。\n"
    $ ctc_mode = "page"
    extend "僕たちは軽く支度を整えて、{w=0.3}山のふもとにあるレストランへ向かうことにした。\n"

    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    show sil_c_start_filming_02 at sil_center, sil_fadeout
    hide sil_c_start_filming_02
    scene black
    with fade

    jump CH_08_restaurant_scene
