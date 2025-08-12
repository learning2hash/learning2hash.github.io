---
layout: publication
title: Entity Disambiguation Via Fusion Entity Decoding
authors: Junxiong Wang, Ali Mousavi, Omar Attia, Ronak Pradeep, Saloni Potdar, Alexander
  M. Rush, Umar Farooq Minhas, Yunyao Li
conference: 'Proceedings of the 2024 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies (Volume 1:
  Long Papers)'
year: 2024
bibkey: wang2024entity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01626'}]
tags: ["NAACL"]
short_authors: Wang et al.
---
Entity disambiguation (ED), which links the mentions of ambiguous entities to
their referent entities in a knowledge base, serves as a core component in
entity linking (EL). Existing generative approaches demonstrate improved
accuracy compared to classification approaches under the standardized ZELDA
benchmark. Nevertheless, generative approaches suffer from the need for
large-scale pre-training and inefficient generation. Most importantly, entity
descriptions, which could contain crucial information to distinguish similar
entities from each other, are often overlooked. We propose an encoder-decoder
model to disambiguate entities with more detailed entity descriptions. Given
text and candidate entities, the encoder learns interactions between the text
and each candidate entity, producing representations for each entity candidate.
The decoder then fuses the representations of entity candidates together and
selects the correct entity. Our experiments, conducted on various entity
disambiguation benchmarks, demonstrate the strong and robust performance of
this model, particularly +1.5% in the ZELDA benchmark compared with GENRE.
Furthermore, we integrate this approach into the retrieval/reader framework and
observe +1.5% improvements in end-to-end entity linking in the GERBIL benchmark
compared with EntQA.