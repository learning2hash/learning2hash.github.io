---
layout: publication
title: 'Cufinufft: A Load-balanced GPU Library For General-purpose Nonuniform Ffts'
authors: "Yu-Hsuan Shih, Garrett Wright, Joakim And\xE9n, Johannes Blaschke, Alex\
  \ H. Barnett"
conference: 2021 IEEE International Parallel and Distributed Processing Symposium
  Workshops (IPDPSW)
year: 2021
bibkey: shih2021cufinufft
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.08463'}]
tags: ["Efficiency", "Tools & Libraries"]
short_authors: Shih et al.
---
Nonuniform fast Fourier transforms dominate the computational cost in many
applications including image reconstruction and signal processing. We thus
present a general-purpose GPU-based CUDA library for type 1 (nonuniform to
uniform) and type 2 (uniform to nonuniform) transforms in dimensions 2 and 3,
in single or double precision. It achieves high performance for a given
user-requested accuracy, regardless of the distribution of nonuniform points,
via cache-aware point reordering, and load-balanced blocked spreading in shared
memory. At low accuracies, this gives on-GPU throughputs around \(10^9\)
nonuniform points per second, and (even including host-device transfer) is
typically 4-10\(\times\) faster than the latest parallel CPU code FINUFFT (at 28
threads). It is competitive with two established GPU codes, being up to
90\(\times\) faster at high accuracy and/or type 1 clustered point distributions.
Finally we demonstrate a 5-12\(\times\) speedup versus CPU in an X-ray
diffraction 3D iterative reconstruction task at \(10^\{-12\}\) accuracy, observing
excellent multi-GPU weak scaling up to one rank per GPU.