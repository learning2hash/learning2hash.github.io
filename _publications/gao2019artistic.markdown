---
layout: publication
title: Artistic Glyph Image Synthesis Via One-stage Few-shot Learning
authors: Yue Gao, Yuan Guo, Zhouhui Lian, Yingmin Tang, Jianguo Xiao
conference: ACM Transactions on Graphics
year: 2019
bibkey: gao2019artistic
citations: 84
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.04987'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Gao et al.
---
Automatic generation of artistic glyph images is a challenging task that
attracts many research interests. Previous methods either are specifically
designed for shape synthesis or focus on texture transfer. In this paper, we
propose a novel model, AGIS-Net, to transfer both shape and texture styles in
one-stage with only a few stylized samples. To achieve this goal, we first
disentangle the representations for content and style by using two encoders,
ensuring the multi-content and multi-style generation. Then we utilize two
collaboratively working decoders to generate the glyph shape image and its
texture image simultaneously. In addition, we introduce a local texture
refinement loss to further improve the quality of the synthesized textures. In
this manner, our one-stage model is much more efficient and effective than
other multi-stage stacked methods. We also propose a large-scale dataset with
Chinese glyph images in various shape and texture styles, rendered from 35
professional-designed artistic fonts with 7,326 characters and 2,460 synthetic
artistic fonts with 639 characters, to validate the effectiveness and
extendability of our method. Extensive experiments on both English and Chinese
artistic glyph image datasets demonstrate the superiority of our model in
generating high-quality stylized glyph images against other state-of-the-art
methods.