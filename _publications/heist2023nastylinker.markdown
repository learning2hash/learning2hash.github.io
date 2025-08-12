---
layout: publication
title: 'Nastylinker: Nil-aware Scalable Transformer-based Entity Linker'
authors: Nicolas Heist, Heiko Paulheim
conference: Lecture Notes in Computer Science
year: 2023
bibkey: heist2023nastylinker
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.04426'}]
tags: ["Scalability"]
short_authors: Nicolas Heist, Heiko Paulheim
---
Entity Linking (EL) is the task of detecting mentions of entities in text and
disambiguating them to a reference knowledge base. Most prevalent EL approaches
assume that the reference knowledge base is complete. In practice, however, it
is necessary to deal with the case of linking to an entity that is not
contained in the knowledge base (NIL entity). Recent works have shown that,
instead of focusing only on affinities between mentions and entities,
considering inter-mention affinities can be used to represent NIL entities by
producing clusters of mentions. At the same time, inter-mention affinities can
help to substantially improve linking performance for known entities. With
NASTyLinker, we introduce an EL approach that is aware of NIL entities and
produces corresponding mention clusters while maintaining high linking
performance for known entities. The approach clusters mentions and entities
based on dense representations from Transformers and resolves conflicts (if
more than one entity is assigned to a cluster) by computing transitive
mention-entity affinities. We show the effectiveness and scalability of
NASTyLinker on NILK, a dataset that is explicitly constructed to evaluate EL
with respect to NIL entities. Further, we apply the presented approach to an
actual EL task, namely to knowledge graph population by linking entities in
Wikipedia listings, and provide an analysis of the outcome.