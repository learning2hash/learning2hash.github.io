---
layout: publication
title: 'Adatriplet: Adaptive Gradient Triplet Loss With Automatic Margin Learning
  For Forensic Medical Image Matching'
authors: Khanh Nguyen, Huy Hoang Nguyen, Aleksei Tiulpin
conference: Lecture Notes in Computer Science
year: 2022
bibkey: nguyen2022adatriplet
citations: 7
additional_links: [{name: Code, url: 'https://github.com/Oulu-IMEDS/AdaTriplet'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.02849'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Khanh Nguyen, Huy Hoang Nguyen, Aleksei Tiulpin
---
This paper tackles the challenge of forensic medical image matching (FMIM)
using deep neural networks (DNNs). FMIM is a particular case of content-based
image retrieval (CBIR). The main challenge in FMIM compared to the general case
of CBIR, is that the subject to whom a query image belongs may be affected by
aging and progressive degenerative disorders, making it difficult to match data
on a subject level. CBIR with DNNs is generally solved by minimizing a ranking
loss, such as Triplet loss (TL), computed on image representations extracted by
a DNN from the original data. TL, in particular, operates on triplets: anchor,
positive (similar to anchor) and negative (dissimilar to anchor). Although TL
has been shown to perform well in many CBIR tasks, it still has limitations,
which we identify and analyze in this work. In this paper, we introduce (i) the
AdaTriplet loss -- an extension of TL whose gradients adapt to different
difficulty levels of negative samples, and (ii) the AutoMargin method -- a
technique to adjust hyperparameters of margin-based losses such as TL and our
proposed loss dynamically. Our results are evaluated on two large-scale
benchmarks for FMIM based on the Osteoarthritis Initiative and Chest X-ray-14
datasets. The codes allowing replication of this study have been made publicly
available at https://github.com/Oulu-IMEDS/AdaTriplet.