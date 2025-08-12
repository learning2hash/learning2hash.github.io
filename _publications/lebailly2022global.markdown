---
layout: publication
title: Global-local Self-distillation For Visual Representation Learning
authors: Tim Lebailly, Tinne Tuytelaars
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: lebailly2022global
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.14676'}]
tags: ["Self-Supervised"]
short_authors: Tim Lebailly, Tinne Tuytelaars
---
The downstream accuracy of self-supervised methods is tightly linked to the
proxy task solved during training and the quality of the gradients extracted
from it. Richer and more meaningful gradients updates are key to allow
self-supervised methods to learn better and in a more efficient manner. In a
typical self-distillation framework, the representation of two augmented images
are enforced to be coherent at the global level. Nonetheless, incorporating
local cues in the proxy task can be beneficial and improve the model accuracy
on downstream tasks. This leads to a dual objective in which, on the one hand,
coherence between global-representations is enforced and on the other,
coherence between local-representations is enforced. Unfortunately, an exact
correspondence mapping between two sets of local-representations does not exist
making the task of matching local-representations from one augmentation to
another non-trivial. We propose to leverage the spatial information in the
input images to obtain geometric matchings and compare this geometric approach
against previous methods based on similarity matchings. Our study shows that
not only 1) geometric matchings perform better than similarity based matchings
in low-data regimes but also 2) that similarity based matchings are highly
hurtful in low-data regimes compared to the vanilla baseline without local
self-distillation. The code is available at
https://github.com/tileb1/global-local-self-distillation.