class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        def days_before_year(year):
            # Total days till previous year
            return year * 365 + year//4 - year//100 + year//400
        
        def days_in_month(month, year):
            days = [31, 28, 31, 30, 31, 30, 
                    31, 31, 30, 31, 30, 31]
            
            if month == 2 and is_leap(year):
                return 29
            return days[month - 1]
        
        def total_days(date):
            year, month, day = map(int, date.split('-'))
            
            # Days till last year
            days = days_before_year(year - 1)
            
            # Add days of current year
            for m in range(1, month):
                days += days_in_month(m, year)
            
            # Add days
            days += day
            
            return days
        
        return abs(total_days(date1) - total_days(date2))