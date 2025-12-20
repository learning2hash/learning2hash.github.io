---
layout: publication
title: 'FLAP: Fast Language-audio Pre-training'
authors: Ching-Feng Yeh, Po-Yao Huang, Vasu Sharma, Shang-Wen Li, Gargi Gosh
conference: 2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)
year: 2023
bibkey: yeh2023flap
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.01615'}]
tags: ["Efficiency", "Evaluation", "Self-Supervised", "Supervised", "Text Retrieval"]
short_authors: Yeh et al.
---
We propose Fast Language-Audio Pre-training (FLAP), a self-supervised
approach that efficiently and effectively learns aligned audio and language
representations through masking, contrastive learning and reconstruction. For
efficiency, FLAP randomly drops audio spectrogram tokens, focusing solely on
the remaining ones for self-supervision. Through inter-modal contrastive
learning, FLAP learns to align paired audio and text representations in a
shared latent space. Notably, FLAP leverages multiple augmented views via
masking for inter-modal contrast and learns to reconstruct the masked portion
of audio tokens. Moreover, FLAP leverages large language models (LLMs) to
augment the text inputs, contributing to improved performance. These approaches
lead to more robust and informative audio-text representations, enabling FLAP
to achieve state-of-the-art (SoTA) performance on audio-text retrieval tasks on
AudioCaps (achieving 53.0% R@1) and Clotho (achieving 25.5% R@1).