from csv_tables import CountryInformationCSVTable,\
                       CountryIndicatorsCSVTable,\
                       CountryDimensionsCSVTable,\
                       CountryIndicatorFactsCSVTable

def etl_job_raw_country_information_and_indicators():
  country_information_table = CountryInformationCSVTable()
  raw_country_information_data = country_information_table.extract()
  country_information_table.transform(raw_country_information_data)
  country_information_table.load()

  country_indicators_table = CountryIndicatorsCSVTable()
  raw_country_indicator_data = country_indicators_table.extract()
  country_indicators_table.transform(raw_country_indicator_data)
  country_indicators_table.load()

def etl_job_country_dimensions_and_indicator_facts():
  country_dimensions_table = CountryDimensionsCSVTable()
  country_dimensions_data = country_dimensions_table.extract()
  country_indicator_facts_table = CountryIndicatorFactsCSVTable()
  country_indicator_facts_data = country_indicator_facts_table.extract()
  country_dimensions_table.transform(country_dimensions_data, country_indicator_facts_data)
  country_dimensions_table.load()
  country_indicator_facts_table.transform(country_dimensions_table.data, country_indicator_facts_data)
  country_indicator_facts_table.load()

if __name__ == "__main__":
  try:
    etl_job_raw_country_information_and_indicators()
    etl_job_country_dimensions_and_indicator_facts()
  except Exception as err:
    print('Error running World Bank ETL pipeline: ', err)
