---
layout: publication
title: Improving Candidate Retrieval With Entity Profile Generation For Wikidata Entity
  Linking
authors: Tuan Manh Lai, Heng Ji, Chengxiang Zhai
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: lai2022improving
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.13404'}]
tags: ["Datasets", "Text Retrieval"]
short_authors: Tuan Manh Lai, Heng Ji, Chengxiang Zhai
---
Entity linking (EL) is the task of linking entity mentions in a document to
referent entities in a knowledge base (KB). Many previous studies focus on
Wikipedia-derived KBs. There is little work on EL over Wikidata, even though it
is the most extensive crowdsourced KB. The scale of Wikidata can open up many
new real-world applications, but its massive number of entities also makes EL
challenging. To effectively narrow down the search space, we propose a novel
candidate retrieval paradigm based on entity profiling. Wikidata entities and
their textual fields are first indexed into a text search engine (e.g.,
Elasticsearch). During inference, given a mention and its context, we use a
sequence-to-sequence (seq2seq) model to generate the profile of the target
entity, which consists of its title and description. We use the profile to
query the indexed search engine to retrieve candidate entities. Our approach
complements the traditional approach of using a Wikipedia anchor-text
dictionary, enabling us to further design a highly effective hybrid method for
candidate retrieval. Combined with a simple cross-attention reranker, our
complete EL framework achieves state-of-the-art results on three Wikidata-based
datasets and strong performance on TACKBP-2010.