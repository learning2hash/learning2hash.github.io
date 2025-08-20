---
layout: publication
title: Unbiased Sentence Encoder For Large-scale Multi-lingual Search Engines
authors: Mahdi Hajiaghayi, Monir Hajiaghayi, Mark Bolin
conference: Arxiv
year: 2021
bibkey: hajiaghayi2021unbiased
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.07719'}]
tags: [Datasets, Scalability]
short_authors: Mahdi Hajiaghayi, Monir Hajiaghayi, Mark Bolin
---
In this paper, we present a multi-lingual sentence encoder that can be used
in search engines as a query and document encoder. This embedding enables a
semantic similarity score between queries and documents that can be an
important feature in document ranking and relevancy. To train such a customized
sentence encoder, it is beneficial to leverage users search data in the form of
query-document clicked pairs however, we must avoid relying too much on search
click data as it is biased and does not cover many unseen cases. The search
data is heavily skewed towards short queries and for long queries is small and
often noisy. The goal is to design a universal multi-lingual encoder that works
for all cases and covers both short and long queries. We select a number of
public NLI datasets in different languages and translation data and together
with user search data we train a language model using a multi-task approach. A
challenge is that these datasets are not homogeneous in terms of content, size
and the balance ratio. While the public NLI datasets are usually two-sentence
based with the same portion of positive and negative pairs, the user search
data can contain multi-sentence documents and only positive pairs. We show how
multi-task training enables us to leverage all these datasets and exploit
knowledge sharing across these tasks.