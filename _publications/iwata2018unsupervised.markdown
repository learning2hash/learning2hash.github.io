---
layout: publication
title: Unsupervised Object Matching For Relational Data
authors: Tomoharu Iwata, Naonori Ueda
conference: Arxiv
year: 2018
bibkey: iwata2018unsupervised
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.03770'}]
tags: ["Unsupervised"]
short_authors: Tomoharu Iwata, Naonori Ueda
---
We propose an unsupervised object matching method for relational data, which
finds matchings between objects in different relational datasets without
correspondence information. For example, the proposed method matches documents
in different languages in multi-lingual document-word networks without
dictionaries nor alignment information. The proposed method assumes that each
object has latent vectors, and the probability of neighbor objects is modeled
by the inner-product of the latent vectors, where the neighbors are generated
by short random walks over the relations. The latent vectors are estimated by
maximizing the likelihood of the neighbors for each dataset. The estimated
latent vectors contain hidden structural information of each object in the
given relational dataset. Then, the proposed method linearly projects the
latent vectors for all the datasets onto a common latent space shared across
all datasets by matching the distributions while preserving the structural
information. The projection matrix is estimated by minimizing the distance
between the latent vector distributions with an orthogonality regularizer. To
represent the distributions effectively, we use the kernel embedding of
distributions that hold high-order moment information about a distribution as
an element in a reproducing kernel Hilbert space, which enables us to calculate
the distance between the distributions without density estimation. The
structural information encoded in the latent vectors are preserved by using the
orthogonality regularizer. We demonstrate the effectiveness of the proposed
method with experiments using real-world multi-lingual document-word relational
datasets and multiple user-item relational datasets.