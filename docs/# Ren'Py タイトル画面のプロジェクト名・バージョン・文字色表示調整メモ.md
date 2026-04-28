# Ren'Py タイトル画面のプロジェクト名・バージョン・文字色表示調整メモ

---

## 目的
- タイトル画面右下に表示される  
  - プロジェクト名  
  - バージョン表記  
を **意図通りに制御**できるようにする。

---

## 1. プロジェクト名の正体と変更方法

### 表示に使われている変数
- `config.name`

### 定義場所（標準）
**game/options.rpy**

```renpy
define config.name = _("魔人の棲む塔")
````

* `_()` は翻訳対応用
* `[config.name!t]` の `!t` は「翻訳して表示」

---

## 2. バージョン表記の正体と変更方法

### 表示に使われている変数

* `config.version`

### 定義場所（標準）

**game/options.rpy**

```renpy
define config.version = "1.0"
```

### 運用例

* 軽微な修正：`1.0.1`
* 機能追加　：`1.1.0`
* 大規模変更：`2.0.0`

※ 命名規則は任意だが、制作ログ的におすすめ。

---

## 3. メインメニューで表示されていたコード

**screen main_menu()** 内のこの部分：

```renpy
if gui.show_name:

    vbox:
        style "main_menu_vbox"

        text "[config.name!t]":
            style "main_menu_title"

        text "[config.version]":
            style "main_menu_version"
```

* `config.name` → プロジェクト名
* `config.version` → バージョン
* `gui.show_name` → 表示ON/OFFのスイッチ

---

## 4. 表示のON / OFF を制御するスイッチ

### 定義場所

**game/gui.rpy**

```renpy
define gui.show_name = True
```

### 挙動

* `True`  → プロジェクト名・バージョンを表示
* `False` → 表示しない

```renpy
define gui.show_name = False
```

👉 screen 側を触らずに一括制御できる。

---

## 5. 「バージョンだけ」表示する方法

### main_menu でプロジェクト名だけコメントアウト

```renpy
if gui.show_name:

    vbox:
        style "main_menu_vbox"

        # text "[config.name!t]":
        #     style "main_menu_title"

        text "[config.version]":
            style "main_menu_version"
```

→ 右下に `V1.0` など、最小限の情報だけ表示できる。

---

## 6. 文字色の変更方法

### 方法A：その場で指定（簡単）

```renpy
text "[config.version]":
    color "#ffffff"
```

---

### 方法B：style でまとめて管理（おすすめ）

```renpy
style main_menu_version:
    color "#dddddd"
```

* `gui.rpy` や `screens.rpy` に定義されていることが多い
* 同じ style を使っている箇所を一括変更できる

---

### 方法C：アウトラインで可読性を上げる（実戦向き）

```renpy
style main_menu_version:
    outlines [(1, "#00000080", 0, 0)]
```

* 明暗どちらの背景でも読める
* 色を変えなくても安定する

---

## 7. 実務的な結論

* タイトルは **ロゴで見せる**
* 情報は **必要最小限**
* バージョンだけ右下に表示するのは完成版として自然
* `gui.show_name` を知っていると管理が楽

---

