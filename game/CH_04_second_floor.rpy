# ---------------------------------------------
# 室内の雨音用seを増やす
init python:
    renpy.music.register_channel(
        "ambient_se",
        mixer="ambient_se", # ミキサー設定
        loop=True
    )
default preferences.volume.ambient_se = 0.6 # デフォルト音量

# ---------------------------------------------

label CH_04_second_floor:
    window hide

    scene black
    with Dissolve(1.0)
    play ambient_se "audio/se/雨の音_2.mp3" 
    pause 1.8

    scene bg_second_floor_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "僕らはカウンター横のエレベーターへ向かう。\n"
    extend "真新しい艶のあるステンレス。\n"
    extend "山のペンションらしからぬ、都会的な光沢。\n"
    extend "操作パネルを見上げると、表示灯は――\n"
    extend "１{w=0.3}{nw}\n"
    extend "２\n"
    $ ctc_mode = "page"
    extend "しかない。\n"

    narrator_arrow "「……二階建てなのにエレベーターあるんだ」\n"
    extend "「バリアフリー対応じゃない？{w=0.3}ほら、段差もほとんどなかったし」\n"
    extend "たしかに、玄関からロビーまでほぼフラットだった。\n"
    $ ctc_mode = "page"
    extend "廊下も広めだった気がする。\n"

    show sil_second_floor_01 at sil_right, sil_fadein

    pause 0.3
    extend "[heroine['first']]がボタンを押す。\n"
    pause 0.3
    hide sil_second_floor_01
    scene black
    with fade

    play sound "audio/se/決定ボタンを押す52.mp3"
    narrator_arrow "静かな電子音。\n"
    play sound "audio/se/自動ドアが開く.mp3"
    extend "ゆっくりと扉が閉まる。\n"
    pause 0.3
    stop ambient_se
    scene bg_second_floor_02 at fullscreen_bg
    show sil_second_floor_02 at sil_center
    with fade
    play music "audio/se/車の中1.mp3"
    extend "１ {w=0.3}→{w=0.3} ２{nw}\n"
    extend "に変わる。\n"
    extend "体がふわっと浮く感覚もそこそこに、{w=0.3}{nw}"
    stop music
    play sound "audio/se/電子レンジでチン.mp3"
    extend "{w=0.3}チンと控えめな音。\n"
    extend "「早っ」\n"
    extend "[heroine['first']]がつぶやき、笑う。\n"
    extend "「階段でも変わらないかもな」\n"
    play sound "audio/se/自動ドアが開く.mp3"
    $ ctc_mode = "page"
    extend "答える間もなく扉が開く。\n"

    hide sil_second_floor_02
    scene black
    with fade
    pause 0.3

    scene bg_second_floor_03 at fullscreen_bg
    with fade
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    play ambient_se "audio/se/雨の音_2.mp3"

    narrator_arrow "目の前には、まっすぐ伸びる廊下。\n"
    extend "天井は高く、間接照明がやわらかく壁を照らしている。\n"
    extend "昼間でも照明は灯っているのか、{w=0.3}今日のような雨の日でも明るい。\n"
    extend "ここも床が落ち着いた木目調。\n"
    extend "スリッパをはいた足音が、パタ、パタ、と軽く響く。\n"
    $ ctc_mode = "page"
    extend "……これは夜中に歩いたら迷惑かもしれないな。\n"

    scene bg_second_floor_04 at fullscreen_bg
    with fade
    narrator_arrow "エレベーター向かいのすぐ左の部屋に、203 のプレートがあった。\n"
    extend "「近っ」\n"
    extend "また短く[heroine['first']]がつぶやき、笑う。\n"
    extend "その隣に、204。\n"
    extend "さらに先に、205、{w=0.3}206。\n"
    extend "僕は何気なく、その先を見る。\n"
    scene bg_second_floor_05 at fullscreen_bg
    with dissolve
    $ ctc_mode = "page"
    extend "通路の途中で、廊下の片側がすっと開けていた。\n"

    narrator_arrow "「ねえ見て、{w=0.3}吹き抜けになってる！」\n"
    extend "[heroine['first']]が小走りで先に進むと、手すり越しに下を覗きだした。\n"
    extend "確かに2階の通路は、途中から回廊のようになっており、中央が大きく空いている。\n"
    extend "「おお、ロビーかな？」\n"
    $ ctc_mode = "page"
    extend "僕も[heroine['first']]に追いつくと一緒になって覗き込んだ\n"

    scene bg_second_floor_06 at fullscreen_bg
    with fade
    narrator_arrow "上から見下ろすロビーは、まるで舞台セットみたいだ。\n"
    extend "一段奥まった場所にゆったりとしたソファがいくつか配置され、{w=0.3}低いテーブルが中央に置かれている。\n"
    extend "木の梁が組まれた天井。\n"
    extend "壁にはさりげなく間接照明が仕込まれていて、全体がやわらかく包まれている。\n"
    extend "ここも館内BGMと雨音がわずかに聞こえるのみで、人の気配はない。\n"
    extend "吹き抜けの端に、木製の階段が伸びているのが見えた。\n"
    $ ctc_mode = "page"
    extend "ロビーへは直接降りられるらしい。\n"

    pause 0.4 
    show sil_bg_second_floor_01 at sil_center, sil_fadein

    narrator_arrow "「これ、{w=0.3}いい」\n"
    extend "[heroine['first']]の声色が変わる。\n"
    extend "「真下に被写体置いて、{w=0.3}上から俯瞰とか、{w=0.3}最高じゃない？」\n"
    show sil_bg_second_floor_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_second_floor_01
    pause 0.4 
    show sil_bg_second_floor_02 at sil_center, sil_fadein
    extend "「いいね、それ」"
    extend "と、すかさず僕も同意する。\n"
    extend "[heroine['first']]がスマホを構える。\n"
    $ ctc_mode = "page"
    extend "「ロケハン開始、{w=0.3}って感じね」\n"

    menu:
        "１　「そうだな、よし、このままロケハンだ！」":
            $ choice_comment = ""
            $ flag_lobby_direct = True # ロビーに直接行ったフラグ（詳細は CH_00_flag.rpy）
            narrator_arrow "「いいね、それ。このまま行こう！ロケハン開始！」\n"
            show sil_bg_second_floor_02 at sil_center, sil_fadeout
            pause 0.4
            hide sil_bg_second_floor_02
            pause 0.4 
            show sil_bg_second_floor_03 at sil_center, sil_fadein
            extend "「OK！決まりだね。」\n"
            $ ctc_mode = "page"
            extend "[heroine['first']]がわざとらしく敬礼する。\n"
            pause 0.4
            show sil_bg_second_floor_03 at sil_center, sil_fadeout
            pause 0.4
            hide sil_bg_second_floor_03
            pause 0.4
            scene black

            jump CH_06_To_the_lobby

        "２　「まず荷物置こうよ。」僕は軽く制止する。":
            $ choice_comment = ""

            narrator_arrow "僕は軽く制止する。\n"
            extend "「まあ、{w=0.3}まず荷物置こうよ。"
            extend "撮影はそのあとで」\n"
            show sil_bg_second_floor_02 at sil_center, sil_fadeout
            pause 0.4
            hide sil_bg_second_floor_02
            pause 0.4 
            show sil_bg_second_floor_03 at sil_center, sil_fadein
            extend "「了解」\n"
            $ ctc_mode = "page"
            extend "[heroine['first']]がわざとらしく敬礼する。\n"
            pause 0.4
            show sil_bg_second_floor_03 at sil_center, sil_fadeout
            pause 0.4
            hide sil_bg_second_floor_03
            pause 0.4
            scene black

            jump CH_05_guest_room