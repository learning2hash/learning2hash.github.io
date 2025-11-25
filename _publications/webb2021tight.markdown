---
layout: publication
title: Tight Lower Bounds For Dynamic Time Warping
authors: Geoffrey I. Webb, Francois Petitjean
conference: Pattern Recognition
year: 2021
bibkey: webb2021tight
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.07076'}]
tags: ["Efficiency", "Similarity Search"]
short_authors: Geoffrey I. Webb, Francois Petitjean
---
Dynamic Time Warping (DTW) is a popular similarity measure for aligning and
comparing time series. Due to DTW's high computation time, lower bounds are
often employed to screen poor matches. Many alternative lower bounds have been
proposed, providing a range of different trade-offs between tightness and
computational efficiency. LB Keogh provides a useful trade-off in many
applications. Two recent lower bounds, LB Improved and LB Enhanced, are
substantially tighter than LB Keogh. All three have the same worst case
computational complexity - linear with respect to series length and constant
with respect to window size. We present four new DTW lower bounds in the same
complexity class. LB Petitjean is substantially tighter than LB Improved, with
only modest additional computational overhead. LB Webb is more efficient than
LB Improved, while often providing a tighter bound. LB Webb is always tighter
than LB Keogh. The parameter free LB Webb is usually tighter than LB Enhanced.
A parameterized variant, LB Webb Enhanced, is always tighter than LB Enhanced.
A further variant, LB Webb*, is useful for some constrained distance functions.
In extensive experiments, LB Webb proves to be very effective for nearest
neighbor search.