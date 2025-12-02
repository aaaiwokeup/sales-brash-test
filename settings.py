import json
import logging
import sqlite3
import argparse

from pathlib import Path


class Settings:
    
    def __init__(self) -> None:
        self._setup_logging()
        self._setup_db()
        self._load_json_files()
        self._init_argparser()

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S',
            )

        self.logging = logging

    def _setup_db(self):
        with sqlite3.connect('sales_brush_test.db') as connection:
            cursor = connection.cursor()

            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS daily_stats (
                    date DATE NOT NULL,
                    campaign_id TEXT NOT NULL,
                    spend FLOAT NOT NULL,
                    conversions INTEGER NOT NULL, 
                    cpa FLOAT,
                    PRIMARY KEY(date, campaign_id)
                    );
                '''
            )

            connection.commit()

    def _init_argparser(self):
        parser = argparse.ArgumentParser(description='SalesBrush test task')
        parser.add_argument('-s', '--start-date', help='write start date in ISO format (YYYY-MM-DD)')
        parser.add_argument('-e', '--end-date', help='write end date in ISO format (YYYY-MM-DD)')

        self.parser = parser

    def _load_json_files(self):
        base_path = Path(__file__).parent

        json_dir = base_path / 'jsons'
        json_files = [
            'fb_spend', 'network_conv'
        ]

        for json_name in json_files:
            file_path = json_dir / f'{json_name}.json'
            if not file_path.exists():
                raise FileNotFoundError(f'JSON file not found: {file_path}')

            with open(file_path) as f:
                setattr(self, json_name, json.load(f))

settings = Settings()
