# News-text analysis coursework

AUSCI 135 group assignment, April 2023: count Canadian province/territory mentions, country mentions, and repeated words in fetched news HTML. Original authorship is preserved: **Zlata Mstyslavska — Part A; Vadim Rudenko — Part B and integration; Harsh Darji — Part C.** The [original assignment brief](docs/assignment.md) remains available.

## Local checks

Use Python 3.12 and `pip install -r requirements.txt`, then `python -m unittest discover -s tests -v`. Checks use local text and mocked HTTP responses; importing `main` no longer starts a scrape. No live publisher requests are required for tests.

`python main.py` is the historical network-enabled entry point. It requests CBC and Windspeaker pages; use it only after checking permission and current site policies. No scheduled scraping or hosted service is included.

## Scope

`main.py` combines the exercises; the separately named files retain the original component submissions. This is simple regular-expression/text-processing coursework, not a robust news analytics pipeline: HTML structure, abbreviation matching, case handling, alias normalization, and short/empty lists can affect results. Current publisher compatibility and accuracy are not claimed. The preserved Part C includes historical heuristic limitations rather than a modern language-processing model.
