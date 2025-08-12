---
layout: publication
title: Neural Cross-lingual Entity Linking
authors: Avirup Sil, Gourab Kundu, Radu Florian, Wael Hamza
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2018
bibkey: sil2017neural
citations: 67
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.01813'}]
tags: ["AAAI"]
short_authors: Sil et al.
---
A major challenge in Entity Linking (EL) is making effective use of
contextual information to disambiguate mentions to Wikipedia that might refer
to different entities in different contexts. The problem exacerbates with
cross-lingual EL which involves linking mentions written in non-English
documents to entries in the English Wikipedia: to compare textual clues across
languages we need to compute similarity between textual fragments across
languages. In this paper, we propose a neural EL model that trains fine-grained
similarities and dissimilarities between the query and candidate document from
multiple perspectives, combined with convolution and tensor networks. Further,
we show that this English-trained system can be applied, in zero-shot learning,
to other languages by making surprisingly effective use of multi-lingual
embeddings. The proposed system has strong empirical evidence yielding
state-of-the-art results in English as well as cross-lingual: Spanish and
Chinese TAC 2015 datasets.