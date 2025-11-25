---
layout: publication
title: \(d_x\)-privacy For Text And The Curse Of Dimensionality
authors: Hassan Jameel Asghar, Robin Carpentier, Benjamin Zi Hao Zhao, Dali Kaafar
conference: Arxiv
year: 2024
bibkey: asghar2024d_x
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.13784'}]
tags: ["Privacy & Security"]
short_authors: Asghar et al.
---
A widely used method to ensure privacy of unstructured text data is the
multidimensional Laplace mechanism for \(d_X\)-privacy, which is a relaxation of
differential privacy for metric spaces. We identify an intriguing peculiarity
of this mechanism. When applied on a word-by-word basis, the mechanism either
outputs the original word, or completely dissimilar words, and very rarely any
semantically similar words. We investigate this observation in detail, and tie
it to the fact that the distance of the nearest neighbor of a word in any word
embedding model (which are high-dimensional) is much larger than the relative
difference in distances to any of its two consecutive neighbors. We also show
that the dot product of the multidimensional Laplace noise vector with any word
embedding plays a crucial role in designating the nearest neighbor. We derive
the distribution, moments and tail bounds of this dot product. We further
propose a fix as a post-processing step, which satisfactorily removes the
above-mentioned issue.