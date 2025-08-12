---
layout: publication
title: 'Mapexif: An Image Scanning And Mapping Tool For Investigators'
authors: Lionel Prat, Nhien-An Le-Khac, Cheryl Baker
conference: Arxiv
year: 2017
bibkey: prat2017mapexif
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.09827'}]
tags: ["Evaluation"]
short_authors: Lionel Prat, Nhien-An Le-Khac, Cheryl Baker
---
Recently, the integration of geographical coordinates into a picture has
become more and more popular. Indeed almost all smartphones and many cameras
today have a built-in GPS receiver that stores the location information in the
Exif header when a picture is taken. Although the automatic embedding of
geotags in pictures is often ignored by smart phone users as it can lead to
endless discussions about privacy implications, these geotags could be really
useful for investigators in analysing criminal activity. Currently, there are
many free tools as well as commercial tools available in the market that can
help computer forensics investigators to cover a wide range of geographic
information related to criminal scenes or activities. However, there are not
specific forensic tools available to deal with the geolocation of pictures
taken by smart phones or cameras. In this paper, we propose and develop an
image scanning and mapping tool for investigators. This tool scans all the
files in a given directory and then displays particular photos based on
optional filters (date, time, device, localisation) on Google Map. The file
scanning process is not based on the file extension but its header. This tool
can also show efficiently to users if there is more than one image on the map
with the same GPS coordinates, or even if there are images with no GPS
coordinates taken by the same device in the same timeline. Moreover, this new
tool is portable; investigators can run it on any operating system without any
installation. Another useful feature is to be able to work in a read-only
environment, so that forensic results will not be modified. We also present and
evaluate this tool real world application in this paper.