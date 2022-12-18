def city(city_name, country = 'Nepal'):
    """display information about cities and country"""
    print(city_name.title() + " is in " + country + ".")

def main():
    city(city_name = 'pokhara')
    city(city_name= 'NewYork', country= 'America')
    city(city_name= 'tokyo', country = 'Japan')
    city(city_name= 'delhi', country = 'India')

if __name__ == "__main__":
    main()