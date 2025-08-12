---
layout: publication
title: 'Prototypical Priors: From Improving Classification To Zero-shot Learning'
authors: Saumya Jetley, Bernardino Romera-Paredes, Sadeep Jayasumana, Philip Torr
conference: Procedings of the British Machine Vision Conference 2015
year: 2015
bibkey: jetley2015prototypical
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.01192'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jetley et al.
---
Recent works on zero-shot learning make use of side information such as
visual attributes or natural language semantics to define the relations between
output visual classes and then use these relationships to draw inference on new
unseen classes at test time. In a novel extension to this idea, we propose the
use of visual prototypical concepts as side information. For most real-world
visual object categories, it may be difficult to establish a unique prototype.
However, in cases such as traffic signs, brand logos, flags, and even natural
language characters, these prototypical templates are available and can be
leveraged for an improved recognition performance. The present work proposes a
way to incorporate this prototypical information in a deep learning framework.
Using prototypes as prior information, the deepnet pipeline learns the input
image projections into the prototypical embedding space subject to minimization
of the final classification loss. Based on our experiments with two different
datasets of traffic signs and brand logos, prototypical embeddings incorporated
in a conventional convolutional neural network improve the recognition
performance. Recognition accuracy on the Belga logo dataset is especially
noteworthy and establishes a new state-of-the-art. In zero-shot learning
scenarios, the same system can be directly deployed to draw inference on unseen
classes by simply adding the prototypical information for these new classes at
test time. Thus, unlike earlier approaches, testing on seen and unseen classes
is handled using the same pipeline, and the system can be tuned for a trade-off
of seen and unseen class performance as per task requirement. Comparison with
one of the latest works in the zero-shot learning domain yields top results on
the two datasets mentioned above.