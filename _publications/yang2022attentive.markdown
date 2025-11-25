---
layout: publication
title: Attentive Mask CLIP
authors: Yifan Yang, Weiquan Huang, Yixuan Wei, Houwen Peng, Xinyang Jiang, Huiqiang
  Jiang, Fangyun Wei, Yin Wang, Han Hu, Lili Qiu, Yuqing Yang
conference: Proceedings of the IEEE/CVF International Conference on Computer Vision
  (ICCV) 2023 pp. 2771-2781
year: 2022
bibkey: yang2022attentive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08653'}]
tags: ["Few Shot & Zero Shot", "ICCV", "Self-Supervised"]
short_authors: Yang et al.
---
Image token removal is an efficient augmentation strategy for reducing the
cost of computing image features. However, this efficient augmentation strategy
has been found to adversely affect the accuracy of CLIP-based training. We
hypothesize that removing a large portion of image tokens may improperly
discard the semantic content associated with a given text description, thus
constituting an incorrect pairing target in CLIP training. To address this
issue, we propose an attentive token removal approach for CLIP training, which
retains tokens with a high semantic correlation to the text description. The
correlation scores are computed in an online fashion using the EMA version of
the visual encoder. Our experiments show that the proposed attentive masking
approach performs better than the previous method of random token removal for
CLIP training. The approach also makes it efficient to apply multiple
augmentation views to the image, as well as introducing instance contrastive
learning tasks between these views into the CLIP framework. Compared to other
CLIP improvements that combine different pre-training targets such as SLIP and
MaskCLIP, our method is not only more effective, but also much more efficient.
Specifically, using ViT-B and YFCC-15M dataset, our approach achieves \(43.9%\)
top-1 accuracy on ImageNet-1K zero-shot classification, as well as \(62.7/42.1\)
and \(38.0/23.2\) I2T/T2I retrieval accuracy on Flickr30K and MS COCO, which are
\(+1.1%\), \(+5.5/+0.9\), and \(+4.4/+1.3\) higher than the SLIP method, while being
\(2.30\times\) faster. An efficient version of our approach running \(1.16\times\)
faster than the plain CLIP model achieves significant gains of \(+5.3%\),
\(+11.3/+8.0\), and \(+9.5/+4.9\) on these benchmarks.