---
layout: publication
title: 'Joint Fusion And Encoding: Advancing Multimodal Retrieval From The Ground
  Up'
authors: Huang et al.
conference: Remote Sensing
year: 2025
bibkey: huang2025joint
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.20008'}]
tags: ["Multimodal-Retrieval"]
---
Information retrieval is indispensable for today's Internet applications, yet
traditional semantic matching techniques often fall short in capturing the
fine-grained cross-modal interactions required for complex queries. Although
late-fusion two-tower architectures attempt to bridge this gap by independently
encoding visual and textual data before merging them at a high level, they
frequently overlook the subtle interplay essential for comprehensive
understanding. In this work, we rigorously assess these limitations and
introduce a unified retrieval framework that fuses visual and textual cues from
the ground up, enabling early cross-modal interactions for enhancing context
interpretation. Through a two-stage training process--comprising post-training
adaptation followed by instruction tuning--we adapt MLLMs as retrievers using a
simple one-tower architecture. Our approach outperforms conventional methods
across diverse retrieval scenarios, particularly when processing complex
multi-modal inputs. Notably, the joint fusion encoder yields greater
improvements on tasks that require modality fusion compared to those that do
not, underscoring the transformative potential of early integration strategies
and pointing toward a promising direction for contextually aware and effective
information retrieval.