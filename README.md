# kotodama
動詞の基本形を、動詞と助動詞の組み合わせ形に変換します
2020.04 日本語における文生成器(surface realizer)を目指していますが、現状は動詞のみの取扱です

## how to use
### install
```
$ pip install kotodama
```

### 動詞と助動詞を組み合わせる
```python:sample.py
from kotodama import kotodama

# auxiliary_verbはset型で何個も引数を持たせて構わない
auxiliary_verb = {"過去","自分の希望"}
verb = "過ごす"
print(kotodama.transformVerb(verb,auxiliary_verb))
# output 過ごしたかった
```
#### 対応している助動詞一覧
基本は以下のサイト様に準拠しています（一部プログラム化する都合上修正を加えています）
https://www.kokugobunpou.com

|  引数 |  単語タイプ | その他の表記　
| ---- | ---- | ---- |
|  使役  |  助動詞  | せる・させる
|  可能  |  助動詞  | れる・られる/自発/尊敬
|  受け身  |  助動詞  | れる・られる/自発/尊敬
|  自分の希望  |  助動詞  | たい・たがる/希望
|  他人の希望  |  助動詞  | たい・たがる/希望
|  です・ます  |  助動詞  | です・ます/丁寧
|  否定  |  助動詞  | ない・ぬ/打ち消し
|  過去  |  助動詞  | た・だ/完了/存続/確認
|  推定  |  助動詞  | らしい
|  伝聞  |  助動詞  | そうだ
|  様態  |  助動詞  | そうだ
|  例示  |  助動詞  | ようだ/たとえ
|  勧誘  |  助動詞  | よう・う/推量/意思
|  て  |  接続助詞  | で

#### 対応していない助動詞一覧
|  引数 |  単語タイプ | その他の表記　
| ---- | ---- | ---- |
| 仮定  | 活用形| 
| 断定　| 助動詞| だ

#### エラーとなる助動詞の組み合わせ
| 助動詞１ | 助動詞２ | 理由　
| ---- | ---- | ---- |
| 可能 | 受け身 | どちらも「れる・られる」だから重複する
| 可能| 勧誘| 勧誘するような行為はそもそも実行可能ではなくてならないため意味が重複する
| 可能| 自分の希望・他人の希望 | したいかどうかは発言者本人にとっては自明なため、可能表現に意味がなくなる
| です・ます|て|文末表現は一文につき一つしか使えない
| です・ます| 勧誘| 文末表現は一文につき一つしか使えない
| て| 勧誘| 文末表現は一文につき一つしか使えない
| 勧誘| 過去| 勧誘は未来の事象に対してしか使えない
| 勧誘| 推定|　勧誘している時点で、勧誘するという行為は確定している
| 勧誘| 伝聞|　勧誘は一人称でしか使えない
| 自分の希望| 他人の希望| どちらも「たり・たがる」なので重複する
| 様態・伝聞| 例示|　例示するこういは一人称で対話相手に示すため、伝聞表現ができない
| 様態| 伝聞|　どちらも「そうだ」だから重複する

####  対応している動詞
以下のサイト様の日本語における常用漢字の動詞に対応しています（一部手動で書き加えています）
http://assets.flips.jp/files/users/ichimai-quiz/joyo.pdf

具体的な対応動詞は以下のファイルを見てください。対応動詞は随時更新していきます
https://github.com/tennmoku71/kotodama/blob/master/kotodama/data/kotodama_dic.csv

--------------------------------------
## ユーザ辞書の追加方法

以下のフォーマットに従い、kotodama_dic.csvの末尾に次の一行を追加してください

```
[基本表記],[活用する述語],[形容詞or動詞],[活用タイプ]
```
- 基本表記：transformVerbの第一引数に合致する述語。複合動詞(見回る, 押し入る, 入れ替える)が入ることもできる
- 活用する述語：基本表記と同じ。ただし基本表記が複合動詞の場合は後ろにある述語を入れる必要がある。基本表記の活用する述語は表記的に後方一致している必要がある
 - 良い例 : 基本表記＝押し入る, 活用する述語=入る
 - 悪い例 : 基本表記＝押し入る, 活用する述語=いる 
- 形容詞 or 動詞 : 現在は動詞のみ対応
- 活用タイプ：[Juman++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)の表記に対応しています

## 複合動詞に対応させる

本ライブラリに分かち書きエンジンを読みこませることで複合動詞にも対応させることができます

```
複合動詞対応前　○見る　×見てみる　×立ち向かう
複合動詞対応語　○見る　○見てみる　○立ち向かう
```

```
# how to activate

# nagisaを使う場合
import nagisa
kotodama.setSegmentationEngine(kotodama.SegmentationEngine.NAGISA, nagisa)

# janomeを使う場合
from janome.tokenizer import Tokenizer
tokenizer = Tokenizer()
kotodama.setSegmentationEngine(kotodama.SegmentationEngine.JANOME, tokenizer)

# jumanppを使う場合(jumanでも同様)
from pyknp import Juman
juman = Juman()
kotodama.setSegmentationEngine(kotodama.SegmentationEngine.JUMAN, juman)

```

## contributeのお願い
動詞の更新やバグの発見、プログラムの改良などに協力してくれる方を募集しています
下記連絡先に一方いただけると嬉しいです

## License
MIT License

## reference
- Hajime Morita, Daisuke Kawahara and Sadao Kurohashi: Morphological Analysis for Unsegmented Languages using Recurrent Neural Network Language Model, Proceedings of EMNLP 2015: Conference on Empirical Methods in Natural Language Processing, pp.2292-2297, (2015.9.17). pdf
- 森田一, 黒橋 禎夫: RNN 言語モデルを用いた日本語形態素解析の実用化, 情報処理学会 第78回全国大会, 慶應義塾大学 矢上キャンパス, (2016.3.10).
- http://assets.flips.jp/files/users/ichimai-quiz/joyo.pdf
- https://www.kokugobunpou.com

## contact
Name：大平義輝
Email：ohira.yoshiki@irl.sys.es.osaka-u.ac.jp
