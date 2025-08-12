---
layout: publication
title: 'OBELICS: An Open Web-scale Filtered Dataset Of Interleaved Image-text Documents'
authors: "Hugo Lauren\xE7on, Lucile Saulnier, L\xE9o Tronchon, Stas Bekman, Amanpreet\
  \ Singh, Anton Lozhkov, Thomas Wang, Siddharth Karamcheti, Alexander M. Rush, Douwe\
  \ Kiela, Matthieu Cord, Victor Sanh"
conference: Arxiv
year: 2023
bibkey: "lauren\xE7on2023obelics"
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.16527'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: "Lauren\xE7on et al."
---
Large multimodal models trained on natural documents, which interleave images
and text, outperform models trained on image-text pairs on various multimodal
benchmarks. However, the datasets used to train these models have not been
released, and the collection process has not been fully specified. We introduce
the OBELICS dataset, an open web-scale filtered dataset of interleaved
image-text documents comprising 141 million web pages extracted from Common
Crawl, 353 million associated images, and 115 billion text tokens. We describe
the dataset creation process, present comprehensive filtering rules, and
provide an analysis of the dataset's content. To show the viability of OBELICS,
we train vision and language models of 9 and 80 billion parameters named
IDEFICS, and obtain competitive performance on different multimodal benchmarks.
We release our dataset, models and code.