---
layout: publication
title: Evaluating Various Tokenizers For Arabic Text Classification
authors: Zaid Alyafeai, Maged S. Al-shaibani, Mustafa Ghaleb, Irfan Ahmad
conference: Neural Processing Letters
year: 2022
bibkey: alyafeai2021evaluating
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.07540'}]
tags: ["Datasets", "Evaluation"]
short_authors: Alyafeai et al.
---
The first step in any NLP pipeline is to split the text into individual
tokens. The most obvious and straightforward approach is to use words as
tokens. However, given a large text corpus, representing all the words is not
efficient in terms of vocabulary size. In the literature, many tokenization
algorithms have emerged to tackle this problem by creating subwords which in
turn limits the vocabulary size in a given text corpus. Most tokenization
techniques are language-agnostic i.e they don't incorporate the linguistic
features of a given language. Not to mention the difficulty of evaluating such
techniques in practice. In this paper, we introduce three new tokenization
algorithms for Arabic and compare them to three other baselines using
unsupervised evaluations. In addition to that, we compare all the six
algorithms by evaluating them on three supervised classification tasks which
are sentiment analysis, news classification and poetry classification using six
publicly available datasets. Our experiments show that none of the tokenization
technique is the best choice overall and that the performance of a given
tokenization algorithm depends on the size of the dataset, type of the task,
and the amount of morphology that exists in the dataset. However, some
tokenization techniques are better overall as compared to others on various
text classification tasks.