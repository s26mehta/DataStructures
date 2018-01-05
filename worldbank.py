import urllib2
import json
import csv

from collections import defaultdict

from csv_tables import *

def extract_raw_country_information(iso2code):
  url = ('http://api.worldbank.org/v2/countries/%s?format=json' % iso2code)
  response = urllib2.urlopen(url).read()
  json_response = json.loads(response)
  if not json_response[1][0]:
    raise ValueError('Invalid response from World Bank countries API')
  return json_response[1][0]

def extract_raw_country_indicator(country_iso2code, indicator, start_year, end_year):
  url = ('http://api.worldbank.org/v2/countries/%s/indicators/%s?date=%s:%s&format=json' %
         (country_iso2code, indicator, start_year, end_year))
  response = urllib2.urlopen(url).read()
  json_response = json.loads(response)
  return json_response[1]


def transform_raw_country_information(raw_country_information):
  clean_country_information = CountryInformation(
    raw_country_information['id'],
    raw_country_information['iso2Code'],
    raw_country_information['name'],
    raw_country_information['region']['value'],
    raw_country_information['capitalCity'])
  return clean_country_information

def transform_raw_country_indicator_information(raw_country_information):
  country_indicator_array_by_year = []
  for info in raw_country_information:
    clean_country_information = CountryIndicators(
      info['country']['id'],
      info['date'],
      info['indicator']['id'],
      info['value'])
    country_indicator_array_by_year.append(clean_country_information)
  return country_indicator_array_by_year

def transform_country_info_to_dimensions(country_information_dictionary, country_indicators_dictionary):
  current_year = 2016
  country_dimensions_array = []
  country_key = 0
  for country, info in country_information_dictionary.iteritems():
    current_population = country_indicators_dictionary[(info['iso2Code'], str(current_year))]['population']
    current_gdp = country_indicators_dictionary[(info['iso2Code'], str(current_year))]['gdp']
    country_dimension = CountryDimension(country_key, info['name'], info['iso3Code'], info['iso2Code'],
                                         info['capital_city'], info['region_name'], current_population, current_gdp)
    country_dimensions_array.append(country_dimension)
    country_key += 1
  return country_dimensions_array

def transform_country_indicator_transitions(country_dimensions, country_indicators_dictionary):
  country_dimensions_array = []
  for year in range(2000, 2017):
    for obj in country_dimensions:
      current_population = country_indicators_dictionary[obj.iso2code, str(year)]['population']
      population_change = 0 if year == 2000 else int(current_population) - int(
        country_indicators_dictionary[obj.iso2code, str(year - 1)]['population'])
      current_gdp = country_indicators_dictionary[obj.iso2code, str(year)]['gdp']
      gdp_change = 0 if year == 2000 else float(current_gdp) - float(
        country_indicators_dictionary[obj.iso2code, str(year - 1)]['gdp'])
      country_dimension = CountryIndicatorTransitions(obj._country_key, year, current_population,
                                                      population_change, current_gdp, gdp_change)
      country_dimensions_array.append(country_dimension)
  return country_dimensions_array

def load_country_info_to_dimensions(country_dimensions, filename):
  with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(
      ['_country_key', 'name', 'iso3code', 'iso2code', 'capital_city', 'region_name', 'current_population',
       'current_gdp'])
    for row in country_dimensions:
      writer.writerow([
        row._country_key,
        row.name,
        row.iso3code,
        row.iso2code,
        row.capital_city,
        row.region_name,
        row.current_population,
        row.current_gdp])

def load_country_indicator_transitions(country_indicator_transitions, filename):
  with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['_country_key', 'year', 'population', 'population_change', 'gdp_usd', 'gdp_usd_change'])
    for row in country_indicator_transitions:
      writer.writerow([
        row._country_key,
        row.year,
        row.population,
        row.population_change,
        row.gdp_usd,
        row.gdp_usd_change])

def load_country_information(transformed_country_information_array, filename):
  with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['iso3Code', 'iso2Code', 'name', 'region_name', 'capital_city'])
    for row in transformed_country_information_array:
      writer.writerow([
        row.country_id,
        row.iso2Code,
        row.name,
        row.region_name,
        row.capital_city])

def load_country_indicator_information(transformed_indicator_information_array, filename):
  with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['iso2Code', 'year', 'indicator_code', 'indicator_value'])
    for country in transformed_indicator_information_array:
      for row in country:
        writer.writerow([
          row.country_iso2code,
          row.year,
          row.indicator_code,
          row.indicator_value])

# TODO: Add comments
def etl_job_1():
  g7_countries = ['ca', 'fr', 'de', 'it', 'jp', 'gb', 'us']
  indicators = ['NY.GDP.MKTP.CD', 'SP.POP.TOTL']
  transformed_country_information_array = []
  transformed_country_indicator_info_array = []
  for country in g7_countries:
    raw_country_information = extract_raw_country_information(country)
    transformed_country_information_array.append(transform_raw_country_information(raw_country_information))

    for indicator in indicators:
      # TODO: PLEASE INCLUDE 1999 for gdp shit and exclude elsewhere
      start_year = 2000
      end_year = 2016
      raw_country_indicator_info = extract_raw_country_indicator(country, indicator, start_year, end_year)
      transformed_country_indicator_info_array.append(
        transform_raw_country_indicator_information(raw_country_indicator_info))

  load_country_information(transformed_country_information_array, 'raw_countries.csv')
  load_country_indicator_information(transformed_country_indicator_info_array, 'raw_indicator.csv')


def etl_job_2():
  country_information_dictionary = defaultdict(defaultdict)
  with open('raw_countries.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      country_information_dictionary[row['iso2Code']].update(row)

  country_indicators_dictionary = defaultdict(defaultdict)
  with open('raw_indicator.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['indicator_code'] == 'NY.GDP.MKTP.CD':
        country_indicators_dictionary[(row['iso2Code'], row['year'])]['gdp'] = row['indicator_value']
      else:
        country_indicators_dictionary[(row['iso2Code'], row['year'])]['population'] = row['indicator_value']

  country_dimensions = transform_country_info_to_dimensions(country_information_dictionary,
                                                            country_indicators_dictionary)
  load_country_info_to_dimensions(country_dimensions, 'dim_country.csv')

  country_indicator_transitions = transform_country_indicator_transitions(country_dimensions,
                                                                          country_indicators_dictionary)
  load_country_indicator_transitions(country_indicator_transitions, 'fct_country_indicator_transitions.csv')


if __name__ == "__main__":
  etl_job_1()
  etl_job_2()
