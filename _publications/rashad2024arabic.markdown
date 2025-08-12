---
layout: publication
title: 'Arabic-nougat: Fine-tuning Vision Transformers For Arabic OCR And Markdown
  Extraction'
authors: Mohamed Rashad
conference: Arxiv
year: 2024
bibkey: rashad2024arabic
citations: 0
additional_links: [{name: Code, url: 'https://github.com/MohamedAliRashad/arabic-nougat'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.17835'}]
tags: ["Datasets", "Evaluation"]
short_authors: Mohamed Rashad
---
We present Arabic-Nougat, a suite of OCR models for converting Arabic book
pages into structured Markdown text. Based on Meta's Nougat architecture,
Arabic-Nougat includes three specialized models: arabic-small-nougat,
arabic-base-nougat, and arabic-large-nougat. These models are fine-tuned on a
synthetic dataset, arabic-img2md, comprising 13.7k pairs of Arabic book pages
and their Markdown representations. Key contributions include the
Aranizer-PBE-86k tokenizer, designed for efficient tokenization, and the use of
torch.bfloat16 precision with Flash Attention 2 for optimized training and
inference. Our models achieve state-of-the-art performance, with
arabic-large-nougat delivering the highest Markdown Structure Accuracy and the
lowest Character Error Rate. Additionally, we release a large-scale dataset
containing 1.1 billion Arabic tokens extracted from over 8,500 books using our
best-performing model, providing a valuable resource for Arabic OCR research.
All models, datasets, and code are open-sourced and available at
https://github.com/MohamedAliRashad/arabic-nougat.