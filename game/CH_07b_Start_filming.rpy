label CH_07b_Start_filming:

    window hide

    $ flag_lobby_photo_taken = True # ロビーで撮影フラグ（CH_00_flag.rpy）
    $ flag_lobby_kino = True # 木下ルートフラグ２（詳細は CH_00_flag.rpy）
    pause 0.4
    scene black
    with fade

    narrator_arrow "僕はスマホを取り出した。\n"
    extend "「……木下さんに聞いてみよう」\n"
    extend "メッセージアプリを開く。\n"
    $ ctc_mode = "page"
    extend "もうすでにロケハン中の写真を逐一送っているから、{w=0.3}何かしら指示をくれるはずだ。\n"

    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master # シェード機能（CH_00_effects.rpy）
    with fade

    narrator_arrow "** [player['last']]：**{nw}\n"
    extend "「ロケハン中です。撮影で迷っています。欲しい写真とかありますか？」\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "数分もしないうちに返信が届いた。\n"

    narrator_arrow "**木下：**{nw}\n"
    extend "「おお、ご苦労。送られた写真見てるよ。」\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "数秒後、また返信が来た。\n"

    narrator_arrow "**木下：**{nw}\n"
    extend "「今どこにいるの？」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    extend "「ロビーにいます」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「いいロビーじゃん」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「ここで死体発見しよう」\n"

    stop music
    stop ambient_se
    play sound "audio/se/過去を思い出す.mp3"
    scene black

    narrator_arrow "「え？」\n"
    extend "思わず声が出た。\n"
    extend "{nw}\n"
    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master
    with fade
    extend "**木下：**{nw}\n"
    extend "「今まさに“死体発見の場所”をどこにするか悩んでたんだよね～」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「ロビーの床でさあ、ちょっと死んでみて！」\n"


    scene bg_to_the_lobby_01 at fullscreen_bg
    with fade
    show sil_b_start_filming_01 at sil_center

    play music "audio/bgm/ぜんぜん余裕です.mp3"
    narrator_arrow "死んでみてだって！？\n"
    extend "そんな憤る僕の肩越しに、[heroine['first']]がスマホをのぞき込む。\n"
    extend "「[player['first']]君、死体役オファー来てるね」\n"
    $ ctc_mode = "page"
    extend "「え！？この床で寝るの……？」\n"

    show sil_b_start_filming_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_01
    pause 0.4

    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master
    with fade
    narrator_arrow "**木下：**{nw}\n"
    extend "「ロケハンなんだから実際にやってみないと！」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「 [player['last']]くんおねがい。映画はリアリティが命！」\n"

    pause 0.4
    scene bg_to_the_lobby_01 at fullscreen_bg
    with fade
    show sil_b_start_filming_02 at sil_center

    narrator_arrow "僕はスマホを見つめた。\n"
    extend "「死体役か……」\n"
    extend "[heroine['first']]は笑いながら言う。\n"
    $ ctc_mode = "page"
    extend "「監督命令！がんばれ！」\n"

    show sil_b_start_filming_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_02
    pause 0.4
    scene black
    with fade

    scene bg_b_start_filming_01 at fullscreen_bg
    with fade

    narrator_arrow "このペンションでは専用のスリッパに履き替えるようになっているし、{w=0.5}毎日きちんと掃除されているんだろうことも理解している。\n"
    extend "それでも――{w=0.5}{nw}\n"
    extend "ロビーの床に直に寝転ぶとなると、{w=0.3}やっぱり少し抵抗がある。\n"
    extend "「なんかさ、{w=0.5}汚れとかないけどさ、{w=0.5}なんかこう……」\n"
    extend "「リアリティだよ！我慢我慢」\n"
    extend "[heroine['first']]はそう言いながらカメラを構える。\n"
    extend "「ううっ」\n"
    $ ctc_mode = "page"
    extend "僕は仕方なく床に横になった。\n"

    show sil_b_start_filming_03 at sil_center, sil_fadein

    narrator_arrow "板張りの床は、雨の湿気のせいかひんやりしている。\n"
    extend "「……冷たい」\n"
    extend "「はい、そのまま動かないで」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "[heroine['first']]は撮影を終わると、すぐにその写真を木下さんに送る。\n"
    $ ctc_mode = "page"
    extend "数秒後、返信。\n"

    show sil_b_start_filming_03 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_03
    pause 0.4
    scene black
    with fade

    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master
    with fade
    narrator_arrow "**木下：**{nw}\n"
    extend "「いいじゃんいいじゃん！」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「たださ、ロビーだと“発見された感”がちょっと弱いんだよね～」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「ウッドデッキ行ってみよっか！」\n"

    pause 0.4
    scene black
    with fade
    pause 0.4
    scene bg_to_the_lobby_04 at fullscreen_bg
    with fade

    narrator_arrow "窓の外は未だ小雨だった。\n"
    extend "ウッドデッキに屋根はあるが、雨粒が横から吹き込んでくる。\n"
    extend "もしかして……？\n"
    $ ctc_mode = "page"
    extend "スマホを見る。\n"


    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master    
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「ウッドデッキでも絵が欲しいんだよね～」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    extend "「雨降ってるのに！？マジっすか！？」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「これくらい働いてよ～」\n"

    scene bg_to_the_lobby_04 at fullscreen_bg
    with fade
    show sil_b_start_filming_04 at fullscreen_bg, sil_fadein
    narrator_arrow "[heroine['first']]が肩を震わせて笑う。\n"
    extend "「[player['first']]くん、続投」\n"
    $ ctc_mode = "page"
    extend "「いやいやいや、ちょっと待って、待って！！」\n"

    stop music fadeout 2.0
    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.0
    show sil_b_start_filming_04 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_04
    pause 0.4
    scene black
    with fade
    pause 0.4
    scene bg_b_start_filming_02 at fullscreen_bg
    with fade

    show sil_b_start_filming_05 at sil_center, sil_fadein

    narrator_arrow "──しかし数分後。\n"
    extend "僕はデッキに仰向けで寝ていた。\n"
    extend "細かい雨が全身に落ちる。\n"
    extend "「……冷たい」\n"
    extend "「はい、いい感じ」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "[heroine['first']]は楽しそうに撮影している。\n"
    $ ctc_mode = "page"
    extend "すぐ返信。\n"

    scene black
    with fade
    narrator_arrow "**木下：**{nw}\n"
    extend "「おお！これはいい！ [player['last']]くん体張ってるねえ」\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "お気に召したようで何よりですね！\n"

    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    pause 0.4
    scene black
    with fade
    pause 0.4
    scene bg_to_the_lobby_06 at fullscreen_bg
    show shade onlayer master
    with fade
    play music "audio/bgm/ぜんぜん余裕です.mp3"

    narrator_arrow "**木下：**{nw}\n"
    extend "「あとさ、この階段！」\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "先ほど送信したロビーの階段の写真を見ているようだ。\n"

    narrator_arrow "**木下：**{nw}\n"
    extend "「バタバタバターッて落下できない？」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    $ ctc_mode = "page"
    extend "「できませんよ！！本物の死体が出ます」\n"
    extend "{nw}\n"
    pause 0.4
    scene black
    with fade
    $ ctc_mode = "page"
    narrator_arrow "数秒後。\n"

    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master    
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「なるほど、じゃあ、階段で死んでみて」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    extend "「はい？」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「階段で死体役、おねがい」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    $ ctc_mode = "page"
    extend "「なんか僕の扱い雑になってきてないですか？」\n"

    pause 0.4
    scene bg_to_the_lobby_06 at fullscreen_bg
    with fade
    narrator_arrow "結局。\n"
    pause 0.4
    show sil_b_start_filming_06 at sil_center, sil_fadein
    extend "僕は階段の途中に横たわることになった。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "[heroine['first']]は冷静に写真を撮る。\n"

    show shade onlayer master
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「いいねえ！ [player['last']]君、様になってるじゃないか！」\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "そんなこと言われてもうれしくないよ。\n"

    show sil_b_start_filming_06 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_06
    hide shade onlayer master
    pause 0.4
    show sil_b_start_filming_07 at sil_center, sil_fadein

    narrator_arrow "[heroine['first']]は撮った写真を確認しながら笑った。\n"
    extend "「このカメリハ、[player['first']]くんの死体コレクションになりそうだね」\n"
    extend "「やめて」\n"
    $ ctc_mode = "page"
    extend "そのやり取りの最中、スマホから返信がくる。\n"

    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master    
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「いいねいいね、バリエーション増えてきたね～」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「次、二階の廊下いってみよっか」\n"

    hide shade onlayer master
    pause 0.4
    scene bg_second_floor_03 at fullscreen_bg
    with fade

    narrator_arrow "二階も未だ誰もいない。\n"
    $ ctc_mode = "page"
    extend "静かな長い廊下がまっすぐ奥まで伸びている。\n"

    show shade onlayer master
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「 [player['last']]くん、この廊下を全力でダッシュしてくれない？」\n"
    extend "{nw}\n"
    extend "** [player['last']]：**{nw}\n"
    extend "「なんと？」\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「いやね、犯人がさ、被害者を追い詰める場面があるんだよね～」\n"

    hide shade onlayer master

    narrator_arrow "今度は走るのかよ……。\n"
    extend "[heroine['first']]が笑いながら言う。\n"
    extend "「はい、走って！頑張って！」\n"
    $ ctc_mode = "page"
    extend "僕は廊下を走ることになった。\n"

    narrator_arrow "「はいスタート！」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]が叫ぶ。\n"

    $ play_anim_once("dash", "images/anim/dash/", speed=0.05, at_list=[fullscreen_bg]) # 影絵アニメーション　ワンショット
    $ renpy.pause(5.0, hard=True) # 完全に操作をロック

    narrator_arrow "一往復。\n"
    extend "二往復。\n"
    extend "三往復。\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]はその様子ずっと撮影している。\n"

    scene bg_second_floor_07 at fullscreen_bg
    with fade
    show sil_b_start_filming_08 at sil_center, sil_fadein

    narrator_arrow "しばらくして、僕は廊下の壁にもたれて息を整えた。\n"
    extend "「……これ本当にロケハン？」\n"
    extend "[heroine['first']]がスマホを見た。\n"
    $ ctc_mode = "page"
    extend "「返信きてる」\n"

    show sil_b_start_filming_08 at sil_center, sil_fadeout
    pause 0.4
    hide sil_b_start_filming_08
    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master    
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「いいね！もう一回お願い！」\n"
    $ ctc_mode = "page"
    extend "{nw}\n"

    narrator_arrow "僕はスマホを握りしめた。\n"
    extend "「……」\n"
    extend "怒りで手が震える。\n"
    $ ctc_mode = "page"
    extend "僕はメッセージを打つ。\n"

    narrator_arrow "** [player['last']]：**{nw}\n"
    extend "「これ本当に映画に使うんですか？」\n"
    extend "{nw}\n"
    extend "しばらくして返信。\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「いや、なんか面白くなってきちゃってw」\n"
    stop music
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "僕はスマホを見つめたまま固まった。\n"

    pause 0.4
    scene bg_second_floor_07 at fullscreen_bg
    with fade
    show sil_b_start_filming_09 at sil_center, sil_fadein
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    narrator_arrow "[heroine['first']]が吹き出した。\n"
    extend "「[player['first']]くん、完全に遊ばれてるね」\n"
    extend "──ふざけやがって！\n"
    $ ctc_mode = "page"
    extend "もう木下さんに指示を聞くのはやめよう。\n"
    stop music fadeout 1.5
    pause 0.3
    scene black
    with slow_fade # ゆっくりフェードアウト 記述は （CH_00_effects.rpy）へ
    $ renpy.pause(1.0, hard=True) # 完全に操作をロック

    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.5
    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master
    with fade
    narrator_arrow "あらかた撮影を終えたころ、スマホに木下さんからねぎらいのメッセージがきた。\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「いやーいい絵が取れたよ、ありがとう」\n"
    extend "{nw}\n"
    extend "無神経な木下さんは、素直に礼を言ったあと、こう続けた。\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    $ ctc_mode = "page"
    extend "「そういえばさ、夕飯は山のふもとのレストラン、予約しといたから」\n"

    pause 0.4
    scene bg_second_floor_07 at fullscreen_bg
    with fade
    show sil_b_start_filming_10 at sil_center, sil_fadein

    narrator_arrow "「……レストラン？」\n"
    extend "そういえば、晩ごはんのことなんて、まったく考えていなかった。\n"
    extend "{nw}\n"
    extend "**木下：**{nw}\n"
    extend "「地図は送っておいたよ」\n"
    extend "{nw}\n"
    extend "[heroine['first']]が肩を揺らして笑う。\n"
    extend "「さすが。段取りだけは完璧だね」\n"
    $ ctc_mode = "page"
    extend "「ほんとだよ……」\n"

    scene black
    with fade

    narrator_arrow "僕はスマホで時間を確認する。\n"
    extend "「……ちょうどいい時間か」\n"
    extend "「行こうよ。おなかすいた」\n"
    $ ctc_mode = "page"
    extend "空腹に急かされるようにして、僕たちはペンションを後にした。\n"

    jump CH_08_restaurant_scene