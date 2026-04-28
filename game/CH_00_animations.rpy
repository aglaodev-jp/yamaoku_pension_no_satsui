# ==================================================
# animations.rpy
# パラパラ漫画（PNG連番）を自動でAnimation登録する（ループ/非ループ両対応）
# ==================================================

init python:
    def make_anim(name, folder, speed=0.05):
        """
        name   : Ren'Py上の画像名（例: "yui idle"）
        folder : game/ から見たフォルダ（例: "images/yui/idle/"）
        speed  : 1フレームの表示秒数（例: 0.05）
        """

        # Ren'Pyが把握している「ゲーム内ファイル一覧」から拾う
        frames = [
            f for f in renpy.list_files()
            if f.startswith(folder) and f.lower().endswith(".png")
        ]

        # ファイル名順に並べる（frame_0000.png → frame_0001.png → ...）
        frames.sort()

        # 見つからない場合は、原因が分かるように明示的に止める
        if not frames:
            raise Exception(
                "Animation frames not found: name='{}', folder='{}'".format(name, folder)
            )

        # Animationに渡す [file, time, file, time, ...] を構築
        anim = []
        for f in frames:
            anim.extend([f, speed])

        # Ren'Pyのimageとして登録（show yui idle が使えるようになる）
        renpy.image(name, Animation(*anim))

init python:
    def make_anim_once(name, folder, speed=0.05, ext=".png", prefix=None):
        """
        連番PNGフォルダから、ワンショット（1回だけ再生→最後で停止）アニメを作る。

        ポイント:
        - Ren'Pyの Animation() は「引数が奇数（最後が画像）」だと最後で止まる。
        - なので、最後のフレームには delay を付けない。
        """

        # Ren'Pyが管理しているファイル一覧から folder 配下の画像を集める
        frames = []
        for f in renpy.list_files():
            if not f.startswith(folder):
                continue
            if not f.lower().endswith(ext):
                continue

            if prefix is not None:
                fname = f.split("/")[-1]
                if not fname.startswith(prefix):
                    continue

            frames.append(f)

        # 連番順に並べる
        frames.sort()

        if not frames:
            raise Exception("make_anim_once: No frames found. folder='{}'".format(folder))

        # Animation に渡す引数を作る
        # 例: [img0, 0.05, img1, 0.05, img2]  ←最後が画像なので止まる
        args = []

        # 最後以外: (画像, delay)
        for f in frames[:-1]:
            args.append(f)
            args.append(speed)

        # 最後: 画像だけ（delayを付けない！）
        args.append(frames[-1])

        # 画像登録
        renpy.image(name, Animation(*args))


    # --------------------------------------------------
    # ワンショットを「何回でも再生」するためのヘルパ
    # --------------------------------------------------
    #
    # make_anim_once() は init 時に Animation を1回だけ作って image 登録します。
    # そのため、同じ画像タグが画面に出たままの状態で
    #   show yui happy once
    # をもう一度実行しても「見た目が変わらない」扱いになり、
    # アニメが再スタートしません（最後のフレーム静止のままになりやすい）。
    #
    # そこで、
    #   1) 毎回「新しい Animation インスタンス」を作る build_anim_once()
    #   2) いったん hide → show して確実に再生をリセットする play_anim_once()
    # を用意します。
    #
    # ★シナリオ側で1行（初回表示だけなら使えます）
    #   show expression build_anim_once("images/yui/happy/", 0.05) as yui at char_center
    #
    # ★タグを強制リセット（hide→show）こちらが複数回使用可能
    #   $ play_anim_once("yui", "images/yui/happy/", speed=0.05, at_list=[char_center])
    #

    def build_anim_once(folder, speed=0.05, ext=".png", prefix=None):
        """
        folder 配下の連番画像から、ワンショット Animation を「その場で生成して返す」。

        - 返り値は displayable（Animation）
        - 呼ぶたびに新しい Animation を作るので、再表示で先頭フレームから再生されやすい
        """

        # Ren'Pyが管理しているファイル一覧から folder 配下の画像を集める
        frames = []
        for f in renpy.list_files():
            if not f.startswith(folder):
                continue
            if not f.lower().endswith(ext):
                continue

            if prefix is not None:
                fname = f.split("/")[-1]
                if not fname.startswith(prefix):
                    continue

            frames.append(f)

        # 連番順に並べる
        frames.sort()

        if not frames:
            raise Exception("build_anim_once: No frames found. folder='{}'".format(folder))

        # Animation に渡す引数を作る
        # 例: [img0, 0.05, img1, 0.05, img2]  ←最後が画像なので止まる
        args = []

        # 最後以外: (画像, delay)
        for f in frames[:-1]:
            args.append(f)
            args.append(speed)

        # 最後: 画像だけ（delayを付けない！）
        args.append(frames[-1])

        return Animation(*args)

    def play_anim_once(tag, folder, speed=0.05, layer="master", at_list=None, zorder=0, ext=".png", prefix=None):
        """
        指定 tag に、ワンショットアニメを「必ず先頭から」再生させる。

        - いったん hide してから show し直す（表示上の差分がなくても再生が走る）
        - at_list は [char_center] のようにリストで渡す
        """
        d = build_anim_once(folder, speed=speed, ext=ext, prefix=prefix)

        # すでに同じ tag が出ていても、確実にリセットする
        renpy.hide(tag, layer=layer)

        # 直後に show（what に displayable を渡す）
        renpy.show(tag, what=d, layer=layer, at_list=at_list, zorder=zorder)

        # 画面更新
        renpy.restart_interaction()

init python:

    def play_image(tag, image_name, at_list=None, layer="master", zorder=0, reset=True):
        """
        画像名ベースで、ループ/ワンショットを統一して表示するヘルパー。

        - image_name は Ren'Py の画像名（例: "yui idle", "yui happy once"）
        - reset=True なら、毎回 hide→show するのでワンショットが確実に先頭から再生される
        - ループ画像でも reset=True で問題なし（同じタグに確実に差し替えられる）
        """

        # ワンショットの「2回目が静止」問題はここで潰す
        if reset:
            renpy.hide(tag, layer=layer)

        # 画像名から displayable を参照して show する
        what = renpy.display.image.ImageReference(image_name)
        renpy.show(tag, what=what, layer=layer, at_list=at_list, zorder=zorder)

        # 画面を即更新
        renpy.restart_interaction()


# ------------　差分アニメ(ループ)　--------------------------------------------------------
# ここにディレクトリを置いておけば、通常画像と同じ要領で使えます。

    # make_anim("dash", "images/anim/dash/", 0.05)              

    
# # ------------　差分アニメ（ワンショット）　--------------------------------------------------------
# ループさせない場合はこんな感じで書いてください。
#
# $ play_anim_once("yui", "images/yui/happy/", speed=0.05, at_list=[char_center])
# $ play_anim_once("dash", "images/anim/dash/", speed=0.05, at_list=[char_center])
# 本当はループ画像と統一させたかったのですが、複雑になってしまった＆記述違うほうがわかりやすくね？と思って直接参照になってます。
# なんかアニメーションをループさせない方が難しかった。


# 公式の記述方法メモ
# # ユイ
# image yui happy once:
#     "images/yui/happy/frame_0000.png"
#     pause 0.05
#     "images/yui/happy/frame_0001.png"
#     pause 0.05
#     "images/yui/happy/frame_0002.png"
#     pause 0.05
#     "images/yui/happy/frame_0003.png"
#     pause 0.05
#     "images/yui/happy/frame_0004.png"
#     pause 0.05
#     "images/yui/happy/frame_0005.png"
#     pause 0.05
#     "images/yui/happy/frame_0006.png"
#     pause 0.05
#     "images/yui/happy/frame_0007.png"
#     pause 0.05
#     "images/yui/happy/frame_0008.png"
#     pause 0.05
#     "images/yui/happy/frame_0009.png"
#     pause 0.05
#     "images/yui/happy/frame_0010.png"
#     pause 0.05
#     "images/yui/happy/frame_0011.png"
#     pause 0.05
#     "images/yui/happy/frame_0012.png"
#     pause 0.05
#     "images/yui/happy/frame_0013.png"
#     pause 0.05
#     "images/yui/happy/frame_0014.png"
#     pause 0.05
#     "images/yui/happy/frame_0015.png"
#     pause 0.05
#     "images/yui/happy/frame_0016.png"
#     pause 0.05
#     "images/yui/happy/frame_0017.png"
#     pause 0.05
#     "images/yui/happy/frame_0018.png"
#     pause 0.05
#     "images/yui/happy/frame_0019.png"
#     pause 0.05