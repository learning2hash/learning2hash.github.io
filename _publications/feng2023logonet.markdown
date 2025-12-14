---
layout: publication
title: 'Logonet: A Fine-grained Network For Instance-level Logo Sketch Retrieval'
authors: Binbin Feng, Jun Li, Jianhua Xu
conference: Lecture Notes in Computer Science
year: 2023
bibkey: feng2023logonet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.02214'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Binbin Feng, Jun Li, Jianhua Xu
---
Sketch-based image retrieval, which aims to use sketches as queries to
retrieve images containing the same query instance, receives increasing
attention in recent years. Although dramatic progress has been made in sketch
retrieval, few efforts are devoted to logo sketch retrieval which is still
hindered by the following challenges: Firstly, logo sketch retrieval is more
difficult than typical sketch retrieval problem, since a logo sketch usually
contains much less visual contents with only irregular strokes and lines.
Secondly, instance-specific sketches demonstrate dramatic appearance variances,
making them less identifiable when querying the same logo instance. Thirdly,
there exist several sketch retrieval benchmarking datasets nowadays, whereas an
instance-level logo sketch dataset is still publicly unavailable. To address
the above-mentioned limitations, we make twofold contributions in this study
for instance-level logo sketch retrieval. To begin with, we construct an
instance-level logo sketch dataset containing 2k logo instances and exceeding
9k sketches. To our knowledge, this is the first publicly available
instance-level logo sketch dataset. Next, we develop a fine-grained
triple-branch CNN architecture based on hybrid attention mechanism termed
LogoNet for accurate logo sketch retrieval. More specifically, we embed the
hybrid attention mechanism into the triple-branch architecture for capturing
the key query-specific information from the limited visual cues in the logo
sketches. Experimental evaluations both on our assembled dataset and public
benchmark datasets demonstrate the effectiveness of our proposed network.