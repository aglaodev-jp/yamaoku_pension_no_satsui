label  CH_02_pension_front:
    window hide
    play music "audio/se/雨の音_2.mp3" fadein 0.5
    scene black
    with fade
    narrator_arrow "エンジンを切ると、雨音が一気に車内を包む。\n"
    extend "ワイパーが止まり、窓ガラスに斜めの線がいくつも重なった。\n"
    extend "……着いた。\n"
    extend "無事に。\n"
    $ ctc_mode = "page"
    extend "山道で対向車が来なくて本当に助かった。\n"

    narrator_arrow "「[player['first']]くん、{w=0.3}運転おつかれさま」\n"
    extend "[heroine['first']]が笑う。\n"
    extend "その声がやけに柔らかくて、僕はそれだけで報われた気がした。\n"
    extend "「いや……ほんと、{w=0.3}なんとか辿り着けてよかった。"
    extend "ガードレールないカーブとか、心臓に悪すぎるだろ」\n"
    extend "「大丈夫だったよ。{w=0.3}全然、酔わなかったし」\n"
    $ ctc_mode = "page"
    extend "それはそれで、僕としては大きな勝利だ。\n"

    # scene bg_pension_front_02 at fullscreen_bg
    show bg movie_loop_1 at fullscreen_bg # ループ動画の背景はshowで表示。sceneだとなぜかできない。
    with fade

    # 雨を表示
    # show rain_back at rain_fade
    # 記述は CH_00_effects.rpy へ
    show rain_front at rain_fade 
    pause 1.0

    narrator_arrow "フロントガラス越しに、改めてペンションを見る。\n"
    extend "……新しい。\n"
    extend "正直、もっと古びた山小屋みたいなのを想像していた。\n"
    $ ctc_mode = "page"
    extend "けれど目の前にあるのは、洗練された木造建築だった。\n"

    narrator_arrow "大きなガラス窓。\n"
    extend "深いブラウンの外壁。\n"
    extend "軒下には間接照明が仕込まれていて、雨粒がそこに淡く照らされている。\n"
    extend "曇天なのに、暗くない。\n"
    $ ctc_mode = "page"
    extend "ガラスに反射する光が、ちょっとだけ幻想的だ。\n"

    narrator_arrow "「思ったより、全然おしゃれだよね」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "[heroine['first']]が、話しながらスマホで一枚撮る。\n"
    extend "「元はもっと古いペンションだったらしいよ。"
    extend "オーナーさんが買い取って、全部リノベーションしたって」\n"
    $ ctc_mode = "page"
    extend "「へえ……」\n"

    narrator_arrow "もっとこう、\n"
    extend "ギシギシ鳴る階段とか、\n"
    extend "照明が一つ切れてる廊下とか、\n"
    $ ctc_mode = "page"
    extend "そういうのを期待していたんだけど。\n"

    narrator_arrow "「探偵ものなのに、おしゃれすぎないか？\n"
    extend "こんなにオープンだと犯罪なんて起こらなそうだ」\n"
    extend "「なにそれ」\n"
    extend "[heroine['first']]がくすっと笑う。\n"
    extend "「ガラス張りの密室事件？」\n"
    extend "「密室じゃないな、それ」\n"
    $ ctc_mode = "page"
    extend "僕もつられて笑う。\n"

    # 雨の追加　二つ重ね掛け
    show rain_back at rain_fade

    narrator_arrow "そのとき、雨脚が少し強まった。\n"
    extend "屋根を打つ音が、さっきよりもはっきり聞こえる。\n"
    extend "「あ」\n"
    extend "[heroine['first']]が空を見上げる。\n"
    extend "「雨、強くなってきたね」\n"
    extend "「さっきより本気出してきてる」\n"
    $ ctc_mode = "page"
    extend "僕はドアノブに手をかけて――止まった。\n"

    narrator_arrow "あれ？"
    extend "……ない。\n"
    extend "「どうしたの？」\n"
    extend "「傘……{w=0.3}忘れたかも」\n"
    $ ctc_mode = "page"
    extend "僕は天井を仰ぐ。\n"

    narrator_arrow "どうかしてる。\n"
    extend "六月の山に行くのに、油断しすぎだ。\n"
    extend "しかし\n"
    extend "「どうせこの雨じゃ外観撮影なんて無理よ」\n"
    extend "[heroine['first']]が窓の外を見ながら言う。\n"
    extend "確かに。\n"
    extend "この雨なら、たとえ傘があってもカメラを出した瞬間に終了だ。\n"
    extend "まあ、今日はロケハンだ。\n"
    extend "下見だ。\n"
    extend "いきなり全部撮る必要はない。\n"
    $ ctc_mode = "page"
    extend "……と、自分に言い聞かせる。\n"

    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.3 
    play sound "audio/se/車のドアを閉める.mp3"
    pause 0.3 
    # sil_fadein をいれたら影絵がフェードインするようにしています（CH_00_sil_transforms.rpy）
    show sil_bg_pension_front at sil_center, sil_fadein 

    narrator_arrow "車のドアを開けると、ひんやりした空気が頬に触れた。\n"
    extend "雨は細かい粒になっていて、すぐに身体をじんわり濡らしていく。\n"
    extend "「チェックイン、{w=0.3}十五時からだよね」\n"
    extend "「うん。{w=0.3}ちょうどいい時間」\n"
    extend "時計を見ると、もう数分で十五時だ。\n"
    extend "「とりあえず中入ろう。"
    extend "濡れる前に」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]が隣に並ぶ。\n"

    narrator_arrow "「走る？」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]が言う。\n"

    $ choice_comment = "僕は……"
    menu:

        "１　「よし！ダッシュだ」僕は走りだした。":
            $ flag_arrival = "run"
        "２　「走ったら滑るだろ」となるべくゆっくり歩く。":
            $ flag_arrival = "walk"
        "３　「いや、ここは慎重に行こう」と少し様子を見る。":
            $ flag_arrival = "wait"

    $ choice_comment = ""  

    if flag_arrival == "run":
        narrator_arrow "「よし！ダッシュだ」\n"
        extend "「え、{w=0.3}ちょっと、{w=0.3}危ないよ」\n"
        extend "[heroine['first']]の静止を聞かずに僕は走りだした。\n"
        extend "思い切り踏み込んだ、{w=0.3}その時。\n"
        extend "「うわっ」\n"
        extend "バランスを崩しかけて、なんとか踏みとどまる。\n"
        $ ctc_mode = "page"
        extend "心臓が一拍遅れて跳ねた。\n"

        narrator_arrow "「ほら言ったじゃん」\n"
        extend "後ろから、呆れたような声。\n"
        extend "振り返ると、唯が笑いながらついてきている。\n"
        extend "「だから危ないって。{w=0.3}ちょっとぐらい濡れてもいいじゃん。{w=0.3}ゆっくり行こ？」\n"
        extend "「……はい」\n"
        $ ctc_mode = "page"
        extend "結局、慎重に歩いていくことにする。\n"


    elif flag_arrival == "walk":
    
        narrator_arrow "「いや、{w=0.3}走ったら滑るだろ」\n"
        extend "僕は、なるべくゆっくり歩いていく。\n"
        extend "しかしその直後、{w=0.3}僕の足が少しだけ滑った。\n"
        extend "「[player['first']]くん、{w=0.3}大丈夫？」\n"
        extend "「……セーフ」\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]が笑う。\n"

    else:
        narrator_arrow "「いや、{w=0.3}ここは慎重に行こう」\n"
        extend "隣で、唯が首をかしげる。\n"
        extend "「慎重って？」\n"
        extend "「……雨が収まるまで、しばらく待つ」\n"
        $ ctc_mode = "page"
        extend "「入口、{w=0.3}すぐそこだよ？」\n"
        
        narrator_arrow "唯が、半歩だけ前に出る。\n"
        extend "確かに、玄関の屋根までは数メートルもない。\n"
        extend "その間にも、雨は容赦なく降り続いている。\n"
        extend "最初は気にならなかった雨粒が、じわじわと肩や袖に染み込んでくる。\n"
        $ ctc_mode = "page"
        extend "髪の先から、冷たい水滴が落ちる。\n"

        narrator_arrow  "「……」\n"
        extend "言葉が続かないまま、{w=0.5}数秒。\n"
        extend "「……いくか」\n"
        $ ctc_mode = "page"
        extend "「でしょ？」\n"

    # フェードアウト この方法だと影絵を消してから画像を消すので少し感じが変わる（CH_00_sil_transforms.rpy）
    show sil_bg_pension_front at sil_center, sil_fadeout 
    pause 0.4
    hide sil_bg_pension_front # そして必ず消す記述を置いてください

    pause 0.4
    scene black
    with dissolve
    jump CH_03_pension_entrance

# -----------------------------------------------------------------------
    # 影絵を消す
    # hide sil_bg_pension_front

    # scene bg_pension_front_02 at fullscreen_bg
    # show sil_bg_pension_front at sil_center
    # with fade
    # 画像と一緒に書けば影絵も一緒にフェードインしてくれます。
    
    # scene test2 at fullscreen_bg
    # with fade
    # hide sil_青
    # こう外に書くと影絵はフェードアウトしてくれるようです。
