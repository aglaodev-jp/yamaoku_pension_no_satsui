label CH_10_last_scene:
    window hide

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_last_scene_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "朝、{w=0.3}カーテンの隙間から明るい光が差し込んでいる。\n"
    extend "僕は体を起こして、{w=0.3}窓の外を見た。\n"
    extend "空はすっかり晴れ渡っていた。\n"
    extend "雨に濡れていた森も、{w=0.3}朝の光の中で静かに輝いている。\n"
    extend "「……晴れてる」\n"
    extend "昨日とはまるで別の世界だった。\n"
    extend "隣で[heroine['first']]も目を覚ましたらしく、{w=0.3}ぼんやりした声で言う。\n"
    extend "「ほんとだね……」\n"
    $ ctc_mode = "page"
    extend "しばらく二人で窓の外を眺めていた。\n"

    scene black
    with Dissolve(1.0)

    pause 1.8
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    scene bg_last_scene_02 at fullscreen_bg
    with fade

    narrator_arrow "身支度を済ませ部屋を出ると、\n"
    extend "「おはようございますー！」\n"
    extend "どこかから元気な声が聞こえる。\n"
    extend "スタッフらしい人たちが、廊下を忙しそうに行き来していた。\n"
    extend "シーツの束を抱えて走る人。\n"
    extend "掃除機をかけている人。\n"
    extend "昨日、あれほど人の気配がなかったのが嘘みたいだ。\n"
    extend "「……なんか、{w=0.3}もう普通の宿だね」\n"
    extend "[heroine['first']]が小さく笑う。\n"
    extend "「うん」\n"
    $ ctc_mode = "page"
    extend "僕も思わず笑ってしまった。\n"

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_last_scene_03 at fullscreen_bg
    with fade

    narrator_arrow "ロビーに降りると、さらに賑やかだった。\n"
    extend "売店のシャッターが開きかけていて、中にスタッフが数人で商品を忙しなく運んでは陳列している。\n"
    extend "カウンターの横には、黒板の立て看板が立てられていた。\n"
    $ ctc_mode = "page"
    extend "大きな文字でこう書かれている。\n"

    narrator_arrow "{cps=60}\n{nw}"
    extend "**WELCOME！！\n{nw}"
    extend "○○大学 登山サークル御一行様**\n{nw}"
    extend "{/cps}\n"
    extend "「……団体くるんだ」\n"
    extend "[heroine['first']]が黒板を見ながら言う。\n"
    $ ctc_mode = "page"
    extend "なんだか、{w=0.3}昨日の雰囲気から、{w=0.3}急に現実に戻されていくようだった。\n"

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_pension_entrance_04 at fullscreen_bg
    with fade

    narrator_arrow "チェックアウトは、カウンターの端に置かれていた小さな木箱に鍵を入れるだけ。\n"
    extend "**KEY DROP**\n"
    extend "「鍵、ここだって」\n"
    extend "僕は部屋の鍵を箱に入れた。\n"
    play sound "audio/se/コーヒーのソーサーを置く.mp3" 
    extend "コトン、{w=0.3}と鳴る小さな音で本当にこの旅行が終わった気がした。\n"
    $ ctc_mode = "page"
    extend "なんだかあっけないもんだな。{w=0.5}\n"

    stop music fadeout 1.5
    scene black
    with Dissolve(1.0)

    pause 1.8

    play music "audio/se/軽井沢の野鳥たち2.mp3" fadein 1.5
    pause 0.3
    scene bg_last_scene_04 at fullscreen_bg
    with fade

    narrator_arrow "玄関を出ると、外は朝の空気でひんやりしていた。\n"
    extend "昨日の雨が嘘みたいに、空はきれいに晴れている。\n"
    extend "僕はスマホを取り出した。\n"
    extend "「せっかくだし外観ちょっと撮っておく？」\n"
    extend "「うん！」\n"

    # ==== フラグ分岐 ====================================================

    if flag_seen_shadow and flag_lobby_kino:

        narrator_arrow "あれ？{w=0.3}何か忘れている気がする……\n"
        extend "ああ、{w=0.3}そうだ\n"
        extend "「そういえばさ、{w=0.3}木下さん見なかった？{w=0.3}まだ寝てんのかな」\n"
        extend "「知らない！」\n"
        extend "[heroine['first']]は、そっけなく言い切るとすぐに視線を逸らした。\n"
        extend "どうやら、昨日の一件がまだ尾を引いているらしい。\n"
        $ ctc_mode = "page"
        extend "まあ……無理もないか。\n"

        narrator_arrow "「ほら早く写真撮って！{w=0.3}ポーズ取ってるんだから」\n"
        extend "「はいはい」\n"
        extend "メッセージも来ていないし……。\n"
        extend "あとで一応、連絡だけ入れておくか。\n"
        extend "僕は気を取り直して、カメラを構え直した。\n"


    else:
        extend "[heroine['first']]はペンションの前に立つと、くるっとこちらを振り向いた。\n"
        extend "「こんな感じ？」\n"
        extend "「いいね、エンドロールとかに使えそう」\n"

    # ====================================================================

    $ ctc_mode = "page"
    extend "しばらく二人で最後の撮影。\n"

    scene black
    with fade

    narrator_arrow "「あと最後に、{w=0.3}もう一つ」\n"
    extend "「なに？」\n"
    extend "「記念写真！」\n"
    extend "[heroine['first']]が楽しげに笑う。\n"
    $ ctc_mode = "page"
    extend "僕たちはペンションを背に並ぶ。\n"

    # ルートチェック２
    jump route_check_2

label route_check_2:

    if flag_seen_shadow and flag_lobby_kino:
        jump last_scene_kino
    else:
        jump last_scene_samo

# -----------------------------------------------------------------------

label last_scene_samo:
    window hide

    scene bg_last_scene_04 at fullscreen_bg
    with fade

    narrator_arrow "「これくらいで入るかな」\n"
    extend "画面をのぞき込むうちに、{w=0.3}自然と二人の距離が少し縮まる。\n"
    show sil_last_scene_01 at sil_center, sil_fadein
    extend "肩が、{w=0.3}軽く触れる。\n"
    extend "そのとき、{w=0.3}ふと思った。\n"
    $ ctc_mode = "page"
    extend "いつも写真を撮る距離よりも少しだけ近くなったような。\n"

    show sil_last_scene_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_last_scene_01
    scene black
    with fade
    pause 0.8

    narrator_arrow "「OK!」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    pause 0.4
    play music "audio/bgm/ドラマティック・シティ.mp3"
    extend "シャッターを切る。\n"
    extend "[heroine['first']]と付き合ってから、{w=0.3}初めての旅行。\n"
    extend "昨日はいろいろあったけれど——{w=0.5}また少しだけ、[heroine['first']]と近づけたのかな。\n"
    $ ctc_mode = "page"
    extend "雨上がりの朝の光の中で、{w=0.3}濡れたペンションの壁がやわらかく光っていた。\n"

    pause 0.3
    scene bg_last_scene_04 at fullscreen_bg
    with fade
    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.3

    narrator_arrow "車に乗り込む前、[heroine['first']]がもう一度ペンションを振り返った。\n"
    extend "「なんかさ、{w=0.3}昨日はちょっと怖かったけどさ、{w=0.3}楽しかったね、{w=0.3}このペンション」\n"
    extend "「また来る？」\n"
    extend "「うん」\n"
    extend "[heroine['first']]は少し考えてから言った。\n"
    extend "「今度はゆっくり泊まりたい」\n"
    extend "少しだけ、間があく。\n"
    extend "「……撮影じゃなくて、{w=0.5}旅行で！」\n"
    $ ctc_mode = "page"
    extend "「いいね！」\n"

    scene black
    with fade
    pause 0.3
    play sound "audio/se/車のドアを閉める.mp3"
    pause 0.3
    play sound "audio/se/車のエンジンをかける2.mp3"
    narrator_arrow "僕は、エンジンをかける。\n"

    stop sound
    pause 0.8

    scene bg_last_scene_06 at fullscreen_bg
    with fade
    narrator_arrow "初めての旅行で、{w=0.3}僕はずっと少しだけ肩に力が入っていた。\n"
    extend "でもきっと、{w=0.3}焦る必要なんてないんだと思う。\n"
    extend "こうして、{w=0.3}同じ時間を過ごしていけばいい。\n"
    extend "バックミラーの中で、{w=0.3}ペンションがだんだん小さくなっていく。\n"
    $ ctc_mode = "page"
    extend "そう、{w=0.3}ゆっくりと。\n"

    scene black
    with fade
    pause 0.8

    $ renpy.movie_cutscene("movies/movie_10.webm", stop_music=False) # 音楽も流す
    scene black
    with Dissolve(1.0)
    pause 1.0

    # エンディングAフラグ
    $ mark_ending("A")
    # エンディングタイプ "samoyed"　このフラグでエンディングロールの背景を分岐
    $ ending_type = "samoyed"

    # スタッフロール（背景は残る／ENDで停止／クリックでフェードアウト＆音楽フェードアウト）
    call screen credits_scroll(scroll_time=90.0, fade_time=1.0, music_fade=2.0)

    # 余韻：必要ならここで黒に落としてからタイトルへ
    scene black
    with Dissolve(1.0)
    pause 0.8

    # タイトル画面へ
    $ renpy.full_restart()

# -----------------------------------------------------------------------

label last_scene_kino:
    window hide

    scene bg_last_scene_04 at fullscreen_bg
    with fade

    narrator_arrow "「これくらいで入るかな」\n"
    extend "画面をのぞき込むうちに、{w=0.3}自然と二人の距離が少し縮まる。\n"
    show sil_last_scene_01 at sil_center, sil_fadein
    extend "肩が、{w=0.3}軽く触れる。\n"
    extend "そのとき――\n"
    $ ctc_mode = "page"
    extend "ぬっ、とフレームの中に第三の顔が入り込んできた。\n"

    show sil_last_scene_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_last_scene_01
    show sil_last_scene_02 at sil_center, sil_fadein

    narrator_arrow "「はいチーズ！！」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "カシャ。\n"
    extend "シャッターが切れた。\n"
    extend "「……」\n"
    extend "「……」\n"
    extend "僕と[heroine['first']]は同時に振り返る。\n"
    $ ctc_mode = "page"
    extend "そこには――\n"

    show sil_last_scene_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_last_scene_02
    show sil_last_scene_03 at sil_center, sil_fadein

    narrator_arrow "「水臭いじゃないか君たち。"
    extend "私を差し置いて記念写真だなんて」\n"
    $ ctc_mode = "page"
    extend "満面の笑顔の木下さんが立っていた。\n"

    narrator_arrow "「木下さん！！{w=0.3}いたんなら言ってくださいよ！」\n"
    extend "僕は思わず言う。\n"
    extend "「びっくりしましたよ」\n"
    extend "[heroine['first']]も困ったように笑う。\n"
    extend "「いやーでもさ、{w=0.3}いい思い出になったでしょう？"
    extend "これぞ青春の1ページだよな！」\n"
    extend "と、{w=0.3}木下さんは、また「あっはっは」と笑う。\n"
    $ ctc_mode = "page"
    extend "……本当になんなんだ、{w=0.3}この人は。\n"

    stop music fadeout 1.5
    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_last_scene_05 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "車に向かう。\n"
    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.8

    extend "僕がドアを開けようとしたそのとき、{w=0.3}後部座席のドアが先に開いた。\n"
    show sil_last_scene_04 at sil_center, sil_fadein
    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.8
    play sound "audio/se/車のドアを閉める.mp3"
    pause 0.8
    extend "「よいしょっと」\n"
    extend "木下さんが当然のように乗り込む。\n"
    show sil_last_scene_05 at sil_center, sil_fadein
    play sound "audio/se/車のドアを閉める.mp3"
    pause 0.8
    play sound "audio/se/車のエンジンをかける2.mp3"
    pause 0.8
    $ renpy.music.set_volume(0.8, channel="music")
    play music "audio/se/車のアイドリング1.mp3"
    extend "僕はゆっくり振り向いた。\n"
    extend "「木下さん」\n"
    extend "「ん？」\n"
    extend "「なんで乗ってるんですか」\n"
    $ ctc_mode = "page"
    extend "木下さんは真顔で言った。\n"


    narrator_arrow "「いや、{w=0.3}だって、{w=0.3}駅まで送ってもらおうかなって。\n"
    extend "タクシーできたから帰りの足ないんだよね……。\n"
    extend "あれぇ？まさか先輩置いてくつもりかい？」\n"
    $ ctc_mode = "page"
    extend "僕は、思いっきりため息をついた。\n"


    narrator_arrow "木下さんは軽く手を上げた。\n"
    extend "「これでも、昨日は悪かったと思ってるんだよ」\n"
    extend "「……本当ですか？」\n"
    extend "僕は訝しむ。\n"
    extend "「ほんとほんと。"
    extend "いやぁ、{w=0.3}ちょっと湯あたりして全裸で倒れてただけなんだけどさ、{w=0.3}結果的に大騒ぎになっちゃったじゃない？」\n"
    $ ctc_mode = "page"
    extend "やっぱり悪びれた様子はない。\n"


    narrator_arrow "木下さんは顎をさすりながら続ける。\n"
    extend "「あれはいいパンチだった。{w=0.5}映研の将来は安泰だね」\n"
    play sound "audio/se/車のドアを開ける.mp3"
    pause 0.3
    play sound "audio/se/車のドアを閉める.mp3"
    pause 0.3
    show sil_last_scene_06 at sil_center, sil_fadein
    extend "「褒めてませんよね。{w=0.3}それ」\n"
    $ ctc_mode = "page"
    extend "丁度、助手席に乗り終えた[heroine['first']]が小さくツッコむ。\n"

    narrator_arrow "木下さんは、さも申し訳なさそうに言う。\n"
    extend "「お詫びにってわけでもないけどさ、{w=0.3}朝飯おごるよ。"
    extend "いい店知ってるんだ。"
    extend "……この辺で有名な山小屋レストランなんだけどさぁ」\n"
    extend "「そこ昨日行きましたよ」\n"
    extend "「知ってた？{w=0.3}あっはっは！」{w=0.5}と笑いながら木下さんは続ける。\n"
    extend "「いや、{w=0.3}あそこモーニングもやっててさ。"
    $ ctc_mode = "page"
    extend "パンとコーヒーがめちゃくちゃうまいらしいのよ～」\n"


    narrator_arrow "[heroine['first']]の目がぱっと輝き振り返る。\n"
    extend "「ほんとですか！？」\n"
    extend "「ほんとほんと」\n"
    extend "「本当にっ！{w=0.3}木下さんのおごりですよ！」\n"
    extend "「もちろん！{w=0.3}全力でおごる」\n"
    extend "「やった！」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]が嬉しそうに笑う。\n"

    narrator_arrow "僕はバックミラー越しに木下さんを見る。\n"
    extend "……まあ、昨日の騒動を思えばそれくらいはしてもらってもいい気がする。\n"
    extend "「じゃあ、遠慮なくごちそうになります」\n"
    $ ctc_mode = "page"
    extend "車はゆっくりペンションを離れた。\n"


    show sil_last_scene_04 at sil_center, sil_fadeout
    show sil_last_scene_06 at sil_center, sil_fadeout
    show sil_last_scene_05 at sil_center, sil_fadeout
    pause 0.4
    hide sil_last_scene_04
    hide sil_last_scene_05
    hide sil_last_scene_06

    stop music fadeout 1.0

    scene black
    with fade
    pause 0.8

    $ renpy.movie_cutscene("movies/movie_10.webm") 

    scene black
    with fade
    pause 0.8
    scene bg_last_scene_06 at fullscreen_bg
    with fade
    pause 0.8

    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/bgm/ドラマティック・シティ.mp3"
    pause 0.8

    narrator_arrow "バックミラーの中でペンションがだんだん小さくなる。\n"
    extend "[heroine['first']]と付き合ってから、{w=0.3}初めての旅行。\n"
    $ ctc_mode = "page"
    extend "昨日はいろいろあったけれど——{w=0.5}また少しだけ、[heroine['first']]と近づけたのかな。\n"

    narrator_arrow "[heroine['first']]がペンションを振り返りながら言う。\n"
    extend "「楽しかったね、{w=0.3}ペンション」\n"
    extend "「また来る？」\n"
    extend "「うん」\n"
    extend "[heroine['first']]は少し考えてから言った。\n"
    extend "「今度はゆっくり泊まりたい」\n"
    extend "少しだけ、{w=0.3}間があく。\n"
    extend "「……撮影じゃなくて、{w=0.5}旅行で！」\n"
    $ ctc_mode = "page"
    extend "「そうだね」\n"

    scene bg_last_scene_04 at fullscreen_bg
    with fade

    narrator_arrow "今度は、{w=0.3}ちゃんとした旅行でまた来たい。\n"
    extend "ゆっくり景色を見て、{w=0.3}のんびり泊まって、{w=0.3}普通に朝を迎えて。\n"
    $ ctc_mode = "page"
    extend "そのころには、{w=0.3}もっと[heroine['first']]と仲良くなれてたらいいな。\n"

    scene black
    with fade

    stop music
    pause 1.0

    narrator_arrow "「いやぁ～{w=0.3}いい車だねぇ、{w=0.3}[player['last']]君。"
    extend "君のお兄さんは、{w=0.3}さぞハイキャリなんだろうな～。"
    extend "……今度紹介してよ！」{w=0.8}\n"
    extend "もちろん、{w=0.8}今度は、{w=0.8}木下さん抜きで。{w=1.8}{nw}\n"

    play music "audio/bgm/Hello,_world.mp3" noloop # noloopでループしない。

    pause 3.0

    # エンディングBフラグ
    $ mark_ending("B")
    # エンディングタイプ "kinoshita"　このフラグでエンディングロールの背景を分岐
    $ ending_type = "kinoshita"

    # スタッフロール（背景は残る／ENDで停止／クリックでフェードアウト＆音楽フェードアウト）
    call screen credits_scroll(scroll_time=70.0, fade_time=1.0, music_fade=2.0)

    # 余韻：必要ならここで黒に落としてからタイトルへ
    scene black
    with Dissolve(1.0)
    pause 0.8

    # タイトル画面へ
    $ renpy.full_restart()