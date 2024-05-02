# Will hold function to parse CLI arguments AND main() function to parse options and log statements
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import argparse
from src.csv_extract import *
from dataclasses import asdict
import json
from pathlib import Path
import csv

def get_options(argv: list[str]) -> argparse.Namespace:
    # default args serve as default dependency injection target classes
    defaults = argparse.Namespace(
        extract_class = Extract,
        series_classes = [Series1PairBuilder, Series2PairBuilder, Series3PairBuilder, Series4PairBuilder]
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, default="data")
    parser.add_argument('source', type=Path, nargs='*', default="/data/data1.csv")
    return parser.parse_args(argv, defaults)


EXTRACT_CLASS: type[Extract] = Extract
BUILDER_CLASSES: list[type[PairBuilder]] = [Series1PairBuilder, Series2PairBuilder, Series3PairBuilder, Series4PairBuilder]

def main(argv: list[str]) -> None:
    builders = [cls for cls in BUILDER_CLASSES]
    extractor = EXTRACT_CLASS(builders)

    options = get_options(argv)

    targets = [
        options.output / "Series_1.ndjson",
        options.output / "Series_2.ndjson",
        options.output / "Series_3.ndjson",
        options.output / "Series_4.ndjson",
    ]

    target_files = [
        target.open('w') for target in targets
    ]

    for source in options.source:
        # source can default
        with source.open() as source:
            rdr = csv.reader(source)
            for row in rdr:
                #zip yields Tuples until input is exhausted
                for pair, wtr in zip(extractor.build_pairs(row), target_files):
                    wtr.write(json.dumps(asdict(pair)) + '\n')
    
    for target in target_files:
        target.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # calls main logic
    args = ["-o", "target", "data/data1.csv"]
    main(args)
