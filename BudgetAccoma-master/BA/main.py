from ba import create_app
if __name__=='__main__':
    app=create_app()
    app.run(debug=True)


    
##forms are like class templates that you can call on
##action is where should i go when a button is clicked and then method is what needs to happen to get there
##best way to access variables from another thing is the=rough request.variables
##browser caches contain a lot of information
##if some session values aren't working, restart your browser
