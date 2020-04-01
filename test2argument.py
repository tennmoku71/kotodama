# すべての組み合わせでテスト
import itertools
from kotodama import kotodama_no_juman

format_all_list = ["可能","受け身","使役","過去","否定","推定","様態","伝聞","例示","勧誘","自分の希望","他人の希望","て","です・ます"]
output_f = open('log.csv', mode='w', encoding='utf-8')

f = open("result.txt",encoding="utf-8",mode="r")
target_verb_hist = []
for verb in f:
    verb = verb.strip()
    target_verb = kotodama_no_juman.kotodama_dic[verb][0]
    
    if not target_verb in target_verb_hist:
        katuyou1 = kotodama_no_juman.kotodama_dic[verb][2]
        print(katuyou1)
        for iternum in range(4):
            for format_list in itertools.combinations(format_all_list,iternum+1):
                output = target_verb+"\t"+":".join(format_list)+"\t"+kotodama_no_juman.transformVerb(verb,set(format_list))
                output_f.write(output.replace("\t",",")+"\n")
                print(output)
        target_verb_hist.append(target_verb)

output_f.close()
f.close()