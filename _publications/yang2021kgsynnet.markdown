---
layout: publication
title: 'Kgsynnet: A Novel Entity Synonyms Discovery Framework With Knowledge Graph'
authors: Yiying Yang, Xi Yin, Haiqin Yang, Xingjian Fei, Hao Peng, Kaijie Zhou, Kunfeng
  Lai, Jianping Shen
conference: Lecture Notes in Computer Science
year: 2021
bibkey: yang2021kgsynnet
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.08893'}]
tags: ["Tools & Libraries"]
short_authors: Yang et al.
---
Entity synonyms discovery is crucial for entity-leveraging applications.
However, existing studies suffer from several critical issues: (1) the input
mentions may be out-of-vocabulary (OOV) and may come from a different semantic
space of the entities; (2) the connection between mentions and entities may be
hidden and cannot be established by surface matching; and (3) some entities
rarely appear due to the long-tail effect. To tackle these challenges, we
facilitate knowledge graphs and propose a novel entity synonyms discovery
framework, named *KGSynNet*. Specifically, we pre-train subword embeddings
for mentions and entities using a large-scale domain-specific corpus while
learning the knowledge embeddings of entities via a joint TransC-TransE model.
More importantly, to obtain a comprehensive representation of entities, we
employ a specifically designed *fusion gate* to adaptively absorb the
entities' knowledge information into their semantic features. We conduct
extensive experiments to demonstrate the effectiveness of our *KGSynNet*
in leveraging the knowledge graph. The experimental results show that the
*KGSynNet* improves the state-of-the-art methods by 14.7% in terms of
hits@3 in the offline evaluation and outperforms the BERT model by 8.3% in the
positive feedback rate of an online A/B test on the entity linking module of a
question answering system.