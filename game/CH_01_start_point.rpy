# CH_01_start_point.rpy

# デバックモード（開発用：公開版は False にしてください。）
default DEBUG_MODE = False

# screens.rpy の"メインメニュースクリーンとゲームメニュースクリーン"に
# "【デバッグ】クリア初期化"項目があるので、公開版は削除 or コメントアウト してください。

# -------- Ren’Py 初期テンプレートからの変更点 -------------
# screens.rpy の　screen say(who, what):変更　window hide / show に連動させる分岐の追加
# screens.rpy オープニング画面の設定の変更。詳しくはdocsフォルダを参照
# text what:の変更（文字を大きく、文字の表示位置の変更、文字の縁取り）
# options.rpy の　default preferences.text_cps　を 0から30へ変更（タイピングエフェクト）
# CH_00_transforms.rpyの追加：背景をフルスクリーンにぴったり表示する transform を設置
# CH_00_menu_transformの追加：選択肢の時間差フェードイン、コメント表示など
# デバックモードの追加
# CH_E_99_end_credits.rpy エンドロール（スタッフロール、エンドクレジット）の作成

# CH_S_system_flags.rpy 作成 クリアフラグなど。
# gui.rpy の define gui.idle_color の色を変更。メニュー文字などUI系文字にアウトライン追加。
# ※ 詳しくはdocsフォルダ'オープニング画面変更点（魔人の棲む塔）.md'を参照
# "gui.rpy" の "フォントとフォントサイズ" 項目　フォントをすべて "fonts/NotoSansJP-Regular.ttf" に変更。

# CH_00_ui_transforms.rpyの作成。 CTC（文末アイコン）用の演出定義

# options.rpy ビルド設定 にてアセット関連のアーカイブ化 配布物から .rpy（ソース）を除外して、.rpyc のみ残す
# options.rpy アイコンの変更
# docsフォルダの追加

# (修正)ヒストリーの表示を修正 screens.rpy の screen history()　style history_name: style history_text:のあたり

# ---------- 影絵ノベルからの実装と変更 -------------------
# 00_transforms.rpy を改良 立ち絵表示に対応（没にしたノベルゲームからの流用）
# CH_A_animations.rpy の追加 キャラクター（今回は影絵）のパラパラ漫画（没にしたノベルゲームからの流用）
# CH_00_effects.rpy の追加
# SnowBlossomで雨を作る（CH_00_effects.rpy）
# スローなフェードアウト（CH_00_effects.rpy）
# シェードをイメージで定義（CH_00_effects.rpy）
# Bを押すことでシェード機能（CH_00_effects.rpy）screens.rpy のヘルプに項目追加
# フラッシュ（CH_00_effects.rpy）
# game/CH_00_sil_transforms.rpyの作成 影絵の表示方法、画面効果。
# game/screens.rpy Input（入力）スクリーンの変更　名前入力を画面の中心にする。
# game/CH_00_menu_transformにコメントを消すロジックを組み込む。$ choice_comment = "" を逐一おく必要がなくなってるはず。
# game/CH_00_bg_movies.rpy の作成。背景ムービー用。
# CH_04_second_floor.rpyに雨用の追加トラック"ambient_se"（要改良）
# ロゴ背後のシェードを白くする。サイズを変更（screens.rpy）
# 左メニュー用にうっすら暗幕（screens.rpy）
# CH_00_flag.rpy 作成。ゲーム中のフラグ管理。
# エンドロールの大幅な変更（CH_E_02_end_credits）
# 画像、ムービー、影絵、影絵アニメーション、雨エフェクトを変更可能に。フラグでその要素の切り替えも可能。
# CH_00_ui_transforms.rpy　の改良。ページ送り、ページめくりアイコンに対応
# options.rpy ビルド設定にムービーをアーカイブ化を追加
# -----------------------------------------------

label start:
    # デバック用分岐 （デバックモードが False なら無視）
    if DEBUG_MODE:
        call CH_00_debug from _call_CH_00_debug
    jump input_names # 本編スタート

label CH_01_start_point:
    scene black
    with fade

    # ムービー（クリックでスキップ可能）
    play music "audio/se/雨の音_2.mp3" # fadein 0.5    
    pause 0.8
    $ renpy.movie_cutscene("movies/movie_01.webm", stop_music=False) 

    play music "audio/se/雨の車の中_bgm_louder2.mp3" # fadein 0.5   
    $ renpy.movie_cutscene("movies/movie_02.webm", stop_music=False)
    # stop_music=False は動画に play music を使う場合必須
    # ムービーを再生するときは、いったん他の音楽を止める設計っぽい。stop_music=自体は、なくても動画再生できるようです。

    # テキストウインドウを完全に非表示にする。（これがないとウインドウが出てしまうので毎回入れてください。）
    window hide    

    scene car_window_forest at fullscreen_bg
    with fade

    # narrator_arrow（キャラクター）を先頭に置くことで設定した専用アイコンの点滅。
    narrator_arrow "エンジンの低い唸りが、車内にゆっくりと満ちている。\n" 
    extend "静かな山道では、その振動だけがやけに現実味を帯びて響く。\n"
    extend "対向車は来ない。\n"
    extend "舗装の縁をなぞるように、道は緩やかに曲がり続けている。\n"
    extend "濡れたアスファルトが鈍く光り、その向こうに薄い霧が立ちのぼる。\n"
    # 面倒ですが最後の行に逐一これを置いてください
    # これを置くと矢印アイコンがページめくりのアイコンになります。
    # CH_00_ui_transforms.rpy
    $ ctc_mode = "page" 
    extend "フロントガラスの向こうで、山の緑がゆっくりと流れていく。\n"

    
    narrator_arrow "まだ覚えたての運転。\n"
    extend "ハンドルを握る手に、じんわりと汗がにじむ。\n"
    extend "慎重に、{w=0.3}慎重に、{w=0.3}ブレーキとアクセルを踏み替える。\n"
    extend "兄から借りてきたＳＵＶは、妙に静かで妙に広い。\n"
    extend "ハンドルが少し重い。\n"
    extend "いや、{w=0.3}たぶん重く感じているのは僕の手のほうだ。\n"
    $ ctc_mode = "page"
    extend "なんせ自動車教習所の車しか知らないんだから。\n"

    narrator_arrow "六月上旬。\n"
    extend "梅雨入り前の空は、{w=0.3}思いのほか低い。\n"
    extend "天気予報は曇りだったから、\n"
    extend "「ぎりぎり大丈夫だな！{w=0.5}君はラッキーだねぇ」\n"
    extend "なんて、{w=0.3}昨日のメッセージで代表の木下さんが言っていたけれど、{w=0.3}今は小雨が降っている。\n"
    extend "慣れない山道に、{w=0.3}慣れない運転。\n"
    $ ctc_mode = "page" 
    extend "ワイパーを一段階動かすだけで、{w=0.3}妙に緊張する。\n"

    narrator_arrow "僕は運転に必死でわからないが、{w=0.3}きっと[heroine['first']]は景色を見ているのだろう。\n"
    extend "「なんかすごい山奥にきちゃったね」\n"
    extend "助手席の[heroine['first']]が言う。\n"
    $ ctc_mode = "page" 
    extend "「ペンションの雰囲気、{w=0.3}最高らしいけど本当？」\n"

# ----- 簡易的な選択肢 -------------------------------------------------------

    $ choice_comment = "[heroine['first']]にそう聞かれ、僕は……"

    menu:
        "１　せっかくだから、[heroine['first']]にテンションを上げてもらおう思った。":
            $ flag_react_intro = "fun" 

        "２　とりあえず、このペンションの良さをそれっぽく語ってみることにした。":
            $ flag_react_intro = "appeal"

        "３　ちょっとくらい怖いことを言っても、たぶん怒られはしないだろうと思った。":
            $ flag_react_intro = "tease"



    $ choice_comment = ""  

    if flag_react_intro == "appeal":

        narrator_arrow "僕はそれらしく、このペンションの良さを伝えてみることにした。\n"
        extend "……正直なところ、{w=0.3}詳しいことは、ほとんど知らないんだけど。\n"
        extend "「ああ、{w=0.3}映画の撮影にはぴったりなんだってよ。"
        extend "なんか、{w=0.3}雰囲気もいいらしいし。"
        extend "静かで、{w=0.3}その……{w=0.5}おしゃれな感じのペンションって聞いた」\n"
        extend "「へえ、{w=0.3}楽しみ！」\n"
        extend "[heroine['first']]は、{w=0.3}少しだけ前のめりになって言う。\n"
        $ ctc_mode = "page" 
        extend "うまく伝わったのかわからないが、{w=0.3}楽しそうだし、{w=0.3}まあいいか。\n"



    elif flag_react_intro == "tease":

        narrator_arrow "正直なところ、{w=0.3}詳しいことはほとんど知らないんだけど。\n"
        $ ctc_mode = "page" 
        extend "僕は[heroine['first']]を、{w=0.3}ちょっとだけ怖がらせてみようと思った。\n"

        narrator_arrow "「ああ、{w=0.3}推理物の撮影にはぴったりなんだってよ。"
        extend "{w=0.3}廊下の奥で誰か倒れてても違和感ないんだって」\n"
        extend "「え、なにそれ……」\n"
        extend "[heroine['first']]は笑ったけれど、{w=0.3}わずかに強張っている気配がした。\n"
        extend "「こういう場所ってさ、{w=0.3}いかにも“現場”が作りやすいんだって。"
        extend "血の跡とかも、{w=0.3}映えそうだって……」\n"
        extend "「ちょっと、{w=0.3}言い方！」\n"
        $ ctc_mode = "page" 
        extend "今度は、はっきりと抗議が飛んできた。\n"

        narrator_arrow "さすがに言いすぎたかと思って、僕は軽く肩をすくめる。\n"
        extend "「いや、{w=0.3}ごめんって。{w=0.5}ほら、{w=0.3}撮影の話だよ、{w=0.3}あくまでも」\n"
        extend "「分かってるけどさ……」\n"
        extend "[heroine['first']]は、小さく息をついて静かになる。\n"
        $ ctc_mode = "page" 
        extend "ちょっと調子に乗りすぎてしまったようだった。\n"

    else:
        narrator_arrow "せっかくだから、[heroine['first']]にテンションを上げてもらおう思った。\n"
        extend "「ああ、{w=0.3}推理物の撮影にはぴったりなんだってよ」\n"
        extend "「なにそれ、怖いー」\n"
        $ ctc_mode = "page" 
        extend "笑いながら言うその声は、どこか弾んでいる。\n"

# ------------------------------------------------------------

    scene black
    with fade
    narrator_arrow "[heroine['first']]とは、{w=0.3}同じ大学の映画研究会で知り合った。\n"
    extend "クリスマスから付き合いだしたから、{w=0.3}半年ぐらいかな。\n"
    extend "まだ初心者カップルだ。\n"
    extend "最近ようやく、名字じゃなくて名前で呼べるようになったくらい。\n"
    $ ctc_mode = "page" 
    extend "僕にとっては初めての彼女だ。\n"

    narrator_arrow "もう半年だし、{w=0.3}距離を詰めたい気もするし、{w=0.3}急ぎすぎるのも違う気がする。\n"
    extend "だから研究会代表の木下さんから映画のロケハンの話を聞いたとき、{w=0.3}正直ちょっと思った。\n"
    extend "{nw}"
    extend "——チャンスかも。\n"
    extend "{nw}"
    extend "ペンション一泊二日。{w=0.3}しかも二人きり。\n"
    $ ctc_mode = "page" 
    extend "撮影の下見という大義名分つき。\n"

    narrator_arrow "いや、{w=0.3}別に何かどうとかあるわけじゃない。\n"
    extend "ただ、{w=0.3}もう少し自然に話せるようになれたらいいな、{w=0.3}くらいだ。\n"
    extend "[heroine['first']]は、{w=0.3}どう思っているんだろう。\n"
    $ ctc_mode = "page" 
    extend "映画のロケハンで旅行に行けることを、{w=0.3}無邪気に喜んでいたけれど。\n"

    $ renpy.movie_cutscene("movies/movie_03.webm", stop_music=True)
    scene car_rain_smartphone at fullscreen_bg
    narrator_arrow "うちの映研では卒業記念映画を製作することが毎年恒例になっている。\n"
    extend "今年の題材は推理物。\n"
    extend "タイトルは――{w=0.8}{nw}\n"
    extend "{nw}\n"
    extend "{cps=10}『山奥ペンションの殺意』{/cps}{nw}\n"
    extend "\n"
    extend "木下さんが決めた。\n"
    extend "木下さん曰く、{w=0.5}「直球のほうが分かりやすい」{w=0.3}らしい。\n"
    extend "……そういうものだろうか。\n"
    $ ctc_mode = "page" 
    extend "まあ、なんというか大雑把な人だが、勢いで決めてしまう決断力は、映研の代表にちょうどいいのかもしれない。\n"

    narrator_arrow "今回のこのペンション小旅行は、{w=0.3}その映画のロケハンとカメラリハーサルを兼ねたものだ。\n"
    extend "現地の雰囲気や光の具合を確かめながら、{w=0.3}ついでにカメラも回してみる。\n"
    extend "いろんな角度から試し撮りをして、{w=0.3}構想を練る。"
    extend "その下準備を僕らが行うわけだ。\n"
    $ ctc_mode = "page" 
    extend "僕たちはまだ大学二年だけれど、この役目は木下さんから直々に頼まれた。\n"

    narrator_arrow "あの人は自宅にこもって脚本を書きながら、{w=0.3}僕たちから送られてくる写真や映像を見て、{w=0.3}場面の流れを組み立てていくらしい。\n"
    extend "……楽な役回りだな、と少しだけ思う。\n"
    $ ctc_mode = "page" 
    extend "現地には来ないくせに、もうすでに細かい指示をよこしている。\n"

    narrator_arrow "「現地の雰囲気、どんな感じか教えて」\n"
    extend "「使えそうなカットは、とりあえず全部撮っといて」\n"
    extend "「場合によっては、どっちかカメラに入って芝居して」\n"
    extend "等々。\n"
    extend "……あの人は適当なようでいて、{w=0.3}撮影については妙に細かいからなぁ。\n"
    $ ctc_mode = "page" 
    extend "ずいぶんと使いが荒いが、{w=0.3}会費で僕たちだけの旅行ができるんだ。{w=0.5}文句は言えない。\n"


    scene car_window_forest at fullscreen_bg
    with fade
    narrator_arrow "「ねえ、{w=0.3}さっきのカーブさ。私、{w=0.3}助手席で不安そうな顔するからさ、{w=0.3}ちょっと減速してもう一回いけない？」\n"
    $ ctc_mode = "page" 
    extend "[heroine['first']]が本気か冗談かわからない顔で言う。\n"

# ----- 簡易的な選択肢 -------------------------------------------------------

    $ choice_comment = "僕は……"

    menu:
        "１　「いいね！それ」提案に軽く乗ってみることにした。":
            $ flag_react_curve = "friendly"
        "２　「いや、無理だから」軽くツッコむことにした。":
            $ flag_react_curve = "normal"
        "３　聞き流すことにした。":
            $ flag_react_curve = "quiet"

    $ choice_comment = ""  


    if flag_react_curve == "friendly":

        narrator_arrow "「いいね、{w=0.3}それ」\n"
        extend "思わず、{w=0.3}軽く乗ってしまった。\n"
        extend "「任せてよ、{w=0.3}名演技するから」\n"
        extend "その気になってしまった[heroine['first']]を、僕は慌ててたしなめる。\n"
        extend "「……でも今日は雨だからさ、{w=0.3}こういうのは帰りにしよう。"
        extend "明日なら晴れるかもしれないし」\n"
        extend "フロントガラスを流れる水を眺めながら言う。\n"

        narrator_arrow "「えー、{w=0.3}今やろうよ」\n"
        extend "[heroine['first']]は、少しだけ不満そうな声を出す。\n"
        extend "「ペンションに着いたら、{w=0.3}いくらでも付き合うよ」\n"


    elif flag_react_curve == "quiet":
        narrator_arrow "僕は何も言わず、ハンドルを握り直した。\n"
        extend "カーブに意識を持っていかれていて、うまく反応が返せない。\n"
        extend "彼女の声が、少し遠くに聞こえる。\n"
        extend "「……うん、{w=0.5}そうだね」\n"
        extend "とりあえず、{w=0.3}言葉だけ返す。\n"

        narrator_arrow "「じゃあさ、{w=0.5}ヒロイン役やるから――」\n"
        extend "「……うん」\n"
        extend "今度は短く返す。\n"
        extend "ちゃんと聞いているつもりなのに、{w=0.3}半分くらいしか頭に入ってこない。\n"
        extend "ブレーキのタイミングと、{w=0.3}対向車の有無と、{w=0.3}濡れた路面。\n"
        extend "そっちに気を取られて、{w=0.3}それどころじゃない。\n"

        narrator_arrow "「もう、{w=0.3}ちゃんと聞いてる？」\n"
        extend "少しだけ、拗ねた声。\n"
        extend "「聞いてるよ。{w=0.5}……ごめん、{w=0.3}ちょっと運転で手一杯」\n"
        extend "「つまんない！」\n"

    else:
        narrator_arrow "「いや、{w=0.3}無理だから。{w=0.3}ここ公道だから」\n"
        extend "「じゃあね、{w=0.3}到着したらね、{w=0.3}緊張してるヒロイン役、{w=0.3}やるから」\n"
        extend "「ペンションのロケハンだから！{w=0.3}そんなのいらないよ」\n"

# ------------------------------------------------------------

    extend "僕は[heroine['first']]にちょっと内気でおとなしいイメージを持っていたのだが、{w=0.3}今日はなんだか妙なテンションだ。\n"
    extend "さっきから、落ち着きがない。\n"
    extend "楽しそう、{w=0.3}というより、少し浮ついている。\n"
    extend "やはりロケハンとは言え１泊２日の小旅行。\n"
    $ ctc_mode = "page" 
    extend "浮かれているのだろうか。\n"
    stop music fadeout 2.0
    scene black
    with fade

    # ここで「溜め」：急に始まる感を消す
    pause 0.8

    # ムービー（クリックでスキップ可能）
    $ renpy.movie_cutscene("movies/movie_04.webm", stop_music=True)

    # 終わりの余韻
    pause 0.2

    # 一度暗転
    scene black
    with dissolve

    scene bg_road_sign_northframe_01 at fullscreen_bg
    with fade

    play music "audio/se/雨の車の中_bgm_louder2.mp3" fadein 0.5

    narrator_arrow "カーブを抜けると、視界が少し開けた。\n"
    extend "霧の向こう、道の脇に小さな木製の看板が立っている。\n"
    extend "{cps=60}\n{nw}"
    extend "Pension\n{nw}"
    extend "North Frame\n{nw}"
    extend "\n{/cps}"
    extend "ペンション・ノースフレーム\n"
    extend "白い文字が雨に濡れてかすかに光っていた。\n"
    extend "ここだ。\n"
    $ ctc_mode = "page" 
    extend "ここが今日、僕たちが宿泊するペンションに間違いない。\n"

    scene black
    with dissolve

    narrator_arrow "看板を過ぎると、霧の向こうに屋根らしき影が見える。\n"
    extend "「見えた？」\n"
    $ ctc_mode = "page" 
    extend "[heroine['first']]が身を乗り出す。\n"

    scene bg_pension_front_01 at fullscreen_bg
    with fade

    # 雨を表示
    # 記述は CH_00_effects.rpy へ
    # show rain_back at rain_fade
    show rain_front at rain_fade 

    narrator_arrow "木立の間に、三角屋根の輪郭が浮かぶ。\n"
    extend "濡れた外壁が、灰色の空の下で静かに佇んでいる。\n"
    extend "なんだか映画みたいだ、と思った。\n"
    extend "いや、そのために来たんだったか\n"
    extend "僕はアクセルを緩め、ゆっくりとハンドルを切る。\n"
    $ ctc_mode = "page" 
    extend "山奥のペンションへと、車は静かに近づいていく。\n"

    stop music fadeout 2.0
    # 雨を止める
    hide rain_back at rain_fade
    hide rain_front at rain_fade

    scene black
    with fade

    pause 0.8

    $ renpy.movie_cutscene("movies/movie_05.webm", stop_music=True)

    pause 0.2

    scene black
    with dissolve

    # ムービー（クリックでスキップ可能）
    $ renpy.movie_cutscene("movies/opening_1.webm", stop_music=True)
    # ムービー（クリックでスキップ可能）
    $ renpy.movie_cutscene("movies/opening_2.webm", stop_music=True)
    # 終わりの余韻
    pause 0.2

    # 一度暗転
    scene black
    with dissolve

    jump CH_02_pension_front

# ---------------------
# メモ
# renpy.full_restart() は ゲームを最初から再起動します。
# return だと「呼び出し元に戻る」なので、構造によってはタイトルに戻らないことがあります。
# 確実にタイトルへ戻すなら`renpy.full_restart() `が鉄板らしいです。
# Ren’Py は Case Sensitive（大小文字を区別） です。
# 画像名に大文字は使えないようです。
# label は、先頭に数字が使えないようです。
# ファイル名は構造的に無視されます。'jump' で、'game/'内の.rpyファイルすべての'label' を参照するそうです。すごいよね。
# 画像はフォルダわけしていてもimages/内だと？ディレクトリ指定せずに名前だけでいけます。もしかしてこれも全部参照してる……？
# ---------------------






