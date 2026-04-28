label CH_09_return_to_room:
    window hide

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_return_to_room_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.5

    play ambient_se "audio/se/雨の音_2.mp3"
    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.3
    play sound "audio/se/車のドアを閉める.mp3"
    play sound "audio/se/車のエンジンをかける2.mp3"
    play music "audio/se/車の中1.mp3"
    narrator_arrow "食事を終え、店を出るころには、すっかり真っ暗になっていた。\n"
    extend "山の空気は昼より少し冷たく、森の匂いが濃くなっている。\n"
    $ ctc_mode = "page"
    extend "車に乗り込み、来た道をそのまま戻る。\n"
    stop music
    scene black
    with fade
    pause 1.0

    play sound "audio/se/入店するときのベル.mp3"
    pause 0.5
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5

    scene bg_return_to_room_02 at fullscreen_bg
    with fade

    narrator_arrow "ペンションに到着。\n"
    extend "扉を開けると、{w=0.3}当然ながらさっきとまったく同じ。\n"
    extend "誰もいない空間に不釣り合いな明るい照明。\n"
    extend "どこからか小さく流れている館内BGM。\n"
    extend "なんだろう、{w=0.3}相変わらず、{w=0.3}寂しい。\n"
    extend "「……なんか、{w=0.3}やっぱり静かだね」\n"
    extend "[heroine['first']]も同じことを感じたのか、あたりを見回して言う。\n"
    $ ctc_mode = "page"
    extend "そのままエレベーターで２階へ。\n"

    scene black
    with fade

    stop music fadeout 1.5

    # ==== フラグ分岐 ====================================================

    # 部屋に行かない→ロビーで撮影した場合
    if flag_lobby_direct and flag_lobby_photo_taken:

        scene bg_second_floor_04 at fullscreen_bg
        with fade
        pause 0.4 
        show sil_bg_guest_room_01 at sil_left, sil_fadein # 左寄せ
        narrator_arrow "考えてみれば、僕たちはチェックインのあと客室に寄らずに動き回っていた。\n"
        $ ctc_mode = "page"
        extend "部屋に戻るというより、ようやく落ち着く場所へ向かう、という感じだった。\n"

        play sound "audio/se/鍵を開ける1.mp3"
        pause 0.4 
        scene black
        with fade
        play sound "audio/se/ドアを開ける1.mp3"
        pause 0.3
        play sound "audio/se/ドアを閉める1.mp3"
        pause 0.8
        scene bg_return_to_room_03 at fullscreen_bg
        with fade

        narrator_arrow "正面に並ぶツインベッド。\n"
        extend "生成りのリネンに、落ち着いた色のクッション。\n"
        extend "木製のヘッドボードと腰壁。\n"
        extend "白い壁には間接照明が灯り、安心感のある柔らかな雰囲気だ。\n"
        extend "ただ、今の僕はその雰囲気をじっくり味わう余裕はあまりなかった。\n"
        extend "食事をしてまた雨の中を戻ってきたせいか部屋に入った途端、どっと疲れが出る。\n"
        extend "静かな客室に、雨音だけが流れている。\n"
        extend "[heroine['first']]がベッドに腰を下ろす。\n"
        pause 0.4 
        show sil_return_to_room_01 at sil_center, sil_fadein
        pause 0.4 
        $ ctc_mode = "page"
        extend "「はぁ……{w=0.3}今日は、思ったより疲れたね」\n"

        show sil_return_to_room_01 at sil_center, sil_fadeout
        pause 0.4
        hide sil_return_to_room_01
        
        scene black
        with fade
        narrator_arrow "僕は、ふと時間を確認する。\n"


    # 部屋に行く→ロビーで撮影した場合

    elif flag_lobby_photo_taken:

        scene bg_return_to_room_03 at fullscreen_bg
        with fade

        narrator_arrow "もちろん客室も、出たときのままだ。\n"
        extend "静かな客室に、雨音だけが流れている。\n"
        extend "[heroine['first']]がベッドに腰を下ろす。\n"
        pause 0.4 
        show sil_return_to_room_01 at sil_center, sil_fadein
        pause 0.4 

        extend "「はぁ……{w=0.3}今日はいっぱい撮ったね」\n"
        $ ctc_mode = "page"
        extend "そう言いながら、スマホを取り出して撮影したデータを確認している。\n"

        narrator_arrow "「とりあえず、残りの写真も木下さんに送っとこ」\n"
        extend "[heroine['first']]は指を動かしながら言う。\n"
        extend "[heroine['first']]はくすっと笑う。\n"
        extend "「あ、{w=0.3}木下さん怒ってる」\n"
        extend "「何を？」\n"

        show sil_return_to_room_01 at sil_center, sil_fadeout
        pause 0.4
        hide sil_return_to_room_01

        scene bg_sumaho_01 at fullscreen_bg
        show shade onlayer master    
        with fade

        extend "「“キミたち、{w=0.3}イチャイチャしてないでちゃんと撮りなさいよ！”って」\n"
        extend "[heroine['first']]が木下さんの真似をする。\n"
        extend "「あー{w=0.3}……ははっ」\n"
        $ ctc_mode = "page"
        extend "思わず僕は笑ってしまう。\n"

        scene black
        with fade

        narrator_arrow "そのとき、スマホの時計が目に入る。\n"
        
    # 部屋に行く→ロビーで撮影しなかった場合（それ以外）
    else:

        scene bg_return_to_room_03 at fullscreen_bg
        with fade

        narrator_arrow "もちろん客室も、出たときのままだ。\n"
        extend "静かな客室に、雨音だけが流れている。\n"
        extend "[heroine['first']]がベッドに腰を下ろす。\n"
        pause 0.4 
        show sil_return_to_room_01 at sil_center, sil_fadein
        pause 0.4 
        $ ctc_mode = "page"
        extend "「はぁ……{w=0.3}今日は、思ったより疲れたね」\n"

        show sil_return_to_room_01 at sil_center, sil_fadeout
        pause 0.4
        hide sil_return_to_room_01

        scene black
        with fade

        narrator_arrow "僕は、ふと時間を確認する。\n"


    # ====================================================================



    extend "**19:55**\n"
    extend "「そういえば、お風呂20時からだったっけ」\n"
    extend "[heroine['first']]が顔を上げる。\n"
    scene bg_return_to_room_03 at fullscreen_bg
    with fade
    pause 0.4 
    show sil_return_to_room_02 at sil_center, sil_fadein
    pause 0.4 
    extend "「あ、{w=0.3}ほんと時間だ。{w=0.3}お先にどうぞ」\n"
    extend "[heroine['first']]は軽く手を振る。\n"

    # ==== フラグ分岐 ====================================================
    # ロビーで撮影していた場合
    if flag_lobby_photo_taken:
        extend "「その間にデータ整理しとくからね」\n"
    # それ以外
    else:
        extend "「その間に、明日撮るところでもメモしておくね」\n"
    $ ctc_mode = "page"
    extend "「了解」\n"

    # ====================================================================
    show sil_return_to_room_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_return_to_room_02

    pause 0.4
    scene black
    with dissolve

    # ルートチェック１
    jump route_check_1

# ===== ルートチェック ============================================

label route_check_1:
    # 人影を見ている and ロビーで木下に相談（木下ルート）
    if flag_seen_shadow and flag_lobby_kino:
        $ route_kino = True
        jump CH_10_public_bath_kinoshita
    # それ以外（サモエドルート）
    else:
        $ route_samoyed = True
        jump CH_10_public_bath_samoyed