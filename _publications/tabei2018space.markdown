---
layout: publication
title: Space-efficient Feature Maps For String Alignment Kernels
authors: Yasuo Tabei, Yoshihiro Yamanishi, Rasmus Pagh
conference: 2019 IEEE International Conference on Data Mining (ICDM)
year: 2019
bibkey: tabei2018space
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.06382'}]
tags: ["Efficiency"]
short_authors: Yasuo Tabei, Yoshihiro Yamanishi, Rasmus Pagh
---
String kernels are attractive data analysis tools for analyzing string data.
Among them, alignment kernels are known for their high prediction accuracies in
string classifications when tested in combination with SVM in various
applications. However, alignment kernels have a crucial drawback in that they
scale poorly due to their quadratic computation complexity in the number of
input strings, which limits large-scale applications in practice. We address
this need by presenting the first approximation for string alignment kernels,
which we call space-efficient feature maps for edit distance with moves
(SFMEDM), by leveraging a metric embedding named edit sensitive parsing (ESP)
and feature maps (FMs) of random Fourier features (RFFs) for large-scale string
analyses. The original FMs for RFFs consume a huge amount of memory
proportional to the dimension d of input vectors and the dimension D of output
vectors, which prohibits its large-scale applications. We present novel
space-efficient feature maps (SFMs) of RFFs for a space reduction from O(dD) of
the original FMs to O(d) of SFMs with a theoretical guarantee with respect to
concentration bounds. We experimentally test SFMEDM on its ability to learn SVM
for large-scale string classifications with various massive string data, and we
demonstrate the superior performance of SFMEDM with respect to prediction
accuracy, scalability and computation efficiency.