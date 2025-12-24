---
title: Efficient Data-driven Perception with Event Cameras

event: Fall 2023 GRASP Seminar
event_url: https://example.org

location: GRASP Lab, University of Pennsylvania
#address:
#  street: 450 Serra Mall
#  city: Stanford
#  region: CA
#  postcode: '94305'
#  country: United States

summary: A talk discussing my work during my Ph.D.
abstract: 'Event cameras are bio-inspired sensors that perceive the environment in an entirely different way. Instead of measuring synchronous frames of absolute intensity at fixed intervals, they only measure changes in intensity and do this independently for each pixel, resulting in an asynchronous stream of events. Events thus carry only the compressed visual signal but do this with a micro-second-level latency and temporal resolution, negligible motion blur, and high dynamic range while consuming low power and using low bandwidth. However, due to their working principle, event cameras output sparse and asynchronous data, which are not directly compatible with standard computer vision algorithms designed for dense frames. Therefore the development of new algorithms to process events, and leverage the advantages of these cameras is at the forefront of active research in event-based vision. In this talk, we will discuss ways to leverage the advantages of event cameras for high-speed robotics, and low-data computational photography. Finally, we will touch upon ways to enhance the efficiency of deep learning-based algorithms with novel asynchronous neural networks that take advantage of the spatiotemporal sparsity in event data.'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2023-11-13T13:00:00Z'
#date_end: '2030-06-01T15:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2023-11-13T00:00:00Z'

authors:
  - Daniel Gehrig

tags: []

# Is this a featured talk? (true/false)
featured: True

image:
  ##caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

#links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: 'https://www.youtube.com/watch?v=O9ZjMJym7gc&t=1s&ab_channel=GRASPLab'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - example
---

