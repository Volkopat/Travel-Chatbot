pipeline:
- name : "nlp_spacy"
- name: "tokenizer_whitespace"
- name: "intent_entity_featurizer_regex"
- name: "ner_crf"
  features: [["low", "title", "upper"], ["bias", "low", "prefix5", "prefix2", "suffix5", "suffix3", "suffix2", "upper", "title", "digit", "pattern"], ["low", "title", "upper"]]
- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
- name: "intent_classifier_tensorflow_embedding"
path: "./models/nlu"
data: "./data/data.json"

