---
layout: publication
title: Injecting Domain Adaptation With Learning-to-hash For Effective And Efficient
  Zero-shot Dense Retrieval
authors: Nandan Thakur, Nils Reimers, Jimmy Lin
conference: Arxiv
year: 2022
bibkey: thakur2022injecting
citations: 6
additional_links: [{name: Code, url: 'https://github.com/thakur-nandan/income.'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.11498'}]
tags: [Memory Efficiency, Datasets, Quantization, Efficiency, Supervised, Few-shot
    & Zero-shot, Unsupervised, Evaluation]
short_authors: Nandan Thakur, Nils Reimers, Jimmy Lin
---
Dense retrieval overcome the lexical gap and has shown great success in
ad-hoc information retrieval (IR). Despite their success, dense retrievers are
expensive to serve across practical use cases. For use cases requiring to
search from millions of documents, the dense index becomes bulky and requires
high memory usage for storing the index. More recently, learning-to-hash (LTH)
techniques, for e.g., BPR and JPQ, produce binary document vectors, thereby
reducing the memory requirement to efficiently store the dense index. LTH
techniques are supervised and finetune the retriever using a ranking loss. They
outperform their counterparts, i.e., traditional out-of-the-box vector
compression techniques such as PCA or PQ. A missing piece from prior work is
that existing techniques have been evaluated only in-domain, i.e., on a single
dataset such as MS MARCO. In our work, we evaluate LTH and vector compression
techniques for improving the downstream zero-shot retrieval accuracy of the
TAS-B dense retriever while maintaining efficiency at inference. Our results
demonstrate that, unlike prior work, LTH strategies when applied naively can
underperform the zero-shot TAS-B dense retriever on average by up to 14%
nDCG@10 on the BEIR benchmark. To solve this limitation, in our work, we
propose an easy yet effective solution of injecting domain adaptation with
existing supervised LTH techniques. We experiment with two well-known
unsupervised domain adaptation techniques: GenQ and GPL. Our domain adaptation
injection technique can improve the downstream zero-shot retrieval
effectiveness for both BPR and JPQ variants of the TAS-B model by on average
11.5% and 8.2% nDCG@10 while both maintaining 32\(\times\) memory efficiency and
14\(\times\) and 2\(\times\) speedup respectively in CPU retrieval latency on BEIR.
All our code, models, and data are publicly available at
https://github.com/thakur-nandan/income.