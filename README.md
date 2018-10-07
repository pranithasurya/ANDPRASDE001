# andpraSDE001

## About

This is a python program to get top 8 Expedia's Facebook posts and save them into JSON file.

## Prerequisites
- Use Python 3.5.0 version
- Make sure the following modules are available : bs4  , urllib.request. You can install these modules using pip(linux/windows) or easyinstall(windows) 


## How to run the program:
- run the command "python expedia_fb_posts_parser.py"

The above command scrapes the expedia fb page and downloads top 8 posts into posts.json file

I have chose to save the following data points:
- message (Expedia's message about the post)
- postlink (which is a link to expedia page)
- postlink_content (text content about the postlink)
- timestamp (when was it actually posted)
- image (image of actual location)

The above data points gives a description of location and immediate redirection for user to book tickets to the location from expedia page. It also tells Expedia's short description about the post to a user.
