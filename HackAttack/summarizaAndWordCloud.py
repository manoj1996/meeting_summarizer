# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import time
import nltk
from wordcloud import WordCloud
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from wordcloud import WordCloud
import webbrowser
import os.path
import matplotlib.pyplot as plt
import webbrowser
import numpy
from sumy.parsers.html import HtmlParser
import os.path
import os;
localtime = time.asctime(time.localtime(time.time()))
localtime = localtime.replace(" ", "_")
dirPath = "Flash_Huddler_"+localtime;
os.mkdir(dirPath);
stop = ["finally", "a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act",
            "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against",
            "ah", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst",
            "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway",
            "anyways", "anywhere", "apparently", "approximately", "are", "aren", "arent", "arise", "around", "as",
            "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "b", "back", "be", "became",
            "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning",
            "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond",
            "biol", "both", "brief", "briefly", "but", "by", "c", "ca", "came", "can", "cannot", "can't", "cause",
            "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains",
            "could", "couldnt", "d", "date", "did", "didn't", "different", "do", "does", "doesn't", "doing", "done",
            "don't", "down", "downwards", "due", "during", "e", "each", "ed", "edu", "effect", "eg", "eight", "eighty",
            "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "et-al", "etc", "even",
            "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "few",
            "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "for", "former", "formerly",
            "forth", "found", "four", "from", "further", "furthermore", "g", "gave", "get", "gets", "getting", "give",
            "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "h", "had", "happens", "hardly", "has",
            "hasn't", "have", "haven't", "having", "he", "hed", "hence", "her", "here", "hereafter", "hereby", "herein",
            "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his", "hither", "home",
            "how", "howbeit", "however", "hundred", "i", "id", "ie", "if", "i'll", "im", "immediate", "immediately",
            "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "into", "invention",
            "inward", "is", "isn't", "it", "itd", "it'll", "its", "itself", "i've", "j", "just", "k", "keep\tkeeps",
            "kept", "kg", "km", "know", "known", "knows", "l", "largely", "last", "lately", "later", "latter",
            "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll",
            "look", "looking", "looks", "ltd", "m", "made", "mainly", "make", "makes", "many", "may", "maybe", "me",
            "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "more",
            "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "n", "na", "name",
            "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never",
            "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone",
            "nor", "normally", "nos", "not", "noted", "nothing", "now", "nowhere", "o", "obtain", "obtained",
            "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "omitted", "on", "once", "one", "ones",
            "only", "onto", "or", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out",
            "outside", "over", "overall", "owing", "own", "p", "page", "pages", "part", "particular", "particularly",
            "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp",
            "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put",
            "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "re", "readily", "really", "recent",
            "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research",
            "respectively", "resulted", "resulting", "results", "right", "run", "s", "said", "same", "saw", "say",
            "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self",
            "selves", "sent", "seven", "several", "shall", "she", "shed", "she'll", "shes", "should", "shouldn't",
            "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly",
            "since", "six", "slightly", "so", "some", "somebody", "somehow", "someone", "somethan", "something",
            "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify",
            "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently",
            "suggest", "sup", "sure\tt", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks",
            "thanx", "that", "that'll", "thats", "that've", "the", "their", "theirs", "them", "themselves", "then",
            "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof",
            "therere", "theres", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'll", "theyre",
            "they've", "think", "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through",
            "throughout", "thru", "thus", "til", "tip", "to", "together", "too", "took", "toward", "towards", "tried",
            "tries", "truly", "try", "trying", "ts", "twice", "two", "u", "un", "under", "unfortunately", "unless",
            "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used", "useful", "usefully",
            "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "very", "via", "viz", "vol",
            "vols", "vs", "w", "want", "wants", "was", "wasnt", "way", "we", "wed", "welcome", "we'll", "went", "were",
            "werent", "we've", "what", "whatever", "what'll", "whats", "when", "whence", "whenever", "where",
            "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which",
            "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos",
            "whose", "why", "widely", "willing", "wish", "with", "within", "without", "wont", "words", "world", "would",
            "wouldnt", "www", "x", "y", "yes", "yet", "you", "youd", "you'll", "your", "youre", "yours", "yourself",
            "yourselves", "you've", "z", "zero"]
def summarize():
    LANGUAGE = "english"
    SENTENCES_COUNT = 100
    parser = PlaintextParser.from_file("firsttext.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    pivot = 20
    u'•' == u'\u2022'
    os.chdir(dirPath);
    c = canvas.Canvas('Summary.pdf')
    c.setPageSize((1000, 1000))
    c.drawString(200, 800, "DISCUSSION POINTS ")
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        string = numpy.unicode(sentence)
        if (len("".join(string.split())) < 160):
            c.drawString(10, 700 - pivot, u'\u2022' + numpy.unicode(string))
        else:
            firstpart, secondpart = string[:len(string) // 2], string[len(string) // 2:]
            print(firstpart)
            print(secondpart)
            c.drawString(10, 700 - pivot, u'\u2022' + numpy.unicode(firstpart))
            pivot += 20
            c.drawString(10, 700 - pivot, u'\u2022' + numpy.unicode(secondpart))
        pivot += 20
    c.save()
    os.chdir("..")
def decisionPoints():
    stop_words = set(stopwords.words('english'))
    st = PorterStemmer()
    keywords = ["Concluding", "Finally", "Highlight", "in the end", "like this"]
    keywords = list(map(str, (map(st.stem, keywords))))
    # print(keywords)
    with open('firsttext.txt', 'r') as myfile:
        textFromSpeech = myfile.read();
    stemmedSpeech = ""
    keyList = dict()
    decisionList = []
    isDecision = False
    isSameSentence = False
    for sentence in textFromSpeech.split("."):
        if (isDecision == True):
            decisionList.append(sentence)
            isDecision = False
        isSameSentence = False
        for word in sentence.split():
            isSameSentence = True
            tempStem = st.stem(word)
            # print(tempStem)
            if (tempStem in keyList.keys()):
                keyList[tempStem].append(word)
            else:
                keyList[str(tempStem)] = []
                keyList[tempStem].append(word)
            if (isDecision == True and isSameSentence == False):
                isDecision = False
                decisionList.append(sentence)
            elif (tempStem in keywords):
                isDecision = True
                decisionList.append(sentence)
            stemmedSpeech += tempStem + " "
    # print(stemmedSpeech)
    print("Key words INDEX ")
    print(keyList)
    print("-----------")
    print("DECISION LIST :")
    print(decisionList)
    print("----------------")
    indexedList = []
    for decision in decisionList:
        templist = [i for i in decision.lower().split()]
        indexedList.append(" ".join(templist))
    for decision in decisionList:
        print(decision)
    print("INDEXED LIST :")
    print("----------------")
    print(indexedList)
    fileIndex = open("/Applications/XAMPP/xamppfiles/htdocs/HackAttack/searchIndex.txt","r");
    indexKeys=dict()
    for i in fileIndex.readlines():
        k=i.split(":")[0]
        if(k not in indexKeys.keys()):
            indexKeys[k]=[]
        else:
            indexKeys[k] = list(i.split(":")[1])
    for sentence in indexedList:
        for word in sentence.split():

            if word not in stop:
                print(word)
                if(word in indexKeys.keys()):
                    indexKeys[word].append(dirPath)
                else:
                    indexKeys[word]=[]
                    indexKeys[word].append(dirPath)

    print("-----INDEX KEYS------")
    print("dict:",indexKeys)
    os.remove("/Applications/XAMPP/xamppfiles/htdocs/HackAttack/searchIndex.txt")
    fileIndexFinal=open("/Applications/XAMPP/xamppfiles/htdocs/HackAttack/searchIndex.txt","w+")
    for i in indexKeys.keys():
        fileIndexFinal.write(i+":"+",".join(indexKeys[i])+"\n")
    fileIndexFinal.close()
    pivot = 20
    u'•' == u'\u2022'
    localtime = time.asctime(time.localtime(time.time()))
    localtime = localtime.replace(" ", "_")
    os.chdir(dirPath)
    c = canvas.Canvas('Decision.pdf')
    c.setPageSize((1000, 1000))
    c.setLineWidth(100)
    c.drawString(200, 800, "DECISION POINTS ")
    for index in indexedList:
        l = []
        for i in index.split():
            if (st.stem(i) not in keywords):
                l.append(i)
                # print(l)
            c.drawString(20, 700 - pivot, u'\u2022' + str(" ".join(l)))
        pivot += 20
    c.save()
    os.chdir("..")
def wordCloud():
    with open('firsttext.txt', 'r') as myfile:
        word_string = myfile.read();
    wordcloud = WordCloud(stopwords=stop,
                          background_color='white',
                          width=1200,
                          height=1000
                          ).generate(word_string)
    localtime = time.asctime(time.localtime(time.time()))
    localtime=localtime.replace(" ", "_")
    plt.imshow(wordcloud)
    plt.axis('off')
    os.chdir(dirPath)
    plt.savefig('WordCloud.png')
    os.chdir("..")


while(os.path.isfile("firsttext.txt")):
    os.remove("firsttext.txt");
url = 'http://localhost/HackAttack/speechToText.html';
cp = "open -a /Applications/Google\ Chrome.app %s"
webbrowser.get(cp).open(url);
while(not os.path.isfile("firsttext.txt")):
    pass

summarize();
decisionPoints();
wordCloud();
url = 'http://localhost/HackAttack/sindex.html';
cp = "open -a /Applications/Google\ Chrome.app %s"
webbrowser.get(cp).open(url);