---
layout: publication
title: Transit Node Routing Reconsidered
authors: Julian Arz, Dennis Luxen, Peter Sanders
conference: Lecture Notes in Computer Science
year: 2013
bibkey: arz2013transit
citations: 53
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1302.5611'}]
tags: ["Efficiency"]
short_authors: Julian Arz, Dennis Luxen, Peter Sanders
---
Transit Node Routing (TNR) is a fast and exact distance oracle for road
networks. We show several new results for TNR. First, we give a surprisingly
simple implementation fully based on Contraction Hierarchies that speeds up
preprocessing by an order of magnitude approaching the time for just finding a
CH (which alone has two orders of magnitude larger query time). We also develop
a very effective purely graph theoretical locality filter without any
compromise in query times. Finally, we show that a specialization to the online
many-to-one (or one-to-many) shortest path further speeds up query time by an
order of magnitude. This variant even has better query time than the fastest
known previous methods which need much more space.