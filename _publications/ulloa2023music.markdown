---
layout: publication
title: Music Recommendation Based On Audio Fingerprint
authors: "Diego Salda\xF1a Ulloa"
conference: Arxiv
year: 2023
bibkey: ulloa2023music
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.17655'}]
tags: ["Recommender Systems"]
short_authors: "Diego Salda\xF1a Ulloa"
---
This work combined different audio features to obtain a more robust
fingerprint to be used in a music recommendation process. The combination of
these methods resulted in a high-dimensional vector. To reduce the number of
values, PCA was applied to the set of resulting fingerprints, selecting the
number of principal components that corresponded to an explained variance of
\(95%\). Finally, with these PCA-fingerprints, the similarity matrix of each
fingerprint with the entire data set was calculated. The process was applied to
200 songs from a personal music library; the songs were tagged with the
artists' corresponding genres. The recommendations (fingerprints of songs with
the closest similarity) were rated successful if the recommended songs' genre
matched the target songs' genre. With this procedure, it was possible to obtain
an accuracy of \(89%\) (successful recommendations out of total recommendation
requests).