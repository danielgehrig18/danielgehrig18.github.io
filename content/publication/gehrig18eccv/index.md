---
title: "Asynchronous, Photometric Feature Tracking using Events and Frames"
authors:
- Daniel Gehrig
- Henri Rebecq
- Guillermo Gallego
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
##date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2018-09-08T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*European Conf. on Computer Vision (ECCV)*"
publication_short: ""

abstract: We present a method that leverages the complementarity of event cameras and standard cameras to track visual features with lowlatency. Event cameras are novel sensors that output pixel-level brightness changes, called “events”. They offer significant advantages over standard cameras, namely a very high dynamic range, no motion blur, and a latency in the order of microseconds. However, because the same scene pattern can produce different events depending on the motion direction, establishing event correspondences across time is challenging. By contrast, standard cameras provide intensity measurements (frames) that do not depend on motion direction. Our method extracts features on frames and subsequently tracks them asynchronously using events, thereby exploiting the best of both types of data. The frames provide a photometric representation that does not depend on motion direction and the events provide low-latency updates. In contrast to previous works, which are based on heuristics, this is the first principled method that uses raw intensity measurements directly, based on a generative event model within a maximum-likelihood framework. As a result, our method produces feature tracks that are both more accurate (subpixel accuracy) and longer than the state of the art, across a wide variety of scenes.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/ECCV18_Gehrig.pdf
url_code: 'https://github.com/uzh-rpg/rpg_eklt'
url_dataset: ''
url_poster: 'https://rpg.ifi.uzh.ch/docs/ECCV18_Gehrig_poster.pdf'
url_project: ''
url_slides: 'https://youtu.be/7EvY8SxdLl8'
url_source: ''
url_video: 'https://youtu.be/A7UfeUnG6c4'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
This paper lead to an oral at ECCV 2018 and was invited to a journal extension by IJCV. 
{{% /callout %}}
