---
layout: publication
title: Few-Shot Keyword Spotting in Any Language
authors: Mazumder et al.
conference: Interspeech 2021
year: 2021
bibkey: mazumder2021few
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01454'}]
tags: ["Few Shot & Zero Shot"]
---
We introduce a few-shot transfer learning method for keyword spotting in any
language. Leveraging open speech corpora in nine languages, we automate the
extraction of a large multilingual keyword bank and use it to train an
embedding model. With just five training examples, we fine-tune the embedding
model for keyword spotting and achieve an average F1 score of 0.75 on keyword
classification for 180 new keywords unseen by the embedding model in these nine
languages. This embedding model also generalizes to new languages. We achieve
an average F1 score of 0.65 on 5-shot models for 260 keywords sampled across 13
new languages unseen by the embedding model. We investigate streaming accuracy
for our 5-shot models in two contexts: keyword spotting and keyword search.
Across 440 keywords in 22 languages, we achieve an average streaming keyword
spotting accuracy of 87.4% with a false acceptance rate of 4.3%, and observe
promising initial results on keyword search.