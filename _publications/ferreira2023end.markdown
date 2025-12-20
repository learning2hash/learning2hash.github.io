---
layout: publication
title: End-to-end Semantic Object Detection With Cross-modal Alignment
authors: Silvan Ferreira, Allan Martins, Ivanovitch Silva
conference: Arxiv
year: 2023
bibkey: ferreira2023end
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.05200'}]
tags: ["Image Retrieval", "Self-Supervised"]
short_authors: Silvan Ferreira, Allan Martins, Ivanovitch Silva
---
Traditional semantic image search methods aim to retrieve images that match
the meaning of the text query. However, these methods typically search for
objects on the whole image, without considering the localization of objects
within the image. This paper presents an extension of existing object detection
models for semantic image search that considers the semantic alignment between
object proposals and text queries, with a focus on searching for objects within
images. The proposed model uses a single feature extractor, a pre-trained
Convolutional Neural Network, and a transformer encoder to encode the text
query. Proposal-text alignment is performed using contrastive learning,
producing a score for each proposal that reflects its semantic alignment with
the text query. The Region Proposal Network (RPN) is used to generate object
proposals, and the end-to-end training process allows for an efficient and
effective solution for semantic image search. The proposed model was trained
end-to-end, providing a promising solution for semantic image search that
retrieves images that match the meaning of the text query and generates
semantically relevant object proposals.