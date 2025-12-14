---
layout: publication
title: Unsupervised Cross-lingual Information Retrieval Using Monolingual Data Only
authors: "Robert Litschko, Goran Glava\u0161, Simone Paolo Ponzetto, Ivan Vuli\u0107"
conference: The 41st International ACM SIGIR Conference on Research &amp; Development
  in Information Retrieval
year: 2018
bibkey: litschko2018unsupervised
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.00879'}]
tags: [Supervised, Robustness, Tools & Libraries, Unsupervised, SIGIR]
short_authors: Litschko et al.
---
We propose a fully unsupervised framework for ad-hoc cross-lingual
information retrieval (CLIR) which requires no bilingual data at all. The
framework leverages shared cross-lingual word embedding spaces in which terms,
queries, and documents can be represented, irrespective of their actual
language. The shared embedding spaces are induced solely on the basis of
monolingual corpora in two languages through an iterative process based on
adversarial neural networks. Our experiments on the standard CLEF CLIR
collections for three language pairs of varying degrees of language similarity
(English-Dutch/Italian/Finnish) demonstrate the usefulness of the proposed
fully unsupervised approach. Our CLIR models with unsupervised cross-lingual
embeddings outperform baselines that utilize cross-lingual embeddings induced
relying on word-level and document-level alignments. We then demonstrate that
further improvements can be achieved by unsupervised ensemble CLIR models. We
believe that the proposed framework is the first step towards development of
effective CLIR models for language pairs and domains where parallel data are
scarce or non-existent.