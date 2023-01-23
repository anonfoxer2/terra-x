import argparse
import sys
import os
from rich.console import Console
from pyfiglet import Figlet
from rich.style import Style
from src.instagram import Instagram
from src.twittr import Twitter

pc = Console()

def twitter_all_commands():
    pc.print("FILE=y/n : ", style="yellow", end='')
    print(" Enable/disable output to a file named '<target username>_<command>.txt'")
    pc.print("JSON=y/n :  \t", style="white", end='')
    print("Enable/disable export to a file named '<target username>_<command>.json'")
    pc.print("tweets\t : ", style="bright_cyan", end='')
    print("Get recent tweets of target")
    pc.print("favtweets : \t", style="yellow", end='')
    print("Get target's recently liked tweets")
    pc.print("followers : \t", style="bright_green", end='')
    print(" Get total followers of target")
    pc.print("following : \t", style="cyan", end='')
    print("Get the accounts that the target is following.")
    pc.print("reset target : \t", style='green', end='')
    print(" Select new target")
    pc.print("timeline : \t", style="dark_cyan", end='')
    print("Full information of target's account")
    pc.print("profile pic : ", style='bright_magenta', end='')
    print("Download target's profile picture")
    pc.print("banner : ", style='steel_blue1', end='')
    print("Download target's profile banner ")
    pc.print('htags : ', style='bright_red', end='')
    print('Get hashtags used by target')
    pc.print('mentions : ', style='pink1')
    print('Get users who got mentioned by target in recent tweets')
    print(" ")
    pc.print(" Also supports basic terminal commands : ", style='cyan')
    pc.print("ls : ", style='pink1', end='')
    pc.print("Displays all commands ", ":search:", style='bright_white')
    pc.print("exit : ", style='orange_red1', end='')
    pc.print("Exit Terra", style='bright_white')
    pc.print("clear : ", style='orchid2', end='')
    pc.print("Clear screen", style='bright_white')
    pc.print('back : ', style='purple', end='')
    pc.print('Back to Main Menu', style='yellow')

def insta_all_commands():
    
    pc.print("FILE=y/n : ", style="yellow",end='')
    print(" Enable/disable output to a file named '<target username>_<command>.txt")
    pc.print("JSON=y/n :  \t", style="white", end='')
    print("Enable/disable export to a file named '<target username>_<command>.json")
    pc.print("locations :  \t", style="green", end='')
    print("Get all pinned locations from target's photos")
    pc.print("captions : \t", style="cyan", end='')
    print("Get target's photos captions")
    pc.print("comments : \t", style="red", end='')
    print("Get allcomments on a target's posts")
    pc.print("followers : \t", style="yellow", end='')
    print("get target's followers")
    pc.print("followings : \t", style="red", end='')
    print("Get users followed by target")
    pc.print("followers emails :  \t", style="green", end='')
    print("Get email of target's followers")
    pc.print("following emails :  \t", style="yellow", end='')
    print("Get email of users followed by the target")
    pc.print("followers  phone :  \t", style="red", end='')
    print("Get phone numbers of target's followers")
    pc.print("followings phone :  \t" ,style="cyan", end='')
    print("Get phone numbers of users followed by the target")
    pc.print("tags : \t", style="yellow", end='')
    print("Get tags used by target")
    pc.print("info : \t", style="white", end='')
    print("Depreciated")
    pc.print("likes : \t", style="red", end='')
    print("Get total likes on all of the target's posts")
    pc.print("mediatype :  \t", style="green", end='')
    print("Get target's posts type (photo or video)")
    pc.print("photodes :  \t", style="cyan", end='')
    print("Get descriptions of target's photos")
    pc.print("photos  : \t", style="yellow", end='')
    print("Download target's photos in output folder")
    pc.print("profile pic :  \t", style="white", end='')
    print("Download target's profile picture")
    pc.print("stories : \t", style="cyan", end='')
    print("Download target's stories")
    pc.print("tagged  :  \t", style="red", end='')
    print("Get list of users tagged by target")
    pc.print("reset target : \t\t", style="white", end='')
    print("Set new target")
    pc.print("commenter : \t", style="red", end='')
    print("Get a list of user who commented target's photos")
    pc.print("ttag  :  \t", style="green", end='')
    print("Get a list of user who tagged target")
    print(" ")
    pc.print(" Also supports basic terminal commands : ", style='cyan')
    pc.print("ls : ", style='pink1', end='')
    pc.print("Display all commands ", ":search:", style='bright_white')
    pc.print("exit : ", style='orange_red1', end='')
    pc.print("Exit Terra", style='bright_white')
    pc.print("clear : ", style='orchid2', end='')
    pc.print("Clear screen", style='bright_white')
    pc.print('back : ', style='purple', end='')
    pc.print('Back to Main Menu', style='yellow')
    
def clear():
    # for windows screen
    if sys.platform.startswith('win'):
        os.system('cls')
    # for mac or linux          
    else:
        os.system('clear')
                
def banner():
    clear()
    banner = Figlet(font='isometric3',justify='right')
    pc.print(banner.renderText("Terra-X"),style="bold red")
    pc.print("                         OSINT TOOL ON SOCIAL MEDIA NETWORKS                                                                                              ", style="cyan1")
    print(" ")
    pc.print("                         @xadhrit (github.com/xadhrit/)                         " , style='bold red')    
    pc.print("                         Terra-x by github.com/anonfoxer2                         " , style='bold red')
    pc.print("                         @owlpilled                         " , style='bold red')  

def _out():
    pc.print("Thank you for using Terra-x!", style="yellow")
    sys.exit(0)

"""
def handle_single(sig, frame):
    pc.print("\n Sending you Out \n", style="red")
    sys.exit(0)
"""
parser = argparse.ArgumentParser(description="Recon with Terra")        
parser.add_argument('target', type=str, help='username of target')
parser.add_argument('-j', '--json', help='save results in a JSON file', action='store_true')
parser.add_argument('-f', '--file', help='save results in a Text File', action='store_true')
args = parser.parse_args()


def main():
    banner()    
    pc.print("  \n> 1 Twitter ",style="bright_yellow")
    pc.print("  \n> 2 Instagram ",style="green3")
    pc.print("  \n> 3 Exit ")
    print(" ")
    pc.print("> Choose one option : ",style='purple',end='')
    u_input = str(input())
    try:
        if u_input == '1':
            parser = argparse.ArgumentParser(description="Recon with Terra")        
            parser.add_argument('target', type=str, help='username of target')
            parser.add_argument('-j', '--json', help='save results in a JSON file', action='store_true')
            parser.add_argument('-f', '--file', help='save results in a Text File', action='store_true')
            args = parser.parse_args()
            api = Twitter(args.target,args.file,args.json)
            
                       
            commands = {
                'ls': twitter_all_commands,
                'help': twitter_all_commands,
                'quit': quit,
                'clear': clear,
                'exit': _out,
                'back': main,
                'reset target': api.reset_target,
                'tweets': api.recent_tweets,
                'favtweets': api.recent_fav,
                'followers': api.get_followers,
                'following': api.get_frnds,
                'timeline': api.user_info,
                'profile pic': api.profile_pic,
                'banner': api.banner_pic,
                'htags': api.get_hashtags,
                'mentions':api.get_mentions
            }
            while True:
                print(" ")
                pc.print("~/Terra Command >$ ", style='purple', end='')
                user_input = input()                
                cmd = commands.get(user_input)
                if cmd:
                    cmd()
                    
                elif user_input == 'FILE=y':
                    api.write_file(True)
                
                elif user_input == 'FILE=n':
                    api.write_file(False)
                    
                elif user_input == 'JSON=y':
                    api.json_dump(True)
                    
                elif user_input == 'JSON=n':
                    api.json_dump(False)
                    
                elif user_input == '':
                    print("")
                    
                else:
                    pc.print("COMMAND NOT FOUND", style="red")                  
      
        
        if u_input == '2':
            parser = argparse.ArgumentParser(description="Recon with Terra")        
            parser.add_argument('target', type=str, help='username of target')
            parser.add_argument('-j', '--json', help='save results in a JSON file', action='store_true')
            parser.add_argument('-f', '--file', help='save results in a Text File', action='store_true')
            args = parser.parse_args()
            api = Instagram(args.target,args.file,args.json)
                                                                                                                      
            commands = {
            'ls': insta_all_commands,
            'help': insta_all_commands,
            'clear': clear,
            'quit': quit,
            'exit': _out,
            'back' : main,
            'locations': api.target_locations,
            'captions': api.__getCaptions__,
            'reset target': api.change_target,
            'comments': api._all_comments,
            'followers': api._followers,
            'followings': api._followings,
            'followers emails': api.followers_email,
            'following emails': api.followings_email,
            'followers phone': api.followers_phoneNumber,
            'followings phone': api.followings_phoneNumber,
            'tags': api._hashtags,
            'timeline': api._user_timeline,
            'likes': api._total_likes,
            'mediatype': api._media_type,
            'photodes': api._photo_description,
            'photos': api._user_photo,
            'profile pic': api._user_profilepic,
            'stories': api._user_stories,
            'tagged': api._people_who_tagged_by_target,
            'commenter':  api._people_who_commented,
            'ttag': api._users_who_tagged
            }

            while True:
                pc.print("~/Terra Command >$ ", style='purple', end='')
                user_input = input()
                
                cmd = commands.get(user_input)
                if cmd:
                    cmd()        
                elif user_input == 'FILE=y':
                    api.write_file(True)
                elif user_input == 'FILE=n':
                    api.write_file(False)
                elif user_input == 'JSON=y':
                    api.json_dump(True)
                elif user_input == 'JSON=n':
                    api.json_dump(False)
                elif user_input == '':
                    print("")
                else:
                    pc.print("COMMAND NOT FOUND", style="red")
        
        if u_input == '3':
            sys.exit(0)
        
        if u_input == 'exit':
            sys.exit(0)

        if KeyboardInterrupt:
            pc.print('Invalid Option! Try Again.... ', style='bold red')
            pc.print('Do you want to choose again ? (y/n)', style='red')
            io = input()
            if io == 'y' or 'Y':
                main()
            elif io == 'n' or 'N':
                sys.exit(0)
            else:
                print('Not an option! Good Bye!')
                sys.exit(0)
        
        else:
            pc.print('Invalid Option! ',style='bright_red')
            sys.exit(0)
          
    except Exception as e:
        pc.print(e,style='orange1')        
    
if __name__ == '__main__':
    main()    
