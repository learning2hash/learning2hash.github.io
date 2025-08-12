---
layout: publication
title: 'Wast-3d: Wasserstein-2 Distance For Scene-to-scene Stylization On 3D Gaussians'
authors: "Dmytro Kotovenko, Olga Grebenkova, Nikolaos Sarafianos, Avinash Paliwal,\
  \ Pingchuan Ma, Omid Poursaeed, Sreyas Mohan, Yuchen Fan, Yilei Li, Rakesh Ranjan,\
  \ Bj\xF6rn Ommer"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: kotovenko2024wast
citations: 1
additional_links: [{name: Code, url: 'https://compvis.github.io/wast3d/\}\{https://compvis.github.io/wast3d/\}\)'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.17917'}]
tags: []
short_authors: Kotovenko et al.
---
While style transfer techniques have been well-developed for 2D image
stylization, the extension of these methods to 3D scenes remains relatively
unexplored. Existing approaches demonstrate proficiency in transferring colors
and textures but often struggle with replicating the geometry of the scenes. In
our work, we leverage an explicit Gaussian Splatting (GS) representation and
directly match the distributions of Gaussians between style and content scenes
using the Earth Mover's Distance (EMD). By employing the entropy-regularized
Wasserstein-2 distance, we ensure that the transformation maintains spatial
smoothness. Additionally, we decompose the scene stylization problem into
smaller chunks to enhance efficiency. This paradigm shift reframes stylization
from a pure generative process driven by latent space losses to an explicit
matching of distributions between two Gaussian representations. Our method
achieves high-resolution 3D stylization by faithfully transferring details from
3D style scenes onto the content scene. Furthermore, WaSt-3D consistently
delivers results across diverse content and style scenes without necessitating
any training, as it relies solely on optimization-based techniques. See our
project page for additional results and source code:
\(\href\{https://compvis.github.io/wast3d/\}\{https://compvis.github.io/wast3d/\}\).