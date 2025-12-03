---
layout: publication
title: 'Irgen: Generative Modeling For Image Retrieval'
authors: Yidan Zhang, Ting Zhang, Dong Chen, Yujing Wang, Qi Chen, Xing Xie, Hao Sun,
  Weiwei Deng, Qi Zhang, Fan Yang, Mao Yang, Qingmin Liao, Jingdong Wang, Baining
  Guo
conference: Arxiv
year: 2023
bibkey: zhang2023irgen
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.10126'}]
tags: ["Datasets", "Hybrid ANN Methods", "Image Retrieval", "Large Scale Search", "Re-Ranking"]
short_authors: Zhang et al.
---
While generative modeling has become prevalent across numerous research
fields, its integration into the realm of image retrieval remains largely
unexplored and underjustified. In this paper, we present a novel methodology,
reframing image retrieval as a variant of generative modeling and employing a
sequence-to-sequence model. This approach is harmoniously aligned with the
current trend towards unification in research, presenting a cohesive framework
that allows for end-to-end differentiable searching. This, in turn, facilitates
superior performance via direct optimization techniques. The development of our
model, dubbed IRGen, addresses the critical technical challenge of converting
an image into a concise sequence of semantic units, which is pivotal for
enabling efficient and effective search. Extensive experiments demonstrate that
our model achieves state-of-the-art performance on three widely-used image
retrieval benchmarks as well as two million-scale datasets, yielding
significant improvement compared to prior competitive retrieval methods. In
addition, the notable surge in precision scores facilitated by generative
modeling presents the potential to bypass the reranking phase, which is
traditionally indispensable in practical retrieval workflows.