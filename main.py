import git_utils
import github_utils

def main():
    print("=== GitHub Repo Manager ===")
    print("1. Init local repo")
    print("2. Add all files")
    print("3. Commit changes")
    print("4. Push to GitHub")
    print("5. Pull latest")
    print("6. Repo status")
    print("7. Create new GitHub repo")
    choice = input("Enter choice: ")

    if choice == "1":
        git_utils.init_repo()
    elif choice == "2":
        git_utils.add_all()
    elif choice == "3":
        msg = input("Enter commit message: ")
        git_utils.commit(msg)
    elif choice == "4":
        git_utils.push()
    elif choice == "5":
        git_utils.pull()
    elif choice == "6":
        git_utils.status()
    elif choice == "7":
        token = input("Enter GitHub token: ")
        name = input("Enter new repo name: ")
        github_utils.create_repo(token, name)
    else:
  print("7. Create new GitHub repo")
        print("Invalid choice")

if __name__ == "__main__":
    main()

