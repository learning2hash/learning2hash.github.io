---
layout: publication
title: Automatic Construction Of A Large-scale Corpus For Geoparsing Using Wikipedia
  Hyperlinks
authors: Keyaki Ohno, Hirotaka Kameko, Keisuke Shirai, Taichi Nishimura, Shinsuke
  Mori
conference: Arxiv
year: 2024
bibkey: ohno2024automatic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.16483'}]
tags: ["Scalability"]
short_authors: Ohno et al.
---
Geoparsing is the task of estimating the latitude and longitude (coordinates)
of location expressions in texts. Geoparsing must deal with the ambiguity of
the expressions that indicate multiple locations with the same notation. For
evaluating geoparsing systems, several corpora have been proposed in previous
work. However, these corpora are small-scale and suffer from the coverage of
location expressions on general domains. In this paper, we propose Wikipedia
Hyperlink-based Location Linking (WHLL), a novel method to construct a
large-scale corpus for geoparsing from Wikipedia articles. WHLL leverages
hyperlinks in Wikipedia to annotate multiple location expressions with
coordinates. With this method, we constructed the WHLL corpus, a new
large-scale corpus for geoparsing. The WHLL corpus consists of 1.3M articles,
each containing about 7.8 unique location expressions. 45.6% of location
expressions are ambiguous and refer to more than one location with the same
notation. In each article, location expressions of the article title and those
hyperlinks to other articles are assigned with coordinates. By utilizing
hyperlinks, we can accurately assign location expressions with coordinates even
with ambiguous location expressions in the texts. Experimental results show
that there remains room for improvement by disambiguating location expressions.