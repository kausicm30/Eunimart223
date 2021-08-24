owner_schema = {
    'type': 'object',
    'required': ['email','password'],
    'properties':{
        'email':{'type':'string'},
        'password':{'type':'string','minLength':2, 'maxLength':10}
    }
}

add_movie_schema={
    'type': 'object',
    'required':['email','movie_name','movie_time','theatre_name'],
    'properties':{
        'email':{'type':'string'},
        'movie_name':{'type':'string'},
        'movie_time':{'type':'string'},
        'theatre_name':{'type':'string'}
    }
}

modify_movie_schema={
    'type': 'object',
    'required':['email','name','theatre','update_movie'],
    'properties':{
        'email':{'type':'string'},
        'name':{'type':'string'},
        'theatre':{'type':'string'},
        'update_movie':{'type':'string'}
    }
}

delete_movie_schema = {
    'type': 'object',
    'required':['email','name','theatre'],
    'properties':{
        'email':{'type':'string'},
        'name':{'type':'string'},
        'theatre':{'type':'string'}
    }
}

admin_schema = {'owner_schema':owner_schema,
                'add_movie_schema':add_movie_schema,
                'modify_movie_schema':modify_movie_schema,
                'delete_movie_schema':delete_movie_schema
                }