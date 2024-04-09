# FactCheckExplorer Python Library 📚

The FactCheckExplorer library provides an easy-to-use Python interface for querying and fetching fact-checking data from Google's Fact Check Explorer tool. This library bypasses the typical front-end limitations, allowing users to retrieve an extensive range of fact-checked claims based on their search criteria.

## Features 🌟

- **Customizable Queries**:  Execute searches using specific keywords, with the ability to filter results by language using standard language codes (e.g., "en" for English, "es" for Spanish).
- **Extended Results**: Bypass the typical limits to fetch up to 10,000 results, providing more comprehensive datasets for analysis.
- **Data Extraction**: Parse the fetched data automatically into structured information for ease of use.
- **CSV Export**: Directly convert and save the data into a CSV file for offline analysis or archiving.

## Installation 🛠️

You can install the FactCheckExplorer library directly from GitHub. Ensure you have `git` and `pip` installed on your machine, then run the following command:

```bash
pipx install git+https://github.com/GONZOsint/factcheckexplorer.git
```

## Quick Start 🚀

Here's how to quickly get started with the FactCheckExplorer library:

```python
from factcheckexplorer import FactCheckLib

# Initialize the library with your query and desired settings
fact_check = FactCheckLib(query="global warming", language="en", num_results=200)

# Fetch the data
fact_check.process()

# Check the CSV file in your directory for the output
```

## Documentation 📖
FactCheckLib Class

    Parameters:
        query: The search query to fetch fact checks for.
        language: (Optional) Language filter for the results, defaults to None (all languages).
        num_results: (Optional) The number of results to fetch, defaults to 100.
        csv_filename: (Optional) The filename for the CSV output, automatically generated if not provided.

    Methods:
        process(): Executes the query and saves the data into a CSV file.
        fetch_data(): Fetches raw data from Google's Fact Check API.
        clean_json(raw_json): Cleans and decodes the JSON response.
        extract_info(data): Parses the cleaned JSON data into structured information.
        convert_to_csv(data): Converts the extracted information into a CSV file.


## Contributing 🤝

Contributions to the FactCheckExplorer library are welcome! Whether it's enhancing functionality, improving documentation, or reporting bugs, please feel free to contribute. Check out our Contributing Guide for more details on making contributions.


## License 📄

The FactCheckExplorer Python Library is licensed under the MIT License. See the LICENSE file for more details.
