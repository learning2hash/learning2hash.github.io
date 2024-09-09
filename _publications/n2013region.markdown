---
layout: publication
title: "Region and Location Based Indexing and Retrieval of MR-T2 Brain Tumor Images"
authors: N Krishna A, Prasad B G
conference: "International Journal of Information Processing,"
year: 2013
bibkey: n2013region
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1312.2061"}
tags: []
---
In this paper, region based and location based retrieval systems have been
implemented for retrieval of MR-T2 axial 2-D brain images. This is done by
extracting and characterizing the tumor portion of 2-D brain slices by use of a
suitable threshold computed over the entire image. Indexing and retrieval is
then performed by computing texture features based on gray-tone spatial-
dependence matrix of segmented regions. A Hash structure is used to index all
images. A combined index is adopted to point to all similar images in terms of
the texture features. At query time, only those images that are in the same hash
bucket as those of the queried image are compared for similarity, thus reducing
the search space and time.
