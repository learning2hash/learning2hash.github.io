---
layout: publication
title: Palm-e An Embodied Multimodal Language Model
authors: Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine, Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus Greff, Andy Zeng, Igor Mordatch, Pete Florence
conference: "Arxiv"
year: 2023
bibkey: driess2023palm
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2303.03378v1"}
tags: ['ARXIV', 'Cross Modal']
---
Large language models excel at a wide range of complex tasks. However enabling general inference in the real world e.g. for robotics problems raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual continuous state estimation and textual input encodings. We train these encodings end-to-end in conjunction with a pre-trained large language model for multiple embodied tasks including sequential robotic manipulation planning visual question answering and captioning. Our evaluations show that PaLM-E a single large embodied multimodal model can address a variety of embodied reasoning tasks from a variety of observation modalities on multiple embodiments and further exhibits positive transfer the model benefits from diverse joint training across internet-scale language vision and visual-language domains. Our largest model PaLM-E-562B with 562B parameters in addition to being trained on robotics tasks is a visual-language generalist with state-of-the-art performance on OK-VQA and retains generalist language capabilities with increasing scale.
