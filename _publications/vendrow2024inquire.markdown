---
layout: publication
title: 'INQUIRE: A Natural World Text-to-image Retrieval Benchmark'
authors: Edward Vendrow, Omiros Pantazis, Alexander Shepard, Gabriel Brostow, Kate
  E. Jones, Oisin Mac Aodha, Sara Beery, Grant van Horn
conference: Advances in Neural Information Processing Systems 37
year: 2024
bibkey: vendrow2024inquire
citations: 0
additional_links: [{name: Code, url: 'https://inquire-benchmark.github.io'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.02537'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval", "Re-Ranking"]
short_authors: Vendrow et al.
---
We introduce INQUIRE, a text-to-image retrieval benchmark designed to
challenge multimodal vision-language models on expert-level queries. INQUIRE
includes iNaturalist 2024 (iNat24), a new dataset of five million natural world
images, along with 250 expert-level retrieval queries. These queries are paired
with all relevant images comprehensively labeled within iNat24, comprising
33,000 total matches. Queries span categories such as species identification,
context, behavior, and appearance, emphasizing tasks that require nuanced image
understanding and domain expertise. Our benchmark evaluates two core retrieval
tasks: (1) INQUIRE-Fullrank, a full dataset ranking task, and (2)
INQUIRE-Rerank, a reranking task for refining top-100 retrievals. Detailed
evaluation of a range of recent multimodal models demonstrates that INQUIRE
poses a significant challenge, with the best models failing to achieve an
mAP@50 above 50%. In addition, we show that reranking with more powerful
multimodal models can enhance retrieval performance, yet there remains a
significant margin for improvement. By focusing on scientifically-motivated
ecological challenges, INQUIRE aims to bridge the gap between AI capabilities
and the needs of real-world scientific inquiry, encouraging the development of
retrieval systems that can assist with accelerating ecological and biodiversity
research. Our dataset and code are available at
https://inquire-benchmark.github.io