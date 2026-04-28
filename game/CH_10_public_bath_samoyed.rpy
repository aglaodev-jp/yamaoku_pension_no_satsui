label CH_10_public_bath_samoyed:
    window hide

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_scream_02 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    play ambient_se "audio/se/雨の音_2.mp3"
    pause 0.8

    show sil_public_bath_01 at sil_center, sil_fadein

    narrator_arrow "部屋を出て、吹き抜けの階段からロビーへ降りる。\n"
    extend "やっぱり人の気配はない。\n"
    extend "昼間と同じ場所のはずなのに、夜になると妙に静かな雰囲気。\n"
    extend "夜になっても相変わらず館内BGMが流れているが、{w=0.3}逆にそれが余計に孤独を感じさせる。\n"
    $ ctc_mode = "page"
    extend "僕は足早にロビーを抜け、大浴場のある一階の廊下へ向かった。\n"

    show sil_public_bath_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_01

    stop music fadeout 1.5
    stop ambient_se fadeout 1.5
    pause 0.4
    scene black
    with fade
    pause 0.4
    scene bg_public_bath_01 at fullscreen_bg
    with fade

    $ renpy.pause(0.5)
    play music "audio/se/エアコン.mp3" volume 0.4

    narrator_arrow "大浴場の前に掛かった暖簾が、空調の風に揺れて、わずかに揺れていた。\n"
    scene bg_public_bath_02a at fullscreen_bg
    with fade
    extend "脱衣所にも、{w=0.3}人はいない。\n"
    extend "まあ、{w=0.3}今日の大浴場は予約制だから、{w=0.3}当然か。\n"
    extend "ロッカーの扉が整然と並ぶ、{w=0.3}静かな空間だ。\n"
    $ ctc_mode = "page"
    extend "このペンションに来てから全く人を見ないので誰もいないかのように感じるが、{w=0.3}それでもきちんとお風呂が準備されているあたり、{w=0.3}どこかにスタッフさんはいるんだろうか。\n"

    pause 0.4
    scene black
    with fade
    pause 0.4

    narrator_arrow "服を脱ぎ、浴室の扉を開ける。\n"

    stop music
    play sound "audio/se/ドアを開ける1.mp3"
    pause 0.5
    scene bg_public_bath_03 at fullscreen_bg
    with fade
    play music "audio/se/お風呂に水を入れる.mp3"
    play ambient_se "audio/se/お風呂でチャポン.mp3"

    narrator_arrow "湯気が、ふわっと広がった。\n"
    extend "浴槽は丸い石組みの風呂。\n"
    extend "端からは小さな滝のように湯が流れ落ちている。\n"
    extend "床と壁は石と木。\n"
    extend "山の温泉旅館みたいな雰囲気。\n"
    $ ctc_mode = "page"
    extend "「大浴場」{w=0.3}というには少しこじんまりしているが、{w=0.3}ペンションにしては妙に本格的だ。\n"

    pause 0.5
    scene bg_public_bath_06 at fullscreen_bg
    with fade

    narrator_arrow "正面には大きな窓。\n"
    extend "昼間ならきっといい景色なんだろうけど、{w=0.3}外は真っ暗で傍の木々に雨粒が流れているのが見えるだけだった。\n"
    pause 0.5
    scene bg_public_bath_04 at fullscreen_bg
    with dissolve
    extend "壁には鏡が並び、{w=0.3}その前にシャワーがいくつも付いている。\n"
    $ ctc_mode = "page"
    extend "椅子や桶もきれいに揃えられていて、{w=0.3}まだ新しい。\n"

    pause 0.4
    scene black
    with fade
    pause 0.4

    narrator_arrow "「……贅沢だな」\n"
    extend "思わず呟く。\n"
    $ ctc_mode = "page"
    extend "完全に貸し切り状態だ。\n"

    stop music
    stop ambient_se

    # ムービー（クリックでスキップ可能）
    $ renpy.movie_cutscene("movies/movie_08.webm", stop_music=True)

    # 終わりの余韻
    pause 0.2

    # 一度暗転
    scene black
    with dissolve

    play music "audio/se/お風呂に水を入れる.mp3"
    play ambient_se "audio/se/お風呂でチャポン.mp3"

    narrator_arrow "シャワーで体を流し、{w=0.3}湯船に足を入れる。\n"
    $ ctc_mode = "page"
    extend "じんわりと温かさが広がる。\n"

    pause 0.5
    scene bg_public_bath_06 at fullscreen_bg
    with dissolve

    narrator_arrow "「ふう…」\n"
    extend "慣れない運転。\n"
    extend "慌ただしい撮影。\n"
    extend "初めての彼女との旅行――\n"
    extend "思っていた以上に、{w=0.3}疲れていたらしい。\n"
    $ ctc_mode = "page"
    extend "肩まで湯に浸かると、今日一日の疲れがゆっくり溶けていく。\n"


    narrator_arrow "外では、{w=0.3}まだ雨が降り続いている。\n"
    extend "今回の旅行。\n"
    extend "もともとは、映画の撮影準備のためのロケハンだった。\n"
    extend "けれど――\n"
    extend "なんだか、普通の旅行みたいでもある。\n"
    extend "雨の山道。\n"
    extend "静かなペンション。\n"
    extend "[heroine['first']]と二人きり。\n"

    # 人影を見た時だけ表示するテキスト
    if flag_seen_shadow:
        extend "そして――\n"
        extend "あの人影の話。\n"

    extend "思考がグルグルとループする。\n"
    $ ctc_mode = "page"
    extend "湯船に揺れる湯気をぼんやり見ながら、ふとひとつの考えが頭をよぎる。\n"

    $ choice_comment = "僕は……"

    menu:
        "１　今回の映画の撮影について考える":
            $ choice_comment = ""
            jump CH_10a_public_bath_samoyed

        "２　[heroine['first']]のことを考える":
            $ choice_comment = ""
            jump CH_10b_public_bath_samoyed

        "３　[heroine['first']]が見た人影のことを考える" if flag_seen_shadow: # 人影を見た場合のみ出現
            $ choice_comment = ""
            jump CH_10c_public_bath_samoyed

label CH_10a_public_bath_samoyed:
    window hide

    pause 0.4
    scene black
    with fade
    pause 0.8
    scene bg_public_bath_17 at fullscreen_bg
    with fade

    narrator_arrow "このペンション、{w=0.3}かなりいいよなあ。\n"
    $ ctc_mode = "page"
    extend "映画の舞台として、{w=0.3}雰囲気は申し分ない。\n"

    narrator_arrow "……ただ、{w=0.3}タブレットでのチェックインとか\n"
    extend "ロビーの壁に掛かっていたデジタルサイネージとか\n"
    extend "あのイミテーションの暖炉とか\n"
    extend "妙に最新設備が混ざっている。\n"
    $ ctc_mode = "page"
    extend "ぱっと見は山奥のペンションらしい、{w=0.3}いい雰囲気なんだけど。\n"

    narrator_arrow "「……ちょっと興が削がれるよな」\n"
    extend "思わず小さく笑ってしまう。\n"
    extend "もちろん、{w=0.3}宿としては便利なんだろうけど。\n"
    $ ctc_mode = "page"
    extend "映画の世界観として考えると、{w=0.3}ああいう現代的な機械はどうしても目立ってしまう。\n"


    narrator_arrow "……まあ。{w=0.5}そのへんは、{w=0.3}木下さんの仕事だ。\n"
    extend "ロケ地を見つけてきたのも、{w=0.3}脚本を書いているのも、{w=0.3}サークル代表の木下さんだ。\n"
    $ ctc_mode = "page"
    extend "うまくやってくれるだろう。\n"

    scene black
    with fade
    pause 0.4
    narrator_arrow "卒業記念か……{w=0.5}いい映画になるといいな。\n"
    $ ctc_mode = "page"
    extend "僕は漠然と思っていた。\n"

    pause 0.8
    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    jump CH_11_scream

label CH_10b_public_bath_samoyed:
    window hide

    scene bg_public_bath_08 at fullscreen_bg
    with fade
    pause 0.8
    show sil_public_bath_16 at sil_center, sil_fadein

    if flag_lobby_photo_taken:
        narrator_arrow "[heroine['first']]のことを考える。\n"
        extend "湯船の中で、今日一日のことを思い返す。\n"
        extend "雨の山道を走って、\n"
        extend "ペンションに着いて、\n"
        $ ctc_mode = "page"
        extend "二人でロケハンをして――\n"


        narrator_arrow "撮影は正直、{w=0.3}思っていたより大変だった。\n"
        extend "カメラを持って歩き回ったり、\n"
        extend "構図を試したり、\n"
        $ ctc_mode = "page"
        extend "同じカットを何度も撮り直したり。\n"


        narrator_arrow "それでも\n"
        extend "「楽しかったな」\n"
        extend "思わず、小さく呟く。\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]もずっと楽しそうだった。\n"

    narrator_arrow "付き合い始めて、{w=0.3}もう半年くらい。\n"
    extend "サークルの仲間として一緒にいる時間の方が長かったからか、{w=0.3}今でもどこか友達みたいな感覚がある。\n"
    extend "それが、{w=0.3}ちょうどいい距離だった。\n"
    extend "けど――\n"
    $ ctc_mode = "page"
    extend "ふと、{w=0.3}あることに気づく。\n"

    show sil_public_bath_16 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_16

    pause 0.4
    scene black
    with fade
    pause 0.8

    narrator_arrow "「……そういえば」\n"
    extend "今日、{w=0.3}僕たちはこのペンションに泊まるんだった。\n"
    extend "同じ部屋で。\n"
    extend "「……」\n"
    $ ctc_mode = "page"
    extend "湯気の中で、{w=0.3}思わず天井を見上げる。\n"

    scene bg_public_bath_17 at fullscreen_bg
    with fade

    narrator_arrow "今までもサークルのみんなで合宿みたいなことはあったけど、{w=0.3}こういう形で二人きりで泊まるのは初めてだ。\n"
    extend "また急に、意識してしまう。\n"
    extend "もし――\n"
    extend "もし、{w=0.3}自分に歯止めがかからなくなったらどうするんだろう。\n"
    $ ctc_mode = "page"
    extend "……いや、{w=0.3}それはさすがにないと思うけど。\n"

    narrator_arrow "でも逆に。\n"
    extend "[heroine['first']]の方から何か言われたら？\n"
    extend "「……いやいや」\n"
    extend "思わず小さく首を振る。\n"
    extend "考えすぎだ。\n"
    extend "[heroine['first']]はそういうタイプじゃない。\n"
    $ ctc_mode = "page"
    extend "……たぶん。\n"

    narrator_arrow "湯船の水面がゆらゆら揺れる。\n"
    extend "もし――\n"
    extend "これ以上の関係になったら。\n"
    extend "今みたいに気楽に笑い合える関係じゃなくなったりしないだろうか。\n"
    extend "友達みたいにくだらない話をして、{w=0.3}ふざけ合って。\n"
    $ ctc_mode = "page"
    extend "そんな時間がなくなったりしないだろうか。\n"

    narrator_arrow "「……」\n"
    extend "小さく息を吐く。\n"
    extend "……まあ。\n"
    extend "まだ何も起きてないのに、{w=0.3}考えすぎか。\n"
    $ ctc_mode = "page"
    extend "湯船に体を沈めながら、{w=0.3}僕は目を閉じた。\n"

    pause 0.4
    scene black
    with fade
    pause 0.8
    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    jump CH_11_scream

label CH_10c_public_bath_samoyed:
    window hide

    pause 0.4
    scene black
    with fade
    pause 0.8
    scene bg_public_bath_08 at fullscreen_bg
    with fade
    pause 0.8
    show sil_public_bath_16 at sil_center, sil_fadein

    narrator_arrow "[heroine['first']]が見たという、{w=0.3}あの人影。\n"
    extend "僕は見ていない。\n"
    extend "だから、{w=0.3}はっきりとは言えない。\n"
    extend "でも――\n"
    $ ctc_mode = "page"
    extend "あの時の[heroine['first']]の様子は、{w=0.3}冗談を言っている感じではなかった。\n"

    narrator_arrow "湯船の水面をぼんやり眺める。\n"
    extend "湯気がゆらゆらと揺れている。\n"
    $ ctc_mode = "page"
    extend "窓の外には、真っ暗な森。\n"

    narrator_arrow "……このペンション、{w=0.3}意外と大きかったよな。\n"
    extend "二階の客室は八室くらいだったけど、一階の廊下とかほかにも部屋がありそうだった。\n"
    extend "「……他の宿泊客かな？」\n"
    extend "ぽつりと呟く。\n"
    $ ctc_mode = "page"
    extend "そう考えるのが、一番自然な気がする。\n"


    narrator_arrow "ロビーでは誰も見なかったけど、{w=0.3}僕たちが来る前から泊まっている人が他にいた可能性だってある。\n"
    extend "あるいは、{w=0.3}スタッフさんかもしれない。\n"
    extend "清掃とか、{w=0.3}設備点検とか。\n"
    extend "この規模のペンションなら、数人くらいはいるだろう。\n"
    extend "――それなら、[heroine['first']]が見たのも説明はつく。\n"
    extend "……つく、{w=0.5}はずだ。\n"
    $ ctc_mode = "page"
    extend "湯気の向こうで、窓ガラスを雨粒が流れていく。\n"

    scene black
    stop music
    stop ambient_se

    narrator_arrow "その時。\n"
    extend "外の闇の中で、一瞬だけ、何かが動いた気がした。\n"

    pause 0.5
    scene bg_public_bath_06 at fullscreen_bg
    with fade
    narrator_arrow "「……？」\n"
    extend "思わず顔を上げる。\n"
    extend "けれど、{w=0.3}窓の外にはただ雨が降っているだけだった。\n"
    $ ctc_mode = "page"
    extend "森は真っ暗で、{w=0.3}何も見えない。\n"

    play music "audio/se/お風呂に水を入れる.mp3" fadein 1.5
    play ambient_se "audio/se/お風呂でチャポン.mp3" fadein 1.5

    narrator_arrow "「……気のせいか」\n"
    extend "自分でそう言って、{w=0.3}小さく息を吐く。\n"
    extend "こんな山の中だ。\n"
    extend "鹿とか、{w=0.3}猿とか、{w=0.3}野生動物がいてもおかしくない。\n"
    extend "そういうことにしておこう。\n"
    $ ctc_mode = "page"
    extend "きちんと鍵を閉めて、{w=0.3}寝ちゃえばへいきさ。\n"

    pause 0.4
    scene black
    with fade
    pause 0.8
    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    jump CH_11_scream