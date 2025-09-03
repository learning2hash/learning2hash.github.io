---
layout: publication
title: 'GRI: Graph-based Relative Isomorphism Of Word Embedding Spaces'
authors: Muhammad Asif Ali, Yan Hu, Jianbin Qin, di Wang
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2023'
year: 2023
bibkey: ali2023gri
citations: 1
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2310.12360'}]
tags: ["EMNLP", "Evaluation", "Graph Based ANN"]
short_authors: Ali et al.
---
Automated construction of bilingual dictionaries using monolingual embedding
spaces is a core challenge in machine translation. The end performance of these
dictionaries relies upon the geometric similarity of individual spaces, i.e.,
their degree of isomorphism. Existing attempts aimed at controlling the
relative isomorphism of different spaces fail to incorporate the impact of
semantically related words in the training objective. To address this, we
propose GRI that combines the distributional training objectives with attentive
graph convolutions to unanimously consider the impact of semantically similar
words required to define/compute the relative isomorphism of multiple spaces.
Experimental evaluation shows that GRI outperforms the existing research by
improving the average P@1 by a relative score of up to 63.6%. We release the
codes for GRI at https://github.com/asif6827/GRI.