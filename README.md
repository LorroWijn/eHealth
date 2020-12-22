# eHealth
 eHealth interventies webpagina

This project has been mainly built up with the use of python and the Django web framework. For more information on Django you can use this website and the tutorials on it : https://www.djangoproject.com/#:~:text=Django%20is%20a%20high%2Dlevel,It's%20free%20and%20open%20source. You can follow these tutorials for an understanding of the framework: https://docs.djangoproject.com/en/3.1/ These tutorials are highly recommended to at least read through, but preferably complete before starting to work on this project. Even we do not know if we have done everything the correct way in this project, so do not be afraid to do something different than we did.

For this application to work you need to install several programs. First you need an interpreter (like visual studios community edition, visual studio code or pycharm (we prefer visual studion code)) to actually be able to edit and run this project. Other programs and versions of these programs can be found in the requirements.txt in this project. For instance you need python, django and bootstrap and maybe more in these specific version. You also need to add python to your path, otherwise your interpreter will not be able to find it. Afterwards this code can be run by opening it with your interpreter and typing "python manage.py runserver" in your terminal and then opening the localhost link that is given to in your webbrowser. Depending on your python version you may have to use python3 instead of python. 

In this framework we have made many pages which all have a corresponding name. All these pages have files like admin.py and apps.py in them. The eHealth page is the overarching page that also holds the models of the project. The models here are also the database construction of this website. When you add models, you can migrate them as can be seen on this page: https://docs.djangoproject.com/en/3.1/topics/migrations/ After this you can enter new model instances through the built in django admin panel by placing admin after the header of the locally running application. We have not yet had the time to implement models and database version, so this may be a task the for the next group (maybe who is reading this). These models can also be used to add users with usernames and passwords for login, but it was not needed yet when we worked on it. Login functions may actually not be needed, but this must be discussed with the product owners of this project. 

If you add new pages, you have to do several things. First you need to copy a folder (like vitaliteit) and paste it on the same height in the file structure of this project with a different name. Secondly you need to add this page to the settings.py file in the VitaminB12Information folder as an installed app. Then you need to change the apps.py and views.py file in the newly pasted folder. Also the urls.py file in the eHealth folder needs to be updated with the new folder.

To access the views (actual html and looks of the page) you have to be in the templates folder of this project. In here you can find the html files of the project and how the pages look. The css is also in these template folders. You can put the css used on these pages in the css.html file in the same folder. Pay attention that the names of these templates may not have the same names, because the static in this project searches through the templates top down and uses the first file that matches this name. When adding a new template, you need to put page-specific html in a new folder and templates used in the entire project in the eHealth folder. This is done so the next group can find the new templates easily. 

For some very complicated actions (like logging in etc), you may need to add certain python code to the views.py file of every page folder. Since we started the project, we did not have the time or need to implement more than loading the pages. More information on views should be looked up through google or the django tutorials like this tutorial: https://docs.djangoproject.com/en/3.1/intro/tutorial03/

If you need to add illustrations in this project or maybe videos, you can add these in the static folder of this project. Just make sure that you make a new 'videos' folder or something like that to keep everything ordered for the next people, working on this project. 

We have incorporated MySQL in this project, but nothing is in the database yet. To use the database (which you must implement yourself first, because we did not need it (could be it still is not needed)) you must add your credentials to the database and then add a database.txt file to the project type with your credentials in it. Your username must be on the first line and your password on the second line. You can run the MySQL database with the next link: https://pypi.org/project/mysqlclient/
However as we mentioned, this is not something we had time for to research well enough, since we did not needed it yet. If another database has your preference please use this or maybe a database is not needed at all in this project. After this you must describe your database in your models. You can use the models.py file in the eHealth folder for the models of the entire project for this. In this models.py file you can state your database structure and then migrate these to your database, like is described in this Django tutorial: https://docs.djangoproject.com/en/3.1/intro/tutorial02/

Several tasks have not been completed during the time we worked on the project. These are tasks we found, but to be sure you need to check the owners of this project for more information about what still has to be done to complete this project. 
1 After this information is added it has a high priority to correctly launch this website by putting it on a stable server with a good domain name. It also needs to be ensured that the server will remain active for a long time, so this is something that needs to be researched and will probably cost the owners of the project some money. This needs to be discussed with them.
2 More functions of the website are meant to be added. These functions should be discussed with the product owners and can be found from several researches of both the students of Zorgtechnologie and AGW. These researches can also be acquired through the owners of the project. Examples of these functions are a workshop environment and reminders through e-mail or a comparable medium.
3 This website is in Dutch, but also can to be translated to English. A button should be added at the bottom or top of every page to change the language. This can be done with the translation functions of Django reachable through this link: https://docs.djangoproject.com/en/3.1/topics/i18n/translation/ Also you may need to add some javascript or views and maybe cookies to make this page work optimal.
4 The current information may need an update since it possibly has been a while since this project is touched. The last update can be seen on github, but we worked on this project until the middle of januari 2021. This should however be checked with the product owners of the website. Also the quality of the information may need an improvement. for instance that there are more illustrations and videos added instead of mainly text.
5 The website has been made responsive (can be read well on smartphones etc) with mediaqueries. However maybe this responsiveness is not well enough for a good website, so this is something that could be improved with other means. For instance more attention should be paid to if the letters on the website are large enough for every person to read. 

Finally after reading through this readme and after you are finished with the project, this readme should be updated by you to ensure that the next group working on this project knows what has to be done to finish the project.

This is everything we could explain to you at the moment. Explaining things like html and css is impossible to explain in a few lines, so you must learn this yourself. Maybe through tutorials and by googling and finding stackoverflow pages or documentation form w3schools. We wish you good luck with this project and hope you can improve it a lot to help people get better EHealth with this web application.
