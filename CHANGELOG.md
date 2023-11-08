# Changelog
現在の最新バージョンは 2.4.0 です。

## [開発中](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/tree/develop)

### 機能追加

- CHANGELOG.mdを新規作成。

### 仕様変更

### 非推奨対応

### 削除対応

### バグ修正

### セキュリティ対応


## [2.4.0](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/releases/tag/v2.4) - 2023-08-29

### バグ修正

- Dockerfileに記載したプロジェクト名にブランチ名が含まれている [#14](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/14)
- 入退室通知は全サーバーを見ている [#4](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/4)
- 入退室通知がされない [#20](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/20)

## [2.3.0](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/releases/tag/v2.3) - 2023-08-25

### 機能追加

- ボットのDocker化対応（ [#8](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/8) ）

### 仕様変更

- マインクラフトサーバーのipアドレスがipv6になる（ [#10](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/10) ）

### セキュリティ対応

- リファクタリング対応（ [#2](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/issues/2) ）


## [2.2.1](https://github.com/Kotoya1852/community-place-for-cats-discord-bot/releases/tag/v2.2) - 2023-08-15

### 仕様変更

- 環境に関するリテラル値を環境変数から取得するよう修正
- Githubで公開し、publicにソースが閲覧できるよう整備
  - これ以降の更新履歴をGithubで管理する。

## 2.2.0 - 2023-08-11

### 機能追加

- イベント参加・辞退コマンドを追加（`!join` / `!leave`）
- イベント情報取得コマンドを追加（`!info`）

### 仕様変更

- ボットステータスのプレゼンス情報をカスタムアクティビティクラスに修正しました。（これ以降、`プレイ中`が削除される）

## 2.1.0 - 2023-07-30

### 機能追加

- コマンドを追加（!help）

### バグ修正

- 入室時に通知が来ないバグを修正


## 2.0.0 - 2023-07-23

### 機能追加

- コマンド機能を追加（!ping）
- ボットステータスを追加（固定文字 `稼働中にゃ！`）

### 仕様変更

- 全ユーザーの通知メッセージがランダムで改変されるようになりました

## 1.3.0 - 2022-08-31

### 機能追加

- 一部ユーザーに対して通知内容が改変されるようになりました

## 1.2.0 - 2022-08-04

### 仕様変更

- 新しくチャンネルを作成しても自動で通知対象になるように修正

## 1.1.0 - 更新日時不明

- 修正内容不明

## 1.0.0 - 2021-08-31

- 新規作成

<!-- Versions -->
[unreleased]: https://github.com/Author/Repository/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/Author/Repository/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/Author/Repository/releases/tag/v0.0.1
