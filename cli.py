import argparse, time
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress
from backend.orchestrator import Orchestrator

console = Console()

def run_cli(topic: str):
    orchestrator = Orchestrator()
    console.rule("[bold green]AI Blog Writer (LLaMA2 via Ollama)")
    console.print(f"Generating draft for: [yellow]{topic}[/yellow]\n")

    with Progress() as progress:
        task = progress.add_task("Generating draft...", total=100)
        for _ in range(20):
            time.sleep(0.1)
            progress.update(task, advance=5)

    result = orchestrator.run_initial(topic)
    draft, evaluation = result["draft"], result["evaluation"]

    with open("output/blog_draft.md", "w") as f:
        f.write(draft)

    console.rule("[bold blue]Draft Preview")
    console.print(Markdown(draft[:2000]))
    console.rule("[bold magenta]Evaluation")
    console.print(evaluation)

    while True:
        action = console.input("\n[cyan]Enter (f) feedback, (a) approve, (q) quit: [/cyan] ")

        if action == "f":
            fb = console.input("[cyan]Your feedback: [/cyan] ")
            console.print("\nRedrafting...\n")
            with Progress() as progress:
                task = progress.add_task("Regenerating...", total=100)
                for _ in range(20):
                    time.sleep(0.1)
                    progress.update(task, advance=5)
            result = orchestrator.redraft(fb)
            draft, evaluation = result["draft"], result["evaluation"]
            with open("output/blog_draft.md", "w") as f:
                f.write(draft)
            console.rule("[bold blue]Updated Draft")
            console.print(Markdown(draft[:2000]))
            console.rule("[bold magenta]Evaluation")
            console.print(evaluation)
        elif action == "a":
            console.print("\nDraft approved! Saved to output/blog_draft.md")
            break
        elif action == "q":
            console.print("\nExiting.")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True)
    args = parser.parse_args()
    run_cli(args.topic)
