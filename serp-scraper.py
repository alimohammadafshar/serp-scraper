from googlesearch import search

# Prompt the user to enter a keyword
keyword = input("Enter a keyword: ")

# Set the number of search results to retrieve
num_results = 10

# Retrieve the top search results for the keyword
search_results = search(keyword, num_results=num_results)

# Print the search results
print(f"Top {num_results} search results for '{keyword}':")
for i, result in enumerate(search_results, start=1):
    print(f"{i}. {result}")
