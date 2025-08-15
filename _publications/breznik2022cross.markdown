---
layout: publication
title: Cross-modality Sub-image Retrieval Using Contrastive Multimodal Image Representations
authors: "Eva Breznik, Elisabeth Wetzer, Joakim Lindblad, Nata\u0161a Sladoje"
conference: Arxiv
year: 2022
bibkey: breznik2022cross
citations: 3
additional_links: [{name: Code, url: 'https://github.com/MIDA-group/CrossModal_ImgRetrieval.'},
  {name: Paper, url: 'https://arxiv.org/abs/2201.03597'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Breznik et al.
---
In tissue characterization and cancer diagnostics, multimodal imaging has
emerged as a powerful technique. Thanks to computational advances, large
datasets can be exploited to discover patterns in pathologies and improve
diagnosis. However, this requires efficient and scalable image retrieval
methods. Cross-modality image retrieval is particularly challenging, since
images of similar (or even the same) content captured by different modalities
might share few common structures. We propose a new application-independent
content-based image retrieval (CBIR) system for reverse (sub-)image search
across modalities, which combines deep learning to generate representations
(embedding the different modalities in a common space) with classical feature
extraction and bag-of-words models for efficient and reliable retrieval. We
illustrate its advantages through a replacement study, exploring a number of
feature extractors and learned representations, as well as through comparison
to recent (cross-modality) CBIR methods. For the task of (sub-)image retrieval
on a (publicly available) dataset of brightfield and second harmonic generation
microscopy images, the results show that our approach is superior to all tested
alternatives. We discuss the shortcomings of the compared methods and observe
the importance of equivariance and invariance properties of the learned
representations and feature extractors in the CBIR pipeline. Code is available
at: https://github.com/MIDA-group/CrossModal_ImgRetrieval.