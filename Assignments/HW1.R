#!/usr/bin/Rscript
# Load
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

# Read the text files for 3 groups 
data2<-c("G:\\STUDY\\MS in CS\\Spring 2017\\CS522 ADM\\HWs\\1\\20news-19997\\20_newsgroups\\comp.sys.ibm.pc.hardware","G:\\STUDY\\MS in CS\\Spring 2017\\CS522 ADM\\HWs\\1\\20news-19997\\20_newsgroups\\comp.sys.mac.hardware","G:\\STUDY\\MS in CS\\Spring 2017\\CS522 ADM\\HWs\\1\\20news-19997\\20_newsgroups\\sci.electronics") 

# Load the data as a corpus 
news <- Corpus(DirSource(data2, recursive=TRUE),readerControl = list(reader=readPlain))

news <- tm_map(news, removeWords,"Subject")
news <- tm_map(news, removeWords,"Organization")
news <- tm_map(news, removeWords,"writes")
news <- tm_map(news, removeWords,"From")
news <- tm_map(news, removeWords,"lines")
news <- tm_map(news, removeWords," NNTP-Posting-Host")
news <- tm_map(news, removeWords,"article")

news <- tm_map(news, tolower) ## Convert to Lower Case 
news <- tm_map(news, removeWords, stopwords("english")) ## Remove Stopwords 
news <- tm_map(news, removePunctuation) ## Remove Punctuations 
news <- tm_map(news, stemDocument) ## Stemming 
news <- tm_map(news, removeNumbers) ## Remove Numbers 
news <- tm_map(news, stripWhitespace) ## Eliminate Extra White Spaces 
news <- tm_map(news , PlainTextDocument)
print("Creating matrices")
dtm <- DocumentTermMatrix(news,control=list(wordLengths=c(4,Inf))) 
tdm <- TermDocumentMatrix(news, control=list(wordLengths=c(4,Inf))) #Term Document Matrix 
print("Created matrices")
Sys.sleep(30)
#Verify Frequent Terms 
m <- as.matrix(tdm) 
Sys.sleep(30)
v <- sort(rowSums(m), decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)
Sys.sleep(30)
dtms <- removeSparseTerms(dtm, 0.15) # Prepare the data 
freq <- colSums(as.matrix(dtm)) # Find word frequencies 
dark2 <- brewer.pal(6, "Dark2") 
wordcloud(names(freq), freq, max.words=100, rot.per=0.2, colors=dark2)
Sys.sleep(30)
dtm_tfxidf2<- weightTfIdf(dtm)
print("END")

Sys.sleep(30)