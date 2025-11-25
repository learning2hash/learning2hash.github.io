---
layout: publication
title: 'Bendvlm: Test-time Debiasing Of Vision-language Embeddings'
authors: Walter Gerych, Haoran Zhang, Kimia Hamidieh, Eileen Pan, Maanas Sharma, Thomas
  Hartvigsen, Marzyeh Ghassemi
conference: Arxiv
year: 2024
bibkey: gerych2024bendvlm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.04420'}]
tags: ["Few Shot & Zero Shot", "Multimodal Retrieval"]
short_authors: Gerych et al.
---
Vision-language model (VLM) embeddings have been shown to encode biases
present in their training data, such as societal biases that prescribe negative
characteristics to members of various racial and gender identities. VLMs are
being quickly adopted for a variety of tasks ranging from few-shot
classification to text-guided image generation, making debiasing VLM embeddings
crucial. Debiasing approaches that fine-tune the VLM often suffer from
catastrophic forgetting. On the other hand, fine-tuning-free methods typically
utilize a "one-size-fits-all" approach that assumes that correlation with the
spurious attribute can be explained using a single linear direction across all
possible inputs. In this work, we propose Bend-VLM, a nonlinear,
fine-tuning-free approach for VLM embedding debiasing that tailors the
debiasing operation to each unique input. This allows for a more flexible
debiasing approach. Additionally, we do not require knowledge of the set of
inputs a priori to inference time, making our method more appropriate for
online, open-set tasks such as retrieval and text guided image generation.