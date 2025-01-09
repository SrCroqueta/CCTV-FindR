import os
import time
import sys

green  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
yellow ="\x1b[1;93m"
magenta   ="\x1b[1;95m"
white  ="\x1b[1;97m"
blue   ="\x1b[1;94m"
red  ='\x1b[1;91m'
underline = '\033[4m'
pink = '\033[35m'
bold = '\033[1m'
black='\033[30m'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# type
def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0007)

def loading_animation():
    symbols = ("⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿")
    for _ in range(3):
        for symbol in symbols:
            time.sleep(0.1)
            print(f"{green} ~>> Loading {symbol}", end='\r')
def loading_animation2():
    symbols = ("〡", "〢", "〣")
    for _ in range(3):
        for symbol in symbols:
            time.sleep(0.1)
            print(f"{yellow} ~>> Loading {symbol}", end='\r')

# logos
chois=f"""{cyan}
  ____ ____ _______     __  _____ _           _ ____  
 / ___/ ___|_   _\ \   / / |  ___(_)_ __   __| |  _ \ 
| |  | |     | |  \ \ / /  | |_  | | '_ \ / _` | |_) |
| |__| |___  | |   \ V /   |  _| | | | | | (_| |  _ < 
 \____\____| |_|    \_/    |_|   |_|_| |_|\__,_|_| \_\
                                                               

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{pink}[GitHub]	▪︎	{white}https://github.com/SrCroqueta
{blue}[BlueSky]	▪︎	{white}srcroqueta.bsky.social

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

    {yellow}[1]  {red}Search by {green} Time zone
    
    {yellow}[2]  {red}Search by {green} Location

    {yellow}[3]  {red}Search by {green} Countries

    {yellow}[4]  {red}Search by {green} Manufacturers

"""



#----------------------------------------------------------------


timeline=f"""{green}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
    ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
    ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{green}[<ID~>github] ▪  {white}https://github.com/SrCroqueta
{cyan}[<ID~>BlueSky ▪  {white}srcroqueta.bsky.social

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{red}01–{green} +00:00     {red}02–{green} +01:00     {red}03–{green} +02:00     {red}04–{green} +03:00
{red}05–{green} +03:30     {red}06–{green} +04:00     {red}07–{green} +05:00     {red}08–{green} +05:30
{red}09–{green} +06:00     {red}10–{green} +07:00     {red}11–{green} +08:00     {red}12–{green} +09:00
{red}13–{green} +10:00     {red}14–{green} +11:00     {red}15–{green} +13:00     {red}16–{green} -
{red}17–{green} -02:00     {red}18–{green} -03:00     {red}19–{green} -04:00     {red}20–{green} -05:00
{red}21–{green} -06:00     {red}22–{green} -07:00     {red}23–{green} -08:00     {red}24–{green} -09:00
{red}25–{green} -10:00

{red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺"""



#----------------------------------------------------------------------------------------------------



cam_n=f"""{green}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{green}[<ID~>github] ▪  {white}https://github.com/SrCroqueta
{cyan}[<ID~>BlueSky ▪  {white}srcroqueta.bsky.social

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺
    {red}01–{green}Dlink        {red}02–{green}DLink-DCS-932  {red}03– {green}TPLink        {red}04–{green}Foscam
    {red}05–{green}Linksys      {red}06–{green}Sony           {red}07–{green}Sony-CS3       {red}08–{green}Vije
    {red}09–{green}Mobotix      {red}10–{green}Panasonic      {red}11–{green}Megapixel      {red}12–{green}ChannelVision
  
{red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺"""


coun_n=f"""{green}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{green}[<ID~>github] ▪  {white}https://github.com/SrCroqueta
{cyan}[<ID~>BlueSky ▪  {white}srcroqueta.bsky.social

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{red}01–{yellow}•United States•            {red}02–{yellow}•Japan•            {red}03–{yellow}•Italy•            {red}04–{yellow}•South Korea•
{red}05–{yellow}•France•                   {red}06–{yellow}•Germany•          {red}07–{yellow}•Taiwan•           {red}08–{yellow}•Russia•
{red}09–{yellow}•United kingdom•           {red}10–{yellow}•Netherlands•      {red}11–{yellow}•Czech Republic•   {red}12–{yellow}•Turkey•
{red}13–{yellow}•Austria•                  {red}14–{yellow}•Switzerland•      {red}15–{yellow}•Spain•            {red}16–{yellow}•Canada•
{red}17–{yellow}•Sweden•                   {red}18–{yellow}•Israel•           {red}19–{yellow}•Poland•           {red}20–{yellow}•Iran•
{red}21–{yellow}•Norway•                   {red}22–{yellow}•Romania•          {red}23–{yellow}•India•            {red}24–{yellow}•Veitnam•
{red}25–{yellow}•Belgium•                  {red}26–{yellow}•Brazil•           {red}27–{yellow}•Bulgaria•         {red}28–{yellow}•Indonesia•
{red}29–{yellow}•Denmark•                  {red}30–{yellow}•Argentina•        {red}31–{yellow}•Mexico•           {red}32–{yellow}•Finland•
{red}33–{yellow}•China•                    {red}34–{yellow}•Chile•            {red}35–{yellow}•South Africa•     {red}36–{yellow}•Slovakia•
{red}37–{yellow}•Kuwait•                   {red}38–{yellow}•Ireland•          {red}39–{yellow}•Egypt•            {red}40–{yellow}•Thailand•
{red}41–{yellow}•Ukraine•                  {red}42–{yellow}•Hong Kong•        {red}43–{yellow}•Greece•           {red}44–{yellow}•Portugal•
{red}45–{yellow}•Malaysia•                 {red}46–{yellow}•Tunisia•          {red}47–{yellow}•New Zealand•      {red}48–{yellow}•Bangladesh•
{red}49–{yellow}•Panama•                   {red}50–{yellow}•Moldova•          {red}51–{yellow}•Nicaragua•        {red}52–{yellow}•Malta•
{red}53–{yellow}•Trinidad and Tobago•      {red}54–{yellow}•Saudi Arabia•     {red}55–{yellow}•Croatia•          {red}56–{yellow}•Cyprus•
{red}57–{yellow}•Pakistan•                 {red}58–{yellow}•U-A-Emirates•     {red}59–{yellow}•Kazakhstan•       {red}60–{yellow}•Kuwait•
{red}61–{yellow}•Georgia•                  {red}62–{yellow}•El Salvador•      {red}63–{yellow}•Luxembourg•       {red}64–{yellow}•Puerto Rico•
{red}65–{yellow}•Costa Rica•               {red}66–{yellow}•Belarus•          {red}67–{yellow}•Albania•          {red}68–{yellow}•Liechtenstein•
{red}69–{yellow}•Bosnia and Herzegovina•   {red}70–{yellow}•Paraguay•         {red}71–{yellow}•Philippines•      {red}72–{yellow}•Faeroe Islands•
{red}73–{yellow}•Guatemala•                {red}74–{yellow}•Nepal•            {red}75–{yellow}•Peru•             {red}76–{yellow}•Uruguay•
{red}77–{yellow}•Andorra•                  {red}78–{yellow}•A- & Barbuda•     {red}79–{yellow}•Armenia•          {red}80–{yellow}•Angola•
{red}81–{yellow}•Australia•                {red}82–{yellow}•Aruba•            {red}83–{yellow}•Azerbaijan•       {red}84–{yellow}•Barbados•
{red}85–{yellow}•The Bahamas•              {red}86–{yellow}•Botswana•         {red}87–{yellow}•Congo•            {red}88–{yellow}•Côte d’Ivoire•
{red}89–{yellow}•Algeria•                  {red}90–{yellow}•null•             {red}91–{yellow}•Gabon•            {red}92–{yellow}•Gibraltar•
{red}93–{yellow}•Guadeloupe•               {red}94–{yellow}•Guam•             {red}95–{yellow}•Guyana•           {red}96–{yellow}•Honduras•
{red}97–{yellow}•Jamaica•                  {red}98–{yellow}•Jordan•           {red}99–{yellow}•Kenya•            {red}100–{yellow}•Cambodia•
{red}101–{yellow}•Saint Kitts & Nevis•     {red}102–{yellow}•Cayman Islands•  {red}103–{yellow}•Laos•            {red}104–{yellow}•Lebanon•
{red}105–{yellow}•Sri Lanka•               {red}106–{yellow}•Morocco•         {red}107–{yellow}•Madagascar•      {red}108–{yellow}•Macedonia•
{red}109–{yellow}•Mongolia•                {red}110–{yellow}•Macau•           {red}112–{yellow}•Martinique•      {red}113–{yellow}•Mauritius•
{red}114–{yellow}•Namibia•                 {red}115–{yellow}•New Caledonia•   {red}116–{yellow}•Nigeria•         {red}117–{yellow}•Qatar•
{red}118–{yellow}•Réunion•                 {red}119–{yellow}•Sudan•           {red}120–{yellow}•Senegal•         {red}121–{yellow}•Suriname•
{red}122–{yellow}•São Tomé•                {red}123–{yellow}•Syria•           {red}124–{yellow}•Tanzania•        {red}125–{yellow}•Uzbekistan•
{red}126–{yellow}•Saint Vincent•           {red}127–{yellow}•Benin•

{red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺"""

loc_n=f"""{green}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡇⠀⠀⢀⣼⠿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{yellow}[!]▪︎ {red}EXIT:{white+bold}CTRL+C
{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺

{green}[<ID~>github] ▪  {white}https://github.com/SrCroqueta
{cyan}[<ID~>BlueSky ▪  {white}srcroqueta.bsky.social

{red}𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺
    {red}01–{green}server        {red}02–{green}farm         {red}03–{green}restaurant      {red}04–{green}park
    {red}05–{green}brid          {red}06–{green}beach        {red}07–{green}bridge          {red}08–{green}sport
    {red}09–{green}shop          {red}10–{green}airline      {red}11–{green}hotel           {red}12–{green}hq    
    {red}13–{green}village       {red}14–{green}road         {red}15–{green}pool            {red}16–{green}surfing
    {red}17–{green}parking       {red}18–{green}traffic
{red}+𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺𝄺"""

def inpt():
    inp=input(f"""{blue}Enter a number {green} > {pink} """)
    return inp
