# Ren'Py `SetVariable` まとめ

## 1. `SetVariable` とは？

`SetVariable` は、**screen（画面）側から変数を書き換えるための Action クラス**です。

通常 script では：

```renpy
$ flag = True
```

と書きますが、screen内では `$` は使えません。

そこで使うのが：

```renpy
action SetVariable("flag", True)
```

---

## 2. 基本構文

```renpy
action SetVariable("変数名", 値)
```

例：

```renpy
textbutton "ON":
    action SetVariable("music_on", True)
```

---

## 3. なぜ文字列で変数名を書くの？

```renpy
SetVariable("flag", True)
```

ここで `"flag"` と書くのは、

> 変数名を文字列で指定して、store内の変数を書き換える

という仕組みだからです。

Ren'Pyは内部的に `store.flag = True` のような処理をしています。

---

## 4. よくある使い方

---

### ① フラグを立てる

```renpy
textbutton "見る":
    action SetVariable("seen_secret", True)
```

→ その後 script 側で：

```renpy
if seen_secret:
    jump secret_route
```

---

### ② 値を切り替える（トグル）

```renpy
textbutton "音楽ON/OFF":
    action SetVariable("music_on", not music_on)
```

---

### ③ メニュー選択と同時に消す（今回の例）

```renpy
action [
    SetVariable("choice_comment", ""),
    action
]
```

---

### ④ 数値を増減する

```renpy
textbutton "+1":
    action SetVariable("score", score + 1)
```

---

## 5. 複数アクションをまとめて実行

Actionはリストで書けます：

```renpy
action [
    SetVariable("flag", True),
    Jump("next_scene")
]
```

順番に実行されます。

---

## 6. `default` との関係

変数は事前に `default` しておくと安全です：

```renpy
default score = 0
```

理由：

* セーブ対応
* 未定義エラー防止
* ロールバック対応

---

## 7. よく似たものとの違い

### `SetScreenVariable`

screen内ローカル変数を書き換える場合はこちら：

```renpy
SetScreenVariable("local_var", 10)
```

→ screenの外では使えません。

---

### `ToggleVariable`

よく使うトグル専用アクション：

```renpy
action ToggleVariable("music_on")
```

内部的には：

```renpy
music_on = not music_on
```

と同じ。

---

## 8. 実用テンプレ例

### ✔ 設定画面風UI

```renpy
default auto_mode = False

screen settings_menu():

    vbox:
        text "オートモード"

        textbutton "ON":
            action SetVariable("auto_mode", True)

        textbutton "OFF":
            action SetVariable("auto_mode", False)
```

---

### ✔ ステータス表示UI

```renpy
default affection = 0

screen affection_debug():

    frame:
        vbox:
            text "好感度: [affection]"

            textbutton "+10":
                action SetVariable("affection", affection + 10)
```

---

## 9. 内部的な考え方

Ren'PyのUIは

> Actionオブジェクトを実行する仕組み

になっています。

`SetVariable` はその中のひとつ。

つまり：

* script → Python実行
* screen → Action実行

という世界が分かれています。

ここを理解すると、Ren'Pyがかなり整理されます。

---

# まとめ

`SetVariable` は

✔ screenからstore変数を変更できる
✔ UI制御の中心
✔ フラグ管理に便利
✔ 複数Actionと組み合わせ可能

---

