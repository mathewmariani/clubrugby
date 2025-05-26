import subprocess

scripts = ["clubs.py", "info.py", "leagues.py", "fixtures.py", "results.py", "standings.py"]

print("🚀 Starting scraping process...\n")

for script in scripts:
    print(f"▶️ Running {script}...\n{'-'*40}")
    result = subprocess.run(["python3", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"❌ Error in {script}:\n{result.stderr}")
    print(f"{'-'*40}\n")

print("🎉 All scripts completed.")