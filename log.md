# 100 Days Of Code - Log

I am an electronic engineer who develops software by trade. 
I wrote my first program in [GW-Basic](https://en.wikipedia.org/wiki/GW-BASIC), long time ago (during the past century!) During my long experience I have caught some bad habits I need to unlearn. I will try my 100 days of code for learning some good ones instead.

Timezone: GMT-3

## Day 0 - (20220801): Monday 1 August, 2022
One of my bad habits is developing code without tests. So, I want to learn Test Driven Development (TDD).
I have noticed the wonderful Youtube channel by ArjanCodes, where these videos appear

[How To Write Unit Tests For Existing Python Code // Part 1 of 2](https://www.youtube.com/watch?v=ULxMQ57engo)

[How To Write Unit Tests For Existing Python Code // Part 2 of 2](https://www.youtube.com/watch?v=NI5IGAim8XU)

[Test-Driven Development In Python // The power of red-green-refactor](https://www.youtube.com/watch?v=B1j6k2j2eJg)

10:00 - Today my work is: watch these videos, and write tests for some code.
22:00 - I watched the videos, learned how to write tests. However, tests don't run properly.

## Day 1 - (20220802): Tuesday 2 August, 2022

Today I managed to refactor my code. Now, tests run, succeding and failing. However, I need to include assertions and use coverage.

## Day 2 - (20220803): Wednesday 3 August, 2022

Today, I manage to get unittest and pytest test working. Tomorrow I will include some assertions.

## Day 3 - (20220804): Thursday 4 August, 2022

Today, I installed coverage and black in a local environment, and learn how to use them. Also, I read about [CI/CD](https://resources.github.com/ci-cd/) and take some notes. Tomorrow, I will try to make a github template repo, with Github Actions.

## Day 4 - (20220805): Friday 5 August, 2022

Day 004 of #100DaysOfCode Today I prepared a github template repo for my #MachineLearning projects. I will publish it Tuesday 9 August 2022.

## Day 5 - (20220806): Saturday 6 August, 2022

Day 005 of #100DaysOfCode. Today I restarted my first python project: scraping data from CIA Factbook (html +csv), 
years 2001 to 2020, generating spreadsheets as output.

## Day 6 - (20220808): Monday 8 August, 2022

Day 006 of #100DaysOfCode. This is the [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet)

## Day 7 - (20220809): Tuesday 9 August, 2022

Day 007 of #100DaysOfCode. This is the [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet)

## Day 8 - (20220810): Wednesday 10 August, 2022

Day 008 of #100DaysOfCode. I continued working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet)

I found a nice structure for python code (including tests), in this repo [Microblog](https://github.com/miguelgrinberg/microblog). Got working python imports!!!

Also, I began to write some docs, and learn some git magic.

## Day 9 - (20220811): Thursday 11 August, 2022

Day 009 of #100DaysOfCode. 

1. I worked in my first [HuggingFace space](https://huggingface.co/spaces/DWB1962/svd_codes)
2. Work in progress...

## Day 10 - (20220812): Friday 12 August, 2022

Day 010 of #100DaysOfCode. Forgot to tweet. I worked with tests for my old code, found some bugs.

## Day 11 - (20220813): Saturday 13 August, 2022

Day 011 of #100DaysOfCode. I worked in configuration with python-dotenv for my  data scraping code.

## Day 12 - (20220815): Monday 15 August, 2022

Day 012 of #100DaysOfCode. Forgot to tweet. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet). Watched the [video by ArjanCodes](https://www.youtube.com/watch?v=iCE1bDoit9Q), and got an idea for scraping data from the CIA Factbook.

## Day 13 - (20220816): Tuesday 16 August, 2022

Day 013 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet). 
Today I wrote a function to walk the directory tree with [os.walk](https://docs.python.org/3.8/library/os.html?highlight=os%20walk#os.walk), and detecting mimetypes with [mimetypes.guess_type](https://docs.python.org/3.8/library/mimetypes.html?highlight=mimetypes%20guess_type#mimetypes.guess_type)

## Day 14 - (20220815): Wednesday 17 August, 2022

Day 014 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet). Today, I wrote quick and dirt code for getting mimetypes from all the files in factbook-{2000:2021} directories.

## Day 15 - (20220816): Thursday 18 August, 2022

Day 015 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet). Forgot to update this repo, forgot to tweet. Too much work, scanning files to detect patterns in the data. 

## Day 16 - (20220817): Friday 19 August, 2022

Day 015 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet). 
Forgot to update this repo, forgot to tweet. Wrote some code, broke some tests. Refactoring the code. I found an interesting pattern: The factbooks have some html files under the fields/ subdirectory, with highly structured data. However, I will resist [the temptation](https://www.reddit.com/r/programming/comments/nlko23/summoning_cthulhu_by_parsing_html_with_regular/). I am writing some code for matching and collecting data from these files. [Original post about the evil attempts of processing html with regex](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)

## Day 17 - (20220818): Saturday 20 August, 2022
Day 015 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet).
Updating this repo, tweeting about it.

## Day 18 - (20220812): Monday 22 August, 2022
Day 016 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet).
Forgot to tweet. I am working with two (or three) days long sprints. 

## Day 19 - (20220823): Tuesday 23 August, 2022
Day 017 of #100DaysOfCode. Working in [github repo for scraping data from CIA Factbook](https://github.com/DanielBerns/CIA_Factbook_to_spreadsheet).
Today, I got the data from factbook-2000. I think that with low effort, I can get the data from factbook-2001

However, factbook-2002 to factbook-2017 are hard stuff. 

factbook-2018 to factbook-2020 are the easiest ones, due to semantic html.

## Day 20 - (20220915): Saturday 17 September, 2022
Day 018 of #100DaysOfCode. Working again after a long time off.

## Day 21 - (20230414): Friday 14 April, 2023
Day 019 of #100DaysOfCode.
