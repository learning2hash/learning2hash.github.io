---
layout: publication
title: Learning To Recommend Items To Wikidata Editors
authors: Kholoud Alghamdi, Miaojing Shi, Elena Simperl
conference: Lecture Notes in Computer Science
year: 2021
bibkey: alghamdi2021learning
citations: 2
additional_links: [{name: Code, url: 'https://github.com/WikidataRec-developer/Wikidata_Recommender'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.06423'}]
tags: ["Recommender Systems"]
short_authors: Kholoud Alghamdi, Miaojing Shi, Elena Simperl
---
Wikidata is an open knowledge graph built by a global community of
volunteers. As it advances in scale, it faces substantial challenges around
editor engagement. These challenges are in terms of both attracting new editors
to keep up with the sheer amount of work and retaining existing editors.
Experience from other online communities and peer-production systems, including
Wikipedia, suggests that personalised recommendations could help, especially
newcomers, who are sometimes unsure about how to contribute best to an ongoing
effort. For this reason, we propose a recommender system WikidataRec for
Wikidata items. The system uses a hybrid of content-based and collaborative
filtering techniques to rank items for editors relying on both item features
and item-editor previous interaction. A neural network, named a neural mixture
of representations, is designed to learn fine weights for the combination of
item-based representations and optimize them with editor-based representation
by item-editor interaction. To facilitate further research in this space, we
also create two benchmark datasets, a general-purpose one with 220,000 editors
responsible for 14 million interactions with 4 million items and a second one
focusing on the contributions of more than 8,000 more active editors. We
perform an offline evaluation of the system on both datasets with promising
results. Our code and datasets are available at
https://github.com/WikidataRec-developer/Wikidata_Recommender.