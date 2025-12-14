---
layout: publication
title: Cross-lingual Knowledge Transfer Via Distillation For Multilingual Information
  Retrieval
authors: Zhiqi Huang, Puxuan Yu, James Allan
conference: Arxiv
year: 2023
bibkey: huang2023cross
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.13400'}]
tags: [Uncategorized]
short_authors: Zhiqi Huang, Puxuan Yu, James Allan
---
In this paper, we introduce the approach behind our submission for the MIRACL
challenge, a WSDM 2023 Cup competition that centers on ad-hoc retrieval across
18 diverse languages. Our solution contains two neural-based models. The first
model is a bi-encoder re-ranker, on which we apply a cross-lingual distillation
technique to transfer ranking knowledge from English to the target language
space. The second model is a cross-encoder re-ranker trained on multilingual
retrieval data generated using neural machine translation. We further fine-tune
both models using MIRACL training data and ensemble multiple rank lists to
obtain the final result. According to the MIRACL leaderboard, our approach
ranks 8th for the Test-A set and 2nd for the Test-B set among the 16 known
languages.