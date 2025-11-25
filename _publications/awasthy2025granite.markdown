---
layout: publication
title: Granite Embedding Models
authors: Parul Awasthy, Aashka Trivedi, Yulong Li, Mihaela Bornea, David Cox, Abraham
  Daniels, Martin Franz, Gabe Goodhart, Bhavani Iyer, Vishwajeet Kumar, Luis Lastras,
  Scott McCarley, Rudra Murthy, Vignesh P, Sara Rosenthal, Salim Roukos, Jaydeep Sen,
  Sukriti Sharma, Avirup Sil, Kate Soule, Arafat Sultan, Radu Florian
conference: Arxiv
year: 2025
bibkey: awasthy2025granite
citations: 0
additional_links: [{name: Code, url: 'https://huggingface.co/collections/ibm-granite'},
  {name: Paper, url: 'https://arxiv.org/abs/2502.20204'}]
tags: ["Evaluation", "Large Scale Search", "Similarity Search", "Text Retrieval"]
short_authors: Awasthy et al.
---
We introduce the Granite Embedding models, a family of encoder-based
embedding models designed for retrieval tasks, spanning dense-retrieval and
sparse retrieval architectures, with both English and Multilingual
capabilities. This report provides the technical details of training these
highly effective 12 layer embedding models, along with their efficient 6 layer
distilled counterparts. Extensive evaluations show that the models, developed
with techniques like retrieval oriented pretraining, contrastive finetuning,
knowledge distillation, and model merging significantly outperform publicly
available models of similar sizes on both internal IBM retrieval and search
tasks, and have equivalent performance on widely used information retrieval
benchmarks, while being trained on high-quality data suitable for enterprise
use. We publicly release all our Granite Embedding models under the Apache 2.0
license, allowing both research and commercial use at
https://huggingface.co/collections/ibm-granite.