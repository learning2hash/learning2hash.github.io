---
layout: publication
title: Nict's Corpus Filtering Systems For The WMT18 Parallel Corpus Filtering Task
authors: Rui Wang, Benjamin Marie, Masao Utiyama, Eiichiro Sumita
conference: Arxiv
year: 2018
bibkey: wang2018nict
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.07043'}]
tags: ["Evaluation"]
short_authors: Wang et al.
---
This paper presents the NICT's participation in the WMT18 shared parallel
corpus filtering task. The organizers provided 1 billion words German-English
corpus crawled from the web as part of the Paracrawl project. This corpus is
too noisy to build an acceptable neural machine translation (NMT) system. Using
the clean data of the WMT18 shared news translation task, we designed several
features and trained a classifier to score each sentence pairs in the noisy
data. Finally, we sampled 100 million and 10 million words and built
corresponding NMT systems. Empirical results show that our NMT systems trained
on sampled data achieve promising performance.