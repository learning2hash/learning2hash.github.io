---
layout: publication
title: Fixed-length Bit-string Representation Of Fingerprint By Normalized Local Structures
authors: Jun Beom Kho, Andrew B. J. Teoh, Wonjune Lee, Jaihie Kim
conference: Arxiv
year: 2018
bibkey: kho2018fixed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.11489'}]
tags: []
short_authors: Kho et al.
---
In this paper, we propose a method to represent a fingerprint image by an
ordered, fixed-length bit-string providing improved accuracy performance,
faster matching time and compressibility. First, we devise a novel
minutia-based local structure modeled by a mixture of 2D elliptical Gaussian
functions in the pixel space. Each local structure is mapped to the Euclidean
space by normalizing the local structure with the number of minutiae that
associates to it. This simple yet crucial crux enables fast dissimilarity
computation of two local structures with Euclidean distance without distortion.
A complementary texture-based local structure to the minutia-based local
structure is also introduced whereby both can be compressed via principal
component analysis and fused easily in the Euclidean space. The fused local
structure is then converted to a K-bit ordered string via a K-means clustering
algorithm. This chain of computation with sole use of Euclidean distance is
vital for speedy and discriminative bit-string conversion. The accuracy can be
further improved by a finger-specific bit-training algorithm in which two
criteria are leveraged to select useful bit positions for matching. Experiments
are performed on Fingerprint Verification Competition (FVC) databases for
comparison with existing techniques to show the superiority of the proposed
method.