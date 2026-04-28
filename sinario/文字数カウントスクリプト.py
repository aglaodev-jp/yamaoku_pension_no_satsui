"""
Markdown (.md) ファイルの文字数をカウントするスクリプト

・絶対パスでファイルを指定
・UTF-8で読み込み
・ファイルが存在しない場合のエラーハンドリング付き
"""

from pathlib import Path


def count_characters(file_path: str) -> int:
    """
    指定された Markdown ファイルの文字数を返す関数

    Parameters
    ----------
    file_path : str
        絶対パスで指定された .md ファイル

    Returns
    -------
    int
        文字数
    """

    path = Path(file_path)

    # ファイル存在確認
    if not path.exists():
        raise FileNotFoundError(f"指定されたファイルが存在しません: {file_path}")

    # 拡張子確認
    if path.suffix.lower() != ".md":
        raise ValueError("指定されたファイルは .md ファイルではありません")

    # ファイル読み込み（UTF-8）
    with path.open("r", encoding="utf-8") as f:
        content = f.read()

    # 文字数カウント
    return len(content)


if __name__ == "__main__":
    # ここに絶対パスを入力してください
    absolute_path = r""

    try:
        char_count = count_characters(absolute_path)
        print(f"文字数: {char_count}")
    except Exception as e:
        print(f"エラー: {e}")