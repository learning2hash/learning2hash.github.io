---
layout: publication
title: 'Levit: A Vision Transformer In Convnet''s Clothing For Faster Inference'
authors: "Ben Graham, Alaaeldin El-Nouby, Hugo Touvron, Pierre Stock, Armand Joulin,\
  \ Herv\xE9 J\xE9gou, Matthijs Douze"
conference: Arxiv
year: 2021
bibkey: graham2021levit
citations: 53
additional_links: [{name: Code, url: 'https://github.com/facebookresearch/LeViT'},
  {name: Paper, url: 'https://arxiv.org/abs/2104.01136'}]
tags: ["Efficiency"]
short_authors: Graham et al.
---
We design a family of image classification architectures that optimize the
trade-off between accuracy and efficiency in a high-speed regime. Our work
exploits recent findings in attention-based architectures, which are
competitive on highly parallel processing hardware. We revisit principles from
the extensive literature on convolutional neural networks to apply them to
transformers, in particular activation maps with decreasing resolutions. We
also introduce the attention bias, a new way to integrate positional
information in vision transformers. As a result, we propose LeVIT: a hybrid
neural network for fast inference image classification. We consider different
measures of efficiency on different hardware platforms, so as to best reflect a
wide range of application scenarios. Our extensive experiments empirically
validate our technical choices and show they are suitable to most
architectures. Overall, LeViT significantly outperforms existing convnets and
vision transformers with respect to the speed/accuracy tradeoff. For example,
at 80% ImageNet top-1 accuracy, LeViT is 5 times faster than EfficientNet on
CPU. We release the code at https://github.com/facebookresearch/LeViT