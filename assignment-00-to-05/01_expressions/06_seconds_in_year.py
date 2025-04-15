# Useful constants to help make the math easier and cleaner!
days_per_year:int = 365
hours_per_day:int = 24
min_per_hour:int = 60
sec_per_min:int = 60

def main():
    # We can get the number of seconds per year by multiplying the handy constants above!
    total_seconds_in_one_year:int = days_per_year * hours_per_day * min_per_hour * sec_per_min
    input_year:int = int(input("Enter a years to convert in seconds: "))
    how_many_years:int = total_seconds_in_one_year * input_year
    print(f"There are {how_many_years} seconds in {input_year} years(s)")



if __name__ == '__main__':
    main()