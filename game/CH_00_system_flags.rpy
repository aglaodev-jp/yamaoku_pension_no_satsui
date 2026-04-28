# system_flags.rpy 
# ------------------------------------------------------------
# system_flags.rpy
# クリア状態を「周回をまたいで」保存する（persistent）
# ------------------------------------------------------------

init python:
    # 初回起動時は persistent に項目が無いので作る
    if not hasattr(persistent, "endings_cleared"):
        persistent.endings_cleared = []  # 例: ["A", "C"]

    def mark_ending(ending_id: str) -> None:
        """
        クリア済みエンディングを persistent に記録する。

        ending_id:
            "A", "B", "C" のような短いIDを想定。
        """
        # 念のため入れ物チェック（事故防止）
        if not hasattr(persistent, "endings_cleared"):
            persistent.endings_cleared = []

        # 二重登録防止
        if ending_id not in persistent.endings_cleared:
            persistent.endings_cleared.append(ending_id)

        # すぐ書き込み（テスト中も安心）
        renpy.save_persistent()

# ------------------------------------------------------------
# persistent の安全な初期化
# screens.rpy の"メインメニュースクリーンとゲームメニュースクリーン"に
# "【デバッグ】クリア初期化"項目があるので、公開版は削除 or コメントアウト
# ------------------------------------------------------------
init python:
    # 属性が無い or None ならリストで作る
    if (not hasattr(persistent, "endings_cleared")) or (persistent.endings_cleared is None):
        persistent.endings_cleared = []
        renpy.save_persistent()

init python:
    def reset_clears():
        """
        クリア済みエンディング記録を全消去する（テスト用）
        """        
        persistent.endings_cleared = []
        renpy.save_persistent()
        renpy.notify("クリア記録をリセットしました。")
