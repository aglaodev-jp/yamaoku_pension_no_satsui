# CH_00_bg_movies.rpy

# ペンション外観（ループ）
image bg movie_loop_1 = Movie( play="movies/bg/bg_loop_1.webm", loop=True )
# モンスター（ループ）
image bg movie_loop_2 = Movie( play="movies/bg/bg_loop_2.webm", loop=True )
image bg movie_loop_3 = Movie( play="movies/bg/bg_loop_3.webm", loop=True )
image bg movie_loop_4 = Movie( play="movies/bg/bg_loop_4.webm", loop=True )
# デジタルサイネージ（ループ）
image bg movie_loop_5 = Movie( play="movies/bg/bg_loop_5.webm", loop=True )
# レストラン（ループ）
image bg movie_loop_6 = Movie( play="movies/bg/bg_loop_6.webm", loop=True )

# ハンバーグ（ループ）
image bg movie_loop_7 = Movie( play="movies/bg/bg_loop_7.webm", loop=True )

# ------- つかいかた ------------------------------------------------
# ループ動画の背景はshowで表示。sceneだとなぜかできない。
    # show bg movie_loop_1 at fullscreen_bg 
    # with fade

# 黒い画面などでかぶせて消す感じ。（たぶんhideを使わなくても大丈夫だと思う）
    # scene black 
    # with dissolve
    # とか
    # scene black
    # whith fade
# with dissolve → 「じわっと重なって切り替わる」
# with fade → 「一度暗転（または明転）してから切り替わる」
