---
layout: publication
title: 'GPR1200: A Benchmark For General-purpose Content-based Image Retrieval'
authors: Konstantin Schall, Kai Uwe Barthel, Nico Hezel, Klaus Jung
conference: Arxiv
year: 2021
bibkey: schall2021gpr1200
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.13122'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Schall et al.
---
Even though it has extensively been shown that retrieval specific training of
deep neural networks is beneficial for nearest neighbor image search quality,
most of these models are trained and tested in the domain of landmarks images.
However, some applications use images from various other domains and therefore
need a network with good generalization properties - a general-purpose CBIR
model. To the best of our knowledge, no testing protocol has so far been
introduced to benchmark models with respect to general image retrieval quality.
After analyzing popular image retrieval test sets we decided to manually curate
GPR1200, an easy to use and accessible but challenging benchmark dataset with a
broad range of image categories. This benchmark is subsequently used to
evaluate various pretrained models of different architectures on their
generalization qualities. We show that large-scale pretraining significantly
improves retrieval performance and present experiments on how to further
increase these properties by appropriate fine-tuning. With these promising
results, we hope to increase interest in the research topic of general-purpose
CBIR.