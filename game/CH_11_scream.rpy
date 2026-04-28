label CH_11_scream:
    window hide

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_scream_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)
    play music "audio/se/エアコン.mp3" volume 0.4
    pause 0.8


    narrator_arrow "大浴場の暖簾をくぐり、廊下に出る。\n"
    extend "相変わらず館内は静か。\n"
    extend "……さっきまで風呂に入っていたせいか、{w=0.3}少しだけ現実感が薄い。\n"
    $ ctc_mode = "page"
    extend "床をぼんやり照らしている自販機のライトの低いジーっという音に、{w=0.3}なぜだか心細さを感じた。\n"

    narrator_arrow "早く部屋に戻ろう。\n"
    extend "そして[heroine['first']]を呼ぼう。\n"
    extend "そう思い、ロビーの方へ歩き出した。\n"
    $ ctc_mode = "page"
    extend "そのとき――\n"

    scene black
    stop music
    play sound "audio/se/「キャー」.mp3"
    narrator_arrow "「きゃああっ！！」\n"
    extend "思わず足が止まる。\n"
    extend "今の声――\n"
    extend "「[heroine['first']]？」\n"
    extend "二階の方だ。\n"
    $ ctc_mode = "page"
    extend "一瞬の静寂。\n"

    narrator_arrow "次の瞬間、\n"
    play sound "audio/se/壁をドンと叩く.mp3"
    pause 0.1
    play sound "audio/se/机をドンと叩く.mp3"
    pause 0.1
    play sound "audio/se/壁をドンと叩く.mp3"
    pause 0.1
    play sound "audio/se/机をドンと叩く.mp3"
    pause 0.1
    play sound "audio/se/壁をドンと叩く.mp3"
    pause 0.1
    play sound "audio/se/机をドンと叩く.mp3"
    pause 0.5
    extend "――ドタドタドタッ！\n"
    extend "誰かが走り去るような激しい足音が二階の廊下に響いた。\n"
    play music "audio/bgm/潜む怪奇.mp3" fadein 1.5
    extend "「……っ！」\n"
    extend "心臓が跳ね上がる。\n"
    extend "[heroine['first']]に何かあったのか！？ただ事ではない。\n"
    extend "「[heroine['first']]！」\n"
    $ ctc_mode = "page"
    extend "僕は反射的にロビーへ走り出した。\n"

    play sound "audio/se/学校の廊下を走る.mp3"
    scene black
    with fade


    scene bg_scream_02 at fullscreen_bg
    with fade

    narrator_arrow "階段を駆け上がろうとした――\n"
    extend "その瞬間。\n"
    play sound "audio/se/家の階段を駆け上る.mp3"
    $ ctc_mode = "page"
    extend "二階の廊下から、誰かが慌てて階段を降りてくる。\n"

    show sil_scream_01 at sil_center, sil_fadein

    stop music
    narrator_arrow "「……っ！」\n"
    extend "[heroine['first']]だった。\n"
    extend "顔色が真っ青で、ほとんど転げるように階段を降りてくる。\n"
    extend "「[heroine['first']]！」\n"
    extend "[heroine['first']]もこちらに気づいた。\n"
    $ ctc_mode = "page"
    extend "「……[player['first']]！」\n"

    scene black
    with fade
    $ play_anim_once("dash", "images/anim/yui_dash/", speed=0.05, at_list=[fullscreen_bg]) 
    pause 0.5
    narrator_arrow "次の瞬間、[heroine['first']]は、まっすぐ僕の方へ走ってきて――\n"
    scene bg_scream_03 at fullscreen_bg
    $ play_anim_once("dash", "images/anim/hug/", speed=0.05, at_list=[fullscreen_bg]) 
    $ renpy.pause(1.0, hard=True) # 完全に操作をロック
    pause 1.0
    extend "抱きついた。\n"
    extend "僕は慣れないことに動揺しながらも、{w=0.3}しっかり受け止める。\n"
    extend "「……いたの」\n"
    extend "[heroine['first']]の声は震えていた。\n"
    extend "「そこに……誰か……！」\n"
    extend "「誰かって……？」\n"
    $ ctc_mode = "page"
    extend "僕の問いに[heroine['first']]は首を振る。\n"

    scene black
    with fade

    play music "audio/bgm/潜む怪奇.mp3" fadein 1.5
    narrator_arrow "幽霊――\n"
    extend "そんな言葉が一瞬、頭をよぎる。\n"
    extend "いや、{w=0.3}そんなわけない。\n"
    extend "考えを振り払った。\n"
    extend "しかし……{w=0.3}さっきの足音。\n"

    scene bg_scream_04 at fullscreen_bg
    with Dissolve(1.0)
    extend "僕は反射的に、二階を見上げた。\n"
    $ ctc_mode = "page"
    extend "誰かが……{w=0.3}何かが……{w=0.3}走っていたのは確かだ。\n"

    narrator_arrow "「……ちょっと見てくる」\n"
    extend "僕がそう言うと\n"
    extend "「だめ」\n"
    extend "と、{w=0.3}僕の服を掴む[heroine['first']]の手に、さらに力が入る。\n"
    extend "「……怖い」\n"
    extend "小さく呟く。\n"
    $ ctc_mode = "page"
    extend "「離れたくない」\n"

    narrator_arrow "僕は少しだけ迷ったが、{w=0.3}すっかりおびえ切った[heroine['first']]をみると置いていくわけにもいかない。\n"
    extend "「じゃあ、一緒に行こう」\n"
    extend "[heroine['first']]は、無言で小さくうなずいた。\n"
    $ ctc_mode = "page"
    extend "僕たちはゆっくりと、ロビーの階段へ向かう。\n"


    scene black
    with Dissolve(1.0)

    pause 1.8

    narrator_arrow "一段ずつ、{w=0.3}慎重に階段を上がる。\n"
    $ ctc_mode = "page"
    extend "木の階段が小さく軋む。\n"

    scene bg_scream_05 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "二階に着く。\n"
    extend "廊下には――\n"
    extend "誰もいなかった。\n"
    extend "静かだ。\n"
    $ ctc_mode = "page"
    extend "さっきの足音が嘘みたいに、{w=0.3}何の気配もない。\n"


    narrator_arrow "「……誰もいない」\n"
    extend "僕は廊下を見渡す。\n"
    extend "客室のドアはすべて閉まっている。\n"
    $ ctc_mode = "page"
    extend "廊下の奥まで人影は見えない。\n"

    play sound "audio/se/ドアを開ける1.mp3"
    pause 0.5
    scene bg_return_to_room_03 at fullscreen_bg
    with fade

    narrator_arrow "念のため、自分たちの客室ものぞいてみる。\n"
    extend "……異常はない。\n"
    extend "[heroine['first']]も不安そうに廊下を見回している。\n"
    extend "「一体あれは……？」\n"
    $ ctc_mode = "page"
    extend "僕が言いかけた、そのとき。\n"

    scene black

    stop music
    play sound "audio/se/壁をドンと叩く.mp3"
    pause 0.5
    play sound "audio/se/机をドンと叩く.mp3"

    narrator_arrow "――ドン！！\n"
    extend "突然、大きな音が廊下に響いた。\n"
    extend "僕と[heroine['first']]は同時に振り向く。\n"
    extend "音は――\n"
    scene bg_scream_05 at fullscreen_bg
    with Dissolve(0.3)
    extend "廊下の奥。\n"
    $ ctc_mode = "page"
    extend "二階の突き当たりだ。\n"

    # ==== フラグ分岐 ====================================================
    if flag_a_Start_filming:
        narrator_arrow "突き当たりには、扉がある。\n"
        extend "ただの物置か何かだと思っていた扉。\n"
    else:
        narrator_arrow "廊下の突き当りには、観音開きの大きな扉があった。\n"
    # ====================================================================
     
    extend "「……あそこ？」\n"
    extend "[heroine['first']]が小さく言う。\n"
    extend "あれはそう……{w=0.3}扉の向こうから、{w=0.3}何かがぶつかったような音だった。\n"
    $ ctc_mode = "page"
    extend "僕たちは顔を見合わせる。\n"

    scene black
    with fade

    narrator_arrow "僕たちはゆっくりと廊下の突き当たりの扉へ近づいていく。\n"
    extend "[heroine['first']]はまだ僕の腕を掴んだままだ。\n"
    extend "「……ここだよな」\n"
    $ ctc_mode = "page"
    extend "僕の問いに[heroine['first']]はうなずくけれど、視線は扉から離れない。\n"

    scene bg_scream_06 at fullscreen_bg
    with fade

    narrator_arrow "古い木の扉だ。\n"
    extend "取っ手はついているが、鍵がかかっているのかどうかはわからない。\n"
    extend "「……開けてみる？」\n"
    extend "僕が言いかけた、その瞬間――\n"
    play sound "audio/se/机をドンと叩く.mp3"
    extend "バンッ！！\n"
    extend "扉が突然、ものすごい勢いで内側から開いた。\n"
    extend "「きゃああっ！！」\n"
    extend "「うわっ！！」\n"
    extend "僕と[heroine['first']]は同時に悲鳴を上げて、思わず後ずさる。\n"
    $ ctc_mode = "page"
    extend "次の瞬間――白い何かが、ものすごい勢いで廊下に飛び出してきた。\n"

    pause 0.2

    scene black
    with dissolve

    $ renpy.movie_cutscene("movies/movie_09.webm", stop_music=True)

    scene bg_scream_07 at fullscreen_bg
    with fade
    play music "audio/bgm/ぜんぜん余裕です.mp3"
    narrator_arrow "……犬だ。\n"
    extend "しかも――\n"
    $ ctc_mode = "page"
    extend "「……でかい」\n"

    narrator_arrow "丸い顔。\n"
    extend "大きな体。\n"
    extend "真っ白で、{w=0.3}まるで、{w=0.3}ぬいぐるみみたいにふわふわの毛。\n"
    extend "それは**大きな白いサモエド**だった。\n"
    extend "「……」\n"
    extend "「……」\n"
    $ ctc_mode = "page"
    extend "僕と[heroine['first']]は顔を見合わせる。\n"

    scene bg_scream_08 at fullscreen_bg
    with fade
    show sil_scream_02 at sil_center

    play sound "audio/se/学校の廊下を走る.mp3"
    narrator_arrow "その時、どこからともなく男性の声が響いた。\n"
    extend "「こら！待て！」\n"
    extend "ロビーの奥から一人の男性が慌てて走ってくる。\n"
    stop sound
    extend "男性は軽やかに近づくと、白い犬の首輪をひょいと掴んだ。\n"
    $ ctc_mode = "page"
    extend "その大きな白いサモエドは、{w=0.3}まるで笑っているみたいな顔で嬉しそうに尻尾を振っている。\n"

    show sil_scream_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_scream_02

    scene bg_scream_09 at fullscreen_bg
    with fade
    show sil_scream_03 at sil_center

    narrator_arrow "「すみません！」\n"
    extend "男性は少し息を切らしながら、こちらに頭を下げた。\n"
    extend "「びっくりさせましたよね」\n"
    extend "僕と[heroine['first']]は、まだ状況を理解できずにただ立ち尽くしていた。\n"
    $ ctc_mode = "page"
    extend "男性はもう一度、申し訳なさそうに頭を下げる。\n"

    narrator_arrow "「この犬、{w=0.3}うちで飼ってるんですよ」\n"
    extend "「……うち？」\n"
    $ ctc_mode = "page"
    extend "「ああ！{w=0.3}すみません。{w=0.3}申し遅れました」\n"

    show sil_scream_03 at sil_center, sil_fadeout
    pause 0.4
    hide sil_scream_03
    scene bg_scream_10 at fullscreen_bg
    with fade
    play sound "audio/se/財布を開ける.mp3"

    narrator_arrow "男性は、ポケットから革のカードケースを取り出した。\n"
    extend "中には{nw}\n"
    extend "「North Frame Pension」{nw}\n"
    $ ctc_mode = "page"
    extend "と書かれたオーナー用の名刺と、{w=0.3}この建物のマスターキーらしい鍵束が入っている。\n"


    scene bg_scream_09 at fullscreen_bg
    with fade
    show sil_scream_03 at sil_center

    narrator_arrow "「私、{w=0.3}このペンションのオーナーなんです。"
    extend "普段は別宅に住んでるんですけどね」\n"
    extend "オーナーは、犬の首輪を軽く引きながら続けた。\n"
    extend "「たまに、この子が勝手にペンションに来ちゃうんですよ。"
    extend "今日も気づいたら中を走り回ってて"
    extend "……本当にすみません」\n"
    extend "サモエドは嬉しそうに尻尾を振りながら、廊下の匂いを嗅いでいる。\n"
    $ ctc_mode = "page"
    extend "その様子を見ていると、{w=0.3}さっきまでの緊張が嘘みたいだった。\n"

    stop music fadeout 2.0
    show sil_scream_03 at sil_center, sil_fadeout
    pause 0.4
    hide sil_scream_03
    scene black
    with fade
    pause 0.4

    narrator_arrow "「……はあ」\n"
    extend "相槌ついでに、{w=0.3}僕は小さく息を吐く。\n"
    $ ctc_mode = "page"
    extend "疲れが、{w=0.5}どっと押し寄せてきた。\n"

    scene bg_scream_11 at fullscreen_bg
    with fade
    show sil_scream_04 at sil_center

    narrator_arrow "「すみません、{w=0.3}お騒がせしました」\n"
    extend "オーナーはそう言うと、{w=0.3}サモエドの首輪を軽く引きながら廊下の奥へ歩き出した。\n"
    extend "サモエドはまだ遊び足りないのか、{w=0.3}嬉しそうに尻尾を振りながら何度もこちらを気にするように振り返る。\n"
    $ ctc_mode = "page"
    extend "やがてオーナーに促され、サモエドは名残惜しそうにもう一度こちらを見ると、{w=0.3}そのまま廊下の奥へと消えていった。\n"

    scene black
    with fade
    pause 0.4
    scene bg_scream_05 at fullscreen_bg
    with fade

    narrator_arrow "やがて二人（？）の気配が消えると、{w=0.3}廊下にはまた静けさが戻った。\n"
    extend "しばらくして――\n"
    extend "「もしかしてさ……」{w=0.5}{nw}"
    extend "と、{w=0.3}[heroine['first']]がおもむろに話し出す。\n"
    extend "「白い幽霊の正体って、{w=0.5}この犬のことじゃない……？」\n"
    extend "確かに、{w=0.5}白い。\n"
    extend "別宅からやってくるならば、{w=0.3}森のほうへ消えていくのもつじつまが合う。\n"
    extend "「ああ、{w=0.3}そうかもね」\n"
    $ ctc_mode = "page"
    extend "そう思うと、{w=0.3}さっきまでの緊張が一気にほどけた。\n"

    narrator_arrow "「……疲れた」\n"
    extend "[heroine['first']]がぽつりと言う。\n"
    extend "さっきまでの恐怖と緊張で、{w=0.3}すっかり気力を使い果たしたようだ。\n"
    extend "「今日は、{w=0.3}もう……{w=0.3}早く寝よう」\n"
    extend "[heroine['first']]が、{w=0.3}またぽつりと言う。\n"
    extend "「……そうだな」\n"
    $ ctc_mode = "page"
    extend "僕もそれに同意した。\n"

    stop music fadeout 2.0

    jump CH_10_last_scene




























































































