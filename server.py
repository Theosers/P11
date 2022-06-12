import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        flash('Sorry, that email was not found')
        return render_template('index.html')

@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        flash("Here is the form to complete")
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])

def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    
    
    time_object = datetime.now()
    comp_time = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    if time_object < comp_time:
        if (int(club['points'])) >= (places_required):
            if places_required <= 12 and places_required > 0:
                flash('Great-booking complete !' + str(places_required) + " places booked for " + str(competition['name']))
                club['points'] = int(club['points']) - places_required
                competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            else:
                flash('You can only book for 12 places or less for a competition')
        else:
            flash('Your club does not have enough points')
    else:
        flash("Sorry, this competition has already taken place ")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/rankings', methods=['GET'])

def display_points():
    return render_template('rankings.html', club=clubs)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))