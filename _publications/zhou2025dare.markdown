---
layout: publication
title: Dare To Plagiarize? Plagiarized Painting Recognition And Retrieval
authors: Sophie Zhou, Shu Kong
conference: 2025 IEEE International Conference on Advanced Visual and Signal-Based
  Systems (AVSS)
year: 2025
bibkey: zhou2025dare
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.23132'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Sophie Zhou, Shu Kong
---
Art plagiarism detection plays a crucial role in protecting artists' copyrights and intellectual property, yet it remains a challenging problem in forensic analysis. In this paper, we address the task of recognizing plagiarized paintings and explaining the detected plagarisms by retrieving visually similar authentic artworks. To support this study, we construct a dataset by collecting painting photos and synthesizing plagiarized versions using generative AI, tailored to specific artists' styles. We first establish a baseline approach using off-the-shelf features from the visual foundation model DINOv2 to retrieve the most similar images in the database and classify plagiarism based on a similarity threshold. Surprisingly, this non-learned method achieves a high recognition accuracy of 97.2% but suffers from low retrieval precision 29.0% average precision (AP). To improve retrieval quality, we finetune DINOv2 with a metric learning loss using positive and negative sample pairs sampled in the database. The finetuned model greatly improves retrieval performance by 12% AP over the baseline, though it unexpectedly results in a lower recognition accuracy (92.7%). We conclude with insightful discussions and outline directions for future research.