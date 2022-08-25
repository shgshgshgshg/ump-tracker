from simple_term_menu import TerminalMenu

options = ["[b] ball", "[s] strike"]
menu = TerminalMenu(options)
idx = menu.show()
print(idx)
