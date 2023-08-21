from django.shortcuts import render

# home page view
def Home(request):
    
    # I'm getting the user os system information in the http metadata from the request.
    myosinfo =   request.META['HTTP_USER_AGENT']
    print('osinfo:',myosinfo)

    # Googling I found a list of 64bit os, I'm not sure how much is trustable
    oslist = ['x86_64','x86-64', 'Win64','x64','amd64','AMD64','WOW64', 'ia64','sparc64','ppc64','IRIX64']
    
    # I'm checkink if the user is in the oslist or not
    for myos in oslist:
        if myos in myosinfo:
            # I found you in oslist
            context={}
            return render(request,'home.html',context)

        else:
            # I didn't find you in the oslist
            msg = "Warning: It seems you are using a 32Bit OS ,the web site doesn't work propertly, your browser hasn't the necessary tools."+ "Your OS Data:" + myosinfo 
            context={'msg':msg}
            return render(request,'home.html',context)
    
    ## I will use just one line in _hyperscript in the home.html.
    ## If oslist doesn't filtering propertly, I'll be safe.
    ## if it is a modern system the msg will disappear,this is due to the _hyperscript line command.
    ## At the end we tested if HTMX can works. If _Hyperscript is working
    ## HTMX is working too.  