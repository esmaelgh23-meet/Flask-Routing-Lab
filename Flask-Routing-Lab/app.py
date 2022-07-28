from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below


app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    # Greet the user
    return f'Hello {username} !'

# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to Ebay"
    
@app.route("/")
def index():
    return render_template ("home.html")

if __name__ == "__main__":
    app.run(debug=True)


    img = img.rotate(180) 
    img.save("adidas_ball134.jpg")

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)


print('which one is yout favorite:')
x = input()

if (x=adidas)
    print ( "great choice, we are happy you love it!")

elif (x=adidas1) 
    print ("great choice, we are happy you love this adidas:)") 

elif (x=nike) 
    print ("great nike shoes, Thank you!")
else (x=puma)
    print("puma is a brand again")

#dynamic images_1
###########################################################################################
import Image,ImageDraw
import cStringIO
import cgi

X,Y = 500, 275 #image width and height

def graph(filename):
    img = Image.new("RGB", (X,Y), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    #draw some axes and markers
    for i in range(X/10):
        draw.line((i*10+30, Y-15, i*10+30, 20), fill="#DDD")
        if i % 5 == 0:
            draw.text((i*10+15, Y-15), `i*10`, fill="#000")
    for j in range(1,Y/10-2):
        draw.text((0,Y-15-j*10), `j*10`, fill="#000")
    draw.line((20,Y-19,X,Y-19), fill="#000")
    draw.line((19,20,19,Y-18), fill="#000")

    #read in file and graph it
    log = file(r"c:\python\random_img\%s" % filename)
    for (i, value) in enumerate(log):
        value = int(value.strip())
        draw.line((i+20,Y-20,i+20,Y-20-value), fill="#55d")

    #write to file object
    f = cStringIO.StringIO()
    img.save(f, "PNG")
    f.seek(0)

    #output to browser
    print "Content-type: image/png\n"
    print f.read()

if __name__ == "__main__":
    form = cgi.FieldStorage()
    if "filename" in form:
        graph(form["filename"].value)
    else:
        print "Content-type: text/html\n"
        print """<html><body>No input file given</body></html>"""

dynamic images_2
###########################################################################################


def randgradient():
    img = Image.new("RGB", (300,300), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    r,g,b = rint(0,255), rint(0,255), rint(0,255)
    dr = (rint(0,255) - r)/300.
    dg = (rint(0,255) - g)/300.
    db = (rint(0,255) - b)/300.
    for i in range(300):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,300), fill=(int(r),int(g),int(b)))

    img.save("out.png", "PNG")

if __name__ == "__main__":
    randgradient()





# Your code should be above











