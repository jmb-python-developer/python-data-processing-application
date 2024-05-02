# Will hold function to parse CLI arguments AND main() function to parse options and log statements
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import argparse
from csv_extract import *
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
def write_pairs_to_files(builders, target_files, row):
    for i, builder in enumerate(builders):
        pair = builder.from_row(row)
        json_data = json.dumps(asdict(pair)) + '\n'
        target_files[i].write(json_data)

def main(argv: list[str] = ["-o", "target", "data/data1.csv"]) -> None:
    builders = [cls() for cls in BUILDER_CLASSES]
    extractor = EXTRACT_CLASS(builders)

    options = get_options(argv)

    targets = [
        options.output / f"Series_{i+1}.ndjson" for i in range(len(builders))
    ]

    target_files = [target.open('w') for target in targets]

    with options.source[0].open() as source:
        rdr = csv.reader(source)
        for row in rdr:
            write_pairs_to_files(extractor.builders, target_files, row)

    for target in target_files:
        target.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
