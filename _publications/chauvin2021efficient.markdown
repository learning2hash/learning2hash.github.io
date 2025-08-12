---
layout: publication
title: Efficient Pairwise Neuroimage Analysis Using The Soft Jaccard Index And 3D
  Keypoint Sets
authors: Laurent Chauvin, Kuldeep Kumar, Christian Desrosiers, William Wells, Matthew
  Toews
conference: IEEE Transactions on Medical Imaging
year: 2021
bibkey: chauvin2021efficient
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.06966'}]
tags: []
short_authors: Chauvin et al.
---
We propose a novel pairwise distance measure between image keypoint sets, for
the purpose of large-scale medical image indexing. Our measure generalizes the
Jaccard index to account for soft set equivalence (SSE) between keypoint
elements, via an adaptive kernel framework modeling uncertainty in keypoint
appearance and geometry. A new kernel is proposed to quantify the variability
of keypoint geometry in location and scale. Our distance measure may be
estimated between \(O(N^2)\) image pairs in \(O(N~log~N)\) operations via keypoint
indexing. Experiments report the first results for the task of predicting
family relationships from medical images, using 1010 T1-weighted MRI brain
volumes of 434 families including monozygotic and dizygotic twins, siblings and
half-siblings sharing 100%-25% of their polymorphic genes. Soft set equivalence
and the keypoint geometry kernel improve upon standard hard set equivalence
(HSE) and appearance kernels alone in predicting family relationships.
Monozygotic twin identification is near 100%, and three subjects with uncertain
genotyping are automatically paired with their self-reported families, the
first reported practical application of image-based family identification. Our
distance measure can also be used to predict group categories, sex is predicted
with an AUC=0.97. Software is provided for efficient fine-grained curation of
large, generic image datasets.