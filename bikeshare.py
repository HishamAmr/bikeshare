import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hi Let\'s Get Start in This Program')
    city = ''
    while city.lower() not in[i.lower() for i in CITY_DATA.keys()]:
        print("Please choose the city you want:")
        print("1-Chicago\n2-New York City\n3-Washington")
        city = input().lower()
        
   


    

    
    month_data = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'all': 7}
    month = ''
    while month.lower() not in [i.lower() for i in month_data.keys()]:
        print("\nPlease choose the month, between January to June or all, for which you're seeking about:\n 1-January\n2-February\n3-March\n4-April\n5-May\n6-June\n7-All")
        month = input().lower()

    if month.lower() not in [i.lower() for i in month_data.keys()]:
        print("\nInvalid input. Please try again.\nRestarting...")


    
    day_data = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7, 'all': 8}
    day = ''
    counter = 0 
    while day.lower() not in [i.lower() for i in day_data]:
        if counter > 0 : 
          print ("Invalid input")
          print ("Please Check your input")
        print("\nPlease choose the day, between monday to sunday or all, for which you're seeking about:")
        print("1-monday\n2-tuesday\n3-wednesday\n4-thursday\n5-friday\n6-saturday\n7-sunday\n8-all")
        day = input().lower()


    print("\nYou have chosen {} as your month.".format(month.title()))
    print("\nYou have chosen {} as your city.".format(city.title()))
    print("\nYou have chosen {} as your day.".format(day.title()))
    
    print('-'*100)
   
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    print("\nLoading data...")
    city_df = pd.read_csv(CITY_DATA[city])
    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    city_df['month'] = city_df['Start Time'].dt.month
    city_df['day_of_week'] = city_df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        city_df = city_df[city_df['month'] == month]
    if day != 'all':
        city_df = city_df[city_df['day_of_week'] == day.title()]
    return city_df


def time_stats(city_df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (city_df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try : 
      pop_month = city_df['month'].mode()[0]
    except : 
      pop_month = city_df['month'].mode() 
    city_df['hour'] = city_df['Start Time'].dt.hour
    try :
      pop_hr = city_df['hour'].mode()[0]
    except : 
      pop_hr = city_df['hour'].mode()
    try : 
      pop_day = city_df['day_of_week'].mode()[0]
    except : 
      pop_day = city_df['day_of_week'].mode()


    print("Most Popular Month : {}".format(pop_month))
    print("Most Popular Day : {}".format(pop_day))
    print("Most Popular Start Hour : {}".format(pop_hr))


    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*100)

def station_stats(city_df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (city_df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try :
      start_station_common = city_df['Start Station'].mode()[0]
      end_station_comm = city_df['End Station'].mode()[0]
      freq_comb = city_df['Start Station'].str.cat(city_df['End Station'], sep=' to ').mode()[0]

    
    except : 
      start_station_common = city_df['Start Station'].mode()
      end_station_comm = city_df['End Station'].mode()
      freq_comb = city_df['Start Station'].str.cat(city_df['End Station'], sep=' to ').mode()
    print("The most commonly used start station: {}".format(start_station_common))
    print("The most commonly used end station: {}".format(end_station_comm))
    print("The most frequent combination of trips are from {}.".format(freq_comb))
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*100)

def trip_duration_stats(city_df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (city_df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    min, sec = divmod( city_df['Trip Duration'].sum(), 60)
    hr, min = divmod(min, 60)
    print("The total trip duration is {} hours, {} mins and {} seconds.".format(hr,min,sec))
    mins, sec = divmod( round(city_df['Trip Duration'].mean()), 60)
    if mins <= 60:
        print("The average trip duration is {} mins and {} seconds.".format(mins, sec))
    else:
        hrs, mins = divmod(mins, 60)
        print("The average trip duration is {} hours, {} mins and {} seconds.".format(hrs,mins,sec))
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*100)

def user_stats(city_df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (city_df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    types_of_users = city_df['User Type'].value_counts()
    print("The types of users are : {}".format(types_of_users))
    try:
        Gender = city_df['Gender'].value_counts()
        print("The types of users by Gender are given below:{}".format(Gender))
    except:
        print("Failed to detect Genders")
    try:
        earl_birth_year = int(city_df['Birth Year'].min())
        common_birth_year = int(city_df['Birth Year'].mode()[0])
        recent_birth_year = int(city_df['Birth Year'].max())
        print('The earliest year of birth: {}'.format(earl_birth_year))
        print('The most common year year of birth: {}'.format(common_birth_year))
        print('The  most recent year of birth: {}'.format(recent_birth_year))
    except:
        print("There are no birth year details in this file.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*100)
def view_data(df):
    u_input = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    index = 0
    while u_input not in  ['y', 'n']:
        print("Do you wish to view the dataset?")
        print("y : Yes")
        print("n : no")

        u_input = input().lower()
        #the raw data from the df is displayed if user opts for it
        if u_input == "y":
             print(df[0:5])
        elif u_input not in ['y', 'n']:
            print("Please check your input")
            print("Invalid response")

    #Extra while loop here to ask user if they want to continue viewing data
    while u_input == 'y':
        print("Do you wish to view more raw data?")
        print("y : Yes")
        print("n : no")

        index += 5
        u_input = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if u_input == "y":
             print(df[index:index+5])
        elif u_input == "n":
             break

    print('-'*100)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        res = input('Would you like to start over?')
        print("y : Yes")
        print("n : no")

        if res.lower() != 'y':
            break

if __name__ == "__main__":
	main()

