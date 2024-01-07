# Daun Daun No Mi

Download selected chapters from One Piece Ex for offline reading and/or Kindle conversion.

- `scraper.py` uses Selenium to access the website and index the image sources for all the desired pages, grouping by chapter and saving into `image_urls.json`.
- `downloader.py` reads from `image_urls.json` and downloads the desired chapters.
