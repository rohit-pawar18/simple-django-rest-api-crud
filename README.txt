# Headers for all api

Content-Type = application/json


#POSt data should be in Body => raw

{
    "title": "task1",
    "description": "test update",
    "user": 1
}


# Task apis
#Crete task
API :- http://localhost:8000/api/tasks/ 
methohd :- POST
Json Body:- {
    "title": "task1",
    "description": "test update",
    "user": 1
}

# LIST app tasks
API :- http://localhost:8000/api/tasks/ 
methohd :- GET
Json Body:- Not required


#update task
API :- http://localhost:8000/api/task/<int:task_id>/
methohd :- PUT
Json Body:- {
    "title": "task1",
    "description": "test update",
    "user": 1
}

#delete task
API :- http://localhost:8000/api/task/<int:task_id>/
methohd :- DELETE
Json Body:- No required



#Comments APIs

#Create Comment
API :- http://localhost:8000/api/comment/ 
methohd :- POST
Json Body:- {
	"comment": "test1",
	"user": 1, 
	"task": 2
}

# GET Comment
API :- http://localhost:8000/api/comment/<int:comment_id>/
methohd :- GET
Json Body:- Not required


#update task
API :- http://localhost:8000/api/comment/<int:comment_id>/
methohd :- PUT
Json Body:- {
	"comment": "test1",
	"user": 1, 
	"task": 2
}

#delete task
API :- http://localhost:8000/api/comment/<int:comment_id>/
methohd :- DELETE
Json Body:- No required