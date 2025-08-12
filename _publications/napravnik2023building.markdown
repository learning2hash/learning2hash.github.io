---
layout: publication
title: 'Building Radiologynet: Unsupervised Annotation Of A Large-scale Multimodal
  Medical Database'
authors: "Mateja Napravnik, Franko Hr\u017Ei\u0107, Sebastian Tschauner, Ivan \u0160\
  tajduhar"
conference: Arxiv
year: 2023
bibkey: napravnik2023building
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.08517'}]
tags: ["Datasets", "Scalability", "Unsupervised"]
short_authors: Napravnik et al.
---
Background and objective: The usage of machine learning in medical diagnosis
and treatment has witnessed significant growth in recent years through the
development of computer-aided diagnosis systems that are often relying on
annotated medical radiology images. However, the availability of large
annotated image datasets remains a major obstacle since the process of
annotation is time-consuming and costly. This paper explores how to
automatically annotate a database of medical radiology images with regard to
their semantic similarity.
  Material and methods: An automated, unsupervised approach is used to
construct a large annotated dataset of medical radiology images originating
from Clinical Hospital Centre Rijeka, Croatia, utilising multimodal sources,
including images, DICOM metadata, and narrative diagnoses. Several appropriate
feature extractors are tested for each of the data sources, and their utility
is evaluated using k-means and k-medoids clustering on a representative data
subset.
  Results: The optimal feature extractors are then integrated into a multimodal
representation, which is then clustered to create an automated pipeline for
labelling a precursor dataset of 1,337,926 medical images into 50 clusters of
visually similar images. The quality of the clusters is assessed by examining
their homogeneity and mutual information, taking into account the anatomical
region and modality representation.
  Conclusion: The results suggest that fusing the embeddings of all three data
sources together works best for the task of unsupervised clustering of
large-scale medical data, resulting in the most concise clusters. Hence, this
work is the first step towards building a much larger and more fine-grained
annotated dataset of medical radiology images.