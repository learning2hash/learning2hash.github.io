---
layout: publication
title: Dual Relation Alignment For Composed Image Retrieval
authors: Xintong Jiang, Yaxiong Wang, Yujiao Wu, Meng Wang, Xueming Qian
conference: Arxiv
year: 2023
bibkey: jiang2023dual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.02169'}]
tags: [Datasets, Image Retrieval, Text Retrieval, Tools & Libraries, Evaluation]
short_authors: Jiang et al.
---
Composed image retrieval, a task involving the search for a target image
using a reference image and a complementary text as the query, has witnessed
significant advancements owing to the progress made in cross-modal modeling.
Unlike the general image-text retrieval problem with only one alignment
relation, i.e., image-text, we argue for the existence of two types of
relations in composed image retrieval. The explicit relation pertains to the
reference image & complementary text-target image, which is commonly exploited
by existing methods. Besides this intuitive relation, the observations during
our practice have uncovered another implicit yet crucial relation, i.e.,
reference image & target image-complementary text, since we found that the
complementary text can be inferred by studying the relation between the target
image and the reference image. Regrettably, existing methods largely focus on
leveraging the explicit relation to learn their networks, while overlooking the
implicit relation. In response to this weakness, We propose a new framework for
composed image retrieval, termed dual relation alignment, which integrates both
explicit and implicit relations to fully exploit the correlations among the
triplets. Specifically, we design a vision compositor to fuse reference image
and target image at first, then the resulted representation will serve two
roles: (1) counterpart for semantic alignment with the complementary text and
(2) compensation for the complementary text to boost the explicit relation
modeling, thereby implant the implicit relation into the alignment learning.
Our method is evaluated on two popular datasets, CIRR and FashionIQ, through
extensive experiments. The results confirm the effectiveness of our
dual-relation learning in substantially enhancing composed image retrieval
performance.