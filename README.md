# Overview

This is a Django web app. It creates a calendar where you can add, delete and view dates. It isn't complete yet and still has a ton of bugs that need to be worked out.
I wrote it to help get me into Django web apps and learn how they work.

To start the test server, just type 'python manage.py runserver'
The home url is '127.0.0.1:8000/cal/June/2021' but you can do any month or year (the month needs to be capitalized (one of those bugs)).

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

There are currently 3 views:

-A view to delete dates - http://127.0.0.1:8000/cal/delete_old/June/2021
  -This view dynamically generates a list of checkboxes from the events that have been added to the calendar. You are then able to check the ones you wish to delete
  and press the delete button. You are then redirected back to the calendar view. If you wish to go back without deleting, you press cancel.

-A view to create a new date - http://127.0.0.1:8000/cal/add_new/June/2021
  - This view has a form that automatically fills in the month and year that you were viewing in the calendar view. You can change them if you need to or just fill in the
  day and content fields. Pressing the add button will add the event and redirect you back to the calendar view. If you wish to return to the calendar view without adding,
  then you can press the cancel button.

-A view to see the actual calendar - http://127.0.0.1:8000/cal/June/2021
  - This view will display the calendar dynamically. It will loop through adding the boxes while filling them with the date content. It has links at the top to transition
  to diffrent months and years. It also has the 'added new' button to add an event and a 'delete old' button to delete an existing date.

# Development Environment

* Python 3.9.5 for the language
* Django 3.2.4 for a library
* HTML (for the templates in Django)
* VS Code for the IDE

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [docs.djangoproject.com](https://docs.djangoproject.com/en/3.2/)
* [w3schools.com](www.w3schools.com)
* [www.tutorialspoint.com](https://www.tutorialspoint.com/django/django_form_processing.htm)
* [www.learningaboutelectronics.com](http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php)

# Future Work

* Handle/check user input
* Fix the calendar weekdays (the weekdays are incorrect)
* Make it editable on the calendar view for quick editing
* Add a to-do list
* Add a view for repeat events
* Work on design, layout and color.
* Add features to deleting events (sorting/filtering list the list)
* Fix the issue with deleting where if you have an event with the same name they both get deleted.
