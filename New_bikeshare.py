import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
             'new york': 'new_york_city.csv', 'New York': 'new_york_city.csv',
             'washington': 'washington.csv', 'Washington': 'washington.csv'}


def get_filters():
    print("\n Welcome to the program")
    print('Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use       a while loop to handle invalid inputs

    # TO DO: get user input for month (all, january, february, ... , june)

    city = ''

    while city not in CITY_DATA.keys():
        print("\nlet's start with which data you want to choose from witch city ^_*")
        print("\n1. chicago. 2. New York. 3. Washington")
        print("\n**Warning** : The input should be Full name of the city (e.g. chicago) ")
        print("\nAnd feel free to write with upper case or lower ")
        print("\nThis is for the git project so ignore it sir ..")

        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nPlease Check your input")
            print("\nRestarting . . .  . ")

    print(f"\nYou have chosen {city.title()} as your city.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    MONTH_DATE = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}

    month = ''

    while month not in MONTH_DATE.keys():
        print("\nNow please choose month you want between January to June, for which your seeking for the data:  ")
        print("\n**Warning**: The input should be Full name of the month (e.g. april)")
        print("\nIf you wwant to see all data for all (month) please type (all)")
        print("\nbtw you can also write ALL, or All, or all .. ")
        month = input().lower()

        if month not in MONTH_DATE.keys():
            print("\nPlease Check your input")
            print("\nRestarting . . .  . ")
    print(f"\nYou have chosen {month.title()} as your month.")

    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week of you choice ..")
        print("\n**Warning**: The input should be Full name of the day (e.g. monday)")
        day = input().lower()
        if day not in DAY_LIST:
            print("\nWrongr answer, make sure of your input that it's acceptable")
            print("\nRestarting ....")
            print("\nGet some coffee ^_* ")

    print(f"\nYou chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city : {city.upper()}, month/s as {month.upper()} and day/s: {day.upper()}.")

    print('-' * 80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data for city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Month and day of week from start time to creat new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filtring ..
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print(f"Most popular month (1 = January, 2 = feburary, ... ): {popular_month}")

    popular_day = df['day_of_week'].mode()[0]
    print(f"\nMost Popular Day: {popular_day}")

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nMost Popular Start Time Hour: {popular_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used Start Station:{common_start_station}")

    common_end_station = df["End Station"].mode()[0]
    print(f"\nThe most commonly used end Satation: {common_end_station}")

    # Using str.cat to combin tow columns in the dataframe
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combination = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of trips are from: {combination} .")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time >>
    total_duration = df['Trip Duration'].sum()

    minute, second = divmod(total_duration, 60)

    hour, minute = divmod(minute, 60)
    print(f"\nThe total of the trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time >>
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe Average trip is {hrs} hourse, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe Average trip is {mins} minutes, {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users by number is : {user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users gender is: {gender}")
    except:
        print("\nThere is no 'Gender' column in this file !!! ")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mod()[0])
        print(f"\nThe earlist year of the birth is: {earliest}")
        print(f"\nThe most recent year of the birth is: {most_recent}")
        print(f"\nThe most common year of the birth is: {common_year}")
    except:
        print("There is no birth year in this file")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def display_data(df):
    """ This function to display 5 row from the csv ^_^"""
    RESPONSE_LIST = ['yes', 'no']
    data = ''
    counter = 0
    while data not in RESPONSE_LIST:
        print("\nDo you want see the first 5 row of data ??")
        print("\nIf you want to see it as I wish .. ")
        print("\nWrite Yes - yes, or No - no .")
        data = input().lower()
        if data == "yes":
            print(df.head(5))
        elif data not in RESPONSE_LIST:
            print("\nPlease Check what you write (: ")
            print("It's not look like what I ask you to write ?!")
            print("\nRestarting ....")
    while data == 'yes':
        print("Do you want see more data ??")
        counter += 5
        data = input().lower()
        # This will display the next 5 row >>
        if data == 'yes':
            print(df[counter:counter + 5])
        elif data != 'yes':
            print("\nsad to see you go ): ")
            print("\nI hope that was helpful, see you next time <3")

    print('-' * 80)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
