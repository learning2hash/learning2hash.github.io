---
layout: publication
title: Text-to-image Generation Via Energy-based CLIP
authors: Roy Ganz, Michael Elad
conference: Arxiv
year: 2024
bibkey: ganz2024text
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.17046'}]
tags: ["Distance Metric Learning", "Evaluation", "Robustness"]
short_authors: Roy Ganz, Michael Elad
---
Joint Energy Models (JEMs), while drawing significant research attention,
have not been successfully scaled to real-world, high-resolution datasets. We
present EB-CLIP, a novel approach extending JEMs to the multimodal
vision-language domain using CLIP, integrating both generative and
discriminative objectives. For the generative objective, we introduce an
image-text joint-energy function based on Cosine similarity in the CLIP space,
training CLIP to assign low energy to real image-caption pairs and high energy
otherwise. For the discriminative objective, we employ contrastive adversarial
loss, extending the adversarial training objective to the multimodal domain.
EB-CLIP not only generates realistic images from text but also achieves
competitive results on the compositionality benchmark, outperforming leading
methods with fewer parameters. Additionally, we demonstrate the superior
guidance capability of EB-CLIP by enhancing CLIP-based generative frameworks
and converting unconditional diffusion models to text-based ones. Lastly, we
show that EB-CLIP can serve as a more robust evaluation metric for
text-to-image generative tasks than CLIP.