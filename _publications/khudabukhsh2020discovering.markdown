---
layout: publication
title: Discovering Bilingual Lexicons In Polyglot Word Embeddings
authors: Khudabukhsh Ashiqur R., Palakodety Shriphani, Mitchell Tom M.
conference: Arxiv
year: 2020
bibkey: khudabukhsh2020discovering
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.13347'}]
tags: ["Unsupervised"]
short_authors: Khudabukhsh Ashiqur R., Palakodety Shriphani, Mitchell Tom M.
---
Bilingual lexicons and phrase tables are critical resources for modern
Machine Translation systems. Although recent results show that without any seed
lexicon or parallel data, highly accurate bilingual lexicons can be learned
using unsupervised methods, such methods rely on the existence of large, clean
monolingual corpora. In this work, we utilize a single Skip-gram model trained
on a multilingual corpus yielding polyglot word embeddings, and present a novel
finding that a surprisingly simple constrained nearest-neighbor sampling
technique in this embedding space can retrieve bilingual lexicons, even in
harsh social media data sets predominantly written in English and Romanized
Hindi and often exhibiting code switching. Our method does not require
monolingual corpora, seed lexicons, or any other such resources. Additionally,
across three European language pairs, we observe that polyglot word embeddings
indeed learn a rich semantic representation of words and substantial bilingual
lexicons can be retrieved using our constrained nearest neighbor sampling. We
investigate potential reasons and downstream applications in settings spanning
both clean texts and noisy social media data sets, and in both resource-rich
and under-resourced language pairs.