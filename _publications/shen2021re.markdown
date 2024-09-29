---
layout: publication
title: Re-ranking For Image Retrieval And Transductive Few-shot Classification
authors: Xi Shen, Yang Xiao, Shell Hu, Othman Sbai, Mathieu Aubry
conference: "Neural Information Processing Systems"
year: 2021
bibkey: shen2021re
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/d9fc0cdb67638d50f411432d0d41d0ba-Abstract.html"}
  - {name: "Code", url: "https://imagine.enpc.fr/~shenx/SSR/.""}
tags: ['Graph', 'Has Code', 'Image Retrieval', 'NEURIPS', 'Supervised']
---
In the problems of image retrieval and few-shot classification the mainstream approaches focus on learning a better feature representation. However directly tackling the distance or similarity measure between images could also be efficient. To this end we revisit the idea of re-ranking the top-k retrieved images in the context of image retrieval (e.g. the k-reciprocal nearest neighbors) and generalize this idea to transductive few-shot learning. We propose to meta-learn the re-ranking updates such that the similarity graph converges towards the target similarity graph induced by the image labels. Specifically the re-ranking module takes as input an initial similarity graph between the query image and the contextual images using a pre-trained feature extractor and predicts an improved similarity graph by leveraging the structure among the involved images. We show that our re-ranking approach can be applied to unseen images and can further boost existing approaches for both image retrieval and few-shot learning problems. Our approach operates either independently or in conjunction with classical re-ranking approaches yielding clear and consistent improvements on image retrieval (CUB Cars SOP rOxford5K and rParis6K) and transductive few-shot classification (Mini-ImageNet tiered-ImageNet and CIFAR-FS) benchmarks. Our code is available at https://imagine.enpc.fr/~shenx/SSR/."
