---
layout: publication
title: Fine-tuning Llama For Multi-stage Text Retrieval
authors: Xueguang Ma, Liang Wang, Nan Yang, Furu Wei, Jimmy Lin
conference: Arxiv
year: 2023
bibkey: ma2023fine
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.08319'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Re-Ranking", "Text Retrieval"]
short_authors: Ma et al.
---
The effectiveness of multi-stage text retrieval has been solidly demonstrated
since before the era of pre-trained language models. However, most existing
studies utilize models that predate recent advances in large language models
(LLMs). This study seeks to explore potential improvements that
state-of-the-art LLMs can bring. We conduct a comprehensive study, fine-tuning
the latest LLaMA model both as a dense retriever (RepLLaMA) and as a pointwise
reranker (RankLLaMA) for both passage retrieval and document retrieval using
the MS MARCO datasets. Our findings demonstrate that the effectiveness of large
language models indeed surpasses that of smaller models. Additionally, since
LLMs can inherently handle longer contexts, they can represent entire documents
holistically, obviating the need for traditional segmenting and pooling
strategies. Furthermore, evaluations on BEIR demonstrate that our
RepLLaMA-RankLLaMA pipeline exhibits strong zero-shot effectiveness. Model
checkpoints from this study are available on HuggingFace.