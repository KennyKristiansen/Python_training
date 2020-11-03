# Python_training
Here i keep a collection of my python training exercises.
These come in the form of book exercises or small projects.

[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python version][python-image]][python-url]
[![Editor used][Pycharm-image]][pycharm-url]


![](header.png)

## Repository overview

### Book exercises

This is where i store projects and exercises that i completed as i first began learning python.
These were mostly written as part of the book "Automate The Boring Stuff With Python" by Al Sweigart.

<img src="https://automatetheboringstuff.com/images/automate_2e_cover.png" width="150" height="200"/>

_[Here][automate_the_boring_stuff-url] is a link to the Authors official website._



### First projects
Here i have saved some of my first projects, that i created without a "recipe" given to me.
A quick example of one small projects, is as follows:

#### plex_server (excel_overview_creator)
> At home i have a media server (plex server), which contains movies and series.
>
> I wanted a quick overview of the content i had, based on the following criteria:
>   1. Sharable.
>   2. Easily updatable.
>   3. Customizable.
>   4. Additional information about content.
>
> For this purpose i decided on an excel file, as the output format. This was based on the fact that it is both easily sharable and tables within it are customizable.
>
> The way the python script ended up working was as follows: 
>   1. Iterate over all files in selected folders.
>   2. Use www.omdbapi.com to collect the wanted information about each file.
>   3. Insert all data into a SQLite database, for easy updatability.
>   4. Use excels built-in PowerQuery to import data from the created SQLite database.
>
>>Here is an example of the excel output that is created.
>![excel_overview_example_picture]

During this project, i learned about the following:

* Integrating and utilizing API-requests.
* Creating and updating SQL databases.
* Aggregate data from an SQL database into Excel, using PowerQuery.

### Maersk

```
Description is underway.
```

### Fitness

```
Description is underway.
```


## Update history

* 0.2 #TODO
    * Complete descriptions of repository folders

* 0.1 First commit
    * Created README.md
    * Filling in descriptions for the repository folders

## Contact information

Kenny H. Kristiansen

Send an Email to <a href = "mailto: KennyKristiansen@hotmail.com">KennyKristiansen@hotmail.com</a>

[LinkedIn](https://www.linkedin.com/in/kenny-kristiansen/)

[GitHub](https://github.com/kennykristiansen)


<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.7-Green
[python-url]: https://www.python.org/
[pycharm-image]: https://img.shields.io/badge/Pycharm-2020.2.320-brightgreen
[pycharm-url]: https://www.jetbrains.com/pycharm/
[automate_the_boring_stuff-image]: https://automatetheboringstuff.com/images/automate_2e_cover.png
[automate_the_boring_stuff-url]: https://automatetheboringstuff.com/2e/chapter0/
[excel_overview_example_picture]: excel_overview.png
[wiki]: https://github.com/yourname/yourproject/wiki