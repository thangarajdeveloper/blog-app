# blog-app
Blog application

This is the blog application used for create, update, delete the blogs and add ablog comments.

copy the source file. then run the below comments in blog_proj path.

pip install Django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

after runnig the above comments. Project will be hosted in http://127.0.0.1:8000/.

below are api's to do the process.
http://127.0.0.1:8000/blogs                       - List the blogs
http://127.0.0.1:8000/blog/<blog_id>              - View the blog details
http://127.0.0.1:8000/addblog                     - add blog
http://127.0.0.1:8000/updateblog/<blog_id>        - update the blog
http://127.0.0.1:8000/deleteblog/<blog_id>        - delete the blog

below are the screenshots for page reference.

Blog lists
![image](https://user-images.githubusercontent.com/84706944/119323075-f0c00180-bc9b-11eb-8259-c057beacb031.png)

Read the full details of the blog
![image](https://user-images.githubusercontent.com/84706944/119323164-0c2b0c80-bc9c-11eb-90da-677640a84516.png)

Add the blog
![image](https://user-images.githubusercontent.com/84706944/119323226-1947fb80-bc9c-11eb-8996-e9efe774f5c5.png)

Update the blog
![image](https://user-images.githubusercontent.com/84706944/119323282-25cc5400-bc9c-11eb-96d8-f3823822ab80.png)


