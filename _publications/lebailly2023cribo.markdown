---
layout: publication
title: 'Cribo: Self-supervised Learning Via Cross-image Object-level Bootstrapping'
authors: "Tim Lebailly, Thomas Stegm\xFCller, Behzad Bozorgtabar, Jean-Philippe Thiran,\
  \ Tinne Tuytelaars"
conference: Arxiv
year: 2023
bibkey: lebailly2023cribo
citations: 0
additional_links: [{name: Code, url: 'https://github.com/tileb1/CrIBo.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2310.07855'}]
tags: [Self-Supervised, Datasets, Supervised, Evaluation]
short_authors: Lebailly et al.
---
Leveraging nearest neighbor retrieval for self-supervised representation
learning has proven beneficial with object-centric images. However, this
approach faces limitations when applied to scene-centric datasets, where
multiple objects within an image are only implicitly captured in the global
representation. Such global bootstrapping can lead to undesirable entanglement
of object representations. Furthermore, even object-centric datasets stand to
benefit from a finer-grained bootstrapping approach. In response to these
challenges, we introduce a novel Cross-Image Object-Level Bootstrapping method
tailored to enhance dense visual representation learning. By employing
object-level nearest neighbor bootstrapping throughout the training, CrIBo
emerges as a notably strong and adequate candidate for in-context learning,
leveraging nearest neighbor retrieval at test time. CrIBo shows
state-of-the-art performance on the latter task while being highly competitive
in more standard downstream segmentation tasks. Our code and pretrained models
are publicly available at https://github.com/tileb1/CrIBo.