from flask import Flask, jsonify,request
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow as ma
from flask_sqlalchemy import SQLAlchemy
from models.my_models import *
from parsers.parse import qbArgs, rbArgs, dfArgs, wrArgs
import os
from datetime import datetime


# initialize the flask application 
app = Flask(__name__)

# connects the heroku database 
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# connects to the local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Will initialize the api, database, and marshmallow object with the flask app
api = Api(app)
db.init_app(app)
ma.init_app(app)



# Makes the app point to this 
# Will recreate the database
with app.app_context():
    db.create_all()

"""
Class breakdown:
These classes inherit the Resource class from the flask_restful module

The resource class lets you get access to the HTTP requests methods for you to edit
You add these resource classes to the api as a resource as known as a endpoint

"""

DEFENSE = ['Defensive End', 'Defensive Tackle', 'Linebacker', 'Cornerback','Safety']


class Player(Resource):
    def get(self,name):
        name = name.replace("-"," ").lower()
        qb = QBModels.query.filter_by(name=name).first()
        rb = RBModels.query.filter_by(name=name).first()
        wr = WRModels.query.filter_by(name=name).first()
        df = DefenseModels.query.filter_by(name=name).first()

        # Will look for the player in each model 
        # Query the stats
        # Serialize the data and send it back as json
        if qb:
            qb_stats = QBStats.query.filter_by(player_id=qb.id).all()
       
            player_schema = QBSchema()
            stats_schema = QBStatsSchema(many=True)

            player = player_schema.dump(qb)
            stats = stats_schema.dump(qb_stats)

            player['stats'] = stats

            return player
        elif rb:
            rb_stats = RBStats.query.filter_by(player_id=rb.id).all()
       
            player_schema = RBSchema()
            stats_schema = RBStatsSchema(many=True)

            player = player_schema.dump(rb)
            stats = stats_schema.dump(rb_stats)

            player['stats'] = stats

            return player
        elif wr:
            wr_stats = WRStats.query.filter_by(player_id=wr.id).all()
       
            player_schema = WRSchema()
            stats_schema = WRStatsSchema(many=True)

            player = player_schema.dump(wr)
            stats = stats_schema.dump(wr_stats)

            player['stats'] = stats

            return player
        elif df:
            df_stats = DefenseStats.query.filter_by(player_id=df.id).all()
       
            player_schema = DefenseSchema()
            stats_schema = DefenseStatsSchema(many=True)

            player = player_schema.dump(df)
            stats = stats_schema.dump(df_stats)

            player['stats'] = stats

            return player
        else:
            return jsonify(error="player not found")


    
    def put(self,name):
        args = None
        name = name.replace("-", " ").lower()

        position = request.form['position'] # Checks the position in the request to see what args we're using
        if position == 'Quarterback':
            args = qbArgs.parse_args()
        elif position == 'Running Back':
            args = rbArgs.parse_args()
        elif position == 'Wide Receiver' or position == 'Tight End':
            args = wrArgs.parse_args()
        elif position in DEFENSE:
            args = dfArgs.parse_args()
        else:
            return jsonify(message='Data has not been sent')

        # Depending on the position im going to add it to their specific position model 
        # if the player isn't in their position model then add them
        # if they are check if the stats aren't duplicates if they are not then add it to the model
        if position == 'Quarterback':
            player = QBModels.query.filter_by(name=name).first()
            if player == None:
                qb = QBModels(name=name,position=args['position'],team=args['team'],number=args['number'])
                qb_stats = QBStats(
                    year= args['year'],
                    games= args['GP'],
                    attempts=args['ATT'],
                    completions= args['CMP'],
                    completionPercent=args['CMP%'],
                    yards=args['YDS'],
                    avgYards=args['AVG'],
                    longestPass=args['LNG'],
                    tds=args['TDS'],
                    ints=args['INT'], 
                    sacks=args['SACK'],
                    fumbles=args['FUM'],
                    passerRating = args['RTG'],
                    qbr= args['QBR'],
                    player=qb
                )
                db.session.add(qb,qb_stats)
                db.session.commit()
            else:
                check_year = QBStats.query.filter_by(year=args['year'],player_id=player.id).first()
                if check_year:
                    if args["year"] == str(datetime.now().year):
                        check_year.games= args['GP']
                        check_year.attempts=args['ATT']
                        check_year.completions= args['CMP']
                        check_year.completionPercent=args['CMP%']
                        check_year.yards=args['YDS']
                        check_year.avgYards=args['AVG']
                        check_year.longestPass=args['LNG']
                        check_year.tds=args['TDS']
                        check_year.ints=args['INT'] 
                        check_year.sacks=args['SACK']
                        check_year.fumbles=args['FUM']
                        check_year.passerRating = args['RTG']
                        check_year.qbr= args['QBR']
                        db.session.commit()
                        return jsonify(message=f"{datetime.now().year} Stat Updated")

                    return jsonify(message=f"{args['year']} stat already in ")
                else:
                    qb_stats = QBStats(
                        year= args['year'],
                        games= args['GP'],
                        attempts=args['ATT'],
                        completions= args['CMP'],
                        completionPercent=args['CMP%'],
                        yards=args['YDS'],
                        avgYards=args['AVG'],
                        longestPass=args['LNG'],
                        tds=args['TDS'],
                        ints=args['INT'], 
                        sacks=args['SACK'],
                        fumbles=args['FUM'],
                        passerRating = args['RTG'],
                        qbr= args['QBR'],
                        player_id = player.id
                    )
                    db.session.add(qb_stats)
                    db.session.commit()
            return jsonify(message="Stat Added")
        elif position == 'Running Back':
            player = RBModels.query.filter_by(name=name).first()
            if player == None:
                rb = RBModels(name=name,team=args['team'],position=args['position'],number=args['number'])
                rb_stats = RBStats(
                    year=args['year'],
                    games=args['GP'],
                    attempts=args['ATT'],
                    yards=args['YDS'],
                    avgYards=args['AVG'],
                    tds=args['TDS'],
                    longestRun=args['LNG'],
                    rushing1stDowns=args['FD'],
                    fumbles=args['FUM'],
                    rushingFumbleLost=args['LST'],
                    player=rb
                )
                db.session.add(rb,rb_stats)
                db.session.commit()
            else:
                check_year = RBStats.query.filter_by(year=args['year'],player_id=player.id).first()
                if check_year:
                    if args["year"] == str(datetime.now().year):
                        check_year.games=args['GP'],
                        check_year.attempts=args['ATT'],
                        check_year.yards=args['YDS'],
                        check_year.avgYards=args['AVG'],
                        check_year.tds=args['TDS'],
                        check_year.longestRun=args['LNG'],
                        check_year.rushing1stDowns=args['FD'],
                        check_year.fumbles=args['FUM'],
                        check_year.rushingFumbleLost=args['LST'],
                        db.session.commit()
                        return jsonify(message=f"{datetime.now().year} Stat Updated")

                    return jsonify(message=f"{args['year']} stat already in ")
                else:
                    rb_stats = RBStats(
                        year=args['year'],
                        games=args['GP'],
                        attempts=args['ATT'],
                        yards=args['YDS'],
                        avgYards=args['AVG'],
                        tds=args['TDS'],
                        longestRun=args['LNG'],
                        rushing1stDowns=args['FD'],
                        fumbles=args['FUM'],
                        rushingFumbleLost=args['LST'],
                        player_id=player.id
                    )
                    db.session.add(rb_stats)
                    db.session.commit()
            return jsonify(message="Stat Added")

        elif position == 'Wide Receiver' or position == 'Tight End':
            player = WRModels.query.filter_by(name=name).first()
            if player == None:
                wr = WRModels(name=name,team=args['team'],position=args['position'],number=args['number'])
                wr_stats = WRStats(
                    year=args['year'],
                    games=args['GP'],
                    targets=args['TGTS'],
                    receptions=args['REC'],
                    yards=args['YDS'],
                    avgYards=args['AVG'],
                    tds=args['TDS'],
                    longestRec=args['LNG'],
                    receivingFirstDowns=args['FD'],
                    fumbles=args['FUM'],
                    rushingFumbleLost=args['LST'],
                    player=wr
                )
                db.session.add(wr,wr_stats)
                db.session.commit()
            else:
                check_year = WRStats.query.filter_by(year=args['year'],player_id=player.id).first()
                if check_year:
                    if args["year"] == str(datetime.now().year):
                        check_year.games=args['GP'],
                        check_year.targets=args['TGTS']
                        check_year.receptions=args['REC']
                        check_year.yards=args['YDS']
                        check_year.avgYards=args['AVG']
                        check_year.tds=args['TDS']
                        check_year.longestRec=args['LNG']
                        check_year.receivingFirstDowns=args['FD']
                        check_year.fumbles=args['FUM']
                        check_year.rushingFumbleLost=args['LST']
                        db.session.commit()
                        return jsonify(message=f"{datetime.now().year} Stat Updated")

                    return jsonify(message=f"{args['year']} stat already in ")
                else:
                    wr_stats = WRStats(
                        year=args['year'],
                        games=args['GP'],
                        targets=args['TGTS'],
                        receptions=args['REC'],
                        yards=args['YDS'],
                        avgYards=args['AVG'],
                        tds=args['TDS'],
                        longestRec=args['LNG'],
                        receivingFirstDowns=args['FD'],
                        fumbles=args['FUM'],
                        rushingFumbleLost=args['LST'],
                        player_id=player.id
                    )
                    db.session.add(wr_stats)
                    db.session.commit()
            return jsonify(message="Stat Added")
            
        else:
            player = DefenseModels.query.filter_by(name=name).first()
            if player == None:
                df = DefenseModels(name=name,team=args['team'],position=args['position'],number=args['number'])
                df_stats = DefenseStats(
                    year=args['year'],
                    games=args['GP'],
                    total=args['TOT'],
                    solo=args['SOLO'],
                    ast=args['AST'],
                    sacks=args['SACK'],
                    forcedFumbles=args['FF'],
                    fumblesRecovered=args['FR'],
                    fumbleYards=args['YDS'],
                    interceptions=args['INT'],
                    intYards=args['INT YARDS'],
                    avgYardsIntercepted=args['AVG'],
                    tds=args['TDS'],
                    longestInterception=args['LNG'],
                    passDef=args['PD'],
                    stuffs=args['STF'],
                    player=df
                )
                db.session.add(df,df_stats)
                db.session.commit()
            else:
                check_year = DefenseStats.query.filter_by(year=args['year'],player_id=player.id).first()
                if check_year:
                    if args["year"] == str(datetime.now().year):
                        check_year.games=args['GP']
                        check_year.total=args['TOT']
                        check_year.solo=args['SOLO']
                        check_year.ast=args['AST']
                        check_year.sacks=args['SACK']
                        check_year.forcedFumbles=args['FF']
                        check_year.fumblesRecovered=args['FR']
                        check_year.fumbleYards=args['YDS']
                        check_year.interceptions=args['INT']
                        check_year.intYards=args['INT YARDS']
                        check_year.avgYardsIntercepted=args['AVG']
                        check_year.tds=args['TDS']
                        check_year.longestInterception=args['LNG']
                        check_year.passDef=args['PD']
                        check_year.stuffs=args['STF']
                        db.session.commit()
                        return jsonify(message=f"{datetime.now().year} Stat Updated")

                    return jsonify(message=f"{args['year']} stat already in ")
                else:
                    df_stats = DefenseStats(
                        year=args['year'],
                        games=args['GP'],
                        total=args['TOT'],
                        solo=args['SOLO'],
                        ast=args['AST'],
                        sacks=args['SACK'],
                        forcedFumbles=args['FF'],
                        fumblesRecovered=args['FR'],
                        fumbleYards=args['YDS'],
                        interceptions=args['INT'],
                        intYards=args['INT YARDS'],
                        avgYardsIntercepted=args['AVG'],
                        tds=args['TDS'],
                        longestInterception=args['LNG'],
                        passDef=args['PD'],
                        stuffs=args['STF'],
                        player_id=player.id
                    )
                    db.session.add(df_stats)
                    db.session.commit()
            return jsonify(message="Stat Added")
        






# Add the resource inherited classes to the api as endpoints to request data from 
api.add_resource(Player,"/NFL/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
 







