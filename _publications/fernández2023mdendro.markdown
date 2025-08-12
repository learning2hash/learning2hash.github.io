---
layout: publication
title: 'Mdendro: An R Package For Extended Agglomerative Hierarchical Clustering'
authors: "Alberto Fern\xE1ndez, Sergio G\xF3mez"
conference: Arxiv
year: 2023
bibkey: "fern\xE1ndez2023mdendro"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.13333'}]
tags: ["Tools & Libraries", "Unsupervised"]
short_authors: "Alberto Fern\xE1ndez, Sergio G\xF3mez"
---
"mdendro" is an R package that provides a comprehensive collection of linkage
methods for agglomerative hierarchical clustering on a matrix of proximity data
(distances or similarities), returning a multifurcated dendrogram or
multidendrogram. Multidendrograms can group more than two clusters at the same
time, solving the nonuniqueness problem that arises when there are ties in the
data. This problem causes that different binary dendrograms are possible
depending both on the order of the input data and on the criterion used to
break ties. Weighted and unweighted versions of the most common linkage methods
are included in the package, which also implements two parametric linkage
methods. In addition, package "mdendro" provides five descriptive measures to
analyze the resulting dendrograms: cophenetic correlation coefficient, space
distortion ratio, agglomeration coefficient, chaining coefficient and tree
balance.