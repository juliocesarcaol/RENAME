# FASTA Identifier Replacement Tool

## Overview
This Python script is designed to parse a TSV (tab-separated values) file containing identifiers and their corresponding values and use this information to replace identifiers in a FASTA file. It is particularly useful for researchers working with genomic data who need to update identifiers in their FASTA files based on information from associated TSV files.

## Features
- **Identifier Parsing**: The script parses a TSV file to extract identifiers and their associated values.
- **Identifier Replacement**: It searches for matching identifiers in a FASTA file and replaces them with new identifiers based on the information from the TSV file.
- **Output Generation**: The modified FASTA file with replaced identifiers is saved as a new file.

## Usage
1. **Input File Paths**: Provide the paths to the TSV and FASTA files when prompted.
2. **Parsing and Replacement**: The script parses the TSV file to extract identifiers and their values, then searches for matching identifiers in the FASTA file and replaces them with new identifiers.
3. **Output**: A new FASTA file with modified identifiers is generated.

## Getting Started
1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the script and follow the prompts to provide the paths to the TSV and FASTA files.

## Requirements
- Python 3.x
- `csv` module

## License
This project is licensed under the BSD3 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the contributors and maintainers of the `csv` module.
