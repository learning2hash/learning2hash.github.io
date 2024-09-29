---
layout: publication
title: Re45;ranking For Image Retrieval And Transductive Few45;shot Classification
authors: Xi Shen, Yang Xiao, Shell Hu, Othman Sbai, Mathieu Aubry
conference: "Neural Information Processing Systems"
year: 2021
bibkey: shen2021image
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/d9fc0cdb67638d50f411432d0d41d0ba-Abstract.html"}
  - {name: "Code", url: "https://imagine.enpc.fr/~shenx/SSR/"}
tags: ['Graph', 'Has Code', 'Image Retrieval', 'NEURIPS', 'Supervised']
---
In the problems of image retrieval and few45;shot classification the mainstream approaches focus on learning a better feature representation. However directly tackling the distance or similarity measure between images could also be efficient. To this end we revisit the idea of re45;ranking the top45;k retrieved images in the context of image retrieval (e.g. the k45;reciprocal nearest neighbors) and generalize this idea to transductive few45;shot learning. We propose to meta45;learn the re45;ranking updates such that the similarity graph converges towards the target similarity graph induced by the image labels. Specifically the re45;ranking module takes as input an initial similarity graph between the query image and the contextual images using a pre45;trained feature extractor and predicts an improved similarity graph by leveraging the structure among the involved images. We show that our re45;ranking approach can be applied to unseen images and can further boost existing approaches for both image retrieval and few45;shot learning problems. Our approach operates either independently or in conjunction with classical re45;ranking approaches yielding clear and consistent improvements on image retrieval (CUB Cars SOP rOxford5K and rParis6K) and transductive few45;shot classification (Mini45;ImageNet tiered45;ImageNet and CIFAR45;FS) benchmarks. Our code is available at https://imagine.enpc.fr/~shenx/SSR/.
