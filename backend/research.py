import requests
import xml.etree.ElementTree as ET

class Research:
    def gather(self, topic: str):
        # Wikipedia
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
            res = requests.get(url, timeout=10)
            wiki_summary = res.json().get("extract", "No Wikipedia result found.")[:500]
        except Exception:
            wiki_summary = "Wikipedia fetch failed."

        # Arxiv
        try:
            url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&start=0&max_results=2"
            res = requests.get(url, timeout=10)
            root = ET.fromstring(res.content)
            arxiv_titles = [e.find("{http://www.w3.org/2005/Atom}title").text for e in root.findall("{http://www.w3.org/2005/Atom}entry")]
        except Exception:
            arxiv_titles = ["No Arxiv results"]

        return {"wikipedia": wiki_summary, "arxiv": arxiv_titles}
