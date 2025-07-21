---
layout: publication
title: 'Llama Nemoretriever Colembed: Top-performing Text-image Retrieval Model'
authors: Xu et al.
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2025
bibkey: xu2025llama
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.05513'}]
tags: ["SIGIR", "Text Retrieval", "Image Retrieval"]
---
Motivated by the growing demand for retrieval systems that operate across modalities, we introduce llama-nemoretriever-colembed, a unified text-image retrieval model that delivers state-of-the-art performance across multiple benchmarks. We release two model variants, 1B and 3B. The 3B model achieves state of the art performance, scoring NDCG@5 91.0 on ViDoRe V1 and 63.5 on ViDoRe V2, placing first on both leaderboards as of June 27, 2025.
  Our approach leverages the NVIDIA Eagle2 Vision-Language model (VLM), modifies its architecture by replacing causal attention with bidirectional attention, and integrates a ColBERT-style late interaction mechanism to enable fine-grained multimodal retrieval in a shared embedding space. While this mechanism delivers superior retrieval accuracy, it introduces trade-offs in storage and efficiency. We provide a comprehensive analysis of these trade-offs. Additionally, we adopt a two-stage training strategy to enhance the model's retrieval capabilities.