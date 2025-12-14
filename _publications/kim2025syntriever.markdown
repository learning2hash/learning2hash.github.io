---
layout: publication
title: 'Syntriever: How To Train Your Retriever With Synthetic Data From Llms'
authors: Minsang Kim, Seungjun Baek
conference: 'Findings of the Association for Computational Linguistics: NAACL 2025'
year: 2025
bibkey: kim2025syntriever
citations: 1
additional_links: [{name: Code, url: 'https://github.com/kmswin1/Syntriever\'}, {
    name: Paper, url: 'https://arxiv.org/abs/2502.03824'}]
tags: [Evaluation, NAACL, Datasets, Tools & Libraries, ACL]
short_authors: Minsang Kim, Seungjun Baek
---
LLMs have boosted progress in many AI applications. Recently, there were
attempts to distill the vast knowledge of LLMs into information retrieval
systems. Those distillation methods mostly use output probabilities of LLMs
which are unavailable in the latest black-box LLMs. We propose Syntriever, a
training framework for retrievers using synthetic data from black-box LLMs.
Syntriever consists of two stages. Firstly in the distillation stage, we
synthesize relevant and plausibly irrelevant passages and augmented queries
using chain-of-thoughts for the given queries. LLM is asked to self-verify the
synthetic data for possible hallucinations, after which retrievers are trained
with a loss designed to cluster the embeddings of relevant passages. Secondly
in the alignment stage, we align the retriever with the preferences of LLMs. We
propose a preference modeling called partial Plackett-Luce ranking to learn LLM
preferences with regularization which prevents the model from deviating
excessively from that trained in the distillation stage. Experiments show that
Syntriever achieves state-of-the-art performances on benchmark datasets from
various domains in nDCG@\(K\). The code is available at
\href\{https://github.com/kmswin1/Syntriever\}\{https://github.com/kmswin1/Syntriever\}.