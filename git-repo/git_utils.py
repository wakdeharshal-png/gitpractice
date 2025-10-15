import os

def init_repo():
    os.system("git init")

def add_all():
    os.system("git add .")

def commit(message):
    os.system(f'git commit -m "{message}"')

def push(branch="main"):
    os.system(f"git push origin {branch}")

def pull(branch="main"):
    os.system(f"git pull origin {branch}")

def status():
    os.system("git status")

