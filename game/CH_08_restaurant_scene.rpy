label CH_08_restaurant_scene:

    pause 0.8
    scene black
    with fade
    $ renpy.movie_cutscene("movies/movie_07.webm") 
    scene car_window_forest at fullscreen_bg

    window hide

    scene bg_restaurant_scene_01 at fullscreen_bg
    with fade
    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.0
    narrator_arrow "ペンションから車で山道を下る。\n"
    extend "しばらく走ると、さっき通ってきた道とは違う、よく整備された広い道路に出た。\n"
    extend "舗装もきれいで、カーブもゆるい。\n"
    extend "山の県道のような走りやすい道だ。\n"
    extend "どうやらこちらが、ふもとの町へ続くメインルートらしい。\n"
    extend "——こっちから来ればよかったな。\n"
    $ ctc_mode = "page"
    extend "そんなことを思いながら車を走らせていると、やがて森の中に温かい灯りが見えてきた。\n"

    scene black
    with fade
    show bg movie_loop_6 at fullscreen_bg # ループ動画
    with fade

    narrator_arrow "小さなログハウス風の建物。\n"
    extend "入り口のランプに照らされた木の看板には{w=0.5}{nw}\n"
    extend "\n{nw}"
    extend "「山小屋レストラン　森の灯」{nw}\n"
    extend "\n"
    extend "と書かれている。\n"
    extend "思いつきで考えたような名前だが、ちょうど暗くなってきた森には妙に似合っていると思った。\n"
    $ ctc_mode = "page"
    extend "普段の木下さんは適当な感じの人だけど、要所でセンスを感じるのはさすが映研会代表といったところか。\n"

    pause 0.4
    scene black
    with dissolve
    play sound "audio/se/ドアを開ける1.mp3"
    pause 0.4
    stop ambient_se
    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.0
    play music "audio/bgm/Secret_Talk.mp3" fadein 1.5
    scene bg_restaurant_scene_02 at fullscreen_bg
    with fade
    narrator_arrow "扉を開けると、木の匂いと料理の香りが広がった。\n"
    extend "店内は落ち着いた山小屋風の内装。\n"
    extend "客は僕たちのほかに一組だけだった。\n"
    pause 0.3 
    show sil_restaurant_scene_01 at sil_center, sil_fadein 
    extend "カウンターの奥から、白髪まじりのマスターが{w=0.3}{nw}\n"
    extend "「いらっしゃい」{nw}\n"
    $ ctc_mode = "page"
    extend "{w=0.3}と顔を出した。\n"


    narrator_arrow "「えっと……予約です。{w=0.5}木下の名前で」\n"
    show sil_restaurant_scene_01 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_01
    show sil_restaurant_scene_02 at sil_center, sil_fadein 
    extend "僕がそう言うとマスターは帳面を確認して頷く。\n"
    extend "「ああ、聞いてるよ。二人だね」\n"
    show sil_restaurant_scene_02 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_02
    show sil_restaurant_scene_03 at sil_center, sil_fadein 
    $ ctc_mode = "page"
    extend "僕たちは窓際のテーブルに案内された。\n"

    pause 0.3 
    show sil_restaurant_scene_03 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_03
    scene bg_restaurant_scene_03 at fullscreen_bg
    with fade
    show sil_restaurant_scene_04 at sil_center, sil_fadein 

    narrator_arrow "水を置きながら、マスターが何気なく聞く。\n"
    extend "「この時間にお客さんは珍しくてね。{w=0.3}観光かい？」\n"
    extend "[heroine['first']]が首を振る。\n"
    extend "「大学の映画サークルで、ちょっと撮影の下見に」\n"
    $ ctc_mode = "page"
    extend "「上のペンションに泊まってるんです」\n"

    pause 0.3 
    show sil_restaurant_scene_04 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_04
    with fade
    show sil_restaurant_scene_05 at sil_center, sil_fadein 

    narrator_arrow "マスターは少し眉を上げた。\n"
    extend "「ペンション？」\n"
    extend "「はい」\n"
    extend "僕が言う。\n"
    extend "「最近オープンしたって聞きました」\n"
    extend "マスターは小さく笑った。\n"
    $ ctc_mode = "page"
    extend "「ああ……改装して、また始めたのか」\n"

    narrator_arrow "[heroine['first']]が聞く。\n"
    extend "「また、って？」\n"
    extend "マスターは少し考えてから言った。\n"
    extend "「前にもペンションだったんだよ。{w=0.3}でも、ずっと閉まっててね」\n"
    extend "「へえ」\n"
    extend "ペンションをリノベーションしたことは知っていたが、{w=0.3}ずっと閉まっていたというのは初耳だ。\n"
    extend "僕は興味を持った。\n"
    $ ctc_mode = "page"
    extend "「どうして閉まってたんですか？」\n"

    stop music fadeout 2.0

    pause 0.3 
    show sil_restaurant_scene_05 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_05
    scene bg_restaurant_scene_05 at fullscreen_bg
    with fade
    show sil_restaurant_scene_06 at sil_center, sil_fadein 

    narrator_arrow "マスターは少し声を落とす。\n"
    extend "「……実はあのペンション、{w=0.3}妙な噂があってな」\n"
    extend "「噂？」\n"
    extend "[heroine['first']]がすこし不安そうに身をすくめる。\n"
    extend "マスターはそれを見て苦笑した。\n"
    extend "「まあ、どこにでもある話だよ」\n"
    $ ctc_mode = "page"
    extend "そして、さらっと言った。\n"

    stop music
    stop ambient_se
    scene black
    play sound "audio/se/チリン.mp3"
    narrator_arrow "「──幽霊が出るってやつだ」\n"

    pause 0.3 
    show sil_restaurant_scene_06 at sil_center, sil_fadeout 
    hide sil_restaurant_scene_06
    scene bg_restaurant_scene_06 at fullscreen_bg
    with fade

    play music "audio/bgm/潜む怪奇.mp3" fadein 1.5

    narrator_arrow "僕と[heroine['first']]は思わず顔を見合わせた。\n"
    extend "「幽霊？」\n"
    extend "マスターは窓の外の暗い森をちらりと見る。\n"
    extend "「昔、宿泊客がよく言ってたんだ。{w=0.3}”夜中にペンションの周りを白い人影が歩いてる”ってな。"
    $ ctc_mode = "page"
    extend "近づくと毎回森の方に消えるらしい」\n"

    pause 0.3 
    scene bg_restaurant_scene_07 at fullscreen_bg
    with fade
    show sil_restaurant_scene_08 at sil_center, sil_fadein 

    narrator_arrow "「え……」\n"
    extend "[heroine['first']]が小さく声を上げる。\n"
    extend "「それ、本当に……？」\n"
    extend "マスターは笑った。\n"
    extend "「まあ、見間違いだろ。{w=0.3}夜の森は、いろんなものが人の形に見えるもんだし」\n"
    extend "それから軽く手を振る。\n"
    $ ctc_mode = "page"
    extend "「今は新しくオープンしてるんだろ？{w=0.3}問題ないってことさ」\n"

    scene black
    with fade
    narrator_arrow "そう言って厨房の方へ戻っていった。\n"
    stop music fadeout 1.5
    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.0
    scene bg_restaurant_scene_03 at fullscreen_bg
    with fade
    show sil_restaurant_scene_09 at sil_center, sil_fadein

    # ==== フラグ分岐 ====================================================
    # 詳細は CH_00_flag.rpy

    if flag_seen_shadow: # 人影を見た場合

        narrator_arrow "「ねえさっき、部屋の窓から見た人影って……{w=0.3}幽霊！？」\n"
        extend "僕は肩をすくめる。\n"
        extend "「ああ、{w=0.3}森の方にいたってやつ？{w=0.3}まさか！」\n"
        extend "「でも……」\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]は納得していない顔で窓の外を見る。\n"

    else:
        narrator_arrow "「……白い幽霊」\n"
        extend "[heroine['first']]は、そうつぶやくと少し不安そうに僕を見る。\n"
        extend "「ねえ、{w=0.3}あのペンション……{w=0.3}本当に大丈夫かな」\n"
        $ ctc_mode = "page"
        extend "その問いに僕は肩をすくめる。\n"

    # ====================================================================

    $ choice_comment = "僕は……"

    menu:
        "１　「それ、ちょっと面白そうだな」と答えた。":
            $ flag_react_ghost = "interest"
        "２　「いや、普通に怖いんだけど」と身震いした。":
            $ flag_react_ghost = "fear"
        "３　「まあ、よくある話でしょ」と受け流した。":
            $ flag_react_ghost = "calm"


    # --- 分岐会話 ----------------------------------------------------

    if flag_react_ghost == "interest":

        narrator_arrow "「それ、{w=0.3}ちょっと面白そうだな」\n"
        extend "思わずそんなことを口にしてしまう。\n"
        extend "[heroine['first']]がぎょっとした顔でこちらを見る。\n"
        extend "「面白そうって……{w=0.3}ちょっと！」\n"
        extend "「いや、{w=0.3}ほら。{w=0.5}雰囲気はあるなって」\n"
        $ ctc_mode = "page"
        extend "「そういう問題じゃないでしょ……」\n"

        narrator_arrow "「こりゃホラー映画のほうがよかったかな？」\n"
        extend "「それ、シャレにならないよ！」\n"
        extend "[heroine['first']]は本気でおびえている。\n"
        $ ctc_mode = "page"
        extend "少し怒らせてしまったようだ。\n"


    elif flag_react_ghost == "fear":

        narrator_arrow "「いや、{w=0.5}普通に怖いんだけど」\n"
        extend "思わず本音が出る。\n"
        extend "[heroine['first']]が少し安心したように肩の力を抜いた。\n"
        extend "「だよね……{w=0.3}ちょっとびっくりした」\n"
        extend "「夜にその話は反則だろ……」\n"
        extend "二人で小さく笑い合う。\n"
        $ ctc_mode = "page"
        extend "……とはいえ、{w=0.3}幽霊なんて話を聞いてしまうと、さすがに少し気になる。\n"


    elif flag_react_ghost == "calm":

        narrator_arrow "「まあ、{w=0.3}よくある話でしょ」\n"
        extend "できるだけ軽く受け流す。\n"
        extend "[heroine['first']]がじっとこちらを見る。\n"
        extend "「……強がってない？」\n"
        extend "図星だった。\n"
        extend "「いやいや、{w=0.3}こういうのは大体見間違いだって」\n"
        extend "僕はなるべく平然とした調子で言う。\n"
        $ ctc_mode = "page"
        extend "けれど、幽霊なんて言葉を聞いたあとでは、動揺を隠せていなかったようだ。\n"

    stop ambient_se
    pause 1.0

    show bg movie_loop_7 at fullscreen_bg # ループ動画の背景はshowで表示。sceneだとなぜかできない。
    with Fade(1.5, 0.3, 2.0)

    play music "audio/se/目玉焼きを焼く.mp3" fadein 1.5

    narrator_arrow "しばらくして、マスターが料理を運んでくる。\n"
    extend "「お待たせ」\n"
    extend "厨房の奥からいい匂いが漂ってきた。\n"
    extend "木のプレートに盛られた料理から、湯気がふわりと立ち上っている。\n"
    extend "ハンバーグに、{w=0.3}焼き野菜。\n"
    $ ctc_mode = "page"
    extend "横にはバターの香りがするライス。\n"


    narrator_arrow "[heroine['first']]の表情がぱっと明るくなる。\n"
    extend "「わあ……{w=0.3}おいしそう」\n"
    extend "料理を目の前にして、幽霊への恐怖心はどこかへ吹き飛んだようだ。\n"
    extend "「いただきます」\n"
    extend "一口食べて、[heroine['first']]が目を丸くする。\n"
    extend "「おいしい！」\n"
    extend "「ほんとだ」\n"
    extend "ハンバーグのシンプルなワンプレート。"
    $ ctc_mode = "page"
    extend "だけど肉の旨みがしっかり閉じ込められていて、{w=0.3}焼き加減も絶妙。\n"


    stop music fadeout 1.5
    pause 0.4
    scene black
    with dissolve

    narrator_arrow "しばらくのあいだ、二人とも夢中で食べ続ける。\n"
    $ ctc_mode = "page"
    extend "──気づけば、幽霊の話題はすっかり消えていた。\n"

    jump CH_09_return_to_room



































