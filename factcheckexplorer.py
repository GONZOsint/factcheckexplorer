import requests
import json
import csv
from datetime import datetime
import re

class FactCheckLib:
    def __init__(self, query, language=None, num_results=100, csv_filename=None):
        self.query = query
        self.language = language
        self.num_results = num_results
        self.csv_filename = csv_filename if csv_filename else f"{self._sanitize_query_for_filename(query)}.csv"
        self.url = 'https://toolbox.google.com/factcheck/api/search'
        self.params = {
            'num_results': str(self.num_results),
            'force': 'false',
            'offset': '0',
            'query': self.query,
        }
        if language and language.lower() != 'all':
            self.params['hl'] = self.language
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json, text/plain, */*',
        }

    def _sanitize_query_for_filename(self, query):
        sanitized_query = re.sub(r'\W+', '_', query)
        return sanitized_query

    def fetch_data(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    @staticmethod
    def clean_json(raw_json):
        try:
            return json.loads(raw_json.lstrip(")]}'\n"))
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            return []

    def extract_info(self, data):
        if not data or not isinstance(data, list) or not data[0]:
            return []
        parsed_claims = []
        tag_mapping = {tag[0]: tag[1] for tag in data[0][2]}
        for claim in data[0][1]:
            claim_details = self._parse_claim(claim, tag_mapping)
            if claim_details:
                parsed_claims.append(claim_details)
        return parsed_claims

    @staticmethod
    def _parse_claim(claim, tag_mapping):
        try:
            claim_text = claim[0][0] if claim[0] else None
            source_details = claim[0][3][0] if claim[0][3] else None
            source_name = source_details[0][0] if source_details and source_details[0] else None
            source_url = source_details[1] if source_details else None
            verdict = source_details[3] if source_details else None
            review_publication_date = source_details[11] if source_details and len(source_details) > 11 else None
            image_url = claim[1] if len(claim) > 1 else None
            claim_tags = claim[0][8] if claim[0] and len(claim[0]) > 8 and claim[0][8] else []
            tags = [tag_mapping[tag[0]] for tag in claim_tags if tag[0] in tag_mapping]
            if review_publication_date:
                review_publication_date = datetime.utcfromtimestamp(review_publication_date).strftime('%Y-%m-%d %H:%M:%S')
            return {
                "Claim": claim_text,
                "Source Name": source_name,
                "Source URL": source_url,
                "Verdict": verdict,
                "Review Publication Date": review_publication_date,
                "Image URL": image_url,
                "Tags": tags
            }
        except Exception as e:
            print(f"Error parsing claim: {e}")
            return None

    def convert_to_csv(self, data):
        if not data:
            print("No data to save.")
            return
        with open(self.csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def process(self):
        raw_json = self.fetch_data()
        if raw_json:
            cleaned_json = self.clean_json(raw_json)
            extracted_info = self.extract_info(cleaned_json)
            if extracted_info:
                self.convert_to_csv(extracted_info)