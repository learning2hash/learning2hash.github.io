---
layout: publication
title: 'Quantart: Quantizing Image Style Transfer Towards High Visual Fidelity'
authors: Siyu Huang, Jie An, Donglai Wei, Jiebo Luo, Hanspeter Pfister
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: huang2022quantart
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.10431'}]
tags: ["CVPR", "Quantization"]
short_authors: Huang et al.
---
The mechanism of existing style transfer algorithms is by minimizing a hybrid
loss function to push the generated image toward high similarities in both
content and style. However, this type of approach cannot guarantee visual
fidelity, i.e., the generated artworks should be indistinguishable from real
ones. In this paper, we devise a new style transfer framework called QuantArt
for high visual-fidelity stylization. QuantArt pushes the latent representation
of the generated artwork toward the centroids of the real artwork distribution
with vector quantization. By fusing the quantized and continuous latent
representations, QuantArt allows flexible control over the generated artworks
in terms of content preservation, style similarity, and visual fidelity.
Experiments on various style transfer settings show that our QuantArt framework
achieves significantly higher visual fidelity compared with the existing style
transfer methods.