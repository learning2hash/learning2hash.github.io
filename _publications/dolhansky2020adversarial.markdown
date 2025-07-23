---
layout: publication
title: Adversarial Collision Attacks On Image Hashing Functions
authors: Dolhansky Brian, Ferrer Cristian Canton
conference: Arxiv
year: 2020
bibkey: dolhansky2020adversarial
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.09473'}]
tags: ["Hashing Methods", "Image Retrieval", "Privacy & Security", "Robustness"]
short_authors: Dolhansky Brian, Ferrer Cristian Canton
---
Hashing images with a perceptual algorithm is a common approach to solving
duplicate image detection problems. However, perceptual image hashing
algorithms are differentiable, and are thus vulnerable to gradient-based
adversarial attacks. We demonstrate that not only is it possible to modify an
image to produce an unrelated hash, but an exact image hash collision between a
source and target image can be produced via minuscule adversarial
perturbations. In a white box setting, these collisions can be replicated
across nearly every image pair and hash type (including both deep and
non-learned hashes). Furthermore, by attacking points other than the output of
a hashing function, an attacker can avoid having to know the details of a
particular algorithm, resulting in collisions that transfer across different
hash sizes or model architectures. Using these techniques, an adversary can
poison the image lookup table of a duplicate image detection service, resulting
in undefined or unwanted behavior. Finally, we offer several potential
mitigations to gradient-based image hash attacks.