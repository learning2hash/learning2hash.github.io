---
layout: publication
title: Visualizing And Improving Scattering Networks
authors: Fergal Cotter, Nick Kingsbury
conference: 2017 IEEE 27th International Workshop on Machine Learning for Signal Processing
  (MLSP)
year: 2017
bibkey: cotter2017visualizing
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.01355'}]
tags: ["Evaluation"]
short_authors: Fergal Cotter, Nick Kingsbury
---
Scattering Transforms (or ScatterNets) introduced by Mallat are a promising
start into creating a well-defined feature extractor to use for pattern
recognition and image classification tasks. They are of particular interest due
to their architectural similarity to Convolutional Neural Networks (CNNs),
while requiring no parameter learning and still performing very well
(particularly in constrained classification tasks).
  In this paper we visualize what the deeper layers of a ScatterNet are
sensitive to using a 'DeScatterNet'. We show that the higher orders of
ScatterNets are sensitive to complex, edge-like patterns (checker-boards and
rippled edges). These complex patterns may be useful for texture
classification, but are quite dissimilar from the patterns visualized in second
and third layers of Convolutional Neural Networks (CNNs) - the current state of
the art Image Classifiers. We propose that this may be the source of the
current gaps in performance between ScatterNets and CNNs (83% vs 93% on
CIFAR-10 for ScatterNet+SVM vs ResNet). We then use these visualization tools
to propose possible enhancements to the ScatterNet design, which show they have
the power to extract features more closely resembling CNNs, while still being
well-defined and having the invariance properties fundamental to ScatterNets.