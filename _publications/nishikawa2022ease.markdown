---
layout: publication
title: 'EASE: Entity-aware Contrastive Learning Of Sentence Embedding'
authors: Sosuke Nishikawa, Ryokan Ri, Ikuya Yamada, Yoshimasa Tsuruoka, Isao Echizen
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: nishikawa2022ease
citations: 20
additional_links: [{name: Code, url: 'https://github.com/studio-ousia/ease'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.04260'}]
tags: ["NAACL", "Self-Supervised"]
short_authors: Nishikawa et al.
---
We present EASE, a novel method for learning sentence embeddings via
contrastive learning between sentences and their related entities. The
advantage of using entity supervision is twofold: (1) entities have been shown
to be a strong indicator of text semantics and thus should provide rich
training signals for sentence embeddings; (2) entities are defined
independently of languages and thus offer useful cross-lingual alignment
supervision. We evaluate EASE against other unsupervised models both in
monolingual and multilingual settings. We show that EASE exhibits competitive
or better performance in English semantic textual similarity (STS) and short
text clustering (STC) tasks and it significantly outperforms baseline methods
in multilingual settings on a variety of tasks. Our source code, pre-trained
models, and newly constructed multilingual STC dataset are available at
https://github.com/studio-ousia/ease.