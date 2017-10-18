# -*- coding: utf-8 -*-
import nltk
from wordcloud import WordCloud
from reportlab.pdfgen import canvas
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
st=PorterStemmer()
keywords=["Concluding","Finally","Highlight","in the end","like this"]
stop=[ "a","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","after","afterwards","again","against","ah","all","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","are","aren","arent","arise","around","as","aside","ask","asking","at","auth","available","away","awfully","b","back","be","became","because","become","becomes","becoming","been","before","beforehand","begin","beginning","beginnings","begins","behind","being","believe","below","beside","besides","between","beyond","biol","both","brief","briefly","but","by","c","ca","came","can","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","could","couldnt","d","date","did","didn't","different","do","does","doesn't","doing","done","don't","down","downwards","due","during","e","each","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","et-al","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","few","ff","fifth","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","further","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","had","happens","hardly","has","hasn't","have","haven't","having","he","hed","hence","her","here","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","him","himself","his","hither","home","how","howbeit","however","hundred","i","id","ie","if","i'll","im","immediate","immediately","importance","important","in","inc","indeed","index","information","instead","into","invention","inward","is","isn't","it","itd","it'll","its","itself","i've","j","just","k","keep\tkeeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","m","made","mainly","make","makes","many","may","maybe","me","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","now","nowhere","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","omitted","on","once","one","ones","only","onto","or","ord","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","s","said","same","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","she","shed","she'll","shes","should","shouldn't","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure\tt","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","these","they","theyd","they'll","theyre","they've","think","this","those","thou","though","thoughh","thousand","throug","through","throughout","thru","thus","til","tip","to","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","very","via","viz","vol","vols","vs","w","want","wants","was","wasnt","way","we","wed","welcome","we'll","went","were","werent","we've","what","whatever","what'll","whats","when","whence","whenever","where","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","whod","whoever","whole","who'll","whom","whomever","whos","whose","why","widely","willing","wish","with","within","without","wont","words","world","would","wouldnt","www","x","y","yes","yet","you","youd","you'll","your","youre","yours","yourself","yourselves","you've","z","zero"]
keywords=list(map(str,(map(st.stem,keywords))))
#print(keywords)
textFromSpeech="Good afternoon my name is Brian and I will be the conference facilitator. This time I would like to welcome everyone to include third quarter 2017 conference call. I will not on the call over to Cherry includes vice president of finance and pressure point thanks Brian. Good afternoon and welcome to into its third quarter fiscal 2017 conference call. I am here with Brad Smith Chairman and CEO and Neil Williams RCF oh. Before we start I'd like to remind everyone that are remarks will include forward-looking statements. I like this there are a number of factors that could cause includes results to differ materially from our expectations. You can learn more about these risks in the press release be issued earlier this afternoon form 10-k for fiscal 2016 Ana ACC filing. All of those documents are available on the investor relations page of includes website at in tute.com. We assume no obligation to update any forward-looking statements. Sum of the numbers in these remarks are presented on and on g a a p basis. To conclude we break inside the compatible g a a p and non VIP numbers in today's press release. Unless otherwise noted all growth rates refer to the current period versus The compare April prior year period and the business metrics and associated growth rates refer to worldwide business metrics. Finally a copy ioffer prepared remarks and supplemental financial information will be available on a website after the scoreland. With that I turn the call over to Brad. Alright. Thanks Jerry and Thanks to all of you for joining us. We are pleased with a performance in a third fiscal quarter. As you know this is a largest quarter of the year and he successfully delivered strong financial results in a complicated tax season. Exiting the quarter are consumer tax revenue was apply percent your to date and his on track to finish at the end of a guidance range for the full fiscal year. Finally we are also driving continued Momentum in a small business franchise with quickbooks online subscriber growth accelerator into 59% and 2.2 million subscribers which is above the upper end of the target in an established for the full fiscal year. As a result we are raising a Outlook for kyudo subscribers to 2.3 million dollars. I like this we are raising a full your revenue guidance and tightening the EPS range to the high end. All in all we are on track to live deliver another got your point with that overview let me click to the drivers of a performance in the third quarter beginning with attacks results. This season prove to be event full from beginning to end but with the letter to the dance filing compare 2 Prime providers renewed competitive environment and a free category a new IRS requirement design to reduce prob. Factors reflected in the 4"
stemmedSpeech=""
keyList=dict()
decisionList=[]
isDecision=False
isSameSentence=False
for sentence in textFromSpeech.split("."):
    if(isDecision==True):
        decisionList.append(sentence)
        isDecision=False
    isSameSentence=False
    for word in sentence.split():
        isSameSentence=True
        tempStem=st.stem(word)
        #print(tempStem)
        if(tempStem in keyList.keys()):
            keyList[tempStem].append(word)
        else:
            keyList[str(tempStem)]=[]
            keyList[tempStem].append(word)
        if (isDecision == True and isSameSentence==False):
            isDecision = False
            decisionList.append(sentence)
        elif(tempStem in keywords):
            isDecision=True
            decisionList.append(sentence)
        '''
        if(isDecision == True):
            isDecision = False
            decisionList.append(sentence)
        '''
        stemmedSpeech+=tempStem+" "
#print(stemmedSpeech)
print("Key words INDEX ")
print(keyList)
print("-----------")
print("DECISION LIST :")
print (decisionList)
print("----------------")
indexedList=[]
for decision in decisionList:
    templist=[i for i in decision.lower().split() if i not in stop_words]
    indexedList.append(" ".join(templist))

for decision in decisionList:
    print(decision)
print("INDEXED LIST :")
print("----------------")
print(indexedList)
pivot=20
u'•' == u'\u2022'
c = canvas.Canvas("test.pdf")
c.setPageSize((1000, 1000))
c.setLineWidth(100)
c.drawString(200, 800, "DECISION POINTS ")
for index in indexedList:
    l=[]
    for i in index.split():
        if(st.stem(i) not in keywords):
            l.append(i)
            #print(l)
        c.drawString(20,700-pivot,u'\u2022'+unicode(" ".join(l)))
    pivot+=20
c.save()