label  CH_03_pension_entrance:
    window hide

    play music "audio/se/雨の音_2.mp3" fadein 0.5
    scene bg_pension_entrance_01 at fullscreen_bg
    with fade
    # 雨を表示
    show rain_back at rain_fade
    show rain_front at rain_fade 
    pause 3.0

    narrator_arrow "石造りのアーチに、重みのある木製のドア。\n"
    extend "落ち着いた色合いで、装飾は控えめながらも質感がいい。\n"
    $ ctc_mode = "page"
    extend "玄関灯はすでに灯っていて、雨粒が淡く反射している。\n"

    narrator_arrow "「ちょっと待って」\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "[heroine['first']]はアーチの前で足を止め、立ち位置を少しずつ変えながらシャッターを切る。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    extend "一枚撮っては確認し、また角度を変える。\n"
    play sound "audio/se/カメラのシャッター2.mp3"
    $ ctc_mode = "page"
    extend "雨脚の様子をうかがいながら、レンズが濡れない一瞬を探している。\n"

    narrator_arrow "……静かだ。\n"
    extend "雨音しか聞こえない。\n"
    $ ctc_mode = "page"
    extend "人の声も足音も聞こえない。\n"

    $ choice_comment = "僕は……"
    
    menu:
        "１　ドアを開けることにした。":
            $ flag_entrance = "lead"
        "２　唯に開けてもらった。":
            $ flag_entrance = "follow"
        "３　少しだけ躊躇した。":
            $ flag_entrance = "hesitate"

    $ choice_comment = ""

    pause 1.0

    scene bg_pension_entrance_02 at fullscreen_bg
    with fade


    if flag_entrance == "lead":
        narrator_arrow "「……まあ、{w=0.3}もう予約時間だし、{w=0.3}入ろうか」\n"
        extend "そう言って、僕はドアに手をかける。\n"
        extend "ひんやりとした取っ手を押し込むと、重みのある扉がゆっくりと開いた。\n"
        extend "「ペンションなんて初めて！{w=0.3}ドキドキするね」\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]が少しだけ弾んだ声で言う。\n"


    elif flag_entrance == "follow":
        narrator_arrow "「ほら、{w=0.3}時間ぴったりだし。{w=0.3}入ろうよ」\n"
        extend "僕が何か言うより先に、[heroine['first']]はそう言ってドアに手をかけ押し開いた。\n"
        extend "「ペンションなんて初めて！{w=0.3}ドキドキするね」\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]の、{w=0.3}そのためらいのなさが羨ましい。\n"


    else:
        narrator_arrow "「営業中、{w=0.3}だよな？{w=0.3}入って大丈夫かな？」\n"
        extend "[heroine['first']]がスマホで予約画面を確認する。\n"
        extend "「大丈夫だよ。ちゃんと予約入ってるし。\n"
        extend "チェックイン十五時って書いてある」\n"
        extend "画面をこちらに見せながら、少し笑う。\n"
        extend "「ほら、時間ぴったり。入ろうよ」\n"
        $ ctc_mode = "page"
        extend "[heroine['first']]がドアを開く。\n"

    # 雨を止める
    hide rain_back at rain_fade
    hide rain_front at rain_fade

    scene black
    with fade
    pause 1.0
    stop music fadeout 2.0

    play sound "audio/se/入店するときのベル.mp3"
    pause 0.5
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5
    play ambient_se "audio/se/雨の音_2.mp3"
    scene bg_pension_entrance_03 at fullscreen_bg
    with fade

    narrator_arrow "扉が開いた瞬間、空気が変わる。\n"
    extend "ふわっと木の匂い。\n"
    extend "わずかに暖房の効いた、乾いた室内の空気。\n"
    extend "外のひんやりした湿気が、すっと引く。\n"
    extend "六月上旬とはいえ、山はやっぱり少し冷える。\n"
    $ ctc_mode = "page"
    extend "濡れた腕が、じんわり温まっていく。\n"

    narrator_arrow "シックな受付カウンター。\n"
    extend "ただ――\n"
    extend "カウンターの向こうに人影はない。\n"
    extend "代わりに、黒いスタンドに固定されたタブレットが備え付けてあった。\n"
    extend "木の内装に対して、やや無機質だ。\n"
    $ ctc_mode = "page"
    extend "画面が自動で切り替わる。\n"

    scene bg_pension_entrance_04 at fullscreen_bg
    with fade

    narrator_arrow "{cps=60}---\n{nw}" # `{cps=数字}` その行だけ文字表示の速度変更
    extend "\n{nw}"
    extend "【本日は簡易宿泊です】\n{nw}"
    extend "・スタッフは常駐しておりません\n{nw}"
    extend "・チェックイン／アウトはセルフ方式です\n{nw}"
    extend "・食事の提供はありません（素泊まり）\n{nw}"
    extend "・緊急時は画面下部の連絡先へ\n{nw}"
    extend "\n{nw}"
    $ ctc_mode = "page"
    extend "---{/cps}{w=1.0}\n" # 文字速度をもどす

    pause 0.4 
    show sil_pension_entrance_01 at sil_center, sil_fadein

    narrator_arrow "「へえ」\n"
    extend "思わず声が出る。\n"
    extend "「無人チェックインなんだ」\n"
    extend "[heroine['first']]が画面をのぞき込む。\n"
    extend "「さすがリノベ物件って感じよね。合理的！」\n"
    extend "僕は少し拍子抜けする。\n"
    extend "「探偵ものの舞台にしては近代的すぎない？」\n"
    extend "「でも雰囲気はいいよ？　素泊まりって分かってるし、{w=0.3}撮影には好都合じゃない？」\n"
    extend "それは、確かにそうだ。\n"
    $ ctc_mode = "page"
    extend "しかし………{w=0.3}なんか違うんだよなあ。\n"

    show sil_pension_entrance_01 at sil_center, sil_fadeout
    pause 0.4
    hide sil_pension_entrance_01

    narrator_arrow "タブレットに\n{nw}"
    extend "【代表者のスマートフォンで予約情報を呼び出してください】\n{nw}{w=0.8}"
    extend "と表示される。\n"

    show sil_pension_entrance_02 at sil_center, sil_fadein

    extend "「予約、私のスマホね」\n"
    extend "[heroine['first']]が自分のスマホを取り出し、QRコードをタブレットにかざす。\n"

    play sound "audio/se/決定ボタンを押す52.mp3"
    pause 0.3

    extend "ポン、と乾いた電子音が短く鳴る。\n"
    extend "僕は自然と、彼女の肩越しに画面をのぞき込んだ。\n"
    $ ctc_mode = "page"
    extend "画面が切り替わる。\n"

    hide sil_pension_entrance_02
    pause 0.3
    narrator_arrow "{cps=60}予約内容確認。\n{nw}"
    extend "\n{nw}"
    extend "代表者名：[player['full']]\n{nw}"
    extend "宿泊人数：２名\n{nw}"
    extend "部屋タイプ：スタンダードツイン\n{nw}"
    $ ctc_mode = "page"
    extend "部屋数：１\n{/cps}"

    scene bg_pension_entrance_04b at fullscreen_bg
    show sil_pension_entrance_03 at sil_center

    stop music
    stop ambient_se
    play sound "audio/se/過去を思い出す.mp3"

    narrator_arrow "……１？\n"
    extend "一瞬、{w=0.3}画面の読み方を間違えたのかと思った。\n"
    extend "スクロールする。\n"
    extend "確認する。\n"
    extend "戻る。\n"
    $ ctc_mode = "page"
    extend "やっぱり、１。\n"

    narrator_arrow "「……あれ？」\n"
    extend "「どうしたの？」\n"
    extend "[heroine['first']]は気づいていない様子で入力を続けている。\n"
    extend "「いや、ちょっと待って」\n"
    $ ctc_mode = "page"
    extend "僕はもう一度、画面を凝視する。\n"

    show sil_pension_entrance_03 at sil_center, sil_fadeout
    pause 0.4
    hide sil_pension_entrance_03

    scene black
    with fade
    pause 0.3

    narrator_arrow "部屋数：１。\n"
    extend "映研のロケハンで、{w=0.3}男女二人。\n"
    extend "普通、{w=0.3}部屋は別だろう。\n"
    extend "……だよな？\n"
    extend "喉が妙に乾く。\n"
    extend "「ちょっと、電話してくる」\n"
    extend "「うん？」\n"

    $ renpy.music.set_volume(0.4, channel="music") # 音楽の音量を小さく
    play music "audio/se/雨の音_2.mp3"
    extend "僕はカウンターから少し離れ、{w=0.3}スマホを取り出す。\n"
    extend "代表の木下さんに電話をかけた。\n"

    play sound "audio/se/電話の呼び出し音.mp3"
    scene bg_pension_entrance_05 at fullscreen_bg
    with fade
    pause 0.2
    stop sound
    show sil_pension_entrance_05 at sil_center, sil_fadein

    narrator_arrow "ワンコールで出た。\n"
    $ renpy.music.set_volume(1.0, channel="music") # 音楽の音量を戻す
    play music "audio/bgm/ぜんぜん余裕です.mp3"

    extend "『おお、[player['last']]君！』\n"
    extend "声がやけに明るい。\n"
    extend "『無事着いたかい！よかったよかった！』\n"
    extend "「あの、{w=0.3}はい、{w=0.3}着きました。{w=0.3}それはいいんですけど」\n"
    extend "『いい写真は撮れそうか？』\n"
    extend "「いや、{w=0.3}あの、{w=0.3}それどころじゃなくてですね」\n"
    $ ctc_mode = "page"
    extend "事情を説明する。\n"

    show sil_pension_entrance_05 at sil_center, sil_fadeout
    pause 0.4
    hide sil_pension_entrance_05

    scene black
    with fade
    pause 0.3

    narrator_arrow "部屋が一室しか取られていないこと。\n"
    extend "僕は聞いていなかったこと。\n"
    extend "これはどういうことなのかということ。\n"
    extend "電話の向こうで、数秒の沈黙。\n"
    $ ctc_mode = "page"
    extend "そして。\n"

    narrator_arrow "『……何を言っているんだね、{w=0.3}[player['last']]君』\n"
    extend "低く、落ち着いた声。\n"
    extend "「え？」\n"
    extend "『君と[heroine['last']]君は交際しとるんだろう？』\n"
    extend "「そ、{w=0.3}それは、{w=0.3}まあ、{w=0.3}はい、{w=0.3}そうですけど」\n"
    extend "『ならば一部屋で問題あるまいよ』\n"
    extend "あるだろう。\n"
    extend "いや、あるよな？\n"
    $ ctc_mode = "page"
    extend "あるよ。\n"

    scene bg_pension_entrance_05 at fullscreen_bg
    show sil_pension_entrance_05 at sil_center

    narrator_arrow "「いやでも、{w=0.3}まだその、{w=0.3}心の準備というか……」\n"
    extend "『中高生じゃあるまいし』\n"
    extend "「そういう問題じゃなくてですね！」\n"
    extend "『会費は有限なのだよ、[player['last']]君』\n"
    extend "きた。\n"
    extend "代表モードだ。\n"
    extend "『今回、ちょうど交際中の二人がロケハンに行くということでな。\n"
    extend "経費削減にもなって実に合理的だと判断した』\n"
    extend "「合理的！？」\n"
    extend "『うむ』\n"
    $ ctc_mode = "page"
    extend "うむ、じゃない。\n"

    show sil_pension_entrance_05 at sil_center, sil_fadeout
    pause 0.3
    hide sil_pension_entrance_05

    scene bg_pension_entrance_04 at fullscreen_bg
    pause 0.3
    show sil_pension_entrance_06 at sil_center, sil_fadein

    narrator_arrow "「それに、[heroine['last']]がなんて言うか……」\n"
    extend "『安心しなさい』\n"
    extend "妙に含みのある声になる。\n"
    extend "『[heroine['last']]君にはきちんと話して、了承を得てある』\n"
    extend "「……え？」\n"
    extend "『君に伝えていなかったのは、奥手な君への配慮というやつだ』\n"
    extend "なにを配慮してるんだ。\n"
    extend "僕はゆっくりと顔を上げる。\n"

    show sil_pension_entrance_06 at sil_center, sil_fadeout
    pause 0.3
    hide sil_pension_entrance_06
    pause 0.3
    show sil_pension_entrance_07 at sil_center, sil_fadein # 右に寄せる

    extend "エントランスでは、[heroine['first']]がカウンター越しにタブレットを撮影している。\n"
    $ ctc_mode = "page"
    extend "どうやら既に必要事項を入力し終わったようだ。\n"

    narrator_arrow "……もしかして。\n"
    extend "道中、{w=0.3}やけに変なテンションだったのは\n"
    extend "「……知ってたのか」\n"
    extend "小さくつぶやく。\n"
    show sil_pension_entrance_07 at sil_center, sil_fadeout
    pause 0.3
    hide sil_pension_entrance_07
    scene black
    with fade
    extend "電話の向こうで、木下がくくっと笑う。\n"
    extend "『[player['last']]君』\n"
    extend "「はい……」\n"
    extend "『健闘を祈る』\n"
    extend "「へ？」\n"
    extend "『何かあればまた連絡を。\n"
    $ ctc_mode = "page"
    extend "健やかな一泊二日を』\n"

    scene bg_pension_entrance_05 at fullscreen_bg
    with fade
    pause 0.3
    show sil_pension_entrance_05 at sil_center, sil_fadein
    stop music
    play sound "audio/se/電話が切れる2.mp3"
    pause 0.1
    play ambient_se "audio/se/雨の音_2.mp3" 
    pause 0.3
    narrator_arrow "切れた。\n"
    extend "……なんなんだ、あの人は。\n"
    $ ctc_mode = "page"
    extend "スマホを握ったまま、立ち尽くす。\n"

    pause 0.3
    scene black
    with fade
    pause 0.3
    narrator_arrow "一部屋。\n"
    extend "ツインってことはベッドは二つだ。\n"
    extend "そうだ、落ち着け。\n"
    extend "物理的には分かれている。\n"
    $ ctc_mode = "page"
    extend "問題はそこじゃない気もするが。\n"
    
    scene bg_pension_entrance_04 at fullscreen_bg
    with fade
    pause 0.4 
    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/bgm/日曜日のカフェ.mp3" fadein 1.5

    narrator_arrow "視線を上げると、[heroine['first']]がこちらを見ていた。\n"
    extend "「木下さん？」\n"
    extend "「あ、うん……」\n"
    extend "「なんて？」\n"
    extend "ほんの少しだけ、意味ありげに笑っているような気がするのは、{w=0.3}気のせいか。\n"
    extend "「……合理的判断らしい」\n"
    extend "「ふふ、{w=0.3}だよね」\n"
    $ ctc_mode = "page"
    extend "やっぱり知ってる。\n"

    pause 0.4
    show sil_pension_entrance_08 at sil_center

    narrator_arrow "「[player['first']]くん、顔赤いよ」\n"
    extend "「赤くない」\n"
    extend "「撮る？」\n"
    extend "「やめて」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]は楽しそうにシャッターを切るふりをする。\n"

    narrator_arrow "……完全に、僕だけが知らなかった側だ。\n"
    extend "代表に振り回され、\n"
    extend "[heroine['first']]に見透かされ。\n"
    $ ctc_mode = "page"
    extend "ロケハンに来たはずなのに、{w=0.3}別の意味で試されている気がする。\n"

    show sil_pension_entrance_08 at sil_center, sil_fadeout
    pause 0.3
    hide sil_pension_entrance_08
    scene black
    with fade

    narrator_arrow "「チェックイン完了。"
    extend "部屋番号出たよ」\n"
    extend "[heroine['first']]が言う。\n"
    extend "タブレットには、\n{nw}"
    extend "【2階 203号室】\n{nw}"
    extend "と表示されている。\n"
    extend "僕は小さく息を吐いた。\n"
    $ ctc_mode = "page"
    extend "……健闘って、なんだよ！\n"
    stop music fadeout 2.0
    pause 1.0
    jump CH_04_second_floor
