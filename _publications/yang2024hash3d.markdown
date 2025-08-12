---
layout: publication
title: 'Hash3d: Training-free Acceleration For 3D Generation'
authors: Xingyi Yang, Xinchao Wang
conference: Arxiv
year: 2024
bibkey: yang2024hash3d
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.06091'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Xingyi Yang, Xinchao Wang
---
The evolution of 3D generative modeling has been notably propelled by the
adoption of 2D diffusion models. Despite this progress, the cumbersome
optimization process per se presents a critical hurdle to efficiency. In this
paper, we introduce Hash3D, a universal acceleration for 3D generation without
model training. Central to Hash3D is the insight that feature-map redundancy is
prevalent in images rendered from camera positions and diffusion time-steps in
close proximity. By effectively hashing and reusing these feature maps across
neighboring timesteps and camera angles, Hash3D substantially prevents
redundant calculations, thus accelerating the diffusion model's inference in 3D
generation tasks. We achieve this through an adaptive grid-based hashing.
Surprisingly, this feature-sharing mechanism not only speed up the generation
but also enhances the smoothness and view consistency of the synthesized 3D
objects. Our experiments covering 5 text-to-3D and 3 image-to-3D models,
demonstrate Hash3D's versatility to speed up optimization, enhancing efficiency
by 1.3 to 4 times. Additionally, Hash3D's integration with 3D Gaussian
splatting largely speeds up 3D model creation, reducing text-to-3D processing
to about 10 minutes and image-to-3D conversion to roughly 30 seconds. The
project page is at https://adamdad.github.io/hash3D/.