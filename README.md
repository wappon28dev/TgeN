# TgeN

Creation of templates for various projects / 色々なプロジェクト用のテンプレート作成

## Description / 説明

プロジェクトのフォルダーの雛形を対話式で作成できます  
[JSON ファイル](./src/tgen/assets/manifests/default/manifest.json)に雛形を先に構成することができます  
フォルダーのアイコンも設定できます

![image](https://user-images.githubusercontent.com/86721991/225624188-57b8b5f2-14b9-480d-921c-17de5f0fea80.png)

## Install / インストール

``` bash
$ pip install git+https://github.com/wappon28dev/TgeN.git
```

## Usage / 使い方

1. エクスプローラーで, プロジェクトを作成したいフォルダーの中で右クリック → `ターミナルで開く`  
   ![image](https://user-images.githubusercontent.com/86721991/225652767-44af8a0b-f722-4748-8669-d91cdc55109b.png)

2. ターミナルが開くので, `tgen` (または, `tn`) と入力

   - そのディレクトリ内にあるディレクトリが一覧表示されます
   - プロジェクトの名前 (= ディレクトリの名前) に, `既にあるディレクトリの数 + 1` が自動で付与されます  
     (まあ連番を消してもいいけど...)

   ![image](https://user-images.githubusercontent.com/86721991/225655028-3b12928d-0b71-464f-b84e-0d4d058373dd.png)

3. マニフェストは `default` で, ディレクトリ名の言語を選ぶ

   ![image](https://user-images.githubusercontent.com/86721991/225657541-9dad0882-a8cc-443b-a9a4-64a2a0642b8c.png)


   ### `default` マニフェストで作成されるディレクトリ一覧
   | ja               | 説明                                 |
   | ---------------- | ------------------------------------ |
   | ar\_完成         | 完成したファイルを入れるディレクトリ |
   | as\_素材         | 素材を入れるディレクトリ             |
   | br\_分岐         | 分岐させたい時に使うディレクトリ     |
   | ol\_バックアップ | 古いファイルを入れるディレクトリ     |
   | te\_テスト       | テスト用のディレクトリ               |
   | wo\_作業         | 作業用のディレクトリ                 |

   | en        | 説明                          |
   | --------- | ----------------------------- |
   | artifacts | Directory for completed files |
   | assets    | Directory for material        |
   | branch    | Directory for branches        |
   | old       | Directory for old files       |
   | test      | Directory for testing         |
   | work      | Directory for work            |

4. "ディレクトリ"と呼ぶか, "フォルダー" と呼ぶかを選択して生成！
   - アイコン付きで生成されます！
   ![image](https://user-images.githubusercontent.com/86721991/225659480-1b68a983-25de-4f9b-b47c-4d01987c28f1.png)

   - 生成されたディレクトリにポイントすると, 上の表の説明が見れます
   ![image](https://user-images.githubusercontent.com/86721991/225661574-b428fa7b-ac3b-43ef-8456-7a84a31f7674.png)

## Uninstall / アンインストール
``` bash
$ pip uninstall TgeN
```

## License / ライセンス
[MIT License](./LICENSE)
