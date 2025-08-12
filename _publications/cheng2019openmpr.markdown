---
layout: publication
title: 'Openmpr: Recognize Places Using Multimodal Data For People With Visual Impairments'
authors: Ruiqi Cheng, Kaiwei Wang, Jian Bai, Zhijie Xu
conference: Measurement Science and Technology
year: 2019
bibkey: cheng2019openmpr
citations: 9
additional_links: [{name: Code, url: 'https://github.com/chengricky/OpenMultiPR'},
  {name: Paper, url: 'https://arxiv.org/abs/1909.06795'}]
tags: ["Datasets", "Evaluation"]
short_authors: Cheng et al.
---
Place recognition plays a crucial role in navigational assistance, and is
also a challenging issue of assistive technology. The place recognition is
prone to erroneous localization owing to various changes between database and
query images. Aiming at the wearable assistive device for visually impaired
people, we propose an open-sourced place recognition algorithm OpenMPR, which
utilizes the multimodal data to address the challenging issues of place
recognition. Compared with conventional place recognition, the proposed OpenMPR
not only leverages multiple effective descriptors, but also assigns different
weights to those descriptors in image matching. Incorporating GNSS data into
the algorithm, the cone-based sequence searching is used for robust place
recognition. The experiments illustrate that the proposed algorithm manages to
solve the place recognition issue in the real-world scenarios and surpass the
state-of-the-art algorithms in terms of assistive navigation performance. On
the real-world testing dataset, the online OpenMPR achieves 88.7% precision at
100% recall without illumination changes, and achieves 57.8% precision at 99.3%
recall with illumination changes. The OpenMPR is available at
https://github.com/chengricky/OpenMultiPR.