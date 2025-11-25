---
layout: publication
title: Match Your Words! A Study Of Lexical Matching In Neural Information Retrieval
authors: "Thibault Formal, Benjamin Piwowarski, St\xE9phane Clinchant"
conference: Arxiv
year: 2021
bibkey: formal2021match
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.05662'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: "Thibault Formal, Benjamin Piwowarski, St\xE9phane Clinchant"
---
Neural Information Retrieval models hold the promise to replace lexical
matching models, e.g. BM25, in modern search engines. While their capabilities
have fully shone on in-domain datasets like MS MARCO, they have recently been
challenged on out-of-domain zero-shot settings (BEIR benchmark), questioning
their actual generalization capabilities compared to bag-of-words approaches.
Particularly, we wonder if these shortcomings could (partly) be the consequence
of the inability of neural IR models to perform lexical matching off-the-shelf.
In this work, we propose a measure of discrepancy between the lexical matching
performed by any (neural) model and an 'ideal' one. Based on this, we study the
behavior of different state-of-the-art neural IR models, focusing on whether
they are able to perform lexical matching when it's actually useful, i.e. for
important terms. Overall, we show that neural IR models fail to properly
generalize term importance on out-of-domain collections or terms almost unseen
during training