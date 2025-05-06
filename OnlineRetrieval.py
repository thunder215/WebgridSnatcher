import requests
from bs4 import BeautifulSoup

def print_unicode_grid(url):
    # Step 1: Fetch the HTML content
    res = requests.get(url)
    if not res.ok:
        print("Failed to fetch the document.")
        return

    # Step 2: Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')

    # Step 3: Find the first table
    table = soup.find("table")
    if not table:
        print("No table found.")
        return

    # Step 4: Read all data rows
    rows = table.find_all("tr")[1:]  # Skip header
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        try:
            x = int(cols[0].get_text(strip=True))
            char = cols[1].get_text(strip=True)
            y = int(cols[2].get_text(strip=True))
            data.append((x, y, char))
        except ValueError:
            continue

    # Step 5: Find grid size
    if not data:
        print("No data rows parsed.")
        return

    max_x = max(x for x, y, c in data)
    max_y = max(y for x, y, c in data)

    # Step 6: Create and fill grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, c in data:
        grid[y][x] = c

    # Step 7: Print the grid
    for row in reversed(grid):
        print("".join(row))


# Call the function with your document URL
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print_unicode_grid(url)
