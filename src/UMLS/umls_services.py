import umls_loader
import json
from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()


@app.post("/create_synonyms_dictionary/")
def create_synonyms_dictionary(words: str):
    word_lst = json.loads(words)
    dict_lemma_to_synonyms = {}
    for word in word_lst:
        synonyms = umls_loader.umls_loader.get_term_aliases(word)
        dict_lemma_to_synonyms[word] = set()
        dict_lemma_to_synonyms[word].add(word)
        synonyms = set(synonyms)
        if synonyms:
            for synonym in synonyms:
                if synonym != word:
                    dict_lemma_to_synonyms[word].add(synonym)
    return {"synonyms": dict_lemma_to_synonyms}


@app.post("/get_broader_terms/")
def get_broader_terms(terms: str, relation_type: str):
    broader_terms = set()
    term_lst = json.loads(terms)
    for term in term_lst:
        broader_terms = umls_loader.umls_loader.get_broader_term(term, relation_type)
        if not broader_terms:
            continue
    return {"broader_terms": broader_terms}
