import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, scrolledtext

# News Scraping Functions
def scrape_newsnation():
    try:
        url = "https://www.newsnationnow.com/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.find_all('h2', class_='entry-title'):
            headline = item.get_text()
            link = item.find('a').get('href')
            articles.append({'headline': headline, 'link': link})

        return articles
    except Exception as e:
        print(f"Error scraping NewsNation: {e}")
        return []

def scrape_apnews():
    try:
        url = "https://apnews.com/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.find_all('h1', class_='Component-h1-0-2-56'):
            headline = item.get_text()
            link = item.find('a').get('href')
            articles.append({'headline': headline, 'link': f"https://apnews.com{link}"})

        return articles
    except Exception as e:
        print(f"Error scraping AP News: {e}")
        return []

def scrape_reuters():
    try:
        url = "https://www.reuters.com/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.find_all('h2', class_='MediaStoryCard__heading__2tYEK'):
            headline = item.get_text()
            link = item.find('a').get('href')
            articles.append({'headline': headline, 'link': f"https://www.reuters.com{link}"})

        return articles
    except Exception as e:
        print(f"Error scraping Reuters: {e}")
        return []

def scrape_cnn():
    try:
        url = "https://www.cnn.com/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.find_all('h3', class_='cd__headline'):
            headline = item.get_text()
            link = item.find('a').get('href')
            articles.append({'headline': headline, 'link': f"https://www.cnn.com{link}"})

        return articles
    except Exception as e:
        print(f"Error scraping CNN: {e}")
        return []

def scrape_local_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.find_all('h2', class_='headline'):
            headline = item.get_text()
            link = item.find('a').get('href')
            articles.append({'headline': headline, 'link': link})

        return articles
    except Exception as e:
        print(f"Error scraping local news from {url}: {e}")
        return []

# Job Scraping Functions
def scrape_indeed(query, location):
    try:
        url = f"https://www.indeed.com/jobs?q={query}&l={location}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = []
        for item in soup.find_all('div', class_='jobsearch-SerpJobCard'):
            title = item.find('h2', class_='title').get_text(strip=True)
            link = item.find('a')['href']
            company = item.find('span', class_='company').get_text(strip=True)
            jobs.append({'title': title, 'company': company, 'link': f"https://www.indeed.com{link}"})

        return jobs
    except Exception as e:
        print(f"Error scraping Indeed: {e}")
        return []

def scrape_monster(query, location):
    try:
        url = f"https://www.monster.com/jobs/search?q={query}&where={location}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = []
        for item in soup.find_all('section', class_='card-content'):
            title = item.find('h2', class_='title').get_text(strip=True)
            link = item.find('a')['href']
            company = item.find('div', class_='company').get_text(strip=True)
            jobs.append({'title': title, 'company': company, 'link': link})

        return jobs
    except Exception as e:
        print(f"Error scraping Monster: {e}")
        return []

def scrape_ziprecruiter(query, location):
    try:
        url = f"https://www.ziprecruiter.com/candidate/search?search={query}&location={location}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = []
        for item in soup.find_all('article', class_='job_result'):
            title = item.find('h2', class_='job_title').get_text(strip=True)
            link = item.find('a')['href']
            company = item.find('div', class_='company_name').get_text(strip=True)
            jobs.append({'title': title, 'company': company, 'link': f"https://www.ziprecruiter.com{link}"})

        return jobs
    except Exception as e:
        print(f"Error scraping ZipRecruiter: {e}")
        return []

def scrape_glassdoor(query, location):
    try:
        url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={query}&locT=C&locId={location}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = []
        for item in soup.find_all('li', class_='react-job-listing'):
            title = item.find('a', class_='jobLink').get_text(strip=True)
            link = item.find('a')['href']
            company = item.find('div', class_='job-search-1lh').get_text(strip=True)
            jobs.append({'title': title, 'company': company, 'link': f"https://www.glassdoor.com{link}"})

        return jobs
    except Exception as e:
        print(f"Error scraping Glassdoor: {e}")
        return []

# GUI Application
class ScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")

        # Set the style
        style = ttk.Style()
        style.configure('TFrame', background='black')
        style.configure('TLabel', background='black', foreground='green', font=('Helvetica', 10, 'bold'))
        style.configure('TButton', background='blue', foreground='white', font=('Helvetica', 10, 'bold'))
        style.configure('TNotebook', background='black')
        style.configure('TNotebook.Tab', background='blue', foreground='white', font=('Helvetica', 10, 'bold'))
        
        self.tabControl = ttk.Notebook(root)
        
        self.news_tab = ttk.Frame(self.tabControl)
        self.jobs_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.news_tab, text="News")
        self.tabControl.add(self.jobs_tab, text="Jobs")

        self.tabControl.pack(expand=1, fill="both")

        # News Tab
        self.news_url_label = ttk.Label(self.news_tab, text="Local News URL:", style='TLabel')
        self.news_url_label.pack(pady=5)
        self.news_url_entry = ttk.Entry(self.news_tab, width=50)
        self.news_url_entry.pack(pady=5)
        self.news_scrape_button = ttk.Button(self.news_tab, text="Scrape News", command=self.scrape_news)
        self.news_scrape_button.pack(pady=5)
        self.news_text = scrolledtext.ScrolledText(self.news_tab, width=100, height=20, background='black', foreground='white', font=('Helvetica', 10, 'bold'))
        self.news_text.pack(pady=10)

        # Jobs Tab
        self.job_query_label = ttk.Label(self.jobs_tab, text="Job Query:", style='TLabel')
        self.job_query_label.pack(pady=5)
        self.job_query_entry = ttk.Entry(self.jobs_tab, width=30)
        self.job_query_entry.pack(pady=5)
        self.job_location_label = ttk.Label(self.jobs_tab, text="Job Location:", style='TLabel')
        self.job_location_label.pack(pady=5)
        self.job_location_entry = ttk.Entry(self.jobs_tab, width=30)
        self.job_location_entry.pack(pady=5)
        self.job_scrape_button = ttk.Button(self.jobs_tab, text="Scrape Jobs", command=self.scrape_jobs)
        self.job_scrape_button.pack(pady=5)
        self.job_text = scrolledtext.ScrolledText(self.jobs_tab, width=100, height=20, background='black', foreground='white', font=('Helvetica', 10, 'bold'))
        self.job_text.pack(pady=10)

    def scrape_news(self):
        self.news_text.delete(1.0, tk.END)
        local_news_url = self.news_url_entry.get()
        
        newsnation_articles = scrape_newsnation()
        apnews_articles = scrape_apnews()
        reuters_articles = scrape_reuters()
        cnn_articles = scrape_cnn()
        local_news_articles = scrape_local_news(local_news_url)
        
        self.display_articles(self.news_text, "NewsNation Articles", newsnation_articles)
        self.display_articles(self.news_text, "AP News Articles", apnews_articles)
        self.display_articles(self.news_text, "Reuters Articles", reuters_articles)
        self.display_articles(self.news_text, "CNN Articles", cnn_articles)
        self.display_articles(self.news_text, "Local News Articles", local_news_articles)

    def scrape_jobs(self):
        self.job_text.delete(1.0, tk.END)
        query = self.job_query_entry.get()
        location = self.job_location_entry.get()
        
        indeed_jobs = scrape_indeed(query, location)
        monster_jobs = scrape_monster(query, location)
        ziprecruiter_jobs = scrape_ziprecruiter(query, location)
        glassdoor_jobs = scrape_glassdoor(query, location)
        
        self.display_jobs(self.job_text, "Indeed Job Listings", indeed_jobs)
        self.display_jobs(self.job_text, "Monster Job Listings", monster_jobs)
        self.display_jobs(self.job_text, "ZipRecruiter Job Listings", ziprecruiter_jobs)
        self.display_jobs(self.job_text, "Glassdoor Job Listings", glassdoor_jobs)

    def display_articles(self, text_widget, title, articles):
        if articles:
            text_widget.insert(tk.END, f"{title}:\n")
            for article in articles:
                text_widget.insert(tk.END, f"Headline: {article['headline']}\nLink: {article['link']}\n\n")
        else:
            text_widget.insert(tk.END, f"No articles found for {title}\n")

    def display_jobs(self, text_widget, title, jobs):
        if jobs:
            text_widget.insert(tk.END, f"{title}:\n")
            for job in jobs:
                text_widget.insert(tk.END, f"Job Title: {job['title']}\nCompany: {job['company']}\nLink: {job['link']}\n\n")
        else:
            text_widget.insert(tk.END, f"No job listings found for {title}\n")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()
