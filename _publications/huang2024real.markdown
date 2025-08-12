---
layout: publication
title: Real-time Level-of-detail Strand-based Hair Rendering
authors: Tao Huang, Yang Zhou, Daqi Lin, Junqiu Zhu, Ling-Qi Yan, Kui Wu
conference: Arxiv
year: 2024
bibkey: huang2024real
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.10565'}]
tags: ["Efficiency"]
short_authors: Huang et al.
---
Strand-based hair rendering has become increasingly popular in production for
its realistic appearance. However, the prevailing level-of-detail solution
employing hair cards for distant hair models introduces a significant
discontinuity in dynamics and appearance during the transition from strands to
cards. We introduce an innovative real-time framework for strand-based hair
rendering that ensures seamless transitions between different levels of detail
(LOD) while maintaining a consistent hair appearance. Our method uses
elliptical thick hairs that contain multiple hair strands at each LOD to
maintain the shapes of hair clusters. In addition to geometric fitting, we
formulate an elliptical Bidirectional Curve Scattering Distribution Functions
(BCSDF) model for a thick hair, accurately capturing single scattering and
multiple scattering within the hair cluster, accommodating a spectrum from
sparse to dense hair distributions. Our framework, tested on various hairstyles
with dynamics as well as knits, shows that it can produce highly similar
appearances to full hair geometries at different viewing distances with
seamless LOD transitions, while achieving up to a 3x speedup.