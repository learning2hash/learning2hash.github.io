---
layout: publication
title: 'Bitup: Efficient Bitmap Data Storage Solution For User Profile'
authors: Derong Tang, Hank Wang
conference: Arxiv
year: 2023
bibkey: tang2023bitup
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.17990'}]
tags: ["Efficiency"]
short_authors: Derong Tang, Hank Wang
---
User profile is widely used in the internet consumer industry, it can be used
in recommendation systems for better user experience, or improving Ads system
with better conversion rate. Most internet situation we must met large scale
data set, thus retrieve efficient and store with less space became a challenge,
how to handle trillions rows of data is very common in our business scene, so
we proposed a novel solution called BitUP, involved the new distributed bitmap
structure to efficient store profile label data, and can querying with better
performance, the fundamental structure is bitmap, that is why our method is
efficient and less storage overhead. Our design can also scale linearly, to
demonstrate the scalability of the proposed solution we show retrieval
efficiency in various industry data, which scales across from terabytes to
petabytes.