---
layout: publication
title: Double Trouble? Impact And Detection Of Duplicates In Face Image Datasets
authors: Torsten Schlett, Christian Rathgeb, Juan Tapia, Christoph Busch
conference: Proceedings of the 13th International Conference on Pattern Recognition
  Applications and Methods
year: 2024
bibkey: schlett2024double
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14088'}]
tags: ["Datasets"]
short_authors: Schlett et al.
---
Various face image datasets intended for facial biometrics research were
created via web-scraping, i.e. the collection of images publicly available on
the internet. This work presents an approach to detect both exactly and nearly
identical face image duplicates, using file and image hashes. The approach is
extended through the use of face image preprocessing. Additional steps based on
face recognition and face image quality assessment models reduce false
positives, and facilitate the deduplication of the face images both for intra-
and inter-subject duplicate sets. The presented approach is applied to five
datasets, namely LFW, TinyFace, Adience, CASIA-WebFace, and C-MS-Celeb (a
cleaned MS-Celeb-1M variant). Duplicates are detected within every dataset,
with hundreds to hundreds of thousands of duplicates for all except LFW. Face
recognition and quality assessment experiments indicate a minor impact on the
results through the duplicate removal. The final deduplication data is publicly
available.