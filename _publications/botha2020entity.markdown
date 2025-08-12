---
layout: publication
title: Entity Linking In 100 Languages
authors: Jan A. Botha, Zifei Shan, Daniel Gillick
conference: Proceedings of the 2020 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2020
bibkey: botha2020entity
citations: 68
additional_links: [{name: Code, url: 'http://goo.gle/mewsli-dataset)'}, {name: Paper,
    url: 'https://arxiv.org/abs/2011.02690'}]
tags: ["Datasets", "EMNLP"]
short_authors: Jan A. Botha, Zifei Shan, Daniel Gillick
---
We propose a new formulation for multilingual entity linking, where
language-specific mentions resolve to a language-agnostic Knowledge Base. We
train a dual encoder in this new setting, building on prior work with improved
feature representation, negative mining, and an auxiliary entity-pairing task,
to obtain a single entity retrieval model that covers 100+ languages and 20
million entities. The model outperforms state-of-the-art results from a far
more limited cross-lingual linking task. Rare entities and low-resource
languages pose challenges at this large-scale, so we advocate for an increased
focus on zero- and few-shot evaluation. To this end, we provide Mewsli-9, a
large new multilingual dataset (http://goo.gle/mewsli-dataset) matched to our
setting, and show how frequency-based analysis provided key insights for our
model and training enhancements.