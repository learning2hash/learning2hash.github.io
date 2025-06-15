---
layout: publication
title: 'Object-centric Open-vocabulary Image-retrieval With Aggregated Features'
authors: Hila Levi, Guy Heller, Dan Levi, Ethan Fetaya
conference: "Arxiv"
year: 2023
citations: 0
bibkey: levi2023object
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2309.14999'}
tags: ['Tools and Libraries', 'Evaluation Metrics', 'Applications']
---
The task of open-vocabulary object-centric image retrieval involves the
retrieval of images containing a specified object of interest, delineated by an
open-set text query. As working on large image datasets becomes standard,
solving this task efficiently has gained significant practical importance.
Applications include targeted performance analysis of retrieved images using
ad-hoc queries and hard example mining during training. Recent advancements in
contrastive-based open vocabulary systems have yielded remarkable
breakthroughs, facilitating large-scale open vocabulary image retrieval.
However, these approaches use a single global embedding per image, thereby
constraining the system's ability to retrieve images containing relatively
small object instances. Alternatively, incorporating local embeddings from
detection pipelines faces scalability challenges, making it unsuitable for
retrieval from large databases.
  In this work, we present a simple yet effective approach to object-centric
open-vocabulary image retrieval. Our approach aggregates dense embeddings
extracted from CLIP into a compact representation, essentially combining the
scalability of image retrieval pipelines with the object identification
capabilities of dense detection methods. We show the effectiveness of our
scheme to the task by achieving significantly better results than global
feature approaches on three datasets, increasing accuracy by up to 15 mAP
points. We further integrate our scheme into a large scale retrieval framework
and demonstrate our method's advantages in terms of scalability and
interpretability.
