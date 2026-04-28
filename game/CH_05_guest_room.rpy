label CH_05_guest_room:
    window hide

    scene bg_second_floor_04 at fullscreen_bg
    with fade
    narrator_arrow "203号室の前で、僕はカードキーをかざす。\n"
    pause 0.4 
    show sil_bg_guest_room_01 at sil_left, sil_fadein # 左寄せ
    play sound "audio/se/鍵を開ける1.mp3"
    pause 0.4 
    extend "カチ、と軽い音。\n"
    extend "「開いた」\n"
    scene black
    with fade
    $ ctc_mode = "page"
    extend "[heroine['first']]がすかさずドアを開ける。\n"
    play sound "audio/se/ドアを開ける1.mp3"
    play sound "audio/se/ドアを閉める1.mp3"
    pause 0.3

    scene bg_guest_room_01 at fullscreen_bg
    with fade
    narrator_arrow "「おお」\n"
    extend "正面に並ぶツインベッド。\n"
    extend "生成りのリネンに、落ち着いた色のクッション。\n"
    extend "木製のヘッドボードと腰壁。\n"
    extend "白い壁には間接照明が灯り、安心感のある柔らかな雰囲気だ。\n"
    extend "「いいじゃん、思ったより全然いい！」\n"
    extend "[heroine['first']]が窓の方へ駆け寄り、カーテンを少し開ける。\n"
    extend "「見て、ほら、すぐ山。"
    extend "ちゃんとペンションって感じする！」\n"
    $ ctc_mode = "page"
    extend "そこまで広いわけではないが、確かにしっかりとした作りだ。\n"

    $ choice_comment = "僕は……"

    menu:
        "１　ここで[heroine['first']]と一緒に一夜を過ごすのかとドギマギした。":
            $ choice_comment = ""
            jump CH_05_guest_room_c_1

        "２　「ベッドどっちにする？僕、窓際がいい！」一緒になってはしゃいだ。":
            $ choice_comment = ""
            jump CH_05_guest_room_c_2

        "３　部屋をひと通り見渡して、ロケハンの現実に引き戻された。":
            $ choice_comment = ""
            jump CH_05_guest_room_c_3

label CH_05_guest_room_c_1:
    window hide

    narrator_arrow "ベッドが、{w=0.3}ふたつ。\n"
    extend "当たり前だけど、{w=0.3}ふたつ。\n"
    extend "生成りのリネンがやけに整って見える。\n"
    extend "枕の距離が、{w=0.3}妙に近く感じる。\n"
    extend "ここで一晩。\n"
    extend "隣に[heroine['first']]がいて。\n"
    extend "合宿だ、{w=0.3}ロケハンだ、{w=0.3}と頭では分かっているのに、{w=0.3}妙な緊張が胸の奥をくすぐった。\n"
    $ ctc_mode = "page"
    extend "落ち着け、{w=0.3}と自分に言い聞かせる。\n"

    pause 0.4 
    show sil_bg_guest_room_02 at sil_center, sil_fadein
    pause 0.4 

    narrator_arrow "視線の置き場に困っていると、[heroine['first']]がベッドにぽすんと腰を下ろした。\n"
    extend "「ふかふかだよ、{w=0.3}これ」\n"
    $ ctc_mode = "page"
    extend "その無邪気な声に、余計に意識してしまう。\n"

    narrator_arrow "……いや、{w=0.3}違う。\n"
    extend "これは映研の活動だ。"
    extend "健全だ。"
    extend "そういうやつだ。"
    extend "僕が一人で変に考えてるだけだ。\n"
    $ ctc_mode = "page"
    extend "そんなことを思っているうちに、{w=0.3}もう[heroine['first']]は部屋の奥をのぞき込んでいる。\n"
    pause 0.4
    show sil_bg_guest_room_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_guest_room_02
    pause 0.4
    scene black
    with fade

    jump CH_05_guest_room_next

label CH_05_guest_room_c_2:
    window hide
    $ flag_seen_shadow = True # 人影フラグ（詳細は CH_00_flag.rpy）

    scene bg_guest_room_02 at fullscreen_bg
    with fade
    pause 0.4 
    show sil_bg_guest_room_03 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「ベッドどっちにする？{w=0.3}僕、{w=0.3}窓際がいい！」{nw}\n"
    extend "勢いのまま言うと、\n"
    extend "「え、{w=0.3}わたしも窓側がいい！」{nw}\n"
    extend "と即答された。\n"
    extend "「ちょ、{w=0.3}早いって」\n"
    extend "「景色見るの、絶対そっちの方がいいもん！」\n"
    extend "くだらない押し問答をしながら、僕たちは並んで窓に近づく。\n"
    $ ctc_mode = "page"
    extend "その瞬間。\n"
    stop music
    stop ambient_se
    hide sil_bg_guest_room_03
    pause 0.4
    scene black

    scene bg_guest_room_02 at fullscreen_bg
    show sil_bg_guest_room_04 at sil_center
    narrator_arrow "「きゃっ！」\n"
    extend "鋭い悲鳴。\n"
    extend "「ど、{w=0.3}どうした？」\n"
    extend "[heroine['first']]が窓の外を指さす。\n"
    extend "「いま、{w=0.3}窓に人影……！」\n"
    extend "「は？」\n"
    $ ctc_mode = "page"
    extend "ここ二階だぞ？\n"
    show sil_bg_guest_room_04 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_guest_room_04
    pause 0.4
    scene black
    with fade
    pause 0.4
    scene bg_guest_room_03 at fullscreen_bg
    with fade
    play sound "audio/se/カーテンを開ける.mp3"
    pause 0.4 
    extend "僕は眉をひそめながら、カーテンを大きく開ける。\n"
    $ ctc_mode = "page"
    extend "そして、{w=0.3}ゆっくり窓を押し上げた。\n"
    scene black
    with fade
    pause 0.4
    play sound "audio/se/窓を開ける.mp3"
    pause 0.8
    $ renpy.movie_cutscene("movies/movie_06.webm") 

    pause 0.4
    play ambient_se "audio/se/雨の音_2.mp3"
    scene bg_guest_room_04 at fullscreen_bg
    with fade
    narrator_arrow "湿った空気が流れ込む。\n"
    extend "うっそうとした森。\n"
    extend "雨粒が霧に溶けて、輪郭を曖昧にしている。\n"
    extend "目を凝らすが——{nw}\n"
    $ ctc_mode = "page"
    extend "動くものは見当たらない。\n"

    pause 0.4
    scene black
    with fade
    pause 0.4
    narrator_arrow "「……誰もいないよ」\n"
    play sound "audio/se/窓を閉める.mp3"
    extend "僕は、そう言って窓を閉めた。\n"
    extend "しかし、[heroine['first']]はまだ少し強張った顔をしている。\n"
    extend "「ほんとに？」\n"
    extend "「見間違いだよ」\n"
    $ ctc_mode = "page"
    extend "そう言いながらも、{w=0.3}背筋にほんのわずかな冷たさが残る。\n"

    $ choice_comment = ""

    menu:
        "１　……もしかして幽霊じゃないか？":
            $ choice_comment = ""
            jump CH_05_guest_room_c_2_1

        "２　いや、覗きか？":
            $ choice_comment = ""
            jump CH_05_guest_room_c_2_2

        "３　まさか、モンスター？":
            $ choice_comment = ""
            jump CH_05_guest_room_c_2_3

label CH_05_guest_room_c_2_1:
    window hide

    scene bg_guest_room_03 at fullscreen_bg
    with fade
    pause 0.4 
    narrator_arrow "「……幽霊じゃないか？」\n"
    extend "半分冗談のつもりだった。\n"
    extend "[heroine['first']]の顔色が、さっと変わる。\n"
    extend "「や、{w=0.3}やめてよ……」\n"
    extend "肩が強張るのが分かった。\n"
    $ ctc_mode = "page"
    extend "しまった、{w=0.3}と思う。\n"

    show sil_bg_guest_room_05 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「いや、違う違う。{w=0.5}真昼だし。{w=0.5}幽霊なんて出るわけないだろ」\n"
    extend "慌てて笑ってみせる。\n"
    extend "「雨と霧で、木の枝が揺れてただけだって。{w=0.5}絶対それ！」\n"
    extend "[heroine['first']]は窓から目を離し、小さく息を吐いた。\n"
    extend "「なんか気持ち悪い……{w=0.3}早くロビー行こ」\n"
    $ ctc_mode = "page"
    extend "「……そうだな」\n"

    show sil_bg_guest_room_05 at sil_center, sil_fadeout
    hide sil_bg_guest_room_05
    scene black
    with fade

    narrator_arrow "確か消灯は22時だったはずだ。\n"
    extend "予約制で風呂の時間も決まってる。\n"
    extend "夕食もある。\n"
    $ ctc_mode = "page"
    extend "思っていたより、余裕はない。\n"

    scene bg_guest_room_05 at fullscreen_bg
    with fade
    show sil_bg_guest_room_06 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「よし、{w=0.3}ロケハン開始だ！すぐ戻ろう！」\n"
    extend "僕は、気分を変えるようにすこし大きめに声をあげた。\n"
    extend "「うん」\n"
    $ ctc_mode = "page"
    extend "その効果あってか、[heroine['first']]はすこし気分を戻したようだ。\n"

    scene black
    with fade
    narrator_arrow "部屋を出るとき、{w=0.3}僕は無意識にもう一度だけ窓の方を振り返った。\n"
    extend "——何もいない。{w=0.5}{nw}\n"
    $ ctc_mode = "page"
    extend "……はずだ。\n"

    jump CH_06_To_the_lobby

label CH_05_guest_room_c_2_2:
    window hide

    scene bg_guest_room_03 at fullscreen_bg
    with fade
    pause 0.4 
    show sil_bg_guest_room_07 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「いや……{w=0.5}覗きか？」\n"
    extend "口にした瞬間、\n"
    extend "「やめてよ！」\n"
    $ ctc_mode = "page"
    extend "必死な[heroine['first']]の様子に僕は苦笑いしながら、少し冷静になる。\n"

    pause 0.4
    show sil_bg_guest_room_07 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_guest_room_07
    pause 0.4 
    show sil_bg_guest_room_08 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「こんな山奥のペンションに、わざわざ覗きに来るやついるか？」\n"
    extend "六月のオフシーズン。"
    extend "客も多くはないはずだ。\n"
    extend "「しかも二階だぞ？{w=0.3}物理的に無理だろ」\n"
    extend "「……でも、{w=0.3}見えた気がしたんだもん」\n"
    $ ctc_mode = "page"
    extend "そう小さくつぶやき、[heroine['first']]は腕をさする。\n"

    pause 0.4
    show sil_bg_guest_room_08 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_guest_room_08
    pause 0.4 
    show sil_bg_guest_room_05 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「きっと霧だよ。{w=0.5}木の影とか」\n"
    extend "僕がそう言ってみせるが、[heroine['first']]の気分は完全に打ち消せたわけではなさそうだ。\n"
    extend "「なんか気持ち悪い……{w=0.3}早くロビー行こ」\n"
    $ ctc_mode = "page"
    extend "「……そうだな」\n"

    show sil_bg_guest_room_05 at sil_center, sil_fadeout
    hide sil_bg_guest_room_05
    scene black
    with fade

    narrator_arrow "確か消灯は22時だったはずだ。\n"
    extend "予約制で風呂の時間も決まってる。\n"
    extend "夕食もある。\n"
    $ ctc_mode = "page"
    extend "思っていたより、余裕はない。\n"

    scene bg_guest_room_05 at fullscreen_bg
    with fade
    show sil_bg_guest_room_06 at sil_center, sil_fadein
    pause 0.4

    narrator_arrow "「よし、{w=0.3}ロケハン開始だ！{w=0.3}すぐ戻ろう！」\n"
    extend "僕は、気分を変えるようにすこし大きめに声をあげた。\n"
    extend "「うん」\n"
    $ ctc_mode = "page"
    extend "その効果あってか、[heroine['first']]はすこし気分を戻したようだ。\n"
    play sound "audio/se/ドアを閉める1.mp3"
    scene black
    with fade
    pause 0.3
    play sound "audio/se/ドアを閉める1.mp3"
    pause 0.3

    $ ctc_mode = "page"
    narrator_arrow "ドアを閉めるとき、{w=0.3}閉ざされたカーテンが妙に重く見えた。\n"

    stop music fadeout 1.0
    stop ambient_se fadeout 1.0
    pause 0.4

    scene black
    with fade

    jump CH_06_To_the_lobby

label CH_05_guest_room_c_2_3:
    window hide
    stop ambient_se
    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/bgm/ぜんぜん余裕です.mp3"
    scene bg_guest_room_02 at fullscreen_bg
    with fade
    narrator_arrow "「……まさか、{w=0.3}モンスター？」\n"
    extend "[heroine['first']]が眉をひそめる。\n"
    extend "「は？」\n"
    extend "「ほら、{w=0.3}この森。{w=0.3}いかにも出そうじゃない？」\n"
    $ ctc_mode = "page"
    extend "僕は指を折る。\n"

    show bg movie_loop_2 at fullscreen_bg 
    with fade
    pause 0.2 
    show sil_bg_guest_room_09 at sil_center, sil_fadein
    narrator_arrow "「まず雪男」\n"
    extend "「六月だよ？」\n"
    extend "「そう……{w=0.3}冬のために買い出しに来てるんだ」\n"
    $ ctc_mode = "page"
    extend "「計画的すぎるでしょ」\n"
    scene black
    with dissolve

    show bg movie_loop_3 at fullscreen_bg 
    pause 0.2 
    show sil_bg_guest_room_10 at sil_center, sil_fadein
    narrator_arrow "「じゃあ……{w=0.3}河童」\n"
    extend "「ここ山だよ？！」\n"
    extend "「出張中」\n"
    play sound "audio/se/ビシッとツッコミ3.mp3"
    extend "「業務範囲広げるな！」\n"
    $ ctc_mode = "page"
    extend "テンポよく叩かれ、僕は肩をすくめた。\n"

    scene black
    with dissolve
    show bg movie_loop_4 at fullscreen_bg 
    pause 0.2 
    show sil_bg_guest_room_11 at sil_center, sil_fadein
    narrator_arrow "「じゃあ、{w=0.3}六月だし……{w=0.3}巨大カエル」\n"
    extend "「なにそれ？」\n"
    extend "「きっとジャンプしてたんだよ。"
    extend "これで２階でも筋が通る」\n"
    extend "「[player['first']]君……{w=0.5}大丈夫？」\n"
    $ ctc_mode = "page"
    extend "少しだけ笑ってくれたが、{w=0.3}だんだん[heroine['first']]は別の意味で心配になってきているようだった。\n"
    scene black
    with fade
    stop music fadeout 1.0
    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.0
    scene bg_guest_room_05 at fullscreen_bg
    with fade
    show sil_bg_guest_room_12 at sil_center, sil_fadein
    pause 0.4
    narrator_arrow "「なんか寒くなってきた……{w=0.5}早くロビー行こ」\n"
    extend "「……だな」\n"
    extend "確か消灯は22時だったはずだ。\n"
    extend "風呂の時間も決まっているし、夕食もある。\n"
    extend "モンスター談義をしている余裕は、あまりない。\n"
    extend "「荷物置いたし、ロビーに戻ろう」\n"
    $ ctc_mode = "page"
    extend "「うん」\n"

    stop music fadeout 1.0
    stop ambient_se fadeout 1.0
    pause 0.4

    scene black
    with fade

    jump CH_06_To_the_lobby

label CH_05_guest_room_c_3:
    window hide

    scene bg_guest_room_02 at fullscreen_bg
    with fade
    narrator_arrow "部屋は、その広さゆえにベッド２つでほぼ埋まっている。\n"
    extend "窓際にテーブルと椅子。\n"
    extend "木製キャビネット下には、ミニ冷蔵庫。\n"
    $ ctc_mode = "page"
    extend "コンパクトな簡易クローゼット。\n"

    narrator_arrow "……なんだかレイアウトがビジネスホテルなんだよなぁ。\n"
    extend "これは画角を考えないと一気に現実感が出てしまうな。\n"
    extend "せっかく彼女と二人きりのお泊りで、そんなことを思ってしまった自分に苦笑する。\n"
    extend "はしゃいでいる[heroine['first']]の手前、そんな感想は口に出さなかった。\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]は、部屋の奥をのぞき込んでいる。\n"

    jump CH_05_guest_room_next

label CH_05_guest_room_next:
    window hide

    scene bg_guest_room_05 at fullscreen_bg
    with fade
    pause 0.4 
    show sil_bg_guest_room_next_01 at sil_center, sil_fadein
    pause 0.4 
    narrator_arrow "「あ、{w=0.3}やっぱり部屋にお風呂ない」\n"
    extend "「そうそう、{w=0.3}共同って書いてあったな」\n"
    $ ctc_mode = "page"
    extend "リノベ物件だし、そこは仕方ないか。\n"

    pause 0.4
    show sil_bg_guest_room_next_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_bg_guest_room_next_01
    pause 0.4

    narrator_arrow "「大浴場って何時だっけ？」\n"
    extend "「[player['first']]君が20時で、{w=0.3}わたしが21時」\n"
    extend "さすがにそこは別々だよな……。\n"
    extend "まてよ、{w=0.3}20時が風呂なら晩御飯はその前に済ませることになるだろう。\n"
    extend "確か消灯時間は22時だったはずだから……。\n"
    pause 0.4 
    show sil_bg_guest_room_next_02 at sil_center, sil_fadein
    pause 0.4 
    extend "「あんまり余裕ないな。{w=0.3}荷物置いて、すぐ戻ろうか」\n"
    extend "「なんかさ、{w=0.3}せっかく泊まりなのに、スケジュールぎっちりだね」\n"
    extend "「まあ、これ、映研の合宿みたいなもんだしな」\n"
    $ ctc_mode = "page"
    extend "「うん」\n"

    stop music fadeout 1.0
    stop ambient_se fadeout 1.0
    pause 0.4

    scene black
    with fade

    jump CH_06_To_the_lobby