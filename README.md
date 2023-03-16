# TgeN

Creation of templates for various projects / 色々なプロジェクト用のテンプレート作成

## Description / 説明

プロジェクトのフォルダーの雛形を対話式で作成できます  
JSON ファイルに雛形を先に構成することができます  
フォルダーのアイコンも設定できます

![image](https://user-images.githubusercontent.com/86721991/225624188-57b8b5f2-14b9-480d-921c-17de5f0fea80.png)

## Install / インストール

_[path/to/your/programs]_ は, 自分でお好きなフォルダーに置き換えてください

```bash
> cd [path/to/your/programs]
> git clone https://github.com/wappon-28-dev/TgeN.git
> cd TgeN
> pip install -r requirements.txt
> python main.py
```

### Registering to environment variables / 環境変数への登録

念のため, GUI で登録することをおすすめしますが, 一応コマンドもおいておきます

#### Powershell

```bash
> $new_dir = [path/to/your/programs]/TgeN
> $new_path = [Environment]::GetEnvironmentVariable("Path", "User")
> $new_path += ";$new_dir"
> [Environment]::SetEnvironmentVariable("Path", $new_path, "User")
```

#### Cmd

```bash
> setx path "%path%;[path/to/your/programs]/TgeN"
```
