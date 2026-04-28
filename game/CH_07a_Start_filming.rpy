label CH_07a_Start_filming:
    window hide

    $ flag_lobby_photo_taken = True # ロビーで撮影フラグ（CH_00_flag.rpy）
    $ flag_a_Start_filming = True
    pause 0.4
    scene bg_to_the_lobby_01 at fullscreen_bg
    with fade
    show sil_a_start_filming_01 at sil_center, sil_fadein

    narrator_arrow "「まずはペンションを探検しながら撮ろうよ」\n"
    extend "「探検？」\n"
    extend "[heroine['first']]が顔を上げる。\n"
    extend "「せっかく来たんだしさ。"
    extend "館内を回りながら、使えそうな場所を探すんだ。\n"
    extend "これ、{w=0.3}どう？」\n"
    extend "「いいね！{w=0.3}まさにロケハンだね」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]も同意してくれた。\n"

    show sil_a_start_filming_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_01
    show sil_a_start_filming_02 at sil_center, sil_fadein

    narrator_arrow "「そうそう」\n"
    extend "[heroine['first']]は少し考えてから、にやっと笑った。\n"
    extend "「じゃあさ、{w=0.3}私が先に歩くから後ろから撮って」\n"
    extend "「なんで？」\n"
    extend "「被写体もあったほうが自然でしょ」\n"
    $ ctc_mode = "page"
    extend "ヒロイン気分で[heroine['first']]が映りたいだけなんじゃないかとも思ったが、{w=0.3}確かに一理ある。\n"

    show sil_a_start_filming_02 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_02


    narrator_arrow "「そうだな。"
    extend "じゃあ、{w=0.3}僕がカメラで使えそうなカットを押さえておこう」\n"
    extend "といっても本格的なものではなく、僕のスマホのカメラだ。"
    extend "しかし[heroine['first']]の気分が出るように、{w=0.3}それっぽくカメラを構えるふりをする。\n"
    show sil_a_start_filming_03 at sil_center, sil_fadein
    extend "「じゃ、{w=0.3}主演女優さん。{w=0.3}どうぞ」\n"
    extend "「はーい」\n"
    extend "[heroine['first']]は立ち上がり、{w=0.3}ロビーを歩き出す。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "僕はそれについていき、つぶさにシャッターを切っていった。\n"

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_to_the_lobby_05 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    show sil_a_start_filming_04 at sil_center, sil_fadein

    narrator_arrow "しばらくして、[heroine['first']]がテーブルの椅子を少し引いて座る。\n"
    extend "すかさず僕は、カメラを構える。\n"
    extend "「こういう雰囲気カット、{w=0.3}意外と使えるんだよね」\n"
    extend "「こういうの？」\n"
    extend "「そう、いいね。そのまま」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "そして、僕は何枚か写真を撮る。\n"

    show sil_a_start_filming_04 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_04
    scene bg_a_start_filming_01 at fullscreen_bg
    with fade
    show sil_a_start_filming_05 at sil_center, sil_fadein

    narrator_arrow "「入口のカットも欲しいな」\n"
    extend "[heroine['first']]がロビーのドアに近づき、軽く開いてみせる。\n"
    extend "「こんな感じ？」\n"
    extend "「うん、雰囲気出てる」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "そして、また数枚写真を撮る。\n"

    show sil_a_start_filming_05 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_05
    scene bg_to_the_lobby_06 at fullscreen_bg
    with fade
    show sil_a_start_filming_06 at sil_center, sil_fadein

    narrator_arrow "「まず階段から降りてきて……」\n"
    extend "[heroine['first']]が二階へ駆け上がる。\n"
    pause 0.4
    show sil_a_start_filming_06 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_06
    extend "「じゃあ行くよ」\n"
    extend "「はーい」\n"
    pause 0.4
    show sil_a_start_filming_07 at sil_center, sil_fadein
    extend "返事とともに、[heroine['first']]が階段をゆっくり降りてくる。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "そして、僕は写真を撮る。\n"

    pause 0.8
    show sil_a_start_filming_07 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_07
    scene black
    with fade

    narrator_arrow "「……なんだか旅行気分だね」\n"
    extend "「仕事です」\n"
    extend "「はいはい」\n"
    extend "様々なポーズで写真に写りたがる[heroine['first']]は、{w=0.3}やはり浮ついているように見える。\n"
    extend "でも、{w=0.3}そんな[heroine['first']]の姿をかわいいと思ってしまう。\n"
    $ ctc_mode = "page"
    extend "これは映画研究会のロケハンだと思いつつも、{w=0.3}僕はすっかり思い出作りを楽しんでいた。\n"

    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_a_start_filming_02 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "ロビーの奥にあるダイニングの扉へ向かう。\n"
    extend "取っ手を引いてみるが、扉は開かなかった。\n"
    extend "「閉まってるね」\n"
    extend "「今日は簡易宿泊で使わないんだろうな」\n"
    extend "「ここ雰囲気よさそうなのに」\n"
    extend "レストランの撮影も必要になりそうな気がするが、今はどうにもならない。\n"
    $ ctc_mode = "page"
    extend "ひとまず諦めることにした。\n"

    scene bg_to_the_lobby_04 at fullscreen_bg
    with fade

    narrator_arrow "[heroine['first']]は大きなガラス窓の方へ歩いていった。\n"
    extend "窓の向こうには、雨に濡れたウッドデッキが広がっている。\n"
    extend "丸いテーブルと椅子がいくつか並んでいるが、絶え間なく降る雨にすっかり濡れていた。\n"
    extend "照明に照らされた感じの雰囲気は悪くないが、とても外で撮影できる状況ではなかった。\n"
    extend "「晴れてたら、ここもいいロケーションだったのにね」\n"
    extend "「確かに」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "しかたなく、窓越しに数枚だけ写真を撮っておく。\n"

    scene bg_a_start_filming_03 at fullscreen_bg
    with fade

    narrator_arrow "ロビー横の廊下へ入る。\n"
    extend "木の床がまっすぐ奥まで続いていて、思ったより奥行きがある。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "僕は廊下の構図を何枚か撮影した。\n"
    extend "途中には小さな売店があるが、シャッターが下りていた。\n"
    extend "「完全オフシーズンだね」\n"
    $ ctc_mode = "page"
    extend "「ほんとだな」\n"


    scene bg_pension_entrance_04 at fullscreen_bg
    with fade


    narrator_arrow "廊下の先は、ついさっき僕たちが入ってきたフロントがあるあたりに通じていた。\n"
    extend "「この辺はさっき撮ったし……」\n"
    extend "「まあいいか」\n"
    extend "フロント周りは一通り見たので、いったんロビーへ戻ることにする。\n"
    $ ctc_mode = "page"
    extend "ロビーの吹き抜けの階段から、再び二階へ上がった。\n"


    scene bg_a_start_filming_04 at fullscreen_bg
    with fade

    narrator_arrow "二階の廊下。\n"
    extend "吹き抜け越しに、ロビーが見下ろせる。\n"
    show sil_a_start_filming_08 at sil_center, sil_fadein
    extend "「俯瞰から撮っておこうかな」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    pause 0.4
    play sound "audio/se/カメラのシャッター2.mp3"
    pause 0.4
    extend "僕は手すり越しにロビーを見下ろしながら何枚か撮影した。\n"
    extend "「わたし、{w=0.3}さっき撮ったよ」\n"
    extend "「あれ？{w=0.3}そうだっけ？」\n"
    $ ctc_mode = "page"
    extend "こうロケーションが多いと、どこを撮影したのかわからなくなるなぁ。\n"

    show sil_a_start_filming_08 at sil_center, sil_fadeout
    pause 0.4
    hide sil_a_start_filming_08
    scene bg_second_floor_03 at fullscreen_bg
    with fade

    narrator_arrow "廊下には客室のドアが並んでいる。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "廊下の奥の構図。\n"
    scene bg_second_floor_04 at fullscreen_bg
    with fade
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "ドアのアップ。\n"
    $ ctc_mode = "page"
    extend "いくつか試しながら撮影していく。\n"

    scene bg_scream_06 at fullscreen_bg
    with fade

    narrator_arrow "廊下の突き当りには、観音開きの大きな扉があった。\n"
    extend "「これ、{w=0.3}なんだろ」\n"
    extend "「掃除道具とか、{w=0.3}物置とか……{w=0.5}じゃない？」\n"
    extend "「ああ、{w=0.3}たしかに、{w=0.3}そんな感じかな」\n"
    extend "まあいいや、{w=0.3}これも写真にとっておこう。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    pause 0.4
    $ ctc_mode = "page"
    extend "特に気にせず、僕たちは反対側の廊下へ戻った。\n"

    scene bg_a_start_filming_05 at fullscreen_bg
    with fade

    narrator_arrow "吹き抜け側の壁にはいくつか絵画が飾られている。\n"
    extend "ペンションらしい、落ち着いた風景画だ。\n"
    extend "「これ、{w=0.3}いくらするんだろ？」\n"
    extend "僕は、とっさにつぶやいた。\n"
    extend "「セコイこと言わないの」\n"
    $ ctc_mode = "page"
    extend "軽く怒られる。\n"


    scene bg_a_start_filming_06 at fullscreen_bg
    with fade

    narrator_arrow "二階廊下の奥に、小さな扉がある。\n"
    extend "他の客室とは違い、その扉には細長い窓がはめ込まれていて、外の様子がうっすらと見えるようになっている。\n"
    extend "取っ手も丸いドアノブではなく、下に押し下げるレバーハンドルだ。\n"
    extend "「ここ、{w=0.3}外に出られるみたい。」\n"
    extend "[heroine['first']]がそっとガラス越しに外を覗き込む。\n"
    extend "窓の向こうには、細い通路のようなスペースと手すりが見えた。\n"
    $ ctc_mode = "page"
    extend "どうやら、外に張り出したバルコニーらしい。\n"

    narrator_arrow "「ちょっとだけ出てみようかな？」\n"
    extend "僕はレバーに手をかけた。\n"
    extend "「えー、{w=0.3}やめときなよ」\n"
    extend "「ちょっとだけ」\n"
    play sound "audio/se/ドアを開ける1.mp3"
    pause 0.8
    scene black
    with fade
    play music "audio/se/雨の音_2.mp3"
    play sound "audio/se/風が吹く1.mp3"
    $ ctc_mode = "page"
    extend "ドアを押すと、わずかに隙間が開き、ひんやりとした湿った空気と、はっきりとした雨音が流れ込んできた。\n"

    narrator_arrow "「ねえ、{w=0.3}やめてってば」\n"
    extend "[heroine['first']]が、少し強い口調で言う。\n"
    extend "「滑りそうだし、危ないって」\n"
    extend "確かに、隙間から見える床はすでに濡れていて風も思ったより強そうだ。\n"
    extend "「……まあ、{w=0.3}そうだな」\n"
    pause 0.8
    scene bg_a_start_filming_06 at fullscreen_bg
    with fade
    stop sound
    stop music
    play sound "audio/se/ドアを閉める1.mp3"
    pause 0.8
    play sound "audio/se/カメラのシャッター2.mp3"
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    play ambient_se "audio/se/雨の音_2.mp3"
    extend "ドアを閉めて、代わりに窓越しに軽く写真だけ撮っておく。\n"
    extend "「きっと晴れてたら、{w=0.3}眺めがいいんだろうなあ」\n"
    $ ctc_mode = "page"
    extend "ここまで来て少し悔しいが、しょうがない。\n"


    scene black
    with Dissolve(1.0)

    pause 1.8

    scene bg_to_the_lobby_01 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    pause 0.8

    narrator_arrow "一旦ロビーに戻ってきた。\n"
    extend "「まだ回ってないところあったかな？」\n"
    extend "「大浴場があるはずなんだけど……{w=0.3}たぶんこっちの奥のほうじゃない？」\n"
    scene bg_scream_04 at fullscreen_bg
    with fade
    extend "階段の下あたりに廊下が続いていた。\n"
    extend "「おお、{w=0.5}こんなところに廊下が」\n"
    $ ctc_mode = "page"
    extend "意外と気づかないもんだな。\n"

    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    scene black
    with Dissolve(1.0)
    play music "audio/se/エアコン.mp3" volume 0.4
    pause 1.8

    scene bg_a_start_filming_07 at fullscreen_bg
    with fade
    narrator_arrow "さっきまでの明るさとは違い、ここは少しだけ照明が落ちている。\n"
    extend "空気も、どこかひんやりとしていた。\n"
    extend "途中に、小さなスペースがある。\n"
    extend "自動販売機と、その横にベンチ。\n"
    extend "さらに脇には、コインロッカーが並んでいた。\n"
    $ ctc_mode = "page"
    extend "自販機の白い光が、そこだけをぼんやりと照らしている。\n"

    scene bg_public_bath_01 at fullscreen_bg
    with fade
    narrator_arrow "自販機の向かい側には、大きめの入り口があった。\n"
    extend "木の枠に、厚手の暖簾がかかっている。\n"
    extend "その奥から、かすかに湯気が流れ出ていた。\n"
    extend "「大浴場だな」\n"
    extend "温泉マークの暖簾がかかったその入り口は、{w=0.3}洋風のペンションの中では少しだけ浮いて見える。\n"
    $ ctc_mode = "page"
    extend "とはいえ、{w=0.3}無理にモダンに寄せたような作りにちょっと和む感じではある。\n"


    narrator_arrow "[heroine['first']]は少しだけ足を緩めて、その扉に視線を向けた。\n"
    extend "「こんなとこにあるんだね。{w=0.5}……撮る？」\n"
    extend "「いや――」\n"
    extend "一瞬だけ迷ってから、{w=0.3}首を横に振る。\n"
    extend "「大浴場は撮影許可がとれなかったんだって。{w=0.5}木下さんが」\n"
    extend "「あ、{w=0.3}このペンションの撮影って、{w=0.3}一応許可撮ってるんだ」\n"
    extend "「当然。{w=0.3}このカメリハは、ゲリラ撮影じゃないんだよ」\n"
    extend "「木下さん、{w=0.3}いつも適当なのに、こういうところちゃんとしてるよね」\n"
    $ ctc_mode = "page"
    extend "「そうそう」\n"


    narrator_arrow "……とはいえ、{w=0.3}ちょっとだけ気になる。\n"
    extend "しかし、{w=0.3}さすがに勝手に入るわけにはいかないか。\n"
    $ ctc_mode = "page"
    extend "まあ、{w=0.3}どうせ今日のお風呂はここを利用するわけだし、{w=0.3}中の様子だけならその時に見れるだろう。\n"

    scene bg_a_start_filming_09 at fullscreen_bg
    with fade
    narrator_arrow "さらに奥へ進む。\n"
    extend "「ここは……？」\n"
    extend "ドアの横に、小さなプレートがついている。\n"
    extend "{nw}\n"
    extend "“Drying Room”{nw}\n"
    extend "\n"
    extend "……乾燥室？\n"
    $ ctc_mode = "page"
    extend "思わず足を止める。\n"


    narrator_arrow "「乾燥室って、{w=0.3}なに？」\n"
    extend "[heroine['first']]が首をかしげる。\n"
    extend "「さあ……」\n"
    $ ctc_mode = "page"
    extend "気になって、ドアを少しだけ開けてみる。\n"

    play sound "audio/se/ドアを開ける1.mp3"
    scene bg_a_start_filming_10 at fullscreen_bg
    with fade

    narrator_arrow "中には、壁に沿って棚とフックが並んでいるだけだった。\n"
    extend "がらんとしていて、置かれているものは何もない。\n"
    extend "「……何もないね」\n"
    extend "「ああ、{w=0.3}あれだ。{w=0.5}たぶん、{w=0.3}冬用だな。{w=0.5}スキーとかの」\n"
    extend "「ああ、{w=0.3}なるほどね」\n"
    extend "今は六月だし、{w=0.3}使われていないのも当然か。\n"
    scene black
    with fade
    play sound "audio/se/ドアを閉める1.mp3"
    extend "軽く中の様子だけ確認して、ドアを閉める。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "特に撮るものもなさそうだが、一応、入口だけ記録しておく。\n"

    scene bg_a_start_filming_11 at fullscreen_bg
    with fade
    narrator_arrow "廊下の一番奥。\n"
    extend "シンプルなドアが一枚ある。\n"
    extend "「ここ、{w=0.3}なんだろ」\n"
    extend "「さあ……」\n"
    extend "少し気になって、軽く押してみる。\n"
    play sound "audio/se/ドアを開ける1.mp3"
    scene black
    with fade
    extend "――開いた。\n"
    play music "audio/se/雨の音_2.mp3" fadein 1.0
    $ ctc_mode = "page"
    extend "と、同時に外の湿った空気と雨風が流れ込んでくる。\n"

    scene bg_a_start_filming_12 at fullscreen_bg
    with fade

    narrator_arrow "「おお！{w=0.3}なんだ、{w=0.3}裏口かよ」\n"
    extend "思わず声をあげる。\n"
    extend "視界の先には、がらんとした砂利の駐車スペースと薄暗い森。\n"
    extend "建物の裏側へ続く小さな出入口だった。\n"
    extend "「スキー終わりは、この裏口から入って乾燥室へ……{w=0.3}って感じじゃない？」\n"
    extend "「な、{w=0.3}なるほど。{w=0.5}導線よくできてるな」\n"
    $ ctc_mode = "page"
    extend "納得して、小さくうなずく。\n"

    play sound "audio/se/風が吹く1.mp3"
    narrator_arrow "納得しかけたところで、強めの風が吹き込んでくる。\n"
    extend "雨粒がわずかに入り込み、腕を一気に濡らす。\n"
    narrator_arrow "「うわ、{w=0.3}ちょ、{w=0.3}ドア閉めるよ」\n"
    stop sound
    stop music
    pause 0.3
    scene black
    with fade

    play sound "audio/se/ドアを閉める1.mp3"
    extend "僕は、そそくさと扉を閉める。\n"
    extend "「うん、{w=0.3}さすがにここは撮らなくていいでしょ」\n"
    $ ctc_mode = "page"
    extend "扉を閉めると、廊下の静けさが戻る。\n"

    narrator_arrow "「うーん……{w=0.3}もう、だいたい見たかのな」\n"
    $ ctc_mode = "page"
    extend "「うん。{w=0.3}こんなもんかも。{w=0.3}戻ろうよ。」\n"


    scene black
    with Dissolve(1.0)

    pause 1.0

    scene bg_scream_03 at fullscreen_bg
    with Fade(1.5, 0.3, 2.0)

    play ambient_se "audio/se/雨の音_2.mp3" fadein 1.5
    narrator_arrow "ロビーに戻ると、窓の外は徐々に日が落ち始めている。\n"
    extend "「……ちょっと暗くなってきたな」\n"
    extend "僕が外を見ながら言う。\n"
    extend "「ほんとだ。{w=0.5}思ったより時間たってるね」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]もつられて窓のほうを見る。\n"

    show sil_a_start_filming_01 at sil_center, sil_fadein

    narrator_arrow "「思ったよりちゃんと撮れたし、今日はこのへんで切り上げるか」\n"
    extend "「賛成」\n"
    extend "と、一息ついたところでポケットのスマホが震えた。\n"
    $ ctc_mode = "page"
    extend "木下さんからのメッセージだ。\n"
    pause 0.3
    show sil_a_start_filming_01 at sil_center, sil_fadeout
    pause 0.3
    hide ssil_a_start_filming_01
    scene black
    with fade


    scene bg_sumaho_01 at fullscreen_bg
    show shade onlayer master # シェード機能（CH_00_effects.rpy）
    with fade

    narrator_arrow "**木下：**{nw}\n"
    extend "「いやーいい絵がいっぱい取れたな！ありがとう」\n"
    $ ctc_mode = "page"
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

    scene bg_scream_03 at fullscreen_bg
    with fade
    pause 0.3
    show sil_b_start_filming_01 at sil_center, sil_fadein

    narrator_arrow "「そうか、もう夕飯か……{w=0.3}段取りいいな」\n"
    extend "こういうところだけは本当に感心する。\n"
    extend "「確かに。{w=0.3}ちょうどよかったね。{w=0.3}なんかおなかすいてきた！」\n"
    extend "[heroine['first']]が肩を揺らして笑う。\n"
    extend "「行くか」\n"
    extend "「うん」\n"
    $ ctc_mode = "page"
    extend "僕たちは軽く支度を整えて、{w=0.3}山のふもとにあるレストランへ向かうことにした。\n"

    stop music fadeout 2.0
    stop ambient_se fadeout 2.0

    show ssil_b_start_filming_01 at sil_center, sil_fadeout
    hide sil_b_start_filming_01
    scene black
    with fade

    jump CH_08_restaurant_scene













