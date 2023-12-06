def user_selection():
    ans = input("Enter section: ")
    if ans == "q":
        return False
    return True 
def main():
    run_me = True 
    while  run_me:
        run_me = user_selection()
