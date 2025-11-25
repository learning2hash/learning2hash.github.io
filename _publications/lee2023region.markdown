---
layout: publication
title: Region-based Contrastive Pretraining For Medical Image Retrieval With Anatomic
  Query
authors: "Ho Hin Lee, Alberto Santamaria-Pang, Jameson Merkow, Ozan Oktay, Fernando\
  \ P\xE9rez-Garc\xEDa, Javier Alvarez-Valle, Ivan Tarapov"
conference: Arxiv
year: 2023
bibkey: lee2023region
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05598'}]
tags: ["Datasets", "Image Retrieval", "Self-Supervised"]
short_authors: Lee et al.
---
We introduce a novel Region-based contrastive pretraining for Medical Image
Retrieval (RegionMIR) that demonstrates the feasibility of medical image
retrieval with similar anatomical regions. RegionMIR addresses two major
challenges for medical image retrieval i) standardization of clinically
relevant searching criteria (e.g., anatomical, pathology-based), and ii)
localization of anatomical area of interests that are semantically meaningful.
In this work, we propose an ROI image retrieval image network that retrieves
images with similar anatomy by extracting anatomical features (via bounding
boxes) and evaluate similarity between pairwise anatomy-categorized features
between the query and the database of images using contrastive learning. ROI
queries are encoded using a contrastive-pretrained encoder that was fine-tuned
for anatomy classification, which generates an anatomical-specific latent space
for region-correlated image retrieval. During retrieval, we compare the
anatomically encoded query to find similar features within a feature database
generated from training samples, and retrieve images with similar regions from
training samples. We evaluate our approach on both anatomy classification and
image retrieval tasks using the Chest ImaGenome Dataset. Our proposed strategy
yields an improvement over state-of-the-art pretraining and co-training
strategies, from 92.24 to 94.12 (2.03%) classification accuracy in anatomies.
We qualitatively evaluate the image retrieval performance demonstrating
generalizability across multiple anatomies with different morphology.