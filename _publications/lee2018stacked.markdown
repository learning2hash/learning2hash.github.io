---
layout: publication
title: Stacked Cross Attention For Image-text Matching
authors: Lee Kuang-huei, Chen Xi, Hua Gang, Hu Houdong, He Xiaodong
conference: Lecture Notes in Computer Science
year: 2018
bibkey: lee2018stacked
citations: 1151
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.08024'}]
tags: ["Evaluation", "Image-Retrieval", "Datasets"]
short_authors: Lee et al.
---
In this paper, we study the problem of image-text matching. Inferring the
latent semantic alignment between objects or other salient stuff (e.g. snow,
sky, lawn) and the corresponding words in sentences allows to capture
fine-grained interplay between vision and language, and makes image-text
matching more interpretable. Prior work either simply aggregates the similarity
of all possible pairs of regions and words without attending differentially to
more and less important words or regions, or uses a multi-step attentional
process to capture limited number of semantic alignments which is less
interpretable. In this paper, we present Stacked Cross Attention to discover
the full latent alignments using both image regions and words in a sentence as
context and infer image-text similarity. Our approach achieves the
state-of-the-art results on the MS-COCO and Flickr30K datasets. On Flickr30K,
our approach outperforms the current best methods by 22.1% relatively in text
retrieval from image query, and 18.2% relatively in image retrieval with text
query (based on Recall@1). On MS-COCO, our approach improves sentence retrieval
by 17.8% relatively and image retrieval by 16.6% relatively (based on Recall@1
using the 5K test set). Code has been made available at:
https://github.com/kuanghuei/SCAN.