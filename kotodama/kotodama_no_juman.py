# -*- coding: utf-8 -*-

kotodama_dic = {}
file = open("kotodama_dic.csv",encoding="utf-8",mode = "r")
for ele in file:
    ele_list = ele.strip().split(",") 
    key = ele_list[0]
    value = ele_list[1:]
    kotodama_dic[key] = value
file.close()

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

    # hiragana = [
    #     ["あ","い","う","え","お"],
    #     ["か","き","く","け","こ"],
    #     ["が","ぎ","ぐ","げ","ご"],
    #     ["さ","し","す","せ","そ"],
    #     ["ざ","じ","ず","ぜ","ぞ"],
    #     ["た","ち","つ","て","と"],
    #     ["だ","ぢ","づ","で","ど"],
    #     ["な","に","ぬ","ね","の"],
    #     ["は","ひ","ふ","へ","ほ"],
    #     ["ば","び","ぶ","べ","ぼ"],
    #     ["ぱ","ぴ","ぷ","ぺ","ぽ"],
    #     ["ま","み","む","め","も"],
    #     ["や",None,"ゆ",None,"よ"],
    #     ["ら","り","る","れ","ろ"],
    #     ["わ","い","う","え","お"]
    # ]

    def get_index(c):
        global hiragana
        for boin in nihongo.hiragana:
            if shin_index in nihongo.hiragana[boin]:
                return boin,nihongo.hiragana[boin].index(shin_index)

    def get_char(boin,shin_index):
        return nihongo.hiragana[boin][shin_index]
    
    def change_shiin(c, shiin_index):
        boin,_ = nihongo.get_index(c)
        return nihongo.get_char(boin,shiin_index)
    
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
phrases.append(phrase(word="可能",mizen="",renyo="",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="母音動詞",conjugation="未然可能"))
phrases.append(phrase(word="可能",mizen="",renyo="",syusi="る",rentai="る",katei="れ",meirei="ろ",before_word_type=None,conjugation="未然可能"))

phrases.append(phrase(word="使役",mizen="せ",renyo="せ",syusi="せる",rentai="せる",katei="せれ",meirei="せろ",before_word_type="子音動詞",conjugation="未然使役"))
phrases.append(phrase(word="使役",mizen="せ",renyo="せ",syusi="せる",rentai="せる",katei="せれ",meirei="せろ",before_word_type="サ変動詞",conjugation="未然使役"))
phrases.append(phrase(word="使役",mizen="させ",renyo="させ",syusi="させる",rentai="させる",katei="させれ",meirei="させろ",before_word_type=None,conjugation="未然使役"))

phrases.append(phrase(word="受け身",mizen="れ",renyo="れ",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="子音動詞",conjugation="未然使役"))
phrases.append(phrase(word="受け身",mizen="れ",renyo="れ",syusi="れる",rentai="れる",katei="れれ",meirei="れろ",before_word_type="サ変動詞",conjugation="未然使役"))
phrases.append(phrase(word="受け身",mizen="られ",renyo="られ",syusi="られる",rentai="られる",katei="られれ",meirei="られろ",before_word_type=None,conjugation="未然使役"))

#動詞の直後しか許されない
phrases.append(phrase(word="過去",mizen="だろ",renyo="",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞ガ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞ナ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞バ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="だろ",renyo="",syusi="だ",rentai="だ",katei="だら",meirei="",before_word_type="子音動詞マ行",conjugation="連用過去"))
phrases.append(phrase(word="過去",mizen="たろ",renyo="",syusi="た",rentai="た",katei="たら",meirei="",before_word_type=None,conjugation="連用過去"))

#命令形だと終止形+"な"
#"ます"だと、未然形+"ん"
phrases.append(phrase(word="否定",mizen="ん",renyo="ん",syusi="ん",rentai="ん",katei="ん",meirei="ん",before_word_type="ます",conjugation="未然"))
phrases.append(phrase(word="否定",mizen="なかろ",renyo="なく",syusi="ない",rentai="ない",katei="なけれ",meirei=None,before_word_type=None,conjugation="未然否定nai"))
phrases.append(phrase(word="否定",mizen=None,renyo=None,syusi=None,rentai=None,katei=None,meirei="な",before_word_type=None,conjugation="終止"))

phrases.append(phrase(word="伝聞",mizen="",renyo="そうで",syusi="そうだ",rentai="",katei="",meirei="",before_word_type=None,conjugation="終止"))

phrases.append(phrase(word="様態",mizen="そう",renyo="そう",syusi="そう",rentai="そう",katei="そう",meirei="",before_word_type=None,conjugation="連体"))

phrases.append(phrase(word="例示",mizen="ようだろ",renyo="ようで",syusi="ようだ",rentai="ような",katei="ようなら",meirei="",before_word_type=None,conjugation="連体"))

phrases.append(phrase(word="推定",mizen="",renyo="らしく",syusi="らしい",rentai="らしい",katei="らしけれ",meirei="",before_word_type=None,conjugation="終止"))

#子音動詞の場合は未然意思、それ以外は未然否定naiになる
#子音動詞の場合はyouではなくuになる
#ますの場合は「かきませんか」になる
#推量・意思ともいう
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="子音動詞",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="形容詞",conjugation="未然意思"))
phrases.append(phrase(word="勧誘",mizen="",renyo="",syusi="う",rentai="う",katei="",meirei="",before_word_type="形容動詞",conjugation="未然意思"))
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
phrases.append(phrase(word="て",mizen="て",renyo="て",syusi="て",rentai="て",katei="て",meirei="て",before_word_type=None,conjugation="連用過去"))

#みなければ、みないなら
phrases.append(phrase(word="仮定nara",mizen="なら",renyo="なら",syusi="なら",rentai="なら",katei="なら",meirei="なら",before_word_type=None,conjugation="終止"))
phrases.append(phrase(word="仮定ba",mizen="ば",renyo="ば",syusi="ば",rentai="ば",katei="ば",meirei="ば",before_word_type=None,conjugation="仮定"))

#直前の単語に"テ"を加える
phrases.append(phrase(word="ください",mizen="ください",renyo="ください",syusi="ください",rentai="ください",katei="ください",meirei="ください",before_word_type=None,conjugation="終止"))

phrase_order = ["使役", "可能", "受け身", "ます", "過去", "否定", "自分の希望", "他人の希望", "推定", "伝聞", "様態", "例示", "勧誘", "です", "て", "仮定nara", "仮定ba"]

NG_dict = {
    "可能":["受け身","勧誘","自分の希望","他人の希望"],
    "仮定":["伝聞","勧誘","です・ます","て"],
    "て":["勧誘","です・ます"],
    "です・ます":["勧誘"],
    "勧誘":["過去","否定","伝聞","様態","例示","推定"],
    "自分の希望":["過去","他人の希望"],
    "他人の希望":["過去"],
    "様態":["例示","伝聞"],
    "例示":["伝聞"]
}


# gyou_hash = {
#     "ア行":["あ","い","う","え","お"],
#     "カ行":["か","き","く","け","こ"],
#     "ガ行":["が","ぎ","ぐ","げ","ご"],
#     "サ行":["さ","し","す","せ","そ"],
#     "ザ行":["ざ","じ","ず","ぜ","ぞ"],
#     "タ行":["た","ち","つ","て","と"],
#     "ダ行":["だ","ぢ","づ","で","ど"],
#     "ナ行":["な","に","ぬ","ね","の"],
#     "ハ行":["は","ひ","ふ","へ","ほ"],
#     "バ行":["ば","び","ぶ","べ","ぼ"],
#     "パ行":["ぱ","ぴ","ぷ","ぺ","ぽ"],
#     "マ行":["ま","み","む","め","も"],
#     "ヤ行":["や","い","ゆ","え","よ"],
#     "ラ行":["ら","り","る","れ","ろ"],
#     "ワ行":["わ","い","う","え","お"]
# }
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

def transformVerb(verb,format_set):

    if not verb in kotodama_dic:
        raise ValueError("辞書に定義されていない単語が入力されました。kotodama_dic.csvに「"+str(verb)+"」を追加してください")

    values = kotodama_dic[verb]
    target_verb = values[0]
    hinsi = values[1]
    katuyou1 = values[2]

    for key in NG_dict:
        if key in format_set:
            for ngword in NG_dict[key]:
                if ngword in format_set:
                    print("remove "+ngword)
                    format_set.remove(ngword)

    if "です・ます" in format_set:
        format_set.remove("です・ます")
        desu = {"伝聞","様態","例示","推定","勧誘","自分の希望","て","仮定","否定","過去"} & format_set
        masu = {"可能","勧誘","他人の希望","て","仮定"} & format_set
        if len(masu)!=0:
            format_set.add("ます")
        elif len(desu)!=0:
            format_set.add("です")
        elif hinsi=="動詞":
            format_set.add("ます")
        elif hinsi=="形容詞" or hinsi=="判定詞":
            format_set.add("です")
        elif hinsi == "接尾辞":
            if katuyou1 == "母音動詞":
                format_set.add("ます")
            else:
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

    header = verb.replace(target_verb,"")
    if len(phrase_list)!=0:
        transformed = header + transformConjugationForm(target_verb,katuyou1,phrase_list[0].conjugation)
    else:
        transformed = header + target_verb

    for i in range(len(phrase_list)):
        if not i+1 ==len(phrase_list):
            c = phrase_list[i+1].conjugation
            if "未然" in c:
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

    return transformed

def joinMultipleVerb(verbs,format_set):
    result = ""
    for i,verb in enumerate(verbs):
        mrph = verb.mrph_list()[-1]
        if i==len(verbs)-1:
            result += transformVerb(mrph,format_set)
        else:
            result += transformVerb(mrph,("て"))
    return result