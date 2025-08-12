---
layout: publication
title: 'Helpful Neighbors: Leveraging Neighbors In Geographic Feature Pronunciation'
authors: Llion Jones, Richard Sproat, Haruko Ishikawa, Alexander Gutkin
conference: Transactions of the Association for Computational Linguistics
year: 2023
bibkey: jones2022helpful
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.10200'}]
tags: ["TACL"]
short_authors: Jones et al.
---
If one sees the place name Houston Mercer Dog Run in New York, how does one
know how to pronounce it? Assuming one knows that Houston in New York is
pronounced "how-ston" and not like the Texas city, then one can probably guess
that "how-ston" is also used in the name of the dog park. We present a novel
architecture that learns to use the pronunciations of neighboring names in
order to guess the pronunciation of a given target feature. Applied to Japanese
place names, we demonstrate the utility of the model to finding and proposing
corrections for errors in Google Maps.
  To demonstrate the utility of this approach to structurally similar problems,
we also report on an application to a totally different task: Cognate reflex
prediction in comparative historical linguistics. A version of the code has
been open-sourced
(https://github.com/google-research/google-research/tree/master/cognate_inpaint_neighbors).