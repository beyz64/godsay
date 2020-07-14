#!/usr/bin/env python3

from sys import argv

columns = 18
space_len = 30

god = r"""
          
{}
                                   //                        
          /\        _/\           //                           
         |  \      /   |         //                            
         |   | __ /   |         //                             
         |    |  |   |         //                                
          |..------..|        //                               
        .-~ /\    \\ ~-.     //                                     
       / ~~~  ~~~~~ ~~~ \                                     
      | *  |     | *  | ||                                    
      |--'/       \ -'.' |                                    
       \~    |_|   ~~~~~/                                     
    .--_~-.._      __.-~                                      
    `-._~~~  ~~~~~~  |\                                       
        ~~~~|______| | |                                      
          / |______| |  \                                     
       \-~ /|      | |\  ~-/                                  
        ~-._|______`-'_.--~                                   
            |  |   |~~                                        
            |__|___|                                          
            |_|| _||                            
            `--'`--'          
"""


# god = r"""


# {}
#                                   //
#                                  //
#                ..------..       //
#             .-~          ~-.      
#         ._ /_______/\_______\ _.
#         \ | | |* |    | *| | | /
#          \|\_\  /  _   \  /_/|/ 
#            \ ~~~  | |   ~~~ /   
#             ~-.._      _..-~    
#               .- ~~~~~~ -.      
#              / .|______|. \     
#             | (.|______|.) |    
#              \._)      (_./     
#                 |______|        
#                 |  |   |        
#                 |__|___|        
#                 |_|| _||
# """


# god = r"""                            

# {}
#                                       //
#                                      //
#                                     //                                                          
#                       ..------..                          
#                /~~-.-~__-'`-__  ~-.  .-~-.                
#               |   /~~~\     / ~~---\|     |               
#               |  ||| * |   | | |  * |     |               
#               /_-|\ \ /     \ \ \__.|\.  |                
#               ~   \~~   |_|   ~~~~ /   ~-.\               
#                    ~-.._      _.-~~                       
#                      .--~~~~~~--.                         
#                     |  |______|  |                        
#                      ~-|______|-~                         
#                        |      |                           
#                        |______|                           
#                        |  |   |                           
#                        |__|___|                           
#                        |_|| _||                 
#                        `--'`--'                           
                                                          



# """


def multiline_converter(string):
    lines = []
    line_len = 0
    line = ""
    string_splitted = str(string).split()
    for index, word in enumerate(string_splitted):
        line += word + " "
        line_len += len(word + " ")
        if(line_len >= columns - 5):
            lines.append(line)
            line = ""
            line_len = 0
        else:
            if index == len(string_splitted) - 1:
                lines.append(line)
    return lines


def beautify(string):
    beautified_string = str()
    if(len(string) > columns):
        beautified_string += " " * space_len + "*" * (columns + 5) + "*\n"
        string = multiline_converter(string)
        for line in string:
            beautified_string += " " * space_len + "*" + (int((columns - len(line) + 6) / 2) * " ") + line + \
                (int((columns - len(line) + 3) / 2) * " ") + "*\n"
        beautified_string += " " * space_len + "*" * (columns + 5) + "*"
    else:
        beautified_string += " " * space_len + "*" * (len(string) + 5) + "*\n"
        beautified_string += " " * space_len + "* " + " "+ string + "  " + "*\n"
        beautified_string += " " * space_len + "*" * (len(string) + 5) + "*"
    return beautified_string


if __name__ == "__main__":
    verse = "insufficient data for meaningful answer."
    if(len(argv) > 1):
        print(god.format(beautify(argv[1])))
    else:
        print(god.format(beautify(verse)))
