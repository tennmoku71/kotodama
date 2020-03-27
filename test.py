# 2個ずつでテスト
from kotodama import kotodama_no_juman
format_all_list = ["可能","受け身","使役","過去","否定","推定","様態","伝聞","例示","勧誘","自分の希望","他人の希望","て","です・ます"]
f = open("result.txt",encoding="utf-8",mode="r")
target_verb_hist = []

output_f = open('log.csv', mode='w', encoding='utf-8')

for verb in f:
    verb = verb.strip()
    target_verb = kotodama_no_juman.kotodama_dic[verb][0]    
    katuyou1 = kotodama_no_juman.kotodama_dic[verb][2]
    print(katuyou1)
    for i in range(len(format_all_list)):
        for j in range(i):
            output = target_verb+"\t"+format_all_list[i]+"\t"+format_all_list[j]+"\t"+kotodama_no_juman.transformVerb(verb,{format_all_list[i],format_all_list[j]})
            output_f.write(output.replace("\t",",")+"\n")
            print(output)

output_f.close()
f.close()
        