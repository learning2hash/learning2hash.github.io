---
layout: publication
title: 'Three-in-one: Robust Enhanced Universal Transferable Anti-facial Retrieval
  In Online Social Networks'
authors: Yunna Lv, Long Tang, Dengpan Ye, Caiyun Xie, Jiacheng Deng, Yiheng He
conference: Arxiv
year: 2024
bibkey: lv2024three
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.09692'}]
tags: ["Image Retrieval", "Neural Hashing", "Privacy & Security", "Robustness"]
short_authors: Lv et al.
---
Deep hash-based retrieval techniques are widely used in facial retrieval
systems to improve the efficiency of facial matching. However, it also carries
the danger of exposing private information. Deep hash models are easily
influenced by adversarial examples, which can be leveraged to protect private
images from malicious retrieval. The existing adversarial example methods
against deep hash models focus on universality and transferability, lacking the
research on its robustness in online social networks (OSNs), which leads to
their failure in anti-retrieval after post-processing. Therefore, we provide
the first in-depth discussion on robustness adversarial perturbation in
universal transferable anti-facial retrieval and propose Three-in-One
Adversarial Perturbation (TOAP). Specifically, we construct a local and global
Compression Generator (CG) to simulate complex post-processing scenarios, which
can be used to mitigate perturbation. Then, we propose robust optimization
objectives based on the discovery of the variation patterns of model's
distribution after post-processing, and generate adversarial examples using
these objectives and meta-learning. Finally, we iteratively optimize
perturbation by alternately generating adversarial examples and fine-tuning the
CG, balancing the performance of perturbation while enhancing CG's ability to
mitigate them. Numerous experiments demonstrate that, in addition to its
advantages in universality and transferability, TOAP significantly outperforms
current state-of-the-art methods in multiple robustness metrics. It further
improves universality and transferability by 5% to 28%, and achieves up to
about 33% significant improvement in several simulated post-processing
scenarios as well as mainstream OSNs, demonstrating that TOAP can effectively
protect private images from malicious retrieval in real-world scenarios.