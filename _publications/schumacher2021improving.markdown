---
layout: publication
title: Improving Zero-shot Multi-lingual Entity Linking
authors: Elliot Schumacher, James Mayfield, Mark Dredze
conference: Arxiv
year: 2021
bibkey: schumacher2021improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08082'}]
tags: ["Few Shot & Zero Shot", "Robustness"]
short_authors: Elliot Schumacher, James Mayfield, Mark Dredze
---
Entity linking -- the task of identifying references in free text to relevant
knowledge base representations -- often focuses on single languages. We
consider multilingual entity linking, where a single model is trained to link
references to same-language knowledge bases in several languages. We propose a
neural ranker architecture, which leverages multilingual transformer
representations of text to be easily applied to a multilingual setting. We then
explore how a neural ranker trained in one language (e.g. English) transfers to
an unseen language (e.g. Chinese), and find that while there is a consistent
but not large drop in performance. How can this drop in performance be
alleviated? We explore adding an adversarial objective to force our model to
learn language-invariant representations. We find that using this approach
improves recall in several datasets, often matching the in-language
performance, thus alleviating some of the performance loss occurring from
zero-shot transfer.