---
layout: publication
title: 'MATE: Meet At The Embedding -- Connecting Images With Long Texts'
authors: Young Kyun Jang, Junmo Kang, Yong Jae Lee, Donghyun Kim
conference: Arxiv
year: 2024
bibkey: jang2024mate
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.09541'}]
tags: [Evaluation, Multimodal Retrieval]
short_authors: Jang et al.
---
While advancements in Vision Language Models (VLMs) have significantly
improved the alignment of visual and textual data, these models primarily focus
on aligning images with short descriptive captions. This focus limits their
ability to handle complex text interactions, particularly with longer texts
such as lengthy captions or documents, which have not been extensively explored
yet. In this paper, we introduce Meet At The Embedding (MATE), a novel approach
that combines the capabilities of VLMs with Large Language Models (LLMs) to
overcome this challenge without the need for additional image-long text pairs.
Specifically, we replace the text encoder of the VLM with a pretrained
LLM-based encoder that excels in understanding long texts. To bridge the gap
between VLM and LLM, MATE incorporates a projection module that is trained in a
multi-stage manner. It starts by aligning the embeddings from the VLM text
encoder with those from the LLM using extensive text pairs. This module is then
employed to seamlessly align image embeddings closely with LLM embeddings. We
propose two new cross-modal retrieval benchmarks to assess the task of
connecting images with long texts (lengthy captions / documents). Extensive
experimental results demonstrate that MATE effectively connects images with
long texts, uncovering diverse semantic relationships.