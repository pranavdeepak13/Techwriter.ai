class Formatter:
    def format(self, draft, citations):
        md = f"# Medium Blog Draft\n\n{draft}\n\n## References\n"
        for i, (src, val) in enumerate(citations.items(), 1):
            md += f"[{i}] {src}: {val}\n"
        return md
