---
layout: publication
title: 'CRD: Collaborative Representation Distance For Practical Anomaly Detection'
authors: Chao Han, Yudong Yan
conference: Arxiv
year: 2024
bibkey: han2024crd
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.09443'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Chao Han, Yudong Yan
---
Visual defect detection plays an important role in intelligent industry.
Patch based methods consider visual images as a collection of image patches
according to positions, which have stronger discriminative ability for small
defects in products, e.g. scratches on pills. However, the nearest neighbor
search for the query image and the stored patches will occupy \\(O(n)\\) complexity
in terms of time and space requirements, posing strict challenges for
deployment in edge environments. In this paper, we propose an alternative
approach to the distance calculation of image patches via collaborative
representation models. Starting from the nearest neighbor distance with \\(L_0\\)
constraint, we relax the constraint to \\(L_2\\) constraint and solve the distance
quickly in close-formed without actually accessing the original stored
collection of image patches. Furthermore, we point out that the main
computational burden of this close-formed solution can be pre-computed by
high-performance server before deployment. Consequently, the distance
calculation on edge devices only requires a simple matrix multiplication, which
is extremely lightweight and GPU-friendly. Performance on real industrial
scenarios demonstrates that compared to the existing state-of-the-art methods,
this distance achieves several hundred times improvement in computational
efficiency with slight performance drop, while greatly reducing memory
overhead.