# Apple Music Library to Spotify Migration

このプログラムは、Apple Music のライブラリから曲データを取り出し、Spotify に移すためのものです。

## 手順

### 1. Apple Music のライブラリから曲データを取り出す

#### (Mac の場合)

1. Apple Music を開きます。
2. 「ファイル」->「ライブラリ」->「プレイリストを書き出し」を選択します。

### 2. ミュージック.xml の編集

ミュージック.xml から

```xml
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
```

の２行と

```xml
</plist>
```

を削除します

### 3. Spotify に曲データを移す

1. Spotify API に登録します。[Spotify Developer](https://developer.spotify.com/documentation/web-api)から API キーを取得します。
2. 取得した API キーを`apptospot.py`に書き込みます。

## インストール

```bash
pip install -r requirements.txt
```

## 使い方

1. `apptospot.py`を実行します。

```bash
python apptospot.py
```

2. プログラムが実行され、Apple Music のライブラリから曲データが取り出され、Spotify に移されます。

3. 自動で Sporify に追加できなかった曲のリストが最後に出力されます。
