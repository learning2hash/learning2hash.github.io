---
layout: publication
title: Cross-modal Semantic Enhanced Interaction For Image-sentence Retrieval
authors: Ge Xuri, Chen Fuhai, Xu Songpei, Tao Fuxiang, Jose Joemon M.
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: ge2022cross
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.08908'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Ge et al.
---
Image-sentence retrieval has attracted extensive research attention in
multimedia and computer vision due to its promising application. The key issue
lies in jointly learning the visual and textual representation to accurately
estimate their similarity. To this end, the mainstream schema adopts an
object-word based attention to calculate their relevance scores and refine
their interactive representations with the attention features, which, however,
neglects the context of the object representation on the inter-object
relationship that matches the predicates in sentences. In this paper, we
propose a Cross-modal Semantic Enhanced Interaction method, termed CMSEI for
image-sentence retrieval, which correlates the intra- and inter-modal semantics
between objects and words. In particular, we first design the intra-modal
spatial and semantic graphs based reasoning to enhance the semantic
representations of objects guided by the explicit relationships of the objects'
spatial positions and their scene graph. Then the visual and textual semantic
representations are refined jointly via the inter-modal interactive attention
and the cross-modal alignment. To correlate the context of objects with the
textual context, we further refine the visual semantic representation via the
cross-level object-sentence and word-image based interactive attention.
Experimental results on seven standard evaluation metrics show that the
proposed CMSEI outperforms the state-of-the-art and the alternative approaches
on MS-COCO and Flickr30K benchmarks.