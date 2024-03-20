import os
from rich.console import Console
import BruteInsta

if __name__ == "__main__":
    try:
        os.mkdir('Data')
    except FileExistsError:
        pass
    try:
        BruteInsta.EXAL()
    except Exception as e:
        Console().print(f"[italic red bold]Error : {str(e).title()}!!")
        exit()
