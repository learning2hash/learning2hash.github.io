---
layout: publication
title: 'Document Valuation In LLM Summaries: A Cluster Shapley Approach'
authors: Zikun Ye, Hema Yoganarasimhan
conference: Arxiv
year: 2025
bibkey: ye2025document
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.23842'}]
tags: ["Evaluation"]
short_authors: Zikun Ye, Hema Yoganarasimhan
---
Large Language Models (LLMs) are increasingly used in systems that retrieve and summarize content from multiple sources, such as search engines and AI assistants. While these models enhance user experience by generating coherent summaries, they obscure the contributions of original content creators, raising concerns about credit attribution and compensation. We address the challenge of valuing individual documents used in LLM-generated summaries. We propose using Shapley values, a game-theoretic method that allocates credit based on each document's marginal contribution. Although theoretically appealing, Shapley values are expensive to compute at scale. We therefore propose Cluster Shapley, an efficient approximation algorithm that leverages semantic similarity between documents. By clustering documents using LLM-based embeddings and computing Shapley values at the cluster level, our method significantly reduces computation while maintaining attribution quality. We demonstrate our approach to a summarization task using Amazon product reviews. Cluster Shapley significantly reduces computational complexity while maintaining high accuracy, outperforming baseline methods such as Monte Carlo sampling and Kernel SHAP with a better efficient frontier. Our approach is agnostic to the exact LLM used, the summarization process used, and the evaluation procedure, which makes it broadly applicable to a variety of summarization settings.