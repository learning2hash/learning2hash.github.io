---
layout: publication
title: Learning To Generate Semantic Layouts For Higher Text-image Correspondence
  In Text-to-image Synthesis
authors: Minho Park, Jooyeol Yun, Seunghwan Choi, Jaegul Choo
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: park2023learning
citations: 7
additional_links: [{name: Code, url: 'https://pmh9960.github.io/research/GCDP'}, {
    name: Paper, url: 'https://arxiv.org/abs/2308.08157'}]
tags: ["ICCV"]
short_authors: Park et al.
---
Existing text-to-image generation approaches have set high standards for
photorealism and text-image correspondence, largely benefiting from web-scale
text-image datasets, which can include up to 5~billion pairs. However,
text-to-image generation models trained on domain-specific datasets, such as
urban scenes, medical images, and faces, still suffer from low text-image
correspondence due to the lack of text-image pairs. Additionally, collecting
billions of text-image pairs for a specific domain can be time-consuming and
costly. Thus, ensuring high text-image correspondence without relying on
web-scale text-image datasets remains a challenging task. In this paper, we
present a novel approach for enhancing text-image correspondence by leveraging
available semantic layouts. Specifically, we propose a Gaussian-categorical
diffusion process that simultaneously generates both images and corresponding
layout pairs. Our experiments reveal that we can guide text-to-image generation
models to be aware of the semantics of different image regions, by training the
model to generate semantic labels for each pixel. We demonstrate that our
approach achieves higher text-image correspondence compared to existing
text-to-image generation approaches in the Multi-Modal CelebA-HQ and the
Cityscapes dataset, where text-image pairs are scarce. Codes are available in
this https://pmh9960.github.io/research/GCDP