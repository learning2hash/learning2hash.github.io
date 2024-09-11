---
layout: publication
title: "Progressive Generative Hashing for Image Retrieval"
authors: Yuqing Ma, Yue He, Fan Ding, Sheng Hu, Jun Li, Xianglong Liu
conference: IJCAI
year: 2018
bibkey: ma2018progressive
additional_links:
   - {name: "PDF", url: "https://www.ijcai.org/proceedings/2018/0121.pdf"}
tags: ["Deep Learning", "IJCAI", "Image Retrieval", "GAN", "Unsupervised"]
---
Recent years have witnessed the success of the emerging hashing techniques in large-scale image
retrieval. Owing to the great learning capacity,
deep hashing has become one of the most promising solutions, and achieved attractive performance
in practice. However, without semantic label information, the unsupervised deep hashing still remains
an open question. In this paper, we propose a novel
progressive generative hashing (PGH) framework
to help learn a discriminative hashing network in an
unsupervised way. Different from existing studies,
it first treats the hash codes as a kind of semantic
condition for the similar image generation, and simultaneously feeds the original image and its codes
into the generative adversarial networks (GANs).
The real images together with the synthetic ones
can further help train a discriminative hashing network based on a triplet loss. By iteratively inputting
the learnt codes into the hash conditioned GANs, we can progressively enable the hashing network
to discover the semantic relations. Extensive experiments on the widely-used image datasets demonstrate that PGH can significantly outperform stateof-the-art unsupervised hashing methods.
