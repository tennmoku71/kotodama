# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2020 Yoshiki Ohira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import os
import warnings
from enum import Enum

FILE_PATH = os.path.dirname(__file__)+"/data/kotodama_dic.csv"
ENCODING = "utf-8"
kotodama_dic = {}
def load():
    file = open(FILE_PATH,encoding=ENCODING,mode = "r")
    for ele in file:
        ele_list = ele.strip().split(",") 
        key = ele_list[0]
        value = ele_list[1:]
        kotodama_dic[key] = value
    file.close()
load()

def add_db(mrph):
    global kotodama_dic
    # kotodama dicに追加
    key = mrph.genkei
    if not key in kotodama_dic:
        value = [mrph.genkei,mrph.hinsi,mrph.katuyou1]
        kotodama_dic[key] = value
        # 辞書ファイルにも追加
        with open(FILE_PATH,encoding=ENCODING,mode='a') as f:
            print("\n%s,%s" % (key,",".join(value)), file=f)

class nihongo:

    hiragana = {
        "ア行":["あ","い","う","え","お"],
        "カ行":["か","き","く","け","こ"],
        "ガ行":["が","ぎ","ぐ","げ","ご"],
        "サ行":["さ","し","す","せ","そ"],
        "ザ行":["ざ","じ","ず","ぜ","ぞ"],
        "タ行":["た","ち","つ","て","と"],
        "ダ行":["だ","ぢ","づ","で","ど"],
        "ナ行":["な","に","ぬ","ね","の"],
        "ハ行":["は","ひ","ふ","へ","ほ"],
        "バ行":["ば","び","ぶ","べ","ぼ"],
        "パ行":["ぱ","ぴ","ぷ","ぺ","ぽ"],
        "マ行":["ま","み","む","め","も"],
        "ヤ行":["や","い","ゆ","え","よ"],
        "ラ行":["ら","り","る","れ","ろ"],
        "ワ行":["わ","い","う","え","お"]
    }

    def get_index(c):
        global hiragana
        for boin in nihongo.hiragana:
            if c in nihongo.hiragana[boin]:
                return boin,nihongo.hiragana[boin].index(c)

    def get_char(boin,shin_index):
        return nihongo.hiragana[boin][shin_index]
    
    def change_shiin(c, shiin_index):
        boin,_ = nihongo.get_index(c)
        return nihongo.get_char(boin,shiin_index)
    
# verbType 母音動詞 子音動詞マ行 子音動詞ワ行 子音動詞カ行 子音動詞ラ行 子音動詞サ行 子音動詞タ行 子音動詞ガ行 子音動詞カ行促音便形 カ変動詞来 サ変動詞
# conjugationForm 未然否定nai 未然否定zu 未然使役 未然意思 未然可能 連用希望 連用過去 終止 連体 仮定 連用音便
def transformConjugationForm(verb, verbType, conjugationForm):

    transformed = verb
    if verbType=="母音動詞":
        if conjugationForm == "終止":
            transformed = verb
        elif conjugationForm == "連体":
            transformed = verb
        else:
            transformed = verb[0:-1]

    elif verbType.startswith("子音動詞"):

        # 活用する母音を取得する
        boin = None
        if verbType[4:6] in nihongo.hiragana:
            # 母音が活用形辞書から取得できる場合はそれを採用
            boin = verbType[4:6]
        else:
            #ない場合は終了系の最後のひらがなから推測する
            boin,_ = nihongo.get_index(verb[-1])

        if conjugationForm.startswith("未然否定"):
            if verb=="有る" or verb=="ある":
                transformed = ""
            else:
                transformed = verb[0:-1] + nihongo.get_char(boin,0)
        elif conjugationForm == "未然意思":
            transformed = verb[0:-1] + nihongo.get_char(boin,4)
        elif conjugationForm == "未然可能":
            transformed = verb[0:-1] + nihongo.get_char(boin,3)
        elif conjugationForm == "未然使役":
            transformed = verb[0:-1] + nihongo.get_char(boin,0)    
        elif conjugationForm == "連用希望":
            transformed = verb[0:-1] + nihongo.get_char(boin,1)
        elif conjugationForm == "連用過去":
            if verbType.endswith("カ行促音便形"):
                transformed = verb[0:-1] + "っ"
            elif verbType.endswith("カ行"):
                transformed = verb[0:-1] + "い"
            elif verbType.endswith("ガ行"):
                transformed = verb[0:-1]  + "い"
            elif verbType.endswith("サ行"):
                transformed = verb[0:-1]  + "し"
            elif verbType.endswith("タ行"):
                transformed = verb[0:-1]  + "っ"
            elif verbType.endswith("ナ行"):
                transformed = verb[0:-1]  + "ん"
            elif verbType.endswith("バ行"):
                transformed = verb[0:-1]  + "ん"
            elif verbType.endswith("マ行"):
                transformed = verb[0:-1]  + "ん"
            elif verbType.endswith("ラ行"):
                transformed = verb[0:-1]  + "っ"
            elif verbType.endswith("ワ行"):
                transformed = verb[0:-1]  + "っ"
            elif verbType.endswith("ワ行文語音便形"):
                transformed = verb[0:-1]  + "う"                

        elif conjugationForm == "仮定":
            transformed = verb[0:-1] + nihongo.get_char(boin,3)   

    elif verbType.startswith("サ変動詞"):
        transformed = verb.replace("する","")
        if conjugationForm == "未然否定nai" or conjugationForm == "未然意思":
            transformed+="し"
        elif conjugationForm == "未然否定zu":
            transformed+="せ"
        elif conjugationForm == "未然使役":
            transformed+="さ"
        elif conjugationForm == "未然可能":
            transformed+="でき"
        elif conjugationForm.startswith("連用"):
            transformed+="し"
        elif conjugationForm.startswith("終止"):
            transformed+="する"
        elif conjugationForm.startswith("連体"):
            transformed+="する"
        elif conjugationForm.startswith("仮定"):
            transformed+="すれ"
        elif conjugationForm.startswith("命令"):
            transformed+="しろ"

    elif verbType.startswith("カ変動詞"):
        transformed = verb.replace("来る","").replace("くる","")
        if conjugationForm.startswith("未然"):
            transformed+="こ"
        elif conjugationForm.startswith("連用"):
            transformed+="き"
        elif conjugationForm.startswith("終止"):
            transformed+="くる"
        elif conjugationForm.startswith("連体"):
            transformed+="くる"
        elif conjugationForm.startswith("仮定"):
            transformed+="くれ"
        elif conjugationForm.startswith("命令"):
            transformed+="こい"

    elif verbType.startswith("ナ形容詞"):
        transformed = verb[0:-1]
        if conjugationForm in ["未然否定zu", "未然使役", "未然意思", "未然可能"]:
            transformed+=""
        elif conjugationForm.startswith("連用過去"):
            transformed+=""
        elif conjugationForm.startswith("連用希望") or conjugationForm=="未然否定nai":
            transformed+="では"
        elif conjugationForm.startswith("終止"):
            transformed+=""
        elif conjugationForm.startswith("連体"):
            transformed+=""
        elif conjugationForm.startswith("仮定"):
            transformed+=""

    elif verb=="いい":
        transformed = ""
        if conjugationForm in ["未然否定zu", "未然使役", "未然意思", "未然可能"]:
            transformed+="よかろ"
        elif conjugationForm.startswith("連用過去"):
            transformed+="よかっ"
        elif conjugationForm.startswith("連用希望") or conjugationForm=="未然否定nai":
            transformed+="よく"
        elif conjugationForm.startswith("終止"):
            transformed+="いい"
        elif conjugationForm.startswith("連体"):
            transformed+="いい"
        elif conjugationForm.startswith("仮定"):
            transformed+="よけれ"

    elif verbType.startswith("判定詞"):
        transformed = verb[0:-1]
        if conjugationForm in ["未然否定zu", "未然使役", "未然意思", "未然可能"]:
            transformed+=""
        elif conjugationForm.startswith("連用過去"):
            transformed+=""
        elif conjugationForm.startswith("連用希望") or conjugationForm=="未然否定nai":
            transformed+="では"
        elif conjugationForm.startswith("終止"):
            transformed+=""
        elif conjugationForm.startswith("連体"):
            transformed+=""
        elif conjugationForm.startswith("仮定"):
            transformed+=""

    elif "形容詞" in verbType:
        transformed = verb[0:-1]
        if conjugationForm in ["未然否定zu", "未然使役", "未然意思", "未然可能"]:
            transformed+="かろ"
        elif conjugationForm.startswith("連用過去"):
            transformed+="かっ"
        elif conjugationForm.startswith("連用希望") or conjugationForm=="未然否定nai":
            transformed+="く"
        elif conjugationForm.startswith("終止"):
            transformed+="い"
        elif conjugationForm.startswith("連体"):
            transformed+="い"
        elif conjugationForm.startswith("仮定"):
            transformed+="けれ"
    return transformed

# formatList　可能　受け身　使役　過去　断定　否定　推定　様態　伝聞　例示　勧誘　打ち消し　自分の希望　他人の希望　前提確認　て　です・ます　終止　仮定　ください
# verbType 母音動詞 子音動詞マ行 子音動詞ワ行 子音動詞カ行 子音動詞ラ行 子音動詞サ行 子音動詞タ行 子音動詞ガ行 子音動詞カ行促音便形 カ変動詞来 サ変動詞
# conjugationForm 未然否定nai 未然否定zu 未然使役 未然意思 連用希望 連用過去 終止 連体 仮定 連用音便
class phrase:

    def __init__(self,word, mizen, renyo, syusi, rentai, katei, meirei,before_word_type,conjugation):
        self.word = word
        self.mizen = mizen
        self.renyo = renyo
        self.syusi = syusi
        self.rentai = rentai
        self.katei = katei
        self.meirei = meirei
        self.before_word_type = before_word_type
        self.conjugation = conjugation
        
    
    
phrases = []
# 直前がサ変動詞なら”れ”を追加する
#phrases.append(phrase(word="可能",mizen="",renyo="",syusi="る",rentai="る",katei="れ",meirei="ろ",before_word_type="サ変動詞",conjugation="未然可能"))
# http://www.gengoj.com/_UPLOAD/post/179.pdf
phrases.append(phrase(word="可能",mizen="られ",renyo="られ",syusi="られる",rentai="られる",katei="られれ",meirei="られろ",before_word_type="母音動詞",conjugation="未然可能"))
phrases.append(phrase(word="可能",mizen="れ",renyo="れ",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="子音動詞",conjugation="未然可能"))
phrases.append(phrase(word="可能",mizen="",renyo="",syusi="る",rentai="る",katei="れ",meirei="ろ",before_word_type="サ変動詞",conjugation="未然可能"))
phrases.append(phrase(word="可能",mizen="られ",renyo="られ",syusi="られる",rentai="られる",katei="られれ",meirei="られろ",before_word_type=None,conjugation="未然可能"))
phrases.append(phrase(word="使役",mizen="せ",renyo="せ",syusi="せる",rentai="せる",katei="せれ",meirei="せろ",before_word_type="子音動詞",conjugation="未然使役"))
phrases.append(phrase(word="使役",mizen="せ",renyo="せ",syusi="せる",rentai="せる",katei="せれ",meirei="せろ",before_word_type="サ変動詞",conjugation="未然使役"))
phrases.append(phrase(word="使役",mizen="させ",renyo="させ",syusi="させる",rentai="させる",katei="させれ",meirei="させろ",before_word_type=None,conjugation="未然使役"))
phrases.append(phrase(word="受け身",mizen="れ",renyo="れ",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="子音動詞",conjugation="未然使役"))
phrases.append(phrase(word="受け身",mizen="れ",renyo="れ",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="サ変動詞",conjugation="未然使役"))
phrases.append(phrase(word="受け身",mizen="られ",renyo="られ",syusi="られる",rentai="られる",katei="られれ",meirei="られろ",before_word_type=None,conjugation="未然使役"))
#動詞の直後しか許されない
phrases.append(phrase(word="過去",mizen="だろ",renyo="だ",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞ガ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="だ",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞ナ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="だ",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞バ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="だ",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞マ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="たろ",renyo="た",syusi="た",rentai="た",katei="たら",meirei="",before_word_type=None,conjugation="連用過去"))
#命令形だと終止形+"な"
#"ます"だと、未然形+"ん"
# 「たい」+「ない」のときだけ、ないを助動詞ではなく、用言として扱う
phrases.append(phrase(word="否定",mizen="ん",renyo="ん",syusi="ん",rentai="ん",katei="ん",meirei="ん",before_word_type="ます",conjugation="未然"))
phrases.append(phrase(word="否定",mizen="なかろ",renyo="なく",syusi="ない",rentai="ない",katei="なけれ",meirei=None,before_word_type="自分の希望",conjugation="連用希望"))
phrases.append(phrase(word="否定",mizen="なかろ",renyo="なく",syusi="ない",rentai="ない",katei="なけれ",meirei=None,before_word_type=None,conjugation="未然否定nai"))
phrases.append(phrase(word="否定",mizen=None,renyo=None,syusi=None,rentai=None,katei=None,meirei="な",before_word_type=None,conjugation="終止"))
phrases.append(phrase(word="伝聞",mizen="",renyo="そうで",syusi="そうだ",rentai="",katei="",meirei="",before_word_type=None,conjugation="終止"))
phrases.append(phrase(word="様態",mizen="そうだろ",renyo="そうで",syusi="そうだ",rentai="そうな",katei="そうなら",meirei="",before_word_type=None,conjugation="連体"))
phrases.append(phrase(word="例示",mizen="ようだろ",renyo="ようで",syusi="ようだ",rentai="ような",katei="ようなら",meirei="",before_word_type=None,conjugation="連体"))
phrases.append(phrase(word="推定",mizen="",renyo="らしく",syusi="らしい",rentai="らしい",katei="らしけれ",meirei="",before_word_type=None,conjugation="終止"))
#子音動詞の場合は未然意思、それ以外は未然否定naiになる
#子音動詞の場合はyouではなくuになる
#ますの場合は「かきませんか」になる
#推量・意思ともいう
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="子音動詞",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="形容詞",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="形容動詞",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="否定・自分の希望・断定・伝聞・様態・例示・です・ます",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="よう",rentai="よう",katei="",meirei="",before_word_type=None,conjugation="未然否定nai"))
#phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="んか",rentai="んか",katei="",meirei="",before_word_type=None,conjugation="未然否定nai"))
# #子音動詞の場合は終止、それ以外は未然否定naiになる
# #動詞の直後しか許されない
# phrases.append(phrase(word="打ち消し",mizen="",renyo="",syusi="まい",rentai="まい",katei="",meirei="",before_word_type="子音動詞",conjugation="終止"))
# phrases.append(phrase(word="打ち消し",mizen="",renyo="",syusi="まい",rentai="まい",katei="",meirei="",before_word_type=None,conjugation="未然否定nai"))
phrases.append(phrase(word="断定",mizen="たろ",renyo="で",syusi="だ",rentai="な",katei="なら",meirei="",before_word_type=None,conjugation="終止"))
phrases.append(phrase(word="自分の希望",mizen="たかろ",renyo="たく",syusi="たい",rentai="たい",katei="たけれ",meirei="",before_word_type=None,conjugation="連用希望"))
phrases.append(phrase(word="他人の希望",mizen="たがら",renyo="たがり",syusi="たがる",rentai="たがる",katei="たがれ",meirei="",before_word_type=None,conjugation="連用希望"))
#動詞の直後なら"ます"、そうでなければ"です"　打ち消し、断定
#伝聞：かくそうです、様態：かくそうです、例示：かくようです、推定：かくらしいです、自分の希望：かきたいです、否定：かかないです
phrases.append(phrase(word="です",mizen="でしょ",renyo="でし",syusi="です",rentai="です",katei="",meirei="",before_word_type="伝聞・様態・例示・推定・自分の希望・否定・過去",conjugation="終止"))
# 形容詞ならそのままつける
phrases.append(phrase(word="です",mizen="でしょ",renyo="でし",syusi="です",rentai="です",katei="",meirei="",before_word_type="形容詞",conjugation="終止"))
# 判定詞なら「だ」を「です」へと活用する
phrases.append(phrase(word="です",mizen="でしょ",renyo="でし",syusi="です",rentai="です",katei="",meirei="",before_word_type="判定詞",conjugation="終止"))
#なし：かきます、否定：かきません、過去：かきました、可能：かけれます、使役：かかせます、受け身：かかられます、勧誘：かきませんか、他人の希望：かきたがります
phrases.append(phrase(word="ます",mizen="ませ",renyo="まし",syusi="ます",rentai="ます",katei="ますれ",meirei="ませ",before_word_type=None,conjugation="連用希望"))
#直前の単語が"て"または"で"なら追加しない
phrases.append(phrase(word="て",mizen="で",renyo="で",syusi="で",rentai="で",katei="で",meirei="",before_word_type="子音動詞ガ行",conjugation="連用過去"))
phrases.append(phrase(word="て",mizen="で",renyo="で",syusi="で",rentai="で",katei="で",meirei="",before_word_type="子音動詞ナ行",conjugation="連用過去"))
phrases.append(phrase(word="て",mizen="で",renyo="で",syusi="で",rentai="で",katei="で",meirei="",before_word_type="子音動詞バ行",conjugation="連用過去"))
phrases.append(phrase(word="て",mizen="で",renyo="で",syusi="で",rentai="で",katei="で",meirei="",before_word_type="子音動詞マ行",conjugation="連用過去"))
phrases.append(phrase(word="て",mizen="て",renyo="て",syusi="て",rentai="て",katei="て",meirei="て",before_word_type=None,conjugation="連用過去"))
#みなければ、みないなら
phrases.append(phrase(word="仮定nara",mizen="なら",renyo="なら",syusi="なら",rentai="なら",katei="なら",meirei="なら",before_word_type=None,conjugation="終止"))
phrases.append(phrase(word="仮定ba",mizen="ば",renyo="ば",syusi="ば",rentai="ば",katei="ば",meirei="ば",before_word_type=None,conjugation="仮定"))
#直前の単語に"テ"を加える
phrases.append(phrase(word="ください",mizen="ください",renyo="ください",syusi="ください",rentai="ください",katei="ください",meirei="ください",before_word_type=None,conjugation="終止"))
phrase_order = ["使役", "可能", "受け身", "自分の希望", "他人の希望", "ます", "否定", "過去", "推定", "伝聞", "様態", "例示", "勧誘", "です", "て", "仮定nara", "仮定ba"]

NG_dict = {
    "可能":["受け身","勧誘","自分の希望","他人の希望"],
    "です・ます":["て","勧誘"],
    "て":["勧誘"],
    "仮定":["伝聞","勧誘","です・ます","て"],
    "勧誘":["過去","推定","伝聞"],
    "自分の希望":["他人の希望"],
    "様態":["例示","伝聞"],
    "例示":["伝聞"]
}

class SegmentationEngine(Enum):
    NAGISA = 1
    JANOME = 2
    JUMAN = 3

engine_name = None
engine = None
def setSegmentationEngine(ename, e):
    global engine_name
    global engine
    engine_name = ename
    engine = e

disable_error_engine = None
def disableError(juman):
    global disable_error_engine
    disable_error_engine = juman

def transformVerb(verb,format_set):
    if type(verb) is not str:
        raise TypeError("transformVerbの第1引数にはstr型を入れてください。引数("+str(type(verb))+")")
    if type(format_set) is list:
        format_set = set(format_set)
    if type(format_set) is not set:    
        raise TypeError("transformVerbの第2引数にはset型を入れてください。引数("+str(type(format_set))+")")
    # 辞書に入力文字列が見つからなかったら
    values = None
    if not verb in kotodama_dic:
        # 分かち書きをして後方一致にて探してみる
        words = None
        if engine_name == SegmentationEngine.NAGISA :
            words = engine.wakati(verb)
        if engine_name == SegmentationEngine.JANOME:
            words = [ token.surface for token in engine.tokenize(verb)]
        if engine_name == SegmentationEngine.JUMAN:
            words = [ mrph.midasi for mrph in engine.analysis(verb).mrph_list()]
        if words is not None and words[-1] in kotodama_dic:
            values = kotodama_dic[words[-1]]
        # もしdisableErrorが実行されていたら、valuesの中身を極力Noneにしない
        if disable_error_engine is not None:
            juman_result = disable_error_engine.analysis(verb)
            for mrph in juman_result.mrph_list():
                if mrph.hinsi in ["動詞","形容詞"]:
                    add_db(mrph)

    if values == None:
        values = kotodama_dic[verb]

    if values == None:
        raise ValueError("辞書に定義されていない単語が入力されました。kotodama_dic.csvに「"+str(verb)+"」を追加してください")

    print("values %s" % str(values))
    target_verb = values[0]
    hinsi = values[1]
    katuyou1 = values[2]

    if not format_set <= set(phrase_order):
        warnings.warn(str(format_set - set(phrase_order))+"は対応していません", UserWarning)
        format_set = format_set & set(phrase_order)

    for key in NG_dict:
        if key in format_set:
            for ng_tag in NG_dict[key]:
                if ng_tag in format_set:
                    #print(key+"と"+ng_tag+"の組み合わせは表現できません。"+ng_tag+"を削除します")
                    return "None"
                    #format_set.remove(ng_tag)

    if "です・ます" in format_set:
        format_set.remove("です・ます")
        if len(format_set) == 0:
            if hinsi=="動詞":
                format_set.add("ます")
            elif hinsi=="形容詞" or hinsi=="判定詞":
                format_set.add("です")
            elif hinsi == "接尾辞":
                if katuyou1 == "母音動詞":
                    format_set.add("ます")
                else:
                    format_set.add("です")
        else:
            index_array = [phrase_order.index(format_value) for format_value in format_set]
            desu = {"自分の希望", "推定", "伝聞", "様態", "例示", "勧誘"}
            masu = {"使役", "可能", "受け身", "他人の希望", "否定", "過去"}
            if phrase_order[max(index_array)] in masu:
                format_set.add("ます")
            elif phrase_order[max(index_array)] in desu:
                format_set.add("です")



    if "仮定" in format_set:
        nara = {"受け身","伝聞","様態","例示","勧誘","です・ます","て"} & format_set
        ba = {"過去","伝聞","勧誘","です・ます","て"} & format_set
        if len(nara)==0:
            format_set.add("仮定nara")
        elif len(ba)==0:
            format_set.add("仮定ba")



    format_set = sorted(format_set, key=phrase_order.index)       



    phrase_list = []
    for i in range(len(format_set)):
        for phrase in phrases:
            if phrase.word == format_set[i]:

                # before word typeは色々ある
                # 動詞のkatuyou1の場合　サ変活用、イ形容詞イ段など
                # 直前の活用形の種類　です　て　過去　ます　など

                # katuyou1を見るのは、動詞または形容詞の直後につくものだけ
                if i==0 and katuyou1 is not None and phrase.before_word_type is not None and phrase.before_word_type in katuyou1:
                    phrase_list.append(phrase)
                    break
                # その他は直前の活用形の種類を見る
                elif i!=0 and phrase.before_word_type is not None and format_set[i-1] in phrase.before_word_type:
                    phrase_list.append(phrase)
                    break

                # 無条件で実行できるものはこちら
                elif phrase.before_word_type==None:
                    phrase_list.append(phrase)
                    break

    print("verb %s target_verb %s" % (verb, target_verb))
    header = verb.replace(target_verb,"")
    print("header %s" % header)
    if len(phrase_list)!=0:
        transformed = header + transformConjugationForm(target_verb,katuyou1,phrase_list[0].conjugation)
    else:
        transformed = header + target_verb

    for i in range(len(phrase_list)):

        #特殊なルールを記述する
        #て・でを追加するときは、直前の文字がて・でではないことを確認する
        if phrase_list[i].word == "て" and ( transformed.endswith("て") or transformed.endswith("で")):
            continue

        #ですを後ろにつける場合、最後が「だ」ならそれを削除
        if phrase_list[i].word == "です" and transformed.endswith("だ"):
            transformed = transformed[:-1]

        if not i+1 ==len(phrase_list):
            c = phrase_list[i+1].conjugation

            # 過去を追加するときは、促音便系に変換する必要があり
            # 否定は「なくー＞なかっ」、自分の希望は「たくー＞たかっ」、他人の希望は「たがりー＞たがっ」
            # 5段活用形の音便のように、終止形の最後の文字を取り除くといった規則性がないうえ、３つしかないため個別にルールを書く
            if phrase_list[i+1].word in ["過去"] and  phrase_list[i].word == "否定":
                transformed += "なかっ"
            elif phrase_list[i+1].word in ["過去"] and  phrase_list[i].word == "自分の希望":
                transformed += "たかっ"
            elif phrase_list[i+1].word in ["過去","て"] and  phrase_list[i].word == "他人の希望":
                transformed += "たがっ"
            elif phrase_list[i+1].word in ["て"] and  phrase_list[i].word == "過去":
                transformed += "たっ"
            elif "未然" in c:
                transformed += phrase_list[i].mizen
            elif "連用" in c:
                transformed += phrase_list[i].renyo
            elif "終止" in c:
                transformed += phrase_list[i].syusi
            elif "連体" in c:
                transformed += phrase_list[i].rentai
            elif "仮定" in c:
                transformed += phrase_list[i].katei
            elif "命令" in c:
                transformed += phrase_list[i].meirei

        else:
            transformed += phrase_list[i].syusi

        # 「せう」は発音しにくいので「しょう」に変わる
        if "せう" in transformed :
            transformed = transformed.replace("せう","しょう")
        # 「らよう」も発音しにくいので「ろう」に変わる
        if "らよう" in transformed :
            transformed = transformed.replace("らよう","ろう")

        print(transformed)

    return transformed

def joinMultipleVerb(verbs,format_set):
    result = ""
    for i,verb in enumerate(verbs):
        if i==len(verbs)-1:
            result += transformVerb(verb,format_set)
        else:
            result += transformVerb(verb,("て"))
    return result