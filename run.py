import sqlite3
from datetime import datetime

from settings import settings


def main():
    with sqlite3.connect('sales_brush_test.db') as connection:
        settings.logging.info(f'Connected to sales_brush_test.db')

        args = settings.parser.parse_args()

        if args.start_date != None:
            start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date().isoformat()
            end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date().isoformat()

            settings.logging.info(f'Start date argument: {start_date} | End date argument: {end_date}')
        else:
            settings.logging.warning('No start-end arguments passed. Using default values')

        cursor = connection.cursor()
        upsert_query = '''
        INSERT INTO daily_stats(date, campaign_id, spend, conversions, cpa)
        VALUES(?, ?, ?, ?, ?)
        ON CONFLICT(date, campaign_id) DO UPDATE SET spend=excluded.spend, conversions=excluded.conversions, cpa=excluded.cpa;
        '''

        data_fb = list()
        data_network = list()

        for fb in settings.fb_spend:
            date = fb['date']
            if start_date <= date <= end_date:
                data_fb.append(fb)
    
        for network in settings.network_conv:
            date = network['date']
            if start_date <= date <= end_date:
                data_network.append(network)

        for i in range(len(data_fb)):
            if data_fb[i]['date'] == data_network[i]['date'] and data_fb[i]['campaign_id'] == data_network[i]['campaign_id']:
                data = data_fb[i] | data_network[i]

                try:
                    cpa = data['spend'] / data['conversions']
                except ZeroDivisionError:
                    cpa = None

                upsert_values = (data['date'], data['campaign_id'], data['spend'], data['conversions'], round(cpa, 2))

                cursor.execute(upsert_query, upsert_values)        
                settings.logging.info(f'daily_stats table upserted with: {upsert_values}')

        connection.commit()
        settings.logging.info(f'Changes committed to sales_brush_test.db')


if __name__ == "__main__":
    main()