---
layout: publication
title: Descriptive Image-text Matching With Graded Contextual Similarity
authors: Jinhyun Jang, Jiyoung Lee, Kwanghoon Sohn
conference: Arxiv
year: 2025
bibkey: jang2025descriptive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.09997'}]
tags: ["Datasets", "Evaluation"]
short_authors: Jinhyun Jang, Jiyoung Lee, Kwanghoon Sohn
---
Image-text matching aims to build correspondences between visual and textual data by learning their pairwise similarities. Most existing approaches have adopted sparse binary supervision, indicating whether a pair of images and sentences matches or not. However, such sparse supervision covers a limited subset of image-text relationships, neglecting their inherent many-to-many correspondences; an image can be described in numerous texts at different descriptive levels. Moreover, existing approaches overlook the implicit connections from general to specific descriptions, which form the underlying rationale for the many-to-many relationships between vision and language. In this work, we propose descriptive image-text matching, called DITM, to learn the graded contextual similarity between image and text by exploring the descriptive flexibility of language. We formulate the descriptiveness score of each sentence with cumulative term frequency-inverse document frequency (TF-IDF) to balance the pairwise similarity according to the keywords in the sentence. Our method leverages sentence descriptiveness to learn robust image-text matching in two key ways: (1) to refine the false negative labeling, dynamically relaxing the connectivity between positive and negative pairs, and (2) to build more precise matching, aligning a set of relevant sentences in a generic-to-specific order. By moving beyond rigid binary supervision, DITM enhances the discovery of both optimal matches and potential positive pairs. Extensive experiments on MS-COCO, Flickr30K, and CxC datasets demonstrate the effectiveness of our method in representing complex image-text relationships compared to state-of-the-art approaches. In addition, DITM enhances the hierarchical reasoning ability of the model, supported by the extensive analysis on HierarCaps benchmark.