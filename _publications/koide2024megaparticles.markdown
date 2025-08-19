---
layout: publication
title: 'Megaparticles: Range-based 6-dof Monte Carlo Localization With Gpu-accelerated
  Stein Particle Filter'
authors: Kenji Koide, Shuji Oishi, Masashi Yokozuka, Atsuhiko Banno
conference: 2024 IEEE International Conference on Robotics and Automation (ICRA)
year: 2024
bibkey: koide2024megaparticles
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.16370'}]
tags: [Efficiency, ICRA, Hashing Methods, Locality Sensitive Hashing, Robustness]
short_authors: Koide et al.
---
This paper presents a 6-DoF range-based Monte Carlo localization method with
a GPU-accelerated Stein particle filter. To update a massive amount of
particles, we propose a Gauss-Newton-based Stein variational gradient descent
(SVGD) with iterative neighbor particle search. This method uses SVGD to
collectively update particle states with gradient and neighborhood information,
which provides efficient particle sampling. For an efficient neighbor particle
search, it uses locality sensitive hashing and iteratively updates the neighbor
list of each particle over time. The neighbor list is then used to propagate
the posterior probabilities of particles over the neighbor particle graph. The
proposed method is capable of evaluating one million particles in real-time on
a single GPU and enables robust pose initialization and re-localization without
an initial pose estimate. In experiments, the proposed method showed an extreme
robustness to complete sensor occlusion (i.e., kidnapping), and enabled
pinpoint sensor localization without any prior information.