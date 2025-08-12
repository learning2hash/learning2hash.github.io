---
layout: publication
title: Unsupervised Representation Learning By Discovering Reliable Image Relations
authors: "Timo Milbich, Omair Ghori, Ferran Diego, Bj\xF6rn Ommer"
conference: Pattern Recognition
year: 2020
bibkey: milbich2019unsupervised
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07808'}]
tags: ["Unsupervised"]
short_authors: Milbich et al.
---
Learning robust representations that allow to reliably establish relations
between images is of paramount importance for virtually all of computer vision.
Annotating the quadratic number of pairwise relations between training images
is simply not feasible, while unsupervised inference is prone to noise, thus
leaving the vast majority of these relations to be unreliable. To nevertheless
find those relations which can be reliably utilized for learning, we follow a
divide-and-conquer strategy: We find reliable similarities by extracting
compact groups of images and reliable dissimilarities by partitioning these
groups into subsets, converting the complicated overall problem into few
reliable local subproblems. For each of the subsets we obtain a representation
by learning a mapping to a target feature space so that their reliable
relations are kept. Transitivity relations between the subsets are then
exploited to consolidate the local solutions into a concerted global
representation. While iterating between grouping, partitioning, and learning,
we can successively use more and more reliable relations which, in turn,
improves our image representation. In experiments, our approach shows
state-of-the-art performance on unsupervised classification on ImageNet with
46.0% and competes favorably on different transfer learning tasks on PASCAL
VOC.