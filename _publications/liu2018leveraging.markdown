---
layout: publication
title: Leveraging Unlabeled Data For Crowd Counting By Learning To Rank
authors: Xialei Liu, Joost van de Weijer, Andrew D. Bagdanov
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: liu2018leveraging
citations: 316
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.03095'}]
tags: ["CVPR"]
short_authors: Xialei Liu, Joost van de Weijer, Andrew D. Bagdanov
---
We propose a novel crowd counting approach that leverages abundantly
available unlabeled crowd imagery in a learning-to-rank framework. To induce a
ranking of cropped images , we use the observation that any sub-image of a
crowded scene image is guaranteed to contain the same number or fewer persons
than the super-image. This allows us to address the problem of limited size of
existing datasets for crowd counting. We collect two crowd scene datasets from
Google using keyword searches and query-by-example image retrieval,
respectively. We demonstrate how to efficiently learn from these unlabeled
datasets by incorporating learning-to-rank in a multi-task network which
simultaneously ranks images and estimates crowd density maps. Experiments on
two of the most challenging crowd counting datasets show that our approach
obtains state-of-the-art results.