---
layout: publication
title: Semi-supervised Lung Nodule Retrieval
authors: Loyman Mark, Greenspan Hayit
conference: Arxiv
year: 2020
bibkey: loyman2020semi
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.01805'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Medical Retrieval", "Supervised", "Unsupervised"]
short_authors: Loyman Mark, Greenspan Hayit
---
Content based image retrieval (CBIR) provides the clinician with visual
information that can support, and hopefully improve, his or her decision making
process. Given an input query image, a CBIR system provides as its output a set
of images, ranked by similarity to the query image. Retrieved images may come
with relevant information, such as biopsy-based malignancy labeling, or
categorization. Ground truth on similarity between dataset elements (e.g.
between nodules) is not readily available, thus greatly challenging machine
learning methods. Such annotations are particularly difficult to obtain, due to
the subjective nature of the task, with high inter-observer variability
requiring multiple expert annotators. Consequently, past approaches have
focused on manual feature extraction, while current approaches use auxiliary
tasks, such as a binary classification task (e.g. malignancy), for which
ground-true is more readily accessible. However, in a previous study, we have
shown that binary auxiliary tasks are inferior to the usage of a rough
similarity estimate that are derived from data annotations. The current study
suggests a semi-supervised approach that involves two steps: 1) Automatic
annotation of a given partially labeled dataset; 2) Learning a semantic
similarity metric space based on the predicated annotations. The proposed
system is demonstrated in lung nodule retrieval using the LIDC dataset, and
shows that it is feasible to learn embedding from predicted ratings. The
semi-supervised approach has demonstrated a significantly higher discriminative
ability than the fully-unsupervised reference.