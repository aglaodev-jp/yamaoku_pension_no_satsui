# CH_01_label input_names

# セーブ・ロード対応のため default を使う
default player = {}
default heroine = {}

label input_names:

    window hide 
    play music "audio/bgm/ドラマティック・シティ.mp3"
    scene bg_pension_entrance_04 at fullscreen_bg
    show shade onlayer master # シェード機能（CH_00_effects.rpy）
    with fade

    # ---- 入力ループ開始 ----
    while True:

        # ===== 主人公 =====
        $ player.clear()

        $ player["last"] = renpy.input("あなたの苗字を入力してください。", length=10).strip() or "森川"
        $ player["first"] = renpy.input("あなたの名前を入力してください。", length=10).strip() or "湊"

        # フルネーム（全角スペース）
        $ player["full"] = f"{player['last']}　{player['first']}"

        # ===== 彼女 =====
        $ heroine.clear()

        $ heroine["last"] = renpy.input("お連れさまの苗字は？", length=10).strip() or "皆瀬"
        $ heroine["first"] = renpy.input("お連れさまの名前は？", length=10).strip() or "唯"

        $ heroine["full"] = f"{heroine['last']}　{heroine['first']}"

        # ===== 確認画面 =====
        $ choice_comment = """
        ご確認をお願いします。

        あなた： [player['full']]
        お連れさま： [heroine['full']]

        この内容でよろしいですか？
        """

        menu:
            "はい":
                $ choice_comment = "" # コメント消す。これを置かなくてもコメントが消えるように対応しましたが、今回は念のためおいています
                jump CH_01_start_point        
            "いいえ":
                $ choice_comment = ""
                "では、もう一度入力してください。"
                # while True により最初に戻る

# ------ つかいかた ----------------------------------
# 苗字
# [player['last']]
# [heroine['last']]

# 名前
# [player['first']]
# [heroine['first']]
# "「[player['first']]くん、運転おつかれさま」\n"

# フルネーム
# [player['full']]
# [heroine['full']

# 会話キャラ定義：
# define p = Character("[player['first']]")
# define h = Character("[heroine['first']]")
# 改まった場面なら：
# define p_formal = Character("[player['last']]")
# define h_formal = Character("[heroine['last']]") など
