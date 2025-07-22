---
layout: publication
title: '3shnet: Boosting Image-sentence Retrieval Via Visual Semantic-spatial Self-highlighting'
authors: Ge Xuri, Xu Songpei, Chen Fuhai, Wang Jie, Wang Guoxin, An Shan, Jose Joemon
  M.
conference: Information Processing &amp; Management
year: 2024
bibkey: ge20243shnet
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.17273'}]
tags: ["Efficiency", "Evaluation", "Datasets"]
short_authors: Ge et al.
---
In this paper, we propose a novel visual Semantic-Spatial Self-Highlighting
Network (termed 3SHNet) for high-precision, high-efficiency and
high-generalization image-sentence retrieval. 3SHNet highlights the salient
identification of prominent objects and their spatial locations within the
visual modality, thus allowing the integration of visual semantics-spatial
interactions and maintaining independence between two modalities. This
integration effectively combines object regions with the corresponding semantic
and position layouts derived from segmentation to enhance the visual
representation. And the modality-independence guarantees efficiency and
generalization. Additionally, 3SHNet utilizes the structured contextual visual
scene information from segmentation to conduct the local (region-based) or
global (grid-based) guidance and achieve accurate hybrid-level retrieval.
Extensive experiments conducted on MS-COCO and Flickr30K benchmarks
substantiate the superior performances, inference efficiency and generalization
of the proposed 3SHNet when juxtaposed with contemporary state-of-the-art
methodologies. Specifically, on the larger MS-COCO 5K test set, we achieve
16.3%, 24.8%, and 18.3% improvements in terms of rSum score, respectively,
compared with the state-of-the-art methods using different image
representations, while maintaining optimal retrieval efficiency. Moreover, our
performance on cross-dataset generalization improves by 18.6%. Data and code
are available at https://github.com/XuriGe1995/3SHNet.