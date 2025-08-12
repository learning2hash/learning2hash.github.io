---
layout: publication
title: Few-shot Sequence Labeling With Label Dependency Transfer And Pair-wise Embedding
authors: Yutai Hou, Zhihan Zhou, Yijia Liu, Ning Wang, Wanxiang Che, Han Liu, Ting
  Liu
conference: Arxiv
year: 2019
bibkey: hou2019few
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.08711'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hou et al.
---
While few-shot classification has been widely explored with similarity based
methods, few-shot sequence labeling poses a unique challenge as it also calls
for modeling the label dependencies. To consider both the item similarity and
label dependency, we propose to leverage the conditional random fields (CRFs)
in few-shot sequence labeling. It calculates emission score with similarity
based methods and obtains transition score with a specially designed transfer
mechanism. When applying CRF in the few-shot scenarios, the discrepancy of
label sets among different domains makes it hard to use the label dependency
learned in prior domains. To tackle this, we introduce the dependency transfer
mechanism that transfers abstract label transition patterns. In addition, the
similarity methods rely on the high quality sample representation, which is
challenging for sequence labeling, because sense of a word is different when
measuring its similarity to words in different sentences. To remedy this, we
take advantage of recent contextual embedding technique, and further propose a
pair-wise embedder. It provides additional certainty for word sense by
embedding query and support sentence pairwisely. Experimental results on slot
tagging and named entity recognition show that our model significantly
outperforms the strongest few-shot learning baseline by 11.76 (21.2%) and 12.18
(97.7%) F1 scores respectively in the one-shot setting.