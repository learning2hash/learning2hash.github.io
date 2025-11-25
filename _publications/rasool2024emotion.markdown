---
layout: publication
title: Emotion-aware Embedding Fusion In Llms (flan-t5, LLAMA 2, Deepseek-r1, And
  Chatgpt 4) For Intelligent Response Generation
authors: Abdur Rasool, Muhammad Irfan Shahzad, Hafsa Aslam, Vincent Chan, Muhammad
  Ali Arshad
conference: AI
year: 2024
bibkey: rasool2024emotion
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.01306'}]
tags: ["Similarity Search"]
short_authors: Rasool et al.
---
Empathetic and coherent responses are critical in auto-mated
chatbot-facilitated psychotherapy. This study addresses the challenge of
enhancing the emotional and contextual understanding of large language models
(LLMs) in psychiatric applications. We introduce Emotion-Aware Embedding
Fusion, a novel framework integrating hierarchical fusion and attention
mechanisms to prioritize semantic and emotional features in therapy
transcripts. Our approach combines multiple emotion lexicons, including NRC
Emotion Lexicon, VADER, WordNet, and SentiWordNet, with state-of-the-art LLMs
such as Flan-T5, LLAMA 2, DeepSeek-R1, and ChatGPT 4. Therapy session
transcripts, comprising over 2,000 samples are segmented into hierarchical
levels (word, sentence, and session) using neural networks, while hierarchical
fusion combines these features with pooling techniques to refine emotional
representations. Atten-tion mechanisms, including multi-head self-attention and
cross-attention, further prioritize emotional and contextual features, enabling
temporal modeling of emotion-al shifts across sessions. The processed
embeddings, computed using BERT, GPT-3, and RoBERTa are stored in the Facebook
AI similarity search vector database, which enables efficient similarity search
and clustering across dense vector spaces. Upon user queries, relevant segments
are retrieved and provided as context to LLMs, enhancing their ability to
generate empathetic and con-textually relevant responses. The proposed
framework is evaluated across multiple practical use cases to demonstrate
real-world applicability, including AI-driven therapy chatbots. The system can
be integrated into existing mental health platforms to generate personalized
responses based on retrieved therapy session data.