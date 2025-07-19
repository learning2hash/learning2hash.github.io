---
layout: publication
title: Cross-modal Retrieval With Implicit Concept Association
authors: Song Yale, Soleymani Mohammad
conference: Arxiv
year: 2018
bibkey: song2018cross
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04318'}]
tags: [Multimodal Retrieval]
---
Traditional cross-modal retrieval assumes explicit association of concepts
across modalities, where there is no ambiguity in how the concepts are linked
to each other, e.g., when we do the image search with a query "dogs", we expect
to see dog images. In this paper, we consider a different setting for
cross-modal retrieval where data from different modalities are implicitly
linked via concepts that must be inferred by high-level reasoning; we call this
setting implicit concept association. To foster future research in this
setting, we present a new dataset containing 47K pairs of animated GIFs and
sentences crawled from the web, in which the GIFs depict physical or emotional
reactions to the scenarios described in the text (called "reaction GIFs"). We
report on a user study showing that, despite the presence of implicit concept
association, humans are able to identify video-sentence pairs with matching
concepts, suggesting the feasibility of our task. Furthermore, we propose a
novel visual-semantic embedding network based on multiple instance learning.
Unlike traditional approaches, we compute multiple embeddings from each
modality, each representing different concepts, and measure their similarity by
considering all possible combinations of visual-semantic embeddings in the
framework of multiple instance learning. We evaluate our approach on two
video-sentence datasets with explicit and implicit concept association and
report competitive results compared to existing approaches on cross-modal
retrieval.