---
layout: publication
title: 'CLASP: Contrastive Language-speech Pretraining For Multilingual Multimodal
  Information Retrieval'
authors: Mohammad Mahdi Abootorabi, Ehsaneddin Asgari
conference: Arxiv
year: 2024
bibkey: abootorabi2024clasp
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13071'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised", "Text Retrieval"]
short_authors: Mohammad Mahdi Abootorabi, Ehsaneddin Asgari
---
This study introduces CLASP (Contrastive Language-Speech Pretraining), a
multilingual, multimodal representation tailored for audio-text information
retrieval. CLASP leverages the synergy between spoken content and textual data.
During training, we utilize our newly introduced speech-text dataset, which
encompasses 15 diverse categories ranging from fiction to religion. CLASP's
audio component integrates audio spectrograms with a pre-trained
self-supervised speech model, while its language encoding counterpart employs a
sentence encoder pre-trained on over 100 languages. This unified lightweight
model bridges the gap between various modalities and languages, enhancing its
effectiveness in handling and retrieving multilingual and multimodal data. Our
evaluations across multiple languages demonstrate that CLASP establishes new
benchmarks in HITS@1, MRR, and meanR metrics, outperforming traditional
ASR-based retrieval methods that rely on transcribing speech into text for
subsequent text retrieval, especially in specific scenarios.