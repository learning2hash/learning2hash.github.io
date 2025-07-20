---
layout: publication
title: Zero Shot Composed Image Retrieval
authors: Kakarla Santhosh, Venkata Gautama Shastry Bulusu
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: kakarla2023zero
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.06602'}]
tags: [CVPR, Image Retrieval]
---
Composed image retrieval (CIR) allows a user to locate a target image by applying a fine-grained textual edit (e.g., ``turn the dress blue'' or ``remove stripes'') to a reference image. Zero-shot CIR, which embeds the image and the text with separate pretrained vision-language encoders, reaches only 20-25% Recall@10 on the FashionIQ benchmark. We improve this by fine-tuning BLIP-2 with a lightweight Q-Former that fuses visual and textual features into a single embedding, raising Recall@10 to 45.6% (shirt), 40.1% (dress), and 50.4% (top-tee) and increasing the average Recall@50 to 67.6%. We also examine Retrieval-DPO, which fine-tunes CLIP's text encoder with a Direct Preference Optimization loss applied to FAISS-mined hard negatives. Despite extensive tuning of the scaling factor, index, and sampling strategy, Retrieval-DPO attains only 0.02% Recall@10 -- far below zero-shot and prompt-tuned baselines -- because it (i) lacks joint image-text fusion, (ii) uses a margin objective misaligned with top-\\(K\\) metrics, (iii) relies on low-quality negatives, and (iv) keeps the vision and Transformer layers frozen. Our results show that effective preference-based CIR requires genuine multimodal fusion, ranking-aware objectives, and carefully curated negatives.