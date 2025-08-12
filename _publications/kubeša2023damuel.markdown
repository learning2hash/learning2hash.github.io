---
layout: publication
title: 'Damuel: A Large Multilingual Dataset For Entity Linking'
authors: "David Kube\u0161a, Milan Straka"
conference: Arxiv
year: 2023
bibkey: "kube\u0161a2023damuel"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.09288'}]
tags: ["Datasets"]
short_authors: "David Kube\u0161a, Milan Straka"
---
We present DaMuEL, a large Multilingual Dataset for Entity Linking containing
data in 53 languages. DaMuEL consists of two components: a knowledge base that
contains language-agnostic information about entities, including their claims
from Wikidata and named entity types (PER, ORG, LOC, EVENT, BRAND, WORK_OF_ART,
MANUFACTURED); and Wikipedia texts with entity mentions linked to the knowledge
base, along with language-specific text from Wikidata such as labels, aliases,
and descriptions, stored separately for each language. The Wikidata QID is used
as a persistent, language-agnostic identifier, enabling the combination of the
knowledge base with language-specific texts and information for each entity.
Wikipedia documents deliberately annotate only a single mention for every
entity present; we further automatically detect all mentions of named entities
linked from each document. The dataset contains 27.9M named entities in the
knowledge base and 12.3G tokens from Wikipedia texts. The dataset is published
under the CC BY-SA license at https://hdl.handle.net/11234/1-5047.