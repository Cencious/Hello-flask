from flask import Flask #from flask module import Flask class.
app= Flask(__name__) #create an instance called app, by passing the varriable__name__
#__name__ variable determines the root path for app.

#defining a route
@app.route('/')#a decorator used to define routes in flask
def index():#a view function, handler for route defined above.
    return'<h1>Hello World</h1>' #a responce which the web browser/ client will receive.

    #setting up a server
    if __name__=='__main__':
        app.run(debug=True)# run launches the flask dev server. debug set to true to activate debugger and reloader during deployment.
