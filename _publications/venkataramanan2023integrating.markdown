---
layout: publication
title: Integrating Visual And Semantic Similarity Using Hierarchies For Image Retrieval
authors: "Aishwarya Venkataramanan, Martin Laviale, C\xE9dric Pradalier"
conference: Lecture Notes in Computer Science
year: 2023
bibkey: venkataramanan2023integrating
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.08431'}]
tags: ["Datasets", "Image Retrieval", "Similarity Search"]
short_authors: "Aishwarya Venkataramanan, Martin Laviale, C\xE9dric Pradalier"
---
Most of the research in content-based image retrieval (CBIR) focus on
developing robust feature representations that can effectively retrieve
instances from a database of images that are visually similar to a query.
However, the retrieved images sometimes contain results that are not
semantically related to the query. To address this, we propose a method for
CBIR that captures both visual and semantic similarity using a visual
hierarchy. The hierarchy is constructed by merging classes with overlapping
features in the latent space of a deep neural network trained for
classification, assuming that overlapping classes share high visual and
semantic similarities. Finally, the constructed hierarchy is integrated into
the distance calculation metric for similarity search. Experiments on standard
datasets: CUB-200-2011 and CIFAR100, and a real-life use case using diatom
microscopy images show that our method achieves superior performance compared
to the existing methods on image retrieval.