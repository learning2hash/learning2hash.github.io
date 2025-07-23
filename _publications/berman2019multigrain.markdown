---
layout: publication
title: 'Multigrain: A Unified Image Embedding For Classes And Instances'
authors: "Berman Maxim, J\xE9gou Herv\xE9, Vedaldi Andrea, Kokkinos Iasonas, Douze\
  \ Matthijs"
conference: Arxiv
year: 2019
bibkey: berman2019multigrain
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.05509'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Neural Hashing", "Similarity Search"]
short_authors: Berman et al.
---
MultiGrain is a network architecture producing compact vector representations
that are suited both for image classification and particular object retrieval.
It builds on a standard classification trunk. The top of the network produces
an embedding containing coarse and fine-grained information, so that images can
be recognized based on the object class, particular object, or if they are
distorted copies. Our joint training is simple: we minimize a cross-entropy
loss for classification and a ranking loss that determines if two images are
identical up to data augmentation, with no need for additional labels. A key
component of MultiGrain is a pooling layer that takes advantage of
high-resolution images with a network trained at a lower resolution.
  When fed to a linear classifier, the learned embeddings provide
state-of-the-art classification accuracy. For instance, we obtain 79.4% top-1
accuracy with a ResNet-50 learned on Imagenet, which is a +1.8% absolute
improvement over the AutoAugment method. When compared with the cosine
similarity, the same embeddings perform on par with the state-of-the-art for
image retrieval at moderate resolutions.