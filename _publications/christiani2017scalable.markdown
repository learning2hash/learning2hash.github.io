---
layout: publication
title: Scalable and robust set similarity join
authors: Christiani Tobias, Pagh Rasmus, Sivertsen Johan
conference: "Arxiv"
year: 2017
bibkey: christiani2017scalable
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1707.06814"}
tags: ['ARXIV']
---
Set similarity join is a fundamental and well-studied database operator. It is usually studied in the exact setting where the goal is to compute all pairs of sets that exceed a given similarity threshold (measured e.g. as Jaccard similarity). But set similarity join is often used in settings where 100% recall may not be important --- indeed, where the exact set similarity join is itself only an approximation of the desired result set. We present a new randomized algorithm for set similarity join that can achieve any desired recall up to 100%, and show theoretically and empirically that it significantly improves on existing methods. The present state-of-the-art exact methods are based on prefix-filtering, the performance of which depends on the data set having many rare tokens. Our method is robust against the absence of such structure in the data. At 90% recall our algorithm is often more than an order of magnitude faster than state-of-the-art exact methods, depending on how well a data set lends itself to prefix filtering. Our experiments on benchmark data sets also show that the method is several times faster than comparable approximate methods. Our algorithm makes use of recent theoretical advances in high-dimensional sketching and indexing that we believe to be of wider relevance to the data engineering community.
