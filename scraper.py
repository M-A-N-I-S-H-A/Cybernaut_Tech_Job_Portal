import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_indeed(query="python developer", location="India", pages=2):
    base_url = "https://www.indeed.com/jobs"
    jobs = []

    for page in range(pages):
        params = {"q": query, "l": location, "start": page*10}
        response = requests.get(base_url, params=params, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        for job_card in soup.find_all("div", class_="job_seen_beacon"):
            title = job_card.find("h2", class_="jobTitle")
            company = job_card.find("span", class_="companyName")
            location = job_card.find("div", class_="companyLocation")
            link = job_card.find("a", href=True)

            jobs.append({
                "title": title.text.strip() if title else None,
                "company": company.text.strip() if company else None,
                "location": location.text.strip() if location else None,
                "link": "https://www.indeed.com" + link["href"] if link else None
            })

    df = pd.DataFrame(jobs)
    df.to_csv("jobs.csv", index=False)
    print("✅ Jobs scraped and saved to jobs.csv")
    return df

if __name__ == "__main__":
    scrape_indeed()
