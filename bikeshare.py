import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
        """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_city = False
    valid_month = False
    valid_day = False

    while not valid_city:

        city = input("Would you like to see the data for Chicago, New York or Washington?\n").title()

        if city == 'Chicago'  or city == 'New York' or city == 'Washington':
            valid_city = True
        else :
            print("That's an invalid input. Let\'s try again.\n") 

    while not valid_month:
    # get user input for month (all, january, february, ... , june)
        month_filter = input("Would you like to filter data by month? Type \"yes\" or \"no\"\n").title()

        if month_filter == "Yes":    
            month = input("Which month? January, February, March, April, May or June?\n").title()
            valid_month = True
            
        elif month_filter == "No":
            print("\nOkay. Will show data for all months.\n")
            valid_month = True
            month = "All"    
            
        else :
            print("\nThat's an invalid input. Let\'s try again.\n")   
        
    while not valid_day:
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("\nWhich day of the week would you like to filter by? Type \"All\" if you want to see data for all days \n").title()

        if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or day == "Sunday" or day == "All":    
            valid_day = True
            
        else :
            print("\nThat's an invalid input. Let\'s try again.\n")   
    return city, month, day
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    # extract month and day of week from Start Time to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'All':
    # use the index of the months list to get the corresponding int
        month = Months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
       """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    modes = df.mode()
    # display the most common month  \
    most_common_month = int(modes['month'][0])  
    print("The most common month is: ", Months[most_common_month-1])

    # display the most common day of week
    print("The most common day of week is: ", modes['day_of_week'][0])

    # display the most common start hour
    print("The most common start hour is: ", int(modes['start_hour'][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
