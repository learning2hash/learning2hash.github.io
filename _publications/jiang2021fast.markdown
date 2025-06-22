---
layout: publication
title: A Fast Randomized Algorithm For Massive Text Normalization
authors: Nan Jiang, Chen Luo, Vihan Lakshman, Yesh Dattatreya, Yexiang Xue
conference: Arxiv
year: 2021
citations: 1
bibkey: jiang2021fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.03024'}]
tags: [Tools and Libraries, ANN Search, KDD, Hashing Methods]
---
Many popular machine learning techniques in natural language processing and
data mining rely heavily on high-quality text sources. However real-world text
datasets contain a significant amount of spelling errors and improperly
punctuated variants where the performance of these models would quickly
deteriorate. Moreover, real-world, web-scale datasets contain hundreds of
millions or even billions of lines of text, where the existing text cleaning
tools are prohibitively expensive to execute over and may require an overhead
to learn the corrections. In this paper, we present FLAN, a scalable randomized
algorithm to clean and canonicalize massive text data. Our algorithm relies on
the Jaccard similarity between words to suggest correction results. We
efficiently handle the pairwise word-to-word comparisons via Locality Sensitive
Hashing (LSH). We also propose a novel stabilization process to address the
issue of hash collisions between dissimilar words, which is a consequence of
the randomized nature of LSH and is exacerbated by the massive scale of
real-world datasets. Compared with existing approaches, our method is more
efficient, both asymptotically and in empirical evaluations, and does not rely
on additional features, such as lexical/phonetic similarity or word embedding
features. In addition, FLAN does not require any annotated data or supervised
learning. We further theoretically show the robustness of our algorithm with
upper bounds on the false positive and false negative rates of corrections. Our
experimental results on real-world datasets demonstrate the efficiency and
efficacy of FLAN.