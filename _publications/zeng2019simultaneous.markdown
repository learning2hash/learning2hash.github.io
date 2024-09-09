---
    layout: publication
    title: "Simultaneous Region Localization and Hash Coding for Fine-grained Image Retrieval"
    authors: Zeng Haien, Lai Hanjiang, Yin Jian
    conference: Arxiv
    year: 2019
    bibkey: zeng2019simultaneous
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1911.08028"}
    tags: ['ARXIV', 'Image Retrieval']
    ---
    Fine-grained image hashing is a challenging problem due to the difficulties of discriminative region localization and hash code generation. Most existing deep hashing approaches solve the two tasks independently. While these two tasks are correlated and can reinforce each other. In this paper, we propose a deep fine-grained hashing to simultaneously localize the discriminative regions and generate the efficient binary codes. The proposed approach consists of a region localization module and a hash coding module. The region localization module aims to provide informative regions to the hash coding module. The hash coding module aims to generate effective binary codes and give feedback for learning better localizer. Moreover, to better capture subtle differences, multi-scale regions at different layers are learned without the need of bounding-box/part annotations. Extensive experiments are conducted on two public benchmark fine-grained datasets. The results demonstrate significant improvements in the performance of our method relative to other fine-grained hashing algorithms.