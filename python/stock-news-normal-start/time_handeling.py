from datetime import datetime, timedelta

class TimeHandling:

    def __init__(self, data):
        self.data = data
        self.time_dely = 1

    def check_last_day_in_list(self):
        # Get the last refreshed date
        last_refreshed_str = self.data['Meta Data']['3. Last Refreshed']
        # Convert the string to a datetime object
        last_refreshed_date = datetime.strptime(last_refreshed_str, '%Y-%m-%d')
        # Check if the last refreshed date is a trading day, if not, find the previous trading day
        return self.get_previous_trading_day(last_refreshed_date)

    def get_previous_trading_day(self, target_date):
        # Convert target_date to string in 'YYYY-MM-DD' format
        target_date_str = target_date.strftime('%Y-%m-%d')
        while target_date_str not in self.data['Time Series (Daily)']:
            target_date -= timedelta(days=1)
            target_date_str = target_date.strftime('%Y-%m-%d')
        return target_date

    def get_data_for_date_closing_time(self, target_date):
        # Ensure the date is a trading day
        valid_date = self.get_previous_trading_day(target_date)
        valid_date_str = valid_date.strftime('%Y-%m-%d')
        # Return the closing time for that date
        return self.data['Time Series (Daily)'][valid_date_str]['4. close']


