---
layout: publication
title: 'Gone In Six Characters: Short Urls Considered Harmful For Cloud Services'
authors: Martin Georgiev, Vitaly Shmatikov
conference: Arxiv
year: 2016
bibkey: georgiev2016gone
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.02734'}]
tags: []
short_authors: Martin Georgiev, Vitaly Shmatikov
---
Modern cloud services are designed to encourage and support collaboration. To
help users share links to online documents, maps, etc., several services,
including cloud storage providers such as Microsoft OneDrive and mapping
services such as Google Maps, directly integrate URL shorteners that convert
long, unwieldy URLs into short URLs, consisting of a domain such as 1drv.ms or
goo.gl and a short token.
  In this paper, we demonstrate that the space of 5- and 6-character tokens
included in short URLs is so small that it can be scanned using brute-force
search. Therefore, all online resources that were intended to be shared with a
few trusted friends or collaborators are effectively public and can be accessed
by anyone. This leads to serious security and privacy vulnerabilities.
  In the case of cloud storage, we focus on Microsoft OneDrive. We show how to
use short-URL enumeration to discover and read shared content stored in the
OneDrive cloud, including even files for which the user did not generate a
short URL. 7% of the OneDrive accounts exposed in this fashion allow anyone to
write into them. Since cloud-stored files are automatically copied into users'
personal computers and devices, this is a vector for large-scale, automated
malware injection.
  In the case of online maps, we show how short-URL enumeration reveals the
directions that users shared with each other. For many individual users, this
enables inference of their residential addresses, true identities, and
extremely sensitive locations they visited that, if publicly revealed, would
violate medical and financial privacy.