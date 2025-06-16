---
layout: publication
title: 'Property-preserving Hashing For \(\ell_1\)-distance Predicates: Applications
  To Countering Adversarial Input Attacks'
authors: Hassan Asghar, Chenhan Zhang, Dali Kaafar
conference: Arxiv
year: 2025
citations: 0
bibkey: asghar2025property
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.16355'}]
tags: [Hashing Methods, Applications, Evaluation Metrics]
---
Perceptual hashing is used to detect whether an input image is similar to a
reference image with a variety of security applications. Recently, they have
been shown to succumb to adversarial input attacks which make small
imperceptible changes to the input image yet the hashing algorithm does not
detect its similarity to the original image. Property-preserving hashing (PPH)
is a recent construct in cryptography, which preserves some property
(predicate) of its inputs in the hash domain. Researchers have so far shown
constructions of PPH for Hamming distance predicates, which, for instance,
outputs 1 if two inputs are within Hamming distance \\(t\\). A key feature of PPH
is its strong correctness guarantee, i.e., the probability that the predicate
will not be correctly evaluated in the hash domain is negligible. Motivated by
the use case of detecting similar images under adversarial setting, we propose
the first PPH construction for an \\(\ell_1\\)-distance predicate. Roughly, this
predicate checks if the two one-sided \\(\ell_1\\)-distances between two images are
within a threshold \\(t\\). Since many adversarial attacks use \\(ℓ₂\\)-distance
(related to \\(\ell_1\\)-distance) as the objective function to perturb the input
image, by appropriately choosing the threshold \\(t\\), we can force the attacker
to add considerable noise to evade detection, and hence significantly
deteriorate the image quality. Our proposed scheme is highly efficient, and
runs in time \\(O(t^2)\\). For grayscale images of size \\(28 \times 28\\), we can
evaluate the predicate in \\(0.0784\\) seconds when pixel values are perturbed by
up to \\(1 %\\). For larger RGB images of size \\(224 \times 224\\), by dividing the
image into 1,000 blocks, we achieve times of \\(0.0128\\) seconds per block for \\(1
%\\) change, and up to \\(0.2641\\) seconds per block for \\(14%\\) change.