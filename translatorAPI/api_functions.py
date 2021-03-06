from nltk.corpus import wordnet  # Import wordnet from the NLTK
from gingerit.gingerit import GingerIt
import nltk
from googletrans import Translator


translator = Translator()

parts_of_speech_dict = {
    'CC': 'Coordinating conjunction',
    'CD': 'Cardinal number',
    'DT': 'Determiner',
    'EX': 'Existential there',
    'FW': 'Foreign word',
    'IN': 'Preposition or subordinating conjunction',
    'JJ': 'Adjective',
    'JJR': 'Adjective, comparative',
    'JJS': 'Adjective, superlative',
    'LS': 'List item marker',
    'MD': 'Modal',
    'NN': 'Noun, singular or mass',
    'NNS': 'Noun, plural',
    'NNP': 'Proper noun, singular',
    'NNPS': 'Proper noun, plural',
    'PDT': 'Predeterminer',
    'POS': 'Possessive ending',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun',
    'RB': 'Adverb',
    'RBR': 'Adverb, comparative',
    'RBS': ' Adverb, superlative',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': 'to',
    'UH': 'Interjection',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non - 3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'WDT': 'Wh - determiner',
    'WP': 'Wh - pronoun',
    'WP$': 'Possessive wh - pronoun',
    'WRB': 'Wh - adverb'
}
languages_dict = {}
languages_dict.update({'languages': ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer',
                      'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']})


# def get_definition(word):
#     try:
#         definition = (dictionary.meaning(word))
#         return definition.get("Noun")

#     except Exception as e:
#         print(e)
#         return []


def get_synonyms(word):
    try:
        synset = wordnet.synsets(word)
        syn_ant = {'synonyms': {},
                   'antonyms': {}}
        if synset:
            '''
            print('Word and Type : ' + synset[0].name())
            print('Synonym of '+word+' is: ' + synset[0].lemmas()[0].name())
            print('The meaning of the word : ' + synset[0].definition())
            print('Example of '+word+' : ' + str(synset[0].examples()))
            '''
            definition = []
            examples = []
            for e in synset:
                definition.append(e.definition())
                for item in e.examples():
                    examples.append(item)

            syn_ant.update({"synonyms": synset[0].lemmas()[0].name(),
                            "definition": definition,  # synset[0].definition()
                            "example": examples})  # (synset[0].examples())
        else:
            syn_ant.update({
                "definition": [],
                "example": []})

        syn = list()
        ant = list()
        if len(word.split()) == 1:
            for synset in wordnet.synsets(word):
                for lemma in synset.lemmas():
                    if lemma.name() not in syn:
                        syn.append(lemma.name())  # add the synonyms
                    if lemma.antonyms():  # When antonyms are available, add them into the list
                        ant.append(lemma.antonyms()[0].name())
            syn_ant['synonyms'] = {word: list(syn)}
            syn_ant['antonyms'] = {word: list(ant)}
            return {'data': syn_ant}

        for w in word.split():
            for synset in wordnet.synsets(w):
                for lemma in synset.lemmas():
                    if lemma.name() not in syn:
                        syn.append(lemma.name())  # add the synonyms
                    if lemma.antonyms():  # When antonyms are available, add them into the list
                        ant.append(lemma.antonyms()[0].name())

            if w in syn_ant.keys():
                syn_ant[w].append(str(syn))
                syn_ant[w+"ant"].append(str(ant))
            else:
                syn_ant = dict(syn_ant)
                syn_ant['synonyms'].update({
                    w: list(syn)
                })
                syn_ant['antonyms'].update({
                    w: list(ant)
                })
            syn.clear()
            ant.clear()

        return {'data': syn_ant}
    except Exception as e:
        print(e)
        error_dict = {'data': 'Something went wrong'}
        return error_dict


def get_correct_word(word):
    try:
        text = word
        # parser = GingerIt()
        # print(type(text))
        # result_dict = parser.parse(text)
        # print(parser.parse(text))
        # return {'data':  result_dict["result"]}
        # b = TextBlob(word)
        # print(str(b.correct()))
        # result = str(b.correct())
        return {'data': word}
    except Exception as e:
        print(e)
        error_dict = {'error': 'Something went wrong'}
        return error_dict


def get_parts_of_speech(word):
    try:
        sentence = word
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        parts_of_speech = tagged
        result_dict = {}
        for items in parts_of_speech:
            items = (list(items))
            try:
                items[1] = parts_of_speech_dict[items[1]]
                # print(items)
                result_dict[items[0]] = items[1]
            except Exception as e:
                pass

        return {'data': result_dict}
    except Exception as e:
        print(e)
        error_dict = {'data': ['Something went wrong']}
        return error_dict


def get_trans(word, form, to):
    try:
        text_to_translate = translator.translate(word, src=form, dest=to)
        text = text_to_translate.text
        return {'data': text}
    except Exception as e:
        print(e)
        error_dict = {'error': 'Something went wrong'}
        return error_dict


def get_all(word, form, to):
    try:
        correct_word = get_correct_word(word).get('data')
        syn_ant = get_synonyms(correct_word).get('data')
        part_of_speech_data = get_parts_of_speech(correct_word).get('data')
        translation = get_trans(correct_word, form, to).get('data')
        result = {
            "word": word,
            "corrected_word": correct_word,
            "synonyms": syn_ant.get('synonyms'),
            "antonyms": syn_ant.get('antonyms'),
            "definition": syn_ant.get('definition'),
            "example": syn_ant.get('example'),
            "parts_of_speech": part_of_speech_data,
            "translation": translation,
        }
        return {'data': result}

    except Exception as e:
        print(e)
        error_dict = {'data': 'Something went wrong'}
        return error_dict
