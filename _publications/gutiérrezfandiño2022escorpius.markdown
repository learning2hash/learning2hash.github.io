---
layout: publication
title: 'Escorpius: A Massive Spanish Crawling Corpus'
authors: "Asier Guti\xE9rrez-Fandi\xF1o, David P\xE9rez-Fern\xE1ndez, Jordi Armengol-Estap\xE9\
  , David Griol, Zoraida Callejas"
conference: IberSPEECH 2022
year: 2022
bibkey: "guti\xE9rrezfandi\xF1o2022escorpius"
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.15147'}]
tags: ["Datasets"]
short_authors: "Guti\xE9rrez-Fandi\xF1o et al."
---
In the recent years, transformer-based models have lead to significant
advances in language modelling for natural language processing. However, they
require a vast amount of data to be (pre-)trained and there is a lack of
corpora in languages other than English. Recently, several initiatives have
presented multilingual datasets obtained from automatic web crawling. However,
the results in Spanish present important shortcomings, as they are either too
small in comparison with other languages, or present a low quality derived from
sub-optimal cleaning and deduplication. In this paper, we introduce esCorpius,
a Spanish crawling corpus obtained from near 1 Pb of Common Crawl data. It is
the most extensive corpus in Spanish with this level of quality in the
extraction, purification and deduplication of web textual content. Our data
curation process involves a novel highly parallel cleaning pipeline and
encompasses a series of deduplication mechanisms that together ensure the
integrity of both document and paragraph boundaries. Additionally, we maintain
both the source web page URL and the WARC shard origin URL in order to complain
with EU regulations. esCorpius has been released under CC BY-NC-ND 4.0 license
and is available on HuggingFace.