---
layout: publication
title: Distant Supervision For Entity Linking
authors: Miao Fan, Qiang Zhou, Thomas Fang Zheng
conference: Arxiv
year: 2015
bibkey: fan2015distant
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.03823'}]
tags: ["Datasets", "Supervised"]
short_authors: Miao Fan, Qiang Zhou, Thomas Fang Zheng
---
Entity linking is an indispensable operation of populating knowledge
repositories for information extraction. It studies on aligning a textual
entity mention to its corresponding disambiguated entry in a knowledge
repository. In this paper, we propose a new paradigm named distantly supervised
entity linking (DSEL), in the sense that the disambiguated entities that belong
to a huge knowledge repository (Freebase) are automatically aligned to the
corresponding descriptive webpages (Wiki pages). In this way, a large scale of
weakly labeled data can be generated without manual annotation and fed to a
classifier for linking more newly discovered entities. Compared with
traditional paradigms based on solo knowledge base, DSEL benefits more via
jointly leveraging the respective advantages of Freebase and Wikipedia.
Specifically, the proposed paradigm facilitates bridging the disambiguated
labels (Freebase) of entities and their textual descriptions (Wikipedia) for
Web-scale entities. Experiments conducted on a dataset of 140,000 items and
60,000 features achieve a baseline F1-measure of 0.517. Furthermore, we analyze
the feature performance and improve the F1-measure to 0.545.