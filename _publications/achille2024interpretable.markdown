---
layout: publication
title: Interpretable Measures Of Conceptual Similarity By Complexity-constrained Descriptive
  Auto-encoding
authors: Alessandro Achille, Greg Ver Steeg, Tian Yu Liu, Matthew Trager, Carson Klingenberg,
  Stefano Soatto
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: achille2024interpretable
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.08919'}]
tags: ["CVPR"]
short_authors: Achille et al.
---
Quantifying the degree of similarity between images is a key copyright issue
for image-based machine learning. In legal doctrine however, determining the
degree of similarity between works requires subjective analysis, and
fact-finders (judges and juries) can demonstrate considerable variability in
these subjective judgement calls. Images that are structurally similar can be
deemed dissimilar, whereas images of completely different scenes can be deemed
similar enough to support a claim of copying. We seek to define and compute a
notion of "conceptual similarity" among images that captures high-level
relations even among images that do not share repeated elements or visually
similar components. The idea is to use a base multi-modal model to generate
"explanations" (captions) of visual data at increasing levels of complexity.
Then, similarity can be measured by the length of the caption needed to
discriminate between the two images: Two highly dissimilar images can be
discriminated early in their description, whereas conceptually dissimilar ones
will need more detail to be distinguished. We operationalize this definition
and show that it correlates with subjective (averaged human evaluation)
assessment, and beats existing baselines on both image-to-image and
text-to-text similarity benchmarks. Beyond just providing a number, our method
also offers interpretability by pointing to the specific level of granularity
of the description where the source data are differentiated.