---
layout: publication
title: End-to-end Neural Entity Linking
authors: Nikolaos Kolitsas, Octavian-Eugen Ganea, Thomas Hofmann
conference: Proceedings of the 22nd Conference on Computational Natural Language Learning
year: 2018
bibkey: kolitsas2018end
citations: 239
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.07699'}]
tags: ["Datasets", "Evaluation"]
short_authors: Nikolaos Kolitsas, Octavian-Eugen Ganea, Thomas Hofmann
---
Entity Linking (EL) is an essential task for semantic text understanding and
information extraction. Popular methods separately address the Mention
Detection (MD) and Entity Disambiguation (ED) stages of EL, without leveraging
their mutual dependency. We here propose the first neural end-to-end EL system
that jointly discovers and links entities in a text document. The main idea is
to consider all possible spans as potential mentions and learn contextual
similarity scores over their entity candidates that are useful for both MD and
ED decisions. Key components are context-aware mention embeddings, entity
embeddings and a probabilistic mention - entity map, without demanding other
engineered features. Empirically, we show that our end-to-end method
significantly outperforms popular systems on the Gerbil platform when enough
training data is available. Conversely, if testing datasets follow different
annotation conventions compared to the training set (e.g. queries/ tweets vs
news documents), our ED model coupled with a traditional NER system offers the
best or second best EL accuracy.