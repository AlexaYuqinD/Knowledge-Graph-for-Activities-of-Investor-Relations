# Knowledge Graph for Activities of Investor Relations

## 1. Crawling Data
Crawl Investor Relation forms of companies of Shenzhen stock market from <a href="http://www.cninfo.com.cn">http://www.cninfo.com.cn</a>. Then filter and read the files.

## 2. Knowledge Extraction
### Objects
investor activity types
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/type1.PNG" 
 width="400" height="110" />
</p>


<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/type2.PNG" 
 width="400" height="110" />
</p>

host names and positions

<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/host.PNG" 
 width="400" height="60" />
</p>

guest names and corresponding companies

<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/guest1.PNG" 
 width="350" height="50" />
</p>

<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/guest2.PNG" 
 width="400" height="120" />
</p>

### Methods
#### (i) Based on Rules
Note: for entity, attribute and relation extraction.

#### (ii) BiLSTM-CRF
Note: only for named entity extraction (people and companies).

Add a CRF layer to a Bi-LSTM architecture.

<p align="center">BiLSTM-CRF Model Structure</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/BiLSTM+CRF2.PNG" 
 width="500" height="390" />
</p>

<br>

##### Performance

<p align="center">Confusion Matrix</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/bi.PNG" 
 width="430" height="130" />
</p>

<br>

<p align="center">Customized Input Test on the Trained Model</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/bi1.PNG" 
 width="500" height="170" />
</p>

#### (iii) IDCNN-CRF
Note: only for named entity extraction (people and companies).

Dilated convolutions can expand the receptive field exponentially.

<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/dilated.PNG" 
 width="500" height="170" />
</p>
<p align="center">Yu F., Koltun V., Multi-Scale Context Aggregation by Dilated Convolutions (2016)</p>

Simply increasing the depth of stacked dilated convolutions would cause overfitting problems. Therefore, Strubell E. et al.(2017) proposed IDCNN(Iterated Dilated Convolutional Neural Networks), which iteratively apply the same small stacks of dilated convolutions. Repeatedly employing
the same parameters in a recurrent fashion helps the model memorize longer and generalize better.


Performance

<p align="center">Confusion Matrix</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/id.PNG" 
 width="400" height="110" />
</p>

<p align="center">Customized Input Test on the Trained Model</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/id1.PNG" 
 width="400" height="110" />
</p>
## 3. Knowledge Merge

Use rule-based methods to implement entity disambiguation and coreference resolution.

## 4. Knowledge Storage
<p align="center">Entity Relationship Diagram</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/er.PNG" 
 width="200" height="110" />
</p>

Based on entity relationship, the data is stored in SPO triples.
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/spo.PNG" 
 width="300" height="150" />
</p>

## 5. Visualization (Knowledge Graph)
Use Gephi to visualize the knowledge graph.
<p align="center">The Whole Knowledge Graph</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/small.PNG" 
 width="300" height="150" />
</p>

<p align="center">Zoomed in Knowledge Graph</p>
<p align="center">
<img src="https://github.com/AlexaYuqinD/Knowledge-Graph-for-Activities-of-Investor-Relations/blob/master/images/big.PNG" 
 width="300" height="150" />
</p>

## Reference
[crownpku/Information-Extraction-Chinese](https://github.com/crownpku/Information-Extraction-Chinese)

[hankcs/HanLP](https://github.com/hankcs/HanLP)

[shiyybua/NER](https://github.com/shiyybua/NER)

[Strubell E., Verga P., Belanger D., McCallum A.](https://arxiv.org/abs/1702.02098)

[Yu F., Koltun V.](https://arxiv.org/abs/1511.07122)
