---
layout: publication
title: Camera-based Piano Sheet Music Identification
authors: Daniel Yang, Tj Tsai
conference: Arxiv
year: 2020
citations: 0
bibkey: yang2020camera
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.14579'}]
tags: [Applications, Hashing Methods, Evaluation Metrics, Tools and Libraries]
---
This paper presents a method for large-scale retrieval of piano sheet music
images. Our work differs from previous studies on sheet music retrieval in two
ways. First, we investigate the problem at a much larger scale than previous
studies, using all solo piano sheet music images in the entire IMSLP dataset as
a searchable database. Second, we use cell phone images of sheet music as our
input queries, which lends itself to a practical, user-facing application. We
show that a previously proposed fingerprinting method for sheet music retrieval
is far too slow for a real-time application, and we diagnose its shortcomings.
We propose a novel hashing scheme called dynamic n-gram fingerprinting that
significantly reduces runtime while simultaneously boosting retrieval accuracy.
In experiments on IMSLP data, our proposed method achieves a mean reciprocal
rank of 0.85 and an average runtime of 0.98 seconds per query.