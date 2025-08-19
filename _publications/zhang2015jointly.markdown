---
layout: publication
title: Jointly Learning Multiple Measures Of Similarities From Triplet Comparisons
authors: Liwen Zhang, Subhransu Maji, Ryota Tomioka
conference: Arxiv
year: 2015
bibkey: zhang2015jointly
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1503.01521'}]
tags: [Tools & Libraries, Distance Metric Learning, Datasets, Evaluation]
short_authors: Liwen Zhang, Subhransu Maji, Ryota Tomioka
---
Similarity between objects is multi-faceted and it can be easier for human
annotators to measure it when the focus is on a specific aspect. We consider
the problem of mapping objects into view-specific embeddings where the distance
between them is consistent with the similarity comparisons of the form "from
the t-th view, object A is more similar to B than to C". Our framework jointly
learns view-specific embeddings exploiting correlations between views.
Experiments on a number of datasets, including one of multi-view crowdsourced
comparison on bird images, show the proposed method achieves lower triplet
generalization error when compared to both learning embeddings independently
for each view and all views pooled into one view. Our method can also be used
to learn multiple measures of similarity over input features taking class
labels into account and compares favorably to existing approaches for
multi-task metric learning on the ISOLET dataset.