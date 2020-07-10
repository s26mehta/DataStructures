import csv
import json
import urllib2

from collections import defaultdict

G7_COUNTRIES = ['ca', 'fr', 'de', 'it', 'jp', 'gb', 'us']
GDP_INDICATOR = 'NY.GDP.MKTP.CD'
POPULATION_INDICATOR = 'SP.POP.TOTL'
INDICATORS = [GDP_INDICATOR, POPULATION_INDICATOR]

# Each CSVTable subclass will implement three functions:
#   - extract: Pulls data from a source
#   - transform: Transforms data returned by the extract function and stores it within the table
#   - load: Writes the table's data to a CSV file (the filename of which is stored
#             in the filename property of the table object)
class CSVTable:

  def __init__(self):
    self.data = []


class CountryInformationCSVTable(CSVTable):
  filename = 'raw_countries.csv'

  def extract(self):
    responses = []
    for country in G7_COUNTRIES:
      url = ('http://api.worldbank.org/v2/countries/%s?format=json' % country)
      response = urllib2.urlopen(url).read()
      json_response = json.loads(response)
      if not json_response[1][0]:
        raise ValueError('Invalid response from World Bank countries API')
      responses.append(json_response[1][0])
    return responses

  def transform(self, raw_country_information_list):
    for raw_country_information in raw_country_information_list:
      clean_country_information = CountryInformation(
        raw_country_information['id'],
        raw_country_information['iso2Code'],
        raw_country_information['name'],
        raw_country_information['region']['value'],
        raw_country_information['capitalCity'])
      self.data.append(clean_country_information)

  def load(self):
    with open(self.filename, 'wb') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(['iso3Code', 'iso2Code', 'name', 'region_name', 'capital_city'])
      for row in self.data:
        writer.writerow([
          row.country_id,
          row.iso2Code,
          row.name,
          row.region_name,
          row.capital_city])


class CountryIndicatorsCSVTable(CSVTable):
  filename = 'raw_indicators.csv'

  def extract(self):
    responses = []
    start_year = 2000
    end_year = 2016
    for country in G7_COUNTRIES:
      for indicator in INDICATORS:
        url = ('http://api.worldbank.org/v2/countries/%s/indicators/%s?date=%s:%s&format=json' %
                (country, indicator, start_year, end_year))
        response = urllib2.urlopen(url).read()
        json_response = json.loads(response)
        if not json_response[1]:
          raise ValueError('Invalid response from World Bank country indicators API')
        responses.append(json_response[1])
    return responses

  def transform(self, raw_country_indicator_list):
    for indicator in raw_country_indicator_list:
      for yearly_info in indicator:
        clean_indicator = CountryIndicator(
          yearly_info['country']['id'],
          yearly_info['date'],
          yearly_info['indicator']['id'],
          yearly_info['value'])
        self.data.append(clean_indicator)

  def load(self):
    with open(self.filename, 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(['iso2Code', 'year', 'indicator_code', 'indicator_value'])
      for row in self.data:
        writer.writerow([
          row.iso2Code,
          row.year,
          row.indicator_code,
          row.indicator_value])


class CountryDimensionsCSVTable(CSVTable):
  filename = 'dim_country.csv'

  def extract(self):
    all_country_information = defaultdict(defaultdict)
    with open(CountryInformationCSVTable.filename, 'rb') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        all_country_information[row['iso2Code']].update(row)
    return all_country_information

  def transform(self, country_information_data, country_indicators_data):
    current_year = 2016
    country_dimensions_data = []
    country_key = 0
    for country, info in country_information_data.iteritems():
      country_and_year = info['iso2Code'], str(current_year)
      current_population = country_indicators_data[country_and_year]['population']
      current_gdp = country_indicators_data[country_and_year]['gdp']
      country_dimension = CountryDimension(country_key, info['name'], info['iso3Code'], info['iso2Code'],
                                           info['capital_city'], info['region_name'], current_population, current_gdp)
      self.data.append(country_dimension)
      country_key += 1

  def load(self):
    with open(self.filename, 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(
        ['_country_key', 'name', 'iso3Code', 'iso2Code', 'capital_city', 'region_name', 'current_population',
         'current_gdp'])
      for row in self.data:
        writer.writerow([
          row._country_key,
          row.name,
          row.iso3Code,
          row.iso2Code,
          row.capital_city,
          row.region_name,
          row.current_population,
          row.current_gdp])


class CountryIndicatorFactsCSVTable(CSVTable):
  filename = 'fct_country_indicator_transitions.csv'

  def extract(self):
    all_country_indicator_data = defaultdict(defaultdict)
    with open(CountryIndicatorsCSVTable.filename, 'rb') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        country_and_year = row['iso2Code'], row['year']
        if row['indicator_code'] == GDP_INDICATOR:
          all_country_indicator_data[country_and_year]['gdp'] = row['indicator_value']
        elif row['indicator_code'] == POPULATION_INDICATOR:
          all_country_indicator_data[country_and_year]['population'] = row['indicator_value']
    return all_country_indicator_data

  def transform(self, country_dimensions_data, country_indicator_facts_data):
    for year in range(2000, 2017):
      for country_dimensions in country_dimensions_data:
        country_and_year = country_dimensions.iso2Code, str(year)
        current_population = country_indicator_facts_data[country_and_year]['population']
        current_gdp = country_indicator_facts_data[country_and_year]['gdp']
        if year == 2000:
          population_change = 'undefined'
          gdp_change = 'undefined'
        else:
          country_and_previous_year = country_dimensions.iso2Code, str(year - 1)
          population_change = int(current_population) - int(country_indicator_facts_data[country_and_previous_year]['population'])
          gdp_change = round(float(current_gdp) - float(country_indicator_facts_data[country_and_previous_year]['gdp']), 2)

        country_indicator_facts = CountryIndicatorFacts(country_dimensions._country_key, year, current_population,
                                                        population_change, current_gdp, gdp_change)
        self.data.append(country_indicator_facts)

  def load(self):
    with open(self.filename, 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(['_country_key', 'year', 'population', 'population_change', 'gdp_usd', 'gdp_usd_change'])
      for row in self.data:
        writer.writerow([
          row._country_key,
          row.year,
          row.population,
          row.population_change,
          row.gdp_usd,
          row.gdp_usd_change])

class CountryInformation:

  def __init__(self, country_id, iso2Code, name, region_name, capital_city):
    self.country_id = country_id
    self.iso2Code = iso2Code
    self.name = name
    self.region_name = region_name
    self.capital_city = capital_city


class CountryIndicator:

  def __init__(self, iso2Code, year, indicator_code, indicator_value):
    self.iso2Code = iso2Code
    self.year = year
    self.indicator_code = indicator_code
    self.indicator_value = indicator_value


class CountryDimension:

  def __init__(self, country_key, name, iso3Code, iso2Code, capital_city, region_name, current_population,
               current_gdp):
    self._country_key = country_key
    self.name = name
    self.iso3Code = iso3Code
    self.iso2Code = iso2Code
    self.capital_city = capital_city
    self.region_name = region_name
    self.current_population = current_population
    self.current_gdp = current_gdp


class CountryIndicatorFacts:

  def __init__(self, country_key, year, population, population_change, gdp_usd, gdp_usd_change):
    self._country_key = country_key
    self.year = year
    self.population = population
    self.population_change = population_change
    self.gdp_usd = gdp_usd
    self.gdp_usd_change = gdp_usd_change
