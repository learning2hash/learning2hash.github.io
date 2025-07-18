---
layout: publication
title: 'Fasttext.zip: Compressing Text Classification Models'
authors: Joulin et al.
conference: Arxiv
year: 2016
bibkey: joulin2016fasttext
citations: 872
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.03651'}]
tags: [Quantization, Hashing Methods, Evaluation]
---
We consider the problem of producing compact architectures for text
classification, such that the full model fits in a limited amount of memory.
After considering different solutions inspired by the hashing literature, we
propose a method built upon product quantization to store word embeddings.
While the original technique leads to a loss in accuracy, we adapt this method
to circumvent quantization artefacts. Our experiments carried out on several
benchmarks show that our approach typically requires two orders of magnitude
less memory than fastText while being only slightly inferior with respect to
accuracy. As a result, it outperforms the state of the art by a good margin in
terms of the compromise between memory usage and accuracy.