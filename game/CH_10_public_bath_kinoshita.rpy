label CH_10_public_bath_kinoshita:
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
    extend "常に館内BGMが流れているが、逆にそれが余計に孤独を感じさせる。\n"
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
    play sound "audio/se/エアコン.mp3" volume 0.4

    narrator_arrow "大浴場の前に掛かった暖簾が、空調の風に揺れて、わずかに揺れていた。\n"
    $ ctc_mode = "page"
    extend "今日の大浴場は予約制なので、{w=0.3}もちろん脱衣所にも人はいない。\n"
    scene black
    with dissolve
    stop sound
    $ ctc_mode = "page"
    narrator_arrow "……はずだった。\n"

    scene bg_public_bath_02b at fullscreen_bg
    with fade

    play music "audio/bgm/潜む怪奇.mp3"
    narrator_arrow "空きっぱなしのロッカーの上に脱ぎ捨てられた洋服とタオル。\n"
    extend "床には、まだ濡れた足跡。\n"
    extend "「……あれ？」\n"
    extend "誰か使っている？{w=0.3}おかしい。\n"
    extend "少しだけ嫌な予感がする。\n"
    $ ctc_mode = "page"
    extend "僕はそっと浴室の扉を覗いた。\n"

    stop music
    play sound "audio/se/ドアを開ける1.mp3"
    pause 0.5
    scene bg_public_bath_03 at fullscreen_bg
    with fade
    play music "audio/se/お風呂に水を入れる.mp3"
    play ambient_se "audio/se/お風呂でチャポン.mp3"
    narrator_arrow "浴槽は丸い石組みの風呂。\n"
    extend "端からは小さな滝のように、静かに湯が流れ落ちている。\n"
    extend "床と壁は石と木。\n"
    extend "山の温泉旅館みたいな、{w=0.3}落ち着いた空間だ。\n"
    extend "木の香りと、{w=0.3}ほのかな湯気。\n"
    $ ctc_mode = "page"
    extend "ここだけ時間がゆっくり流れているような、{w=0.3}不思議な静けさがあった。\n"
    stop music
    stop ambient_se

    pause 0.5
    scene black
    with dissolve

    # 現在の文字表示速度を退避（演出後に元へ戻すため）
    $ _old_cps = preferences.text_cps
    # 文字速度変更：1文字ずつゆっくり表示
    $ preferences.text_cps = 20
    $ ctc_mode = "page"
    narrator_arrow "しかし、{w=0.5}その静かな空間の中心に、{w=0.5}場違いなものがあった。\n"

    # 演出終了後、文字表示速度を元に戻す
    $ preferences.text_cps = _old_cps

    pause 0.4
    show sil_public_bath_02 at sil_center, sil_fadein
    play music "audio/bgm/真夜中に鳴り出すピアノ.mp3"

    narrator_arrow "男が倒れている。\n"
    extend "浴室の床には、{w=0.3}真っ赤な血。\n"
    extend "男は、その血だまりに顔をうずめるようにして倒れていた。\n"
    extend "ぴくりとも動かない。\n"
    $ ctc_mode = "page"
    extend "暖かな雰囲気と、{w=0.3}その湯気の中で、{w=0.3}その身体だけが妙に冷たく見えた。\n"

    narrator_arrow "「……っ！？」\n"
    extend "思わず息を呑む。\n"
    extend "頭が真っ白になる。\n"
    extend "これは……{w=0.3}死体だ。\n"
    extend "{cps=5}──完全に──{/cps}\n"
    extend "{cps=60}……死んでる！！{/cps}\n"
    $ ctc_mode = "page"
    extend "理解した瞬間、全身の血が一気に引いた。\n"

    stop music
    hide sil_public_bath_02
    scene bg_public_bath_05 at fullscreen_bg
    show sil_public_bath_03 at sil_center
    play sound "audio/se/男性の悲鳴.mp3" volume 1.2
    play music "audio/bgm/ゾンビホラーパニック.mp3"

    narrator_arrow "「うわああああっ！！」\n"
    extend "思わず悲鳴が飛び出した。\n"
    extend "「救急車！！{w=0.3}警察！！{w=0.3}で、{w=0.3}電話！！」\n"
    extend "動こうにも立ち上がることができない。\n"
    extend "「助けて！！{w=0.3}誰か！！{w=0.3}[heroine['first']]！！{w=0.3}[heroine['first']]！！」\n"
    extend "恥ずかしげもなく[heroine['first']]の名前を連呼する。\n"
    $ ctc_mode = "page"
    extend "{cps=5}僕は、{w=0.3}すっかり気が動転していた。{/cps}\n"
    hide sil_public_bath_03

    stop music
    play sound "audio/se/決定ボタンを押す12.mp3" volume 1.0
    scene bg_public_bath_05 at fullscreen_bg
    show sil_public_bath_04 at sil_center
    narrator_arrow "そのとき。\n"
    extend "動かない、{w=0.3}と思った男がびくっと動いた。\n"
    extend "「うおっ！？{w=0.3}うるさいなぁ！！」\n"
    extend "男が突然起き上がる。\n"
    extend "「なんだよ！{w=0.3}大声出すなよ！」\n"
    extend "「……え？」\n"
    extend "僕は呆然とする。\n"
    $ ctc_mode = "page"
    extend "その顔を見た瞬間、{w=0.3}今度は別の意味で、{w=0.3}思考が止まった。\n"
    hide sil_public_bath_04
    scene black
    with dissolve

    scene bg_public_bath_03 at fullscreen_bg
    with fade
    show sil_public_bath_05 at sil_center

    play music "audio/bgm/ぜんぜん余裕です.mp3"
    narrator_arrow "「……き、{w=0.3}木下さん！？」\n"
    extend "口に出した自分の言葉が信じられなかった。\n"
    extend "おもわず素っ頓狂な声が出る。\n"
    extend "「やあ、{w=0.3} [player['last']]くん～」\n"
    $ ctc_mode = "page"
    extend "対する木下さんは、{w=0.3}あまりにもいつも通りの声、{w=0.3}あまりにいつも通りの調子だった。\n"
    show sil_public_bath_05 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_05

    scene black
    with dissolve
    narrator_arrow "しかも――\n"
    extend "**全裸。**\n"
    $ ctc_mode = "page"
    extend "しばらく沈黙が流れる。\n"

    scene bg_public_bath_03 at fullscreen_bg
    with fade
    show sil_public_bath_06 at sil_center, sil_fadein

    narrator_arrow "おもむろに、木下さんが鼻をすすった。\n"
    extend "そのとき。\n"
    extend "{nw}\n"
    extend "ぽたっ{w=0.8}{nw}\n"
    extend "{nw}\n"
    $ ctc_mode = "page"
    extend "赤いものが床に落ちた。\n"

    show sil_public_bath_06 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_06
    scene bg_public_bath_05 at fullscreen_bg
    with fade
    show sil_public_bath_07 at sil_center, sil_fadein
    narrator_arrow "「……鼻血？」\n"
    extend "「いやー参ったね」\n"
    extend "木下さんは頭をかきながら言う。\n"
    extend "「お風呂入ってたら湯あたりしたっぽくてさ。"
    extend "立ちくらみしてそのまま倒れちゃったみたい。"
    extend "拍子に鼻打って鼻血まででちゃってた」\n"
    show sil_public_bath_07 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_07
    pause 0.4
    scene bg_public_bath_03 at fullscreen_bg
    with dissolve
    show sil_public_bath_08 at sil_center
    extend "「あっはっは」と笑う木下さん。\n"
    extend "「いやー参った参った」\n"
    $ ctc_mode = "page"
    extend "……この血だまり、{w=0.5}鼻血かよ。\n"

    show sil_public_bath_08 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_08
    show sil_public_bath_09 at sil_center

    narrator_arrow "僕は当然の質問をする。\n"
    extend "「木下さん、{w=0.3}なんでここにいるんですか？"
    extend "風呂まで入って…{w=0.3}自宅で脚本を書くんじゃなかったんですか」\n"
    $ ctc_mode = "page"
    extend "木下さんは、にやっと笑った。\n"

    show sil_public_bath_09 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_09
    show sil_public_bath_10 at sil_center, sil_fadein

    narrator_arrow "「いやぁ、{w=0.3}二人にさぁ、{w=0.3}このペンションのロケハン頼んだじゃない？\n"
    extend "どこをどう撮るか考えながらさ、ホームページとかレビューとか色々見てたら……\n"
    extend "あーここ、{w=0.3}いいなぁ、{w=0.3}って思っちゃってさ」\n"
    extend "「……はあ」\n"
    extend "「だからさ、{w=0.3}こっそり内緒で来ちゃった」\n"
    show sil_public_bath_10 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_10
    show sil_public_bath_08 at sil_center, sil_fadein
    extend "また「あっはっは」と愉快そうに笑う。\n"
    extend "「いやいやいやいや」\n"
    extend "僕は思わずツッコミを入れる。\n"
    extend "「きちゃったって……{w=0.3}普通来ます？{w=0.5}来てたんなら教えてくださいよ！\n"
    $ ctc_mode = "page"
    extend "家にいるふりまでして僕らとチャットで会話して撮影だなんて……{w=0.3}あれはいったいなんだったんですか！？」\n"

    show sil_public_bath_08 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_08
    show sil_public_bath_05 at sil_center, sil_fadein

    narrator_arrow "木下さんは肩をすくめる。\n"
    extend "「いやぁ、{w=0.3}それはさ、{w=0.3}せっかく二人に頼んだ手前、{w=0.3}邪魔しちゃ悪いかなって思ってさ。{w=0.3}一応、気ぃ使ったわけよ」\n"
    extend "「どういうことですか？」\n"
    $ ctc_mode = "page"
    extend "僕は眉をひそめる。\n"

    show sil_public_bath_05 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_05

    scene black
    with fade
    narrator_arrow "木下さんは、にやにや笑った。\n"
    extend "「どういうことって、{w=0.3}そりゃ君……恋路だよ。{w=0.3}うら若き二人の」\n"
    $ ctc_mode = "page"
    extend "「……？」\n"

    scene bg_public_bath_03 at fullscreen_bg
    with fade
    show sil_public_bath_11 at sil_center, sil_fadein

    narrator_arrow "「だってさぁ{w=0.3}半年付き合って二人きりで旅行だろ？{w=0.3}青春イベントじゃん？{w=0.3}いや見守るしかないじゃん！？」\n"
    extend "両手を広げて、なぜか誇らしげに言い切る。\n"
    $ ctc_mode = "page"
    extend "「見守るって！そんな……{w=0.3}隠れてペンションに泊まるのは見守りじゃないですよ！」\n"

    narrator_arrow "木下さんは笑いながら言う。\n"
    extend "「いやーそこは先輩としての責任というものだよねぇ～。"
    extend "映研としての！"
    extend "いや人生としての！」\n"
    $ ctc_mode = "page"
    extend "「……」\n"

    show sil_public_bath_11 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_11
    show sil_public_bath_12 at sil_center, sil_fadein
    narrator_arrow "「大変だったよ～君の車をタクシーでこっそり追跡するの。"
    extend "そこから物陰でペンションに入るのを見守り、"
    extend "森からちゃんと部屋に入るのを見守り……」\n"
    stop music
    play sound "audio/se/過去を思い出す.mp3"
    hide sil_public_bath_12
    scene bg_public_bath_06 at fullscreen_bg
    extend "「森から！？」\n"
    extend "「そう、{w=0.3}雨に濡れまくって大変だったんだから……"
    extend "あ、{w=0.3}部屋の中は覗いてないぞ！そこは断じてないぞ！」\n"
    $ ctc_mode = "page"
    extend "僕はふと気づく。\n"

    scene black
    with fade

    narrator_arrow "「……じゃあ」\n"
    $ ctc_mode = "page"
    extend "[heroine['first']]が見た人影って\n"

    pause 0.4
    scene bg_public_bath_03 at fullscreen_bg
    with fade
    show sil_public_bath_11 at sil_center, sil_fadein

    narrator_arrow "「……幽霊の正体は、{w=0.3}木下さんだったんだ」\n"
    extend "「幽霊？なんだそりゃ」\n"
    $ ctc_mode = "page"
    extend "そのとき、大浴場の入口から足音が聞こえた。\n"

    scene black
    stop music fadeout 1.0
    play sound "audio/se/学校の廊下を走る.mp3"

    narrator_arrow "「[player['first']]！！」\n"
    extend "[heroine['first']]の声だ。\n"
    extend "僕の悲鳴を聞いて駆けつけてきてくれたんだ！\n"
    play sound "audio/se/ドアを開ける1.mp3"
    extend "次の瞬間、[heroine['first']]が浴室に飛び込んでくる。\n"
    extend "「大丈夫――」\n"
    extend "そして。\n"
    play sound "audio/se/過去を思い出す.mp3"
    extend "固まった。\n"
    extend "視線の先には\n"
    $ ctc_mode = "page"
    extend "{cps=5}**全裸の木下さん。**{/cps}\n"


    narrator_arrow "「きゃあああああ！！変質者！！」{nw}\n"
    extend "[heroine['first']]の拳が一直線に飛んだ！{w=0.3}\n"
    play sound "audio/se/重いキック1.mp3"

    # 影絵アニメーション　ワンショット（詳細は CH_00_animations.rpy）
    $ play_anim_once("dash", "images/anim/panch/", speed=0.05, at_list=[fullscreen_bg]) 
    $ renpy.pause(1.0, hard=True) # 完全に操作をロック

    extend "**バシン！！**{w=0.5}{nw}\n"
    $ ctc_mode = "page"
    extend "「ぐはっ！！」{w=0.5}{nw}\n"

    # 影絵アニメーション　ワンショット（詳細は CH_00_animations.rpy）
    $ play_anim_once("dash", "images/anim/knockback_motion/", speed=0.05, at_list=[fullscreen_bg]) 
    play sound "audio/se/背負い投げ1.mp3"
    # フラッシュ（記述は CH_00_effects.rpy）
    call punch_hit from _call_punch_hit 
    $ renpy.pause(3.0, hard=True) # 完全に操作をロック

    narrator_arrow "顎に[heroine['first']]のパンチをうけた木下さんは、吹き飛んだ。\n"
    extend "木下さんの体が、{w=0.3}まるで軽い人形みたいに宙に浮く。\n"
    extend "ぐるん、{w=0.3}と不自然に一回転。\n"
    $ ctc_mode = "page"
    extend "そのまま壁にぶち当たり頽れる。\n"

    scene black
    with fade
    narrator_arrow "……そして。{w=0.8}{nw}\n"
    extend "ぴたり、{w=0.3}と動かなくなった。\n"
    extend "「…………」\n"
    $ ctc_mode = "page"
    extend "――木下さんは、{w=0.8}再度気絶した。\n"
    pause 0.6
    scene bg_public_bath_07 at fullscreen_bg
    with fade
    show sil_public_bath_14 at sil_center, sil_fadein
    play music "audio/se/お風呂に水を入れる.mp3" fadein 1.5

    narrator_arrow "浴室に、静寂が戻る。\n"
    extend "[heroine['first']]は肩で息をしている。\n"
    extend "その拳が、ゆっくり震えていた。\n"
    extend "そして汚いものを見るかのように一瞥\n"
    $ ctc_mode = "page"
    extend "その時、やっと[heroine['first']]は過ちに気づいたようだ。\n"

    show sil_public_bath_14 at sil_center, sil_fadeout
    pause 0.4
    hide sil_public_bath_14
    show sil_public_bath_15 at sil_center, sil_fadein
    narrator_arrow "「……あれ？」\n"
    extend "[heroine['first']]は、再度鼻血を流しながら気絶する木下さんの顔を覗き込む。\n"
    extend "「……え？{w=0.3}木下さん？」\n"
    extend "[heroine['first']]の顔がみるみる青くなる。\n"
    extend "「え、{w=0.3}なんで！？{w=0.3}なんでここに！？」\n"
    extend "そして次の瞬間。\n"
    extend "{cps=20}「……やっちゃった？」{/cps}\n"
    $ ctc_mode = "page"
    extend "恐る恐る僕を見る。\n"

    scene black
    with fade

    narrator_arrow "僕は、{w=0.3}その質問に答えられなかった。\n"
    extend "顔を青ざめオロオロする彼女。\n"
    extend "湯気の立ちこめる浴室。\n"
    extend "床には鼻血の湖。\n"
    extend "壁際には、{w=0.3}鼻血を流しながら気絶する、{w=0.3}全裸の映画研究会代表。\n"
    extend "――なんだこの状況。\n"
    $ ctc_mode = "page"
    extend "僕は静かに思った。\n"
    scene black
    with Dissolve(1.0)

    stop music fadeout 2.0

    jump CH_10_last_scene

