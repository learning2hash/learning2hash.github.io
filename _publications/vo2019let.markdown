---
layout: publication
title: Let's Transfer Transformations Of Shared Semantic Representations
authors: Nam Vo, Lu Jiang, James Hays
conference: Arxiv
year: 2019
bibkey: vo2019let
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.00793'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Nam Vo, Lu Jiang, James Hays
---
With a good image understanding capability, can we manipulate the images high
level semantic representation? Such transformation operation can be used to
generate or retrieve similar images but with a desired modification (for
example changing beach background to street background); similar ability has
been demonstrated in zero shot learning, attribute composition and attribute
manipulation image search. In this work we show how one can learn
transformations with no training examples by learning them on another domain
and then transfer to the target domain. This is feasible if: first,
transformation training data is more accessible in the other domain and second,
both domains share similar semantics such that one can learn transformations in
a shared embedding space. We demonstrate this on an image retrieval task where
search query is an image, plus an additional transformation specification (for
example: search for images similar to this one but background is a street
instead of a beach). In one experiment, we transfer transformation from
synthesized 2D blobs image to 3D rendered image, and in the other, we transfer
from text domain to natural image domain.