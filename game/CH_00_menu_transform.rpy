# 00_menu_transform.rpy
# 選択肢（menu）UIの見た目・演出をまとめて管理するファイル

# ------------------------------------------------------------
# 選択肢の上に出すコメント（必要な時だけ入れる）
# default はセーブ対象の変数。UI表示に使うのでここで定義してOK。
# ------------------------------------------------------------
default choice_comment = ""

# ------------------------------------------------------------
# スタイル定義（縁取り・色など）
# screen上の text / textbutton は Character と別の系統なので、
# ここで明示的に outlines や color を指定する必要がある。
# ------------------------------------------------------------

# コメントテキスト用（フェードなし・即表示）
style choice_comment_text:
    size 32
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]   # (太さ, 色, xオフセット, yオフセット)

# 選択肢ボタンの文字用（通常時・hover時）
style choice_button_text:
    size 28
    color "#ffffff"                  # 通常時の文字色（灰色を回避）
    hover_color "#ffffcc"            # マウスを乗せたときの色
    outlines [(2, "#000000", 0, 0)]

# （任意）ボタン自体の余白なども調整したい場合の例
# style choice_button:
#     padding (18, 10)               # (左右, 上下) など調整可能

# ------------------------------------------------------------
# Transform（動き）
# 1行ずつ「遅延→フェードイン」させる
# Transform() のキーワード引数に linear= は存在しないので、
# ATL(transformブロック)で pause/linear を書くのが正解。
# ------------------------------------------------------------
transform choice_item_fadein(d=0.0):
    alpha 0.0
    pause d
    linear 0.4 alpha 1.0

# ------------------------------------------------------------
# 既定の choice 画面を差し替え
# menu: を書くと、この screen choice が呼ばれる
# ------------------------------------------------------------
screen choice(items):

    # 上部コメント（フェードなし）
    if choice_comment:
        text choice_comment:
            style "choice_comment_text"
            xalign 0.5
            yalign 0.25

    # 選択肢
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 20

        # 互換性重視でカウンタ方式（enumerateを避ける）
        $ i = 0
        for caption, action, chosen in items:
            textbutton caption:
                # （追加）まずコメントを消す → 本来のaction
                action [ SetVariable("choice_comment", ""), action ]
                # 文字スタイル（色・縁取り）
                text_style "choice_button_text"

                # （任意）ボタン全体スタイルも使うなら
                # style "choice_button"

                # 順番にフェードイン
                at choice_item_fadein(i * 0.2)

            $ i += 1
