from kotodama import kotodama

# import nagisa
# kotodama.setSegmentationEngine(kotodama.SegmentationEngine.NAGISA, nagisa)

# from janome.tokenizer import Tokenizer
# tokenizer = Tokenizer()
# kotodama.setSegmentationEngine(kotodama.SegmentationEngine.JANOME, tokenizer)

# from pyknp import Juman
# juman = Juman()
# kotodama.setSegmentationEngine(kotodama.SegmentationEngine.JUMAN, juman)

tag_set = {"過去","自分の希望"}
verb = "君と過ごす"
print(kotodama.transformVerb(verb,tag_set))