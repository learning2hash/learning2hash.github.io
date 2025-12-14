---
layout: publication
title: A Statutory Article Retrieval Dataset In French
authors: Antoine Louis, Gerasimos Spanakis
conference: Arxiv
year: 2021
bibkey: louis2021a
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.11792'}]
tags: [Evaluation, Supervised, Few-shot & Zero-shot, Datasets, Scalability]
short_authors: Antoine Louis, Gerasimos Spanakis
---
Statutory article retrieval is the task of automatically retrieving law
articles relevant to a legal question. While recent advances in natural
language processing have sparked considerable interest in many legal tasks,
statutory article retrieval remains primarily untouched due to the scarcity of
large-scale and high-quality annotated datasets. To address this bottleneck, we
introduce the Belgian Statutory Article Retrieval Dataset (BSARD), which
consists of 1,100+ French native legal questions labeled by experienced jurists
with relevant articles from a corpus of 22,600+ Belgian law articles. Using
BSARD, we benchmark several state-of-the-art retrieval approaches, including
lexical and dense architectures, both in zero-shot and supervised setups. We
find that fine-tuned dense retrieval models significantly outperform other
systems. Our best performing baseline achieves 74.8% R@100, which is promising
for the feasibility of the task and indicates there is still room for
improvement. By the specificity of the domain and addressed task, BSARD
presents a unique challenge problem for future research on legal information
retrieval. Our dataset and source code are publicly available.