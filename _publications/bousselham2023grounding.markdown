---
layout: publication
title: 'Grounding Everything: Emerging Localization Properties In Vision-language
  Transformers'
authors: Walid Bousselham, Felix Petersen, Vittorio Ferrari, Hilde Kuehne
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: bousselham2023grounding
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.00878'}]
tags: ["CVPR"]
short_authors: Bousselham et al.
---
Vision-language foundation models have shown remarkable performance in
various zero-shot settings such as image retrieval, classification, or
captioning. But so far, those models seem to fall behind when it comes to
zero-shot localization of referential expressions and objects in images. As a
result, they need to be fine-tuned for this task. In this paper, we show that
pretrained vision-language (VL) models allow for zero-shot open-vocabulary
object localization without any fine-tuning. To leverage those capabilities, we
propose a Grounding Everything Module (GEM) that generalizes the idea of
value-value attention introduced by CLIPSurgery to a self-self attention path.
We show that the concept of self-self attention corresponds to clustering, thus
enforcing groups of tokens arising from the same object to be similar while
preserving the alignment with the language space. To further guide the group
formation, we propose a set of regularizations that allows the model to finally
generalize across datasets and backbones. We evaluate the proposed GEM
framework on various benchmark tasks and datasets for semantic segmentation. It
shows that GEM not only outperforms other training-free open-vocabulary
localization methods, but also achieves state-of-the-art results on the
recently proposed OpenImagesV7 large-scale segmentation benchmark.