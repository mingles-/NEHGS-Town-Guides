from collections import OrderedDict
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/vt')
def vt():
    dictionary = []
    alphabet = []

    with open("static/VT - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:
            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1]).decode(encoding='UTF-8', errors='strict')
            if "Founded In:" in val:
                date = stripdate(val)
            if "Onsite Archive:" in val:
                onsiteArchive = stripcolonON(val)

            if "County:" in val:
                county = stripcolon(val)
            if "Parent Towns(s):" in val:
                parentTown = stripcolon(val).decode(encoding='UTF-8', errors='strict')
            if "Probate District:" in val:
                probateDistrict = stripcolon(val)
            if "Other Names:" in val:
                otherNames = stripcolon(val).decode(encoding='UTF-8', errors='strict')
            if "Related Databases:" in val:
                j = i+1
                while "</td>" not in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name,
                    'date': date,
                    'onsiteArchive': onsiteArchive,
                    'county': county,
                    'parentTown': parentTown,
                    'probateDistrict': probateDistrict,
                    'otherNames': otherNames,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary

    return render_template('vt.html', dictionary=dictionary, alphabet=alphabet)


@app.route('/ri')
def ri():
    dictionary = []
    alphabet = []

    with open("static/RI - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:

            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1])
            if "Founded In:" in val:
                date = stripdate(val)
            if "Town Hall:" in val:
                townHall = stripcolon(val)
            if "County:" in val:
                county = stripcolon(val)
            if "Parent Towns(s):" in val:
                parentTown = stripcolon(val)
            if "Other Names:" in val:
                otherNames = stripcolon(val).decode(encoding='UTF-8', errors='strict')
            if "Related Databases:" in val:
                j = i+1
                while not "</td>" in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name,
                    'date': date,
                    'townHall': townHall,
                    'county': county,
                    'parentTown': parentTown,
                    'otherNames': otherNames,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary

    return render_template('ri.html', dictionary=dictionary, alphabet=alphabet)


@app.route('/nh')
def nh():
    dictionary = []
    alphabet = []

    with open("static/NH - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:

            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1]).decode(encoding='UTF-8', errors='strict')
            if "Established:" in val:
                date = stripdate(val)

            if "Named:" in val:
                date = stripdate(val)

            if "County:" in val:
                county = stripcolon(val)

            if "Other Names:" in val:
                otherNames = stripcolon(val)

            if "Parent Towns(s):" in val:
                parentTown = stripcolon(val).decode(encoding='UTF-8', errors='strict')

            if "Related Databases:" in val:
                j = i+1

                while "</td>" not in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name.strip(),
                    'date': date,
                    'county': county,
                    'otherNames': otherNames,
                    'parentTown': parentTown,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary

    return render_template('nh.html', dictionary=dictionary, alphabet=alphabet)

@app.route('/ma')
def ma():
    dictionary = []
    alphabet = []

    with open("static/MA - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:

            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1]).decode(encoding='UTF-8', errors='strict')
            if "Founded In:" in val:
                date = stripdate(val)

            if "County:" in val:
                county = stripcolon(val)

            if "Detailed Information:" in val:
                detInfo = stripcolon(val)
                if ("town profile") in detInfo:
                    detInfo = "<a href=/search/database-search?location="\
                              + name.replace(" ", "%20")+"&database=Massachusetts%3A%20Historical%20Data%20" \
                              "Relating%20to%20Cities%20and%20Towns&>Town Profile</a>"

            if "Other Names:" in val:
                otherNames = stripcolon(val)

            if "Parent Towns(s):" in val:
                parentTown = stripcolon(val).decode(encoding='UTF-8', errors='strict')

            if "Related Databases:" in val:
                j = i+1
                while not "</td>" in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name.strip(),
                    'date': date,
                    'county': county,
                    'detInfo': detInfo,
                    'otherNames': otherNames,
                    'parentTown': parentTown,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary

    return render_template('ma.html', dictionary=dictionary, alphabet=alphabet)

@app.route('/me')
def me():
    dictionary = []
    alphabet = []

    with open("static/ME - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:

            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1])

            if "Year Organized:" in val:
                date = stripdate(val)

            if "County:" in val:
                county = stripcolon(val)

            if "Pre-1892 State Registry:" in val:
                registry = stripcolonON(val)[1:]

            if "Other Names:" in val:
                otherNames = stripcolon(val)

            if "Origins:" in val:
                origins = stripcolon(val)

            if "Related Databases:" in val:
                j = i+1
                while not "</td>" in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name,
                    'date': date,
                    'county': county,
                    'registry': registry,
                    'otherNames': otherNames,
                    'origins': origins,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary
    return render_template('me.html', dictionary=dictionary, alphabet=alphabet)


@app.route('/ct')
def ct():
    dictionary = []
    alphabet = []

    with open("static/CT - Tables.html") as openfile:

        thefile = list(enumerate(openfile))
        for i, val in thefile:

            dbList = []

            if "<h2>" in val:
                if "<a name=" in thefile[i+1][1]:
                    dbLetter = str(thefile[i+1][1]).split(chr(34))[1]
                else:
                    name = striptitle(thefile[i+1][1])

            if "Founded In:" in val:
                date = stripdate(val)

            if "County:" in val:
                county = stripcolon(val)

            if "Parent Towns(s):" in val:
                parentTown = stripcolon(val)

            if "Other Names:" in val:
                otherNames = stripcolon(val)

            if "Related Databases:" in val:
                j = i+1
                while not "</td>" in val:
                    val = thefile[j][1]
                    stripHTML(val, dbList)
                    j += 1

                dictionary.append({
                    'dbLetter': dbLetter,
                    'name': name,
                    'date': date,
                    'county': county,
                    'parentTown': parentTown,
                    'otherNames': otherNames,
                    'relatedDB': dbList,
                    })

    for d in dictionary:
        alphabet.append(d['dbLetter'])

    alphabet = list(OrderedDict.fromkeys(alphabet))
    print dictionary
    return render_template('ct.html', dictionary=dictionary, alphabet=alphabet)


def stripHTML(val, dbList):
    if "<a " in val:
        val = val.split("\n")[0]
        dbList.append(str(val).decode(encoding='UTF-8',errors='strict').replace("&nbsp;", ""))


# strips old html from entry with colon and a date
def stripdate(thestring):
    newstring = str(thestring).split(":")[1]
    if newstring.split("&nbsp;&nbsp;")[1][0] == "1":
        newstring = newstring.split("&nbsp;&nbsp;")[1][0:4]
    else:
        newstring = " "
    return newstring


# strips old html from entry with colon and a date
def stripcolon(thestring):
    newstring = str(thestring).split(":")[1]
    newstring = newstring.split("&nbsp;&nbsp;")[1]
    if newstring[0] == "\n":
        newstring = " "
    else:
         newstring = newstring.split("\n")[0]
    return newstring


def stripcolonON(thestring):
    newstring = str(thestring).split(":")[1]
    if newstring[0] == "\n":
        newstring = " "
    else:
         newstring = newstring.split("\n")[0]

    return newstring


# strips old html from title
def striptitle(thestring):
    newstring = thestring
    if newstring[0] == "\n":
        newstring = " "
    else:
         newstring = newstring.split("\n")[0]
    return newstring


def strip_census(theString):
    if theString[0] == "\n":
        theString = " "
    else:
        theString = theString.split("\n")[0]
    return theString

if __name__ == '__main__':
    app.run()
