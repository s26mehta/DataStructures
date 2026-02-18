# [Demo] Show candidate what the system look like when adding a new link, like Google Maps link, Instagram link, Youtube link. 
# When given a URL, the system can suggest a featured link-app (featured rendering instead of a classic boring link).

# Question: Here is a JSON for all link-apps (https://link-types-assets.production.linktr.ee/marketplace/v1/link-apps.json). 
# Help me prototype a link-app searching & recommendation system.

# You can use any tool/IDE you want (screen-share is preferred). Do not limit to the Codepad.
# If you use Codepad, you can use the AIAssistant feature.
# Let’s focus on building a real working solution.
# Example URLs: Google Maps URL https://maps.app.goo.gl/vL4J1N2K2xikqE7a7

# Instagram URL https://www.instagram.com/linktr.ee/

# Youtube URL https://www.youtube.com/watch?v=7mGSXLGZvUA&t=2s

"""
Given a url
   -> find some key words that tell us the platform
   -> use key words to figure out which category
        -> Categories: share, grow, sell
             -> use key words to find search terms that potentially map to linkTypes

             
{
    category -> {linktypes -> searchTerms}
}


Share
    - music
    - videos [generic, tiktok, facebook, instagram]
    - twitch
    - documents


Sell
    - amazon products
    - instagram shop products
    - tiktop shop products
    - documents
    - donations

Grow
    - Profile [Tiktok, Instagram]
    - Maps
    - calendar link



"""
from urllib.request import urlopen
import json
import requests
from requests.exceptions import RequestException

class Solution:
    def __init__(self, link_to_data):
        self.link_to_data = link_to_data
        self.parsed_data = {}
    
    def parse_data_from_link(self):
        with urlopen(self.link_to_data) as response:
            raw_data = response.read()
        decoded_data = raw_data.decode('utf-8')
        json_data = json.loads(decoded_data)


        for category in json_data['categories']:
            category_title = category.get('id')
            
            self.parsed_data[category_title] = {}
            
            link_types = category.get('linkTypes', [])
            
            for link_type in link_types:
                link_type_id = link_type.get('linkTypeId')
                search_terms = link_type.get('searchTerms', [])
                alias = link_type.get('alias', '')
                tagline = link_type.get('tagline', '')
                
                if link_type_id:
                    self.parsed_data[category_title][link_type_id] = [search_terms, alias, tagline]

        return self.parsed_data

    def recommend_linktypes(self, link):
        result_dict = {}
        
        normalized_input = link.lower()

        for category_id, linktypes_data in self.parsed_data.items():
            # Initialize a list to hold matching link types for this category
            matching_linktypes = []

            for link_type_id, (search_terms, alias, tagline) in linktypes_data.items():
                
                # Check if any search term for this link type is in the input string
                is_match = False
                for term in search_terms:
                    # Normalize the search term for comparison
                    normalized_term = term.lower()
                    
                    # Check for an exact match or if the search term is a substring 
                    # within the normalized input string.
                    if normalized_term in normalized_input:
                        is_match = True
                        break  # Found a match, move to the next link type
                
                if is_match:
                    matching_linktypes.append(link_type_id)

            # Only add the category to the final result if there are matches
            if matching_linktypes:
                result_dict[category_id] = matching_linktypes

        return result_dict
    
    def check_link(self, link):
        # Check if link is a tiny link
        #        -> if yes fetch full    
        pass

    def is_shortened_and_fetch_full_link(url: str) -> dict:
        """
        Checks if a given URL is a shortened link and, if so, fetches the final, 
        redirected URL.

        A link is considered 'shortened' if the initial request results in a 
        redirection (HTTP status 3xx) to a different final URL.

        Args:
            url: The potentially shortened URL (e.g., 'https://bit.ly/example').

        Returns:
            A dictionary containing the results:
            {
                'original_url': str,
                'is_shortened': bool,
                'final_url': str,
                'status': str 
            }
        """
        # 1. Prepare the output structure
        result = {
            'original_url': url,
            'is_shortened': False,
            'final_url': url,  # Default to the original URL
            'status': 'Success'
        }

        # 2. Use a HEAD request to minimize data transfer, as we only need headers
        #    (which contain redirect info). We set allow_redirects=True to let 
        #    requests handle the full redirection chain.
        try:
            # Define headers to mimic a common browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Use a timeout to prevent the script from hanging on unresponsive servers
            response = requests.head(url, headers=headers, allow_redirects=True, timeout=10)
            
            # Raise an exception for bad status codes (4xx or 5xx)
            response.raise_for_status()

            # 3. Check for redirection history
            # If response.history is non-empty, a redirect occurred.
            if response.history:
                # The final URL is the URL of the last response
                final_url = response.url
                
                # Check if the final URL is actually different from the original
                # Note: We use the response.request.url which is the URL after normalization 
                # by requests, but for simple checking, we rely on the final URL being different.
                if final_url != url:
                    result['is_shortened'] = True
                    result['final_url'] = final_url
                    result['status'] = f"Successfully fetched final link after {len(response.history)} redirect(s)"
                else:
                    # This case is rare but covers instances where a redirect chain 
                    # might lead back to the original URL.
                    result['is_shortened'] = False
                    result['final_url'] = url
                    result['status'] = "No redirection or final URL matches original URL."

            else:
                # No history means no redirection occurred
                result['is_shortened'] = False
                result['final_url'] = url
                result['status'] = "Link is not shortened (no redirection observed)."

        # 4. Handle exceptions
        except requests.TooManyRedirects:
            result['status'] = "Error: Too many redirects (potential loop detected)."
        except requests.exceptions.Timeout:
            result['status'] = "Error: Request timed out."
        except requests.exceptions.HTTPError as e:
            result['status'] = f"Error: HTTP error occurred: {e.response.status_code} {e.response.reason}"
        except RequestException as e:
            result['status'] = f"Error: An error occurred during the request: {e}"
        except Exception as e:
            result['status'] = f"Error: An unexpected error occurred: {e}"

        return result



solution = Solution("https://link-types-assets.production.linktr.ee/marketplace/v1/link-apps.json")
solution.parse_data_from_link()
print(solution.recommend_linktypes("https://www.ig.com/linktr.ee/"))
