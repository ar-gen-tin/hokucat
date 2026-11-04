<p align="center">
  <img src="../../assets/hokucat.png" width="100" height="100" alt="Hokucat の黒猫と琥珀色の星">
</p>

<h1 align="center">Hokucat</h1>

<p align="center"><strong>macOS 用のライブ壁紙</strong></p>

<p align="center">
  <a href="../../README.md">English</a> · <a href="../../README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · 日本語 · <a href="README.ko.md">한국어</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.ar.md">العربية</a>
</p>

<p align="center"><strong><a href="https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/Hokucat-1.4.74.dmg">v1.4.74 プレビュー版をダウンロード</a></strong> · <a href="https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.74/SHA256SUMS.txt">SHA-256</a></p>

壁紙ライブラリの閲覧、プレビュー、利用できる設定の調整をひとつのウインドウで行えます。AI で自分だけの壁紙を作ることもできます。

<a href="../../assets/hokucat-demo.mp4"><img src="../../assets/hokucat-demo.gif" width="960" alt="Hokucat の猫の短いプレビュー。クリックすると編集版の紹介映像を再生します"></a>

[公式サイト](https://hokucat.com/) · [紹介映像を見る](../../assets/hokucat-demo.mp4) · [壁紙を作る](../ai-wallpapers.md) · [よくある質問](../faq.md)

*映像は編集して制作した壁紙の紹介です。プレビュー素材に登場する第三者の PC 向け作品はテスト専用です。[作者と作品の公開ページ](../credits.md)をご確認ください。*

<img src="../../assets/hokucat-dashboard.jpg" width="960" alt="ライブラリ、プレビュー、設定をまとめた Hokucat の壁紙ダッシュボード">

*1.4.73 レビュー版で撮影した壁紙ダッシュボードの実際の画面。*

## Hokucat を試す

**1.4.74 は Developer ID で署名されたプレビュー版**です。**macOS 13 以降**の **Apple シリコンと Intel** Mac に対応しています。Apple の公証はまだ完了しておらず、macOS が初回起動をブロックする場合があります。更新内容は[変更履歴](../../CHANGELOG.md)をご覧ください。

DMG をダウンロードして開き、Hokucat を Applications（アプリケーション）フォルダにドラッグしたら：

1. Applications（アプリケーション）フォルダから Hokucat を起動し、メニューバーで**壁紙ダッシュボード…**を選びます。
2. 壁紙を選択します。同じ画面でプレビューし、その作品で利用できる設定を調整します。
3. **壁紙を適用**をクリックします。複数のディスプレイを使っている場合は、先に適用先を選びます。

## 自分に合ったデスクトップに

- **探しやすいライブラリ。** 壁紙を検索し、コレクションを手動で並べ替えたり、名前順に整列したりできます。
- **プレビューと設定を同じ画面に。** 選択した作品と設定項目を一緒に確認できます。対応する動画では、適用前に表示のフィット方法、速度、左右反転を調整できます。
- **シンプルなライブラリ管理。** ドラッグで並べ替え、右クリックメニューからよく使う操作を実行し、確認のうえで読み込んだ壁紙を削除できます。元のファイルは元の場所に残ります。
- **Mac で使い慣れた操作。** メニューバーから Hokucat を使い、普段のデスクトップ操作を続けながら、猫の視線やドラッグできる星で遊べます。利用できる操作は壁紙ごとに異なります。
- **ディスプレイごとの選択。** 接続したディスプレイごとに異なる壁紙を設定できます。Hokucat は選択内容を記憶します。

アプリの表示言語は**英語、簡体字中国語、繁体字中国語、日本語、韓国語、ブラジルポルトガル語、スペイン語、フランス語、アラビア語**です。設定から切り替えられます。

## AI で壁紙を作る

Codex、Claude Code、Grok Bot のいずれかでオリジナルの無音ループ動画を作るか、使用許可のある動画を用意してください。[制作ガイド](../ai-wallpapers.md)にはプロンプトと実行可能なサンプルがあり、**壁紙ダッシュボード → 読み込む…**から開けるパッケージを作れます。

Package v1 は **PNG/JPEG 画像と無音の MP4/MOV/M4V 動画**に対応しています。AI は素材制作を手伝い、Hokucat は読み込んだファイルをローカルで再生します。一般的なインタラクティブ Web や Windows Scene のプロジェクト、リアルタイムのポインタ・音声入力、API やエージェントへのリアルタイム接続は、このパッケージ形式の対象外です。一部の内蔵壁紙や移植された壁紙には、それぞれ独自のインタラクティブ機能があります。

[`examples/make-wallpaper.py`](../../examples/make-wallpaper.py) が生成するアニメーションは、このリポジトリ用に作られた自己完結型のサンプルです。テスト用に紹介している第三者の PC 向け壁紙とは別のものです。

## 質問、フィードバック、クレジット

互換性や読み込み方法は[よくある質問](../faq.md)をご覧ください。[問題を報告する](https://github.com/ar-gen-tin/hokucat/issues)際は、macOS と Hokucat のバージョン、再現手順を添えてください。ドキュメント、翻訳、サンプルの改善も歓迎します。[貢献ガイド](../../CONTRIBUTING.md)をご覧ください。

このリポジトリには公開ドキュメント、紹介素材、制作サンプルが含まれています。**Mac アプリ全体のソースコードは含まれていません。** 記録済みのプレビュー版の変更は[変更履歴](../../CHANGELOG.md)で確認できます。

Hokucat は **0xCodila (Bodila51)** の [Grok Bot Wallpaper](https://github.com/Bodila51/grokbot-wallpaper) をもとに発展しました。第三者の作品には引き続き各作者を明記しています。テスト版での展示は、再配布の許可を意味するものではありません。[プロジェクトの沿革と素材のクレジット](../credits.md)
