---
layout: publication
title: Few-shot Image Recognition With Manifolds
authors: Debasmit Das, J. H. Moon, C. S. George Lee
conference: Lecture Notes in Computer Science
year: 2020
bibkey: das2020few
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.12084'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Debasmit Das, J. H. Moon, C. S. George Lee
---
In this paper, we extend the traditional few-shot learning (FSL) problem to
the situation when the source-domain data is not accessible but only high-level
information in the form of class prototypes is available. This limited
information setup for the FSL problem deserves much attention due to its
implication of privacy-preserving inaccessibility to the source-domain data but
it has rarely been addressed before. Because of limited training data, we
propose a non-parametric approach to this FSL problem by assuming that all the
class prototypes are structurally arranged on a manifold. Accordingly, we
estimate the novel-class prototype locations by projecting the few-shot samples
onto the average of the subspaces on which the surrounding classes lie. During
classification, we again exploit the structural arrangement of the categories
by inducing a Markov chain on the graph constructed with the class prototypes.
This manifold distance obtained using the Markov chain is expected to produce
better results compared to a traditional nearest-neighbor-based Euclidean
distance. To evaluate our proposed framework, we have tested it on two image
datasets - the large-scale ImageNet and the small-scale but fine-grained
CUB-200. We have also studied parameter sensitivity to better understand our
framework.