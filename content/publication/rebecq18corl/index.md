---
title: "ESIM: an Open Event Camera Simulator"
authors:
- Henri Rebecq
- Daniel Gehrig
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2018-10-29T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*Conference on Robot Learning (CoRL), 2018.*"
publication_short: ""

abstract: "Event cameras measure changes of intensity asynchronously, in the form of a stream of events, which encode per-pixel brightness changes. In the last few years, their outstanding properties (asynchronous sensing, no motion blur, high dynamic range) have led to exciting vision applications, with very low-latency and high robustness. However, these sensors are still scarce and expensive to get, slowing down progress of the research community. To address these issues, there is a huge demand for cheap, high-quality synthetic, labeled event for algorithm prototyping, deep learning and algorithm benchmarking. The development of such a simulator, however, is not trivial since event cameras work fundamentally differently from frame-based cameras. We present the first event camera simulator that can generate a large amount of reliable event data. The key component of our simulator is a theoretically sound, adaptive rendering scheme that only samples frames when necessary, through a tight coupling between the rendering engine and the event simulator. We release ESIM as open source." 

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CORL18_Rebecq.pdf
url_code: 'https://rpg.ifi.uzh.ch/esim/index.html'
url_dataset: ''
url_poster: ''
url_project: 'https://rpg.ifi.uzh.ch/esim/index.html'
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/ytKOIX_2clo'

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
